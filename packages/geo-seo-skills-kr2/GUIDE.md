# geo-seo-skills-kr 사용 가이드

이 가이드는 GEO·SEO 분석 도구를 처음 사용하는 분을 위한 단계별 안내서입니다.
개념 이해부터 첫 분석 실행까지 순서대로 따라하실 수 있습니다.

**코어 계층(18개 스킬):** Claude 웹 / Claude Code 모두 사용 가능.
**확장 계층(4개 스킬):** Claude Code 전용 — Playwright 실측·자동 파이프라인 (10번 섹션 참고).

---

## 1. GEO란 무엇인가요?

### AI 검색의 등장

2023년부터 검색 방식이 바뀌고 있습니다.
사람들이 구글 검색 결과 10개를 클릭하는 대신, **ChatGPT·Perplexity·Google AI Overviews** 같은 AI에게 직접 질문하고 답변을 받는 방식이 빠르게 늘고 있습니다.

> "서울 근처 가장 좋은 회계 소프트웨어는?"
> → AI가 직접 답변을 생성하면서 특정 브랜드를 **인용**합니다.

이때 AI가 인용하는 브랜드는 검색 결과 1위 사이트가 아닐 수 있습니다.
AI가 신뢰할 수 있다고 판단하는 사이트, AI 크롤러가 접근 가능한 사이트, AI가 이해하기 쉬운 구조의 사이트가 인용됩니다.

### GEO가 SEO와 다른 점

| 구분 | 기존 SEO | GEO |
|---|---|---|
| 목표 | 구글 검색 결과 상위 노출 | AI 답변 속 브랜드 인용 |
| 최적화 대상 | 구글 알고리즘 | ChatGPT·Perplexity·Google AI·Bing Copilot |
| 핵심 요소 | 키워드·백링크·페이지 속도 | 콘텐츠 신뢰도·구조화 데이터·AI 크롤러 접근 |
| 확인 방법 | 순위 도구 | AI 플랫폼 직접 테스트 + 기술 분석 |

GEO는 기존 SEO를 대체하는 것이 아니라 **함께 관리해야 하는 새로운 영역**입니다.

### 이 도구가 하는 일

이 라이브러리는 사이트의 GEO 현황을 자동으로 분석하고, 어떤 부분을 개선해야 AI 검색에 더 많이 노출될 수 있는지 알려줍니다.

- AI 봇이 사이트를 방문할 수 있는지 확인 (`/geo crawlers`)
- 콘텐츠가 AI에게 인용될 만큼 신뢰도가 있는지 평가 (`/geo citability`)
- ChatGPT·Perplexity·Google AIO 각 플랫폼별 최적화 상태 진단 (`/geo platforms`)
- 개선에 필요한 코드와 파일을 직접 생성 (`/geo schema`, `/geo llmstxt`)

---

## 2. 내 레벨 확인하기

이 도구는 사용자의 기술 수준에 따라 **같은 분석을 다른 방식으로** 전달합니다.
어떤 레벨을 선택하든 분석 깊이는 동일합니다.

| 레벨 | 나는 이런 사람입니다 | 출력 방식 |
|---|---|---|
| **L1 — 마케팅 담당자** | 코드를 다루지 않고 마케팅·콘텐츠 업무를 합니다 | "개발팀에 요청할 사항" 중심의 비즈니스 언어 |
| **L2 — 웹마스터** | FTP 접속, CMS 파일 수정, 플러그인 설치가 가능합니다 | FTP·CMS 경로와 파일 수정 단계별 안내 |
| **L3 — 개발자** | 소스코드 수정, 스크립트 작성, CLI 실행이 가능합니다 | 코드 스니펫, 기술 명세, 자동화 스크립트 |

**레벨을 잘 모르겠다면 L1을 선택하세요.**
분석 결과에서 "개발팀에 전달할 내용"을 자동으로 작성해 드립니다.

---

## 3. 시작하기 — 공통 절차

레벨에 상관없이 처음 한 번만 하면 됩니다.

### 3-1. 레벨 설정

```
/geo level
```

실행하면 아래와 같은 선택 메뉴가 표시됩니다.

```
안녕하세요! GEO-SEO 분석 도구입니다.
분석 결과를 어떤 방식으로 받으시겠어요?

  1) 마케팅 담당자
  2) 웹마스터 / 사이트 운영자
  3) 개발자

번호를 입력해 주세요 (1 / 2 / 3):
```

번호를 입력하면 해당 레벨에 맞는 명령어 메뉴가 표시됩니다.
레벨은 `/geo level` 을 다시 실행해서 언제든 바꿀 수 있습니다.

### 3-2. 첫 번째 분석 실행

레벨 설정 후 전체 분석을 먼저 실행하는 것을 권장합니다.

```bash
/geo audit https://내-사이트-주소.com
```

`https://내-사이트-주소.com` 자리에 분석할 사이트 주소를 입력하세요.

### 3-3. Claude Code 확장 계층 시작 (선택)

실제 브라우저로 AI 인용을 실측하거나 자동 파이프라인을 사용하려면 확장 계층을 먼저 초기화합니다.
자세한 내용은 **10번 섹션**을 참고하세요.

```bash
/geo-code init                           # 환경 점검
/geo-code pipeline https://example.com  # 파이프라인 자동 실행
```

---

## 4. L1 — 마케팅 담당자 가이드

### 4-1. 추천 실행 순서

```bash
/geo level                          # 레벨을 1(마케팅 담당자)로 설정
/geo audit https://example.com      # 전체 GEO 현황 파악
/geo brands https://example.com     # 브랜드가 AI에 얼마나 알려져 있는지 확인
/geo platforms https://example.com  # ChatGPT·Perplexity 등 플랫폼별 노출 확인
/geo report                         # 경영진에게 보고할 종합 보고서 생성
```

### 4-2. 결과를 어떻게 해석하나요?

`/geo audit` 실행 후 L1 레벨로는 아래와 같은 형태로 결과를 받습니다.

```
[ GEO 현황 요약 ]

종합 등급: 보통 (52/100)

잘 되어 있는 부분:
  - 사이트가 안전(HTTPS)하게 운영되고 있습니다.
  - 구글 검색에는 잘 노출되고 있습니다.

개발팀에 요청이 필요한 부분:
  1. [긴급] AI 봇 차단 해제
     Claude AI 검색에서 이 사이트가 보이지 않는 상태입니다.
     → 개발팀 요청: "robots.txt에서 ClaudeBot, GPTBot 차단 해제"

  2. [중요] 회사 정보 구조화 데이터 추가
     AI가 우리 회사 정보를 정확히 이해하지 못하고 있습니다.
     → 개발팀 요청: "Organization 스키마 마크업 추가"
```

숫자와 등급보다는 **"무엇을 개발팀에 요청해야 하는지"**에 집중하시면 됩니다.

### 4-3. 보고서를 생성하려면

```bash
/geo report
```

`GEO-종합보고서.md` 파일이 생성됩니다.
이 파일을 열면 경영진·팀장에게 보고할 수 있는 형태로 정리된 내용을 확인할 수 있습니다.

### 4-4. L1에서 사용 가능한 명령어

| 명령어 | 언제 사용하나요? |
|---|---|
| `/geo audit <url>` | 처음 분석 시작, 또는 전체 현황 파악 |
| `/geo content <url>` | "우리 콘텐츠가 AI에게 신뢰받는지" 확인할 때 |
| `/geo citability <url>` | "우리 글이 AI 답변에 인용될 가능성"을 확인할 때 |
| `/geo crawlers <url>` | "AI 봇이 우리 사이트를 방문할 수 있는지" 확인할 때 |
| `/geo brands <url>` | "AI가 우리 브랜드를 얼마나 알고 있는지" 확인할 때 |
| `/geo platforms <url>` | "ChatGPT·Perplexity에 우리가 어떻게 보이는지" 확인할 때 |
| `/geo report` | 분석 결과를 보고서로 정리할 때 |

---

## 5. L2 — 웹마스터 가이드

### 5-1. 추천 실행 순서

```bash
/geo level                              # 레벨을 2(웹마스터)로 설정
/geo audit https://example.com          # 전체 감사
/geo technical https://example.com      # robots.txt·sitemap·보안 헤더 상세 점검
/geo llmstxt https://example.com        # llms.txt 파일 생성
/geo compare https://example.com https://competitor.com  # 경쟁사와 GEO 비교
/geo report                             # 체크리스트 형태 보고서
```

### 5-2. 기술 SEO 점검 결과 보는 법

`/geo technical` 실행 시 L2 레벨로는 아래처럼 파일 수정 경로까지 안내합니다.

```
[robots.txt] ClaudeBot 차단 중

현재 설정:
  User-agent: ClaudeBot
  Disallow: /

수정 방법 (FTP / cPanel 파일 관리자):
  1. 사이트 루트(/) 경로의 robots.txt 파일 열기
  2. 위 두 줄 삭제 또는 아래로 변경:
     User-agent: ClaudeBot
     Allow: /
  3. 저장 후 반영까지 최대 24시간 소요

확인 URL: https://example.com/robots.txt
```

### 5-3. llms.txt란 무엇인가요?

`llms.txt`는 AI 크롤러에게 사이트 구조를 안내하는 표준 파일입니다.
`robots.txt`가 검색 봇에게 허용/차단 규칙을 알려주듯, `llms.txt`는 AI에게 사이트의 핵심 내용을 요약해서 전달합니다.

```bash
/geo llmstxt https://example.com
```

실행하면 현재 llms.txt 존재 여부를 확인하고, 없으면 사이트에 맞는 내용으로 생성해 줍니다.

### 5-4. L2에서 추가로 사용 가능한 명령어

| 명령어 | 언제 사용하나요? |
|---|---|
| `/geo technical <url>` | robots.txt·sitemap·속도·보안 헤더 점검 |
| `/geo llmstxt <url>` | llms.txt 파일 진단 및 생성 |
| `/geo compare <url1> <url2>` | 경쟁사와 GEO 현황 비교 |

---

## 6. L3 — 개발자 가이드

### 6-1. 추천 실행 순서 — 신규 클라이언트 온보딩

```bash
/geo level                                 # 레벨을 3(개발자)로 설정

# 영업 단계: 잠재 고객 빠른 스캔
/geo prospect https://lead1.com https://lead2.com https://lead3.com

# 본 분석: 계약 후 상세 감사
/geo audit https://client.com
/geo technical https://client.com
/geo schema https://client.com
/geo llmstxt https://client.com

# 제안서 및 보고서 생성
/geo proposal                              # GEO-*.md 파일 자동 수집 후 Sprint 로드맵 생성
/geo report-pdf                            # 클라이언트 납품용 PDF 생성
```

### 6-2. 영업 스캔 활용하기

여러 도메인을 한 번에 스캔하여 영업 우선순위를 정할 수 있습니다.

```bash
/geo prospect https://a.com https://b.com https://c.com
```

A~D 등급으로 분류된 결과가 나옵니다.

```
A급 (즉시 제안): a.com — GEO 점수 28/100, 개선 여지 72점
  핵심 문제: llms.txt 없음, AI 봇 전면 차단, 스키마 0개
  예상 공수: 8시간

B급 (부분 제안): b.com — GEO 점수 45/100, 개선 여지 55점
  핵심 문제: FAQPage 스키마 없음, Organization 스키마 없음

D급 (제안 불필요): c.com — GEO 점수 82/100, 이미 잘 구성됨
```

### 6-3. 제안서 자동 생성

`/geo audit`, `/geo technical`, `/geo schema` 등의 분석 파일이 현재 디렉토리에 있으면 자동으로 수집하여 Sprint 로드맵 제안서를 만듭니다.

```bash
/geo proposal
```

생성되는 `GEO-제안서-[도메인]-[날짜].md` 파일에는 아래 내용이 포함됩니다.

- 현황 점수 요약표
- Sprint 1 (즉시 적용, 1~2주): 난이도 낮고 효과 높은 항목
- Sprint 2 (단기, 3~4주): 콘텐츠·스키마 구조 강화
- Sprint 3 (중장기, 1~3개월): 외부 권위 확보·자동화
- 항목별 예상 공수 및 담당 파트

### 6-4. L3 전용 명령어

| 명령어 | 언제 사용하나요? |
|---|---|
| `/geo schema <url>` | JSON-LD 스키마 9종 자동 생성 (Organization·FAQPage 등) |
| `/geo proposal` | 분석 결과를 Sprint 제안서로 정리 |
| `/geo prospect <url>...` | 잠재 고객 GEO 빠른 스캔 (배치 지원) |
| `/geo report-pdf` | 전체 분석 결과를 PDF 단일 보고서로 생성 |

### 6-5. Claude Code 확장 계층 활용하기 (Code 전용)

Claude Code 환경에서 Playwright 실측과 자동 파이프라인을 추가로 사용할 수 있습니다.

```bash
# 환경 초기화 (처음 한 번)
/geo-code init

# 단일 도메인 전체 사이클 자동 실행
/geo-code pipeline https://example.com --cp

# 복수 도메인 배치 스캔 후 하위 도메인 집중 분석
/geo-code pipeline https://a.com https://b.com https://c.com

# 분석 결과·BASELINE 상태 확인
/geo-code status example.com
```

| 명령어 | 언제 사용하나요? |
|---|---|
| `/geo-code init` | 환경 점검 (최초 1회 또는 오류 시) |
| `/geo-code pipeline <url>` | audit → realtime → tracker 자동 순서 실행 |
| `/geo realtime <url> --cp --track` | CP 콘텐츠 기반 실측 + BASELINE 스냅샷 기록 |
| `/geo tracker <도메인>` | BASELINE 시계열 변화 보고서 생성 |
| `/geo batch <url>...` | 복수 도메인 간이 스캔 비교 표 |

자세한 내용은 **10번 섹션**을 참고하세요.

---

## 7. GEO 점수 이해하기

모든 분석 결과에는 0~100점의 GEO 점수와 등급이 표시됩니다.

| 점수 | 등급 | 의미 |
|---|---|---|
| 80–100 | 우수 | AI 검색 최적화 상위 수준, 인용 가능성 높음 |
| 60–79 | 양호 | 기본 최적화 완료, 일부 개선 여지 있음 |
| 40–59 | 보통 | 주요 개선 과제 다수, 조치 필요 |
| 20–39 | 미흡 | 즉각적인 조치 필요 |
| 0–19 | 위험 | AI 검색에서 거의 노출되지 않는 수준 |

점수가 낮아도 걱정하지 마세요. 대부분의 사이트가 40~60점대에 분포하며, 이는 **개선 여지가 크다**는 의미이기도 합니다.

### 심각도 분류

GEO 감사 결과의 개선 과제는 아래 4단계로 분류되어 처리 기한과 함께 제시됩니다.

| 심각도 | 의미 | 처리 기한 |
|---|---|---|
| **CRITICAL** | AI 크롤러 전면 차단, 순수 CSR, HTTPS 미적용 등 — 즉각 조치 | 1주 이내 |
| **HIGH** | 주요 봇 차단, llms.txt 없음, Organization 스키마 없음 등 | 1달 이내 |
| **MEDIUM** | llms.txt 불완전, sameAs 부족, dateModified 없음 등 | 3달 이내 |
| **LOW** | OG 불완전, alt 일부 없음, FAQ 구조 없음 등 | 순차 개선 |

> CRITICAL 항목이 1개라도 있으면 총점이 높아도 실질적인 AI 가시성은 낮습니다.

---

## 8. 자주 묻는 질문

**Q. Claude Code와 Claude 웹 중 어느 환경에서 써야 하나요?**

두 환경 모두 사용 가능합니다. 다만 차이가 있습니다.

| 항목 | Claude 웹 | Claude Code (코어) | Claude Code (확장) |
|---|---|---|---|
| 데이터 수집 | WebFetch | WebFetch + Bash | Playwright 실측 |
| AI 인용 확인 | 간접 추정 | 간접 추정 | 실제 브라우저 실측 |
| 파일 저장 | 대화창에 결과 출력 | 로컬 폴더에 자동 저장 | 로컬 폴더에 자동 저장 |
| 복수 도메인 | 수동 순차 실행 | /geo batch | /geo-code pipeline 자동화 |
| 시계열 추적 | 불가 | 불가 | /geo tracker |

반복적으로 사용하거나 파일로 저장이 필요하다면 Claude Code를 권장합니다.
Playwright 실측과 자동 파이프라인이 필요하면 **10번 섹션**의 확장 계층을 활용하세요.

---

**Q. 레벨을 바꾸면 이전 분석 결과가 사라지나요?**

아니요. 레벨은 출력 방식만 바꿉니다. `/geo level` 로 레벨을 변경해도 이전에 생성된 `GEO-*.md` 파일은 그대로 유지됩니다.

---

**Q. L1인데 개발자용 명령어를 쓰고 싶다면?**

L1 레벨에서 L2·L3 전용 명령어를 실행하면 두 가지 선택지를 안내해 드립니다.

```
이 기능은 웹마스터·개발자 모드에서 사용할 수 있습니다.

  1) 모드 변경 후 직접 실행  →  /geo level 입력
  2) 담당자에게 전달할 요청 메모 생성  →  지금 바로 만들어 드립니다
```

2번을 선택하면 개발팀에 전달할 작업 요청 메모를 자동으로 작성해 드립니다.

---

**Q. 분석한 결과 파일은 어디에 저장되나요?**

Claude Code 환경에서는 `/geo` 명령어를 실행한 디렉토리에 아래 형태로 저장됩니다.

```
GEO-감사-보고서.md                    ← /geo audit 결과
GEO-콘텐츠-분석.md                    ← /geo content 결과
GEO-인용가능성-분석.md                ← /geo citability 결과
GEO-크롤러-분석.md                    ← /geo crawlers 결과
GEO-종합보고서.md                     ← /geo report 결과
GEO-제안서-[도메인]-[날짜].md         ← /geo proposal 결과
GEO-BRAND-BASELINE-[날짜].json        ← /geo brand 추적 스냅샷
GEO-REALTIME-[도메인]-[날짜].md       ← /geo realtime 실측 결과 (Code 전용)
GEO-TRACKER-[도메인]-[날짜].md        ← /geo tracker 시계열 보고서 (Code 전용)
GEO-BATCH-[날짜].md                   ← /geo batch 배치 스캔 비교 (Code 전용)
```

---

**Q. AI 검색 최적화는 얼마나 자주 해야 하나요?**

AI 플랫폼의 업데이트 주기에 맞춰 분기별(3개월) 재검토를 권장합니다.
사이트 구조나 콘텐츠를 크게 변경했다면 변경 직후 `/geo audit` 을 다시 실행하세요.

---

## 9. 다국어 사이트 GEO 분석

한국어 이외 언어(영어·일본어·중국어·스페인어)를 지원하는 사이트라면 다국어 GEO 기능을 활용하세요.

### 출력 언어 설정

```
/geo lang
```

실행하면 보고서를 작성할 언어를 선택하는 메뉴가 나옵니다 (ko·en·ja·zh·es).

### 사이트 언어 자동 감지

`/geo audit`, `/geo technical` 등 주요 명령어는 hreflang 태그·html lang 속성·URL 패턴을 자동으로 읽어 `SITE_LANGS`를 설정합니다. 두 개 이상의 언어가 감지되면 다국어 분석 모듈이 자동으로 활성화됩니다.

### 다국어 전용 명령어

| 명령어 | 기능 | 레벨 |
|---|---|---|
| `/geo multilang <url>` | hreflang 구현·언어별 콘텐츠 품질·AI 가시성 통합 진단 | L2·L3 |
| `/geo lang-platform <url>` | 언어별 AI 플랫폼 현황 및 봇 허용 전략 | L1·L2·L3 |
| `/geo technical <url>` | hreflang 분석 20점 포함 기술 SEO 진단 | L2·L3 |

### 한국어 사이트 체크리스트

네이버 AI 브리핑·AI 탭에 노출되려면 일반 GEO 최적화 외에 아래 항목이 추가로 필요합니다.

1. robots.txt에 `Yeti`, `NaverBot` 허용
2. Naver Search Advisor 등록 및 sitemap 제출
3. 첫 문단에 직접 답변 배치 (D.I.A. 구조)
4. H3 태그로 질문 형식 FAQ 구성
5. 작성일·수정일 날짜 명시

---

## 10. Claude Code 확장 계층 시작하기

확장 계층은 실제 브라우저를 열어 AI 인용을 실측하고, 복수 스킬을 자동 순서로 연결합니다.
**Claude Code 전용**이며 Node.js와 Playwright가 필요합니다.

### 10-1. 환경 준비

```bash
/geo-code init
```

Node.js · Playwright · browser-citation.js · Chrome CDP 5개 항목을 자동 점검합니다.
FAIL 항목이 있으면 해결 방법을 안내합니다.

```
[ geo-code 환경 점검 ]

  Node.js          v20.x.x   PASS
  Playwright       1.x.x     PASS
  Chromium                   PASS
  browser-citation           PASS
  Chrome CDP       9222      PASS

환경 준비 완료. /geo-code pipeline https://example.com 을 실행하세요.
```

ChatGPT·Gemini·Claude·Grok는 최초 1회 로그인이 필요합니다.
`/geo realtime <url> --headed` 를 실행하면 Chrome 창이 열립니다. 각 플랫폼에 로그인한 후 창을 닫지 말고 기다리면 세션이 저장됩니다.

### 10-2. 파이프라인 실행

**단일 도메인:**

```bash
/geo-code pipeline https://example.com
```

아래 순서로 자동 실행됩니다.

```
[Step 0] 환경 간이 확인
[Step 1] /geo audit        → GEO 감사 보고서 생성
[Step 2] /geo brand        → BASELINE 없을 때 자동 생성
[Step 3] /geo realtime --cp --track  → 실측 + 스냅샷 기록
[Step 4] /geo tracker      → 시계열 보고서 생성
[Step 5] 종합 요약 출력
```

**복수 도메인:**

```bash
/geo-code pipeline https://a.com https://b.com https://c.com
```

배치 스캔 후 점수 하위 3개 도메인을 선별하고 각각 파이프라인을 실행합니다.

### 10-3. 상태 확인

```bash
/geo-code status example.com
```

현재 폴더의 분석 파일 목록, BASELINE 마지막 측정일·다음 예정일, CP 프로젝트 연동 상태를 한 번에 확인합니다.

### 10-4. 4주 추적 사이클

Gap을 꾸준히 줄이려면 4주마다 재측정하는 것을 권장합니다.

```
1주차  /geo-code pipeline https://example.com --cp   (초기 측정)
4주차  /geo-code pipeline https://example.com --cp   (재측정 + BASELINE 갱신)
4주차  /geo tracker example.com                      (시계열 변화 확인)
```

`/geo tracker` 보고서에서 Gap 등급 변화(INVISIBLE → DISTANT → PARTIAL → ALIGNED → ANCHORED)와
포지셔닝 반영률·SOV·BCI 추이를 확인할 수 있습니다.

---

## 11. 다음 단계

이 가이드를 읽고 첫 분석을 완료했다면, 아래 파일을 참고하여 더 깊이 활용하세요.

| 파일 | 내용 |
|---|---|
| `README.md` | 22개 스킬 전체 목록, 레벨 매트릭스, 워크플로 요약 |
| `CLAUDE.md` | 라이브러리 설계 원칙, 주요 결정 사항, 진행 이력 |
| `skills/geo-code/SKILL.md` | 확장 계층 오케스트레이터 내부 로직 |
