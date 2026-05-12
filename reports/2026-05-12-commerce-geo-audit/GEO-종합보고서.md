# 한국 주요 커머스 4개사 GEO 종합 감사 보고서

report_id: `geo-commerce-four-sites-2026-05-12`  
generated_at: `2026-05-12 Asia/Seoul`  
scope: `Coupang, Gmarket, Musinsa, Olive Young public web surfaces`  
score_type: `mixed`  
evidence_label: `readiness_signal + heuristic_signal`  
confidence: `medium`  
evidence_path: `reports/2026-05-12-commerce-geo-audit/evidence/summary.json`  
last_verified: `2026-05-12`  
measurement_status: `not measured`  
commerce_status: `product/schema only partly observed; merchant/catalog/action eligibility not proven`  
private_surface_status: `public only`  
regional_context: `named region: Korea, Korean commerce`  
policy_risk: `caution`

## 1. Executive Conclusion

이번 감사는 `/GEO` 실행 번들의 `geo-audit`, `geo-crawlers`, `geo-citability`, `geo-content`, `geo-technical`, `geo-schema`, `geo-platform-optimizer`, `geo-report`, commerce readiness, measurement loop, policy risk gate를 통합해 수행했다.

결론은 명확하다. 네 사이트 모두 브랜드와 커머스 자산은 강하지만, AI 검색/GEO readiness는 `봇 접근 정책`, `challenge/403`, `llms.txt 부재`, `공개 HTML의 구조화 데이터 확인 한계`, `실제 AI citation 측정 부재`에서 갈린다.

순위:

| 순위 | 사이트 | 종합 점수 | 판정 | 핵심 이유 |
|---:|---|---:|---|---|
| 1 | 무신사 | 62 | 양호 | AI 검색·사용자 요청 봇 허용, 홈페이지 200, hreflang 존재 |
| 2 | 올리브영 | 53 | 보통 | robots 정책은 AI 친화적이나 challenge가 공개 접근성을 낮춤 |
| 3 | 쿠팡 | 40 | 보통 하단 | 브랜드는 강하지만 일반/AI crawler 접근 통제가 강함 |
| 4 | G마켓 | 39 | 미흡 상단 | Cloudflare challenge와 제한적 robots 허용으로 AI 검색 readiness 약함 |

## 2. Scope And Evidence

감사 대상:

- `https://www.coupang.com/`
- `https://www.gmarket.co.kr/`
- `https://www.musinsa.com/`
- `https://www.oliveyoung.co.kr/`

사용 증거:

- 공개 HTTP 수집: 홈페이지, `robots.txt`, `llms.txt`, `sitemap.xml`, `sitemap_index.xml`
- 공개 HTML 메타: title, description, canonical, hreflang, JSON-LD 수
- 브라우저 확인: 각 사이트 `robots.txt`의 접근 정책
- GEO 내부 primary/expert source map: OpenAI/Google/Anthropic crawler docs, commerce readiness references

비사용 증거:

- 로그인·회원 표면
- 앱 전용 화면
- 광고 계정, Search Console, analytics, 서버 로그
- 내부 상품 feed, 주문·전환 데이터
- 실제 AI 플랫폼 prompt 결과

## 3. Platform Truth And Access Profile

AI crawler 토큰은 같은 의미가 아니다.

| 구분 | 예 | 의미 |
|---|---|---|
| 학습 crawler | `GPTBot`, `ClaudeBot` | 모델 개선/학습 계열 접근 제어 |
| 검색 crawler | `OAI-SearchBot`, `Claude-SearchBot`, `Googlebot`, `Bingbot` | 검색·색인·검색 기반 답변 후보성 |
| 사용자 요청 fetcher | `ChatGPT-User`, `Claude-User` | 사용자가 요청한 URL/콘텐츠 접근 |
| product/control token | `Google-Extended` | Google Search가 아니라 Gemini/Vertex AI 계열 제어 |

따라서 “GPTBot 허용”만으로 ChatGPT Search 노출을 주장할 수 없고, “Googlebot 허용”만으로 Google AI Overviews 노출을 주장할 수 없다.

## 4. Measurement Status

이번 결과는 `readiness_signal + heuristic_signal`이다. 측정된 AI visibility가 아니다.

측정으로 전환하려면 다음 capture가 필요하다.

| evidence label | 필요한 증거 |
|---|---|
| observed_answer | 플랫폼, 프롬프트, 날짜, locale/account, 답변 캡처 |
| observed_citation | 답변 캡처 + visible source URL |
| referral_signal | analytics/server log/referrer/UTM |
| conversion_signal | add-to-cart/order/lead/CRM event tied to AI/search path |

## 5. Commerce And Action Status

네 사이트 모두 commerce capability 자체는 강하지만, AI commerce readiness는 아래 레이어로 분리해야 한다.

| 사이트 | product identity | schema readiness | merchant readiness | catalog/feed | checkout/action | measurement |
|---|---|---|---|---|---|---|
| 쿠팡 | 강함 추정 | 미확인 | 강함 추정 | 미확인 | 미확인 | 미측정 |
| G마켓 | 강함 추정 | 미확인 | 강함 추정 | 미확인 | 미확인 | 미측정 |
| 무신사 | 강함 | 홈페이지 약함 | 강함 추정 | 강함 추정 | 미확인 | 미측정 |
| 올리브영 | 강함 | 미확인 | 강함 추정 | 미확인 | 미확인 | 미측정 |

Product schema는 필요 조건일 수 있지만, AI shopping/action eligibility의 충분 조건은 아니다.

## 6. Regional And Situational Context

한국 대형 커머스의 공통 조건:

- 봇 방어와 검색 노출의 균형이 중요하다.
- 상품 가격·재고·쿠폰·회원 혜택은 동적이며 AI 답변 오류 위험이 크다.
- 정책, 배송, 반품, 멤버십, 브랜드관, 카테고리 가이드 같은 안정 정보가 AI 인용 후보로 더 적합하다.
- 뷰티/헬스 계열은 효능·성분 표현의 정책 리스크가 있다.

## 7. Policy Risk Gate

| 사이트 | robots | terms | privacy | regulated claims | brand claims | commerce eligibility |
|---|---|---|---|---|---|---|
| 쿠팡 | caution | unknown | pass | pass | caution | unknown |
| G마켓 | caution | unknown | pass | pass | caution | unknown |
| 무신사 | pass | unknown | pass | pass | caution | unknown |
| 올리브영 | caution | unknown | pass | caution | caution | unknown |

정책상 이 보고서는 법률 자문이 아니며, 사이트 약관·내부 보안 정책·플랫폼 eligibility 검토를 대체하지 않는다.

## 8. Prioritized Remediation Plan

### 전체 공통 즉시 과제

1. **AI 검색용 crawler와 학습용 crawler 정책 분리**
   - `OAI-SearchBot`, `ChatGPT-User`, `Claude-SearchBot`, `Claude-User`, `PerplexityBot`을 `GPTBot`, `ClaudeBot`, `Google-Extended`와 분리해 결정한다.

2. **AI 인용 후보 표면을 상품 상세보다 안정 정보로 먼저 설계**
   - 배송, 반품, 고객보호, 멤버십, 카테고리 가이드, 브랜드 공식 설명을 answer-ready 구조로 만든다.

3. **`llms.txt` 또는 AI 안내 파일 도입**
   - 도입하되 “AI 노출 보장”이 아니라 heuristic/adoption-dependent 신호로 관리한다.

4. **대표 URL 샘플링 기반 schema 검증**
   - 홈, 카테고리, 상품, 정책, 매거진/가이드 URL을 나눠 Product/Offer/Organization/WebSite/BreadcrumbList/FAQPage를 확인한다.

5. **Prompt panel baseline 측정**
   - 변경 전후 같은 프롬프트로 ChatGPT, Perplexity, Google AI Overviews, Claude Search를 캡처한다.

### 사이트별 최우선

| 사이트 | 이번 주 최우선 |
|---|---|
| 쿠팡 | AI 검색용 봇 허용 정책을 기존 검색엔진 정책과 별도 검토 |
| G마켓 | Cloudflare challenge가 verified crawler를 막는지 확인 |
| 무신사 | `llms.txt`와 Organization/Product schema 보강 |
| 올리브영 | robots 허용과 Cloudflare 통과 정책의 실제 일치 여부 검증 |

## 9. Remaining Gaps And Next Verification

다음 라운드는 네 단계로 닫아야 한다.

1. 대표 URL 샘플 수집: 사이트별 홈 1, 카테고리 5, 상품 10, 정책 5.
2. 렌더링 HTML 검증: JSON-LD, canonical, hreflang, noindex, content visibility.
3. AI platform capture: 동일 prompt panel로 answer/citation 캡처.
4. measurement linkage: analytics/referral/conversion 이벤트 확인.

현재 보고서는 `공개 표면 readiness 감사`이며, 실제 AI 플랫폼 노출·인용·전환 성과 리포트가 아니다.
