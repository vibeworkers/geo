# 쿠팡 GEO-SEO 감사 보고서

report_id: `geo-commerce-coupang-2026-05-12`  
generated_at: `2026-05-12 Asia/Seoul`  
scope: `https://www.coupang.com/` 공개 웹 표면  
score_type: `mixed`  
evidence_label: `readiness_signal + heuristic_signal`  
confidence: `medium`  
evidence_path: `reports/2026-05-12-commerce-geo-audit/evidence/coupang.json`  
last_verified: `2026-05-12`  
measurement_status: `not measured`  
commerce_status: `merchant/catalog ready 추정, public crawler/action readiness 제한`  
private_surface_status: `public only`  
regional_context: `named region: Korea, Korean commerce`  
policy_risk: `caution`

## 1. Executive Conclusion

쿠팡은 브랜드·상거래 규모 자체는 매우 강하지만, 공개 GEO readiness 관점에서는 `봇 접근 통제`가 가장 큰 병목이다. 이번 공개 수집에서 홈페이지, `robots.txt`, `llms.txt`, `sitemap.xml` 모두 로컬 HTTP 클라이언트 기준 `403 Access Denied`를 반환했다. 브라우저로 확인되는 `robots.txt`도 일반 `User-agent: *`에 `Disallow: /`를 두고, Google/Naver/Bing/Yeti/Daum 계열에 제한적 경로를 허용하는 구조로 보인다.

종합 GEO 점수: **40/100 — 보통 하단**

| 영역 | 점수 | 상태 |
|---|---:|---|
| AI 크롤러 접근 | 34 | 위험 |
| AI 인용 가능성 | 44 | 주의 |
| 콘텐츠 품질 | 52 | 주의 |
| 기술 SEO | 38 | 위험 |
| 스키마 마크업 | 30 | 위험 |
| 플랫폼 최적화 | 38 | 위험 |

## 2. Scope And Evidence

공개 URL만 확인했다. 로그인, 앱, 내부 상품 피드, 광고 계정, Search Console, 서버 로그, 전환 데이터는 쓰지 않았다.

핵심 증거:

| 확인 대상 | 관측 |
|---|---|
| 홈페이지 | `403`, `AkamaiGHost`, `Access Denied` |
| `/robots.txt` | 로컬 수집 `403`; 브라우저 확인 시 검색엔진별 제한 허용 정책 존재 |
| `/llms.txt` | `403` |
| `/sitemap.xml` | `403` |
| JSON-LD | 공개 HTTP 수집 기준 0개 |

## 3. Platform Truth And Access Profile

OpenAI의 `GPTBot`, `OAI-SearchBot`, `ChatGPT-User`, Anthropic의 `ClaudeBot`, `Claude-SearchBot`, `Claude-User`, Google의 `Googlebot`과 `Google-Extended`는 서로 다른 목적의 crawler/control surface다. 이 감사에서는 crawler 접근 가능성을 AI 노출·인용 성과로 직접 환산하지 않았다.

쿠팡의 현재 공개 접근 프로필은 `검색엔진 중심 선택 허용 + 일반/비명시 봇 차단`에 가깝다. 이 구조는 기존 검색엔진 최적화에는 방어적으로 작동할 수 있지만, ChatGPT Search, Claude Search, Perplexity류 public answer/citation readiness에는 불리하다.

## 4. Measurement Status

측정된 AI 답변, citation, referral, conversion은 없다. 따라서 이 보고서의 점수는 `readiness_signal`과 `heuristic_signal`이다.

관측되지 않은 것:

- ChatGPT, Claude, Perplexity, Google AI Overviews에서 쿠팡 URL이 실제 인용되는지
- AI 검색 유입 referrer가 있는지
- AI 유입이 장바구니·구매 전환으로 이어지는지

## 5. Commerce And Action Status

쿠팡은 상거래 인프라 자체는 강한 사이트지만, GEO commerce readiness는 “상품 판매 가능”과 “AI 플랫폼 shopping/action surface에 적합”을 분리해야 한다. 공개 수집에서는 Product/Offer schema, catalog feed, merchant policy facts, checkout/action measurement를 확인하지 못했다.

판정:

- product_identity: `likely strong, not fully captured`
- schema_readiness: `unknown/weak from public fetch`
- merchant_readiness: `likely strong, public evidence incomplete`
- catalog_readiness: `unknown`
- action_readiness: `unknown`
- measurement_readiness: `not measured`

## 6. Regional And Situational Context

한국 대형 커머스는 봇 방어, 가격·재고 동적 렌더링, 앱 중심 전환 경로가 강하다. 따라서 단순 “전체 봇 허용”이 정답은 아니다. 목표를 `AI 검색 노출 확대`와 `가격/재고/회원 혜택 보호`로 분리하고, 검색·사용자 요청 봇과 학습용 봇을 별도 정책으로 둬야 한다.

## 7. Policy Risk Gate

| 항목 | 상태 | 근거 |
|---|---|---|
| robots_status | caution | 일반 접근 `403`, robots 정책은 제한 허용형 |
| terms_status | unknown | 약관 검토 미실시 |
| privacy_status | pass | 공개 표면만 사용 |
| regulated_claims_status | pass | 규제 조언 없음 |
| brand_claims_status | caution | 브랜드 노출 성과는 미측정 |
| commerce_eligibility_status | unknown | AI shopping/action eligibility 미확인 |

## 8. Prioritized Remediation Plan

1. **AI 검색용 봇 정책 분리**
   - 담당: SEO/플랫폼/보안
   - 내용: `OAI-SearchBot`, `ChatGPT-User`, `Claude-SearchBot`, `Claude-User`, `PerplexityBot`을 학습용 봇과 분리해 허용 가능 범위를 검토한다.
   - 기대 효과: AI 검색·사용자 요청 기반 citation readiness 개선.

2. **공개 `llms.txt` 또는 AI 안내 색인 제공**
   - 담당: SEO/콘텐츠
   - 내용: 쿠팡 전체가 아니라 카테고리·브랜드·정책·도움말 중심의 안전한 AI 안내 파일을 만든다.
   - 경계: `llms.txt`는 보장 신호가 아니라 adoption-dependent heuristic이다.

3. **상품/정책 페이지 schema 샘플 검증**
   - 담당: 프론트엔드/SEO
   - 내용: Product, Offer, AggregateRating, shipping/return policy 구조화 데이터를 대표 상품군에서 검증한다.

4. **AI 답변 측정 패널 구성**
   - 담당: 마케팅/데이터
   - 내용: “쿠팡 로켓배송 반품 정책”, “쿠팡 와우 멤버십 혜택” 같은 정보성 질의와 상품 탐색 질의를 분리해 baseline을 캡처한다.

## 9. Remaining Gaps And Next Verification

다음 검증은 브라우저 렌더링, 검색엔진 캐시/색인, 대표 상품 URL, 정책 URL, Search Console 또는 서버 로그가 필요하다. 현재 보고서는 공개 HTTP와 브라우저 robots 확인 기반의 readiness 감사이며, 실제 AI citation 성과 보고서가 아니다.
