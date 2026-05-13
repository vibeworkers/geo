---
name: geo-crawlers
description: >
  AI 크롤러 접근 평가. ChatGPT, Gemini, Claude, Perplexity, Copilot, Grok,
  네이버 AI 브리핑(Yeti), Baidu Ernie(Baiduspider), Yahoo! Japan(YahooSeeker),
  Apple Intelligence(Applebot) 등 글로벌·언어별 AI 서비스의 봇 접근 현황을 진단한다.
  봇 용도(학습용/검색용)를 구분하고 사이트 운영 언어·목표에 따른 허용 전략(A~G)을 안내한다.
  SITE_LANGS가 설정된 경우 언어별 적합 봇 세트를 자동 선택하여 평가한다.
  robots.txt 허용 현황, llms.txt 설정, 기술 접근성, 크롤링 효율 4개 차원으로 평가한다.
  모든 레벨에서 동일하게 분석하며 출력 방식만 달라진다.
  트리거: "크롤러", "AI 봇", "robots.txt", "크롤링", "crawlers", "네이버 봇", "Yeti",
  "Baiduspider", "/geo crawlers".
audience: L1, L2, L3
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# geo-crawlers — AI 크롤러 접근 평가

> 실행 시 USER_LEVEL을 확인한다. 설정되지 않은 경우 레벨 선택을 먼저 요청한다.
> 결과는 USER_LEVEL에 맞는 출력 템플릿으로 전달하고 `GEO-크롤러-분석.md`로 저장한다.

---

## 실행 단계

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

robots.txt에서 아래 봇의 허용/차단 여부를 각각 확인한다.
SITE_LANGS가 설정된 경우, 사이트 언어에 해당하는 지역별 봇도 함께 확인한다.

#### 글로벌 AI 봇 — 전 언어 공통 대상

| 봇 이름 | User-agent | 서비스 | 용도 |
|---|---|---|---|
| GPTBot | `GPTBot` | OpenAI ChatGPT | 학습 |
| OAI-SearchBot | `OAI-SearchBot` | ChatGPT 실시간 브라우징 | 검색 |
| ChatGPT-User | `ChatGPT-User` | ChatGPT 브라우징 | 검색 |
| ClaudeBot | `ClaudeBot` | Anthropic Claude | 학습 |
| anthropic-ai | `anthropic-ai` | Anthropic 데이터 수집 | 학습 |
| Google-Extended | `Google-Extended` | Google Gemini · AI Overviews | 학습+검색 |
| PerplexityBot | `PerplexityBot` | Perplexity AI | 검색 |
| Bingbot | `Bingbot` | Microsoft Copilot | 검색 |
| GrokBot | `GrokBot` | xAI Grok | 학습 |
| xAI-Grok | `xAI-Grok` | Grok 실시간 검색 | 검색 |
| Grok-DeepSearch | `Grok-DeepSearch` | Grok 심층 검색 | 검색 |
| Applebot | `Applebot` | Apple Intelligence · Siri | 학습+검색 |
| Meta-ExternalAgent | `Meta-ExternalAgent` | Meta AI | 학습 |

#### 지역별 AI 봇 — SITE_LANGS에 해당 언어 포함 시 추가 확인

| 봇 이름 | User-agent | 서비스 | 언어/지역 | 용도 |
|---|---|---|---|---|
| Yeti | `Yeti` | 네이버 AI 브리핑 · AI 탭 · 일반 검색 | 한국어 (ko) | 검색+학습 |
| NaverBot | `NaverBot` | 네이버 검색 | 한국어 (ko) | 검색 |
| YahooSeeker | `YahooSeeker` | Yahoo! Japan AI 검색 | 일본어 (ja) | 검색 |
| Baiduspider | `Baiduspider` | Baidu Ernie · 바이두 검색 | 중국어 (zh) | 검색+학습 |
| Baiduspider-render | `Baiduspider-render` | 바이두 렌더링 봇 | 중국어 (zh) | 검색 |
| SogouBot | `Sogou web spider` | Sogou AI | 중국어 (zh) | 검색 |
| 360Spider | `360Spider` | 360 AI | 중국어 (zh) | 검색 |

#### AI 학습 소스 봇 — 선택적 확인

AI 검색 봇은 아니지만, AI 모델 학습 데이터 소스로 활용될 수 있는 봇이다.
차단 시 아카이브에서 누락되어 일부 AI 모델 학습 데이터에 영향을 줄 수 있다.

| 봇 이름 | User-agent | 서비스 | 용도 |
|---|---|---|---|
| ia_archiver | `ia_archiver` | Internet Archive (Wayback Machine) | 웹 아카이브·AI 학습 소스 |

> **참고:** Internet Archive 데이터는 GPT, LLaMA 등 대형 모델 학습 데이터셋(Common Crawl, The Pile 등)에 간접 포함된다. 직접 AI 검색 봇과 달리 즉각적인 GEO 효과는 없으나, 장기 학습 데이터 가시성 확보 관점에서 허용을 권장한다.

> **한국 시장 주의:** 클로바X는 2026년 4월 9일 서비스 종료. 네이버 AI 브리핑·AI 탭은 Yeti가 콘텐츠 수집을 담당하므로 전용 AI 봇이 별도로 없다. Yeti 허용이 네이버 AI 인용의 전제 조건이다.

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
| A. 글로벌 전체 허용 | 글로벌 AI 봇 전체 (13개) | — | 영어 사이트 GEO 최대화 |
| B. 검색만 허용 | OAI-SearchBot·ChatGPT-User·PerplexityBot·Bingbot·Google-Extended·xAI-Grok·Grok-DeepSearch | GPTBot·ClaudeBot·anthropic-ai·GrokBot·Applebot | 실시간 인용은 원하나 학습 데이터 제공 거부 |
| C. 선택적 허용 | 특정 서비스만 | 나머지 | 특정 AI 플랫폼 파트너십 등 |
| D. 한국 시장 추가 | 전략 A + Yeti·NaverBot | — | 한국어 사이트, 네이버 AI 브리핑·AI 탭 최적화 |
| E. 일본 시장 추가 | 전략 A + YahooSeeker | — | 일본어 사이트, Yahoo! Japan AI 최적화 |
| F. 중국 시장 추가 | 전략 A + Baiduspider·Baiduspider-render·SogouBot·360Spider | — | 중국어 사이트, 바이두 AI 최적화 |
| G. 다국어 전체 허용 | 전략 A + D + E + F (최대 20개) | — | 다국어 사이트 전체 AI 가시성 최대화 |

**전략별 GEO 영향**

- 전략 A: 글로벌 AI 검색 노출 + 미래 모델 학습 모두 반영 → 영어 사이트 GEO 점수 최고
- 전략 B: 현재 AI 검색 노출은 가능하나, 학습용 봇 차단으로 미래 모델이 브랜드를 학습하지 못해 장기 GEO 효과 감소. 저작권·콘텐츠 보호가 우선일 때 선택.
- 전략 C: 노출 범위 제한, 특수 목적에만 적합
- 전략 D: 네이버 AI 브리핑 인용 위해 Yeti 허용 필수. C-rank 기반 인용 최적화와 병행.
- 전략 E: Yahoo! Japan AI 검색 노출을 위해 YahooSeeker 허용 필수.
- 전략 F: 바이두 인덱싱을 위해 ICP 번호 등록과 병행 필요. Baiduspider 허용만으로는 부족.
- 전략 G: 다국어 사이트 전체 커버리지. hreflang 설정과 반드시 병행.

---

### 4단계: 크롤러 접근 4개 차원 평가

각 차원을 0–25점으로 평가한다. 합산 점수(0–100)가 크롤러 점수다.

#### AI 봇 허용 상태 — 0~25점

SITE_LANGS를 기준으로 평가 대상 봇 세트를 결정한다.

| 신호 | 확인 항목 | 적용 조건 |
|---|---|---|
| GPTBot / OAI-SearchBot / ChatGPT-User 허용 | ChatGPT 관련 봇 차단 여부 | 전 언어 |
| ClaudeBot / anthropic-ai 허용 | Claude 관련 봇 차단 여부 | 전 언어 |
| Google-Extended 허용 | Gemini · AI Overviews 봇 차단 여부 | 전 언어 |
| PerplexityBot 허용 | Perplexity 봇 차단 여부 | 전 언어 |
| Bingbot 허용 | Copilot 관련 봇 차단 여부 | 전 언어 |
| GrokBot / xAI-Grok / Grok-DeepSearch 허용 | Grok 관련 봇 차단 여부 | 전 언어 |
| Applebot 허용 | Apple Intelligence · Siri 봇 차단 여부 | 전 언어 |
| Yeti / NaverBot 허용 | 네이버 AI 브리핑·AI 탭 봇 차단 여부 | SITE_LANGS에 `ko` 포함 시 |
| YahooSeeker 허용 | Yahoo! Japan AI 봇 차단 여부 | SITE_LANGS에 `ja` 포함 시 |
| Baiduspider / SogouBot / 360Spider 허용 | 중국 AI 봇 차단 여부 | SITE_LANGS에 `zh` 포함 시 |
| ia_archiver 허용 | Internet Archive 봇 차단 여부 | 선택적 — 차단 시 참고 표기 |

점수 산정: 사이트 언어 기준 적합 봇 세트 중 허용된 비율에 비례하여 0–25점 부여. 전체 차단 0점, 전체 허용 25점. ia_archiver는 점수 산정에서 제외하고 별도 참고 항목으로 표기한다.

#### AI 안내 파일 — 0~25점

AI 크롤러가 사이트 구조를 이해할 수 있도록 안내하는 파일 존재 여부와 품질을 평가한다.

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
| Apple Intelligence | 가능 / 차단 | 가능 / 차단 | [한 줄] |
| 네이버 AI 브리핑·AI 탭 | 가능 / 차단 | 가능 / 차단 | [ko 사이트만 표시] |
| Yahoo! Japan AI | 가능 / 차단 | — | [ja 사이트만 표시] |
| Baidu Ernie (바이두) | 가능 / 차단 | 가능 / 차단 | [zh 사이트만 표시] |

> AI 검색 노출: 지금 AI 검색 결과에 인용될 수 있는가
> AI 모델 학습: 미래 AI가 이 브랜드를 기억할 수 있는가
> 지역별 항목: SITE_LANGS에 해당 언어가 없으면 출력 생략

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

### 글로벌 봇 (전 언어 공통)

| 봇 | 서비스 | 용도 | 현재 상태 | 조치 필요 |
|---|---|---|---|---|
| GPTBot | ChatGPT | 학습 | 허용 / 차단 | 예 / 아니오 |
| OAI-SearchBot | ChatGPT 브라우징 | 검색 | 허용 / 차단 | 예 / 아니오 |
| ChatGPT-User | ChatGPT 브라우징 | 검색 | 허용 / 차단 | 예 / 아니오 |
| ClaudeBot | Claude | 학습 | 허용 / 차단 | 예 / 아니오 |
| anthropic-ai | Claude | 학습 | 허용 / 차단 | 예 / 아니오 |
| Google-Extended | Gemini / AI Overviews | 학습+검색 | 허용 / 차단 | 예 / 아니오 |
| PerplexityBot | Perplexity | 검색 | 허용 / 차단 | 예 / 아니오 |
| Bingbot | Copilot | 검색 | 허용 / 차단 | 예 / 아니오 |
| GrokBot | Grok | 학습 | 허용 / 차단 | 예 / 아니오 |
| xAI-Grok | Grok 실시간 검색 | 검색 | 허용 / 차단 | 예 / 아니오 |
| Grok-DeepSearch | Grok 심층 검색 | 검색 | 허용 / 차단 | 예 / 아니오 |
| Applebot | Apple Intelligence | 학습+검색 | 허용 / 차단 | 예 / 아니오 |
| Meta-ExternalAgent | Meta AI | 학습 | 허용 / 차단 | 예 / 아니오 |

### 지역별 봇 (SITE_LANGS 해당 언어 포함 시만 출력)

| 봇 | 서비스 | 언어 | 용도 | 현재 상태 | 조치 필요 |
|---|---|---|---|---|---|
| Yeti | 네이버 AI 브리핑·AI 탭 | ko | 검색+학습 | 허용 / 차단 | 예 / 아니오 |
| NaverBot | 네이버 검색 | ko | 검색 | 허용 / 차단 | 예 / 아니오 |
| YahooSeeker | Yahoo! Japan AI | ja | 검색 | 허용 / 차단 | 예 / 아니오 |
| Baiduspider | Baidu Ernie | zh | 검색+학습 | 허용 / 차단 | 예 / 아니오 |
| SogouBot | Sogou AI | zh | 검색 | 허용 / 차단 | 예 / 아니오 |
| 360Spider | 360 AI | zh | 검색 | 허용 / 차단 | 예 / 아니오 |

---

## 권장 전략

현재 차단 상태와 사이트 운영 언어를 고려한 권장 전략: **[A / B / C / D / E / F / G]**

- 전략 A (글로벌 전체 허용): 글로벌 AI 검색 노출 + 미래 모델 학습 모두 허용. **영어 단일 사이트라면 이 전략 권장.**
- 전략 B (검색만 허용): 실시간 인용은 허용하나, 학습용 봇 차단으로 미래 모델이 브랜드를 학습하지 못해 장기 GEO 효과 감소. 저작권·콘텐츠 보호가 우선일 때만 선택.
- 전략 C (선택적 허용): 특정 서비스만 선택해 허용. 특수 목적에만 적합.
- 전략 D (한국 시장): 전략 A + Yeti·NaverBot 허용. **한국어 사이트, 네이버 AI 브리핑 최적화 필수.**
- 전략 E (일본 시장): 전략 A + YahooSeeker 허용. **일본어 사이트 권장.**
- 전략 F (중국 시장): 전략 A + Baiduspider·SogouBot·360Spider 허용. ICP 번호 등록과 병행 필수.
- 전략 G (다국어 전체): 전략 A + D + E + F 통합. **다국어 사이트라면 이 전략 권장.**

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

### Global Bots (글로벌 AI 봇 — 13개)

| Bot | User-agent | Type | Status | Directive | Source |
|---|---|---|---|---|---|
| GPTBot | `GPTBot` | Training | Allowed / Blocked | [규칙] | robots.txt L[줄] |
| OAI-SearchBot | `OAI-SearchBot` | Search | Allowed / Blocked | [규칙] | — |
| ChatGPT-User | `ChatGPT-User` | Search | Allowed / Blocked | [규칙] | — |
| ClaudeBot | `ClaudeBot` | Training | Allowed / Blocked | [규칙] | — |
| anthropic-ai | `anthropic-ai` | Training | Allowed / Blocked | [규칙] | — |
| Google-Extended | `Google-Extended` | Both | Allowed / Blocked | [규칙] | — |
| PerplexityBot | `PerplexityBot` | Search | Allowed / Blocked | [규칙] | — |
| Bingbot | `Bingbot` | Search | Allowed / Blocked | [규칙] | — |
| GrokBot | `GrokBot` | Training | Allowed / Blocked | [규칙] | — |
| xAI-Grok | `xAI-Grok` | Search | Allowed / Blocked | [규칙] | — |
| Grok-DeepSearch | `Grok-DeepSearch` | Search | Allowed / Blocked | [규칙] | — |
| Applebot | `Applebot` | Both | Allowed / Blocked | [규칙] | — |
| Meta-ExternalAgent | `Meta-ExternalAgent` | Training | Allowed / Blocked | [규칙] | — |

### Regional Bots (SITE_LANGS 조건부 — 7개)

| Bot | User-agent | Region | Status | Directive | 적용 조건 |
|---|---|---|---|---|---|
| Yeti | `Yeti` | 한국 | Allowed / Blocked | [규칙] | SITE_LANGS에 ko 포함 시 |
| NaverBot | `NaverBot` | 한국 | Allowed / Blocked | [규칙] | SITE_LANGS에 ko 포함 시 |
| YahooSeeker | `YahooSeeker` | 일본 | Allowed / Blocked | [규칙] | SITE_LANGS에 ja 포함 시 |
| Baiduspider | `Baiduspider` | 중국 | Allowed / Blocked | [규칙] | SITE_LANGS에 zh 포함 시 |
| Baiduspider-render | `Baiduspider-render` | 중국 | Allowed / Blocked | [규칙] | SITE_LANGS에 zh 포함 시 |
| SogouBot | `Sogou web spider` | 중국 | Allowed / Blocked | [규칙] | SITE_LANGS에 zh 포함 시 |
| 360Spider | `360Spider` | 중국 | Allowed / Blocked | [규칙] | SITE_LANGS에 zh 포함 시 |

---

## Recommended Strategy: [A / B / C / D / E / F / G]

현재 상태를 기준으로 권장 전략과 robots.txt 수정 코드를 제시한다.

### Strategy A — 전체 허용 (GEO 최적화)
  ```
  # Primary AI bots — full access
  User-agent: GPTBot
  Allow: /

  User-agent: ChatGPT-User
  Allow: /

  User-agent: ClaudeBot
  Allow: /

  User-agent: anthropic-ai
  Allow: /

  User-agent: Google-Extended
  Allow: /

  User-agent: PerplexityBot
  Allow: /

  User-agent: Bingbot
  Allow: /

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

  User-agent: anthropic-ai
  Disallow: /

  User-agent: GrokBot
  Disallow: /

  # Search bots — allowed
  User-agent: ChatGPT-User
  Allow: /

  User-agent: Google-Extended
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

### Strategy D — 한국 시장 (전략 A + 한국 봇)
  ```
  # Global AI bots — full access
  User-agent: GPTBot
  Allow: /

  User-agent: OAI-SearchBot
  Allow: /

  User-agent: ChatGPT-User
  Allow: /

  User-agent: ClaudeBot
  Allow: /

  User-agent: anthropic-ai
  Allow: /

  User-agent: Google-Extended
  Allow: /

  User-agent: PerplexityBot
  Allow: /

  User-agent: Bingbot
  Allow: /

  User-agent: GrokBot
  Allow: /

  User-agent: xAI-Grok
  Allow: /

  User-agent: Grok-DeepSearch
  Allow: /

  User-agent: Applebot
  Allow: /

  User-agent: Meta-ExternalAgent
  Allow: /

  # Korean market bots — 네이버 AI 브리핑·AI 탭 최적화
  User-agent: Yeti
  Allow: /

  User-agent: NaverBot
  Allow: /

  Sitemap: https://[도메인]/sitemap.xml
  ```

### Strategy E — 일본 시장 (전략 A + 일본 봇)
  ```
  # Global AI bots — full access
  User-agent: GPTBot
  Allow: /

  User-agent: OAI-SearchBot
  Allow: /

  User-agent: ChatGPT-User
  Allow: /

  User-agent: ClaudeBot
  Allow: /

  User-agent: anthropic-ai
  Allow: /

  User-agent: Google-Extended
  Allow: /

  User-agent: PerplexityBot
  Allow: /

  User-agent: Bingbot
  Allow: /

  User-agent: GrokBot
  Allow: /

  User-agent: xAI-Grok
  Allow: /

  User-agent: Grok-DeepSearch
  Allow: /

  User-agent: Applebot
  Allow: /

  User-agent: Meta-ExternalAgent
  Allow: /

  # Japanese market bots — Yahoo! Japan AI 최적화
  User-agent: YahooSeeker
  Allow: /

  Sitemap: https://[도메인]/sitemap.xml
  ```

### Strategy F — 중국 시장 (전략 A + 중국 봇)
  ```
  # Global AI bots — full access
  User-agent: GPTBot
  Allow: /

  User-agent: OAI-SearchBot
  Allow: /

  User-agent: ChatGPT-User
  Allow: /

  User-agent: ClaudeBot
  Allow: /

  User-agent: anthropic-ai
  Allow: /

  User-agent: Google-Extended
  Allow: /

  User-agent: PerplexityBot
  Allow: /

  User-agent: Bingbot
  Allow: /

  User-agent: GrokBot
  Allow: /

  User-agent: xAI-Grok
  Allow: /

  User-agent: Grok-DeepSearch
  Allow: /

  User-agent: Applebot
  Allow: /

  User-agent: Meta-ExternalAgent
  Allow: /

  # Chinese market bots — Baidu Ernie·Sogou AI·360 AI 최적화
  User-agent: Baiduspider
  Allow: /

  User-agent: Baiduspider-render
  Allow: /

  User-agent: Sogou web spider
  Allow: /

  User-agent: 360Spider
  Allow: /

  Sitemap: https://[도메인]/sitemap.xml
  ```

### Strategy G — 다국어 전체 허용 (전략 A + D + E + F)
  ```
  # Global AI bots — full access
  User-agent: GPTBot
  Allow: /

  User-agent: OAI-SearchBot
  Allow: /

  User-agent: ChatGPT-User
  Allow: /

  User-agent: ClaudeBot
  Allow: /

  User-agent: anthropic-ai
  Allow: /

  User-agent: Google-Extended
  Allow: /

  User-agent: PerplexityBot
  Allow: /

  User-agent: Bingbot
  Allow: /

  User-agent: GrokBot
  Allow: /

  User-agent: xAI-Grok
  Allow: /

  User-agent: Grok-DeepSearch
  Allow: /

  User-agent: Applebot
  Allow: /

  User-agent: Meta-ExternalAgent
  Allow: /

  # Korean market bots — 네이버 AI 브리핑·AI 탭 최적화
  User-agent: Yeti
  Allow: /

  User-agent: NaverBot
  Allow: /

  # Japanese market bots — Yahoo! Japan AI 최적화
  User-agent: YahooSeeker
  Allow: /

  # Chinese market bots — Baidu Ernie·Sogou AI·360 AI 최적화
  User-agent: Baiduspider
  Allow: /

  User-agent: Baiduspider-render
  Allow: /

  User-agent: Sogou web spider
  Allow: /

  User-agent: 360Spider
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
