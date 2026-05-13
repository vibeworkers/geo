# Coupang GEO 개별 감사 리포트
## Evidence-state boundary

- Measured: 이 리포트는 직접 AI 플랫폼 출력, citation URL, referral log, conversion data를 측정하지 않았다.
- Readiness: 홈페이지 초기 HTML, robots.txt, sitemap.xml, llms.txt, metadata, structured data처럼 공개 접근 가능한 설정 신호를 확인했다.
- Heuristic: 콘텐츠·브랜드·카테고리 구조가 AI 답변과 검색 시스템에서 사용되기 쉬운지 공학적으로 추론했다.
- Manual fallback: 봇 방어, 로그인, 지역 제한, 런타임 제한 때문에 직접 확인하지 못한 항목은 별도 수동 확인이 필요하다.

따라서 본문의 점수는 `heuristic readiness score`이며, 실제 ChatGPT·Claude·Perplexity·Gemini·NAVER AI 인용률 또는 노출률을 의미하지 않는다.


- 대상 URL: https://www.coupang.com/
- 감사일: 2026-05-12
- 감사 범위: 홈페이지 초기 HTML, robots.txt, sitemap.xml, llms.txt, 기본 메타/구조화 데이터 신호
- 증거 파일: `evidence/coupang.json`

## 1. 결론

GEO 준비도 점수: **0/100**

핵심 판단:

- 홈페이지 라이브 접근 실패로 AI/검색 크롤러의 기본 접근성 리스크가 큼
- meta description 부재 또는 초기 HTML에서 감지되지 않음
- canonical 링크가 초기 HTML에서 감지되지 않음
- llms.txt가 감지되지 않음
- JSON-LD 구조화 데이터가 초기 HTML에서 감지되지 않음

## 2. 라이브 접근성 증거

| 항목 | 결과 |
|---|---|
| Homepage | 접근 실패: HTTPError: HTTP Error 403: Forbidden |
| robots.txt | 접근 실패: HTTPError: HTTP Error 403: Forbidden |
| sitemap.xml | 접근 실패: HTTPError: HTTP Error 404: Not Found |
| llms.txt | 접근 실패: HTTPError: HTTP Error 403: Forbidden |

## 3. 발견성 / 인용 가능성 신호

| 신호 | 감지값 |
|---|---|
| HTML lang | 미감지 |
| Title | 미감지 |
| Meta description | 미감지 |
| OG title | 미감지 |
| OG description | 미감지 |
| Canonical | 미감지 |
| hreflang count | 0 |
| JSON-LD count | 0 |
| robots.txt 내 Sitemap | 미감지 |
| robots.txt 내 명시 AI bot user-agent | 미감지 |

## 4. GEO 관점 주요 리스크

1. 홈페이지 라이브 접근 실패로 AI/검색 크롤러의 기본 접근성 리스크가 큼
2. meta description 부재 또는 초기 HTML에서 감지되지 않음
3. canonical 링크가 초기 HTML에서 감지되지 않음
4. llms.txt가 감지되지 않음
5. JSON-LD 구조화 데이터가 초기 HTML에서 감지되지 않음
6. sitemap.xml 또는 robots.txt 내 Sitemap 지시가 확인되지 않음

## 5. 우선 개선 액션

1. `llms.txt` 또는 AI 크롤러용 안내 파일을 둘지 결정하고, 주요 카테고리/브랜드/정책/고객지원 문서의 canonical URL을 명확히 노출한다.
2. 초기 HTML에서 title, meta description, canonical, JSON-LD가 서버 렌더링 또는 크롤러 접근 가능한 형태로 확인되는지 재점검한다.
3. `robots.txt`에 Sitemap 지시를 명확히 두고, AI bot별 허용/차단 정책을 의도적으로 문서화한다.
4. 다국어 또는 글로벌 노출이 필요한 경우 `hreflang`과 언어별 대표 URL을 보강한다.
5. 브랜드/상품/카테고리 단위로 AI가 인용하기 쉬운 요약, FAQ, 정책 페이지, 구조화 데이터를 정리한다.

## 6. 증거 경계

이 리포트는 라이브 초기 접근 증거 기반의 1차 GEO 감사다. 로그인 후 개인화 화면, 앱 전용 화면, 자바스크립트 렌더 후 DOM, 실제 AI 플랫폼 질의 결과, 검색 콘솔 데이터는 포함하지 않았다.
