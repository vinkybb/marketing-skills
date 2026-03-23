from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Channel:
    name: str
    roi: float
    cpa: float
    capacity: float
    stability: float


def normalize(values: list[float], reverse: bool = False) -> list[float]:
    if not values:
        return []
    minimum = min(values)
    maximum = max(values)
    if minimum == maximum:
        normalized = [1.0 for _ in values]
    else:
        normalized = [(value - minimum) / (maximum - minimum) for value in values]
    if reverse:
        return [1 - value for value in normalized]
    return normalized


def load_channels(path: str) -> list[Channel]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    channels = [
        Channel(
            name=str(item["name"]),
            roi=float(item["roi"]),
            cpa=float(item["cpa"]),
            capacity=float(item["capacity"]),
            stability=float(item["stability"]),
        )
        for item in payload
    ]
    if not channels:
        raise ValueError("channels-file 至少需要包含一个渠道")
    return channels


def distribute_budget(total_budget: float, shares: list[float]) -> list[float]:
    raw_values = [total_budget * share for share in shares]
    rounded = [round(value, 2) for value in raw_values]
    diff = round(total_budget - sum(rounded), 2)
    if rounded:
        rounded[0] = round(rounded[0] + diff, 2)
    return rounded


def score_channels(channels: list[Channel], strategy: str) -> dict[str, object]:
    roi_scores = normalize([item.roi for item in channels])
    cpa_scores = normalize([item.cpa for item in channels], reverse=True)
    capacity_scores = normalize([item.capacity for item in channels])
    stability_scores = normalize([item.stability for item in channels])
    efficiency_scores = [(roi * 0.6) + (cpa * 0.4) for roi, cpa in zip(roi_scores, cpa_scores)]

    strategies = {
        "conservative": {"efficiency": 0.35, "stability": 0.45, "scale": 0.20, "test": 0.10},
        "balanced": {"efficiency": 0.40, "stability": 0.30, "scale": 0.30, "test": 0.15},
        "aggressive": {"efficiency": 0.35, "stability": 0.15, "scale": 0.50, "test": 0.25},
    }
    if strategy not in strategies:
        raise ValueError(f"未知策略: {strategy}")

    weights = strategies[strategy]
    weighted_scores = [
        (efficiency * weights["efficiency"])
        + (stability * weights["stability"])
        + (capacity * weights["scale"])
        for efficiency, stability, capacity in zip(efficiency_scores, stability_scores, capacity_scores)
    ]
    total_score = sum(weighted_scores) or 1.0
    core_budget = 1 - weights["test"]
    core_shares = [(score / total_score) * core_budget for score in weighted_scores]
    test_pool = weights["test"]
    test_total = sum(capacity_scores) or len(capacity_scores) or 1.0
    test_shares = [(score / test_total) * test_pool for score in capacity_scores]
    final_shares = [core + test for core, test in zip(core_shares, test_shares)]
    share_total = sum(final_shares) or 1.0
    final_shares = [share / share_total for share in final_shares]

    reasons = {
        "conservative": "偏向稳定性更高的渠道，测试预算较低。",
        "balanced": "在效率、稳定性和扩量之间做均衡分配。",
        "aggressive": "提高扩量潜力和测试预算，接受更高波动。",
    }
    return {
        "strategy": strategy,
        "test_budget_ratio": weights["test"],
        "reason": reasons[strategy],
        "scores": weighted_scores,
        "shares": final_shares,
    }


def allocate_budget(total_budget: float, goal: str, channels: list[Channel]) -> dict[str, object]:
    if total_budget <= 0:
        raise ValueError("total_budget 必须大于 0")

    strategies: dict[str, object] = {}
    for strategy in ("conservative", "balanced", "aggressive"):
        result = score_channels(channels, strategy)
        shares = result["shares"]
        allocations = distribute_budget(total_budget, shares)
        strategies[strategy] = {
            "goal": goal,
            "test_budget_ratio": result["test_budget_ratio"],
            "reason": result["reason"],
            "allocations": [
                {
                    "channel": channel.name,
                    "budget": budget,
                    "share": round(share, 4),
                    "score": round(score, 4),
                }
                for channel, budget, share, score in zip(channels, allocations, shares, result["scores"])
            ],
        }

    return {
        "total_budget": total_budget,
        "goal": goal,
        "channel_count": len(channels),
        "strategies": strategies,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="渠道预算分配工具")
    parser.add_argument("--total-budget", type=float, required=True)
    parser.add_argument("--goal", required=True)
    parser.add_argument("--channels-file", required=True)
    args = parser.parse_args()

    channels = load_channels(args.channels_file)
    result = allocate_budget(args.total_budget, args.goal, channels)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

