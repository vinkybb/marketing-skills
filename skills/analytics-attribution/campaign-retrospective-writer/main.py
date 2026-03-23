from __future__ import annotations

import argparse
import json
from pathlib import Path


def ratio(actual: float, target: float) -> float:
    if target <= 0:
        return 0.0
    return actual / target


def build_retrospective(payload: dict[str, object]) -> dict[str, object]:
    campaign_name = str(payload["campaign_name"])
    goal_metrics = payload.get("goal_metrics", [])
    channel_performance = payload.get("channel_performance", [])
    wins = [str(item) for item in payload.get("wins", [])]
    issues = [str(item) for item in payload.get("issues", [])]
    notes = [str(item) for item in payload.get("notes", [])]

    metric_reviews: list[dict[str, object]] = []
    highlights: list[str] = []
    problems: list[str] = list(issues)
    action_items: list[str] = []

    for metric in goal_metrics:
        name = str(metric["name"])
        target = float(metric["target"])
        actual = float(metric["actual"])
        achievement = ratio(actual, target)
        metric_reviews.append(
            {
                "name": name,
                "target": target,
                "actual": actual,
                "achievement_rate": round(achievement, 4),
            }
        )
        if achievement >= 1.0:
            highlights.append(f"{name} 达成率 {achievement:.0%}，高于目标。")
        else:
            problems.append(f"{name} 达成率 {achievement:.0%}，低于目标。")
            action_items.append(f"针对 {name} 复盘转化链路并补充下轮修正动作。")

    scored_channels: list[dict[str, object]] = []
    for channel in channel_performance:
        name = str(channel["name"])
        spend = float(channel.get("spend", 0))
        leads = float(channel.get("leads", 0))
        conversions = float(channel.get("conversions", 0))
        cpl = round(spend / leads, 2) if leads > 0 else None
        cpa = round(spend / conversions, 2) if conversions > 0 else None
        scored_channels.append(
            {
                "name": name,
                "spend": spend,
                "leads": leads,
                "conversions": conversions,
                "cpl": cpl,
                "cpa": cpa,
            }
        )

    if scored_channels:
        best_channel = min(
            (item for item in scored_channels if item["cpa"] is not None),
            key=lambda item: item["cpa"],
            default=None,
        )
        worst_channel = max(
            (item for item in scored_channels if item["cpa"] is not None),
            key=lambda item: item["cpa"],
            default=None,
        )
        if best_channel:
            highlights.append(
                f"{best_channel['name']} 的 CPA 最优，为 {best_channel['cpa']}。"
            )
        if worst_channel:
            problems.append(
                f"{worst_channel['name']} 的 CPA 偏高，为 {worst_channel['cpa']}。"
            )
            action_items.append(
                f"下轮降低 {worst_channel['name']} 的低效投放并重新验证素材与定向。"
            )

    highlights.extend(wins)
    if notes:
        action_items.append(f"将团队补充说明纳入下轮计划：{'；'.join(notes)}。")

    deduped_highlights = list(dict.fromkeys(highlights))
    deduped_problems = list(dict.fromkeys(problems))
    deduped_actions = list(dict.fromkeys(action_items))

    return {
        "campaign_name": campaign_name,
        "summary": {
            "goal_count": len(goal_metrics),
            "highlight_count": len(deduped_highlights),
            "issue_count": len(deduped_problems),
        },
        "metric_reviews": metric_reviews,
        "highlights": deduped_highlights,
        "issues": deduped_problems,
        "action_items": deduped_actions,
        "channel_reviews": scored_channels,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="活动复盘自动摘要")
    parser.add_argument("--input-file", required=True)
    args = parser.parse_args()

    payload = json.loads(Path(args.input_file).read_text(encoding="utf-8"))
    result = build_retrospective(payload)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

