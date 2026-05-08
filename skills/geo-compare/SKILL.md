---
name: geo-compare
description: >
  자사 URL과 경쟁사 URL의 GEO 신호를 항목별로 비교 분석한다.
  사이트 설정(도메인 루트 기준)과 페이지 콘텐츠(입력 URL 기준)를 분리하여
  각각 30점으로 평가하고 경쟁사 대비 격차를 도출한다.
  L2(웹마스터·운영자)와 L3(개발자) 전용 스킬.
  트리거: "경쟁사 비교", "GEO 비교", "compare".
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# geo-compare — GEO 경쟁 비교 분석

> 이 서브스킬은 `cogarch` 없이 직접 열어도 닫히는 standalone GEO 실행 계약이다.
> 숨은 레벨 세션 상태를 요구하지 않는다. 요청에 수신자 맥락이 없으면 이 문서 안에서 `L1`(manager), `L2`(operator), `L3`(builder) 중 하나의 수신자 레벨을 직접 정한다.
> `L1`로 판단되면 아래 안내 메시지를 출력하고 실행을 중단한다.
> `L2` 또는 `L3`로 판단되면 아래 단계를 순서대로 실행한다.
> 결과는 `GEO-비교분석-[자사도메인]-vs-[경쟁사도메인].md`로 저장한다.

---

## L1 접근 안내 (L1이면 이 메시지 출력 후 중단)

```
경쟁사 비교는 기술 신호 수집이 필요한 분석입니다.

현재 레벨(마케팅 담당자)에서는 직접 실행이 어렵습니다.

선택 사항:
1. 이 작업을 다시 요청할 때 `L2 운영자 프로필로 진행해 주세요.` 또는 `L3 개발자 프로필로 진행해 주세요.`처럼 수신자 레벨을 직접 명시하세요.
2. 개발팀 또는 운영팀에 아래 내용을 전달하세요:

   "자사 사이트와 경쟁사 사이트의 AI 검색 최적화 현황을 비교해 주세요.
    분석 항목: robots.txt 크롤러 정책, llms.txt, 스키마 마크업, 콘텐츠 구조"
```

---

## 점수 구조

비교는 두 레벨로 분리하여 평가한다.

| 레벨 | 기준 | 영역 | 만점 |
|---|---|---|---|
| **사이트 설정** | 도메인 루트 | AI 크롤러 접근성 / AI 안내 파일 / 사이트 기술 기반 | 30점 |
| **페이지 콘텐츠** | 입력 URL | 스키마 마크업 / 콘텐츠 구조 / 페이지 기술 신호 | 30점 |

사이트 설정과 페이지 콘텐츠는 성격이 다르므로 합산하지 않고 각각 표시한다.
경쟁 비교에서 platform, regional, private, policy 차이가 보이면
`../../references/platform-truth-registry.md`,
`../../references/regional-situational-routing.md`,
`../../references/private-surface-routing.md`,
`../../references/policy-risk-gate.md` 중 해당 reference를 함께 표시한다.
observed answer, citation, referral, conversion 비교는
`../../references/measurement-capture-template.md`가 있을 때만 측정된
결과로 보고한다.

---

## 실행 단계

### 0단계: 비교 대상 확인

사용자가 두 URL을 제공했는지 확인한다.

- **자사 URL**: 분석 및 개선 대상
- **경쟁사 URL**: 벤치마크 기준 (1개 이상, 최대 3개 권장)

URL이 제공되지 않은 경우:
```
비교할 URL을 알려주세요.

예: https://mysite.com/blog/post-A 와 https://competitor.com/blog/post-B 비교
```

---

### 1단계: 사이트 설정 수집 (도메인 루트 기준)

입력 URL에서 도메인을 추출하여 루트 경로의 파일을 수집한다.

**수집 항목:** robots.txt, llms.txt, llms-full.txt, sitemap.xml

**Claude Code 환경 (Bash)**

```bash
python3 -c "
import requests
from urllib.parse import urlparse

urls = ['[자사_URL]', '[경쟁사_URL]']

for url in urls:
    parsed = urlparse(url)
    base = f'{parsed.scheme}://{parsed.netloc}'
    print(f'\n=== 사이트 설정: {parsed.netloc} ===')

    site_targets = {
        'robots.txt': base + '/robots.txt',
        'llms.txt': base + '/llms.txt',
        'llms-full.txt': base + '/llms-full.txt',
        'sitemap.xml': base + '/sitemap.xml',
    }

    for name, target_url in site_targets.items():
        try:
            r = requests.get(target_url, headers={'User-Agent':'GEO-Audit/1.0'}, timeout=15)
            preview = r.text[:600].replace('\n', ' ') if r.status_code == 200 else ''
            print(f'  {name}: {r.status_code}  {preview}')
        except Exception as e:
            print(f'  {name}: ERROR {e}')

    # HTTPS 확인
    http_url = f'http://{parsed.netloc}/'
    try:
        r = requests.get(http_url, allow_redirects=False, timeout=10)
        https_redirect = r.status_code in (301, 302) and 'https' in r.headers.get('Location', '')
        print(f'  HTTP→HTTPS 리다이렉트: {https_redirect}')
    except Exception as e:
        print(f'  HTTPS 확인 ERROR: {e}')
"
```

**Claude 웹 환경 (WebFetch 대체)**

> 각 도메인에 대해 순서대로 WebFetch로 로드한다.
> - `https://[자사도메인]/robots.txt`
> - `https://[자사도메인]/llms.txt`
> - `https://[자사도메인]/sitemap.xml`
> - 경쟁사 도메인도 동일하게 반복
>
> HTTP 상태 코드 직접 확인이 필요한 경우: https://httpstatus.io/

---

### 2단계: 페이지 콘텐츠 수집 (입력 URL 기준)

입력된 URL 그대로 각 페이지의 HTML을 수집한다.

**수집 항목:** 스키마 마크업 종류, OG/Twitter 메타태그, canonical, 콘텐츠 구조

**Claude Code 환경 (Bash)**

```bash
python3 -c "
import requests, re
from urllib.parse import urlparse

urls = ['[자사_URL]', '[경쟁사_URL]']

for url in urls:
    print(f'\n=== 페이지 콘텐츠: {url} ===')
    try:
        r = requests.get(url, headers={'User-Agent':'GEO-Audit/1.0'}, timeout=15)
        html = r.text

        # 스키마 마크업
        schema_blocks = re.findall(r'application/ld\+json.*?</script>', html, re.DOTALL)
        schema_types = re.findall(r'\"@type\"\s*:\s*\"([^\"]+)\"', html)
        print(f'  스키마 블록: {len(schema_blocks)}개  타입: {list(set(schema_types))}')

        # 메타태그
        og_title = bool(re.search(r'og:title', html))
        og_desc = bool(re.search(r'og:description', html))
        og_image = bool(re.search(r'og:image', html))
        twitter = bool(re.search(r'twitter:card', html))
        canonical = bool(re.search(r'rel=[\"\\']canonical', html))
        print(f'  OG(title·desc·image): {og_title}·{og_desc}·{og_image}  Twitter: {twitter}  canonical: {canonical}')

        # 콘텐츠 구조
        h1 = len(re.findall(r'<h1[ >]', html))
        h2 = len(re.findall(r'<h2[ >]', html))
        faq = bool(re.search(r'FAQPage|faq|자주\s*묻는', html, re.IGNORECASE))
        author = bool(re.search(r'author|byline|작성자', html, re.IGNORECASE))
        print(f'  H1: {h1}  H2: {h2}  FAQ: {faq}  저자: {author}')
    except Exception as e:
        print(f'  ERROR: {e}')
"
```

**Claude 웹 환경 (WebFetch 대체)**

> 자사 URL → 경쟁사 URL 순서로 WebFetch로 로드한다.
> 각 페이지에서 스키마 블록(`application/ld+json`), OG 태그, canonical, 제목 구조를 확인한다.

---

### 3단계: 6개 영역 비교 평가

#### 사이트 설정 영역 (도메인 루트 기준 — 합계 30점)

**S1. AI 크롤러 접근성 (0~10점)** — robots.txt 기반

| 확인 항목 | 배점 |
|---|---|
| 학습용 봇(GPTBot·ClaudeBot) 허용 또는 의도적 차단 근거 명시 | 2점 |
| 검색/사용자 요청 봇(OAI-SearchBot·ChatGPT-User·Claude-SearchBot·Claude-User·PerplexityBot·Bingbot) 허용 | 4점 |
| Googlebot 접근 및 색인 가능성 확보 | 2점 |
| Google-Extended 처리 명확. Gemini 학습/grounding 제어이며 Google Search 포함·순위와 분리 | 1점 |
| Grok 계열 토큰은 first-party 근거 확인 또는 `확인 필요`로 표기 | 1점 |

**S2. AI 안내 파일 (0~10점)** — llms.txt 기반

| 확인 항목 | 배점 |
|---|---|
| llms.txt 존재. heuristic / adoption-dependent 신호이며 AI 수집·인용을 보장하지 않음 | 3점 |
| 사이트 설명·주요 URL·Sitemap 포함 (품질) | 5점 |
| llms-full.txt 존재 | 2점 |

**S3. 사이트 기술 기반 (0~10점)** — 도메인 루트 기반

| 확인 항목 | 배점 |
|---|---|
| HTTPS 적용 및 HTTP→HTTPS 리다이렉트 | 4점 |
| sitemap.xml 존재 | 3점 |
| www/non-www 리다이렉트 통일 | 3점 |

---

#### 페이지 콘텐츠 영역 (입력 URL 기준 — 합계 30점)

**P1. 스키마 마크업 (0~10점)** — 페이지 HTML 기반

| 확인 항목 | 배점 |
|---|---|
| Article 또는 BlogPosting (datePublished·author 포함) | 2점 |
| FAQPage 또는 HowTo | 2점 |
| Organization (name·url·logo·sameAs 포함) | 2점 |
| speakable 속성 | 2점 |
| BreadcrumbList | 2점 |

**P2. 콘텐츠 구조 (0~10점)** — 페이지 HTML 기반

| 확인 항목 | 배점 |
|---|---|
| 직접 답변 가능한 정의 문장 또는 FAQ 블록 | 3점 |
| 명확한 제목 계층 구조 (H1 1개, H2 복수) | 3점 |
| 통계·출처 링크 포함 | 2점 |
| 저자명·작성일 명시 | 2점 |

**P3. 페이지 기술 신호 (0~10점)** — 페이지 HTML 기반

| 확인 항목 | 배점 |
|---|---|
| Open Graph 완비 (og:title·og:description·og:image·og:url) | 4점 |
| Twitter Card (twitter:card·twitter:title) | 2점 |
| canonical 태그 | 2점 |
| 저자 Person 스키마 또는 바이라인 | 2점 |

---

### 4단계: 비교 점수 산출

```
사이트 설정 점수 = S1 + S2 + S3  (만점 30점)
페이지 콘텐츠 점수 = P1 + P2 + P3  (만점 30점)
```

**격차 분석:**
- 자사 점수 − 경쟁사 점수 = 격차
- 양수(+): 자사 우위 영역 → 유지
- 음수(−): 경쟁사 우위 영역 → 개선 대상

---

### 5단계: 레벨별 보고서 출력

아래 출력 템플릿에 따라 보고서를 작성하고 저장한다.

---

## 레벨별 출력 템플릿

---

### L2 출력 — 웹마스터 / 운영자

```markdown
# GEO 경쟁 비교 분석

분석일: [날짜]
자사: [자사 URL]  |  경쟁사: [경쟁사 URL]

---

## 사이트 설정 비교 (도메인 루트 기준)

| 영역 | 자사 | 경쟁사 | 격차 |
|---|---|---|---|
| AI 크롤러 접근성 (robots.txt) | [X]/10 | [X]/10 | [+/-X] |
| AI 안내 파일 (llms.txt) | [X]/10 | [X]/10 | [+/-X] |
| 사이트 기술 기반 (HTTPS·sitemap) | [X]/10 | [X]/10 | [+/-X] |
| **사이트 설정 합계** | **[X]/30** | **[X]/30** | **[+/-X]** |

---

## 페이지 콘텐츠 비교 (입력 URL 기준)

| 영역 | 자사 | 경쟁사 | 격차 |
|---|---|---|---|
| 스키마 마크업 | [X]/10 | [X]/10 | [+/-X] |
| 콘텐츠 구조 | [X]/10 | [X]/10 | [+/-X] |
| 페이지 기술 신호 (OG·canonical) | [X]/10 | [X]/10 | [+/-X] |
| **페이지 콘텐츠 합계** | **[X]/30** | **[X]/30** | **[+/-X]** |

---

## 경쟁사 우위 항목 (격차 큰 순)

### 1. [영역명] — [격차]점 뒤처짐

**경쟁사 현황:** [경쟁사가 갖추고 있는 것]
**자사 현황:** [자사 누락 항목]
**수정 방법 (WordPress/FTP 기준):**
1. [구체적 단계]
2. [구체적 단계]
**예상 소요:** [시간/난이도]

### 2. [영역명] — [격차]점 뒤처짐

**경쟁사 현황:** [설명]
**자사 현황:** [설명]
**수정 방법:**
1. [단계]

---

## 자사 우위 항목 (유지 권고)

| 항목 | 자사 현황 | 권고 |
|---|---|---|
| [항목] | [현황] | 유지 |

---

## 즉시 실행 가능한 개선 (이번 주)

1. **[작업 제목]** — 사이트 설정 / 페이지 콘텐츠
   - 방법: [단계별 안내]
   - 효과: 경쟁사 대비 [X]점 격차 해소

2. **[작업 제목]**
   - 방법: [안내]
   - 효과: [효과]
```

---

### L3 출력 — 개발자

```markdown
# GEO Competitive Analysis

Date: [날짜]
Self: [자사 URL]  vs  Competitor: [경쟁사 URL]

---

## Score Summary

### Site Configuration (Domain Root)

| 영역 | 자사 | 경쟁사 | Gap |
|---|---|---|---|
| AI Crawler Access (robots.txt) | [X]/10 | [X]/10 | [+/-X] |
| AI Guide Files (llms.txt) | [X]/10 | [X]/10 | [+/-X] |
| Site Tech Foundation | [X]/10 | [X]/10 | [+/-X] |
| **Site Config Total** | **[X]/30** | **[X]/30** | **[+/-X]** |

### Page Content (Input URL)

| 영역 | 자사 | 경쟁사 | Gap |
|---|---|---|---|
| Schema Markup | [X]/10 | [X]/10 | [+/-X] |
| Content Structure | [X]/10 | [X]/10 | [+/-X] |
| Page Tech Signals | [X]/10 | [X]/10 | [+/-X] |
| **Page Content Total** | **[X]/30** | **[X]/30** | **[+/-X]** |

---

## Site Configuration Comparison

### robots.txt

**자사 ([도메인]):**
```
[robots.txt 주요 내용]
```

**경쟁사 ([도메인]):**
```
[robots.txt 주요 내용]
```

봇별 허용·차단 차이: [분석]

---

### llms.txt

| 항목 | 자사 | 경쟁사 |
|---|---|---|
| 파일 존재 | ✅ / ❌ | ✅ / ❌ |
| 사이트 설명 (블록쿼트) | ✅ / ❌ | ✅ / ❌ |
| 주요 URL 목록 | [수]개 | [수]개 |
| Sitemap 링크 | ✅ / ❌ | ✅ / ❌ |
| llms-full.txt | ✅ / ❌ | ✅ / ❌ |

---

### Site Tech Foundation

| 항목 | 자사 | 경쟁사 |
|---|---|---|
| HTTPS + HTTP→HTTPS 리다이렉트 | ✅ / ❌ | ✅ / ❌ |
| sitemap.xml | ✅ / ❌ | ✅ / ❌ |
| www 리다이렉트 통일 | ✅ / ❌ | ✅ / ❌ |

---

## Page Content Comparison

### Schema Markup

| Schema Type | 자사 | 경쟁사 |
|---|---|---|
| Article / BlogPosting | ✅ / ❌ | ✅ / ❌ |
| FAQPage / HowTo | ✅ / ❌ | ✅ / ❌ |
| Organization | ✅ / ❌ | ✅ / ❌ |
| speakable | ✅ / ❌ | ✅ / ❌ |
| BreadcrumbList | ✅ / ❌ | ✅ / ❌ |

---

### Page Tech Signals

| Tag / 항목 | 자사 | 경쟁사 |
|---|---|---|
| og:title | ✅ / ❌ | ✅ / ❌ |
| og:description | ✅ / ❌ | ✅ / ❌ |
| og:image | ✅ / ❌ | ✅ / ❌ |
| twitter:card | ✅ / ❌ | ✅ / ❌ |
| canonical | ✅ / ❌ | ✅ / ❌ |
| 저자 Person 스키마 | ✅ / ❌ | ✅ / ❌ |

---

## Critical Gaps (경쟁사 우위 — 자사 누락)

### [CRITICAL] [항목명] — [사이트 설정 / 페이지 콘텐츠]
경쟁사: [구현 현황]
자사: [누락 현황]
영향: [AI 검색에 미치는 영향]
해결:
```[코드 또는 설정 예시]```

---

## Implementation Priority

| 우선순위 | 레벨 | 작업 | 난이도 | 예상 점수 향상 | 담당 |
|---|---|---|---|---|---|
| 1 | 사이트 / 페이지 | [작업] | 낮음 / 보통 / 높음 | +[X]점 | [FE/BE/콘텐츠] |
| 2 | [레벨] | [작업] | [난이도] | +[X]점 | [담당] |
| 3 | [레벨] | [작업] | [난이도] | +[X]점 | [담당] |

---

## 재분석 명령어

```text
# 경쟁사 변경 후 재비교
https://[자사URL] 와 https://[새경쟁사URL] 비교

# 전체 자사 감사
https://[자사URL] 전체 감사
```
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
