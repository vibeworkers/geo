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

### Installation

Portable baseline installation:

1. Install this package in a supported skill root, or keep this repository
   checkout intact as one package.
2. Keep `SKILL.md`, `README.md`, `agents/`, `references/`, `scripts/`, and
   `LICENSE` together.
3. Run `python3 scripts/check_geo_skill.py` to verify that the package is
   consistent.
4. Start the skill with `geo <request>` or `$geo <request>`.

Advanced workflow installation:

1. Keep the repo-owned `skills/` directory in the same checkout or
   installation.
2. Confirm that subskills such as `skills/geo-audit` and `skills/geo-schema`
   are present.
3. Read the matching `skills/geo-*/SKILL.md` when a workflow needs extra
   tools, network access, or export support.
4. If you are using this repository checkout, that bundle is already included.

### Runtime Compatibility

`geo` uses one shared `geo <request>` or `$geo <request>` contract across
Codex/ChatGPT, Claude, and Gemini.
This repository currently ships native runtime metadata only for Codex /
OpenAI in `agents/openai.yaml`.
Claude and Gemini users should follow the shared GEO contract in this
`README.md` and `SKILL.md`; if a runtime-local surface is added later, it may
run the same advanced-workflow setup guide with runtime-local first-use
wording, installation hints, or response packaging only.
Automatic runtime-local setup guidance is possible only when that runtime
exposes a native metadata, extension, or skill slot and can surface the active
runtime or model identity.
See `references/runtime-adaptation.md` for current runtime-specific
boundaries.

### Feature Guide

Core router capabilities:

| Capability | What it does | When to use | How to start |
| --- | --- | --- | --- |
| Strategy and learning design | turns raw GEO ideas into lecture, workshop, or study structure | when you have a teaching goal, agenda, or note set but no clear flow yet | `geo design a 90-minute GEO workshop for B2B marketers using these notes.` |
| Source ownership and planning | decides which note, draft, file, or report should own a change | when GEO material is scattered and you need one working surface before editing | `geo decide whether this schema guidance belongs in this brief or this report.` |
| Asset generation | turns source material into checklists, handouts, templates, and evidence notes | when you already have material but need a reusable deliverable | `geo turn these notes into a GEO audit checklist.` |
| Clarification-first intake | asks short pre-questions and freezes goal, scope, surface, success, and evidence target before planning | when the request is broad, ambiguous, or underspecified | `geo improve GEO for this brand.` and answer the follow-up intake questions |

Advanced execution workflows available with `skills/*`:

| Workflow | What it does | When to use | How to start |
| --- | --- | --- | --- |
| `geo-audit` | runs a full GEO + SEO audit across crawler, content, citability, technical, and platform signals | when you need a broad baseline review of a site or property | `geo audit https://example.com for GEO and AI visibility.` |
| `geo-brand-mentions` | reviews external brand mention visibility across the web and AI-visible sources | when you need to understand whether a brand is being surfaced and cited | `geo review brand mentions for Brand X in AI-visible sources.` |
| `geo-citability` | evaluates whether pages are answer-ready and citation-friendly | when inclusion in AI answers matters more than raw traffic alone | `geo assess citability for these product and docs pages.` |
| `geo-compare` | compares GEO gaps against competitors | when prioritization depends on a competitor benchmark | `geo compare example.com with competitor.com for GEO gaps.` |
| `geo-content` | reviews content quality, trust, and E-E-A-T signals | when content exists but depth, authority, or answer quality is weak | `geo review content quality and E-E-A-T for these pages.` |
| `geo-crawlers` | checks `robots.txt`, bot access, `llms.txt`, and crawlability | when crawler access or indexing rules may be blocking visibility | `geo check crawler access, robots.txt, and llms.txt for example.com.` |
| `geo-llmstxt` | audits or drafts `llms.txt` guidance | when a site needs explicit LLM-facing crawling guidance | `geo create an llms.txt recommendation for example.com.` |
| `geo-platform-optimizer` | reviews visibility across Google AI Overviews, Perplexity, ChatGPT, Copilot, and Grok | when you want platform-specific GEO exposure guidance | `geo review how this brand shows up across ChatGPT, Perplexity, and Google AI Overviews.` |
| `geo-proposal` | turns findings into a scoped proposal or remediation plan | when audit work must become an actionable roadmap | `geo draft a 6-week proposal from these GEO findings.` |
| `geo-prospect` | runs a lightweight discovery scan for sales or consulting | when you need a fast first-pass prospect review before deeper work | `geo run a prospect scan for example.com.` |
| `geo-report` | combines multiple findings into one report | when separate GEO findings need executive synthesis | `geo combine these crawler, schema, and technical findings into one report.` |
| `geo-report-pdf` | packages markdown for PDF delivery | when client delivery needs print-oriented formatting | `geo package this GEO report for PDF delivery.` |
| `geo-schema` | generates or validates JSON-LD schema | when a page needs schema markup or schema correction | `geo create JSON-LD for this product page.` |
| `geo-technical` | diagnoses technical SEO and implementation risks | when rendering, performance, architecture, or indexing issues block GEO | `geo run a technical GEO review for example.com.` |

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

Choose the closest capability or workflow from the feature guide, then phrase
the request directly in one sentence or one short packet with your materials.

When you provide your own notes, files, pasted text, or explicit file paths,
those materials become the working source of truth.
If goal, scope, working surface, success condition, or evidence target are
still unclear, GEO asks a short pre-question set first and locks those
completion conditions before planning.
If you do not provide a stronger brand, outputs default to `VibeWorkers.net`.

### Optional Advanced Workflows

When the local execution bundle `skills/*` is present, GEO can route advanced
work such as audit, crawlers, `llms.txt`, schema, compare, report, proposal,
prospect, and technical review workflows.
Each `skills/geo-*` subskill owns its own workflow contract.
The representative `geo` router selects a subskill, but you should be able to
read and use that subskill directly from the files included in this package.

### Enable Advanced Workflows

Advanced workflows are available only when the local `skills/*` bundle is part
of your GEO installation or checkout.
If you are using this repository checkout, that bundle is already included.
Think of advanced-workflow setup as the getting-started guide for this
environment.
When an advanced workflow is requested for the first time in a local
environment, GEO may walk through this guide before it starts the workflow.
If the active runtime or model changes, GEO may walk through the same guide
again because setup hints, permissions, or export steps can differ.
Some runtimes can show this guide automatically. Otherwise, follow it manually
here, in
`references/execution-skill-matrix.md`, and in the matching
`skills/geo-*/SKILL.md`.

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

### Advanced Workflow Troubleshooting

If advanced workflows are not available or do not start as expected:

- verify that `skills/` is present in the same checkout or installation as this
  package
- if you copied only `README.md` and `SKILL.md`, reinstall from a GEO checkout
  or package that also includes `skills/*`
- if you are unsure which workflow to use, start with a plain request through
  `geo <request>` or `$geo <request>` and let the router choose the matching
  subskill
- if GEO asks clarification questions first, answer them before expecting an
  audit, schema, report, or other execution workflow to start
- if you switched to a different runtime or model, rerun the setup guide before
  expecting the same workflow to continue with unchanged hints or permissions
- if the matching subskill needs tools, network access, credentials, or export
  steps, open that subskill's `SKILL.md` and follow its local contract
- if your runtime does not provide automatic setup-guide onboarding, use this
  `README.md`, `references/execution-skill-matrix.md`, and the matching
  `skills/geo-*/SKILL.md` directly; you should not need any separate hidden
  global setup or a command from an earlier session just to start

### Project Docs

- `README.md`: project introduction, installation, and feature guide
- `SKILL.md`: full GEO routing contract
- `references/runtime-adaptation.md`: runtime compatibility and per-runtime boundaries
- `references/execution-skill-matrix.md`: advanced execution workflow list
- `skills/geo-*/SKILL.md`: workflow-specific setup, permissions, and outputs

### Package Provenance

This package was created with a private `generateSkill` workflow derived from
the public Skill Creator skill.
The private creator workflow is not included in this repository; this
repository ships the resulting GEO package and its user-facing docs.

### License

This repository is licensed under `CC BY-NC-ND 4.0`
(`Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International`).

- Authors: 김범수, 유수호, 고경만.
- See `LICENSE` for repository terms.
- Canonical deed: <https://creativecommons.org/licenses/by-nc-nd/4.0/>
- Canonical legal code: <https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode>

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

### 설치

Portable baseline 설치:

1. 이 패키지를 지원되는 skill root에 설치하거나, 이 저장소 checkout 전체를
   하나의 패키지로 유지합니다.
2. `SKILL.md`, `README.md`, `agents/`, `references/`, `scripts/`,
   `LICENSE`를 함께 유지합니다.
3. `python3 scripts/check_geo_skill.py`를 실행해 패키지 정합성을
   확인합니다.
4. `geo <request>` 또는 `$geo <request>`로 시작합니다.

Advanced workflow 설치:

1. repo 소유 `skills/` 디렉터리를 같은 checkout 또는 installation 안에
   함께 둡니다.
2. `skills/geo-audit`, `skills/geo-schema` 같은 서브스킬이 실제로 있는지
   확인합니다.
3. workflow에 추가 도구, 네트워크 접근, export 지원이 필요하면 해당
   `skills/geo-*/SKILL.md`를 읽습니다.
4. 이 저장소 checkout을 그대로 사용한다면 그 번들은 이미 포함되어
   있습니다.

### 런타임 호환성

`geo`는 Codex/ChatGPT, Claude, Gemini에서 공통 `geo <request>` 또는
`$geo <request>` 계약으로 사용합니다.
현재 이 저장소는 Codex / OpenAI용 native runtime metadata만
`agents/openai.yaml`로 포함합니다.
Claude와 Gemini 사용자는 지금은 이 `README.md`와 `SKILL.md`의 공통 GEO
계약을 따라 사용하고, 나중에 runtime-local surface가 추가되더라도 같은 고급
workflow setup guide를 런타임별 첫 실행 문구, 설치 힌트, 응답 포장 수준에서만
다르게 얹을 수 있습니다.
자동 런타임별 setup guide는 해당 런타임이 native metadata, extension,
skill slot을 제공하고 현재 활성 런타임 또는 모델 정체성을 드러낼 수 있을 때만
가능합니다.
현재 런타임별 경계는 `references/runtime-adaptation.md`를 참고하세요.

### 기능 가이드

기본 라우터 기능:

| 기능 | 무엇을 하는가 | 언제 쓰는가 | 어떻게 시작하는가 |
| --- | --- | --- | --- |
| 전략 및 학습 설계 | GEO 아이디어를 강의, 워크숍, 학습 구조로 정리합니다 | 교육 목표, 아젠다, 노트는 있지만 흐름이 아직 없을 때 | `geo design a 90-minute GEO workshop for B2B marketers using these notes.` |
| source 소유권 판단과 계획 | 어떤 note, draft, file, report가 수정의 정본이 될지 정합니다 | GEO 자료가 흩어져 있어 먼저 작업 surface를 고정해야 할 때 | `geo decide whether this schema guidance belongs in this brief or this report.` |
| 재사용 자산 생성 | source material을 checklist, handout, template, evidence note로 바꿉니다 | 원자료는 있지만 재사용 가능한 deliverable이 아직 없을 때 | `geo turn these notes into a GEO audit checklist.` |
| 사전 질문 intake | 계획 전에 goal, scope, surface, success, evidence target을 짧게 잠급니다 | 요청이 넓거나 모호하거나 누락이 있을 때 | `geo improve GEO for this brand.`라고 시작한 뒤 후속 intake 질문에 답합니다 |

`skills/*`가 있을 때 사용할 수 있는 고급 실행 workflow:

| Workflow | 무엇을 하는가 | 언제 쓰는가 | 어떻게 시작하는가 |
| --- | --- | --- | --- |
| `geo-audit` | crawler, content, citability, technical, platform 신호를 함께 보는 전체 GEO + SEO 감사 | 사이트나 자산의 전체 상태를 한 번에 점검해야 할 때 | `geo audit https://example.com for GEO and AI visibility.` |
| `geo-brand-mentions` | 웹과 AI 노출 source에서 브랜드 언급 가시성을 점검합니다 | 브랜드가 실제로 얼마나 노출되고 인용되는지 알고 싶을 때 | `geo review brand mentions for Brand X in AI-visible sources.` |
| `geo-citability` | 페이지가 답변용 source로 인용되기 쉬운지 평가합니다 | 단순 트래픽보다 AI 답변 내 포함 가능성이 중요할 때 | `geo assess citability for these product and docs pages.` |
| `geo-compare` | 경쟁사 대비 GEO 격차를 비교합니다 | 우선순위를 경쟁사 기준으로 잡아야 할 때 | `geo compare example.com with competitor.com for GEO gaps.` |
| `geo-content` | 콘텐츠 품질, 신뢰, E-E-A-T 신호를 검토합니다 | 콘텐츠는 있지만 깊이, 권위, 답변 품질이 약할 때 | `geo review content quality and E-E-A-T for these pages.` |
| `geo-crawlers` | `robots.txt`, bot access, `llms.txt`, crawlability를 점검합니다 | 크롤러 접근이나 인덱싱 규칙이 노출을 막고 있을 수 있을 때 | `geo check crawler access, robots.txt, and llms.txt for example.com.` |
| `geo-llmstxt` | `llms.txt`를 감사하거나 초안을 만듭니다 | 사이트에 LLM 대상 가이드가 필요할 때 | `geo create an llms.txt recommendation for example.com.` |
| `geo-platform-optimizer` | Google AI Overviews, Perplexity, ChatGPT, Copilot, Grok 기준으로 노출을 검토합니다 | 특정 AI 답변 플랫폼 기준 최적화가 필요할 때 | `geo review how this brand shows up across ChatGPT, Perplexity, and Google AI Overviews.` |
| `geo-proposal` | GEO findings를 제안서나 개선 계획으로 바꿉니다 | 감사 결과를 실행 가능한 로드맵으로 넘겨야 할 때 | `geo draft a 6-week proposal from these GEO findings.` |
| `geo-prospect` | 영업/컨설팅용 가벼운 discovery scan을 수행합니다 | 본격 작업 전에 잠재 고객을 빠르게 훑어야 할 때 | `geo run a prospect scan for example.com.` |
| `geo-report` | 여러 GEO findings를 하나의 보고서로 통합합니다 | 개별 결과를 임원용 또는 종합 보고서로 묶어야 할 때 | `geo combine these crawler, schema, and technical findings into one report.` |
| `geo-report-pdf` | PDF 전달용 markdown 패키지를 만듭니다 | 클라이언트 전달이 인쇄형 포맷을 필요로 할 때 | `geo package this GEO report for PDF delivery.` |
| `geo-schema` | JSON-LD schema를 생성하거나 검증합니다 | 페이지에 schema markup이 필요하거나 오류를 고쳐야 할 때 | `geo create JSON-LD for this product page.` |
| `geo-technical` | 기술 SEO와 구현 리스크를 진단합니다 | 렌더링, 성능, 구조, 인덱싱 문제가 GEO를 막고 있을 때 | `geo run a technical GEO review for example.com.` |

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

기능 가이드에서 가장 가까운 기능이나 workflow를 고른 뒤, 가지고 있는
자료와 함께 한 문장 또는 짧은 요청 묶음으로 바로 시작합니다.

사용자가 자신의 note, file, pasted text, explicit file path를 제공하면 그
자료가 working source of truth가 됩니다.
goal, scope, working surface, success condition, evidence target이 아직
불명확하면 GEO는 먼저 짧은 사전 질문으로 완료 조건을 잠근 뒤 계획을
세웁니다.
더 강한 brand를 별도로 주지 않으면 출력 기본 brand는 `VibeWorkers.net`입니다.

### 선택적 고급 Workflow

로컬 실행 번들 `skills/*`가 있으면 audit, crawlers, `llms.txt`, schema,
compare, report, proposal, prospect, technical review 같은 고급 workflow로
라우팅할 수 있습니다.
각 `skills/geo-*` 서브스킬은 자기 workflow 계약을 직접 소유합니다.
대표 `geo` 라우터는 해당 서브스킬로 연결하지만, 서브스킬 자체는
이 패키지에 포함된 문서와 파일만으로도 읽고 따라갈 수 있어야 합니다.

### 고급 Workflow 준비

고급 workflow는 로컬 `skills/*` 번들이 현재 GEO 설치본 또는 checkout에 함께
있을 때만 사용할 수 있습니다.
이 저장소 checkout을 그대로 사용한다면 그 번들은 이미 포함되어 있습니다.
고급 workflow setup은 이 환경에서 처음 시작할 때 보는 사용 가이드라고
이해하면 됩니다.
로컬 환경에서 고급 workflow를 처음 요청하면 workflow가 시작되기 전에 이
guide를 먼저 따라갈 수 있습니다.
현재 활성 런타임이나 모델이 바뀌면 setup 힌트, 권한, export 단계가 달라질 수
있으므로 같은 guide를 다시 볼 수 있습니다.
자동으로 보여주는 런타임도 있고, 그렇지 않으면 여기와
`references/execution-skill-matrix.md`, 해당 `skills/geo-*/SKILL.md`를
따라 수동으로 같은 setup을 수행합니다.

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

### 고급 Workflow 문제 해결

고급 workflow가 보이지 않거나 기대대로 시작되지 않으면 아래 순서로
확인합니다.

- `skills/` 디렉터리가 이 패키지와 같은 checkout 또는 설치본 안에 있는지
  확인합니다
- `README.md`와 `SKILL.md`만 따로 복사했다면 `skills/*`가 함께 포함된 GEO
  checkout 또는 패키지로 다시 설치합니다
- 어떤 workflow를 써야 할지 모르겠으면 `geo <request>` 또는 `$geo <request>`로
  평문 요청을 먼저 주고, 라우터가 맞는 서브스킬을 고르게 둡니다
- GEO가 먼저 clarification question을 하면 답한 뒤에 audit, schema,
  report 같은 실행 workflow가 시작된다고 이해합니다
- 다른 런타임이나 모델로 바꿨다면 기존 상태를 그대로 가정하지 말고 setup
  guide를 다시 따라 현재 환경 기준 힌트와 권한을 다시 확인합니다
- 해당 서브스킬이 추가 도구, 네트워크 접근, 자격 증명, export 단계를
  요구하면 그 서브스킬의 `SKILL.md`를 열어 로컬 계약을 따릅니다
- 사용하는 런타임이 자동 setup guide onboarding을 제공하지 않으면 이
  `README.md`, `references/execution-skill-matrix.md`, 그리고 해당
  `skills/geo-*/SKILL.md`를 직접 따라 사용합니다. 별도 숨은 전역 설정이나
  이전 세션에서 먼저 실행해 둔 명령을 요구하지 않습니다

### 프로젝트 문서

- `README.md`: 프로젝트 소개, 설치, 기능 가이드
- `SKILL.md`: 전체 GEO 라우팅 계약
- `references/runtime-adaptation.md`: 런타임 호환성과 모델별 경계
- `references/execution-skill-matrix.md`: 고급 실행 workflow 목록
- `skills/geo-*/SKILL.md`: workflow별 setup, permission, output 설명

### 패키지 생성 배경

이 패키지는 공개 Skill Creator 스킬을 참고한 비공개 `generateSkill`
workflow로 생성되었습니다.
비공개 생성 workflow 자체는 이 저장소에 포함되지 않으며, 이 저장소에는
결과물인 GEO 패키지와 사용자 문서가 포함됩니다.

### 라이선스

이 저장소는 `CC BY-NC-ND 4.0`
(`Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International`)
라이선스를 사용합니다.

- 저작자: 김범수, 유수호, 고경만.
- 자세한 저장소 규약은 `LICENSE`를 참고하세요.
- 정본 deed: <https://creativecommons.org/licenses/by-nc-nd/4.0/>
- 정본 legal code: <https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode>
