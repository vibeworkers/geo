---
name: geo-technical
description: >
  기술 SEO 평가. 크롤링·색인 가능성, hreflang·다국어 URL 구조, 페이지 속도, 모바일 최적화, 보안·URL 구조를
  기술적으로 진단하고 수정 방법을 제공한다.
  다국어 사이트(SITE_LANGS 2개 이상)는 hreflang 분석 모듈(x-default·양방향 참조·언어-지역 코드 정확성)을 추가 실행한다.
  L2는 FTP·CMS 수정 방법, L3는 코드 스니펫과 서버 설정까지 포함한다.
  L1(마케팅 담당자)은 이 스킬 대신 geo-audit 결과의 개발팀 전달 목록을 활용한다.
  트리거: "기술 SEO", "페이지 속도", "Core Web Vitals", "크롤링", "hreflang", "다국어 URL", "technical", "/geo technical".
audience: L2, L3
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# geo-technical — 기술 SEO 평가

> 실행 시 USER_LEVEL을 확인한다.
> L1인 경우 아래 안내 메시지를 출력하고 실행을 중단한다.
> L2 또는 L3인 경우 아래 단계를 순서대로 실행한다.
> 결과는 USER_LEVEL에 맞는 출력 템플릿으로 전달하고 `GEO-기술SEO-분석.md`로 저장한다.

---

## L1 접근 안내 (L1이면 이 메시지 출력 후 중단)

```
기술 SEO 진단은 서버 설정·코드 수정이 필요한 기술 작업입니다.

현재 레벨(마케팅 담당자)에서는 직접 실행이 어렵습니다.

선택 사항:
1. 레벨을 변경하려면 `/geo level` 을 입력하세요.
2. 개발팀 또는 운영팀에 아래 내용을 전달하세요:

   "사이트의 기술 SEO 상태(페이지 속도·크롤링·모바일 최적화)를
    점검하고 개선 항목을 알려주세요.
    명령어: /geo technical https://[도메인]"
```

---

## 실행 단계

### 0단계: 렌더링 방식 사전 판정

> 이 단계를 가장 먼저 실행한다. 순수 CSR 판정 시 이후 모든 항목에 경고를 삽입한다.

HTML 응답 본문을 기준으로 렌더링 방식을 판정한다.

| 렌더링 상태 | 판정 기준 | 결과 | 점수 조정 |
|---|---|---|---|
| SSR / SSG | HTML body에 실제 텍스트 콘텐츠 존재, `__NEXT_DATA__`·`__NUXT__` 스크립트 태그 존재 | PASS | 정상 채점 |
| 하이브리드 | 핵심 콘텐츠는 SSR, 일부 동적 컴포넌트는 CSR | WARNING | 스키마·메타 항목에 경고 추가 |
| CSR + SSR 신호 | 빈 루트 + `__NEXT_DATA__`·`__NUXT__` 등 SSR 신호 존재 | WARNING | 동일 |
| 순수 CSR | `<div id="root">`, `<div id="app">`, `<app-root>` 등 빈 루트 엘리먼트, body 텍스트 극소량 | **CRITICAL** | 전체 출력 상단에 경고 배너 삽입 |

**감지 방법:**
- `<div id="root">` / `<div id="app">` / `<app-root>` 빈 루트 엘리먼트 확인
- `__NEXT_DATA__` / `__NUXT__` 스크립트 태그 — SSR 신호
- HTML `<body>` 내 실제 텍스트 분량 확인 (200자 미만이면 CSR 의심)
- `<noscript>` 태그 대체 콘텐츠 존재 여부

**순수 CSR 판정 시 경고 배너 (보고서 최상단에 삽입):**

```
> ⚠ [CRITICAL] 순수 CSR 감지
> AI 크롤러(GPTBot·ClaudeBot·PerplexityBot 등)는 JavaScript를 실행하지 않으므로
> 이 페이지의 콘텐츠에 접근할 수 없습니다.
> 아래 점수는 실제보다 낮게 평가될 수 있으며, SSR/SSG 전환이 최우선 과제입니다.
```

---

### 1단계: 기술 상태 수집

> **Claude Code 환경:** 아래 Bash 스크립트 실행 (HTTP 헤더·응답 시간·상태 코드 정확히 수집)
> **Claude 웹 환경:** WebFetch로 기본 확인 후 외부 도구로 보완
> - 응답 시간·HTTP 헤더 확인: https://httpstatus.io/
> - Core Web Vitals 측정: https://pagespeed.web.dev/

**Claude Code 환경 (Bash)**

```bash
python3 -c "
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import time

url = '[TARGET_URL]'
parsed = urlparse(url)
base = f'{parsed.scheme}://{parsed.netloc}'

# 응답 속도 측정
start = time.time()
r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=30)
elapsed = round((time.time() - start) * 1000)

print(f'HTTP Status: {r.status_code}')
print(f'Response Time: {elapsed}ms')
print(f'HTTPS: {url.startswith(\"https\")}')
print(f'Content-Type: {r.headers.get(\"Content-Type\", \"없음\")}')
print(f'X-Robots-Tag: {r.headers.get(\"X-Robots-Tag\", \"없음\")}')
print(f'Content-Length: {r.headers.get(\"Content-Length\", \"없음\")}')
print('---')

# 주요 파일 확인
for path in ['/robots.txt', '/sitemap.xml', '/sitemap_index.xml']:
    pr = requests.get(base + path, timeout=15)
    print(f'{path}: {pr.status_code}')

print('---')

# hreflang 태그 수집
soup = BeautifulSoup(r.text, 'html.parser')
html_lang = soup.find('html').get('lang', '없음') if soup.find('html') else '없음'
print(f'html lang 속성: {html_lang}')
hreflangs = soup.find_all('link', rel='alternate')
hreflang_tags = [t for t in hreflangs if t.get('hreflang')]
print(f'hreflang 태그 수: {len(hreflang_tags)}개')
has_x_default = False
langs = []
for tag in hreflang_tags:
    lang = tag.get('hreflang', '')
    href = tag.get('href', '')
    if lang == 'x-default':
        has_x_default = True
    langs.append(lang)
    print(f'  hreflang=\"{lang}\" href=\"{href}\"')
print(f'x-default: {\"있음\" if has_x_default else \"없음\"}')
print(f'감지된 언어: {langs}')
"
```

**Claude 웹 환경 (WebFetch 대체)**

WebFetch로 아래 URL을 순서대로 로드한다.
- 대상 URL (홈페이지 HTML 확인)
- `https://[도메인]/robots.txt`
- `https://[도메인]/sitemap.xml`

수집 불가 항목 (외부 도구 활용):
- HTTP 헤더·X-Robots-Tag·응답 시간 → https://httpstatus.io/
- Core Web Vitals (LCP·CLS·INP) → https://pagespeed.web.dev/

WebFetch로 홈페이지 HTML을 로드하고 다음을 확인한다.

- `<meta name="viewport">` — 모바일 대응 여부
- `<meta name="robots">` — noindex, nofollow 여부
- `<link rel="canonical">` — canonical 설정
- `<html lang="">` — 언어 속성
- `<link rel="alternate" hreflang="...">` — hreflang 태그 목록 및 x-default 존재 여부
- 이미지 `alt` 속성 누락 수
- `<title>` 길이 (60자 이내 권장)
- `<meta name="description">` 길이 (160자 이내 권장)
- 깨진 링크 여부 (내부 링크 href 확인)
- JavaScript 렌더링 의존도 (noscript 내 콘텐츠 존재 여부)

---

### 1-1단계: hreflang 분석 (SITE_LANGS 2개 이상인 경우에만 실행)

> 단일 언어 사이트(SITE_LANGS = ["ko"] 등 1개)는 이 단계를 건너뛰고 hreflang 항목 20점 전체 산입.

`references/hreflang-checklist.md` 기준으로 아래 항목을 검사한다.

#### 필수 항목 (F1–F5) — 총 16점

| 코드 | 항목 | 기준 | 배점 |
|---|---|---|---|
| F1 | x-default 설정 | `hreflang="x-default"` 태그 존재 | 4점 |
| F2 | 모든 언어 버전 hreflang 태그 | SITE_LANGS 각 언어에 태그 존재 | 3점 |
| F3 | 언어-지역 코드 정확성 | ISO 639-1 (+ISO 3166-1) 형식, 언더스코어·대문자·3자리 코드 금지 | 3점 |
| F4 | 양방향 참조 완성 | A→B 참조 시 B→A 참조도 존재 | 4점 |
| F5 | 자기 참조(self-reference) | 각 페이지가 자신의 URL도 hreflang에 포함 | 2점 |

#### URL 일관성 항목 (U1–U4) — 총 4점

| 코드 | 항목 | 기준 | 배점 |
|---|---|---|---|
| U1 | 절대 URL 사용 | `https://example.com/ko/` 형태 (상대 URL 금지) | 1점 |
| U2 | canonical 충돌 없음 | hreflang URL과 canonical URL 일치 | 1점 |
| U3 | 실제 200 응답 | hreflang 명시 URL이 리다이렉트 없이 200 응답 | 1점 |
| U4 | robots.txt 차단 없음 | 언어 버전 URL이 robots.txt에 차단되지 않음 | 1점 |

**hreflang 소계: [합산]/20점**

---

### 2단계: 기술 SEO 평가 (다국어 사이트: 4개 차원 × 20점 / 단일 언어: 4개 차원 × 25점)

> **다국어 사이트 (SITE_LANGS 2개 이상):** 각 차원 0–20점, hreflang 20점 별도 → 합산 100점  
> **단일 언어 사이트:** 각 차원 0–25점 → 합산 100점

#### 크롤링·색인 가능성 — 0~25점 (단일 언어) / 0~20점 (다국어)

> hreflang은 1-1단계에서 별도 20점으로 평가한다. 다국어 사이트는 이 차원을 20점 기준으로 환산한다.

| 신호 | 확인 항목 | 기준 |
|---|---|---|
| robots.txt | 존재 및 AI 봇 허용 여부 | 존재 + 핵심 봇 허용 |
| sitemap.xml | 존재 및 robots.txt 등록 | 존재 + Sitemap: 지시자 |
| noindex | 주요 페이지 noindex 미설정 | meta 및 X-Robots-Tag 모두 확인 |
| canonical | 중복 URL 정리 여부 | 자기 참조 canonical 권장 |
| 색인 깊이 | 주요 콘텐츠 클릭 3회 이내 도달 | 3클릭 이내 접근 가능 |

#### 페이지 속도·성능 — 0~25점 (단일 언어) / 0~20점 (다국어)

Core Web Vitals 기준으로 평가한다. (Google 2024 기준)

| 지표 | 양호 기준 | 개선 필요 | 불량 |
|---|---|---|---|
| LCP (최대 콘텐츠 렌더링) | 2.5초 이내 | 2.5–4초 | 4초 초과 |
| CLS (누적 레이아웃 변화) | 0.1 이하 | 0.1–0.25 | 0.25 초과 |
| INP (다음 페인트 반응성) | 200ms 이하 | 200–500ms | 500ms 초과 |

> 실제 Core Web Vitals 측정은 PageSpeed Insights 또는 CrUX 데이터가 필요하다.
> 수집 불가 시 응답 시간·HTML 크기·이미지 최적화 여부로 간접 추정한다.

| 신호 | 확인 항목 |
|---|---|
| 서버 응답 시간 | 200ms 이내 여부 |
| 이미지 포맷 | WebP 또는 AVIF 사용 여부 |
| 이미지 크기 | width·height 속성 명시 여부 (CLS 방지) |
| JavaScript 차단 | render-blocking JS 여부 |
| 브라우저 캐싱 | Cache-Control 헤더 설정 여부 |

#### 모바일·접근성 — 0~25점 (단일 언어) / 0~20점 (다국어)

| 신호 | 확인 항목 |
|---|---|
| viewport 메타 태그 | `content="width=device-width, initial-scale=1"` |
| 터치 요소 간격 | 버튼·링크 44px 이상 |
| 폰트 크기 | 본문 16px 이상 |
| 가로 스크롤 | 모바일에서 가로 스크롤 없음 |
| 언어 속성 | `<html lang="ko">` 또는 해당 언어 코드 |
| alt 텍스트 | 모든 이미지 alt 속성 존재 |

#### 보안·URL 구조 — 0~25점 (단일 언어) / 0~20점 (다국어)

| 신호 | 확인 항목 |
|---|---|
| HTTPS | 전체 사이트 HTTPS 제공 여부 |
| HTTP → HTTPS 리다이렉트 | HTTP 요청 시 301 리다이렉트 여부 |
| URL 소문자 | URL이 소문자로 통일되어 있는가 |
| URL 특수문자 | 한글·공백 없이 슬러그 사용 여부 |
| 불필요한 파라미터 | 세션 ID 등 색인 불필요한 파라미터 제거 여부 |
| 4xx 오류 | 주요 내부 링크 404 없음 여부 |

---

### 3단계: 기술 점수 산출

**단일 언어 사이트 (SITE_LANGS 1개)**

```
기술 점수(100) = (크롤링색인/25 × 30) +
                 (속도성능/25 × 30) +
                 (모바일접근성/25 × 25) +
                 (보안URL/25 × 15)
```

**다국어 사이트 (SITE_LANGS 2개 이상)**

```
기술 점수(100) = hreflang(0~20) +
                 (크롤링색인/20 × 20) +
                 (속도성능/20 × 20) +
                 (모바일접근성/20 × 20) +
                 (보안URL/20 × 20)
```

크롤링 가능성과 속도가 동등하게 가장 큰 비중을 차지한다. 다국어 사이트는 hreflang이 크롤링 차원과 동등한 비중(각 20점)을 가진다.

**점수 등급표**

| 점수 | 등급 | 상태 |
|---|---|---|
| 80–100 | 우수 | 기술 SEO 최적화 완료 |
| 60–79 | 양호 | 일부 개선 여지 있음 |
| 40–59 | 보통 | 주요 기술 이슈 존재 |
| 20–39 | 미흡 | 즉각적인 기술 조치 필요 |
| 0–19 | 위험 | 기술 문제로 AI·검색 접근 심각 |

---

### 4단계: 레벨별 보고서 출력

아래 출력 템플릿에 따라 보고서를 작성하고 `GEO-기술SEO-분석.md`로 저장한다.

---

## 레벨별 출력 템플릿

---

### L2 출력 — 웹마스터 / 운영자

점수와 함께 FTP·CMS에서 직접 수정할 수 있는 방법을 단계별로 안내한다.
각 문제의 수정 전후 내용을 명확히 보여준다.

```markdown
# [사이트명] 기술 SEO 분석

분석일: [날짜]  |  URL: [URL]

---

## 기술 점수: [점수]/100 — [등급]

| 차원 | 점수 | 주요 발견 |
|---|---|---|
| 크롤링·색인 가능성 | [X]/25 | [발견 사항 한 줄] |
| 페이지 속도·성능 | [X]/25 | [발견 사항 한 줄] |
| 모바일·접근성 | [X]/25 | [발견 사항 한 줄] |
| 보안·URL 구조 | [X]/25 | [발견 사항 한 줄] |

---

## 우선순위별 수정 과제

### 즉시 처리 가능

**1. [문제 제목]**
- 현재 상태: [설명]
- 수정 방법:
  1. FTP 접속 → [경로] 이동
  2. [파일명] 열기
  3. 다음 내용 수정:
     ```
     [수정 전]
     ```
     ↓ 변경
     ```
     [수정 후]
     ```
  4. 저장 후 브라우저에서 확인
- WordPress 사용 시: [플러그인 또는 메뉴 경로]
- 소요 시간: [예상 시간]
- 예상 효과: [효과]

**2. [문제 제목]**
[동일 형식]

### 개발팀 요청 사항

**[문제 제목]**
- 현재 상태: [설명]
- 요청 내용: [개발팀에 전달할 내용]
- 우선순위: [높음 / 보통]

---

## 기술 지표 요약

| 지표 | 현재 값 | 기준 | 평가 |
|---|---|---|---|
| 서버 응답 시간 | [X]ms | 200ms 이내 | 통과 / 개선 필요 |
| HTTPS | [예 / 아니오] | 필수 | 통과 / 개선 필요 |
| viewport 태그 | [있음 / 없음] | 필수 | 통과 / 개선 필요 |
| sitemap.xml | [있음 / 없음] | 권장 | 통과 / 개선 필요 |
| robots.txt | [있음 / 없음] | 권장 | 통과 / 개선 필요 |
| 이미지 alt 누락 | [X]개 | 0개 | 통과 / 개선 필요 |
| hreflang (다국어) | [X]/20점 또는 해당 없음 | x-default·양방향 참조 필수 | 통과 / 개선 필요 / 해당 없음 |
```

---

### L3 출력 — 개발자

전체 기술 명세, HTTP 헤더 분석, 수정 코드 스니펫을 포함한다.

```markdown
# [사이트명] Technical SEO Analysis

Date: [날짜]  |  URL: [URL]

---

## Technical Score: [점수]/100

**단일 언어 사이트 (4 dimensions × 25pts)**

| Dimension | Score | Key Findings | Action Required |
|---|---|---|---|
| Crawlability & Indexability | [X]/25 | [발견 목록] | [조치 목록] |
| Page Speed & Performance | [X]/25 | [발견 목록] | [조치 목록] |
| Mobile & Accessibility | [X]/25 | [발견 목록] | [조치 목록] |
| Security & URL | [X]/25 | [발견 목록] | [조치 목록] |

**다국어 사이트 (hreflang 20pts + 4 dimensions × 20pts)**

| Dimension | Score | Key Findings | Action Required |
|---|---|---|---|
| hreflang & Multilingual URL | [X]/20 | [발견 목록] | [조치 목록] |
| Crawlability & Indexability | [X]/20 | [발견 목록] | [조치 목록] |
| Page Speed & Performance | [X]/20 | [발견 목록] | [조치 목록] |
| Mobile & Accessibility | [X]/20 | [발견 목록] | [조치 목록] |
| Security & URL | [X]/20 | [발견 목록] | [조치 목록] |

---

## HTTP Response Analysis

```
URL: [URL]
Status: [200 / 301 / 404]
Response Time: [X]ms
Content-Type: [값]
X-Robots-Tag: [값 또는 없음]
Cache-Control: [값 또는 없음]
Strict-Transport-Security: [값 또는 없음]
```

---

## hreflang Analysis (다국어 사이트만 해당 — SITE_LANGS 2개 이상)

> 단일 언어 사이트면 이 섹션을 생략한다.

| Check | Code | Result | Score |
|---|---|---|---|
| x-default 설정 | F1 | Pass / Fail | /4 |
| 언어 버전 hreflang 존재 | F2 | Pass / Fail | /3 |
| 언어-지역 코드 정확성 | F3 | Pass / Fail | /3 |
| 양방향 참조 완성 | F4 | Pass / Fail | /4 |
| 자기 참조 포함 | F5 | Pass / Fail | /2 |
| 절대 URL 사용 | U1 | Pass / Fail | /1 |
| canonical 충돌 없음 | U2 | Pass / Fail | /1 |
| 실제 200 응답 | U3 | Pass / Fail | /1 |
| robots.txt 차단 없음 | U4 | Pass / Fail | /1 |
| **합계** | | | **/20** |

**감지된 hreflang 태그:**
```
[hreflang="ko-KR" href="https://example.com/ko/"]
[hreflang="en-US" href="https://example.com/en/"]
[hreflang="x-default" href="https://example.com/"]
```

**URL 구조:** [서브디렉토리 / 서브도메인 / ccTLD / 쿼리 파라미터] — [GEO 권장도: 높음 / 보통 / 낮음]

---

## Critical Issues

### [CRITICAL] HTTPS 미적용
현재: HTTP로 서비스 중
영향: 보안 취약, 브라우저 경고, 검색·AI 신뢰도 감소
해결 (Nginx):
  ```nginx
  server {
      listen 80;
      server_name [도메인];
      return 301 https://$host$request_uri;
  }
  ```
해결 (Apache .htaccess):
  ```apache
  RewriteEngine On
  RewriteCond %{HTTPS} off
  RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
  ```
검증: `curl -I http://[도메인]`

### [CRITICAL] noindex 설정 감지
현재: `<meta name="robots" content="noindex">` 또는 X-Robots-Tag: noindex
영향: 검색 엔진 및 AI 크롤러 색인 불가
해결: 해당 태그 제거 또는 조건부 적용 로직 수정
검증: `curl -I [URL] | grep -i x-robots`

### [WARNING] sitemap.xml robots.txt 미등록
현재: robots.txt에 Sitemap 지시자 없음
영향: 크롤러가 sitemap을 자동 발견하지 못함
해결:
  ```
  # robots.txt 하단에 추가
  Sitemap: https://[도메인]/sitemap.xml
  ```

### [WARNING] 이미지 alt 텍스트 누락 ([X]개)
현재: alt 속성 없는 이미지 [X]개 발견
영향: 접근성 불량, 이미지 SEO 감점
해결 예시:
  ```html
  <!-- 수정 전 -->
  <img src="/images/product.jpg">

  <!-- 수정 후 -->
  <img src="/images/product.jpg" alt="[설명적인 alt 텍스트]" width="800" height="600">
  ```

---

## Core Web Vitals 추정

| Metric | Estimated | Target | Status |
|---|---|---|---|
| LCP | [추정값 또는 측정 필요] | ≤ 2.5s | [Pass / Fail / Unknown] |
| CLS | [추정값 또는 측정 필요] | ≤ 0.1 | [Pass / Fail / Unknown] |
| INP | [추정값 또는 측정 필요] | ≤ 200ms | [Pass / Fail / Unknown] |

> 정확한 측정: https://pagespeed.web.dev/ 또는 Google Search Console → Core Web Vitals

---

## 구현 우선순위

| 우선순위 | 작업 | 파일/위치 | 난이도 | 담당 |
|---|---|---|---|---|
| 1 | [작업] | [파일] | 낮음 / 보통 / 높음 | [FE/BE/DevOps] |
| 2 | [작업] | [파일] | [난이도] | [담당] |
| 3 | [작업] | [파일] | [난이도] | [담당] |
```
