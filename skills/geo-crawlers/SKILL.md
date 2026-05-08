---
name: geo-crawlers
description: >
  AI 크롤러 접근 평가. ChatGPT, Gemini, Claude, Perplexity, Copilot, Grok 등
  상업적 점유율 상위 AI 서비스의 봇이 사이트를 얼마나 자유롭게 수집할 수 있는지 진단한다.
  봇 용도(학습용/검색용)를 구분하고 사이트 목표에 따른 허용 전략을 함께 안내한다.
  robots.txt 허용 현황, llms.txt 설정, 기술 접근성, 크롤링 효율 4개 차원으로 평가한다.
  모든 레벨에서 동일하게 분석하며 출력 방식만 달라진다.
  트리거: "크롤러", "AI 봇", "robots.txt", "크롤링", "crawlers".
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# geo-crawlers — AI 크롤러 접근 평가

> 이 서브스킬은 `cogarch` 없이 직접 열어도 닫히는 standalone GEO 실행 계약이다.
> 숨은 레벨 세션 상태를 요구하지 않는다. 요청에 수신자 맥락이 없으면 이 문서 안에서 `L1`(manager), `L2`(operator), `L3`(builder) 중 하나의 수신자 레벨을 직접 정하고 그 레벨에 맞춰 출력한다.
> 결과는 선택한 수신자 레벨에 맞는 출력 템플릿으로 전달하고 `GEO-크롤러-분석.md`로 저장한다.

---

## 실행 단계

### 0단계: 플랫폼 truth registry 확인

AI crawler, search bot, user-triggered fetch, commerce/action token은
`../../references/platform-truth-registry.md`의 source_url, last_verified,
confidence, package_action 기준으로 분리한다. registry에서 `확인 필요`로
표시된 Grok 계열 항목은 robots.txt 구현 권고가 아니라 추가 공식 근거
수집 과제로 남긴다.

### 1단계: robots.txt 및 llms.txt 수집

> **Claude Code 환경:** 아래 Bash 스크립트 실행 (HTTP 상태 코드 포함 정확한 수집)
> **Claude 웹 환경:** WebFetch로 각 URL을 순서대로 로드. 내용이 반환되면 존재, 오류 페이지면 미존재로 판단.
> HTTP 헤더 확인이 필요한 경우 외부 도구 활용: https://httpstatus.io/

**Claude Code 환경 (Bash)**

```bash
python3 -c "
import requests
from urllib.parse import urlparse

url = '[TARGET_URL]'
parsed = urlparse(url)
base = f'{parsed.scheme}://{parsed.netloc}'

for path in ['/robots.txt', '/llms.txt', '/sitemap.xml']:
    r = requests.get(base + path, headers={'User-Agent':'GEO-Audit/1.0'}, timeout=15)
    print(f'{path} STATUS: {r.status_code}')
    if r.status_code == 200:
        print(r.text[:3000])
    print('---')
"
```

**Claude 웹 환경 (WebFetch 대체)**

WebFetch로 아래 URL을 순서대로 로드한다.
- `https://[도메인]/robots.txt`
- `https://[도메인]/llms.txt`
- `https://[도메인]/sitemap.xml`

---

### 2단계: AI 봇 허용 현황 확인

robots.txt에서 아래 봇 또는 robots 제어 토큰의 허용/차단 여부를 각각 확인한다.
2026-05-07 기준 공식 문서로 확인된 항목과, first-party 공식 근거가 아직 부족해
`확인 필요`로 취급해야 하는 항목을 분리한다.

#### 핵심 대상 — 상업적 점유율 상위 AI 서비스

| 봇/토큰 이름 | User-agent token | 서비스 | 용도 | 근거 수준 |
|---|---|---|---|---|
| GPTBot | `GPTBot` | OpenAI | 학습 | 공식 |
| OAI-SearchBot | `OAI-SearchBot` | ChatGPT Search | 검색 노출용 자동 크롤링 | 공식 |
| ChatGPT-User | `ChatGPT-User` | ChatGPT 사용자 동작 | 사용자 요청 기반 가져오기, 자동 검색 색인 아님 | 공식 |
| ClaudeBot | `ClaudeBot` | Anthropic Claude | 학습 | 공식 |
| Claude-SearchBot | `Claude-SearchBot` | Claude Search | 검색 품질/색인 | 공식 |
| Claude-User | `Claude-User` | Claude 사용자 동작 | 사용자 요청 기반 가져오기 | 공식 |
| Googlebot | `Googlebot` | Google Search · AI Overviews | 검색 색인 | 공식 |
| Google-Extended | `Google-Extended` | Gemini Apps · Vertex AI Gemini | Gemini 학습/grounding 제어. Google Search 포함·순위 신호 아님 | 공식 |
| PerplexityBot | `PerplexityBot` | Perplexity AI | 검색 |
| Bingbot | `Bingbot` | Microsoft Copilot | 검색 |
| GrokBot | `GrokBot` | xAI Grok | 학습 추정 | 확인 필요 |
| xAI-Grok | `xAI-Grok` | Grok 실시간 검색 | 검색 추정 | 확인 필요 |
| Grok-DeepSearch | `Grok-DeepSearch` | Grok 심층 검색 | 검색 추정 | 확인 필요 |

**판정 기준**

- `Disallow: /` 또는 명시적 Disallow 규칙 → 차단
- `Allow: /` 또는 규칙 없음 → 허용
- `Crawl-delay` 설정 → 수집 속도 제한

---

### 3단계: 사이트 목표별 허용 전략 확인

봇 허용 여부는 사이트 목표에 따라 달라진다.
분석 전에 사이트 운영자의 목표를 파악하고 아래 전략 중 하나를 기준으로 평가한다.

| 전략 | 허용 대상 | 차단 대상 | 적합한 상황 |
|---|---|---|---|
| A. 전체 허용 | 공식 학습/검색/사용자 요청 봇 전체. Grok 계열은 근거 확인 후 선택 | — | GEO 최대화, 브랜드 노출 우선 |
| B. 검색·사용자 요청만 허용 | OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Claude-User, Googlebot, PerplexityBot, Bingbot | GPTBot, ClaudeBot, Google-Extended, GrokBot | 실시간 인용·검색 접근은 원하나 학습/grounding 데이터 제공은 거부 |
| C. 선택적 허용 | 특정 서비스만 | 나머지 | 특정 AI 플랫폼 파트너십 등 |

**전략별 GEO 영향**

- 전략 A: 실시간 인용 + 미래 모델 학습 모두 반영 → GEO 점수 최고, 장기 브랜드 인식 강화
- 전략 B: 현재 AI 검색 노출은 가능하나, 학습용 봇 차단으로 미래 모델이 브랜드를 학습하지 못해 장기 GEO 효과 감소. 저작권·콘텐츠 보호가 우선일 때 선택.
- 전략 C: 노출 범위 제한, 특수 목적에만 적합

---

### 4단계: 크롤러 접근 4개 차원 평가

각 차원을 0–25점으로 평가한다. 합산 점수(0–100)가 크롤러 점수다.

#### AI 봇 허용 상태 — 0~25점

**핵심 AI 접근 신호**의 허용 현황을 기준으로 평가한다. 검색 노출, 사용자 요청
가져오기, 학습, Gemini grounding 제어는 같은 의미가 아니므로 결과 표에서 분리한다.

| 신호 | 확인 항목 |
|---|---|
| GPTBot / OAI-SearchBot / ChatGPT-User 허용 | OpenAI 학습·검색·사용자 요청 경로 차단 여부 |
| ClaudeBot / Claude-SearchBot / Claude-User 허용 | Anthropic 학습·검색·사용자 요청 경로 차단 여부 |
| Googlebot 허용 | Google Search 색인 및 AI Overviews 후보 노출 차단 여부 |
| Google-Extended 처리 명확 | Gemini 학습/grounding 제어 토큰 허용·차단 여부. Google Search 포함·순위와 분리 |
| PerplexityBot 허용 | Perplexity 봇 차단 여부 |
| Bingbot 허용 | Copilot 관련 봇 차단 여부 |
| GrokBot / xAI-Grok / Grok-DeepSearch 허용 | Grok 관련 추정 토큰 차단 여부. first-party 근거 확인 필요 |

점수 산정: 허용된 핵심 접근 신호 비율에 비례하여 0–25점 부여하되,
`Google-Extended` 차단 자체를 Google Search 접근 차단으로 감점하지 않는다.
검색, 사용자 요청, 학습, grounding 제어의 의미를 결과 설명에서 분리한다.
전체 접근 신호 차단 0점, 전체 접근 신호 허용 25점.

#### AI 안내 파일 — 0~25점

AI용 콘텐츠 패키징을 돕는 보조 파일 존재 여부와 품질을 평가한다. `llms.txt`는
heuristic / adoption-dependent 신호이며 특정 AI 플랫폼의 수집·인용을 보장하지 않는다.

| 신호 | 확인 항목 |
|---|---|
| llms.txt 존재 | 사이트 루트에 /llms.txt 파일 존재 여부 |
| 사이트 설명 | llms.txt 내 사이트 목적·주제 설명 포함 여부 |
| 주요 URL 목록 | 핵심 페이지 링크 포함 여부 |
| sitemap 링크 | llms.txt 내 sitemap.xml 경로 안내 여부 |
| 업데이트 날짜 | llms.txt 최종 수정일 명시 여부 |

#### 기술 접근성 — 0~25점

AI 크롤러가 기술적으로 콘텐츠에 접근할 수 있는지 평가한다.

| 신호 | 확인 항목 |
|---|---|
| JavaScript 의존도 | JS 없이도 본문 콘텐츠 접근 가능 여부 |
| 메타 noindex | `<meta name="robots" content="noindex">` 미설정 여부 |
| X-Robots-Tag | HTTP 헤더에 noindex 지시 여부 |
| canonical 태그 | 중복 콘텐츠 정리 여부 |
| HTTPS | 사이트 전체 HTTPS 제공 여부 |

#### 크롤링 효율 — 0~25점

AI 크롤러가 효율적으로 사이트를 순회할 수 있는지 평가한다.

| 신호 | 확인 항목 |
|---|---|
| sitemap.xml 존재 | /sitemap.xml 또는 /sitemap_index.xml 존재 여부 |
| sitemap robots.txt 등록 | `Sitemap:` 지시자 포함 여부 |
| Crawl-delay 과도 설정 | 30초 초과 설정 여부 (초과 시 감점) |
| 응답 속도 | 홈페이지 응답 2초 이내 여부 |
| 내부 링크 깊이 | 주요 콘텐츠 클릭 3회 이내 접근 가능 여부 |

---

### 5단계: 크롤러 점수 산출

```
크롤러 점수 = (AI봇허용 × 0.35) +
             (AI안내파일 × 0.25) +
             (기술접근성 × 0.25) +
             (크롤링효율 × 0.15)
```

**점수 등급표**

| 점수 | 등급 | 상태 |
|---|---|---|
| 80–100 | 우수 | 핵심 AI 봇 전체 허용, 접근 최적화 |
| 60–79 | 양호 | 일부 개선 필요 |
| 40–59 | 보통 | 핵심 봇 일부 차단 또는 기술 이슈 존재 |
| 20–39 | 미흡 | 다수 AI 봇 차단, 즉각 조치 필요 |
| 0–19 | 위험 | AI 크롤러 전면 차단 상태 |

---

### 6단계: 레벨별 보고서 출력

아래 출력 템플릿에 따라 보고서를 작성하고 `GEO-크롤러-분석.md`로 저장한다.

---

## 레벨별 출력 템플릿

---

### L1 출력 — 마케팅 담당자

AI 봇의 사이트 접근 여부를 일상 언어로 전달한다.
"AI 검색 엔진이 이 사이트를 볼 수 있는가"를 중심으로 설명한다.
학습용/검색용 구분은 "AI가 브랜드를 아는가 vs AI 검색에 노출되는가"로 풀어서 설명한다.

```markdown
# [사이트명] AI 봇 접근 현황 분석

분석일: [날짜]  |  분석 URL: [URL]

---

## AI 봇 접근 현황: [원활 / 일부 제한 / 대부분 차단 / 전면 차단]

[한 줄 요약]
예) "ChatGPT와 Perplexity AI 봇이 차단되어 AI 검색에서 사이트 내용이 누락될 수 있습니다."

---

## AI 서비스별 접근 가능 여부

| AI 서비스 | AI 검색 노출 | AI 모델 학습 | 설명 |
|---|---|---|---|
| ChatGPT (OpenAI) | 가능 / 차단 | 가능 / 차단 | [한 줄] |
| Gemini (Google) | 가능 / 차단 | 가능 / 차단 | [한 줄] |
| Claude (Anthropic) | 가능 / 차단 | 가능 / 차단 | [한 줄] |
| Perplexity AI | 가능 / 차단 | — | [한 줄] |
| Bing Copilot | 가능 / 차단 | — | [한 줄] |
| Grok (xAI) | 가능 / 차단 | 가능 / 차단 | [한 줄] |

> AI 검색 노출: 지금 AI 검색 결과에 인용될 수 있는가
> AI 모델 학습: 미래 AI가 이 브랜드를 기억할 수 있는가

---

## 지금 개선할 수 있는 것 (마케팅팀)

1. **[조치 제목]**
   왜 중요한가: [이유 1–2문장]
   어떻게: [구체적인 방법, 기술 용어 없이]

---

## 개발팀 / 운영팀 전달 요청

| 요청 내용 | 담당 | 이유 | 우선순위 |
|---|---|---|---|
| [요청] | 개발팀 / 운영팀 | [이유 한 줄] | 높음 / 보통 |
```

---

### L2 출력 — 웹마스터 / 운영자

점수와 함께 robots.txt와 llms.txt를 FTP·CMS에서 직접 수정하는 방법을 안내한다.
전략 시나리오(A·B·C)를 제시하고 운영자가 선택할 수 있도록 한다.

```markdown
# [사이트명] AI 크롤러 접근 분석

분석일: [날짜]  |  URL: [URL]

---

## 크롤러 점수: [점수]/100 — [등급]

| 차원 | 점수 | 주요 발견 |
|---|---|---|
| AI 봇 허용 상태 | [X]/25 | [발견 사항 한 줄] |
| AI 안내 파일 | [X]/25 | [발견 사항 한 줄] |
| 기술 접근성 | [X]/25 | [발견 사항 한 줄] |
| 크롤링 효율 | [X]/25 | [발견 사항 한 줄] |

---

## AI 봇별 허용 현황

### 핵심 대상

| 봇 | 서비스 | 용도 | 현재 상태 | 조치 필요 |
|---|---|---|---|---|
| GPTBot | OpenAI | 학습 | 허용 / 차단 | 예 / 아니오 |
| OAI-SearchBot | ChatGPT Search | 검색 노출 | 허용 / 차단 | 예 / 아니오 |
| ChatGPT-User | ChatGPT 사용자 동작 | 사용자 요청 가져오기 | 허용 / 차단 | 예 / 아니오 |
| ClaudeBot | Claude | 학습 | 허용 / 차단 | 예 / 아니오 |
| Claude-SearchBot | Claude Search | 검색 품질/색인 | 허용 / 차단 | 예 / 아니오 |
| Claude-User | Claude 사용자 동작 | 사용자 요청 가져오기 | 허용 / 차단 | 예 / 아니오 |
| Googlebot | Google Search / AI Overviews | 검색 색인 | 허용 / 차단 | 예 / 아니오 |
| Google-Extended | Gemini Apps / Vertex AI Gemini | 학습·grounding 제어 | 허용 / 차단 | 예 / 아니오 |
| PerplexityBot | Perplexity | 검색 | 허용 / 차단 | 예 / 아니오 |
| Bingbot | Copilot | 검색 | 허용 / 차단 | 예 / 아니오 |
| GrokBot | Grok | 학습 추정 | 허용 / 차단 / 확인 필요 | 예 / 아니오 |
| xAI-Grok | Grok 실시간 검색 | 검색 추정 | 허용 / 차단 / 확인 필요 | 예 / 아니오 |
| Grok-DeepSearch | Grok 심층 검색 | 검색 추정 | 허용 / 차단 / 확인 필요 | 예 / 아니오 |

---

## 권장 전략

현재 차단 상태와 사이트 목표를 고려한 권장 전략: **[A / B / C]**

- 전략 A (전체 허용): AI 검색 노출 + 미래 모델 학습 모두 허용. GEO 점수 최대화. **GEO 목표라면 이 전략 권장.**
- 전략 B (검색만 허용): 실시간 인용은 허용하나, 학습용 봇 차단으로 미래 모델이 브랜드를 학습하지 못해 장기 GEO 효과 감소. 저작권·콘텐츠 보호가 우선일 때만 선택.
- 전략 C (선택적 허용): 특정 서비스만 선택해 허용. 특수 목적에만 적합.

---

## 우선순위별 수정 과제

### 즉시 처리 — robots.txt 수정

**차단된 AI 봇 허용으로 변경**
- 현재 상태: [차단된 봇 목록]
- 수정 방법:
  1. FTP 접속 → 사이트 루트(/) 이동
  2. `robots.txt` 파일 열기 (없으면 신규 생성)
  3. 아래 전략에 맞는 내용으로 수정 후 저장
  4. 브라우저에서 [도메인]/robots.txt 확인
- WordPress 사용 시: Yoast SEO → 도구 → 파일 편집기 → robots.txt 직접 수정 가능
- 소요 시간: 5분

### 즉시 처리 — llms.txt 생성

**llms.txt 파일 생성 및 업로드**
- 현재 상태: [존재 / 없음]
- 수정 방법:
  1. 아래 내용으로 `llms.txt` 파일 생성
  2. FTP로 사이트 루트(/)에 업로드
  3. 브라우저에서 [도메인]/llms.txt 확인
- 기본 템플릿:
  ```
  # [사이트명]
  > [사이트 한 줄 설명]

  ## 주요 콘텐츠
  - [섹션명]: [URL]

  ## Sitemap
  - [sitemap URL]
  ```
- 소요 시간: 10분
```

---

### L3 출력 — 개발자

전체 기술 명세, 봇별 허용 현황표, 전략별 robots.txt 코드를 포함한다.

```markdown
# [사이트명] AI Crawler Access Analysis

Date: [날짜]  |  URL: [URL]

---

## Crawler Score: [점수]/100

| Dimension | Score | Key Findings | Missing |
|---|---|---|---|
| AI Bot Allowance | [X]/25 | [발견 목록] | [누락 항목] |
| AI Guide Files | [X]/25 | [발견 목록] | [누락 항목] |
| Technical Access | [X]/25 | [발견 목록] | [누락 항목] |
| Crawl Efficiency | [X]/25 | [발견 목록] | [누락 항목] |

---

## AI Bot Access Matrix

### Primary Bots (상업적 핵심 대상)

| Bot | User-agent | Type | Status | Directive | Source |
|---|---|---|---|---|---|
| GPTBot | `GPTBot` | Training | Allowed / Blocked | [규칙] | robots.txt L[줄] |
| OAI-SearchBot | `OAI-SearchBot` | Search | Allowed / Blocked | [규칙] | — |
| ChatGPT-User | `ChatGPT-User` | User-initiated fetch | Allowed / Blocked | [규칙] | — |
| ClaudeBot | `ClaudeBot` | Training | Allowed / Blocked | [규칙] | — |
| Claude-SearchBot | `Claude-SearchBot` | Search | Allowed / Blocked | [규칙] | — |
| Claude-User | `Claude-User` | User-initiated fetch | Allowed / Blocked | [규칙] | — |
| Googlebot | `Googlebot` | Search indexing | Allowed / Blocked | [규칙] | — |
| Google-Extended | `Google-Extended` | Gemini training/grounding control | Allowed / Blocked | [규칙] | — |
| PerplexityBot | `PerplexityBot` | Search | Allowed / Blocked | [규칙] | — |
| Bingbot | `Bingbot` | Search | Allowed / Blocked | [규칙] | — |
| GrokBot | `GrokBot` | Training, unverified | Allowed / Blocked / Verify first | [규칙] | — |
| xAI-Grok | `xAI-Grok` | Search, unverified | Allowed / Blocked / Verify first | [규칙] | — |
| Grok-DeepSearch | `Grok-DeepSearch` | Search, unverified | Allowed / Blocked / Verify first | [규칙] | — |

---

## Recommended Strategy: [A / B / C]

현재 상태를 기준으로 권장 전략과 robots.txt 수정 코드를 제시한다.

### Strategy A — 전체 허용 (GEO 최적화)
  ```
  # Primary AI bots — full access
  User-agent: GPTBot
  Allow: /

  User-agent: ChatGPT-User
  Allow: /

  User-agent: OAI-SearchBot
  Allow: /

  User-agent: ClaudeBot
  Allow: /

  User-agent: Claude-SearchBot
  Allow: /

  User-agent: Claude-User
  Allow: /

  User-agent: Googlebot
  Allow: /

  User-agent: Google-Extended
  Allow: /

  User-agent: PerplexityBot
  Allow: /

  User-agent: Bingbot
  Allow: /

  # Grok tokens — verify first-party docs or server-log evidence before use.
  User-agent: GrokBot
  Allow: /

  User-agent: xAI-Grok
  Allow: /

  User-agent: Grok-DeepSearch
  Allow: /

  Sitemap: https://[도메인]/sitemap.xml
  ```

### Strategy B — 검색만 허용 (학습 차단)
  ```
  # Training bots — blocked
  User-agent: GPTBot
  Disallow: /

  User-agent: ClaudeBot
  Disallow: /

  User-agent: Google-Extended
  Disallow: /

  # Grok tokens — verify first-party docs or server-log evidence before use.
  User-agent: GrokBot
  Disallow: /

  # Search bots — allowed
  User-agent: OAI-SearchBot
  Allow: /

  User-agent: ChatGPT-User
  Allow: /

  User-agent: Claude-SearchBot
  Allow: /

  User-agent: Claude-User
  Allow: /

  User-agent: Googlebot
  Allow: /

  User-agent: PerplexityBot
  Allow: /

  User-agent: Bingbot
  Allow: /

  User-agent: xAI-Grok
  Allow: /

  User-agent: Grok-DeepSearch
  Allow: /

  Sitemap: https://[도메인]/sitemap.xml
  ```

검증: `curl -A "GPTBot" https://[도메인]/robots.txt`

---

## Critical Issues

### [WARNING] llms.txt 없음
현재: /llms.txt → 404
해결:
  ```
  # llms.txt — [사이트명]
  > [사이트 설명]

  ## 주요 섹션
  - [섹션명]: [URL]

  ## Optional
  - Sitemap: [URL]
  ```
배포: 사이트 루트에 정적 파일로 제공
검증: `curl -I https://[도메인]/llms.txt`

---

## 구현 우선순위

| 우선순위 | 작업 | 난이도 | 예상 크롤러 효과 | 담당 |
|---|---|---|---|---|
| 1 | robots.txt 전략 적용 | 낮음 | 높음 | DevOps / 운영 |
| 2 | llms.txt 생성 및 배포 | 낮음 | 보통 | FE / 운영 |
| 3 | sitemap.xml robots.txt 등록 | 낮음 | 보통 | DevOps |
| 4 | JS 의존 콘텐츠 SSR 전환 | 높음 | 높음 | FE |
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
