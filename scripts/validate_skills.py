from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"

EXPECTED_SKILLS = {
    "skills/market-research/market-landscape-scan/SKILL.md",
    "skills/market-research/competitor-gap-analysis/SKILL.md",
    "skills/market-research/user-voice-mining/SKILL.md",
    "skills/stp-brand/icp-builder/SKILL.md",
    "skills/stp-brand/persona-generator/SKILL.md",
    "skills/stp-brand/positioning-statement-crafter/SKILL.md",
    "skills/content/content-strategy-planner/SKILL.md",
    "skills/content/editorial-calendar-generator/SKILL.md",
    "skills/content/multi-channel-rewriter/SKILL.md",
    "skills/seo-geo-aeo/keyword-cluster-builder/SKILL.md",
    "skills/seo-geo-aeo/serp-intent-analyzer/SKILL.md",
    "skills/seo-geo-aeo/page-seo-optimizer/SKILL.md",
    "skills/seo-geo-aeo/answer-engine-optimizer/SKILL.md",
    "skills/paid-media/channel-budget-allocator/SKILL.md",
    "skills/paid-media/ad-angle-generator/SKILL.md",
    "skills/paid-media/ad-copy-variant-generator/SKILL.md",
    "skills/growth-cro/funnel-diagnostics/SKILL.md",
    "skills/growth-cro/experiment-designer/SKILL.md",
    "skills/growth-cro/ab-test-sample-size/SKILL.md",
    "skills/crm-private-domain/lifecycle-segmentation/SKILL.md",
    "skills/crm-private-domain/winback-automation-planner/SKILL.md",
    "skills/analytics-attribution/marketing-kpi-framework/SKILL.md",
    "skills/analytics-attribution/campaign-retrospective-writer/SKILL.md",
}

REQUIRED_SECTIONS = [
    "## 类型",
    "## 说明",
    "## 适用场景",
    "## 输入",
    "## 输出",
    "## 执行流程",
    "## 示例",
]

PYTHON_SKILLS = {
    "skills/seo-geo-aeo/keyword-cluster-builder": ["main.py", "examples/keywords.txt"],
    "skills/paid-media/channel-budget-allocator": ["main.py", "examples/channels.json"],
    "skills/growth-cro/ab-test-sample-size": ["main.py"],
    "skills/analytics-attribution/campaign-retrospective-writer": [
        "main.py",
        "examples/input.json",
    ],
}


def main() -> None:
    errors: list[str] = []
    discovered = {
        str(path.relative_to(ROOT))
        for path in SKILLS_ROOT.glob("*/*/SKILL.md")
    }

    missing = sorted(EXPECTED_SKILLS - discovered)
    extra = sorted(discovered - EXPECTED_SKILLS)
    if missing:
        errors.extend(f"缺少 skill 文档: {path}" for path in missing)
    if extra:
        errors.extend(f"存在未登记的 skill 文档: {path}" for path in extra)

    for relative_path in sorted(discovered):
        content = (ROOT / relative_path).read_text(encoding="utf-8")
        for section in REQUIRED_SECTIONS:
            if section not in content:
                errors.append(f"{relative_path} 缺少章节: {section}")

    for relative_dir, required_files in PYTHON_SKILLS.items():
        directory = ROOT / relative_dir
        content = (directory / "SKILL.md").read_text(encoding="utf-8")
        if "Python Skill" not in content:
            errors.append(f"{relative_dir}/SKILL.md 未标记为 Python Skill")
        if "## 命令行" not in content:
            errors.append(f"{relative_dir}/SKILL.md 缺少命令行章节")
        for required_file in required_files:
            if not (directory / required_file).exists():
                errors.append(f"{relative_dir} 缺少文件: {required_file}")

    if errors:
        print("Skill 校验失败：")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print(f"Skill 校验通过：共 {len(discovered)} 个 skill 目录。")


if __name__ == "__main__":
    main()

