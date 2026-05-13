---
name: geo-lang-platform
description: >
  언어별 AI 플랫폼 매핑 및 봇 허용 전략 진단. SITE_LANGS를 기반으로 각 언어에서
  주요 AI 플랫폼(네이버 AI 브리핑·ChatGPT·Perplexity·Yahoo! Japan·Baidu Ernie 등)의
  접근 상태를 확인하고 언어별 최적화 포인트를 제시한다.
  L1은 플랫폼 현황 요약, L2는 robots.txt 전략 안내, L3는 전체 코드 스니펫 포함.
  트리거: "AI 플랫폼", "봇 전략", "네이버 AI", "ChatGPT 봇", "lang-platform",
           "언어별 AI", "다국어 봇", "/geo lang-platform".
audience: L1, L2, L3
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# geo-lang-platform — 언어별 AI 플랫폼 매핑

> 실행 시 USER_LEVEL과 SITE_LANGS를 확인한다.
> SITE_LANGS가 설정되지 않은 경우 `/geo lang` 으로 먼저 언어를 설정하도록 안내한다.
> 결과는 USER_LEVEL에 맞는 출력 템플릿으로 전달하고 `GEO-언어플랫폼-[도메인]-[날짜].md`로 저장한다.

---

## 실행 단계

### 1단계: SITE_LANGS 확인

SITE_LANGS가 비어 있으면 먼저 자동 감지를 시도한다.

> **Claude Code 환경:** Bash로 hreflang 태그·html lang 속성·URL 패턴 파싱
> **Claude 웹 환경:** WebFetch로 HTML 확인

```
SITE_LANGS 자동 감지 순서:
1. <link rel="alternate" hreflang="..."> 태그에서 언어 코드 수집
2. <html lang=""> 속성
3. URL 패턴 (/ko/, /en/, /ja/ 등)
4. 감지 불가 → 사용자에게 /geo lang 실행 안내
```

---

### 2단계: robots.txt 봇 허용 현황 수집

> **Claude Code 환경 (Bash)**

```bash
python3 -c "
import requests
from urllib.parse import urlparse

url = '[TARGET_URL]'
parsed = urlparse(url)
base = f'{parsed.scheme}://{parsed.netloc}'

robots_url = base + '/robots.txt'
r = requests.get(robots_url, timeout=10)
print(f'robots.txt 상태: {r.status_code}')
if r.status_code == 200:
    print(r.text)
"
```

> **Claude 웹 환경:** WebFetch로 `https://[도메인]/robots.txt` 로드

**확인 봇 목록 (SITE_LANGS 기반 분기)**

SITE_LANGS에 ko 포함:
- `Yeti` — 네이버 AI 브리핑·AI 탭 (필수)
- `NaverBot` — 네이버 일반 검색 (필수)

SITE_LANGS에 en 포함:
- `GPTBot` — ChatGPT 학습
- `OAI-SearchBot` — ChatGPT 실시간 브라우징
- `ChatGPT-User` — ChatGPT 브라우징
- `PerplexityBot` — Perplexity AI
- `Bingbot` — Microsoft Copilot
- `Google-Extended` — Gemini·AI Overviews
- `GrokBot` — Grok 학습
- `xAI-Grok` — Grok 검색
- `Grok-DeepSearch` — Grok 심층 검색
- `Applebot` — Apple Intelligence·Siri
- `Meta-ExternalAgent` — Meta AI

SITE_LANGS에 ja 포함:
- `YahooSeeker` — Yahoo! Japan AI 검색

SITE_LANGS에 zh 포함:
- `Baiduspider` — Baidu Ernie
- `Baiduspider-render` — 바이두 렌더링 봇
- `Sogou web spider` — Sogou AI
- `360Spider` — 360 AI

---

### 3단계: 언어별 AI 플랫폼 접근 상태 평가

SITE_LANGS 각 언어에 대해 아래 기준으로 평가한다.

**평가 기준**

| 상태 | 조건 |
|---|---|
| 최적 | 해당 언어 핵심 봇 전체 허용 + 플랫폼별 추가 최적화 완료 |
| 양호 | 핵심 봇 허용, 일부 최적화 항목 미완성 |
| 부족 | 핵심 봇 1개 이상 차단 |
| 차단 | 핵심 봇 전체 차단 또는 robots.txt 없음 |

**언어별 핵심 AI 플랫폼 및 최적화 포인트**

#### 한국어 (ko) 핵심 항목

| 플랫폼 | 봇 | 허용 상태 | 최적화 포인트 |
|---|---|---|---|
| 네이버 AI 브리핑 | Yeti | 허용 / 차단 | C-rank + D.I.A. 구조 |
| 네이버 AI 탭 | Yeti·NaverBot | 허용 / 차단 | FAQPage 스키마 + 에이전틱 구조 |
| ChatGPT | GPTBot·OAI-SearchBot | 허용 / 차단 | GPTBot 허용 + 콘텐츠 깊이 |
| Gemini | Google-Extended | 허용 / 차단 | E-E-A-T + Google 최적화 |

한국어 추가 최적화 항목:
- Naver Search Advisor 등록 및 sitemap 제출
- 작성일·수정일 명시 (신선도 신호)
- D.I.A. 구조: 첫 문단 직접 답변, H3 질문 형식 FAQ, 목록·표·단계별 가이드
- C-rank: 네이버 블로그·지식iN 채널 운영

#### 영어 (en) 핵심 항목

| 플랫폼 | 봇 | 허용 상태 | 최적화 포인트 |
|---|---|---|---|
| ChatGPT | GPTBot·OAI-SearchBot·ChatGPT-User | 허용 / 차단 | 콘텐츠 깊이, 외부 링크 |
| Perplexity AI | PerplexityBot | 허용 / 차단 | 직접 답변 구조, 출처 명확성 |
| Google Gemini / AI Overviews | Google-Extended | 허용 / 차단 | E-E-A-T, FAQPage 스키마 |
| Microsoft Copilot | Bingbot | 허용 / 차단 | Bing Webmaster Tools 등록 |
| Grok | GrokBot·xAI-Grok·Grok-DeepSearch | 허용 / 차단 | X(Twitter) 계정 연결 |
| Apple Intelligence | Applebot | 허용 / 차단 | 구조화 데이터 |
| Meta AI | Meta-ExternalAgent | 허용 / 차단 | Facebook·Instagram 연계 |

영어 추가 최적화 항목:
- Wikipedia 등재 또는 언급
- Reddit·Quora 브랜드 언급 확보
- E-E-A-T 저자 바이라인·자격증명 명시

#### 일본어 (ja) 핵심 항목

| 플랫폼 | 봇 | 허용 상태 | 최적화 포인트 |
|---|---|---|---|
| Yahoo! Japan AI | YahooSeeker | 허용 / 차단 | Yahoo! Japan Search Console 등록 |
| ChatGPT | GPTBot·OAI-SearchBot | 허용 / 차단 | 일본어 FAQ 구조 |
| Perplexity AI | PerplexityBot | 허용 / 차단 | 일본어 직접 답변 구조 |
| Google Gemini | Google-Extended | 허용 / 차단 | Google Japan 검색 최적화 |

일본어 추가 최적화 항목:
- Yahoo! Japan Search Console 등록 및 sitemap 제출
- 일본어 날짜 형식: `2026年5月9日`
- Yahoo! Japan 디렉토리 등록 검토

#### 중국어 (zh) 핵심 항목

| 플랫폼 | 봇 | 허용 상태 | 최적화 포인트 |
|---|---|---|---|
| Baidu Ernie (文心一言) | Baiduspider·Baiduspider-render | 허용 / 차단 | ICP 번호 필수, 바이두 검색자원플랫폼 등록 |
| Sogou AI | Sogou web spider | 허용 / 차단 | SogouBot Allow |
| 360 AI | 360Spider | 허용 / 차단 | 360Spider Allow |

중국어 특별 고려사항:
- ICP 번호(互联网内容提供商) 필수 — 미등록 시 중국 내 AI 인덱싱 불가
- Great Firewall 접근 가능 여부 외부 도구로 확인
- zh-CN(간체) vs zh-TW(번체) hreflang 분리 필수
- 중국 내 서버 또는 CDN 노드 필요

#### 스페인어 (es) 핵심 항목

| 플랫폼 | 봇 | 허용 상태 | 최적화 포인트 |
|---|---|---|---|
| ChatGPT | GPTBot·OAI-SearchBot | 허용 / 차단 | 스페인어 직접 답변 구조 |
| Perplexity AI | PerplexityBot | 허용 / 차단 | 출처 명확성, 권위 신호 |
| Google Gemini | Google-Extended | 허용 / 차단 | E-E-A-T, 라틴아메리카 로컬 신호 |
| Microsoft Copilot | Bingbot | 허용 / 차단 | Bing Webmaster Tools 등록 |

스페인어 추가 최적화 항목:
- hreflang 지역 분리: es-ES / es-MX / es-AR / es-CO
- 통화·단위 로컬라이즈: EUR(스페인) vs MXN(멕시코)
- 날짜 형식: `9 de mayo de 2026`

---

### 4단계: 권장 전략 산출

```
SITE_LANGS 조합 → 권장 전략:
- ["ko"] 또는 ["ko", "en"] → 전략 D
- ["en"] → 전략 A
- ["ko", "en", "ja"] 또는 ["en", "ja"] → 전략 D + E (= 전략 G 준비)
- zh 포함 → 전략 F 추가
- 3개 이상 언어 → 전략 G (전체 허용)
```

---

## 레벨별 출력 템플릿

---

### L1 출력 — 마케팅 담당자

AI 플랫폼별 현황과 개선 요청 문구만 제공한다.

```markdown
# [사이트명] 언어별 AI 플랫폼 현황

진단일: [날짜]  |  URL: [URL]  |  사이트 언어: [SITE_LANGS]

---

## AI 플랫폼 접근 요약

| 언어 | 주요 AI 플랫폼 | 현재 상태 | 중요도 |
|---|---|---|---|
| 한국어 | 네이버 AI 브리핑·ChatGPT·Gemini | 최적 / 양호 / 부족 / 차단 | 높음 |
| 영어 | ChatGPT·Perplexity·Copilot | 최적 / 양호 / 부족 / 차단 | 높음 |
| 일본어 | Yahoo! Japan AI·ChatGPT | 최적 / 양호 / 부족 / 차단 | 보통 |
| 중국어 | Baidu Ernie·Sogou AI | 최적 / 양호 / 부족 / 차단 | 조건부 |
| 스페인어 | ChatGPT·Perplexity·Gemini | 최적 / 양호 / 부족 / 차단 | 보통 |

---

## 핵심 문제

### [언어] — [문제 제목]
- 현재 상태: [설명]
- AI 서비스 영향: [영향]
- 개발팀 전달 메시지:
  "[개발팀에 전달할 요청 내용]"

---

## 한국어 사이트 네이버 AI 브리핑 최적화 체크리스트

> 한국어 사이트인 경우에만 표시

| 항목 | 상태 | 설명 |
|---|---|---|
| Yeti 봇 허용 | 완료 / 미완료 | robots.txt에 Yeti Allow 필요 |
| Naver Search Advisor 등록 | 완료 / 미완료 | search.naver.com/info/webmaster |
| sitemap 제출 | 완료 / 미완료 | Naver Search Advisor에 제출 |
| D.I.A. 구조 | 완료 / 미완료 | 첫 문단 직접 답변, H3 FAQ 구조 |
| 작성일·수정일 표시 | 완료 / 미완료 | 신선도 신호 — 날짜 명시 필수 |
```

---

### L2 출력 — 웹마스터 / 운영자

robots.txt 수정 안내와 플랫폼별 등록 방법을 포함한다.

```markdown
# [사이트명] 언어별 AI 플랫폼 진단

진단일: [날짜]  |  URL: [URL]  |  SITE_LANGS: [언어 목록]  |  권장 전략: [A/D/E/F/G]

---

## 언어별 AI 봇 허용 현황

### 한국어 봇 (SITE_LANGS에 ko 포함 시)

| 봇 | User-agent | AI 서비스 | 현재 상태 | 조치 |
|---|---|---|---|---|
| Yeti | `Yeti` | 네이버 AI 브리핑·AI 탭 | 허용 / 차단 | [차단 시 수정 방법] |
| NaverBot | `NaverBot` | 네이버 일반 검색 | 허용 / 차단 | [차단 시 수정 방법] |

### 글로벌 봇

| 봇 | User-agent | AI 서비스 | 현재 상태 |
|---|---|---|---|
| GPTBot | `GPTBot` | ChatGPT | 허용 / 차단 |
| OAI-SearchBot | `OAI-SearchBot` | ChatGPT 브라우징 | 허용 / 차단 |
| PerplexityBot | `PerplexityBot` | Perplexity AI | 허용 / 차단 |
| Google-Extended | `Google-Extended` | Gemini·AI Overviews | 허용 / 차단 |
| Bingbot | `Bingbot` | Microsoft Copilot | 허용 / 차단 |

### 일본어 봇 (SITE_LANGS에 ja 포함 시)

| 봇 | User-agent | AI 서비스 | 현재 상태 |
|---|---|---|---|
| YahooSeeker | `YahooSeeker` | Yahoo! Japan AI | 허용 / 차단 |

### 중국어 봇 (SITE_LANGS에 zh 포함 시)

| 봇 | User-agent | AI 서비스 | 현재 상태 |
|---|---|---|---|
| Baiduspider | `Baiduspider` | Baidu Ernie | 허용 / 차단 |
| SogouBot | `Sogou web spider` | Sogou AI | 허용 / 차단 |
| 360Spider | `360Spider` | 360 AI | 허용 / 차단 |

---

## 권장 전략: [A / D / E / F / G]

**robots.txt 수정 방법 (FTP 또는 CMS)**

1. FTP 접속 → 사이트 루트 디렉토리 이동
2. `robots.txt` 파일 열기
3. 아래 코드를 기존 내용에 추가 (기존 Disallow: / 규칙이 있으면 삭제 또는 수정)
4. 저장 후 `https://[도메인]/robots.txt` 에서 확인

추가할 코드 (차단된 봇이 있는 경우):
```
User-agent: [차단된 봇]
Allow: /
```

---

## 언어별 플랫폼 등록 현황

| 언어 | 플랫폼 | 등록 상태 | 등록 URL |
|---|---|---|---|
| ko | Naver Search Advisor | 등록 / 미등록 | search.naver.com/info/webmaster |
| en | Google Search Console | 등록 / 미등록 | search.google.com/search-console |
| en | Bing Webmaster Tools | 등록 / 미등록 | webmaster.bing.com |
| ja | Yahoo! Japan Search Console | 등록 / 미등록 | search.yahoo.co.jp/webmaster |
| zh | 바이두 검색자원플랫폼 | 등록 / 미등록 | ziyuan.baidu.com |

---

## 우선순위별 개선 과제

1. [가장 중요한 봇 차단 해제]: robots.txt 수정
2. [플랫폼 등록 미완료]: [등록 URL]에서 사이트맵 제출
3. [콘텐츠 최적화]: [해당 언어별 최적화 포인트]
```

---

### L3 출력 — 개발자

전체 봇 허용 현황 매트릭스, robots.txt 코드, 서버별 설정을 포함한다.

```markdown
# [사이트명] Language-Platform AI Bot Matrix

Date: [날짜]  |  URL: [URL]  |  SITE_LANGS: [언어 목록]  |  Strategy: [A/D/E/F/G]

---

## Full Bot Access Matrix

### Global Bots (13개)

| Bot | User-agent | Service | Status | Directive | Line |
|---|---|---|---|---|---|
| GPTBot | `GPTBot` | ChatGPT Training | Allowed / Blocked | [규칙] | L[줄] |
| OAI-SearchBot | `OAI-SearchBot` | ChatGPT Search | Allowed / Blocked | [규칙] | — |
| ChatGPT-User | `ChatGPT-User` | ChatGPT Browsing | Allowed / Blocked | [규칙] | — |
| ClaudeBot | `ClaudeBot` | Claude Training | Allowed / Blocked | [규칙] | — |
| anthropic-ai | `anthropic-ai` | Claude Data | Allowed / Blocked | [규칙] | — |
| Google-Extended | `Google-Extended` | Gemini + AI Overviews | Allowed / Blocked | [규칙] | — |
| PerplexityBot | `PerplexityBot` | Perplexity AI | Allowed / Blocked | [규칙] | — |
| Bingbot | `Bingbot` | Microsoft Copilot | Allowed / Blocked | [규칙] | — |
| GrokBot | `GrokBot` | Grok Training | Allowed / Blocked | [규칙] | — |
| xAI-Grok | `xAI-Grok` | Grok Search | Allowed / Blocked | [규칙] | — |
| Grok-DeepSearch | `Grok-DeepSearch` | Grok DeepSearch | Allowed / Blocked | [규칙] | — |
| Applebot | `Applebot` | Apple Intelligence | Allowed / Blocked | [규칙] | — |
| Meta-ExternalAgent | `Meta-ExternalAgent` | Meta AI | Allowed / Blocked | [규칙] | — |

### Regional Bots (SITE_LANGS 조건부)

| Bot | User-agent | Region | Service | Status | Condition |
|---|---|---|---|---|---|
| Yeti | `Yeti` | ko | 네이버 AI 브리핑·AI 탭 | Allowed / Blocked | SITE_LANGS에 ko 포함 시 |
| NaverBot | `NaverBot` | ko | 네이버 검색 | Allowed / Blocked | SITE_LANGS에 ko 포함 시 |
| YahooSeeker | `YahooSeeker` | ja | Yahoo! Japan AI | Allowed / Blocked | SITE_LANGS에 ja 포함 시 |
| Baiduspider | `Baiduspider` | zh | Baidu Ernie | Allowed / Blocked | SITE_LANGS에 zh 포함 시 |
| Baiduspider-render | `Baiduspider-render` | zh | Baidu Render | Allowed / Blocked | SITE_LANGS에 zh 포함 시 |
| SogouBot | `Sogou web spider` | zh | Sogou AI | Allowed / Blocked | SITE_LANGS에 zh 포함 시 |
| 360Spider | `360Spider` | zh | 360 AI | Allowed / Blocked | SITE_LANGS에 zh 포함 시 |

---

## Recommended robots.txt (Strategy [A/D/E/F/G])

전략에 맞는 전체 robots.txt 코드를 `/geo crawlers` 에서 생성할 수 있다.
현재 차단된 봇에 대한 즉시 수정 코드:

```
# 추가할 코드
User-agent: [차단된 봇 1]
Allow: /

User-agent: [차단된 봇 2]
Allow: /
```

검증: `curl -A "[봇 이름]" https://[도메인]/robots.txt`

---

## Platform Registration Checklist

| Platform | Language | Status | Console URL | Sitemap Submitted |
|---|---|---|---|---|
| Naver Search Advisor | ko | 등록 / 미등록 | search.naver.com/info/webmaster | 예 / 아니오 |
| Google Search Console | all | 등록 / 미등록 | search.google.com/search-console | 예 / 아니오 |
| Bing Webmaster Tools | en | 등록 / 미등록 | webmaster.bing.com | 예 / 아니오 |
| Yahoo! Japan Search Console | ja | 등록 / 미등록 | search.yahoo.co.jp/webmaster | 예 / 아니오 |
| 바이두 검색자원플랫폼 | zh | 등록 / 미등록 | ziyuan.baidu.com | 예 / 아니오 |

---

## Implementation Priority

| Priority | Task | Difficulty | Owner | Expected Impact |
|---|---|---|---|---|
| 1 | [봇 차단 해제] | Low | DevOps | AI 가시성 즉시 개선 |
| 2 | [플랫폼 등록] | Low | 운영 | 인덱싱 가속 |
| 3 | [콘텐츠 최적화] | Med | Content | 인용 가능성 향상 |
```
