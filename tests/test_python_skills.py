from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(relative_path: str, module_name: str):
    path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"无法加载模块: {relative_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


class PythonSkillsTestCase(unittest.TestCase):
    def test_ab_test_sample_size(self) -> None:
        module = load_module(
            "skills/growth-cro/ab-test-sample-size/main.py",
            "ab_test_sample_size_main",
        )
        result = module.proportion_sample_size_per_group(0.1, 0.02, 0.05, 0.8)
        self.assertGreater(result, 1000)

    def test_keyword_cluster_builder(self) -> None:
        module = load_module(
            "skills/seo-geo-aeo/keyword-cluster-builder/main.py",
            "keyword_cluster_builder_main",
        )
        clusters = module.build_clusters(
            [
                "私域运营",
                "私域用户召回",
                "会员体系搭建",
                "会员积分体系",
            ],
            min_similarity=0.2,
        )
        self.assertEqual(len(clusters), 2)
        self.assertGreaterEqual(clusters[0]["size"], 2)

    def test_channel_budget_allocator(self) -> None:
        module = load_module(
            "skills/paid-media/channel-budget-allocator/main.py",
            "channel_budget_allocator_main",
        )
        result = module.allocate_budget(
            500000,
            "leads",
            [
                module.Channel("搜索", 3.2, 120, 0.7, 0.9),
                module.Channel("信息流", 2.4, 95, 0.9, 0.6),
                module.Channel("短视频", 2.8, 105, 1.0, 0.7),
            ],
        )
        balanced = result["strategies"]["balanced"]["allocations"]
        total_budget = sum(item["budget"] for item in balanced)
        self.assertAlmostEqual(total_budget, 500000, places=2)

    def test_campaign_retrospective_writer(self) -> None:
        module = load_module(
            "skills/analytics-attribution/campaign-retrospective-writer/main.py",
            "campaign_retrospective_writer_main",
        )
        result = module.build_retrospective(
            {
                "campaign_name": "新品首发",
                "goal_metrics": [
                    {"name": "有效线索", "target": 500, "actual": 540},
                    {"name": "成交数", "target": 50, "actual": 42},
                ],
                "channel_performance": [
                    {"name": "搜索", "spend": 60000, "leads": 200, "conversions": 18},
                    {"name": "短视频", "spend": 90000, "leads": 260, "conversions": 14},
                ],
                "wins": ["搜索渠道带来高质量线索。"],
                "issues": ["短视频素材疲劳较快。"],
                "notes": ["下次提前准备更多创意版本"],
            }
        )
        self.assertEqual(result["campaign_name"], "新品首发")
        self.assertGreaterEqual(len(result["highlights"]), 1)
        self.assertGreaterEqual(len(result["action_items"]), 1)


if __name__ == "__main__":
    unittest.main()
