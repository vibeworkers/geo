#!/usr/bin/env python3

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


REQUIRED_FILES = [
    "AGENTS.md",
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
    "references/measurement-loop.md",
    "references/commerce-readiness.md",
    "references/platform-truth-registry.md",
    "references/measurement-capture-template.md",
    "references/commerce-audit-worksheet.md",
    "references/private-surface-routing.md",
    "references/regional-situational-routing.md",
    "references/policy-risk-gate.md",
    "references/report-template-contract.md",
    "references/implementation-completion-plan.md",
    "references/user-level-workflow-guide.md",
    "references/execution-skill-matrix.md",
    "references/cogarch-alignment.md",
    "references/sequence-dependent-autopilot.md",
    "references/organic-capability-system.md",
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
    "## Sequence-Dependent Autopilot",
    "## Clarification-First Intake",
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
    "This package uses `VibeWorkers` as its output brand.",
    "The official website is <https://vibeworkers.net>.",
    "outputs default to `VibeWorkers`.",
    "This package is intended to move across supported skill roots without hidden",
    "When this checkout is used as beta-A, beta-A is represented by the separate",
    "representative skill name and command surface remain `geo`.",
    "VibeWorkers 의 컨트리뷰터: 김범수, 유수호, 고경만.",
    "Prompt templates, activation prompts, routing examples, and experiment prompts",
    "Choose conversation language: Korean or English.",
    "geo language Korean",
    "geo language English",
    "$geo language Korean",
    "$geo language English",
    "Treat bundled references as the default only when no stronger source surface",
    "If goal, scope, working surface, success condition, or evidence target is still",
    "Freeze a clarification packet with at least `goal / scope / surface / success / evidence target`.",
    "Do not assume any preexisting GEO workspace path exists.",
    "Do not claim a specific local execution subskill exists without checking",
    "No special bootstrap is required beyond installing this skill package in a",
    "No external API credential is required for the bundled portable baseline.",
    "No third-party licensed asset is required for the bundled routing baseline.",
    "Repository-level reuse terms are declared in `LICENSE` under `CC BY-NC-ND 4.0`.",
    "Use one routed entry command surface instead of a multi-subcommand CLI.",
    "- `geo <request>`: explicit plain command activation",
    "- `$geo <request>`: explicit skill-marker activation",
    "the representative command surface routes audit, crawler, schema, report, and",
    "delegated execution subskills must stay usable when opened directly and must",
    "Keep one shared portable GEO core in this `SKILL.md`.",
    "Do not fork the portable GEO routing contract per runtime.",
    "Use runtime-specific adaptation only when invocation, metadata, evidence",
    "Runtime-local first-use onboarding is allowed only when the target runtime",
    "When an advanced workflow is requested for the first time in a local",
    "the same guide remains manual in `README.md`,",
    "The shared portable package must stay usable even when no runtime-local",
    "Load `references/runtime-adaptation.md` only when the request is about",
    "Treat advanced-workflow setup as a guide-style feature.",
    "run that setup guide before promising execution.",
    "If the active runtime or model changes, rerun the same guide so runtime-local",
    "Each delegated subskill must still explain its own setup, permissions, access",
    "If a downstream workspace has stricter license, content, or permission rules,",
    "The legal authors are 김범수, 유수호, 고경만.",
    "render `VibeWorkers 의 컨트리뷰터: 김범수, 유수호, 고경만.`",
    "**Output brand** — default to `VibeWorkers`;",
    "Its official website is <https://vibeworkers.net>.",
    "They are routed by `geo`, but each one must remain a standalone contract rather",
    "`references/organic-capability-system.md` treats deep-audit-ecommerce and",
    "physical compatibility path for the `deep-audit-ecommerce` capability",
    "`packages/geo-seo-skills-kr2/` is the KR2 capability",
    "separate user-facing report",
    "one source-order decision, one evidence",
    "Gate 15: Organic capability composition",
    "compose `deep-audit-ecommerce` and `kr2` as needed under the root",
]

INLINE_GATE_PHRASES = [
    "**Gate 0: Conversation language selection**",
    "Exit: ask the user to choose exactly one conversation language: Korean or",
    "valid language command is supplied.",
    "**Gate 1: GEO-domain trigger**",
    "Entry: the request is about GEO strategy, GEO teaching material, GEO",
    "**Gate 2: Clarification-first intake**",
    "clarification packet with `goal / scope / surface / success / evidence target`.",
    "**Gate 3: Context mode selection**",
    "Exit: choose `portable-baseline`, `user-material`, or `local-overlay`.",
    "**Gate 4: Owning surface selection**",
    "Exit: pick `framework-source`, `working-source`, `evidence-note`,",
    "**Gate 5: Source-order protection**",
    "confirmed working source -> supporting evidence or framework -> derived",
    "**Gate 6: Derived-output readiness**",
    "run the advanced-workflow",
    "do not promise HTML, slide, or export refreshes without checking",
    "do not skip the setup-guide pass when first-use or",
    "**Gate 7: Evidence closure**",
    "response ends with one concrete next action or one explicit blocker.",
    "**Gate 8: Measurement confidence boundary**",
    "`references/measurement-loop.md`: readiness,",
    "heuristic, observed answer, observed citation, referral, or conversion.",
    "**Gate 9: Commerce/action readiness boundary**",
    "platform transaction eligibility.",
    "**Gate 10: Private surface boundary**",
    "public crawler, public search, private connector, logged-in user",
    "**Gate 11: Regional/situational boundary**",
    "regional or vertical claims must use a confirmed source pack",
    "**Gate 12: Policy risk boundary**",
    "robots, terms, privacy, regulated claims, brand claims",
    "**Gate 13: Whole-system completion boundary**",
    "completion_rubric_path_or_inline",
    "**Gate 14: Sequence-dependent autopilot**",
    "ordered dependency graph",
    "all_must_passed=true",
    "failed_must_queue",
    "**Gate 15: Organic capability composition**",
    "one evidence ledger, one completion",
    "judgment, and one report contract.",
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

CAPABILITY_PACKAGE_DIRS = [
    "packages/geo-deep-audit-ecommerce",
    "packages/geo-seo-skills-kr2",
]

PORTABILITY_SURFACE_SUFFIXES = {".md", ".yaml", ".yml"}

CAPABILITY_VALIDATOR_SCRIPTS = [
    "packages/geo-deep-audit-ecommerce/scripts/check_deep_audit_ecommerce_contract.py",
    "packages/geo-seo-skills-kr2/scripts/check_kr2_evidence_contract.py",
]

README_REQUIRED_PHRASES = [
    "# GEO",
    "This README is bilingual: English first, Korean second.",
    "이 README는 영어 먼저, 한국어 다음 순서의 이중언어 문서입니다.",
    "## English",
    "## 한국어",
    "Portable GEO skill package",
    "### Quick Summary",
    "`geo` helps solve these GEO work problems:",
    "### What This Project Is",
    "`beta-A` is not a separate skill name.",
    "### Why It Exists",
    "### Installation",
    "### Runtime Compatibility",
    "### Feature Guide",
    "### How To Use",
    "### Optional Advanced Workflows",
    "### Enable Advanced Workflows",
    "### Advanced Workflow Troubleshooting",
    "### Project Docs",
    "### System Notes",
    "### Package Provenance",
    "Additional guidance is included for:",
    "runtime compatibility across Codex/ChatGPT, Claude, and Gemini",
    "setup and model-specific optimization hints when a runtime can surface them",
    "`geo` is packaged as one portable skill with one representative router.",
    "`SKILL.md` owns the routing contract, `skills/geo-*` own advanced execution",
    "a Cognitive Architecture based skill",
    "Portable baseline installation:",
    "Advanced workflow installation:",
    "`geo` uses one shared `geo <request>` or `$geo <request>` contract across",
    "This repository currently ships native runtime metadata only for Codex /",
    "model-specific setup hints, or response packaging",
    "Automatic runtime-local setup guidance is possible only when that runtime",
    "Core router capabilities:",
    "Advanced execution workflows available with `skills/*`:",
    "| Capability | What it does | When to use | How to start |",
    "| Workflow | What it does | When to use | How to start |",
    "Each `skills/geo-*` subskill owns its own workflow contract.",
    "read and use that subskill directly from the files included in this package.",
    "If you are using this repository checkout, that bundle is already included.",
    "Think of advanced-workflow setup as the getting-started guide for this",
    "GEO may walk through this guide before it starts the workflow.",
    "If the active runtime or model changes, GEO may walk through the same guide",
    "permissions, or export steps can differ.",
    "Some runtimes can show this guide automatically.",
    "To make advanced workflows available:",
    "If advanced workflows are not available or do not start as expected:",
    "if GEO asks clarification questions first, answer them before expecting an",
    "if you switched to a different runtime or model, rerun the setup guide before",
    "`skills/geo-*/SKILL.md` directly;",
    "global setup or a command from an earlier session just to start",
    "treat the matching subskill as the workflow owner for setup, permissions,",
    "Stored prompts are written in English.",
    "Choose conversation language: Korean or English.",
    "geo language Korean",
    "geo language English",
    "$geo language Korean",
    "$geo language English",
    "`geo <request>`",
    "`$geo <request>`",
    "If goal, scope, working surface, success condition, or evidence target are",
    "`skills/*`",
    "`VibeWorkers`",
    "<https://vibeworkers.net>",
    "outputs default to `VibeWorkers`.",
    "`SKILL.md`",
    "`references/runtime-adaptation.md`",
    "`references/execution-skill-matrix.md`",
    "`references/measurement-loop.md`",
    "`references/commerce-readiness.md`",
    "`references/platform-truth-registry.md`",
    "`references/measurement-capture-template.md`",
    "`references/commerce-audit-worksheet.md`",
    "`references/private-surface-routing.md`",
    "`references/regional-situational-routing.md`",
    "`references/policy-risk-gate.md`",
    "`references/report-template-contract.md`",
    "`references/implementation-completion-plan.md`",
    "`references/user-level-workflow-guide.md`",
    "`references/cogarch-alignment.md`",
    "`references/sequence-dependent-autopilot.md`",
    "`references/organic-capability-system.md`",
    "### beta Organic System Integration",
    "### beta 유기적 시스템 통합",
    "`docs/beta/organic-beta-integration.ko.md`",
    "`packages/geo-deep-audit-ecommerce/`",
    "`packages/geo-seo-skills-kr2/`",
    "Organic capability workflows use `packages/*`",
    "geo core -> capability selection -> shared evidence ledger -> one report contract",
    "`skills/geo-*/SKILL.md`",
    "private `generateSkill` workflow derived from",
    "the public Skill Creator skill.",
    "This repository is licensed under `CC BY-NC-ND 4.0`",
    "Authors: 김범수, 유수호, 고경만.",
    "See `LICENSE` for repository terms.",
    "### 한눈 요약",
    "`geo`는 아래 GEO 문제를 해결하도록 돕습니다.",
    "### 이 프로젝트는 무엇인가",
    "`beta-A`는 별도 스킬명이 아닙니다.",
    "### 왜 존재하는가",
    "### 설치",
    "### 런타임 호환성",
    "### 기능 가이드",
    "### 사용하는 방법",
    "### 선택적 고급 Workflow",
    "### 고급 Workflow 준비",
    "### 고급 Workflow 문제 해결",
    "### 프로젝트 문서",
    "### 시스템 개요",
    "### 패키지 생성 배경",
    "추가로 아래 안내를 함께 제공합니다.",
    "Codex/ChatGPT, Claude, Gemini용 런타임 호환성",
    "런타임이 노출할 수 있을 때의 setup 및 모델별 최적화 힌트",
    "`geo`는 하나의 대표 라우터를 가진 portable skill 패키지로 묶여 있습니다.",
    "`SKILL.md`는 라우팅 계약을 소유하고, `skills/geo-*`는 고급 실행 workflow를",
    "Cognitive Architecture 기반 skill 설계",
    "Portable baseline 설치:",
    "Advanced workflow 설치:",
    "`geo`는 Codex/ChatGPT, Claude, Gemini에서 공통 `geo <request>` 또는",
    "현재 이 저장소는 Codex / OpenAI용 native runtime metadata만",
    "모델별 setup 힌트,",
    "자동 런타임별 setup guide는 해당 런타임이 native metadata, extension,",
    "기본 라우터 기능:",
    "`skills/*`가 있을 때 사용할 수 있는 고급 실행 workflow:",
    "| 기능 | 무엇을 하는가 | 언제 쓰는가 | 어떻게 시작하는가 |",
    "| Workflow | 무엇을 하는가 | 언제 쓰는가 | 어떻게 시작하는가 |",
    "각 `skills/geo-*` 서브스킬은 자기 workflow 계약을 직접 소유합니다.",
    "상위 `geo` 라우터는 그 서브스킬로 연결만 한다고 이해합니다",
    "이 저장소 checkout을 그대로 사용한다면 그 번들은 이미 포함되어 있습니다.",
    "이 패키지에 포함된 문서와 파일만으로도 읽고 따라갈 수 있어야 합니다.",
    "고급 workflow setup은 이 환경에서 처음 시작할 때 보는 사용 가이드라고",
    "guide를 먼저 따라갈 수 있습니다.",
    "같은 guide를 다시 볼 수 있습니다.",
    "자동으로 보여주는 런타임도 있고",
    "고급 workflow를 사용할 수 있게 하려면:",
    "고급 workflow가 보이지 않거나 기대대로 시작되지 않으면 아래 순서로",
    "GEO가 먼저 clarification question을 하면 답한 뒤에 audit, schema,",
    "다른 런타임이나 모델로 바꿨다면 기존 상태를 그대로 가정하지 말고 setup",
    "이전 세션에서 먼저 실행해 둔 명령을 요구하지 않습니다",
    "저작자: 김범수, 유수호, 고경만.",
    "`references/cogarch-alignment.md`",
    "`references/sequence-dependent-autopilot.md`",
    "`references/organic-capability-system.md`",
    "저장된 prompt는 영어로 작성합니다.",
    "goal, scope, working surface, success condition, evidence target이 아직",
    "`geo`의 output brand는 `VibeWorkers`입니다.",
    "<https://vibeworkers.net>",
    "출력 기본",
    "brand는 `VibeWorkers`입니다.",
    "공개 Skill Creator 스킬을 참고한 비공개 `generateSkill`",
    "이 저장소는 `CC BY-NC-ND 4.0`",
    "자세한 저장소 규약은 `LICENSE`를 참고하세요.",
    "Canonical deed: <https://creativecommons.org/licenses/by-nc-nd/4.0/>",
    "Canonical legal code: <https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode>",
]

EXECUTION_MATRIX_REQUIRED_PHRASES = [
    "# GEO Execution Skill Matrix",
    "This repository includes an optional local execution bundle under `skills/*`.",
    "Each subskill below owns its own setup, permission, access-profile, and output",
    "A subskill must remain usable without `cogarch`, `~/.cogarch`,",
    "Subskill examples should describe direct inputs or plain-language requests, not",
    "Treat this section as the advanced-workflow setup guide.",
    "Run this guide the first time an advanced workflow is requested in a local",
    "Run the same guide again when the active runtime or model changes.",
    "If you already know the exact workflow owner, you can open that subskill",
    "## Troubleshooting",
    "If GEO asks clarification questions first, answer them before expecting an",
    "If you switched to a different runtime or model, rerun the setup guide",
    "hidden global files or hidden session-state commands.",
    "## Standalone execution subskills",
    "| Skill | Primary use | Typical trigger | Local profile | Typical output |",
    "## Reference-guided extensions",
    "`references/measurement-loop.md`",
    "`references/commerce-readiness.md`",
    "`references/platform-truth-registry.md`",
    "`references/measurement-capture-template.md`",
    "`references/commerce-audit-worksheet.md`",
    "`references/private-surface-routing.md`",
    "`references/regional-situational-routing.md`",
    "`references/policy-risk-gate.md`",
    "`references/report-template-contract.md`",
    "`references/implementation-completion-plan.md`",
    "`references/cogarch-alignment.md`",
    "`references/sequence-dependent-autopilot.md`",
    "`references/organic-capability-system.md`",
    "## Organic capability composition",
    "`packages/geo-deep-audit-ecommerce/`",
    "`packages/geo-seo-skills-kr2/`",
    "one source-order decision, one evidence",
]

RESTORED_SUBSKILL_REQUIRED_PHRASES = [
    "standalone GEO 실행 계약이다.",
    "숨은 레벨 세션 상태를 요구하지 않는다.",
    "`L1`(manager), `L2`(operator), `L3`(builder)",
]

RESTORED_SUBSKILL_DISALLOWED_STRINGS = [
    "/geo ",
    "USER_LEVEL",
    "레벨을 변경하려면 `/geo level`",
    "~/.cogarch",
    "OPERATIONS.md",
]

SUBSKILL_REFERENCE_REQUIRED = {
    "geo-audit": [
        "../../references/measurement-capture-template.md",
        "../../references/commerce-audit-worksheet.md",
        "../../references/private-surface-routing.md",
        "../../references/regional-situational-routing.md",
        "../../references/policy-risk-gate.md",
        "../../references/report-template-contract.md",
    ],
    "geo-brand-mentions": [
        "../../references/measurement-capture-template.md",
        "../../references/private-surface-routing.md",
    ],
    "geo-citability": [
        "../../references/measurement-capture-template.md",
    ],
    "geo-compare": [
        "../../references/platform-truth-registry.md",
        "../../references/regional-situational-routing.md",
        "../../references/private-surface-routing.md",
        "../../references/policy-risk-gate.md",
        "../../references/measurement-capture-template.md",
    ],
    "geo-content": [
        "../../references/policy-risk-gate.md",
        "../../references/measurement-capture-template.md",
    ],
    "geo-crawlers": [
        "../../references/platform-truth-registry.md",
    ],
    "geo-llmstxt": [
        "../../references/measurement-capture-template.md",
        "../../references/policy-risk-gate.md",
    ],
    "geo-platform-optimizer": [
        "../../references/platform-truth-registry.md",
        "../../references/measurement-capture-template.md",
        "../../references/private-surface-routing.md",
    ],
    "geo-proposal": [
        "../../references/platform-truth-registry.md",
        "../../references/measurement-capture-template.md",
        "../../references/commerce-audit-worksheet.md",
        "../../references/private-surface-routing.md",
        "../../references/regional-situational-routing.md",
        "../../references/policy-risk-gate.md",
        "../../references/report-template-contract.md",
    ],
    "geo-prospect": [
        "../../references/platform-truth-registry.md",
        "../../references/commerce-audit-worksheet.md",
        "../../references/regional-situational-routing.md",
        "../../references/policy-risk-gate.md",
        "../../references/measurement-capture-template.md",
    ],
    "geo-report": [
        "../../references/report-template-contract.md",
        "../../references/measurement-capture-template.md",
        "../../references/commerce-audit-worksheet.md",
        "../../references/private-surface-routing.md",
        "../../references/regional-situational-routing.md",
        "../../references/policy-risk-gate.md",
    ],
    "geo-report-pdf": [
        "../../references/report-template-contract.md",
    ],
    "geo-schema": [
        "../../references/commerce-readiness.md",
        "../../references/commerce-audit-worksheet.md",
        "../../references/platform-truth-registry.md",
    ],
    "geo-technical": [
        "../../references/measurement-capture-template.md",
        "../../references/policy-risk-gate.md",
        "../../references/private-surface-routing.md",
    ],
}

VERSIONING_PROTOCOL_REQUIRED_PHRASES = [
    "# GEO Versioning Protocol",
    "Tag format: `X.Y.Z` without a leading `v`",
    "Every normal release uses all three numeric parts, for example `0.9.0`, not",
    "This package is still in the three-part `0.Y.Z` phase.",
    "Start the protocol-governed line at `0.1.0`.",
    "Use the three-part form `0.Y.Z` with these rules:",
    "Historical tags `0.0.1` through `0.0.4` predate this protocol and remain",
    "Auxiliary delivery and sharing surfaces such as `docs/`, social-preview images,",
    "are not part of the portable GEO package contract unless a future protocol",
    "`main` is the release line",
    "`codex/<topic>` is the default short-lived working branch shape",
    "When the same project is split into a separate branch, worktree, or folder",
    "the branch boundary represents the variant.",
    "They are not rename requirements by themselves.",
    "validator-enforced required files, required sections, or required",
    "phrases that alter routed invocation, source-order, runtime adaptation,",
    "README or reference wording about auxiliary delivery, sharing, or social",
    "validator changes for auxiliary delivery or share-preview guidance that do",
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
    "target version must match the three-part form X.Y.Z without a leading v",
    "CHANGELOG contains non-empty Unreleased release notes",
    "release decision passed for",
]

LICENSE_REQUIRED_PHRASES = [
    "Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International",
    "SPDX-License-Identifier: CC-BY-NC-ND-4.0",
    "Authors: 김범수, 유수호, 고경만.",
    "Unless otherwise noted, the contents of this repository are licensed under the",
    "You may share the material with proper attribution for noncommercial purposes.",
    "Commercial use is not permitted.",
    "you may not distribute the modified material.",
    "https://creativecommons.org/licenses/by-nc-nd/4.0/",
    "https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode",
]

RUNTIME_ADAPTATION_REQUIRED_PHRASES = [
    "# GEO Runtime Adaptation",
    "Keep one shared portable GEO core in `SKILL.md`.",
    "Do not import the full CogArch multi-tool topology into `geo` just to express",
    "Runtime adaptation must not replace context modes, source-order rules, language",
    "Runtime adaptation may optimize invocation wording, metadata, evidence",
    "## Current Shipped Runtime Surfaces",
    "## First-Use Runtime-Local Onboarding",
    "Codex / OpenAI: `agents/openai.yaml` is bundled today.",
    "no runtime-local surface is bundled in this repository yet",
    "Use that onboarding as the advanced-workflow setup guide for the first advanced",
    "Rerun the same guide when the active runtime or model changes, because",
    "If the runtime cannot surface that trigger or runtime/model identity natively,",
    "The shared portable package must remain usable even when no runtime-local",
    "Do not fork the whole skill package unless `geo` itself later becomes a",
]

PLATFORM_TRUTH_FILES = [
    "skills/geo-crawlers/SKILL.md",
    "skills/geo-platform-optimizer/SKILL.md",
    "skills/geo-report-pdf/SKILL.md",
    "skills/geo-compare/SKILL.md",
    "skills/geo-prospect/SKILL.md",
    "skills/geo-llmstxt/SKILL.md",
]

PLATFORM_TRUTH_REQUIRED_PHRASES = [
    "OAI-SearchBot",
    "Claude-SearchBot",
    "Claude-User",
    "Googlebot",
    "Google Search 포함",
    "확인 필요",
    "heuristic / adoption-dependent",
]

PLATFORM_TRUTH_DISALLOWED_STRINGS = [
    "anthropic-ai",
    "핵심 대상 7개",
    "7개 봇",
    "7 bots",
    "학습+검색",
    "Google-Extended | 이중",
    "Google-Extended 봇: [허용 / 차단]",
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
        "AGENTS.md",
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
        "references/measurement-loop.md",
        "references/commerce-readiness.md",
        "references/platform-truth-registry.md",
        "references/measurement-capture-template.md",
        "references/commerce-audit-worksheet.md",
        "references/private-surface-routing.md",
        "references/regional-situational-routing.md",
        "references/policy-risk-gate.md",
        "references/report-template-contract.md",
        "references/implementation-completion-plan.md",
        "references/user-level-workflow-guide.md",
        "references/execution-skill-matrix.md",
        "references/cogarch-alignment.md",
        "references/sequence-dependent-autopilot.md",
        "references/organic-capability-system.md",
        "references/versioning-protocol.md",
        "scripts/check_geo_release.py",
    ]:
        text = read_text(skill_dir / rel_path)
        for disallowed in DISALLOWED_STRINGS:
            if disallowed in text:
                fail(f"stale alias or script reference found in {rel_path}: {disallowed}")


def ensure_no_absolute_path_leaks(skill_dir: Path) -> None:
    for rel_path in [
        "AGENTS.md",
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
        "references/measurement-loop.md",
        "references/commerce-readiness.md",
        "references/platform-truth-registry.md",
        "references/measurement-capture-template.md",
        "references/commerce-audit-worksheet.md",
        "references/private-surface-routing.md",
        "references/regional-situational-routing.md",
        "references/policy-risk-gate.md",
        "references/report-template-contract.md",
        "references/implementation-completion-plan.md",
        "references/user-level-workflow-guide.md",
        "references/execution-skill-matrix.md",
        "references/cogarch-alignment.md",
        "references/sequence-dependent-autopilot.md",
        "references/organic-capability-system.md",
        "references/versioning-protocol.md",
        "scripts/check_geo_release.py",
    ]:
        text = read_text(skill_dir / rel_path)
        for pattern in PORTABILITY_PATH_PATTERNS:
            if pattern.search(text):
                fail(f"absolute path leak found in {rel_path}: pattern {pattern.pattern}")

    for skill_name in RESTORED_SUBSKILLS:
        rel_path = f"skills/{skill_name}/SKILL.md"
        text = read_text(skill_dir / rel_path)
        for pattern in PORTABILITY_PATH_PATTERNS:
            if pattern.search(text):
                fail(f"absolute path leak found in {rel_path}: pattern {pattern.pattern}")

    for rel_root in CAPABILITY_PACKAGE_DIRS:
        package_root = skill_dir / rel_root
        if not package_root.exists():
            fail(f"required capability package missing: {rel_root}")
        for path in sorted(package_root.rglob("*")):
            if not path.is_file():
                continue
            if path.suffix not in PORTABILITY_SURFACE_SUFFIXES:
                continue
            text = read_text(path)
            rel_path = path.relative_to(skill_dir)
            for pattern in PORTABILITY_PATH_PATTERNS:
                if pattern.search(text):
                    fail(
                        "absolute path leak found in "
                        f"{rel_path}: pattern {pattern.pattern}"
                    )


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
        'default_prompt: "Use geo or $geo. At the first interaction for a new GEO session, ask the user to choose conversation language: Korean or English. Apply that choice only to conversational replies. During the session, accept geo language Korean, geo language English, $geo language Korean, and $geo language English as commands that switch only the conversation language. Keep stored prompts, routing examples, and experiment prompts in English. If goal, scope, working surface, success condition, or evidence target is unclear, ask a short pre-question set first and freeze a clarification packet with goal, scope, surface, success, and evidence target before planning. If the request asks for an advanced execution workflow and this is the first such workflow in the local environment, or the active runtime/model changed, run the advanced-workflow setup guide before promising execution. Confirm skills/*, surface any matching subskill setup or permission requirements, and if native onboarding cannot carry the full guide, fall back to README.md, references/execution-skill-matrix.md, and the matching `skills/geo-*/SKILL.md`. Then choose portable-baseline, user-material, or local-overlay mode, treat VibeWorkers as the default GEO output brand, treat https://vibeworkers.net as the official website for that brand, let an explicit user or confirmed source brand own the output surface when that source owns the deliverable, default outputs to VibeWorkers when no stronger source brand is confirmed, route the GEO request to the smallest confirmed source surface, and delegate execution-intent requests to a matching local subskill only when skills/* is confirmed. Preserve the legal authors as 김범수, 유수호, 고경만. When contributor names are surfaced, render `VibeWorkers 의 컨트리뷰터: 김범수, 유수호, 고경만.`"',
    ]:
        if phrase not in text:
            fail(f"missing phrase in agents/openai.yaml: {phrase}")


def ensure_reference_contract(skill_dir: Path) -> None:
    concept_map = read_text(skill_dir / "references/concept-map.md")
    gate_conditions = read_text(skill_dir / "references/gate-conditions.md")
    experiments = read_text(skill_dir / "references/experiment-scenarios.md")
    runtime_adaptation = read_text(skill_dir / "references/runtime-adaptation.md")
    measurement_loop = read_text(skill_dir / "references/measurement-loop.md")
    commerce_readiness = read_text(skill_dir / "references/commerce-readiness.md")
    platform_truth = read_text(skill_dir / "references/platform-truth-registry.md")
    measurement_capture = read_text(skill_dir / "references/measurement-capture-template.md")
    commerce_audit = read_text(skill_dir / "references/commerce-audit-worksheet.md")
    private_surface = read_text(skill_dir / "references/private-surface-routing.md")
    regional_situational = read_text(skill_dir / "references/regional-situational-routing.md")
    policy_risk = read_text(skill_dir / "references/policy-risk-gate.md")
    report_template = read_text(skill_dir / "references/report-template-contract.md")
    implementation_completion = read_text(skill_dir / "references/implementation-completion-plan.md")
    glossary = read_text(skill_dir / "references/glossary.md")
    execution_matrix = read_text(skill_dir / "references/execution-skill-matrix.md")
    cogarch_alignment = read_text(skill_dir / "references/cogarch-alignment.md")
    sequence_autopilot = read_text(skill_dir / "references/sequence-dependent-autopilot.md")
    organic_capability = read_text(skill_dir / "references/organic-capability-system.md")

    for phrase in [
        "`portable-baseline`",
        "`user-material`",
        "`local-overlay`",
        "`default_output_brand`: `VibeWorkers`",
        "`brand_website`: `https://vibeworkers.net`",
        "`output_brand_rule`: if the user or confirmed source names a stronger brand,",
        "`prompt_language`: English",
        "`conversation_language`: first-session user choice between Korean and English",
        "`conversation_language_commands`: `geo language Korean`",
        "`authors`: 김범수, 유수호, 고경만",
        "`contributors_display_label`: `VibeWorkers 의 컨트리뷰터: 김범수, 유수호, 고경만.`",
        "`execution_overlay_rule`: `skills/*` is a repo-local execution bundle",
        "`measurement_loop_reference`: `references/measurement-loop.md`",
        "`commerce_readiness_reference`: `references/commerce-readiness.md`",
        "`platform_truth_reference`: `references/platform-truth-registry.md`",
        "`measurement_capture_reference`: `references/measurement-capture-template.md`",
        "`commerce_audit_reference`: `references/commerce-audit-worksheet.md`",
        "`private_surface_reference`: `references/private-surface-routing.md`",
        "`regional_situational_reference`: `references/regional-situational-routing.md`",
        "`policy_risk_reference`: `references/policy-risk-gate.md`",
        "`report_template_reference`: `references/report-template-contract.md`",
        "`implementation_completion_reference`: `references/implementation-completion-plan.md`",
        "`sequence_dependent_autopilot_reference`: `references/sequence-dependent-autopilot.md`",
        "`clarification_rule`: if `goal / scope / surface / success / evidence target`",
        "`sequence_dependent_autopilot_rule`: when the user asks for all processes,",
        "Derived outputs should follow source changes, not replace them.",
        "Do not assume a local overlay or hidden workspace path exists.",
        "| clarification packet | minimal pre-plan packet with `goal / scope / surface / success / evidence target`",
        "| advanced-workflow setup guide | `README.md`, `references/execution-skill-matrix.md`, matching",
        "`advanced_workflow_setup_rule`: when an advanced workflow is requested for",
        "Run the advanced-workflow setup guide before promising execution when",
        "| measurement loop reference | `references/measurement-loop.md`",
        "| commerce readiness reference | `references/commerce-readiness.md`",
        "| platform truth registry | `references/platform-truth-registry.md`",
        "| measurement capture template | `references/measurement-capture-template.md`",
        "| commerce audit worksheet | `references/commerce-audit-worksheet.md`",
        "| private surface routing | `references/private-surface-routing.md`",
        "| regional situational routing | `references/regional-situational-routing.md`",
        "| policy risk gate | `references/policy-risk-gate.md`",
        "| report template contract | `references/report-template-contract.md`",
        "| implementation completion plan | `references/implementation-completion-plan.md`",
        "| sequence-dependent autopilot | `references/sequence-dependent-autopilot.md`",
    ]:
        if phrase not in concept_map:
            fail(f"missing concept-map phrase: {phrase}")

    for phrase in [
        "Gate 0: Conversation language selection",
        "Gate 1: GEO-domain trigger",
        "Gate 2: Clarification-first intake",
        "Gate 3: Context mode selection",
        "Gate 6: Derived-output readiness",
        "Gate 7: Evidence closure",
        "Gate 8: Measurement confidence boundary",
        "Gate 9: Commerce/action readiness boundary",
        "Gate 10: Private surface boundary",
        "Gate 11: Regional/situational boundary",
        "Gate 12: Policy risk boundary",
        "Gate 13: Whole-system completion boundary",
        "Gate 14: Sequence-dependent autopilot",
        "packet with `goal / scope / surface / success / evidence target` is locked.",
        "`execution-bundle`",
        "advanced-workflow",
        "runtime or model changed",
        "readiness scores, crawler access, schema validity, or",
        "Product schema alone is treated as commerce readiness",
        "public crawler, public search, private",
        "regional or vertical claims must use a confirmed source pack",
        "robots, terms, privacy, regulated claims, brand claims",
        "`completion_rubric_path_or_inline`",
        "ordered dependency graph",
        "`all_must_passed=true`",
    ]:
        if phrase not in gate_conditions:
            fail(f"missing gate condition phrase: {phrase}")

    scenario_count = len(re.findall(r"^### Scenario", experiments, flags=re.MULTILINE))
    if scenario_count < 8:
        fail("experiment scenarios must include at least 8 scenario blocks")
    for phrase in [
        "Expected mode: `portable-baseline`",
        "Expected default output brand: `VibeWorkers`",
        "Expected brand website: `https://vibeworkers.net`",
        "Expected branding boundary: if no stronger source brand is confirmed, keep",
        "Expected mode: `user-material`",
        "Expected mode: `local-overlay`",
        "Expected lane: `framework-source`",
        "Expected lane: `working-source`",
        "Expected lane: `derived-deliverable`",
        "Expected lane: `execution-bundle`",
        "Expected behavior: ask exactly `Choose conversation language: Korean or English.`",
        "Expected behavior: ask short pre-questions first until `goal / scope / surface / success / evidence target` are locked",
        "Expected behavior: switch conversation replies to English without changing stored prompts",
        "Expected behavior: when contributor names are surfaced, render exactly `VibeWorkers 의 컨트리뷰터: 김범수, 유수호, 고경만.`",
        "Expected boundary: confirm `skills/*` and route to `geo-audit`",
        "Expected behavior: do not pretend the portable baseline alone bundles a live crawler",
        "Expected behavior: run the advanced-workflow setup guide before promising execution",
        "Expected behavior: rerun the advanced-workflow setup guide before execution because runtime-local hints may differ",
        "Expected boundary: classify readiness, heuristic, observed answer, observed citation, referral, and conversion separately",
        "Expected boundary: Product schema alone does not prove commerce readiness",
        "Expected boundary: use `references/platform-truth-registry.md` before implementation advice",
        "Expected boundary: Do not use private evidence to claim public visibility",
        "Expected boundary: regional or vertical claims must use a confirmed source pack",
        "Expected boundary: check robots, terms, privacy, regulated claims, brand claims, and commerce eligibility",
        "Expected boundary: use `references/report-template-contract.md`",
        "Expected boundary: use `references/implementation-completion-plan.md`",
        "Expected boundary: use `references/sequence-dependent-autopilot.md`",
        "Expected behavior: build an ordered dependency graph",
    ]:
        if phrase not in experiments:
            fail(f"missing experiment phrase: {phrase}")

    for phrase in [
        "portable baseline",
        "user-material mode",
        "local overlay",
        "execution-bundle",
        "derived-deliverable",
        "clarification packet",
        "advanced-workflow setup guide",
        "default output brand",
        "brand website",
        "output brand rule",
        "prompt language",
        "conversation language",
        "language command",
        "authors",
        "contributor display label",
        "VibeWorkers",
        "https://vibeworkers.net",
        "platform truth registry",
        "measurement capture template",
        "commerce audit worksheet",
        "private surface routing",
        "regional situational routing",
        "policy risk gate",
        "report template contract",
        "implementation completion plan",
        "readiness_signal",
        "observed_answer",
        "observed_citation",
        "referral_signal",
        "conversion_signal",
        "policy risk",
    ]:
        if phrase not in glossary:
            fail(f"missing glossary phrase: {phrase}")

    for phrase in RUNTIME_ADAPTATION_REQUIRED_PHRASES:
        if phrase not in runtime_adaptation:
            fail(f"missing runtime-adaptation phrase: {phrase}")

    for phrase in EXECUTION_MATRIX_REQUIRED_PHRASES:
        if phrase not in execution_matrix:
            fail(f"missing execution-matrix phrase: {phrase}")

    for phrase in [
        "# GEO Measurement Loop",
        "do not claim measured visibility",
        "`readiness_signal`",
        "`heuristic_signal`",
        "`observed_answer`",
        "`observed_citation`",
        "`referral_signal`",
        "`conversion_signal`",
        "prompt panel",
        "before/after",
        "Treating `llms.txt` as guaranteed ingestion or citation.",
    ]:
        if phrase not in measurement_loop:
            fail(f"missing measurement-loop phrase: {phrase}")

    for phrase in [
        "# GEO Commerce Readiness",
        "Product schema alone does not prove commerce readiness.",
        "OpenAI Commerce",
        "shopping research",
        "merchant listing structured data",
        "Instant Buy",
        "price, availability, shipping, returns",
        "Checkout/action",
        "`catalog_readiness`",
        "`measurement_readiness`",
    ]:
        if phrase not in commerce_readiness:
            fail(f"missing commerce-readiness phrase: {phrase}")

    for phrase in [
        "# GEO Platform Truth Registry",
        "source_url",
        "last_verified",
        "confidence",
        "package_action",
        "OAI-SearchBot",
        "Google-Extended",
        "Claude-SearchBot",
        "Claude-User",
        "확인 필요",
        "heuristic / adoption-dependent",
    ]:
        if phrase not in platform_truth:
            fail(f"missing platform-truth phrase: {phrase}")

    for phrase in [
        "# GEO Measurement Capture Template",
        "Prompt Panel",
        "Run Metadata",
        "Capture Table",
        "Before/After Comparison",
        "evidence_label",
        "observed_citation",
        "conversion_signal",
    ]:
        if phrase not in measurement_capture:
            fail(f"missing measurement-capture phrase: {phrase}")

    for phrase in [
        "# GEO Commerce Audit Worksheet",
        "Product Identity",
        "Schema Readiness",
        "Merchant Facts",
        "Catalog / Feed",
        "Checkout / Action",
        "Measurement Readiness",
        "platform_eligibility_status",
    ]:
        if phrase not in commerce_audit:
            fail(f"missing commerce-audit phrase: {phrase}")

    for phrase in [
        "# GEO Private Surface Routing",
        "public_crawler_surface",
        "private_connector_surface",
        "logged_in_user_surface",
        "user_provided_context_surface",
        "permission profile",
        "Do not use private evidence",
    ]:
        if phrase not in private_surface:
            fail(f"missing private-surface phrase: {phrase}")

    for phrase in [
        "# GEO Regional And Situational Routing",
        "Naver",
        "Kakao",
        "Daum",
        "regulated",
        "new brand",
        "mature brand",
        "requires separate official evidence",
    ]:
        if phrase not in regional_situational:
            fail(f"missing regional-situational phrase: {phrase}")

    for phrase in [
        "# GEO Policy Risk Gate",
        "robots",
        "terms",
        "privacy",
        "regulated claims",
        "brand claims",
        "commerce eligibility",
        "not legal advice",
    ]:
        if phrase not in policy_risk:
            fail(f"missing policy-risk phrase: {phrase}")

    for phrase in [
        "# GEO Report Template Contract",
        "score_type",
        "evidence_label",
        "confidence",
        "measurement_status",
        "commerce_status",
        "private_surface_status",
        "regional_context",
        "policy_risk",
        "Claim boundary ledger",
        "Actor-first handoff",
        "measured facts",
        "interpretation",
        "assumptions",
        "unknowns",
    ]:
        if phrase not in report_template:
            fail(f"missing report-template phrase: {phrase}")

    for phrase in [
        "# GEO Cogarch Alignment Contract",
        "compatibility, not inheritance",
        "without depending on `cogarch`, `~/.cogarch`",
        "Goal -> Rubric -> Iteration -> Score -> Next Action",
        "measured / interpretation / assumption / unknown",
        "owner split",
        "actor-first handoff",
        "portable knowledge packet",
        "The package fails portability if this alignment requires `cogarch`",
    ]:
        if phrase not in cogarch_alignment:
            fail(f"missing cogarch-alignment phrase: {phrase}")

    for phrase in [
        "# GEO Sequence-Dependent Autopilot",
        "guided completion",
        "`전부 해줘`",
        "`전체 진행`",
        "`전체 수행`",
        "`do everything`",
        "`continue until complete`",
        "ordered dependency graph",
        "Execute next unblocked phase",
        "Verify phase",
        "Record ledger",
        "all_must_passed=true",
        "failed_must_queue",
        "Do not require the user to know the names of subskills",
    ]:
        if phrase not in sequence_autopilot:
            fail(f"missing sequence-autopilot phrase: {phrase}")

    for phrase in [
        "# GEO Organic Capability System",
        "`geo` is the single representative system.",
        "The physical folders under `skills/` and `packages/` are ownership and",
        "| Commerce capability | `packages/geo-deep-audit-ecommerce/`",
        "| KR2 capability | `packages/geo-seo-skills-kr2/`",
        "`deep-audit-ecommerce`.",
        "`kr2`.",
        "one evidence ledger and one report contract",
        "Integration takes priority over preserving both reports",
        "Do not upgrade `Readiness` or `Heuristic` to `Measured` unless direct",
        "Do not make `cogarch`, `~/.cogarch`, `OPERATIONS.md`, or hidden session",
        "It must be a single GEO judgment flow:",
        "serve one organic `geo` system",
    ]:
        if phrase not in organic_capability:
            fail(f"missing organic-capability phrase: {phrase}")

    for phrase in [
        "# GEO P2-P13 Implementation Completion Plan",
        "RQ1",
        "RQ13",
        "RQ14",
        "P2-P13 Sequence",
        "P14",
        "completion_judgment",
        "all_must_passed",
        "failed_must_queue",
        "verification set",
    ]:
        if phrase not in implementation_completion:
            fail(f"missing implementation-completion phrase: {phrase}")

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
        for phrase in RESTORED_SUBSKILL_REQUIRED_PHRASES:
            if phrase not in text:
                fail(f"missing standalone subskill phrase in {skill_name}: {phrase}")
        for phrase in SUBSKILL_REFERENCE_REQUIRED.get(skill_name, []):
            if phrase not in text:
                fail(f"missing P2-P13 reference in restored skill {skill_name}: {phrase}")
        for disallowed in RESTORED_SUBSKILL_DISALLOWED_STRINGS:
            if disallowed in text:
                fail(f"hidden dependency leaked into restored skill {skill_name}: {disallowed}")


def ensure_platform_truth_contract(skill_dir: Path) -> None:
    combined = "\n".join(read_text(skill_dir / rel_path) for rel_path in PLATFORM_TRUTH_FILES)

    for phrase in PLATFORM_TRUTH_REQUIRED_PHRASES:
        if phrase not in combined:
            fail(f"missing platform truth phrase: {phrase}")

    for phrase in PLATFORM_TRUTH_DISALLOWED_STRINGS:
        if phrase in combined:
            fail(f"stale platform truth phrase found: {phrase}")


def ensure_capability_validators_pass(skill_dir: Path) -> None:
    for rel_path in CAPABILITY_VALIDATOR_SCRIPTS:
        script_path = skill_dir / rel_path
        if not script_path.exists():
            fail(f"missing capability validator: {rel_path}")

        completed = subprocess.run(
            ["python3", str(script_path)],
            cwd=skill_dir,
            text=True,
            capture_output=True,
            check=False,
        )
        if completed.returncode != 0:
            detail = (completed.stdout + completed.stderr).strip()
            fail(f"capability validator failed ({rel_path}): {detail}")


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
    ensure_platform_truth_contract(skill_dir)
    ensure_capability_validators_pass(skill_dir)

    print("[ok] geo skill package and portable contract are consistent")


if __name__ == "__main__":
    main()
