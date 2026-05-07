# GEO

This README is bilingual: English first, Korean second.
이 README는 영어 먼저, 한국어 다음 순서의 이중언어 문서입니다.

## English

Portable GEO skill package for turning GEO ideas, notes, and working materials
into structured guidance, reusable assets, and optional execution workflows.

### What This Project Is

`geo` is a portable skill package for GEO strategy, teaching-material design,
evidence work, and optional local execution workflows.
It can start from bundled references, but it is designed to work with the
user's real notes, drafts, files, and source materials when they are provided.

### Why It Exists

GEO work often gets split across notes, drafts, evidence documents, reusable
assets, and derived outputs.
This project provides one entrypoint so users can start from the right source,
keep source and output separate, and move from GEO thinking to practical
deliverables without depending on a hidden machine-local workspace.

### What You Can Do

- structure a GEO lecture, workshop, or study flow
- decide which note, draft, or source surface should own a change
- turn source material into checklists, handouts, templates, or evidence notes
- run optional local audit, schema, report, proposal, or technical GEO
  workflows when the execution bundle is available

### How To Use

Stored prompts are written in English.

At the first interaction of a new GEO session, the LLM asks:

```text
Choose conversation language: Korean or English.
```

Use either of these commands to start:

- `geo <request>`
- `$geo <request>`

During the session, switch only the conversation language with:

```text
geo language Korean
geo language English
$geo language Korean
$geo language English
```

When you provide your own notes, files, pasted text, or explicit file paths,
those materials become the working source of truth.
If goal, scope, working surface, success condition, or evidence are still
unclear, GEO asks a short pre-question set first and locks those completion
conditions before planning.
If you do not provide a stronger brand, outputs default to `VibeWorkers.net`.

### Optional Advanced Workflows

When the local execution bundle `skills/*` is present, GEO can route advanced
work such as audit, crawlers, `llms.txt`, schema, compare, report, proposal,
prospect, and technical review workflows.
Each `skills/geo-*` subskill owns its own workflow contract.
The representative `geo` router selects a subskill, but the subskill itself
must remain usable without `cogarch`, hidden global files, or hidden
session-state commands.

### Enable Advanced Workflows

Advanced workflows are available only when the local `skills/*` bundle is part
of your GEO installation or checkout.
If you are using this repository checkout, that bundle is already included.

To make advanced workflows available:

- keep the `skills/` directory together with this package
- verify that subskills such as `skills/geo-audit` and `skills/geo-schema` are
  present
- start through `geo <request>` or `$geo <request>` and ask for a concrete
  audit, crawler, schema, compare, report, proposal, prospect, or technical
  review task
- check the matching subskill when a workflow needs extra tools, network
  access, or export tooling
- treat the matching subskill as the workflow owner for setup, permissions,
  and output details; the top-level `geo` router only routes you there

### Project Docs

- `SKILL.md`: full GEO routing contract
- `references/execution-skill-matrix.md`: advanced execution workflow list

### License

This repository is licensed under `CC BY-ND 4.0`
(`Creative Commons Attribution-NoDerivatives 4.0 International`).

- Authors: 김범수, 유수호, 고경만.
- Repository terms: `LICENSE`
- Canonical deed: <https://creativecommons.org/licenses/by-nd/4.0/>
- Canonical legal code: <https://creativecommons.org/licenses/by-nd/4.0/legalcode>

## 한국어

GEO 아이디어, 노트, 작업 자료를 구조화된 가이드, 재사용 자산, 선택적 실행
workflow로 연결하는 portable GEO skill 패키지입니다.

### 이 프로젝트는 무엇인가

`geo`는 GEO 전략, 교육 자료 설계, 근거 작업, 그리고 선택적인 로컬 실행
workflow를 위한 portable skill 패키지입니다.
bundled reference만으로 시작할 수도 있지만, 사용자의 실제 note, draft, file,
source material이 주어지면 그 자료를 기준으로 동작하도록 설계되어 있습니다.

### 왜 존재하는가

GEO 작업은 note, draft, evidence document, 재사용 asset, derived output으로
쉽게 흩어집니다.
이 프로젝트는 사용자가 올바른 source에서 시작하고, source와 output을
분리하며, 숨겨진 machine-local workspace에 의존하지 않고도 GEO 사고를 실제
deliverable로 이어갈 수 있게 하나의 entrypoint를 제공합니다.

### 사용자가 할 수 있는 일

- GEO 강의, 워크숍, 학습 흐름의 구조 잡기
- 어떤 note, draft, source surface가 수정의 소유권을 가져야 하는지 판단하기
- source material을 checklist, handout, template, evidence note로 바꾸기
- execution bundle이 있을 때 audit, schema, report, proposal, technical GEO
  workflow를 실행하기

### 사용하는 방법

저장된 prompt는 영어로 작성합니다.

새 GEO session의 첫 상호작용에서 LLM은 아래 질문을 합니다.

```text
Choose conversation language: Korean or English.
```

시작 명령은 아래 둘 중 하나를 사용합니다.

- `geo <request>`
- `$geo <request>`

세션 중에는 아래 명령으로 대화 언어만 변경합니다.

```text
geo language Korean
geo language English
$geo language Korean
$geo language English
```

사용자가 자신의 note, file, pasted text, explicit file path를 제공하면 그
자료가 working source of truth가 됩니다.
goal, scope, working surface, success condition, evidence가 아직 불명확하면
GEO는 먼저 짧은 사전 질문으로 완료 조건을 잠근 뒤 계획을 세웁니다.
더 강한 brand를 별도로 주지 않으면 출력 기본 brand는 `VibeWorkers.net`입니다.

### 선택적 고급 Workflow

로컬 실행 번들 `skills/*`가 있으면 audit, crawlers, `llms.txt`, schema,
compare, report, proposal, prospect, technical review 같은 고급 workflow로
라우팅할 수 있습니다.
각 `skills/geo-*` 서브스킬은 자기 workflow 계약을 직접 소유합니다.
대표 `geo` 라우터는 해당 서브스킬로 연결하지만, 서브스킬 자체는
`cogarch`, 숨은 전역 파일, 숨은 세션 상태 명령 없이도 읽고 사용할 수
있어야 합니다.

### 고급 Workflow 준비

고급 workflow는 로컬 `skills/*` 번들이 현재 GEO 설치본 또는 checkout에 함께
있을 때만 사용할 수 있습니다.
이 저장소 checkout을 그대로 사용한다면 그 번들은 이미 포함되어 있습니다.

고급 workflow를 사용할 수 있게 하려면:

- `skills/` 디렉터리를 이 패키지와 함께 유지합니다
- `skills/geo-audit`, `skills/geo-schema` 같은 서브스킬이 실제로 있는지
  확인합니다
- `geo <request>` 또는 `$geo <request>`로 시작한 뒤 audit, crawler,
  schema, compare, report, proposal, prospect, technical review처럼 구체적인
  실행 요청을 합니다
- workflow에 추가 도구, 네트워크 접근, export 도구가 필요하면 해당
  서브스킬 문서를 확인합니다
- setup, permission, output detail은 해당 서브스킬이 직접 소유하고,
  상위 `geo` 라우터는 그 서브스킬로 연결만 한다고 이해합니다

### 프로젝트 문서

- `SKILL.md`: 전체 GEO 라우팅 계약
- `references/execution-skill-matrix.md`: 고급 실행 workflow 목록

### 라이선스

이 저장소는 `CC BY-ND 4.0`
(`Creative Commons Attribution-NoDerivatives 4.0 International`) 라이선스를
사용합니다.

- 저작자: 김범수, 유수호, 고경만.
- 저장소 규약: `LICENSE`
- 정본 deed: <https://creativecommons.org/licenses/by-nd/4.0/>
- 정본 legal code: <https://creativecommons.org/licenses/by-nd/4.0/legalcode>
