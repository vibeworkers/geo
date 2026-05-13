---
name: geo-multilang
description: >
  다국어 GEO 통합 진단. SITE_LANGS를 자동 감지하여 언어 버전별 hreflang 구현 상태,
  콘텐츠 품질 격차, AI 플랫폼 가시성 격차를 비교하고 언어별 개선 우선순위를 제시한다.
  단일 언어 사이트에서 실행 시 다국어 전환 로드맵으로 전환한다.
  L2는 운영 관점 개선 방법, L3는 코드 스니펫과 서버 설정까지 포함한다.
  트리거: "다국어", "hreflang", "언어별 SEO", "multilingual", "국제화", "i18n", "/geo multilang".
audience: L2, L3
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# geo-multilang — 다국어 GEO 통합 진단

> 실행 시 USER_LEVEL을 확인한다.
> L1인 경우 아래 안내 메시지를 출력하고 실행을 중단한다.
> L2 또는 L3인 경우 아래 5개 단계를 순서대로 실행한다.
> 결과는 USER_LEVEL에 맞는 출력 템플릿으로 전달하고 `GEO-다국어-[도메인]-[날짜].md`로 저장한다.

---

## L1 접근 안내 (L1이면 이 메시지 출력 후 중단)

```
다국어 GEO 진단은 hreflang 설정과 언어별 코드 수정이 필요한 기술 작업입니다.

현재 레벨(마케팅 담당자)에서는 직접 실행이 어렵습니다.

선택 사항:
1. 레벨을 변경하려면 `/geo level` 을 입력하세요.
2. 개발팀 또는 운영팀에 아래 내용을 전달하세요:

   "사이트의 다국어 hreflang 설정과 언어별 AI 가시성 상태를
    점검하고 개선 항목을 알려주세요.
    명령어: /geo multilang https://[도메인]"
```

---

## 실행 단계

### 1단계: 언어 버전 감지

> **Claude Code 환경:** Bash 스크립트로 정확히 수집
> **Claude 웹 환경:** WebFetch로 HTML 분석 + 수동 확인

**Claude Code 환경 (Bash)**

```bash
python3 -c "
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re

url = '[TARGET_URL]'
parsed = urlparse(url)
base = f'{parsed.scheme}://{parsed.netloc}'

r = requests.get(url, headers={'User-Agent': 'GEO-Audit/1.0'}, timeout=15)
soup = BeautifulSoup(r.text, 'html.parser')

# html lang 속성
html_lang = soup.find('html').get('lang', '없음') if soup.find('html') else '없음'
print(f'html lang: {html_lang}')

# hreflang 태그
hreflangs = soup.find_all('link', rel='alternate')
hreflang_tags = [t for t in hreflangs if t.get('hreflang')]
langs = []
urls_by_lang = {}
for tag in hreflang_tags:
    lang = tag.get('hreflang', '')
    href = tag.get('href', '')
    langs.append(lang)
    urls_by_lang[lang] = href
    print(f'  hreflang=\"{lang}\" href=\"{href}\"')

print(f'감지된 언어: {langs}')
print(f'x-default: {\"있음\" if \"x-default\" in langs else \"없음\"}')

# URL 패턴에서 언어 감지
url_langs = re.findall(r'/([a-z]{2})(?:-[A-Z]{2})?/', base + '/')
print(f'URL 패턴 언어: {list(set(url_langs))}')
"
```

**Claude 웹 환경 (WebFetch 대체)**

WebFetch로 대상 URL을 로드하고 다음을 확인한다.
- `<html lang="">` — 기본 언어
- `<link rel="alternate" hreflang="...">` — 모든 hreflang 태그 목록
- URL 경로 패턴 (`/ko/`, `/en/`, `/ja/` 등)

수집 결과로 SITE_LANGS를 구성한다.

```
SITE_LANGS 자동 구성 우선순위:
1. hreflang 태그에서 수집된 언어 코드 (x-default 제외)
2. html lang 속성 값
3. URL 패턴 (/ko/, /en/ 등)
4. 감지 불가 → ["ko"] 기본값
```

---

### 2단계: hreflang 구현 상태 검증

`references/hreflang-checklist.md` 기준으로 검사한다.

#### 2-1. 필수 항목 검사 (F1–F5)

| 코드 | 항목 | 결과 | 점수 |
|---|---|---|---|
| F1 | x-default 설정 | Pass / Fail | /4 |
| F2 | 모든 언어 버전 hreflang 태그 존재 | Pass / Fail | /3 |
| F3 | 언어-지역 코드 정확성 | Pass / Fail | /3 |
| F4 | 양방향 참조 완성 | Pass / Fail | /4 |
| F5 | 자기 참조(self-reference) 포함 | Pass / Fail | /2 |

#### 2-2. URL 일관성 검사 (U1–U4)

| 코드 | 항목 | 결과 | 점수 |
|---|---|---|---|
| U1 | 절대 URL 사용 | Pass / Fail | /1 |
| U2 | canonical 충돌 없음 | Pass / Fail | /1 |
| U3 | 실제 200 응답 | Pass / Fail | /1 |
| U4 | robots.txt 차단 없음 | Pass / Fail | /1 |

#### 2-3. 언어 버전 완전성 검사 (C1–C3)

| 코드 | 항목 | 결과 |
|---|---|---|
| C1 | 누락된 언어 버전 없음 | Pass / Fail |
| C2 | 언어별 페이지 수 일치 | Pass / Fail / 부분 |
| C3 | 고아 페이지 없음 (hreflang 참조 URL 404 없음) | Pass / Fail |

**hreflang 점수: [합산]/20점**

#### 2-4. URL 구조 평가

| 구조 방식 | 감지 여부 | GEO 권장도 |
|---|---|---|
| 서브디렉토리 (`/ko/`) | 예 / 아니오 | 높음 |
| 서브도메인 (`ko.`) | 예 / 아니오 | 보통 |
| ccTLD (`.kr`) | 예 / 아니오 | 조건부 |
| 쿼리 파라미터 (`?lang=ko`) | 예 / 아니오 | 낮음 |

---

### 3단계: 언어별 콘텐츠 품질 비교

SITE_LANGS의 각 언어 버전 URL을 개별 WebFetch/Bash로 수집하여 비교한다.

**평가 항목**

| 항목 | 기준 | 평가 방식 |
|---|---|---|
| 번역 완성도 | 기준 언어 대비 페이지 수 비율 | hreflang 등록 수 비교 |
| 콘텐츠 길이 | 기준 언어 페이지 대비 90% 이상 | HTML 텍스트 길이 비교 |
| 제목·메타 번역 | `<title>`, `<meta description>` 해당 언어로 작성 | 태그 언어 확인 |
| 구조화 데이터 | JSON-LD에 `inLanguage` 속성 존재 | script 태그 파싱 |
| 날짜 형식 | 해당 언어 날짜 표기법 준수 | 텍스트 패턴 매칭 |

**언어별 콘텐츠 품질 등급**

```
각 언어 버전에 대해 다음 등급을 산출한다:
- COMPLETE (90%+): 번역 완성, 품질 이상 없음
- PARTIAL (60~89%): 부분 번역, 일부 섹션 미번역
- STUB (30~59%): 기본 구조만 번역, 내용 빈약
- MISSING (30% 미만): 번역 미완성 또는 기계 번역 의심
```

---

### 4단계: 언어별 AI 플랫폼 가시성 비교

`references/lang-platform-map.md` 기준으로 각 언어의 AI 플랫폼 접근 상태를 진단한다.

**언어별 핵심 봇 접근 상태**

SITE_LANGS에 포함된 언어별로 아래 항목을 확인한다.

| 언어 | 핵심 AI 플랫폼 | 핵심 봇 | robots.txt 허용 | 권장 전략 |
|---|---|---|---|---|
| ko | 네이버 AI 브리핑·AI 탭 | Yeti·NaverBot | 예 / 아니오 | 전략 D |
| en | ChatGPT·Perplexity·Copilot | GPTBot·PerplexityBot·Bingbot | 예 / 아니오 | 전략 A |
| ja | Yahoo! Japan AI·ChatGPT | YahooSeeker·GPTBot | 예 / 아니오 | 전략 E |
| zh | Baidu Ernie·360 AI·Sogou AI | Baiduspider·360Spider·Sogou web spider | 예 / 아니오 | 전략 F |
| es | ChatGPT·Perplexity·Gemini | GPTBot·PerplexityBot·Google-Extended | 예 / 아니오 | 전략 A |

**전체 사이트 권장 전략**

```
SITE_LANGS 조합 → 권장 전략 매핑:
- ["ko"] → 전략 D
- ["en"] → 전략 A
- ["ko", "en"] → 전략 D (= A + 한국 봇)
- ["ko", "en", "ja"] → 전략 D + E
- ["ko", "en", "ja", "zh"] → 전략 G (전체 허용)
- 그 외 → 전략 G
```

---

### 5단계: 종합 점수 산출 및 보고서 출력

**다국어 GEO 점수 (100점)**

| 차원 | 배점 | 설명 |
|---|---|---|
| hreflang 구현 | 30점 | 2단계 점수를 20점 → 30점으로 환산 |
| 언어별 콘텐츠 품질 | 30점 | COMPLETE(30) / PARTIAL(20) / STUB(10) / MISSING(0) 평균 |
| AI 봇 접근 | 20점 | SITE_LANGS 각 언어 핵심 봇 허용률 |
| URL 구조 | 10점 | 서브디렉토리(10) / 서브도메인(7) / ccTLD(7) / 쿼리파라미터(0) |
| 구조화 데이터 | 10점 | inLanguage·availableLanguage·translationOfWork 등 |

**점수 등급표**

| 점수 | 등급 | 상태 |
|---|---|---|
| 80–100 | 우수 | 다국어 GEO 최적화 완료 |
| 60–79 | 양호 | 일부 언어 버전 개선 여지 |
| 40–59 | 보통 | hreflang 또는 콘텐츠 격차 존재 |
| 20–39 | 미흡 | 다국어 구현 불완전, 즉각 조치 필요 |
| 0–19 | 위험 | 다국어 설정 부재 또는 심각한 오류 |

---

## 레벨별 출력 템플릿

---

### L2 출력 — 웹마스터 / 운영자

운영·CMS에서 직접 조치할 수 있는 항목 중심으로 정리한다.

```markdown
# [사이트명] 다국어 GEO 진단

진단일: [날짜]  |  URL: [URL]  |  감지 언어: [SITE_LANGS]

---

## 다국어 GEO 점수: [점수]/100 — [등급]

| 차원 | 점수 | 상태 |
|---|---|---|
| hreflang 구현 | [X]/30 | [등급] |
| 언어별 콘텐츠 품질 | [X]/30 | [등급] |
| AI 봇 접근 | [X]/20 | [등급] |
| URL 구조 | [X]/10 | [서브디렉토리·서브도메인·ccTLD·쿼리파라미터] |
| 구조화 데이터 | [X]/10 | [등급] |

---

## hreflang 현황

| 항목 | 상태 | 조치 |
|---|---|---|
| x-default | 있음 / 없음 | [없으면 추가 방법] |
| 양방향 참조 | 완성 / 미완성 | [미완성이면 수정 방법] |
| 언어-지역 코드 | 정확 / 오류 | [오류 코드 목록] |

**운영팀 즉시 조치 가능 항목:**
1. [조치 항목] — [CMS/FTP 경로 및 수정 방법]
2. [조치 항목]

**개발팀 요청 항목:**
- [조치 항목] — [이유 및 요청 내용]

---

## 언어별 콘텐츠 품질

| 언어 | 등급 | 페이지 수 | 주요 문제 |
|---|---|---|---|
| [언어] | COMPLETE / PARTIAL / STUB / MISSING | [X]페이지 | [문제 한 줄] |

---

## AI 플랫폼 접근 현황

| 언어 | AI 플랫폼 | 봇 허용 | 현재 상태 |
|---|---|---|---|
| ko | 네이버 AI 브리핑 | Yeti·NaverBot | 허용 / 차단 |
| en | ChatGPT·Perplexity | GPTBot·PerplexityBot | 허용 / 차단 |
| [기타] | [플랫폼] | [봇] | [상태] |

**권장 전략: [A / D / E / F / G]**
→ robots.txt 수정 방법은 `/geo crawlers` 결과를 참고하세요.

---

## 우선순위별 개선 과제

### 즉시 처리 가능 (운영팀)
1. [항목]: [방법]
2. [항목]: [방법]

### 개발팀 요청
- [항목]: [요청 내용]
```

---

### L3 출력 — 개발자

전체 기술 명세, 코드 스니펫, 서버 설정을 포함한다.

```markdown
# [사이트명] Multilingual GEO Analysis

Date: [날짜]  |  URL: [URL]  |  SITE_LANGS: [언어 목록]

---

## Multilingual GEO Score: [점수]/100

| Dimension | Score | Findings |
|---|---|---|
| hreflang Implementation | [X]/30 | [발견 목록] |
| Content Quality per Lang | [X]/30 | [발견 목록] |
| AI Bot Access | [X]/20 | [발견 목록] |
| URL Structure | [X]/10 | [구조 방식] |
| Structured Data | [X]/10 | [발견 목록] |

---

## hreflang Audit

| Check | Code | Result | Score |
|---|---|---|---|
| x-default | F1 | Pass / Fail | /4 |
| All lang versions tagged | F2 | Pass / Fail | /3 |
| Code accuracy | F3 | Pass / Fail | /3 |
| Bidirectional reference | F4 | Pass / Fail | /4 |
| Self-reference | F5 | Pass / Fail | /2 |
| Absolute URLs | U1 | Pass / Fail | /1 |
| No canonical conflict | U2 | Pass / Fail | /1 |
| 200 response | U3 | Pass / Fail | /1 |
| Not blocked by robots | U4 | Pass / Fail | /1 |
| **Total** | | | **/20** |

**Detected hreflang tags:**
```html
<link rel="alternate" hreflang="ko-KR" href="https://example.com/ko/">
<link rel="alternate" hreflang="en-US" href="https://example.com/en/">
<link rel="alternate" hreflang="x-default" href="https://example.com/">
```

**Fix — Missing x-default:**
```html
<!-- <head> 내부에 추가 -->
<link rel="alternate" hreflang="x-default" href="https://[도메인]/">
```

**Fix — Bidirectional reference (ko 페이지에서 en을 참조하지 않는 경우):**
```html
<!-- ko 페이지에 추가 -->
<link rel="alternate" hreflang="en-US" href="https://[도메인]/en/">
```

---

## Content Quality per Language

| Language | Grade | Pages | Title Translated | Meta Translated | inLanguage |
|---|---|---|---|---|---|
| ko | COMPLETE / PARTIAL / STUB | [X] | Yes / No | Yes / No | Yes / No |
| en | COMPLETE / PARTIAL / STUB | [X] | Yes / No | Yes / No | Yes / No |
| [기타] | — | [X] | — | — | — |

**Fix — inLanguage 구조화 데이터 추가:**
```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "inLanguage": "ko-KR",
  "url": "https://[도메인]/ko/",
  "name": "[페이지 제목]"
}
```

---

## AI Bot Access Matrix

| Language | Platform | Bot | Status | Fix |
|---|---|---|---|---|
| ko | 네이버 AI 브리핑 | Yeti | Allowed / Blocked | robots.txt Allow: / |
| ko | 네이버 AI 탭 | NaverBot | Allowed / Blocked | robots.txt Allow: / |
| en | ChatGPT | GPTBot | Allowed / Blocked | — |
| ja | Yahoo! Japan AI | YahooSeeker | Allowed / Blocked | robots.txt Allow: / |
| zh | Baidu Ernie | Baiduspider | Allowed / Blocked | robots.txt Allow: / |

**Recommended Strategy: [A / D / E / F / G]**
→ `/geo crawlers` 에서 전체 robots.txt 코드 생성 가능

---

## Implementation Priority

| Priority | Task | File/Location | Difficulty | Owner |
|---|---|---|---|---|
| 1 | [작업] | [경로] | Low / Med / High | [FE/BE/DevOps] |
| 2 | [작업] | [경로] | [난이도] | [담당] |
| 3 | [작업] | [경로] | [난이도] | [담당] |
```
