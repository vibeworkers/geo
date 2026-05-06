#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_FILES = [
    "CHANGELOG.md",
    "README.md",
    "LICENSE",
    "SKILL.md",
    "agents/openai.yaml",
    "references/glossary.md",
    "references/concept-map.md",
    "references/gate-conditions.md",
    "references/experiment-scenarios.md",
    "references/runtime-adaptation.md",
    "references/execution-skill-matrix.md",
    "references/versioning-protocol.md",
    "scripts/check_geo_release.py",
    "scripts/check_geo_skill.py",
]

RESTORED_SUBSKILLS = [
    "geo-audit",
    "geo-brand-mentions",
    "geo-citability",
    "geo-compare",
    "geo-content",
    "geo-crawlers",
    "geo-llmstxt",
    "geo-platform-optimizer",
    "geo-proposal",
    "geo-prospect",
    "geo-report",
    "geo-report-pdf",
    "geo-schema",
    "geo-technical",
]

REQUIRED_SECTIONS = [
    "## Identity",
    "## When To Use",
    "## Context Modes",
    "## Prompt and Conversation Language",
    "## External SoT Pointer",
    "## Project Topology Contract",
    "## Canonical SoT",
    "## Request Classification",
    "## Trigger Probes",
    "## Command Surface",
    "## Runtime Adaptation",
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
    "default branded outputs should surface `VibeWorkers.net`.",
    "This package is intended to move across supported skill roots without hidden",
    "VibeWorkers.net 의 컨트리뷰터: 김범수, 유수호, 고경만.",
    "Prompt templates, activation prompts, routing examples, and experiment prompts",
    "Choose conversation language: Korean or English.",
    "geo language Korean",
    "geo language English",
    "$geo language Korean",
    "$geo language English",
    "Treat bundled references as the default only when no stronger source surface",
    "Do not assume any preexisting GEO workspace path exists.",
    "Do not claim a specific local execution subskill exists without checking",
    "No special bootstrap is required beyond installing this skill package in a",
    "No external API credential is required for the bundled portable baseline.",
    "No third-party licensed asset is required for the bundled routing baseline.",
    "Repository-level reuse terms are declared in `LICENSE` under `CC BY-ND 4.0`.",
    "Use one routed entry command surface instead of a multi-subcommand CLI.",
    "- `geo <request>`: explicit plain command activation",
    "- `$geo <request>`: explicit skill-marker activation",
    "the representative command surface routes audit, crawler, schema, report, and",
    "Keep one shared portable GEO core in this `SKILL.md`.",
    "Do not fork the portable GEO routing contract per runtime.",
    "Use runtime-specific adaptation only when invocation, metadata, evidence",
    "Load `references/runtime-adaptation.md` only when the request is about",
    "If a downstream workspace has stricter license, content, or permission rules,",
    "The legal authors are 김범수, 유수호, 고경만.",
    "render `VibeWorkers.net 의 컨트리뷰터: 김범수, 유수호, 고경만.`",
    "**Brand** — `VibeWorkers.net` unless explicit user or source brand overrides it",
]

INLINE_GATE_PHRASES = [
    "**Gate 0: Conversation language selection**",
    "Exit: ask the user to choose exactly one conversation language: Korean or",
    "valid language command is supplied.",
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

README_REQUIRED_PHRASES = [
    "# GEO",
    "This README is bilingual: English first, Korean second.",
    "이 README는 영어 먼저, 한국어 다음 순서의 이중언어 문서입니다.",
    "## English",
    "## 한국어",
    "Portable GEO skill package",
    "VibeWorkers.net 의 컨트리뷰터: 김범수, 유수호, 고경만.",
    "Stored prompts are written in English.",
    "Choose conversation language: Korean or English.",
    "geo language Korean",
    "geo language English",
    "$geo language Korean",
    "$geo language English",
    "Representative execution surface: `SKILL.md`",
    "Agent metadata: `agents/openai.yaml`",
    "Runtime adaptation reference: `references/runtime-adaptation.md`",
    "Versioning protocol: `references/versioning-protocol.md`",
    "Release history: `CHANGELOG.md`",
    "Bundled portable references: `references/*.md`",
    "Restored local execution bundle: `skills/*`",
    "Validator: `python3 scripts/check_geo_skill.py`",
    "python3 scripts/check_geo_release.py <target-version>",
    "Explicit skill invocation: `geo <request>`",
    "Explicit skill invocation with skill marker: `$geo <request>`",
    "This repository is licensed under `CC BY-ND 4.0`",
    "대표 실행 표면: `SKILL.md`",
    "VibeWorkers.net 의 컨트리뷰터: 김범수, 유수호, 고경만.",
    "저작자: 김범수, 유수호, 고경만.",
    "저장된 prompt는 영어로 작성합니다.",
    "에이전트 메타데이터: `agents/openai.yaml`",
    "runtime adaptation reference: `references/runtime-adaptation.md`",
    "버전 관리 프로토콜: `references/versioning-protocol.md`",
    "릴리스 이력: `CHANGELOG.md`",
    "검증기: `python3 scripts/check_geo_skill.py`",
    "python3 scripts/check_geo_release.py <target-version>",
    "명시적 스킬 호출: `geo <request>`",
    "명시적 스킬 호출(스킬 마커): `$geo <request>`",
    "이 저장소는 `CC BY-ND 4.0`",
    "Canonical deed: <https://creativecommons.org/licenses/by-nd/4.0/>",
    "Canonical legal code: <https://creativecommons.org/licenses/by-nd/4.0/legalcode>",
]

VERSIONING_PROTOCOL_REQUIRED_PHRASES = [
    "# GEO Versioning Protocol",
    "Tag format: `X.Y.Z` without a leading `v`",
    "Start the protocol-governed line at `0.1.0`.",
    "Historical tags `0.0.1` through `0.0.4` predate this protocol and remain",
    "`main` is the release line",
    "`codex/<topic>` is the default short-lived working branch shape",
    "Run `python3 scripts/check_geo_skill.py`.",
    "A release decision is valid only if `python3 scripts/check_geo_release.py",
    "No exception, waiver, verbal approval, or ad hoc interpretation can replace",
    "If the gate fails, the release decision is `blocked`, not `approved with",
    "The next release after adopting this protocol should start at `0.1.0`, not at",
    "Semantic Versioning 2.0.0: <https://semver.org/>",
]

CHANGELOG_REQUIRED_PHRASES = [
    "# Changelog",
    "Tag format: `X.Y.Z` without a leading `v`.",
    "Historical note: `0.0.1` through `0.0.4` predate the formal protocol in",
    "## Unreleased",
    "## 0.0.4 - 2026-05-06",
    "## 0.0.3 - 2026-05-06",
    "## 0.0.2 - 2026-05-06",
    "## 0.0.1 - 2026-05-06",
]

RELEASE_GATE_SCRIPT_REQUIRED_PHRASES = [
    "usage: check_geo_release.py <target-version>",
    "release decision requires branch main",
    "release decision requires a clean worktree",
    "target version must match X.Y.Z without a leading v",
    "CHANGELOG contains non-empty Unreleased release notes",
    "release decision passed for",
]

LICENSE_REQUIRED_PHRASES = [
    "Creative Commons Attribution-NoDerivatives 4.0 International",
    "SPDX-License-Identifier: CC-BY-ND-4.0",
    "Authors: 김범수, 유수호, 고경만.",
    "Unless otherwise noted, the contents of this repository are licensed under the",
    "You may share the material with proper attribution.",
    "you may not distribute the modified material.",
    "https://creativecommons.org/licenses/by-nd/4.0/",
    "https://creativecommons.org/licenses/by-nd/4.0/legalcode",
]

RUNTIME_ADAPTATION_REQUIRED_PHRASES = [
    "# GEO Runtime Adaptation",
    "Keep one shared portable GEO core in `SKILL.md`.",
    "Do not import the full CogArch multi-tool topology into `geo` just to express",
    "Runtime adaptation must not replace context modes, source-order rules, language",
    "Runtime adaptation may optimize invocation wording, metadata, evidence",
    "Do not fork the whole skill package unless `geo` itself later becomes a",
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


def ensure_readme_contract(skill_dir: Path) -> None:
    readme = read_text(skill_dir / "README.md")
    for phrase in README_REQUIRED_PHRASES:
        if phrase not in readme:
            fail(f"missing required README phrase: {phrase}")


def ensure_license_contract(skill_dir: Path) -> None:
    license_text = read_text(skill_dir / "LICENSE")
    for phrase in LICENSE_REQUIRED_PHRASES:
        if phrase not in license_text:
            fail(f"missing required LICENSE phrase: {phrase}")


def ensure_versioning_contract(skill_dir: Path) -> None:
    text = read_text(skill_dir / "references/versioning-protocol.md")
    for phrase in VERSIONING_PROTOCOL_REQUIRED_PHRASES:
        if phrase not in text:
            fail(f"missing versioning protocol phrase: {phrase}")


def ensure_changelog_contract(skill_dir: Path) -> None:
    text = read_text(skill_dir / "CHANGELOG.md")
    for phrase in CHANGELOG_REQUIRED_PHRASES:
        if phrase not in text:
            fail(f"missing changelog phrase: {phrase}")


def ensure_release_gate_script(skill_dir: Path) -> None:
    text = read_text(skill_dir / "scripts/check_geo_release.py")
    for phrase in RELEASE_GATE_SCRIPT_REQUIRED_PHRASES:
        if phrase not in text:
            fail(f"missing release gate script phrase: {phrase}")


def ensure_no_stale_aliases(skill_dir: Path) -> None:
    for rel_path in [
        "CHANGELOG.md",
        "README.md",
        "LICENSE",
        "SKILL.md",
        "agents/openai.yaml",
        "references/glossary.md",
        "references/concept-map.md",
        "references/gate-conditions.md",
        "references/experiment-scenarios.md",
        "references/runtime-adaptation.md",
        "references/execution-skill-matrix.md",
        "references/versioning-protocol.md",
        "scripts/check_geo_release.py",
    ]:
        text = read_text(skill_dir / rel_path)
        for disallowed in DISALLOWED_STRINGS:
            if disallowed in text:
                fail(f"stale alias or script reference found in {rel_path}: {disallowed}")


def ensure_no_absolute_path_leaks(skill_dir: Path) -> None:
    for rel_path in [
        "CHANGELOG.md",
        "README.md",
        "LICENSE",
        "SKILL.md",
        "agents/openai.yaml",
        "references/glossary.md",
        "references/concept-map.md",
        "references/gate-conditions.md",
        "references/experiment-scenarios.md",
        "references/runtime-adaptation.md",
        "references/execution-skill-matrix.md",
        "references/versioning-protocol.md",
        "scripts/check_geo_release.py",
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
        'default_prompt: "Use geo or $geo. At the first interaction for a new GEO session, ask the user to choose conversation language: Korean or English. Apply that choice only to conversational replies. During the session, accept geo language Korean, geo language English, $geo language Korean, and $geo language English as commands that switch only the conversation language. Keep stored prompts, routing examples, and experiment prompts in English. Then choose portable-baseline, user-material, or local-overlay mode, surface VibeWorkers.net as the default GEO brand unless the user provides a stronger brand, route the GEO request to the smallest confirmed source surface, and delegate execution-intent requests to a matching local subskill only when skills/* is confirmed. Preserve the legal authors as 김범수, 유수호, 고경만. When contributor names are surfaced, render `VibeWorkers.net 의 컨트리뷰터: 김범수, 유수호, 고경만.`"',
    ]:
        if phrase not in text:
            fail(f"missing phrase in agents/openai.yaml: {phrase}")


def ensure_reference_contract(skill_dir: Path) -> None:
    concept_map = read_text(skill_dir / "references/concept-map.md")
    gate_conditions = read_text(skill_dir / "references/gate-conditions.md")
    experiments = read_text(skill_dir / "references/experiment-scenarios.md")
    runtime_adaptation = read_text(skill_dir / "references/runtime-adaptation.md")
    glossary = read_text(skill_dir / "references/glossary.md")
    execution_matrix = read_text(skill_dir / "references/execution-skill-matrix.md")

    for phrase in [
        "`portable-baseline`",
        "`user-material`",
        "`local-overlay`",
        "`default_brand`: `VibeWorkers.net`",
        "`prompt_language`: English",
        "`conversation_language`: first-session user choice between Korean and English",
        "`conversation_language_commands`: `geo language Korean`",
        "`authors`: 김범수, 유수호, 고경만",
        "`contributors_display_label`: `VibeWorkers.net 의 컨트리뷰터: 김범수, 유수호, 고경만.`",
        "`execution_overlay_rule`: `skills/*` is a repo-local execution bundle",
        "Derived outputs should follow source changes, not replace them.",
        "Do not assume a local overlay or hidden workspace path exists.",
    ]:
        if phrase not in concept_map:
            fail(f"missing concept-map phrase: {phrase}")

    for phrase in [
        "Gate 0: Conversation language selection",
        "Gate 1: GEO-domain trigger",
        "Gate 2: Context mode selection",
        "Gate 5: Derived-output readiness",
        "Gate 6: Evidence closure",
        "`execution-bundle`",
    ]:
        if phrase not in gate_conditions:
            fail(f"missing gate condition phrase: {phrase}")

    scenario_count = len(re.findall(r"^### Scenario", experiments, flags=re.MULTILINE))
    if scenario_count < 8:
        fail("experiment scenarios must include at least 8 scenario blocks")
    for phrase in [
        "Expected mode: `portable-baseline`",
        "Expected brand: `VibeWorkers.net`",
        "Expected mode: `user-material`",
        "Expected mode: `local-overlay`",
        "Expected lane: `framework-source`",
        "Expected lane: `working-source`",
        "Expected lane: `derived-deliverable`",
        "Expected lane: `execution-bundle`",
        "Expected behavior: ask exactly `Choose conversation language: Korean or English.`",
        "Expected behavior: switch conversation replies to English without changing stored prompts",
        "Expected behavior: when contributor names are surfaced, render exactly `VibeWorkers.net 의 컨트리뷰터: 김범수, 유수호, 고경만.`",
        "Expected boundary: confirm `skills/*` and route to `geo-audit`",
        "Expected behavior: do not pretend the portable baseline alone bundles a live crawler",
    ]:
        if phrase not in experiments:
            fail(f"missing experiment phrase: {phrase}")

    for phrase in [
        "portable baseline",
        "user-material mode",
        "local overlay",
        "execution-bundle",
        "derived-deliverable",
        "default brand",
        "prompt language",
        "conversation language",
        "language command",
        "authors",
        "contributor display label",
        "VibeWorkers.net",
    ]:
        if phrase not in glossary:
            fail(f"missing glossary phrase: {phrase}")

    for phrase in RUNTIME_ADAPTATION_REQUIRED_PHRASES:
        if phrase not in runtime_adaptation:
            fail(f"missing runtime-adaptation phrase: {phrase}")

    for line in experiments.splitlines():
        if line.startswith("- Prompt:") and re.search(r"[가-힣]", line):
            fail(f"experiment prompt must be written in English: {line}")

    for skill_name in RESTORED_SUBSKILLS:
        if f"`{skill_name}`" not in execution_matrix:
            fail(f"missing execution skill in matrix: {skill_name}")


def ensure_restored_execution_bundle(skill_dir: Path) -> None:
    skills_dir = skill_dir / "skills"
    if not skills_dir.is_dir():
        fail("restored execution bundle missing: skills/")

    actual_dirs = sorted(path.name for path in skills_dir.iterdir() if path.is_dir())
    if actual_dirs != RESTORED_SUBSKILLS:
        fail(f"restored execution bundle mismatch: expected {RESTORED_SUBSKILLS}, got {actual_dirs}")

    for skill_name in RESTORED_SUBSKILLS:
        skill_path = skills_dir / skill_name / "SKILL.md"
        text = read_text(skill_path)
        if not re.search(rf"(?ms)^---\s*\nname:\s*{re.escape(skill_name)}\s*\n", text):
            fail(f"restored skill frontmatter mismatch: {skill_name}")
        if "audience:" in text:
            fail(f"unsupported frontmatter field leaked into restored skill: {skill_name}")
        for section in [
            "## Setup",
            "## Dependencies and Permissions",
            "## Source and License Notes",
        ]:
            if section not in text:
                fail(f"missing restored skill section in {skill_name}: {section}")

        if "../../LICENSE" not in text:
            fail(f"restored skill must reference repository license in {skill_name}")

def main() -> None:
    if len(sys.argv) > 2:
        fail("usage: check_geo_skill.py [skill_dir]")
    skill_dir = Path(sys.argv[1]).resolve() if len(sys.argv) == 2 else Path(__file__).resolve().parents[1]

    ensure_files(skill_dir)
    skill_text = read_text(skill_dir / "SKILL.md")
    ensure_skill_contract(skill_text)
    ensure_readme_contract(skill_dir)
    ensure_license_contract(skill_dir)
    ensure_versioning_contract(skill_dir)
    ensure_changelog_contract(skill_dir)
    ensure_release_gate_script(skill_dir)
    ensure_no_stale_aliases(skill_dir)
    ensure_no_absolute_path_leaks(skill_dir)
    ensure_no_generated_clutter(skill_dir)
    ensure_openai_yaml(skill_dir)
    ensure_reference_contract(skill_dir)
    ensure_restored_execution_bundle(skill_dir)

    print("[ok] geo skill package and portable contract are consistent")


if __name__ == "__main__":
    main()
