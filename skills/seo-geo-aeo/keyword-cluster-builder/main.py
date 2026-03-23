from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path


TOKEN_RE = re.compile(r"[a-z0-9]+", re.IGNORECASE)
CJK_RE = re.compile(r"[\u4e00-\u9fff]")


@dataclass(frozen=True)
class ClusterKeyword:
    raw: str
    normalized: str
    tokens: frozenset[str]


def normalize_keyword(keyword: str) -> str:
    return re.sub(r"\s+", " ", keyword.strip().lower())


def extract_tokens(text: str) -> frozenset[str]:
    normalized = normalize_keyword(text)
    latin_tokens = TOKEN_RE.findall(normalized)
    cjk_chars = CJK_RE.findall(normalized)
    cjk_bigrams = ["".join(cjk_chars[i : i + 2]) for i in range(len(cjk_chars) - 1)]
    phrase = normalized.replace(" ", "")
    features = set(latin_tokens)
    features.update(cjk_chars)
    features.update(cjk_bigrams)
    if phrase:
        features.add(phrase)
    return frozenset(features)


def similarity(left: ClusterKeyword, right: ClusterKeyword) -> float:
    if left.normalized == right.normalized:
        return 1.0
    if left.normalized in right.normalized or right.normalized in left.normalized:
        return 0.78
    overlap = left.tokens & right.tokens
    union = left.tokens | right.tokens
    if not union:
        return 0.0
    jaccard = len(overlap) / len(union)
    containment = len(overlap) / min(len(left.tokens), len(right.tokens))
    score = max(jaccard, containment * 0.85)
    if left.raw[:2] == right.raw[:2]:
        score += 0.08
    if overlap and len(overlap) >= 2:
        score += 0.12
    return min(score, 1.0)


def choose_label(cluster: list[ClusterKeyword]) -> str:
    if len(cluster) == 1:
        return cluster[0].raw
    centrality_scores: list[tuple[float, ClusterKeyword]] = []
    for candidate in cluster:
        score = sum(similarity(candidate, other) for other in cluster if other != candidate)
        centrality_scores.append((score, candidate))
    centrality_scores.sort(key=lambda item: (-item[0], len(item[1].raw), item[1].raw))
    return centrality_scores[0][1].raw


def load_keywords(keywords: list[str], keywords_file: str | None) -> list[str]:
    values = [item.strip() for item in keywords if item.strip()]
    if keywords_file:
        content = Path(keywords_file).read_text(encoding="utf-8").strip()
        if not content:
            return values
        if content.startswith("["):
            parsed = json.loads(content)
            values.extend(str(item).strip() for item in parsed if str(item).strip())
        else:
            values.extend(line.strip() for line in content.splitlines() if line.strip())
    deduped: list[str] = []
    seen: set[str] = set()
    for keyword in values:
        normalized = normalize_keyword(keyword)
        if normalized and normalized not in seen:
            seen.add(normalized)
            deduped.append(keyword)
    if not deduped:
        raise ValueError("至少需要提供一个关键词")
    return deduped


def build_clusters(keywords: list[str], min_similarity: float = 0.35) -> list[dict[str, object]]:
    if not 0 < min_similarity <= 1:
        raise ValueError("min_similarity 必须在 (0, 1] 区间")

    nodes = [
        ClusterKeyword(raw=keyword, normalized=normalize_keyword(keyword), tokens=extract_tokens(keyword))
        for keyword in keywords
    ]
    parent = list(range(len(nodes)))

    def find(index: int) -> int:
        while parent[index] != index:
            parent[index] = parent[parent[index]]
            index = parent[index]
        return index

    def union(left: int, right: int) -> None:
        left_root = find(left)
        right_root = find(right)
        if left_root != right_root:
            parent[right_root] = left_root

    for left in range(len(nodes)):
        for right in range(left + 1, len(nodes)):
            if similarity(nodes[left], nodes[right]) >= min_similarity:
                union(left, right)

    grouped: dict[int, list[ClusterKeyword]] = {}
    for index, node in enumerate(nodes):
        grouped.setdefault(find(index), []).append(node)

    clusters: list[dict[str, object]] = []
    ordered_clusters = sorted(grouped.values(), key=lambda group: (-len(group), choose_label(group)))
    for idx, cluster in enumerate(ordered_clusters, start=1):
        label = choose_label(cluster)
        clusters.append(
            {
                "cluster_id": f"cluster_{idx}",
                "label": label,
                "keywords": [item.raw for item in sorted(cluster, key=lambda item: (len(item.raw), item.raw))],
                "size": len(cluster),
                "priority": "high" if len(cluster) >= 3 else "medium" if len(cluster) == 2 else "low",
            }
        )
    return clusters


def main() -> None:
    parser = argparse.ArgumentParser(description="关键词聚类工具")
    parser.add_argument("--business-domain", required=True)
    parser.add_argument("--locale", required=True)
    parser.add_argument("--keyword", action="append", default=[])
    parser.add_argument("--keywords-file")
    parser.add_argument("--min-similarity", type=float, default=0.35)
    args = parser.parse_args()

    keywords = load_keywords(args.keyword, args.keywords_file)
    result = {
        "business_domain": args.business_domain,
        "locale": args.locale,
        "keyword_count": len(keywords),
        "clusters": build_clusters(keywords, min_similarity=args.min_similarity),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
