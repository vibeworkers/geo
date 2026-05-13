# geo-seo-skills-kr2 전체 소개 및 기능 팩트체크

검토 기준일: 2026-05-13 KST
검토 대상: `beta-B` 브랜치의 `packages/geo-seo-skills-kr2/`

이 문서는 beta-B에 추가된 GEO/SEO 스킬 패키지가 주장하는 기능이 실제로 가능한
범위인지, 그리고 그 기능이 스킬 파일과 라우팅 계약으로 만들어져 있는지 확인하는
전체 소개 문서다.

## 결론

`geo-seo-skills-kr2`는 "AI가 반드시 인용하게 만드는 도구"가 아니라, 사이트의
AI/검색 친화 준비 신호를 점검하고 일부 런타임에서는 직접 관측값을 수집하는
근거 기반 감사 패키지로 보는 것이 타당하다.

- 실제 구현: `skills/` 아래 21개 서브스킬이 존재한다.
- 기능 구성: 17개 코어 분석/보고 명령, 4개 로컬 Code 확장 명령, 2개 세션 제어
  명령으로 구성된다.
- 근거 상태: 대부분은 `Readiness` 또는 `Heuristic`이며, `/geo realtime`처럼
  플랫폼 출력, citation URL, 로그, 스크린샷을 저장할 때만 `Measured`가 가능하다.
- 한계: robots.txt, schema, hreflang, `llms.txt`, 콘텐츠 품질 점수는 실제 AI
  노출률이나 인용률을 보장하지 않는다.

## 실제 가능성 판정

현실적으로 가능한 일은 다음으로 제한된다.

| 판정 | 실제로 가능한 일 | 필요한 근거 |
|---|---|---|
| 가능 | 공개 URL의 HTML, robots.txt, sitemap, schema, hreflang, metadata, HTTP 상태를 읽고 readiness를 판단 | 실제 fetch 결과 또는 사용자가 제공한 원문 |
| 가능 | 공식 문서와 표준에 맞춰 crawler, structured data, sitemap, hreflang, platform bot 설정을 점검 | RFC/W3C/Sitemaps.org/공식 플랫폼 문서 |
| 조건부 가능 | AI 플랫폼 답변에서 URL/브랜드/citation이 나오는지 관측 | Playwright 또는 수동 캡처로 저장된 raw output |
| 조건부 가능 | 시간에 따른 변화 추세를 말함 | 동일 기준으로 반복 저장된 baseline/capture가 2회 이상 |
| 불가 | 캡처 없이 "AI가 실제로 인용한다", "노출된다", "순위가 오른다"고 단정 | 직접 관측이 없으므로 금지 |
| 불가 | `llms.txt`, schema, robots 허용만으로 플랫폼 채택이나 인용을 보장 | 제안/준비 신호일 뿐 결과 보장 근거가 아님 |

## 판정 기준

기능 주장은 아래 evidence state 중 하나로 제한한다.

| 상태 | 허용되는 주장 | 금지되는 과장 |
|---|---|---|
| `Measured` | 직접 캡처한 플랫폼 출력, citation URL, 로그, referral, conversion이 있다 | 캡처 없이 "인용됨", "노출됨"이라고 말하기 |
| `Readiness` | robots.txt, sitemap, schema, hreflang, metadata, `llms.txt` 같은 준비 신호가 있다 | 준비 신호를 실제 순위, 색인, AI 인용으로 승격하기 |
| `Heuristic` | 콘텐츠 품질, 권위 신호, 답변 구조에서 가능성을 추정한다 | 점수를 실측 성과처럼 표현하기 |
| `Manual Fallback` | 현재 런타임에서 확인하지 못해 사용자가 외부에서 확인해야 한다 | 미확인 항목을 통과로 처리하기 |

## 외부 타당성 근거

이 패키지의 기능 타당성은 내부 주장만으로 성립하지 않는다. 아래 외부 근거를
기준으로 기능별 가능 범위를 제한한다.

| 영역 | 외부 근거 | 패키지에서 가능한 주장 |
|---|---|---|
| robots.txt/크롤러 접근 | [RFC 9309](https://www.rfc-editor.org/rfc/rfc9309), [Google robots.txt 해석](https://developers.google.com/search/reference/robots_txt), [OpenAI crawlers](https://platform.openai.com/docs/bots) | 크롤러 접근 준비 상태를 판단할 수 있다. 접근 제어 또는 실제 AI 인용 증거는 아니다. |
| 구조화 데이터 | [schema.org](https://schema.org/docs/schemas.html), [Google structured data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) | JSON-LD/schema 준비 상태와 검색 이해 가능성을 점검할 수 있다. AI citation 보장은 아니다. |
| 다국어/hreflang | [Google localized versions](https://developers.google.com/search/docs/specialty/international/localized-versions) | 언어/지역별 URL 신호와 alternates 준비 상태를 점검할 수 있다. |
| 콘텐츠 품질 | [Google helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | 사람 중심 콘텐츠, 신뢰성, 권위 신호를 휴리스틱으로 평가할 수 있다. |
| 로컬 브라우저 실측 | [Playwright](https://playwright.dev/docs/intro) | 브라우저 자동화로 플랫폼 출력 캡처를 시도할 수 있다. 로그인/정책/접근 가능성에 따라 실패할 수 있다. |
| llms.txt | [llms.txt proposal](https://llmstxt.org/) | LLM용 안내 파일 초안과 배치 가이드를 만들 수 있다. 공식 웹 표준이나 플랫폼 채택 보장은 아니다. |
| 한국 검색 로컬 맥락 | [NAVER Search Advisor robots.txt](https://searchadvisor.naver.com/guide/seo-basic-robots) | NAVER/Yeti 관련 robots 구현 참고로 사용할 수 있다. 한국 서비스 동작에 대한 공식 로컬 근거다. |
| AI 크롤러 불확실성 | [arXiv:2505.21733](https://arxiv.org/abs/2505.21733), [arXiv:2503.06035](https://arxiv.org/abs/2503.06035) | robots 준수와 스크래핑 동작은 불안정할 수 있으므로 실측 없는 visibility 주장을 제한해야 한다. |

## 근거 확립성 판정

아래 판정은 "출처가 존재한다"가 아니라, 그 출처가 확립되고 인정되는 근거 층에
속하는지를 기준으로 한다.

| 기능군 | 확립성 등급 | 인정 근거 층 | 판정 | 문서 내 제한 |
|---|---|---|---|---|
| robots.txt, crawler allow/disallow, crawl readiness | 확립된 공학 표준 + 공식 구현 문서 | IETF RFC 9309, Google/OpenAI/Anthropic/Perplexity crawler 문서 | 기능 가능. 크롤러 지시 파일과 플랫폼별 bot 식별은 실제 문서 기반으로 점검할 수 있다. | 접근 제어, 보안 통제, 실제 수집/인용 보장으로 말하면 안 된다. 서버 로그나 플랫폼 캡처가 있어야 `Measured`다. |
| sitemap, canonical, HTTP 상태, 기술 SEO 신호 | 확립된 웹 운영 관행 + 공식 문서 | Sitemaps.org 프로토콜, 검색엔진 webmaster 문서 | 기능 가능. 발견 가능성/readiness 점검 근거로 충분하다. | 색인, 순위, AI 답변 채택 보장은 아니다. |
| JSON-LD/schema 구조화 데이터 | 확립된 데이터 표준 + 공식 검색 문서 | W3C JSON-LD Recommendation, schema.org, Google structured data 문서 | 기능 가능. 기계 판독 가능한 의미 부여와 검색 이해 보조로 인정된다. | AI citation 또는 rich result 발생을 보장하지 않는다. |
| hreflang/다국어 URL 신호 | 공식 검색 구현 문서 | Google localized versions/hreflang 문서 | 기능 가능. 언어/지역 URL 매핑의 readiness 점검으로 타당하다. | Google 중심 구현 근거이므로 모든 AI 플랫폼의 언어 선택 보장으로 확장하면 안 된다. |
| 콘텐츠 품질, E-E-A-T, people-first content | 공식 품질 프레임워크 + 전문가 휴리스틱 | Google helpful content 및 Search Quality Rater Guidelines 계열 문서 | 기능 가능하지만 `Heuristic`이다. 신뢰성/전문성/답변성 점검 근거로 쓸 수 있다. | 점수를 실측 ranking factor나 AI citation 확률로 표현하면 안 된다. |
| AI 플랫폼 realtime 캡처 | 도구 공식 문서 + 직접 관측 | Playwright 공식 문서, 저장된 raw output/screenshot/log | 조건부 가능. 캡처 산출물이 있을 때만 `Measured`다. | 로그인, 약관, bot 차단, UI 변경으로 실패할 수 있으며 미캡처 상태는 `Manual Fallback`이다. |
| `llms.txt` | 제안/실험 단계 | llmstxt.org proposal | 기능은 가능하지만 확립된 표준은 아니다. 초안 작성과 배치 점검까지만 타당하다. | "공식 웹 표준", "플랫폼 채택 완료", "없으면 AI 누락"이라고 말하면 안 된다. |
| AI crawler compliance/visibility 주장 | 학술/실증 주의 근거 | AI crawler/robots 준수 관련 arXiv 실증 연구 | 제한 근거로 타당하다. 불확실성 때문에 실측을 요구해야 한다는 주장에 쓴다. | 특정 플랫폼의 현재 동작을 학술 논문만으로 단정하면 안 된다. 최신 공식 문서와 로그 확인이 필요하다. |

## 전체 기능 및 매칭 표

| 명령/기능 | 실제 서브스킬 | 계층 | 레벨 | 가능한 산출물 | 최대 기본 evidence state | 타당성 판정 |
|---|---|---|---|---|---|---|
| `/geo audit` | `geo-audit` | Core | L1-L3 | 사이트 GEO/SEO 종합 감사 | `Readiness` + `Heuristic` | 가능. 기술 신호와 콘텐츠 신호를 종합하지만 AI 노출 실측은 아님 |
| `/geo brand` | `geo-brand` | Core | L1-L3 | 브랜드 인식 Gap, CP 입력, baseline | `Heuristic`; 직접 AI 답변 캡처 시 `Measured` | 조건부 가능. 캡처 없이 브랜드 인식 실측으로 표현하면 안 됨 |
| `/geo content` | `geo-content` | Core | L1-L3 | E-E-A-T/콘텐츠 품질 개선안 | `Heuristic` | 가능. 품질 평가 휴리스틱이며 검색/AI 성과 보장은 아님 |
| `/geo citability` | `geo-citability` | Core | L1-L3 | AI 인용 가능성 평가 | `Heuristic` | 가능. "인용 가능성" 추정으로만 표현해야 함 |
| `/geo crawlers` | `geo-crawlers` | Core | L1-L3 | AI/search bot 접근 준비 점검 | `Readiness` | 가능. robots와 bot 정책 신호이며 실제 준수/인용 보장은 아님 |
| `/geo brands` | `geo-brand-mentions` | Core | L1-L3 | 외부 브랜드 언급 인벤토리 | `Heuristic`; URL 캡처 시 `Measured` | 조건부 가능. 수집 URL이 있을 때만 관측값으로 인정 |
| `/geo platforms` | `geo-platform-optimizer` | Core | L1-L3 | 플랫폼별 최적화 권고 | `Readiness` + `Heuristic` | 가능. 플랫폼 문서와 준비 신호 기반 권고로 제한 |
| `/geo lang-platform` | `geo-lang-platform` | Core | L1-L3 | 언어별 AI 플랫폼/봇 전략 | `Readiness` + `Heuristic` | 가능. 지역 플랫폼 상태는 최신 공식 근거 확인 필요 |
| `/geo report` | `geo-report` | Core | L1-L3 | 종합 보고서 | 입력 evidence state 상속 | 가능. 새 증거 생성이 아니라 집계 산출물 |
| `/geo technical` | `geo-technical` | Core | L2-L3 | 기술 SEO/GEO 이슈 목록 | `Readiness` | 가능. HTTP, robots, sitemap, canonical, hreflang, schema 신호 점검 |
| `/geo multilang` | `geo-multilang` | Core | L2-L3 | 다국어/hreflang 진단 | `Readiness` + `Heuristic` | 가능. hreflang과 언어별 콘텐츠 비교는 준비/휴리스틱 |
| `/geo llmstxt` | `geo-llmstxt` | Core | L2-L3 | `llms.txt` 진단/초안 | `Readiness` + `Heuristic` | 가능하되 제안 표준으로 표시해야 함 |
| `/geo compare` | `geo-compare` | Core | L2-L3 | 경쟁 URL 비교표 | `Readiness` + `Heuristic` | 가능. 동일 기준 비교이며 플랫폼 결과 실측은 아님 |
| `/geo schema` | `geo-schema` | Core | L3 | JSON-LD 감지/생성 가이드 | `Readiness` | 가능. schema.org/Google 구조화 데이터 원리에 부합 |
| `/geo proposal` | `geo-proposal` | Core | L3 | 개선 제안서 | 입력 evidence state 상속 + `Heuristic` | 가능. 비즈니스 제안 산출물이며 실측 증거를 새로 만들지 않음 |
| `/geo prospect` | `geo-prospect` | Core/Extension | L3 | 잠재 고객 빠른 스캔 | `Readiness` + `Heuristic` | 가능. 영업 선별용 약식 판단으로 제한 |
| `/geo report-pdf` | `geo-report-pdf` | Extension | L3 | PDF용 보고서 마크다운/변환 안내 | `Manual Fallback` 또는 입력 state 상속 | 가능. 렌더러가 없으면 수동 변환 안내가 맞음 |
| `/geo realtime` | `geo-realtime` | Extension | L3 | AI 플랫폼 출력/citation 캡처 | 캡처 성공 시 `Measured` | 조건부 가능. Playwright, 로그인, 플랫폼 접근, 저장 로그가 필요 |
| `/geo tracker` | `geo-tracker` | Extension | L3 | baseline 시계열 추적 | 관측 baseline 존재 시 `Measured` | 조건부 가능. 최소 2개 이상 관측 스냅샷이 있어야 추세 판단 가능 |
| `/geo batch` | `geo-batch` | Extension | L3 | 복수 도메인 간이 비교 | `Readiness` + `Heuristic` | 가능. 빠른 선별용이며 실측 visibility는 아님 |
| `/geo-code init` | `geo-code` | Extension | L3 | Node/Playwright/CDP 환경 점검 | `Manual Fallback` 또는 환경 `Measured` | 가능. 로컬 환경 검사 자체는 측정 가능 |
| `/geo-code pipeline` | `geo-code` | Extension | L3 | audit -> realtime -> tracker 자동 순서 | 각 단계 evidence state 상속 | 조건부 가능. realtime 단계 성공 여부에 따라 `Measured`가 달라짐 |
| `/geo-code status` | `geo-code` | Extension | L3 | 분석 파일/baseline/CP 연동 상태 | 로컬 파일 관측 시 `Measured` | 가능. 로컬 파일 시스템 접근이 필요 |
| `/geo level` | 없음 | Session | L1-L3 | 사용자 레벨 변경 | evidence 비생산 | 가능. 실행 모드 변수 변경 |
| `/geo lang` | 없음 | Session | L1-L3 | 출력 언어 변경 | evidence 비생산 | 가능. 출력 언어 변수 변경 |

## 실제 스킬 구현 검토

`skills/` 아래 다음 서브스킬 파일이 존재한다.

`geo-audit`, `geo-batch`, `geo-brand`, `geo-brand-mentions`, `geo-citability`,
`geo-code`, `geo-compare`, `geo-content`, `geo-crawlers`, `geo-lang-platform`,
`geo-llmstxt`, `geo-multilang`, `geo-platform-optimizer`, `geo-proposal`,
`geo-prospect`, `geo-realtime`, `geo-report`, `geo-report-pdf`, `geo-schema`,
`geo-technical`, `geo-tracker`.

구현 관점의 판단:

- 스킬 파일 존재 여부는 충족한다.
- 대표 라우팅 계약은 `SKILL.md`가 소유한다.
- 기능별 근거 한계는 `references/function-matching-matrix.md`가 소유한다.
- 근거 색인은 `references/source-index.md`가 소유한다.
- evidence-state 정의는 `references/evidence-boundary.md`가 소유한다.
- `/geo brand`와 `/geo brands`는 서로 다른 기능이므로 트리거도 분리해야 한다.
- `/geo-code`는 확장 계층 오케스트레이터로, 라우팅 표와 매칭 표에 명시되어야 한다.

## 과장 금지 문구

다음 표현은 직접 측정값이 없는 한 사용하지 않는다.

- "AI가 인용한다"
- "ChatGPT 검색에 노출된다"
- "Perplexity가 반드시 참조한다"
- "스키마를 넣으면 AI 답변에 나온다"
- "robots 허용이면 모든 AI 크롤러가 수집한다"
- "`llms.txt`가 없으면 AI에서 누락된다"

대신 다음처럼 표현한다.

- "AI/search crawler 접근 준비 신호가 개선된다"
- "구조화 데이터가 페이지 의미를 기계가 이해하기 쉽게 만든다"
- "직접 캡처가 없으므로 현재 결과는 `Readiness`/`Heuristic`이다"
- "`llms.txt`는 제안/구현 참고이며 공식 채택 보장은 아니다"

## 검증 명령

계약이나 reference를 수정한 뒤에는 아래를 실행한다.

```bash
python3 packages/geo-seo-skills-kr2/scripts/check_kr2_evidence_contract.py
python3 scripts/check_geo_skill.py
```
