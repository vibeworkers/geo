# hreflang 검사 체크리스트

작성일: 2026-05-09  
용도: `geo-technical`, `geo-multilang` 스킬의 hreflang 분석 기준 문서

---

## 1. hreflang 개요

hreflang은 같은 콘텐츠의 언어·지역별 버전을 검색엔진과 AI 크롤러에 알리는 HTML 속성이다.  
잘못 설정된 hreflang은 AI 크롤러가 잘못된 언어 버전을 수집하거나 중복 콘텐츠로 판단하는 원인이 된다.

**GEO 관점 영향:**
- AI 크롤러가 언어에 맞는 페이지 버전을 정확히 수집 → 언어별 인용 가능성 상승
- 잘못된 설정 → 영어 쿼리에 한국어 페이지가 인용되는 등 언어 불일치 발생

---

## 2. hreflang 구현 방식 3가지

| 방식 | 위치 | 예시 | 권장도 |
|---|---|---|---|
| HTML `<link>` 태그 | `<head>` 내부 | `<link rel="alternate" hreflang="ko" href="https://example.com/ko/">` | 높음 |
| HTTP 헤더 | 서버 응답 헤더 | `Link: <https://example.com/ko/>; rel="alternate"; hreflang="ko"` | 보통 (비HTML 파일에 적합) |
| XML Sitemap | sitemap.xml | `<xhtml:link rel="alternate" hreflang="ko" href="..."/>` | 높음 (대규모 사이트) |

---

## 3. 언어·지역 코드 기준

### 3-1. 언어 코드 (ISO 639-1)

| 언어 | 코드 |
|---|---|
| 한국어 | `ko` |
| 영어 | `en` |
| 일본어 | `ja` |
| 중국어 간체 | `zh` |
| 스페인어 | `es` |
| 프랑스어 | `fr` |
| 독일어 | `de` |
| 포르투갈어 | `pt` |

### 3-2. 언어-지역 코드 조합 (ISO 639-1 + ISO 3166-1)

| 대상 | 코드 | 비고 |
|---|---|---|
| 한국어 (한국) | `ko-KR` | |
| 영어 (미국) | `en-US` | |
| 영어 (영국) | `en-GB` | |
| 영어 (호주) | `en-AU` | |
| 일본어 (일본) | `ja-JP` | |
| 중국어 간체 (중국) | `zh-CN` | |
| 중국어 번체 (대만) | `zh-TW` | |
| 중국어 번체 (홍콩) | `zh-HK` | |
| 스페인어 (스페인) | `es-ES` | |
| 스페인어 (멕시코) | `es-MX` | |
| 스페인어 (아르헨티나) | `es-AR` | |
| 스페인어 (콜롬비아) | `es-CO` | |
| 포르투갈어 (브라질) | `pt-BR` | |
| 포르투갈어 (포르투갈) | `pt-PT` | |

### 3-3. x-default

| 코드 | 용도 |
|---|---|
| `x-default` | 어떤 언어·지역에도 해당하지 않는 사용자를 위한 기본 페이지. 필수 설정. |

---

## 4. 필수 검사 항목

### 4-1. 기본 구조 검사 (반드시 통과해야 함)

```
□ F1. x-default 설정
      <link rel="alternate" hreflang="x-default" href="[기본 URL]">
      → 미설정 시: 언어 매칭 실패 사용자에게 기본 페이지 지정 불가

□ F2. 각 언어 버전 hreflang 태그 존재
      사이트에 /ko/, /en/, /ja/ 등 언어 버전이 있으면 모든 버전에 hreflang 태그 필수

□ F3. 언어-지역 코드 정확성
      올바른 예: ko-KR, en-US, zh-CN, zh-TW
      잘못된 예: ko_KR (언더스코어 불가), KO (대문자 불가), kor (3자리 불가)

□ F4. 양방향 참조 완성
      A 페이지가 B 페이지를 hreflang으로 가리키면, B 페이지도 A 페이지를 가리켜야 함
      → 단방향 참조 시 검색엔진·AI 크롤러가 신호를 무시할 수 있음

□ F5. 자기 참조(self-reference) 포함
      각 페이지는 자기 자신도 hreflang에 포함해야 함
      예) ko 페이지에서: hreflang="ko-KR" href="[현재 페이지 URL]"
```

### 4-2. URL 일관성 검사

```
□ U1. 절대 URL 사용
      상대 URL(href="/ko/") 사용 시 도메인 혼용 환경에서 오작동 가능
      → 반드시 https://example.com/ko/ 형태로 기입

□ U2. canonical과 충돌 없음
      hreflang에 명시된 URL이 canonical 태그와 일치해야 함
      충돌 예: hreflang="ko" href="https://example.com/ko/"
              canonical → https://example.com/ (언어 버전이 canonical로 정규화되면 무효)

□ U3. hreflang URL이 실제 200 응답
      hreflang에 기입한 URL이 리디렉션(301·302) 없이 직접 200 응답해야 함
      → 리디렉션 체인이 있으면 AI 크롤러가 최종 URL을 hreflang 대상으로 인식하지 못할 수 있음

□ U4. robots.txt 차단 없음
      hreflang에 명시된 언어 버전 URL이 robots.txt에 차단되지 않았는가
      → 차단된 URL을 hreflang에 기입해도 크롤러가 접근 불가
```

### 4-3. 언어 버전 완전성 검사

```
□ C1. 누락된 언어 버전 없음
      사이트에 존재하는 모든 언어 버전이 hreflang에 포함됐는가
      예) /ko/, /en/, /ja/ 세 버전이 있는데 /ja/가 hreflang 미등록이면 일본어 크롤러에 미노출

□ C2. 언어별 페이지 수 일치
      ko 버전 100페이지, en 버전 50페이지인 경우:
      → en에 미번역 50페이지는 hreflang 미등록 또는 x-default 지정 권장

□ C3. 고아 페이지 없음
      hreflang이 참조하는 URL 중 실제로 존재하지 않는 페이지(404) 없음
```

---

## 5. 경고 항목 (Warning — 권장사항)

```
△ W1. Sitemap에 hreflang 포함 여부
      대규모 사이트(1,000페이지 이상)는 HTML 태그 방식 외에 sitemap에도 hreflang 추가 권장

△ W2. 언어별 sitemap 분리 여부
      ko.xml, en.xml, ja.xml 등 언어별 sitemap을 분리하면 크롤러 효율 향상

△ W3. HTTP 헤더 hreflang (비HTML 파일)
      PDF·CSV 등 비HTML 파일에 다국어 버전이 있으면 HTTP 헤더 방식으로 hreflang 설정

△ W4. 지역 세분화 필요 여부
      스페인어 사이트: es 단일 코드보다 es-ES, es-MX 등 지역 분리 권장
      중국어 사이트: zh 단일 코드보다 zh-CN, zh-TW 분리 권장

△ W5. Crawl-delay 설정
      언어별 URL에 과도한 Crawl-delay(30초 초과) 설정 여부 확인
```

---

## 6. 언어별 URL 구조 평가

| 구조 방식 | 예시 | GEO 권장도 | 장점 | 단점 |
|---|---|---|---|---|
| **서브디렉토리** | `example.com/ko/` | 높음 | 단일 도메인 크롤 예산 집중, 관리 편의 | 없음 |
| **서브도메인** | `ko.example.com` | 보통 | 서버 분리 용이 | 별도 크롤 예산 소모, 권위 분산 |
| **ccTLD** | `example.co.kr` | 조건부 | 지역 신뢰도 최고 | 관리 비용 높음, 복수 도메인 |
| **쿼리 파라미터** | `example.com?lang=ko` | 낮음 | 구현 간단 | AI 크롤러 혼란, 캐시 비효율 |

---

## 7. 진단 코드 (Claude Code 환경 Bash)

```bash
python3 -c "
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

url = '[TARGET_URL]'
r = requests.get(url, headers={'User-Agent': 'GEO-Audit/1.0'}, timeout=15)
soup = BeautifulSoup(r.text, 'html.parser')

# hreflang 태그 수집
hreflangs = soup.find_all('link', rel='alternate')
print(f'hreflang 태그 수: {len(hreflangs)}개')
print()

has_x_default = False
langs = []
for tag in hreflangs:
    lang = tag.get('hreflang', '')
    href = tag.get('href', '')
    if lang == 'x-default':
        has_x_default = True
    langs.append(lang)
    print(f'  hreflang=\"{lang}\" href=\"{href}\"')

print()
print(f'x-default: {\"있음\" if has_x_default else \"없음 (경고)\"}')
print(f'감지된 언어: {langs}')
"
```

---

## 8. 점수 산정 기준 (geo-multilang·geo-technical 공통)

| 항목 | 배점 | 감점 조건 |
|---|---|---|
| x-default 설정 | 4점 | 미설정 시 0점 |
| 양방향 참조 완성 | 4점 | 단방향 존재 시 -2점 |
| 언어-지역 코드 정확성 | 4점 | 오류 코드 1개당 -1점 |
| 언어 버전 완전성 | 4점 | 누락 버전 1개당 -1점 |
| canonical 충돌 없음 | 2점 | 충돌 발견 시 0점 |
| 실제 200 응답 | 2점 | 404 URL 존재 시 0점 |
| **합계** | **20점** | |

> geo-technical 기술 점수(0~100점) 내 hreflang 항목 최대 20점으로 반영.

---

## 9. 변경 이력

| 날짜 | 변경 내용 |
|---|---|
| 2026-05-09 | 최초 작성. 필수 5개·경고 5개 항목, 언어별 URL 구조 평가, 진단 코드, 점수 산정 기준 포함 |
