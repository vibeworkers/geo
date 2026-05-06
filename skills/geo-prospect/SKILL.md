---
name: geo-prospect
description: >
  잠재 클라이언트 도메인의 GEO 현황을 빠르게 스캔하여 영업 기회를 파악한다.
  전체 감사보다 가볍게 핵심 신호만 확인하고 개선 여지와 제안 포인트를 도출한다.
  단일 도메인 또는 복수 도메인 배치 스캔을 지원한다.
  L3(개발자·컨설턴트) 전용 스킬.
  트리거: "잠재 고객", "영업 스캔", "prospect", "/geo prospect".
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# geo-prospect — 잠재 클라이언트 GEO 빠른 스캔

> 실행 시 USER_LEVEL을 확인한다.
> L1 또는 L2인 경우 아래 안내 메시지를 출력하고 실행을 중단한다.
> L3인 경우 아래 단계를 순서대로 실행한다.
> 결과는 `GEO-잠재고객-[도메인]-[날짜].md`로 저장한다.
> 복수 도메인인 경우 `GEO-잠재고객-배치-[날짜].md`로 저장한다.

---

## L1 / L2 접근 안내 (L1·L2이면 이 메시지 출력 후 중단)

```
GEO 잠재 고객 스캔은 영업·컨설팅 목적의 기술 분석 작업입니다.

현재 레벨에서는 직접 실행이 어렵습니다.

선택 사항:
1. 레벨을 변경하려면 `/geo level` 을 입력하세요.
2. 개발팀 또는 컨설턴트에게 아래 내용을 전달하세요:

   "아래 도메인의 GEO 현황을 빠르게 확인하고 개선 여지를 파악해 주세요.
    명령어: /geo prospect https://[도메인]"
```

---

## 스캔 범위

geo-prospect는 전체 감사(/geo audit)보다 가볍고 빠르다.
영업 판단에 필요한 핵심 신호 10개만 확인하여 개선 여지를 측정한다.

| 신호 | 확인 방법 | 배점 |
|---|---|---|
| HTTPS 적용 | HTTP→HTTPS 리다이렉트 | 10점 |
| robots.txt — AI 봇 허용 | 학습용 + 검색용 봇 차단 여부 | 20점 |
| llms.txt 존재 | 사이트 루트 확인 | 15점 |
| sitemap.xml 존재 | 사이트 루트 확인 | 10점 |
| JSON-LD 스키마 | 홈페이지 스키마 블록 수 | 15점 |
| Open Graph 태그 | og:title·og:description·og:image | 10점 |
| Twitter Card | twitter:card 태그 | 5점 |
| FAQ / HowTo 스키마 | FAQPage·HowTo @type 존재 여부 | 10점 |
| Organization 스키마 | sameAs 포함 여부 | 5점 |

**GEO 현황 점수 = 위 항목 합산 (100점 만점)**

**개선 여지 = 100 − GEO 현황 점수**
점수가 낮을수록 개선 여지가 크고 영업 기회가 많다.

---

## 영업 등급 판정

| GEO 현황 점수 | 개선 여지 | 영업 등급 | 판단 |
|---|---|---|---|
| 0–39 | 61–100 | A급 | 즉시 제안 — 개선 여지 매우 높음 |
| 40–59 | 41–60 | B급 | 부분 제안 — 특정 영역 집중 |
| 60–79 | 21–40 | C급 | 유지 관리 제안 — 모니터링 중심 |
| 80–100 | 0–20 | D급 | 제안 불필요 — 이미 잘 구성됨 |

---

## 실행 단계

### 0단계: 대상 도메인 확인

사용자가 제공한 도메인 목록을 파악한다.

- **단일 스캔:** `/geo prospect https://example.com`
- **배치 스캔:** `/geo prospect https://a.com https://b.com https://c.com`

도메인이 제공되지 않은 경우:
```
스캔할 도메인을 알려주세요.

예:
  /geo prospect https://example.com
  /geo prospect https://a.com https://b.com https://c.com
```

---

### 1단계: 핵심 신호 수집

**Claude Code 환경 (Bash)**

```bash
python3 -c "
import requests, re
from urllib.parse import urlparse

domains = ['[도메인1]', '[도메인2]']  # 배치 스캔 시 복수 입력

results = {}
for domain in domains:
    base = f'https://{domain}' if not domain.startswith('http') else domain
    parsed = urlparse(base)
    origin = f'{parsed.scheme}://{parsed.netloc}'
    r_data = {'domain': parsed.netloc, 'score': 0, 'signals': {}}

    # HTTPS 리다이렉트 확인
    try:
        http_r = requests.get(f'http://{parsed.netloc}/', allow_redirects=False, timeout=10)
        https_ok = http_r.status_code in (301, 302) and 'https' in http_r.headers.get('Location', '')
        r_data['signals']['https'] = https_ok
        if https_ok: r_data['score'] += 10
    except: r_data['signals']['https'] = False

    # 루트 파일 확인
    for path, key, pts in [('/robots.txt','robots',0), ('/llms.txt','llms',15), ('/sitemap.xml','sitemap',10)]:
        try:
            res = requests.get(origin + path, headers={'User-Agent':'GEO-Prospect/1.0'}, timeout=10)
            exists = res.status_code == 200
            r_data['signals'][key] = {'exists': exists, 'content': res.text[:800] if exists else ''}
            if exists and key != 'robots': r_data['score'] += pts
        except: r_data['signals'][key] = {'exists': False, 'content': ''}

    # robots.txt AI 봇 허용 여부 (20점)
    robots_content = r_data['signals'].get('robots', {}).get('content', '')
    ai_bots = ['GPTBot', 'ClaudeBot', 'anthropic-ai', 'GrokBot',
               'ChatGPT-User', 'PerplexityBot', 'Bingbot',
               'xAI-Grok', 'Grok-DeepSearch', 'Google-Extended']
    disallowed = [b for b in ai_bots if 'Disallow' in robots_content and b in robots_content]
    allowed_count = len(ai_bots) - len(disallowed)
    bot_score = int(allowed_count / len(ai_bots) * 20)
    r_data['signals']['ai_bots'] = {'allowed': allowed_count, 'total': len(ai_bots), 'disallowed': disallowed}
    r_data['score'] += bot_score

    # 홈페이지 HTML 분석
    try:
        page = requests.get(base, headers={'User-Agent':'GEO-Prospect/1.0'}, timeout=15)
        html = page.text

        schema_count = html.count('application/ld+json')
        schema_types = re.findall(r'\"@type\"\s*:\s*\"([^\"]+)\"', html)
        has_faq = any(t in ['FAQPage','HowTo'] for t in schema_types)
        has_org = 'Organization' in schema_types
        has_og = all(tag in html for tag in ['og:title','og:description','og:image'])
        has_twitter = 'twitter:card' in html

        r_data['signals']['schema'] = {'count': schema_count, 'types': list(set(schema_types))}
        r_data['signals']['faq_schema'] = has_faq
        r_data['signals']['org_schema'] = has_org
        r_data['signals']['og'] = has_og
        r_data['signals']['twitter'] = has_twitter

        if schema_count >= 1: r_data['score'] += 15
        if has_og: r_data['score'] += 10
        if has_twitter: r_data['score'] += 5
        if has_faq: r_data['score'] += 10
        if has_org: r_data['score'] += 5

    except: pass

    results[parsed.netloc] = r_data
    print(f'{parsed.netloc}: {r_data[\"score\"]}점')
    for k, v in r_data[\"signals\"].items():
        print(f'  {k}: {v}')

print('---')
for domain, d in results.items():
    grade = 'A급' if d['score'] < 40 else 'B급' if d['score'] < 60 else 'C급' if d['score'] < 80 else 'D급'
    print(f'{domain}: {d[\"score\"]}점 ({grade})')
"
```

**Claude 웹 환경 (WebFetch 대체)**

> 각 도메인에 대해 순서대로 WebFetch로 로드한다.
> - `https://[도메인]/robots.txt` — AI 봇 차단 여부 확인
> - `https://[도메인]/llms.txt` — 존재 여부 확인
> - `https://[도메인]/sitemap.xml` — 존재 여부 확인
> - `https://[도메인]/` — 홈페이지 HTML에서 스키마·OG 태그 확인
>
> 각 항목을 수동으로 평가하여 점수를 산출한다.

---

### 2단계: 영업 포인트 도출

점수 기반으로 제안 포인트를 자동 분류한다.

**즉시 제안 가능한 개선 항목 (미구현 항목):**

| 항목 | 없을 때 제안 메시지 | 예상 공수 |
|---|---|---|
| llms.txt | "AI 크롤러 안내 파일이 없습니다. 1시간 내 구현 가능합니다." | 1h |
| AI 봇 차단 | "주요 AI 봇이 차단되어 AI 검색에 노출되지 않습니다." | 0.5h |
| FAQPage 스키마 | "FAQ 콘텐츠가 있지만 AI가 인용할 수 없는 구조입니다." | 2h |
| Organization 스키마 | "브랜드 정체성이 AI에게 전달되지 않고 있습니다." | 1h |
| Open Graph | "SNS 공유 시 이미지·제목이 표시되지 않습니다." | 1h |
| sitemap.xml | "검색 엔진이 사이트 구조를 파악하기 어렵습니다." | 2h |

---

### 3단계: 보고서 출력

아래 출력 템플릿에 따라 보고서를 작성하고 저장한다.

---

## 출력 템플릿 (L3 전용)

### 단일 도메인 스캔

```markdown
# GEO 잠재 고객 스캔

스캔일: [날짜]  |  대상: [도메인]

---

## GEO 현황 점수: [점수]/100 — [A·B·C·D]급

개선 여지: [100-점수]점

| 신호 | 상태 | 점수 |
|---|---|---|
| HTTPS + HTTP 리다이렉트 | ✅ / ❌ | [X]/10 |
| AI 봇 허용 (robots.txt) | [N]/6개 허용 | [X]/20 |
| llms.txt | ✅ / ❌ | [X]/15 |
| sitemap.xml | ✅ / ❌ | [X]/10 |
| JSON-LD 스키마 | [N]개 블록 | [X]/15 |
| Open Graph 완비 | ✅ / ❌ | [X]/10 |
| Twitter Card | ✅ / ❌ | [X]/5 |
| FAQPage / HowTo 스키마 | ✅ / ❌ | [X]/10 |
| Organization 스키마 | ✅ / ❌ | [X]/5 |

---

## 영업 제안 포인트

### 즉시 제안 가능 (단기 성과)

1. **[개선 항목]** — 예상 공수 [X]시간
   [제안 메시지]

2. **[개선 항목]** — 예상 공수 [X]시간
   [제안 메시지]

### 추가 제안 (중기)

- [항목]: [설명]

---

## 총 예상 공수

즉시 항목: [X]시간  |  중기 항목: [X]시간  |  **합계: [X]시간**

---

## 다음 단계

- 전체 감사: `/geo audit https://[도메인]`
- 제안서 작성: `/geo proposal`
- 경쟁사 비교: `/geo compare https://[도메인] https://[경쟁사]`
```

---

### 배치 스캔 (복수 도메인)

```markdown
# GEO 잠재 고객 배치 스캔

스캔일: [날짜]  |  대상: [N]개 도메인

---

## 도메인별 현황 요약

| 도메인 | GEO 점수 | 등급 | HTTPS | llms.txt | AI봇 | 스키마 | OG | 개선 여지 |
|---|---|---|---|---|---|---|---|---|
| [도메인1] | [X]/100 | A급 | ✅/❌ | ✅/❌ | [N]/6 | [N]개 | ✅/❌ | [X]점 |
| [도메인2] | [X]/100 | B급 | ✅/❌ | ✅/❌ | [N]/6 | [N]개 | ✅/❌ | [X]점 |
| [도메인3] | [X]/100 | C급 | ✅/❌ | ✅/❌ | [N]/6 | [N]개 | ✅/❌ | [X]점 |

---

## 영업 우선순위

### A급 — 즉시 접촉 권고

| 도메인 | 핵심 문제 | 예상 공수 | 제안 포인트 |
|---|---|---|---|
| [도메인] | [문제 1], [문제 2] | [X]h | [포인트] |

### B급 — 부분 제안 권고

| 도메인 | 핵심 문제 | 예상 공수 | 제안 포인트 |
|---|---|---|---|
| [도메인] | [문제] | [X]h | [포인트] |

### C·D급 — 모니터링

| 도메인 | 현황 | 재스캔 권고 시점 |
|---|---|---|
| [도메인] | 양호 | 3개월 후 |

---

## 도메인별 상세 제안 포인트

### [도메인1]
- [제안 포인트 1]
- [제안 포인트 2]

### [도메인2]
- [제안 포인트 1]

---

## 전체 감사 대상 (A급 우선)

```bash
/geo audit https://[A급 도메인1]
/geo audit https://[A급 도메인2]
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
