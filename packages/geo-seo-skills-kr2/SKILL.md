---
name: geo-seo-skills-kr2
description: >
  GEO + SEO 통합 분석 도구. AI 검색(ChatGPT, Claude, Perplexity, Gemini,
  Google AI Overviews, 네이버 AI 브리핑 등) 최적화와 전통 SEO 기반을 동시에 점검한다.
  사용자 레벨(마케팅 담당자 / 웹마스터 / 개발자)에 따라 분석 결과와
  액션 아이템의 표현 방식이 달라진다. 한·영·일·중·스페인어 다국어 사이트 분석과
  언어별 AI 플랫폼 최적화를 지원한다.
  트리거: "geo", "seo", "감사", "분석", "AI 검색", "최적화", "사이트 점검",
  "크롤러", "llms.txt", "스키마", "브랜드 멘션", "다국어", "hreflang", URL 입력 시.
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# GEO-SEO 분석 도구

> **출력 언어:** OUTPUT_LANG 변수에 따라 결과를 출력한다. 기본값은 `ko`(한국어).
> URL, 코드 블록, 점수 수치, 기술 용어(JSON-LD, LCP, llms.txt 등)는 언어 무관 원문 유지.

---

## 언어 시스템

### 세션 변수

| 변수 | 역할 | 기본값 |
|---|---|---|
| `SITE_LANGS` | 분석 대상 사이트의 언어 목록 (자동 감지) | `["ko"]` |
| `OUTPUT_LANG` | 분석 결과 출력 언어 | SITE_LANGS[0] 또는 `ko` |

### SITE_LANGS 자동 감지 순서

1. `<html lang="">` 속성 확인
2. `<link rel="alternate" hreflang="...">` 태그 목록 수집
3. URL 패턴 (`/en/`, `/ja/`, `en.example.com` 등) 확인
4. 감지 실패 시 `["ko"]` 기본 적용

### OUTPUT_LANG 초기화 순서

1. 사용자가 `/geo lang <코드>` 명시적 지정 → 해당 값 사용
2. 미지정 + SITE_LANGS 감지됨 → SITE_LANGS[0] 사용
3. 미지정 + 감지 실패 → `ko` 기본값

지원 코드: `ko` · `en` · `ja` · `zh` · `es`

### `/geo lang` — 출력 언어 변경

`/geo lang` 또는 `/geo lang <코드>` 입력 시 OUTPUT_LANG을 갱신한다.

코드 직접 입력 예: `/geo lang en` → OUTPUT_LANG을 `en`으로 즉시 변경.

코드 생략 시 아래 선택 메뉴를 출력한다.

```
출력 언어를 선택하세요:
  1) 한국어 (ko)
  2) English (en)
  3) 日本語 (ja)
  4) 中文简体 (zh)
  5) Español (es)

번호를 입력해 주세요:
```

---

## 사용자 레벨 시스템

이 도구는 사용자의 기술 수준에 따라 동일한 분석을 다른 방식으로 전달한다.
분석 깊이는 모든 레벨에서 동일하며, **표현 방식과 액션 아이템 형태**만 달라진다.

| 레벨 | 대상 | 출력 방식 |
|---|---|---|
| **L1** | 마케팅 담당자 | 비즈니스 언어, 담당자에게 요청할 내용 중심 |
| **L2** | 웹마스터 / 운영자 | FTP·CMS·파일 수정 작업 단계별 안내 |
| **L3** | 개발자 | 코드 스니펫, 기술 명세, CLI 명령어 포함 |

레벨은 세션 시작 시 한 번 선택하며, `/geo level` 로 언제든 변경 가능하다.

---

## 레벨 선택 로직

사용자가 `/geo` 또는 `/geo <명령>` 을 처음 실행할 때 USER_LEVEL이 설정되지
않은 경우, 아래 선택 메뉴를 출력하고 입력을 기다린다.
USER_LEVEL이 이미 설정된 경우에는 바로 해당 명령을 실행한다.

**레벨 선택 메뉴:**

```
안녕하세요! GEO-SEO 분석 도구입니다.
분석 결과를 어떤 방식으로 받으시겠어요?

  1) 마케팅 담당자
     기술 배경 없이 마케팅·콘텐츠 업무를 담당하는 분
     → 비즈니스 언어로 쉽게 설명해 드립니다

  2) 웹마스터 / 사이트 운영자
     FTP 접속, 파일 수정, CMS 관리가 가능한 분
     → 운영 작업 중심으로 단계별 안내해 드립니다

  3) 개발자
     소스코드 수정, 스크립트 작성이 가능한 분
     → 코드와 기술 명세를 제공합니다

번호를 입력해 주세요 (1 / 2 / 3):
```

선택 후 아래 형식으로 확인 메시지를 출력하고 해당 레벨의 명령어 메뉴를 보여준다.

| 선택 | 확인 메시지 |
|---|---|
| 1 | "**마케팅 담당자 모드**로 설정되었습니다. 비즈니스 언어로 쉽게 안내해 드립니다." |
| 2 | "**웹마스터 모드**로 설정되었습니다. 운영 작업 중심으로 단계별 안내해 드립니다." |
| 3 | "**개발자 모드**로 설정되었습니다. 코드와 기술 명세를 제공합니다." |

이후 모든 서브스킬 실행 시 USER_LEVEL 값을 컨텍스트로 전달한다.

---

## `/geo level` — 레벨 변경

`/geo level` 입력 시 레벨 선택 메뉴를 다시 출력하고 USER_LEVEL을 갱신한다.

```
현재 모드: [마케팅 담당자 / 웹마스터 / 개발자]

변경할 모드를 선택하세요:
  1) 마케팅 담당자
  2) 웹마스터 / 사이트 운영자
  3) 개발자

번호를 입력해 주세요 (1 / 2 / 3):
```

변경 후 새 모드 확인 메시지와 함께 해당 레벨의 명령어 메뉴를 출력한다.

---

## 레벨별 명령어 메뉴

`/geo` 또는 `/geo help` 실행 시 USER_LEVEL에 따라 출력한다.

### L1 메뉴 (마케팅 담당자)

```
[ GEO-SEO 분석 도구 — 마케팅 담당자 모드 ]

분석할 사이트 주소와 함께 명령을 입력하세요.

  /geo audit <주소>      사이트 전체 분석 (처음이라면 여기서 시작)
  /geo brand <주소>      AI 브랜드 인식 Gap 분석 (포지셔닝 vs 현재 인식)
  /geo content <주소>    콘텐츠 품질 및 신뢰도 확인
  /geo citability <주소> 내 글이 AI 검색에 인용될 가능성 점수
  /geo crawlers <주소>   AI 봇이 사이트를 볼 수 있는지 확인
  /geo brands <주소>     브랜드 언급 현황 (YouTube, Reddit, Wikipedia 등)
  /geo platforms <주소>  ChatGPT·Perplexity·Google AIO별 노출 분석
  /geo report <주소>     종합 보고서 생성
  /geo lang-platform <주소>  언어별 AI 플랫폼 분석 (네이버 AI 브리핑·ChatGPT·바이두 등)

  /geo level             사용자 레벨 변경
  /geo lang              출력 언어 변경 (ko·en·ja·zh·es)
```

### L2 메뉴 (웹마스터 / 운영자)

```
[ GEO-SEO 분석 도구 — 웹마스터 모드 ]

  /geo audit <url>       전체 감사
  /geo brand <url>       AI 브랜드 인식 Gap 분석 및 추적
  /geo content <url>     콘텐츠 품질 / E-E-A-T 분석
  /geo citability <url>  AI 인용 가능성 점수
  /geo crawlers <url>    AI 크롤러 접근 설정 확인
  /geo brands <url>      브랜드 멘션 스캔
  /geo platforms <url>   플랫폼별 최적화 분석
  /geo technical <url>   기술 SEO 점검 (robots.txt, sitemap, 보안 헤더)
  /geo llmstxt <url>     llms.txt 생성 및 검증
  /geo multilang <url>        다국어 사이트 GEO 진단 (hreflang·언어별 콘텐츠·번역 품질)
  /geo lang-platform <url>    언어별 AI 플랫폼 최적화 분석
  /geo compare <url1> <url2>  경쟁사 URL과 GEO 신호 비교 분석
  /geo report <url>           보고서 생성

  /geo level             레벨 변경
  /geo lang              출력 언어 변경
```

### L3 메뉴 (개발자)

```
[ GEO-SEO 분석 도구 — 개발자 모드 ]

  /geo audit <url>       전체 감사
  /geo brand <url>       AI 브랜드 인식 Gap 분석
  /geo brand <url> --track       Gap 변화 추적 (4주 순환 측정)
  /geo content <url>     콘텐츠 / E-E-A-T 분석
  /geo citability <url>  AI 인용 가능성 점수
  /geo crawlers <url>    AI 크롤러 접근 분석
  /geo brands <url>      브랜드 멘션 스캔
  /geo platforms <url>   플랫폼별 최적화
  /geo technical <url>   기술 SEO 전체 감사
  /geo llmstxt <url>     llms.txt 생성 / 검증
  /geo schema <url>      JSON-LD 스키마 감지 / 생성
  /geo compare <url1> <url2>  경쟁사 URL과 GEO 신호 비교 분석
  /geo report <url>           마크다운 보고서 생성
  /geo report-pdf             PDF 보고서 생성
  /geo multilang <url>         다국어 사이트 GEO 진단 (hreflang·번역 품질·언어별 AI 가시성)
  /geo lang-platform <url>     언어별 AI 플랫폼 최적화 분석
  /geo proposal <도메인>       GEO 개선 제안서 자동 생성
  /geo prospect <url>...       잠재 고객 GEO 빠른 스캔 (배치 지원)
  /geo realtime <url>          실측 인용 확인 — Code 전용 (Playwright 필요)
  /geo realtime <url> --cp     CP 콘텐츠 기반 질문 자동 생성 후 실측
  /geo tracker <도메인>         Gap 시계열 추적 — Code 전용 (BASELINE 파일 필요)
  /geo batch <url1> <url2> ...  복수 도메인 배치 스캔 — Code 전용

  /geo level             레벨 변경
  /geo lang              출력 언어 변경
```

---

## 명령어 라우팅

각 명령 실행 시 USER_LEVEL을 서브스킬에 전달한다.
서브스킬은 USER_LEVEL에 따라 레벨별 출력 템플릿을 적용한다.

| 명령어 | 서브스킬 | 사용 가능 레벨 |
|---|---|---|
| `/geo audit` | geo-audit | L1, L2, L3 |
| `/geo brand` | geo-brand | L1, L2, L3 |
| `/geo content` | geo-content | L1, L2, L3 |
| `/geo citability` | geo-citability | L1, L2, L3 |
| `/geo crawlers` | geo-crawlers | L1, L2, L3 |
| `/geo brands` | geo-brand-mentions | L1, L2, L3 |
| `/geo platforms` | geo-platform-optimizer | L1, L2, L3 |
| `/geo report` | geo-report | L1, L2, L3 |
| `/geo technical` | geo-technical | L2, L3 |
| `/geo llmstxt` | geo-llmstxt | L2, L3 |
| `/geo compare` | geo-compare | L2, L3 |
| `/geo schema` | geo-schema | L3 |
| `/geo report-pdf` | geo-report-pdf | L3 |
| `/geo proposal` | geo-proposal | L3 |
| `/geo prospect` | geo-prospect | L3 |
| `/geo multilang` | geo-multilang | L2, L3 |
| `/geo lang-platform` | geo-lang-platform | L1, L2, L3 |
| `/geo lang` | OUTPUT_LANG 변수 갱신 (서브스킬 없음) | L1, L2, L3 |
| `/geo realtime` | geo-realtime (확장 계층 — Code 전용) | L3 |
| `/geo tracker` | geo-tracker (확장 계층 — Code 전용) | L3 |
| `/geo batch` | geo-batch (확장 계층 — Code 전용) | L3 |

**레벨 초과 접근 처리:**

L1 사용자가 L2/L3 전용 명령어를, L2 사용자가 L3 전용 명령어를 입력하면
아래 흐름으로 처리한다.

```
이 기능은 [웹마스터·운영자 / 개발자] 모드에서 사용할 수 있습니다.

두 가지 방법이 있습니다:
  1) 모드 변경 후 직접 실행  →  `/geo level` 입력
  2) 담당자에게 전달할 요청 메모 생성  →  지금 바로 만들어 드립니다

어떻게 하시겠어요? (1 / 2):
```

사용자가 **2번**을 선택하면 아래 형식의 전달 메모를 생성한다.

```
[담당자 전달용] ○○ 작업 요청

작업 내용: (예) llms.txt 파일 생성 및 서버 루트에 배포
이유:       AI 검색 엔진이 사이트 구조를 이해하는 데 필요한 표준 파일입니다.
            없을 경우 ChatGPT·Perplexity 등에서 사이트가 누락될 수 있습니다.
요청 위치:  사이트 루트 (https://example.com/llms.txt)
참고 자료:  https://llmstxt.org
우선순위:   높음 / 보통 / 낮음
```

전달 메모 생성 후 레벨 변경 안내도 함께 출력한다:
"모드를 변경하고 직접 실행하려면 `/geo level` 을 입력하세요."

---

## 환경 분기 가이드

이 도구는 **코어 계층**과 **확장 계층**으로 구분된다.

### 코어 계층 — Claude 웹 / Claude Code 모두 지원

WebFetch 기반 원격 분석으로 실행되며 별도 설치 없이 작동한다.  
17개 스킬 전체(`/geo audit` ~ `/geo lang-platform`)가 여기에 해당한다.

### 확장 계층 — Claude Code 전용

로컬 브라우저 자동화(Playwright) 또는 파일 시스템 접근이 필요하다.

| 명령어 | 필요 도구 | 설명 |
|---|---|---|
| `/geo realtime` | Playwright + Node.js | 브라우저 실측 인용 확인 |
| `/geo tracker` | 로컬 파일 시스템 | BASELINE 기반 Gap 시계열 추적 |
| `/geo batch` | Bash + WebFetch | 복수 도메인 간이 GEO 스캔 비교 |

Claude Code에서 확장 계층을 파이프라인으로 실행하려면
`/geo-code init` → `/geo-code pipeline <url>` 순서로 시작하세요.

**Claude 웹에서 확장 계층 명령어를 호출하면 아래 메시지를 출력하고 중단한다.**

```
이 기능은 Claude Code(터미널)에서만 실행할 수 있습니다.
Playwright 브라우저 자동화 또는 로컬 파일 시스템 접근이 필요하므로
웹 환경에서는 지원되지 않습니다.

Claude Code를 실행한 후 동일 명령어를 다시 입력해 주세요.
설치 안내: https://docs.anthropic.com/claude-code
```

---

## 전체 감사 흐름 (/geo audit)

`/geo audit <url>` 실행 시 아래 순서로 분석한다.

**1단계: 사이트 기본 정보 수집**
- WebFetch로 홈페이지 로드
- 비즈니스 유형 감지 (SaaS / 로컬 / 이커머스 / 미디어 / 에이전시 / 기타)
- sitemap.xml 또는 내부 링크에서 주요 페이지 추출 (최대 50개)

**2단계: 영역별 분석 (순차 실행)**

모든 레벨에서 동일한 5개 영역을 빠짐없이 분석한다.
레벨에 따라 달라지는 것은 **분석 실행 여부가 아니라 결과 표현 방식**이다.

| 순서 | 분석 영역 | 서브스킬 |
|---|---|---|
| 1 | AI 가시성 (인용, 크롤러, llms.txt, 브랜드) | geo-citability + geo-crawlers |
| 2 | 플랫폼 최적화 | geo-platform-optimizer |
| 3 | 기술 SEO | geo-technical |
| 4 | 콘텐츠 품질 / E-E-A-T | geo-content |
| 5 | 스키마 마크업 | geo-schema |

**레벨별 출력 차이 예시 — 기술 SEO 결과:**

- **L1 (마케팅 담당자):**
  ```
  [개발팀 전달 필요] 기술 문제 2건 발견

  1. AI 봇 차단 (긴급)
     Claude AI 검색에서 이 사이트가 보이지 않는 상태입니다.
     → 개발팀 요청: "robots.txt에서 ClaudeBot 차단 해제"

  2. 구조화 데이터 없음 (중요)
     구글과 AI가 사이트 정보를 정확히 이해하지 못하고 있습니다.
     → 개발팀 요청: "Organization 스키마 마크업 추가"
  ```

- **L2 (웹마스터):**
  ```
  [기술 SEO] robots.txt — ClaudeBot 차단 중

  현재 설정:
    User-agent: ClaudeBot
    Disallow: /

  FTP 접속 → 사이트 루트(/) → robots.txt 파일 수정:
    User-agent: ClaudeBot
    Allow: /

  저장 후 반영까지 최대 24시간 소요.
  ```

- **L3 (개발자):**
  ```
  robots.txt: ClaudeBot Disallowed (Critical)

  현재: User-agent: ClaudeBot / Disallow: /
  권장:
    User-agent: GPTBot
    User-agent: ClaudeBot
    User-agent: PerplexityBot
    Allow: /

  반영 후 Search Console 크롤 통계로 확인 권장.
  ```

**3단계: 종합 GEO 점수 산출**

| 카테고리 | 가중치 |
|---|---|
| AI 인용 가능성 | 25% |
| 브랜드 권위 신호 | 20% |
| 콘텐츠 품질 / E-E-A-T | 20% |
| 기술 기반 | 15% |
| 구조화 데이터 | 10% |
| 플랫폼 최적화 | 10% |

**4단계: 레벨별 보고서 출력**
`geo-report` 서브스킬을 호출하여 USER_LEVEL에 맞는 보고서를 생성한다.

---

## 비즈니스 유형별 분석 조정

홈페이지 분석 결과에 따라 권고사항을 조정한다.

| 유형 | 감지 신호 | 주요 조정 사항 |
|---|---|---|
| SaaS | 가격 페이지, 무료 체험, /dashboard | SoftwareApplication 스키마, 비교 페이지 전략 |
| 로컬 비즈니스 | 전화번호, 주소, 지도 임베드 | LocalBusiness 스키마, Google Business Profile |
| 이커머스 | 장바구니, 상품 페이지, 가격 | Product 스키마, 리뷰 수집 |
| 미디어 / 블로그 | 바이라인, 날짜, article 스키마 | Article 스키마, 저자 E-E-A-T |
| 에이전시 | 포트폴리오, 사례 연구 | Organization 스키마, 신뢰 신호 |

---

## 출력 파일 목록

| 명령어 | 출력 파일명 |
|---|---|
| `/geo audit` | `GEO-감사-보고서.md` |
| `/geo brand` | `GEO-BRAND-GAP-[브랜드]-[날짜].md` · `GEO-BRAND-CP-인풋-[날짜].md` · `GEO-BRAND-BASELINE-[날짜].json` |
| `/geo content` | `GEO-콘텐츠-분석.md` |
| `/geo citability` | `GEO-인용가능성-분석.md` |
| `/geo crawlers` | `GEO-크롤러-분석.md` |
| `/geo brands` | `GEO-브랜드언급-분석.md` |
| `/geo platforms` | `GEO-플랫폼-분석.md` |
| `/geo technical` | `GEO-기술SEO-분석.md` |
| `/geo llmstxt` | `GEO-llmstxt-분석.md` |
| `/geo schema` | `GEO-스키마-[도메인].md` |
| `/geo compare` | `GEO-비교분석-[자사도메인]-vs-[경쟁사도메인].md` |
| `/geo report` | `GEO-종합보고서.md` |
| `/geo report-pdf` | `GEO-보고서-[도메인]-[날짜].md` |
| `/geo proposal` | `GEO-제안서-[도메인]-[날짜].md` |
| `/geo prospect` | `GEO-잠재고객-[도메인]-[날짜].md` |
| `/geo multilang` | `GEO-다국어-[도메인]-[날짜].md` |
| `/geo lang-platform` | `GEO-언어플랫폼-[도메인]-[날짜].md` |
| `/geo realtime` | `GEO-REALTIME-[도메인]-[날짜].md` (Code 전용) |
| `/geo tracker` | `GEO-TRACKER-[도메인]-[날짜].md` (Code 전용) |
| `/geo batch` | `GEO-BATCH-[날짜].md` (Code 전용) |

---

## 품질 기준

- 페이지 크롤 최대 50개 (감사 품질 우선)
- 페이지당 요청 타임아웃 30초
- 요청 간 1초 간격 (서버 부하 방지)
- robots.txt 항상 준수
- 80% 이상 내용 중복 페이지 건너뜀

---

## Generate-skill Package Closeout

This section records the `generate-skill` functionization closeout for the
portable KR2 package. It owns packaging, routing, runtime compatibility, and
validation metadata only. The GEO/SEO domain contract remains in the command
routing and subskills above.

### Working Source of Truth and Clarification Packet

| Field | Locked value |
|---|---|
| Goal | Package the complete KR2 GEO/SEO material as a reusable skill package. |
| Scope | Preserve KR2 behavior and route work through the bundled GEO subskills. |
| Exclusions | Do not import CogArch topology, hidden session state, or beta-A/main governance changes into this ordinary skill. |
| Working surface | Complete KR2 source package supplied by the user. |
| Success condition | `SKILL.md`, `agents/openai.yaml`, references, and subskills validate as a portable package. |
| Evidence target | `skills-ref validate` and `quick_validate.py` pass on this package directory. |
| Runtime target | Shared skill package with a local OpenAI/Codex compatibility adapter. |
| Provider / provenance | Project-local KR2 package material maintained in the GEO repository. |
| Output brand | No global output brand is imposed by this skill; deliverable branding follows the user's project request. |

### Trigger Contract

Use this skill when the user asks for Korean GEO/SEO analysis, AI search
optimization, multilingual GEO checks, brand mention visibility, llms.txt,
schema, crawler access, platform optimization, report generation, proposal
creation, or GEO/SEO batch work.

Should-trigger examples:

- `한국어 사이트 GEO/SEO 감사를 해줘`
- `이 URL의 llms.txt와 AI 크롤러 접근성을 점검해줘`
- `브랜드가 ChatGPT, Perplexity, Google AI Overviews에서 어떻게 보일지 분석해줘`
- `다국어 hreflang과 언어별 AI 플랫폼 최적화를 점검해줘`

Should-not-trigger examples:

- General marketing copywriting with no GEO, SEO, AI search, crawler, schema, or citation objective.
- Generic web app debugging unrelated to discoverability, crawler access, structured data, or search visibility.
- CogArch global skill governance, branch management, or cross-tool topology work.

### Capability Split

| Surface | Responsibility |
|---|---|
| `SKILL.md` | Representative routing contract, language/user-level handling, command map, package closeout. |
| `skills/*/SKILL.md` | Advanced GEO execution subskills for audit, brand, content, crawlers, schema, reports, realtime, tracker, and batch work. |
| `references/` | Reusable checklists, language/platform maps, glossary, concept map, and evidence boundary notes. |
| `agents/openai.yaml` | Local OpenAI/Codex compatibility metadata only. |
| Root notes such as `GUIDE.md`, `PROGRESS.md`, and upgrade plans | Source/provenance and implementation context; not hidden runtime requirements. |

### Runtime Compatibility Gate

Status: `runtime-delta implemented`.

The shared portable core is this package directory and its `SKILL.md` routing
contract. `agents/openai.yaml` is the only runtime-local artifact added by this
functionization pass, and it is treated as a local OpenAI/Codex compatibility
adapter rather than a universal runtime guarantee.

This ordinary skill must remain usable without requiring `~/.cogarch`, hidden
slash commands, hidden session variables outside the documented USER_LEVEL and
OUTPUT_LANG concepts, or cross-tool symlink topology.

### Legacy Package Distillation Gate

| Owner | Role |
|---|---|
| Source package owner | Complete KR2 material supplied as the working source package. |
| Target owner | GEO repository `beta-B` package surface at `packages/geo-seo-skills-kr2`. |
| `generate-skill` | Packaging, routing, validation, and closeout criteria. |
| `cogarch` | Optional consumer/indexer/governance gateway, not the owner of this ordinary skill's domain content. |

Action label: `merge`.

The KR2 execution contract is merged into the `geo-seo-skills-kr2` package
surface. CogArch topology and global governance assumptions are not merged into
this ordinary skill.

### Code / LLM Boundary

Code-enforced checks:

- Package validation must pass before release or installation handoff.
- Root `name` must match the package directory name: `geo-seo-skills-kr2`.
- Subskill routing must target files that exist under `skills/`.
- Runtime-local metadata must stay confined to `agents/openai.yaml` unless a new owned adapter is explicitly added.

LLM judgment areas:

- Which GEO subskill best matches an ambiguous user request.
- How to adapt output depth to L1, L2, or L3 user level.
- How to reconstruct English-first evidence into natural Korean while preserving mechanism, limitation, and decision relevance.
- Whether a near-miss request should be routed to general writing, web engineering, or governance instead of this skill.

### Portable Handoff Metadata

Setup/install note: copy or install the package directory as `geo-seo-skills-kr2`
in a supported skill root. Keep the directory name and root `name` field aligned.

Dependencies: no bundled external API credential is required for the base routing
contract. Some advanced execution paths may require web fetching, browser
measurement, Playwright, crawler access, or project-provided URLs as described by
the relevant subskill.

Permissions: the package may read target URLs and local reference files during
analysis. File writes should be limited to requested deliverables such as reports,
llms.txt drafts, schemas, or package maintenance changes.

Network: network access is task-dependent and should be disclosed when live URL,
search, crawler, or AI platform evidence is requested.

Source/license notes: the package is derived from the complete KR2 working source
material provided for this GEO project. Downstream users must preserve any
stricter source, license, privacy, or client-data boundaries attached to their
project materials.

Hidden local path rule: this package must not depend on the original source path,
branch-local session state, or CogArch global topology to execute its ordinary
GEO/SEO routing contract.

### Routing Experiments

| Prompt | Expected behavior |
|---|---|
| `example.com의 GEO audit를 한국어로 해줘` | Trigger this skill, initialize user level if needed, route to `geo-audit`, and return a Korean GEO/SEO audit plan or result. |
| `hreflang과 네이버 AI 브리핑까지 포함해서 다국어 GEO를 봐줘` | Trigger this skill and route to multilingual/language-platform analysis. |
| `브랜드 슬로건을 더 감성적으로 바꿔줘` | Do not trigger unless the user adds GEO/SEO/search visibility intent. |

### Rubric

Must:

- `SKILL.md` exists at package root and its frontmatter `name` is `geo-seo-skills-kr2`.
- `agents/openai.yaml` exists as the local compatibility adapter.
- The package contains `references/` and `skills/` surfaces rather than embedding every detail in this root file.
- `Runtime Compatibility Gate`, `Legacy Package Distillation Gate`, `Code / LLM Boundary`, `Portable Handoff Metadata`, and `Trigger Contract` remain present in this closeout section.
- Validation evidence includes `skills-ref validate` and `quick_validate.py` passing on the package directory.

Should:

- Keep Korean as the default output language while preserving technical terms exactly where precision requires it.
- Prefer English-language primary/expert evidence for core claims, with Korean sources labeled as local context when used.
- Keep future runtime deltas small and explicit instead of forking the whole package by host runtime.
