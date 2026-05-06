# GEO

This README is bilingual: English first, Korean second.
이 README는 영어 먼저, 한국어 다음 순서의 이중언어 문서입니다.

## English

Portable GEO skill package for routing GEO strategy, teaching-material, and
evidence work across bundled references, user-provided sources, and confirmed
local overlays.

### Entrypoints

- Human entrypoint: `README.md`
- Representative execution surface: `SKILL.md`
- Agent metadata: `agents/openai.yaml`
- Bundled portable references: `references/*.md`
- Validator: `python3 scripts/check_geo_skill.py`

### What This Repository Owns

This repository packages a portable `geo` skill that:

- stays usable even when no local GEO workspace exists
- defaults to bundled references until stronger user material or a confirmed
  local overlay is available
- routes requests across framework, working-source, evidence-note,
  asset-surface, and derived-deliverable lanes
- keeps `Vibeworkers.net` as the default brand unless a stronger user or source
  brand overrides it

### Repository Layout

- `SKILL.md`: canonical routing contract and representative skill surface
- `references/glossary.md`: portable term contract
- `references/concept-map.md`: topology, modes, and routing edges
- `references/gate-conditions.md`: gate-by-gate routing conditions
- `references/experiment-scenarios.md`: positive and negative routing probes
- `agents/openai.yaml`: default activation prompt for the OpenAI agent surface
- `scripts/check_geo_skill.py`: package validator for portability and contract
  consistency

### Command Surface

This package uses one routed entry command surface instead of multiple
subcommands.

- Explicit skill invocation: `geo <request>`
- Explicit skill invocation with skill marker: `$geo <request>`
- Natural-language trigger: a clearly GEO-scoped request may activate the skill
  without the prefix, but explicit invocation wins when routing is ambiguous
- Boundary: build, export, crawl, or deploy work is not implied by the command
  alone; the source surface must still be confirmed first

Examples:

- `geo GEO 강의 구조를 어떻게 짜야 할지 기본 틀부터 잡아줘.`
- `$geo 이 GEO 초안에서 어느 문서가 실제 작업 정본이 되어야 하는지 정리해줘.`

### Validate

Run the targeted validator from the repository root:

```bash
python3 scripts/check_geo_skill.py
```

Expected result:

```text
[ok] geo skill package and portable contract are consistent
```

### License

This repository is licensed under `CC BY-ND 4.0`
(`Creative Commons Attribution-NoDerivatives 4.0 International`).

- Repository terms: `LICENSE`
- Canonical deed: <https://creativecommons.org/licenses/by-nd/4.0/>
- Canonical legal code: <https://creativecommons.org/licenses/by-nd/4.0/legalcode>

## 한국어

이 저장소는 번들 reference, 사용자 제공 source, 확인된 로컬 overlay 사이에서
GEO 전략, 교육 자료, 근거 작업을 라우팅하기 위한 portable GEO skill 패키지입니다.

### 진입점

- 사람용 진입점: `README.md`
- 대표 실행 표면: `SKILL.md`
- 에이전트 메타데이터: `agents/openai.yaml`
- 번들 portable reference: `references/*.md`
- 검증기: `python3 scripts/check_geo_skill.py`

### 이 저장소가 담당하는 범위

이 저장소는 다음 성격의 portable `geo` skill을 패키징합니다.

- 로컬 GEO 워크스페이스가 없어도 사용할 수 있음
- 더 강한 사용자 자료나 확인된 로컬 overlay가 나오기 전까지는 bundled
  reference를 기본값으로 사용함
- 요청을 framework-source, working-source, evidence-note, asset-surface,
  derived-deliverable lane으로 라우팅함
- 더 강한 사용자 또는 source brand가 없으면 기본 브랜드를
  `Vibeworkers.net`으로 유지함

### 저장소 구조

- `SKILL.md`: 정본 라우팅 계약이자 대표 skill 표면
- `references/glossary.md`: portable 용어 계약
- `references/concept-map.md`: topology, mode, routing edge 정의
- `references/gate-conditions.md`: gate 단위 라우팅 조건
- `references/experiment-scenarios.md`: positive / negative routing probe
- `agents/openai.yaml`: OpenAI agent 표면의 기본 activation prompt
- `scripts/check_geo_skill.py`: portability와 계약 일관성을 검증하는 패키지
  validator

### 명령 표면

이 패키지는 여러 하위 명령 대신 하나의 routed entry command surface를
사용합니다.

- 명시적 스킬 호출: `geo <request>`
- 명시적 스킬 호출(스킬 마커): `$geo <request>`
- 자연어 트리거: GEO 범위가 명확하면 prefix 없이도 skill이 활성화될 수
  있지만, 라우팅이 모호할 때는 명시적 호출이 우선함
- 경계: build, export, crawl, deploy 작업은 명령만으로 암시되지 않으며,
  먼저 source surface를 확인해야 함

예시:

- `geo GEO 강의 구조를 어떻게 짜야 할지 기본 틀부터 잡아줘.`
- `$geo 이 GEO 초안에서 어느 문서가 실제 작업 정본이 되어야 하는지 정리해줘.`

### 검증

저장소 루트에서 아래 validator를 실행합니다.

```bash
python3 scripts/check_geo_skill.py
```

예상 결과:

```text
[ok] geo skill package and portable contract are consistent
```

### 라이선스

이 저장소는 `CC BY-ND 4.0`
(`Creative Commons Attribution-NoDerivatives 4.0 International`) 라이선스를
사용합니다.

- 저장소 규약: `LICENSE`
- 정본 deed: <https://creativecommons.org/licenses/by-nd/4.0/>
- 정본 legal code: <https://creativecommons.org/licenses/by-nd/4.0/legalcode>
