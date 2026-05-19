#!/usr/bin/env python3
"""Static evidence-contract checks for the KR2 GEO skill package.

This checker is intentionally conservative. It verifies that the package has a
routing matrix, external source index, evidence boundary, and that every root
routed subskill resolves to an on-disk skill. It does not prove factual truth;
it guards against losing the evidence contract.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
README = ROOT / "README.md"
OVERVIEW = ROOT / "OVERVIEW.md"
SKILLS = ROOT / "skills"
REFERENCES = ROOT / "references"
REPORTS = ROOT / "reports" / "2026-05-12-individual-geo-audits" / "README.md"
PORTABILITY_PATH_PATTERNS = [
    re.compile(r"/Volumes/"),
    re.compile(r"/Users/"),
]
PORTABILITY_SURFACE_SUFFIXES = {".md", ".yaml", ".yml"}

REQUIRED_FILES = [
    OVERVIEW,
    REFERENCES / "evidence-boundary.md",
    REFERENCES / "source-index.md",
    REFERENCES / "function-matching-matrix.md",
    REFERENCES / "lang-platform-map.md",
]

REQUIRED_SECTIONS = [
    "### Working Source of Truth and Clarification Packet",
    "### Trigger Contract",
    "### Capability Split",
    "### Runtime Compatibility Gate",
    "### Legacy Package Distillation Gate",
    "### Code / LLM Boundary",
    "### 3-Layer Classification",
    "### Portable Handoff Metadata",
    "### Rubric",
]

REQUIRED_EVIDENCE_TERMS = [
    "Measured",
    "Readiness",
    "Heuristic",
    "Manual Fallback",
]

REQUIRED_SOURCE_TERMS = [
    "RFC 9309",
    "OpenAI",
    "Anthropic",
    "Google",
    "schema.org",
    "hreflang",
    "Playwright",
    "W3C",
    "Sitemaps.org",
    "arXiv",
    "Evidence Maturity Matrix",
    "Established",
    "Emerging/proposal",
    "Empirical caution",
]

REQUIRED_OVERVIEW_TERMS = [
    "전체 기능 및 매칭 표",
    "외부 타당성 근거",
    "근거 확립성 판정",
    "실제 가능성 판정",
    "확립된",
    "robots.txt",
    "structured data",
    "hreflang",
    "llms.txt",
    "제안",
    "Playwright",
    "`/geo-code pipeline`",
]

REQUIRED_REALITY_TERMS = [
    "현실 가능성 게이트",
    "AI가 인용한다",
    "Readiness",
    "Heuristic",
]

REQUIRED_RUNTIME_HINT_TERMS = [
    "GEO_TUNNEL_ROOT",
    "00_tunnel",
]

REQUIRED_SKILL_PHRASES = [
    "Fixed (this `SKILL.md`, validator text, package boundary notes):",
    "Flexible values are defined in `references/source-index.md`,",
    "`references/function-matching-matrix.md`, `references/lang-platform-map.md`,",
    "`references/concept-map.md`, and the matching file under `skills/*/SKILL.md`.",
    "whether a claim must remain `Readiness` / `Heuristic` or can be upgraded to",
    "`Measured`",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def read(path: Path) -> str:
    if not path.exists():
        fail(f"missing required file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def routed_subskills(skill_text: str) -> set[str]:
    names: set[str] = set()
    for line in skill_text.splitlines():
        if not line.startswith("| `/geo"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        subskill = cells[1]
        match = re.search(r"(geo-[a-z0-9-]+)", subskill)
        if match:
            names.add(match.group(1))
    return names


def portability_surfaces() -> list[Path]:
    surfaces: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix not in PORTABILITY_SURFACE_SUFFIXES:
            continue
        surfaces.append(path)
    return sorted(surfaces, key=lambda path: path.as_posix())


def main() -> None:
    skill_text = read(SKILL)

    for path in REQUIRED_FILES:
        read(path)

    for section in REQUIRED_SECTIONS:
        if section not in skill_text:
            fail(f"SKILL.md missing section: {section}")

    for path in portability_surfaces():
        text = read(path)
        for pattern in PORTABILITY_PATH_PATTERNS:
            if pattern.search(text):
                fail(
                    "absolute path leak found in "
                    f"{path.relative_to(ROOT)}: pattern {pattern.pattern}"
                )

    boundary = read(REFERENCES / "evidence-boundary.md")
    for term in REQUIRED_EVIDENCE_TERMS:
        if term not in boundary:
            fail(f"evidence-boundary.md missing term: {term}")

    source_index = read(REFERENCES / "source-index.md")
    for term in REQUIRED_SOURCE_TERMS:
        if term not in source_index:
            fail(f"source-index.md missing source family: {term}")

    matrix = read(REFERENCES / "function-matching-matrix.md")
    overview = read(OVERVIEW)
    readme = read(README)
    routed = routed_subskills(skill_text)
    if not routed:
        fail("no routed subskills found in SKILL.md")

    for name in sorted(routed):
        if not (SKILLS / name / "SKILL.md").exists():
            fail(f"routed subskill missing: skills/{name}/SKILL.md")
        if f"`{name}`" not in matrix:
            fail(f"function-matching-matrix.md missing routed subskill: {name}")

    for command in ["`/geo-code init`", "`/geo-code pipeline`", "`/geo-code status`"]:
        if command not in matrix:
            fail(f"function-matching-matrix.md missing command: {command}")
        if command not in overview:
            fail(f"OVERVIEW.md missing command: {command}")

    for term in REQUIRED_OVERVIEW_TERMS:
        if term not in overview:
            fail(f"OVERVIEW.md missing term: {term}")

    for term in REQUIRED_REALITY_TERMS:
        if term not in readme and term not in skill_text:
            fail(f"README.md or SKILL.md missing reality gate term: {term}")

    for term in REQUIRED_RUNTIME_HINT_TERMS:
        if term not in readme:
            fail(f"README.md missing local runtime hint: {term}")

    if "observed site data" not in matrix or "stored platform output" not in matrix:
        fail("function-matching-matrix.md missing realistic-claim guard")

    if "`OVERVIEW.md`" not in readme:
        fail("README.md missing OVERVIEW.md pointer")

    brand_mentions = read(SKILLS / "geo-brand-mentions" / "SKILL.md")
    if '"/geo brand"' in brand_mentions or '"/geo brand".' in brand_mentions:
        fail("geo-brand-mentions trigger must not collide with /geo brand")
    if '"/geo brands"' not in brand_mentions:
        fail("geo-brand-mentions trigger missing /geo brands")

    for phrase in ["heuristic readiness", "Measured", "Readiness", "Heuristic"]:
        if phrase not in skill_text:
            fail(f"SKILL.md missing evidence disclosure phrase: {phrase}")

    for phrase in REQUIRED_SKILL_PHRASES:
        if phrase not in skill_text:
            fail(f"SKILL.md missing phrase: {phrase}")

    if REPORTS.exists():
        report_text = REPORTS.read_text(encoding="utf-8")
        for phrase in ["Measured", "Readiness", "Heuristic", "Manual fallback"]:
            if phrase not in report_text:
                fail(f"audit README missing evidence-state phrase: {phrase}")

    print("KR2 evidence contract: OK")


if __name__ == "__main__":
    main()
