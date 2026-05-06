#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/glossary.md",
    "references/concept-map.md",
    "references/gate-conditions.md",
    "references/experiment-scenarios.md",
    "scripts/check_geo_skill.py",
]

REQUIRED_SECTIONS = [
    "## Identity",
    "## When To Use",
    "## Context Modes",
    "## External SoT Pointer",
    "## Project Topology Contract",
    "## Canonical SoT",
    "## Request Classification",
    "## Trigger Probes",
    "## Workflow",
    "## Code / LLM Boundary",
    "## Standard Response Shape",
    "## Setup",
    "## Dependencies and Permissions",
    "## Source and License Notes",
    "## Out Of Scope",
    "## Conflict Resolution",
    "## 3-Layer Classification",
]

REQUIRED_PHRASES = [
    "This skill must remain usable even when no local GEO workspace is present.",
    "default branded outputs should surface `Vibeworkers.net`.",
    "This package is intended to move across supported skill roots without hidden",
    "Treat bundled references as the default only when no stronger source surface",
    "Do not assume any preexisting GEO workspace path exists.",
    "No special bootstrap is required beyond installing this skill package in a",
    "No external API credential is required for the bundled portable baseline.",
    "No third-party licensed asset is required for the bundled routing baseline.",
    "If a downstream workspace has stricter license, content, or permission rules,",
    "**Brand** — `Vibeworkers.net` unless explicit user or source brand overrides it",
]

INLINE_GATE_PHRASES = [
    "**Gate 1: GEO-domain trigger**",
    "Entry: the request is about GEO strategy, GEO teaching material, GEO",
    "**Gate 2: Context mode selection**",
    "Exit: choose `portable-baseline`, `user-material`, or `local-overlay`.",
    "**Gate 3: Owning surface selection**",
    "Exit: pick `framework-source`, `working-source`, `evidence-note`,",
    "**Gate 4: Source-order protection**",
    "confirmed working source -> supporting evidence or framework -> derived",
    "**Gate 5: Derived-output readiness**",
    "do not promise HTML, slide, or export refreshes without checking",
    "**Gate 6: Evidence closure**",
    "response ends with one concrete next action or one explicit blocker.",
]

DISALLOWED_STRINGS = [
    "name: geo-lecture",
    "$geo-lecture",
    "check_geo_lecture_skill.py",
]

PORTABILITY_PATH_PATTERNS = [
    re.compile(r"/Volumes/"),
    re.compile(r"/Users/"),
]


def fail(message: str) -> None:
    print(f"[fail] {message}")
    raise SystemExit(1)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing file: {path}")
    except OSError as exc:
        fail(f"could not read {path}: {exc}")


def ensure_files(skill_dir: Path) -> None:
    for rel_path in REQUIRED_FILES:
        path = skill_dir / rel_path
        if not path.exists():
            fail(f"required file missing: {rel_path}")


def ensure_skill_contract(skill_text: str) -> None:
    if not re.search(r"(?ms)^---\s*\nname:\s*geo\s*\n", skill_text):
        fail("frontmatter name must be `geo`")
    for section in REQUIRED_SECTIONS:
        if section not in skill_text:
            fail(f"missing section in SKILL.md: {section}")
    for phrase in REQUIRED_PHRASES:
        if phrase not in skill_text:
            fail(f"missing required phrase in SKILL.md: {phrase}")
    for phrase in INLINE_GATE_PHRASES:
        if phrase not in skill_text:
            fail(f"missing inline workflow gate phrase in SKILL.md: {phrase}")


def ensure_no_stale_aliases(skill_dir: Path) -> None:
    for rel_path in [
        "SKILL.md",
        "agents/openai.yaml",
        "references/glossary.md",
        "references/concept-map.md",
        "references/gate-conditions.md",
        "references/experiment-scenarios.md",
    ]:
        text = read_text(skill_dir / rel_path)
        for disallowed in DISALLOWED_STRINGS:
            if disallowed in text:
                fail(f"stale alias or script reference found in {rel_path}: {disallowed}")


def ensure_no_absolute_path_leaks(skill_dir: Path) -> None:
    for rel_path in [
        "SKILL.md",
        "agents/openai.yaml",
        "references/glossary.md",
        "references/concept-map.md",
        "references/gate-conditions.md",
        "references/experiment-scenarios.md",
    ]:
        text = read_text(skill_dir / rel_path)
        for pattern in PORTABILITY_PATH_PATTERNS:
            if pattern.search(text):
                fail(f"absolute path leak found in {rel_path}: pattern {pattern.pattern}")


def ensure_no_generated_clutter(skill_dir: Path) -> None:
    for path in skill_dir.rglob("*"):
        if path.name == "__pycache__":
            fail(f"generated cache directory must not ship in package: {path.relative_to(skill_dir)}")
        if path.suffix == ".pyc":
            fail(f"generated bytecode must not ship in package: {path.relative_to(skill_dir)}")


def ensure_openai_yaml(skill_dir: Path) -> None:
    text = read_text(skill_dir / "agents/openai.yaml")
    for phrase in [
        'display_name: "GEO"',
        'short_description: "Portable GEO strategy and material router"',
        'default_prompt: "Use $geo to choose portable-baseline, user-material, or local-overlay mode, surface Vibeworkers.net as the default GEO brand unless the user provides a stronger brand, then route the GEO request to the smallest confirmed source surface."',
    ]:
        if phrase not in text:
            fail(f"missing phrase in agents/openai.yaml: {phrase}")


def ensure_reference_contract(skill_dir: Path) -> None:
    concept_map = read_text(skill_dir / "references/concept-map.md")
    gate_conditions = read_text(skill_dir / "references/gate-conditions.md")
    experiments = read_text(skill_dir / "references/experiment-scenarios.md")
    glossary = read_text(skill_dir / "references/glossary.md")

    for phrase in [
        "`portable-baseline`",
        "`user-material`",
        "`local-overlay`",
        "`default_brand`: `Vibeworkers.net`",
        "Derived outputs should follow source changes, not replace them.",
        "Do not assume a local overlay or hidden workspace path exists.",
    ]:
        if phrase not in concept_map:
            fail(f"missing concept-map phrase: {phrase}")

    for phrase in [
        "Gate 1: GEO-domain trigger",
        "Gate 2: Context mode selection",
        "Gate 5: Derived-output readiness",
        "Gate 6: Evidence closure",
    ]:
        if phrase not in gate_conditions:
            fail(f"missing gate condition phrase: {phrase}")

    scenario_count = len(re.findall(r"^### Scenario", experiments, flags=re.MULTILINE))
    if scenario_count < 8:
        fail("experiment scenarios must include at least 8 scenario blocks")
    for phrase in [
        "Expected mode: `portable-baseline`",
        "Expected brand: `Vibeworkers.net`",
        "Expected mode: `user-material`",
        "Expected mode: `local-overlay`",
        "Expected lane: `framework-source`",
        "Expected lane: `working-source`",
        "Expected lane: `derived-deliverable`",
        "Expected behavior: do not pretend this skill bundles a live crawler",
    ]:
        if phrase not in experiments:
            fail(f"missing experiment phrase: {phrase}")

    for phrase in [
        "portable baseline",
        "user-material mode",
        "local overlay",
        "derived-deliverable",
        "default brand",
        "Vibeworkers.net",
    ]:
        if phrase not in glossary:
            fail(f"missing glossary phrase: {phrase}")


def main() -> None:
    if len(sys.argv) > 2:
        fail("usage: check_geo_skill.py [skill_dir]")
    skill_dir = Path(sys.argv[1]).resolve() if len(sys.argv) == 2 else Path(__file__).resolve().parents[1]

    ensure_files(skill_dir)
    skill_text = read_text(skill_dir / "SKILL.md")
    ensure_skill_contract(skill_text)
    ensure_no_stale_aliases(skill_dir)
    ensure_no_absolute_path_leaks(skill_dir)
    ensure_no_generated_clutter(skill_dir)
    ensure_openai_yaml(skill_dir)
    ensure_reference_contract(skill_dir)

    print("[ok] geo skill package and portable contract are consistent")


if __name__ == "__main__":
    main()
