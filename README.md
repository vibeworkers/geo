# GEO

This README is bilingual: English first, Korean second.
이 README는 영어 먼저, 한국어 다음 순서의 이중언어 문서입니다.

## English

Portable GEO skill package for routing GEO strategy, teaching-material, and
evidence work across bundled references, user-provided sources, confirmed
local overlays, and a restored local execution bundle under `skills/*`.

VibeWorkers.net 의 컨트리뷰터: 김범수, 유수호, 고경만.

### Purpose

This repository exists to provide one portable `geo` entrypoint for GEO
strategy, teaching-material design, evidence work, and execution routing
without assuming a hidden machine-local workspace.
It should remain usable as a standalone package first, then adopt stronger
user material or a confirmed local overlay when those sources exist.

### Background

GEO work usually spans multiple surfaces at once: reference notes, editable
drafts, validation evidence, reusable assets, and execution tools for audit,
schema, and report work.
Without an explicit router, teams tend to edit the wrong artifact, treat a
derived deliverable as the source of truth, or depend on paths that only exist
on one machine.
This repository separates the shared portable contract in `SKILL.md` from
runtime-specific adaptation in `references/runtime-adaptation.md`, and exposes
the repo-local execution bundle only after it is confirmed.

### Core Capabilities

- portable-baseline routing from bundled references when no stronger source is
  available
- source-order protection across bundled references, user material, local
  overlays, execution overlays, and derived outputs
- working-lane classification across framework-source, working-source,
  evidence-note, asset-surface, execution-bundle, and derived-deliverable
- restored execution workflows for audit, brand-mentions, citability, compare,
  content, crawlers, `llms.txt`, platform, proposal, prospect, report, PDF,
  schema, and technical GEO work
- bilingual operator-facing documentation while stored prompts and routing
  examples stay in English
- release governance that keeps `README.md`, `CHANGELOG.md`, validators, and
  the release gate aligned

### Typical Use Cases

- structure a GEO lecture, workshop, or study flow from the foundation
- decide which GEO note, draft, or source surface should own a change
- turn source material into checklists, handouts, templates, or evidence notes
- run a repo-local GEO audit, schema, crawler, report, or proposal workflow
  only after `skills/*` is confirmed

### Entrypoints

- Human entrypoint: `README.md`
- Representative execution surface: `SKILL.md`
- Agent metadata: `agents/openai.yaml`
- Runtime adaptation reference: `references/runtime-adaptation.md`
- Versioning protocol: `references/versioning-protocol.md`
- Release history: `CHANGELOG.md`
- Bundled portable references: `references/*.md`
- Restored local execution bundle: `skills/*`
- Validator: `python3 scripts/check_geo_skill.py`
- Release gate: `python3 scripts/check_geo_release.py <target-version>`

### What This Repository Owns

This repository packages a portable `geo` skill that:

- stays usable even when no local GEO workspace exists
- defaults to bundled references until stronger user material or a confirmed
  local overlay is available
- routes requests across framework, working-source, evidence-note,
  asset-surface, execution-bundle, and derived-deliverable lanes
- keeps one shared portable core plus a separate runtime-adaptation contract
  for Codex, Claude, and Gemini
- restores 14 repo-local execution subskills for audit, crawler, compare,
  schema, report, proposal, and prospect workflows
- keeps `VibeWorkers.net` as the default brand unless a stronger user or source
  brand overrides it
- renders contributor names as `VibeWorkers.net 의 컨트리뷰터: 김범수, 유수호, 고경만.`
  when contributor provenance is surfaced
- keeps stored prompts, activation prompts, routing examples, and experiment
  prompts in English
- asks the user to choose Korean or English at the first interaction of a new
  GEO session, and applies that choice only to conversational replies

### Language Policy

Stored prompts are written in English.

At the first interaction of a new GEO session, the LLM asks:

```text
Choose conversation language: Korean or English.
```

The selected language applies only to conversation with the LLM. It does not
change stored prompts, routing examples, source material, code, schema snippets,
or user-provided evidence.

During the session, switch only the conversation language with:

```text
geo language Korean
geo language English
$geo language Korean
$geo language English
```

### Repository Layout

- `SKILL.md`: canonical routing contract and representative skill surface
- `CHANGELOG.md`: release history keyed by git tag
- `references/glossary.md`: portable term contract
- `references/concept-map.md`: topology, modes, and routing edges
- `references/gate-conditions.md`: gate-by-gate routing conditions
- `references/experiment-scenarios.md`: positive and negative routing probes
- `references/runtime-adaptation.md`: Codex, Claude, and Gemini adaptation
  guidance without forking the shared GEO contract
- `references/execution-skill-matrix.md`: restored execution subskill matrix
- `references/versioning-protocol.md`: branch, tag, changelog, and version bump rules
- `skills/*`: restored local execution bundle delegated by `SKILL.md`
- `agents/openai.yaml`: default activation prompt for the OpenAI agent surface
- `scripts/check_geo_skill.py`: package validator for portability and contract
  consistency and execution bundle completeness
- `scripts/check_geo_release.py`: release-decision gate for target-version
  approval

### Command Surface

This package uses one routed entry command surface instead of multiple
subcommands.

- Explicit skill invocation: `geo <request>`
- Explicit skill invocation with skill marker: `$geo <request>`
- Mid-session conversation language switch: `geo language Korean`
- Mid-session conversation language switch: `geo language English`
- Mid-session conversation language switch with skill marker: `$geo language Korean`
- Mid-session conversation language switch with skill marker: `$geo language English`
- Natural-language trigger: a clearly GEO-scoped request may activate the skill
  without the prefix, but explicit invocation wins when routing is ambiguous
- Delegation: audit, schema, compare, report, proposal, and crawler requests
  route to `skills/*` only after the local execution bundle is confirmed
- Boundary: build, export, crawl, or deploy work is not implied by the
  portable baseline alone; the source surface must still be confirmed first

Examples:

- `geo How should I structure a GEO lecture from the foundation?`
- `$geo Review this GEO draft and identify the working source of truth.`

### Versioning and Release

This repository versions the portable GEO package as one public contract
surface.
The canonical rules live in `references/versioning-protocol.md`, and the
release history lives in `CHANGELOG.md`.

High-level rules:

- Tag format: `X.Y.Z` without a leading `v`
- `main` is the release line; use short-lived working branches such as
  `codex/<topic>` for non-trivial changes
- While the package is pre-`1.0.0`, use `0.Y.Z`: bump `Z` for backward-
  compatible fixes and clarifications, bump `Y` when the public package
  contract changes
- Historical tags `0.0.1` through `0.0.4` predate the formal protocol and
  remain immutable
- New release tags should be annotated tags
- When a release-impacting entrypoint or package-contract surface changes,
  refresh `README.md` in the same change set because it is the human entrypoint
- A release decision is valid only if
  `python3 scripts/check_geo_release.py <target-version>` passes; there are no
  exceptions

### Validate

Run the targeted validator from the repository root:

```bash
python3 scripts/check_geo_skill.py
```

Expected result:

```text
[ok] geo skill package and portable contract are consistent
```

Before creating a release tag, update `CHANGELOG.md` and confirm the rules in
`references/versioning-protocol.md`.
If the release-impacting change touched entrypoints, defaults, required
references/scripts, or other human-facing contract surfaces, refresh
`README.md` in the same change set before running the release gate.
Use `python3 scripts/check_geo_release.py <target-version>` as the final
release-decision gate.

To validate the restored execution subskills individually:

```bash
for d in skills/*; do skills-ref validate "$d"; done
```

### License

This repository is licensed under `CC BY-ND 4.0`
(`Creative Commons Attribution-NoDerivatives 4.0 International`).

- Repository terms: `LICENSE`
- Canonical deed: <https://creativecommons.org/licenses/by-nd/4.0/>
- Canonical legal code: <https://creativecommons.org/licenses/by-nd/4.0/legalcode>

## 한국어

이 저장소는 번들 reference, 사용자 제공 source, 확인된 로컬 overlay 사이에서
GEO 전략, 교육 자료, 근거 작업을 라우팅하기 위한 portable GEO skill
패키지이며, `skills/*` 아래 복원된 로컬 실행 번들을 함께 제공합니다.

VibeWorkers.net 의 컨트리뷰터: 김범수, 유수호, 고경만.

### 목적

이 저장소는 숨겨진 machine-local workspace를 가정하지 않고도 GEO 전략, 교육
자료 설계, 근거 작업, 실행 라우팅을 처리할 수 있는 하나의 portable `geo`
진입점을 제공하기 위해 존재합니다.
기본적으로는 standalone package로 바로 쓸 수 있어야 하고, 더 강한 사용자 자료
또는 확인된 로컬 overlay가 있을 때만 그 표면을 받아들여야 합니다.

### 배경

GEO 작업은 보통 reference note, 편집 가능한 draft, validation evidence,
재사용 asset, audit/schema/report용 실행 도구처럼 여러 표면을 동시에
가로지릅니다.
명시적인 router가 없으면 팀은 잘못된 산출물을 수정하거나, derived deliverable을
source of truth처럼 취급하거나, 한 대의 머신에만 있는 경로에 의존하게 됩니다.
이 저장소는 shared portable contract를 `SKILL.md`에 두고, runtime-specific
adaptation은 `references/runtime-adaptation.md`로 분리하며, repo-local 실행
번들은 실제로 확인된 경우에만 노출합니다.

### 핵심 기능

- 더 강한 source가 없을 때 bundled reference를 기준으로 동작하는
  portable-baseline routing
- bundled reference, user material, local overlay, execution overlay,
  derived output 사이의 source-order 보호
- framework-source, working-source, evidence-note, asset-surface,
  execution-bundle, derived-deliverable로 나누는 작업 lane 분류
- audit, brand-mentions, citability, compare, content, crawlers, `llms.txt`,
  platform, proposal, prospect, report, PDF, schema, technical GEO 작업을
  위한 복원된 실행 workflow
- 저장된 prompt와 routing example은 영어로 유지하면서 operator-facing 문서는
  이중언어로 제공
- `README.md`, `CHANGELOG.md`, validator, release gate를 함께 맞추는 릴리스
  거버넌스

### 대표 사용 예시

- GEO 강의, 워크숍, 학습 흐름의 기초 구조를 잡기
- 어떤 GEO note, draft, source surface가 수정의 소유권을 가져야 하는지 판단하기
- source material을 checklist, handout, template, evidence note로 바꾸기
- `skills/*`가 확인된 뒤에만 repo-local GEO audit, schema, crawler, report,
  proposal workflow를 실행하기

### 진입점

- 사람용 진입점: `README.md`
- 대표 실행 표면: `SKILL.md`
- 에이전트 메타데이터: `agents/openai.yaml`
- runtime adaptation reference: `references/runtime-adaptation.md`
- 버전 관리 프로토콜: `references/versioning-protocol.md`
- 릴리스 이력: `CHANGELOG.md`
- 번들 portable reference: `references/*.md`
- 복원된 로컬 실행 번들: `skills/*`
- 검증기: `python3 scripts/check_geo_skill.py`
- 릴리스 게이트: `python3 scripts/check_geo_release.py <target-version>`

### 이 저장소가 담당하는 범위

이 저장소는 다음 성격의 portable `geo` skill을 패키징합니다.

- 로컬 GEO 워크스페이스가 없어도 사용할 수 있음
- 더 강한 사용자 자료나 확인된 로컬 overlay가 나오기 전까지는 bundled
  reference를 기본값으로 사용함
- 요청을 framework-source, working-source, evidence-note, asset-surface,
  execution-bundle, derived-deliverable lane으로 라우팅함
- Codex, Claude, Gemini별 adapt는 분리하되 shared portable core는 하나로 유지함
- audit, crawler, compare, schema, report, proposal, prospect workflow를 위한
  14개 로컬 실행 스킬을 복원함
- 더 강한 사용자 또는 source brand가 없으면 기본 브랜드를
  `VibeWorkers.net`으로 유지함
- 컨트리뷰터 provenance를 노출할 때는
  `VibeWorkers.net 의 컨트리뷰터: 김범수, 유수호, 고경만.` 형식으로 표기함
- 저장된 prompt, activation prompt, routing example, experiment prompt는
  영어로 유지함
- 새 GEO session의 첫 상호작용에서 Korean 또는 English 중 대화 언어를
  선택하게 하며, 그 선택은 LLM과의 대화에만 적용함

### 언어 정책

저장된 prompt는 영어로 작성합니다.

새 GEO session의 첫 상호작용에서 LLM은 아래 질문을 합니다.

```text
Choose conversation language: Korean or English.
```

선택한 언어는 LLM과의 대화에만 적용됩니다. 저장된 prompt, routing
example, source material, code, schema snippet, 사용자 제공 evidence에는
적용하지 않습니다.

세션 중에는 아래 명령으로 대화 언어만 변경합니다.

```text
geo language Korean
geo language English
$geo language Korean
$geo language English
```

### 저장소 구조

- `SKILL.md`: 정본 라우팅 계약이자 대표 skill 표면
- `CHANGELOG.md`: git tag 기준 릴리스 이력
- `references/glossary.md`: portable 용어 계약
- `references/concept-map.md`: topology, mode, routing edge 정의
- `references/gate-conditions.md`: gate 단위 라우팅 조건
- `references/experiment-scenarios.md`: positive / negative routing probe
- `references/runtime-adaptation.md`: shared GEO 계약을 바꾸지 않는
  Codex, Claude, Gemini adapt 가이드
- `references/execution-skill-matrix.md`: 복원된 실행 스킬 매트릭스
- `references/versioning-protocol.md`: 브랜치, 태그, changelog, 버전 bump 규칙
- `skills/*`: `SKILL.md`가 위임하는 로컬 실행 번들
- `agents/openai.yaml`: OpenAI agent 표면의 기본 activation prompt
- `scripts/check_geo_skill.py`: portability와 계약 일관성을 검증하는 패키지
  validator이자 실행 번들 완결성 점검기
- `scripts/check_geo_release.py`: target version 승인용 release-decision gate

### 명령 표면

이 패키지는 여러 하위 명령 대신 하나의 routed entry command surface를
사용합니다.

- 명시적 스킬 호출: `geo <request>`
- 명시적 스킬 호출(스킬 마커): `$geo <request>`
- 세션 중 대화 언어 변경: `geo language Korean`
- 세션 중 대화 언어 변경: `geo language English`
- 스킬 마커가 있는 세션 중 대화 언어 변경: `$geo language Korean`
- 스킬 마커가 있는 세션 중 대화 언어 변경: `$geo language English`
- 자연어 트리거: GEO 범위가 명확하면 prefix 없이도 skill이 활성화될 수
  있지만, 라우팅이 모호할 때는 명시적 호출이 우선함
- 위임: audit, schema, compare, report, proposal, crawler 요청은 로컬 실행
  번들이 확인된 경우에만 `skills/*`로 라우팅함
- 경계: build, export, crawl, deploy 작업은 portable baseline만으로
  암시되지 않으며, 먼저 source surface를 확인해야 함

예시:

- `geo How should I structure a GEO lecture from the foundation?`
- `$geo Review this GEO draft and identify the working source of truth.`

### 버전 관리와 릴리스

이 저장소는 portable GEO package 전체를 하나의 public contract surface로
버전 관리합니다.
정본 규칙은 `references/versioning-protocol.md`, 릴리스 이력은
`CHANGELOG.md`에 둡니다.

핵심 규칙:

- 태그 형식은 앞에 `v`를 붙이지 않는 `X.Y.Z`
- `main`을 릴리스 라인으로 두고, 의미 있는 변경은 `codex/<topic>` 같은
  짧은 작업 브랜치에서 준비
- `1.0.0` 이전에는 `0.Y.Z`를 사용하고, 하위 호환되는 수정/명확화는 `Z`,
  공개 package 계약 변경은 `Y`를 올림
- 기존 `0.0.1`부터 `0.0.4`까지의 태그는 정식 프로토콜 이전 이력이므로
  그대로 보존
- 새 릴리스 태그는 annotated tag를 기본값으로 사용
- 공개 package 계약 또는 entrypoint가 바뀌면 사람용 진입점인 `README.md`를
  같은 change set에서 함께 갱신
- 릴리스 판단은 반드시
  `python3 scripts/check_geo_release.py <target-version>` 통과를 기준으로
  하며 예외를 두지 않음

### 검증

저장소 루트에서 아래 validator를 실행합니다.

```bash
python3 scripts/check_geo_skill.py
```

예상 결과:

```text
[ok] geo skill package and portable contract are consistent
```

릴리스 태그를 만들기 전에는 `CHANGELOG.md`를 갱신하고
`references/versioning-protocol.md` 규칙과 함께 검증합니다.
entrypoint, 기본 동작, required reference/script 같은 사람 읽기용 계약이
바뀐 패스라면 release gate를 돌리기 전에 같은 change set에서 `README.md`도
함께 갱신합니다.
최종 릴리스 판단 게이트는
`python3 scripts/check_geo_release.py <target-version>`입니다.

복원된 실행 스킬을 개별 검증하려면:

```bash
for d in skills/*; do skills-ref validate "$d"; done
```

### 라이선스

이 저장소는 `CC BY-ND 4.0`
(`Creative Commons Attribution-NoDerivatives 4.0 International`) 라이선스를
사용합니다.

- 저작자: 김범수, 유수호, 고경만.
- 저장소 규약: `LICENSE`
- 정본 deed: <https://creativecommons.org/licenses/by-nd/4.0/>
- 정본 legal code: <https://creativecommons.org/licenses/by-nd/4.0/legalcode>
