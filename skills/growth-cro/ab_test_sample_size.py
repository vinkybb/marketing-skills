from __future__ import annotations

import argparse
import json
import math
from statistics import NormalDist


def proportion_sample_size_per_group(
    baseline_rate: float,
    min_detectable_effect: float,
    alpha: float = 0.05,
    power: float = 0.8,
) -> int:
    if not 0 < baseline_rate < 1:
        raise ValueError("baseline_rate 必须在 (0, 1) 区间")
    if not 0 < min_detectable_effect < 1:
        raise ValueError("min_detectable_effect 必须在 (0, 1) 区间")
    if baseline_rate + min_detectable_effect >= 1:
        raise ValueError("baseline_rate + min_detectable_effect 必须小于 1")
    if not 0 < alpha < 1:
        raise ValueError("alpha 必须在 (0, 1) 区间")
    if not 0 < power < 1:
        raise ValueError("power 必须在 (0, 1) 区间")

    p1 = baseline_rate
    p2 = baseline_rate + min_detectable_effect
    p_bar = (p1 + p2) / 2
    z_alpha = NormalDist().inv_cdf(1 - alpha / 2)
    z_beta = NormalDist().inv_cdf(power)
    numerator = z_alpha * math.sqrt(2 * p_bar * (1 - p_bar)) + z_beta * math.sqrt(
        p1 * (1 - p1) + p2 * (1 - p2)
    )
    n = (numerator**2) / ((p2 - p1) ** 2)
    return math.ceil(n)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline-rate", type=float, required=True)
    parser.add_argument("--mde", type=float, required=True)
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--power", type=float, default=0.8)
    args = parser.parse_args()

    sample_size = proportion_sample_size_per_group(
        baseline_rate=args.baseline_rate,
        min_detectable_effect=args.mde,
        alpha=args.alpha,
        power=args.power,
    )
    total = sample_size * 2
    result = {
        "per_group_sample_size": sample_size,
        "total_sample_size": total,
        "baseline_rate": args.baseline_rate,
        "mde": args.mde,
        "alpha": args.alpha,
        "power": args.power,
    }
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
