---
name: geo-platform-optimizer
description: >
  AI 플랫폼별 최적화 평가. Google AI Overviews, Perplexity AI, ChatGPT,
  Microsoft Copilot, Grok 5개 플랫폼에서 사이트가 얼마나 잘 노출되는지 진단한다.
  플랫폼마다 작동 방식이 다르므로 각각의 최적화 신호를 별도로 평가하고
  종합 플랫폼 점수를 산출한다.
  모든 레벨에서 동일하게 분석하며 출력 방식만 달라진다.
  트리거: "플랫폼 최적화", "AI Overviews", "Perplexity", "platform", "/geo platform".
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# geo-platform-optimizer — AI 플랫폼별 최적화 평가

> 실행 시 USER_LEVEL을 확인한다. 설정되지 않은 경우 레벨 선택을 먼저 요청한다.
> 결과는 USER_LEVEL에 맞는 출력 템플릿으로 전달하고 `GEO-플랫폼-분석.md`로 저장한다.

---

## 플랫폼별 작동 방식 요약

각 플랫폼은 콘텐츠를 처리하는 방식이 다르다. 동일한 사이트라도 플랫폼마다 최적화 전략이 달라진다.

| 플랫폼 | 작동 방식 | 핵심 최적화 포인트 |
|---|---|---|
| Google AI Overviews | Google 인덱스 + Gemini 모델 | E-E-A-T, 구조화 데이터, Core Web Vitals |
| Perplexity AI | 실시간 웹 크롤링 + 인용 | 직접 답변 구조, 출처 명확성 |
| ChatGPT | 학습 데이터 + 실시간 브라우징 | GPTBot 허용, 콘텐츠 깊이 |
| Microsoft Copilot | Bing 인덱스 기반 | Bing Webmaster Tools, Bingbot 허용 |
| Grok (xAI) | X(Twitter) 데이터 + 실시간 검색 | X 계정 연결, GrokBot 허용 |

---

## 실행 단계

### 1단계: 전제 조건 확인

WebFetch로 사이트 기본 상태를 확인한다.
geo-crawlers 분석 결과가 있으면 봇 허용 현황을 재사용한다.

- robots.txt: 각 플랫폼 봇 허용 여부
- 홈페이지 로딩 속도 (응답 시간)
- HTTPS 여부
- 모바일 대응 여부 (viewport 메타 태그)

---

### 2단계: 플랫폼별 최적화 상태 평가

#### Google AI Overviews 평가

Google AI Overviews는 Google 검색 결과 상단에 AI가 직접 답변을 생성한다.
기존 Google SEO 최적화와 연결되어 있으나, AI 답변 선택 기준은 별도로 존재한다.

| 신호 | 확인 항목 |
|---|---|
| Google-Extended 허용 | robots.txt에서 Google-Extended 차단 여부 |
| Featured Snippet 구조 | 정의 단락, 단계별 목록, 표 형식 콘텐츠 |
| FAQ 스키마 | FAQPage JSON-LD 적용 여부 |
| 페이지 속도 | Core Web Vitals LCP 2.5초 이내 여부 |
| 모바일 최적화 | 모바일 친화적 레이아웃 여부 |
| E-E-A-T 신호 | 저자 정보, 날짜, 출처 명시 여부 |
| Google Search Console | 사이트 등록 및 색인 상태 |

#### Perplexity AI 평가

Perplexity는 질문에 대해 웹을 실시간 검색하고 출처를 명시하며 답변한다.
직접 인용 가능한 콘텐츠 구조가 핵심이다.

| 신호 | 확인 항목 |
|---|---|
| PerplexityBot 허용 | robots.txt에서 PerplexityBot 차단 여부 |
| 직접 답변 단락 | 질문에 바로 답하는 명확한 문장 존재 |
| 출처 명확성 | 작성일, 저자, 조직명 표시 여부 |
| 통계·데이터 출처 | 수치에 출처 링크 여부 |
| 콘텐츠 최신성 | 수정일 명시, 6개월 이내 업데이트 여부 |
| HTTPS | 보안 접속 여부 |

#### ChatGPT 평가

ChatGPT는 학습 데이터(GPTBot)와 실시간 브라우징(ChatGPT-User) 두 경로를 통해 콘텐츠를 사용한다.

| 신호 | 확인 항목 |
|---|---|
| GPTBot 허용 | robots.txt에서 GPTBot 차단 여부 |
| ChatGPT-User 허용 | ChatGPT-User 차단 여부 |
| 콘텐츠 깊이 | 표면적 설명을 넘어 원리·사례·수치 포함 여부 |
| Open Graph | og:title, og:description, og:url 완비 여부 |
| 구조화된 데이터 | Article 스키마 적용 여부 |
| 브랜드 언급 외부 | 타 사이트에서 이 사이트를 인용하는지 |

#### Microsoft Copilot 평가

Copilot은 Bing 검색 인덱스를 기반으로 작동한다.
Bing에 잘 색인되어 있으면 Copilot 노출도 자연스럽게 따라온다.

| 신호 | 확인 항목 |
|---|---|
| Bingbot 허용 | robots.txt에서 Bingbot 차단 여부 |
| Bing Webmaster Tools | 사이트 등록 여부 (수동 확인 필요) |
| sitemap.xml | Bing에 sitemap 제출 여부 |
| 구조화 데이터 | Bing이 인식하는 Schema.org 적용 여부 |
| 메타 설명 | meta description 160자 이내 명확하게 작성 여부 |
| 내부 링크 구조 | 주요 페이지로의 클릭 3회 이내 접근 가능 여부 |

#### Grok 평가

Grok은 X(Twitter) 데이터와 실시간 웹 검색을 결합한다.
X 계정과의 연결이 다른 플랫폼에 없는 고유한 최적화 포인트다.

| 신호 | 확인 항목 |
|---|---|
| GrokBot 허용 | robots.txt에서 GrokBot 차단 여부 |
| xAI-Grok 허용 | xAI-Grok 차단 여부 |
| Grok-DeepSearch 허용 | Grok-DeepSearch 차단 여부 |
| X(Twitter) 계정 연결 | 공식 X 계정에서 사이트 URL 등록 여부 |
| Twitter Card 메타 태그 | twitter:card, twitter:title, twitter:description 설정 여부 |
| 실시간 콘텐츠 | 최신 정보·업데이트 게시 빈도 |

---

### 3단계: 플랫폼 최적화 점수 산출

5개 플랫폼을 4개 그룹으로 묶어 평가한다.
각 그룹 0–25점, 합산 0–100점이 플랫폼 점수다.

```
플랫폼 점수 = (Google AI Overviews × 0.35) +
             (실시간검색AI × 0.30) +
             (대화형AI × 0.20) +
             (공통기반신호 × 0.15)
```

| 그룹 | 포함 플랫폼 | 가중치 | 이유 |
|---|---|---|---|
| Google AI Overviews | Google | 35% | 검색 트래픽 점유율 최대 |
| 실시간 검색 AI | Perplexity, Copilot | 30% | 인용 기반 실시간 답변 |
| 대화형 AI | ChatGPT, Grok | 20% | 학습 + 브라우징 혼합 |
| 공통 기반 신호 | 전체 공통 | 15% | 속도·HTTPS·구조화 데이터 |

**점수 등급표**

| 점수 | 등급 | 상태 |
|---|---|---|
| 80–100 | 우수 | 주요 AI 플랫폼 전반에서 최적화 |
| 60–79 | 양호 | 일부 플랫폼 개선 여지 있음 |
| 40–59 | 보통 | 주요 플랫폼 신호 미흡 |
| 20–39 | 미흡 | 다수 플랫폼에서 노출 낮음 |
| 0–19 | 위험 | AI 플랫폼 전반에서 거의 노출 없음 |

---

### 4단계: 레벨별 보고서 출력

아래 출력 템플릿에 따라 보고서를 작성하고 `GEO-플랫폼-분석.md`로 저장한다.

---

## 레벨별 출력 템플릿

---

### L1 출력 — 마케팅 담당자

"각 AI 서비스에서 우리 사이트가 얼마나 잘 보이는가"를 중심으로 전달한다.
플랫폼별 현황을 한눈에 파악할 수 있도록 구성하고,
마케팅팀이 즉시 실행할 수 있는 조치를 안내한다.

```markdown
# [사이트명] AI 플랫폼 노출 현황 분석

분석일: [날짜]  |  분석 URL: [URL]

---

## AI 플랫폼 노출 현황: [우수 / 양호 / 보통 / 미흡 / 위험]

[한 줄 요약]
예) "Google AI 검색에서는 노출되지만 Perplexity와 Copilot에서는 거의 보이지 않는 상태입니다."

---

## 플랫폼별 노출 현황

| AI 플랫폼 | 노출 수준 | 핵심 문제 |
|---|---|---|
| Google AI Overviews | 좋음 / 주의 / 위험 | [한 줄] |
| Perplexity AI | 좋음 / 주의 / 위험 | [한 줄] |
| ChatGPT | 좋음 / 주의 / 위험 | [한 줄] |
| Microsoft Copilot | 좋음 / 주의 / 위험 | [한 줄] |
| Grok | 좋음 / 주의 / 위험 | [한 줄] |

---

## 지금 할 수 있는 것 (마케팅팀)

1. **[조치 제목]**
   왜 중요한가: [이유 1–2문장]
   어떻게: [구체적인 방법, 기술 용어 없이]

2. **[조치 제목]**
   왜 중요한가: [이유]
   어떻게: [방법]

---

## 개발팀 / 운영팀 전달 요청

| 요청 내용 | 담당 | 이유 | 우선순위 |
|---|---|---|---|
| [요청] | 개발팀 / 운영팀 | [이유 한 줄] | 높음 / 보통 |
```

---

### L2 출력 — 웹마스터 / 운영자

플랫폼별 점수와 함께 CMS·FTP에서 직접 수정할 수 있는 방법을 안내한다.
Bing Webmaster Tools, Twitter Card 등 플랫폼별 설정 방법을 단계별로 안내한다.

```markdown
# [사이트명] AI 플랫폼 최적화 분석

분석일: [날짜]  |  URL: [URL]

---

## 플랫폼 점수: [점수]/100 — [등급]

| 그룹 | 점수 | 주요 발견 |
|---|---|---|
| Google AI Overviews | [X]/25 | [발견 사항 한 줄] |
| 실시간 검색 AI (Perplexity · Copilot) | [X]/25 | [발견 사항 한 줄] |
| 대화형 AI (ChatGPT · Grok) | [X]/25 | [발견 사항 한 줄] |
| 공통 기반 신호 | [X]/25 | [발견 사항 한 줄] |

---

## 플랫폼별 상세 현황

### Google AI Overviews
- Google-Extended 봇: [허용 / 차단]
- FAQ 스키마: [있음 / 없음]
- 페이지 속도: [빠름 / 보통 / 느림]
- 핵심 문제: [한 줄]

### Perplexity AI
- PerplexityBot: [허용 / 차단]
- 직접 답변 구조: [있음 / 없음]
- 콘텐츠 최신성: [최신 / 오래됨]
- 핵심 문제: [한 줄]

### ChatGPT
- GPTBot / ChatGPT-User: [허용 / 차단]
- Open Graph 태그: [완비 / 부족]
- 핵심 문제: [한 줄]

### Microsoft Copilot
- Bingbot: [허용 / 차단]
- Bing Webmaster Tools: [등록 / 미등록]
- 핵심 문제: [한 줄]

### Grok
- GrokBot / xAI-Grok / Grok-DeepSearch: [허용 / 차단]
- X(Twitter) 계정 연결: [있음 / 없음]
- Twitter Card: [설정 / 미설정]
- 핵심 문제: [한 줄]

---

## 우선순위별 수정 과제

### 즉시 처리 가능

**1. [문제 제목]**
- 현재 상태: [설명]
- 수정 방법:
  1. [단계별 안내]
  2. [단계]
- WordPress 사용 시: [플러그인 또는 직접 수정 방법]
- 소요 시간: [예상 시간]

### 개발팀 요청

**[문제 제목]**
- 현재 상태: [설명]
- 요청 내용: [개발팀에 전달할 내용]
- 예상 효과: [효과]
```

---

### L3 출력 — 개발자

전체 기술 명세, 플랫폼별 점수 breakdown, Twitter Card·Open Graph 코드를 포함한다.

```markdown
# [사이트명] AI Platform Optimization Analysis

Date: [날짜]  |  URL: [URL]

---

## Platform Score: [점수]/100

| Group | Score | Weight | Weighted | Key Gaps |
|---|---|---|---|---|
| Google AI Overviews | [X]/25 | 35% | [X] | [갭 목록] |
| Real-time Search AI | [X]/25 | 30% | [X] | [갭 목록] |
| Conversational AI | [X]/25 | 20% | [X] | [갭 목록] |
| Common Signals | [X]/25 | 15% | [X] | [갭 목록] |
| **합계** | | | **[점수]/100** | |

---

## Platform-by-Platform Analysis

### Google AI Overviews
| Signal | Status | Detail |
|---|---|---|
| Google-Extended | Allowed / Blocked | [설명] |
| FAQ Schema | Present / Missing | [설명] |
| LCP | [X]ms | Pass / Fail (기준: 2500ms) |
| E-E-A-T | Strong / Weak | [설명] |
| Mobile-friendly | Pass / Fail | [설명] |

### Perplexity AI
| Signal | Status | Detail |
|---|---|---|
| PerplexityBot | Allowed / Blocked | [설명] |
| Direct Answer Structure | Present / Missing | [설명] |
| dateModified | Present / Missing | [설명] |
| Source Attribution | Present / Missing | [설명] |

### ChatGPT
| Signal | Status | Detail |
|---|---|---|
| GPTBot | Allowed / Blocked | [설명] |
| ChatGPT-User | Allowed / Blocked | [설명] |
| OG Tags Complete | Yes / No | [설명] |
| Article Schema | Present / Missing | [설명] |

### Microsoft Copilot
| Signal | Status | Detail |
|---|---|---|
| Bingbot | Allowed / Blocked | [설명] |
| Bing Webmaster Tools | Registered / Not | 수동 확인 필요 |
| sitemap.xml | Present / Missing | [설명] |
| meta description | Optimized / Missing | [설명] |

### Grok
| Signal | Status | Detail |
|---|---|---|
| GrokBot | Allowed / Blocked | [설명] |
| xAI-Grok | Allowed / Blocked | [설명] |
| Grok-DeepSearch | Allowed / Blocked | [설명] |
| Twitter Card | Present / Missing | [설명] |
| X account linked | Yes / No | [설명] |

---

## Critical Issues

### [CRITICAL] Twitter Card 미설정
현재: Twitter Card 메타 태그 없음
영향: Grok의 X 데이터 기반 인식 약화, SNS 공유 시 미리보기 없음
해결:
  ```html
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@[계정]">
  <meta name="twitter:title" content="[페이지 제목]">
  <meta name="twitter:description" content="[설명 160자 이내]">
  <meta name="twitter:image" content="https://[도메인]/og-image.jpg">
  ```

### [CRITICAL] Open Graph 불완전
현재: og:image 또는 og:description 누락
영향: ChatGPT 브라우징·Perplexity 인용 시 메타데이터 불완전
해결:
  ```html
  <meta property="og:type" content="website">
  <meta property="og:title" content="[페이지 제목]">
  <meta property="og:description" content="[설명 160자 이내]">
  <meta property="og:url" content="https://[도메인]/[경로]">
  <meta property="og:image" content="https://[도메인]/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  ```

---

## 구현 우선순위

| 우선순위 | 작업 | 플랫폼 영향 | 난이도 | 담당 |
|---|---|---|---|---|
| 1 | [작업] | [플랫폼] | 낮음 / 보통 / 높음 | [FE/BE/운영] |
| 2 | [작업] | [플랫폼] | [난이도] | [담당] |
| 3 | [작업] | [플랫폼] | [난이도] | [담당] |
```

---

## Setup

This restored execution skill is bundled inside the local `geo` execution
bundle under `skills/`.

Use it after the representative `geo` router has confirmed a direct execution
request, or invoke this subskill explicitly in a compatible agent surface that
loads nested skill directories.

## Dependencies and Permissions

This skill uses the tool boundary declared in frontmatter `allowed-tools`.

Network reads and local report writes are expected when the workflow runs.
External APIs are not required beyond the HTTP or browser-access checks already
named in the skill body.

## Source and License Notes

This restored execution surface preserves the original GEO-SEO execution
workflow inside the current repository's local execution bundle.

Repository-level reuse terms are inherited from `../../LICENSE`.
