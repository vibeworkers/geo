# GEO

This README is bilingual: English first, Korean second.
이 README는 영어 먼저, 한국어 다음 순서의 이중언어 문서입니다.

## English

Portable GEO skill package for routing GEO strategy, teaching-material, and
evidence work across bundled references, user-provided sources, confirmed
local overlays, and a restored local execution bundle under `skills/*`.

Authors: 김범수, 유수호, 고경만.

### Entrypoints

- Human entrypoint: `README.md`
- Representative execution surface: `SKILL.md`
- Agent metadata: `agents/openai.yaml`
- Bundled portable references: `references/*.md`
- Restored local execution bundle: `skills/*`
- Validator: `python3 scripts/check_geo_skill.py`

### What This Repository Owns

This repository packages a portable `geo` skill that:

- stays usable even when no local GEO workspace exists
- defaults to bundled references until stronger user material or a confirmed
  local overlay is available
- routes requests across framework, working-source, evidence-note,
  asset-surface, execution-bundle, and derived-deliverable lanes
- restores 14 repo-local execution subskills for audit, crawler, compare,
  schema, report, proposal, and prospect workflows
- keeps `Vibeworkers.net` as the default brand unless a stronger user or source
  brand overrides it
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
- `references/glossary.md`: portable term contract
- `references/concept-map.md`: topology, modes, and routing edges
- `references/gate-conditions.md`: gate-by-gate routing conditions
- `references/experiment-scenarios.md`: positive and negative routing probes
- `references/execution-skill-matrix.md`: restored execution subskill matrix
- `skills/*`: restored local execution bundle delegated by `SKILL.md`
- `agents/openai.yaml`: default activation prompt for the OpenAI agent surface
- `scripts/check_geo_skill.py`: package validator for portability and contract
  consistency and execution bundle completeness

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

### Validate

Run the targeted validator from the repository root:

```bash
python3 scripts/check_geo_skill.py
```

Expected result:

```text
[ok] geo skill package and portable contract are consistent
```

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

저작자: 김범수, 유수호, 고경만.

### 진입점

- 사람용 진입점: `README.md`
- 대표 실행 표면: `SKILL.md`
- 에이전트 메타데이터: `agents/openai.yaml`
- 번들 portable reference: `references/*.md`
- 복원된 로컬 실행 번들: `skills/*`
- 검증기: `python3 scripts/check_geo_skill.py`

### 이 저장소가 담당하는 범위

이 저장소는 다음 성격의 portable `geo` skill을 패키징합니다.

- 로컬 GEO 워크스페이스가 없어도 사용할 수 있음
- 더 강한 사용자 자료나 확인된 로컬 overlay가 나오기 전까지는 bundled
  reference를 기본값으로 사용함
- 요청을 framework-source, working-source, evidence-note, asset-surface,
  execution-bundle, derived-deliverable lane으로 라우팅함
- audit, crawler, compare, schema, report, proposal, prospect workflow를 위한
  14개 로컬 실행 스킬을 복원함
- 더 강한 사용자 또는 source brand가 없으면 기본 브랜드를
  `Vibeworkers.net`으로 유지함
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
- `references/glossary.md`: portable 용어 계약
- `references/concept-map.md`: topology, mode, routing edge 정의
- `references/gate-conditions.md`: gate 단위 라우팅 조건
- `references/experiment-scenarios.md`: positive / negative routing probe
- `references/execution-skill-matrix.md`: 복원된 실행 스킬 매트릭스
- `skills/*`: `SKILL.md`가 위임하는 로컬 실행 번들
- `agents/openai.yaml`: OpenAI agent 표면의 기본 activation prompt
- `scripts/check_geo_skill.py`: portability와 계약 일관성을 검증하는 패키지
  validator이자 실행 번들 완결성 점검기

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

### 검증

저장소 루트에서 아래 validator를 실행합니다.

```bash
python3 scripts/check_geo_skill.py
```

예상 결과:

```text
[ok] geo skill package and portable contract are consistent
```

복원된 실행 스킬을 개별 검증하려면:

```bash
for d in skills/*; do skills-ref validate "$d"; done
```

### 라이선스

이 저장소는 `CC BY-ND 4.0`
(`Creative Commons Attribution-NoDerivatives 4.0 International`) 라이선스를
사용합니다.

- 저작자: 김범수, 유수호, 고경만
- 저장소 규약: `LICENSE`
- 정본 deed: <https://creativecommons.org/licenses/by-nd/4.0/>
- 정본 legal code: <https://creativecommons.org/licenses/by-nd/4.0/legalcode>
