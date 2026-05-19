#!/usr/bin/env python3
"""Static contract checks for the GEO deep-audit ecommerce package."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
AGENT = ROOT / "agents" / "openai.yaml"
REFERENCES = ROOT / "references"
RAW = ROOT / "raw"
SCORECARD = RAW / "audit_scorecard.csv"
SUMMARY_SCRIPT = ROOT / "scripts" / "summarize_scorecard.py"

PORTABILITY_PATH_PATTERNS = [
    re.compile(r"/Volumes/"),
    re.compile(r"/Users/"),
]
PORTABILITY_SURFACE_SUFFIXES = {".md", ".yaml", ".yml"}

REQUIRED_FILES = [
    SKILL,
    AGENT,
    REFERENCES / "glossary.md",
    REFERENCES / "concept-map.md",
    REFERENCES / "evidence-boundary.md",
    REFERENCES / "source-index.md",
    RAW / "00_Executive_Summary.md",
    RAW / "01_Coupang_Deep_GEO_Audit.md",
    RAW / "02_Gmarket_Deep_GEO_Audit.md",
    RAW / "03_Musinsa_Deep_GEO_Audit.md",
    RAW / "04_OliveYoung_Deep_GEO_Audit.md",
    RAW / "05_Crawler_Access_Matrix.md",
    RAW / "06_Roadmap_and_Priorities.md",
    RAW / "07_Methodology_Limitations.md",
    SCORECARD,
    SUMMARY_SCRIPT,
]

REQUIRED_SECTIONS = [
    "## Overview",
    "## Working Source Of Truth",
    "## When To Use",
    "## Workflow",
    "## Runtime Compatibility Gate",
    "## Provider / Provenance vs Output Brand",
    "## Trigger Contract",
    "## Code / LLM Boundary",
    "## 3-Layer Classification",
    "## Setup",
    "## Dependencies And Permissions",
    "## Source And License Notes",
    "## References",
    "## Rubric",
]

REQUIRED_SKILL_PHRASES = [
    "The raw source files under `raw/` are immutable evidence.",
    "Create derived summaries, tables, or recommendations from the copied raw files",
    "Closure status: `runtime-delta implemented`.",
    "preserve raw source files",
    "use the smallest raw source surface",
    "the workflow skeleton and lane labels",
    "the actual contents of `raw/*.md` and `raw/audit_scorecard.csv`",
    "which evidence label applies to a given claim",
]

REQUIRED_EVIDENCE_TERMS = [
    "captured audit finding",
    "recommendation",
    "methodology assumption",
    "requires live validation",
    "observed AI citation",
    "referral traffic",
    "conversion lift",
]

REQUIRED_SOURCE_TERMS = [
    "raw/00_Executive_Summary.md",
    "raw/01_Coupang_Deep_GEO_Audit.md",
    "raw/02_Gmarket_Deep_GEO_Audit.md",
    "raw/03_Musinsa_Deep_GEO_Audit.md",
    "raw/04_OliveYoung_Deep_GEO_Audit.md",
    "raw/05_Crawler_Access_Matrix.md",
    "raw/06_Roadmap_and_Priorities.md",
    "raw/07_Methodology_Limitations.md",
    "raw/audit_scorecard.csv",
]

EXPECTED_RANKING = ["Musinsa", "Olive Young", "Gmarket", "Coupang"]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def read(path: Path) -> str:
    if not path.exists():
        fail(f"missing required file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def portability_surfaces() -> list[Path]:
    surfaces: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix not in PORTABILITY_SURFACE_SUFFIXES:
            continue
        surfaces.append(path)
    return sorted(surfaces, key=lambda path: path.as_posix())


def ensure_scorecard_summary() -> None:
    completed = subprocess.run(
        ["python3", str(SUMMARY_SCRIPT), str(SCORECARD)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        detail = (completed.stdout + completed.stderr).strip()
        fail(f"summarize_scorecard.py failed: {detail}")

    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        fail(f"summarize_scorecard.py did not emit valid JSON: {exc}")

    if payload.get("site_count") != 4:
        fail("scorecard summary must report site_count=4")

    ranking = payload.get("ranking")
    if not isinstance(ranking, list) or [row.get("site") for row in ranking] != EXPECTED_RANKING:
        fail("scorecard ranking order drifted from the packaged audit")

    if payload.get("score_fields") != [
        "crawler_access",
        "citability",
        "content_quality",
        "technical_seo",
        "structured_data",
        "platform_optimization",
    ]:
        fail("scorecard score_fields drifted from the packaged contract")


def main() -> None:
    skill_text = read(SKILL)
    for path in REQUIRED_FILES:
        read(path)

    for section in REQUIRED_SECTIONS:
        if section not in skill_text:
            fail(f"SKILL.md missing section: {section}")

    for phrase in REQUIRED_SKILL_PHRASES:
        if phrase not in skill_text:
            fail(f"SKILL.md missing phrase: {phrase}")

    evidence = read(REFERENCES / "evidence-boundary.md")
    for term in REQUIRED_EVIDENCE_TERMS:
        if term not in evidence:
            fail(f"evidence-boundary.md missing term: {term}")

    source_index = read(REFERENCES / "source-index.md")
    for term in REQUIRED_SOURCE_TERMS:
        if term not in source_index:
            fail(f"source-index.md missing file pointer: {term}")

    concept_map = read(REFERENCES / "concept-map.md")
    for phrase in ["`raw/` owns copied evidence and must not be edited.", "`scripts/` owns deterministic parsing of packaged data."]:
        if phrase not in concept_map:
            fail(f"concept-map.md missing package boundary phrase: {phrase}")

    agent = read(AGENT)
    for phrase in ['display_name: "GEO Deep Audit Ecommerce"', 'short_description: "Package ecommerce GEO audit evidence"']:
        if phrase not in agent:
            fail(f"agents/openai.yaml missing phrase: {phrase}")

    for path in portability_surfaces():
        text = read(path)
        for pattern in PORTABILITY_PATH_PATTERNS:
            if pattern.search(text):
                fail(
                    "absolute path leak found in "
                    f"{path.relative_to(ROOT)}: pattern {pattern.pattern}"
                )

    ensure_scorecard_summary()
    print("GEO deep audit ecommerce contract: OK")


if __name__ == "__main__":
    main()
