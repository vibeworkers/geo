# G마켓 GEO-SEO 감사 보고서

report_id: `geo-commerce-gmarket-2026-05-12`  
generated_at: `2026-05-12 Asia/Seoul`  
scope: `https://www.gmarket.co.kr/` 공개 웹 표면  
score_type: `mixed`  
evidence_label: `readiness_signal + heuristic_signal`  
confidence: `medium`  
evidence_path: `reports/2026-05-12-commerce-geo-audit/evidence/gmarket.json`  
last_verified: `2026-05-12`  
measurement_status: `not measured`  
commerce_status: `merchant/catalog ready 추정, public crawler/action readiness 제한`  
private_surface_status: `public only`  
regional_context: `named region: Korea, Korean commerce`  
policy_risk: `caution`

## 1. Executive Conclusion

G마켓은 공개 HTTP 수집 기준 Cloudflare challenge가 강하게 작동하며, 홈페이지와 `robots.txt`가 `403`을 반환했다. 브라우저로 확인되는 `robots.txt`는 `User-agent: *`에 `Disallow: /`를 두고, GoogleBot, BingBot, Yeti, Daumoa, Twitterbot, GPTBot 등에 일부 경로(`/n`, `/e`)를 허용하는 구조다.

종합 GEO 점수: **39/100 — 미흡 상단**

| 영역 | 점수 | 상태 |
|---|---:|---|
| AI 크롤러 접근 | 36 | 위험 |
| AI 인용 가능성 | 42 | 주의 |
| 콘텐츠 품질 | 46 | 주의 |
| 기술 SEO | 36 | 위험 |
| 스키마 마크업 | 28 | 위험 |
| 플랫폼 최적화 | 36 | 위험 |

## 2. Scope And Evidence

공개 URL만 확인했다. 수집기는 홈페이지, `robots.txt`, `llms.txt`, `sitemap.xml`, `sitemap_index.xml`을 확인했다.

| 확인 대상 | 관측 |
|---|---|
| 홈페이지 | `403`, Cloudflare challenge, `cf-mitigated: challenge` |
| `/robots.txt` | 로컬 수집 `403`, 브라우저 확인 시 제한 허용형 robots 정책 |
| `/llms.txt` | `403` |
| `/sitemap.xml` | `403` |
| JSON-LD | 공개 HTTP 수집 기준 0개 |

## 3. Platform Truth And Access Profile

GPTBot 일부 허용은 “OpenAI 학습용 crawler 접근 일부 가능성”에 가깝고, `OAI-SearchBot`이나 `ChatGPT-User` 허용과 같은 뜻이 아니다. ChatGPT Search, Claude Search, Perplexity citation readiness는 별도로 봐야 한다.

G마켓의 접근 프로필은 `선택된 기존 검색/학습 봇 일부 허용 + 일반 crawler 차단 + challenge 기반 보호`다. AI 검색 readiness를 높이려면 검색용 봇과 사용자 요청 fetcher를 학습용 봇과 분리해야 한다.

## 4. Measurement Status

측정된 AI 답변·인용·유입·전환은 없다. 점수는 준비도와 간접 신호만 의미한다.

## 5. Commerce And Action Status

상거래 기능 자체와 AI commerce/action readiness는 분리된다. 공개 challenge 때문에 대표 상품의 Product/Offer schema, feed consistency, policy facts, action surface를 확인하지 못했다.

판정:

- product_identity: `likely strong, public capture limited`
- schema_readiness: `unknown/weak from public fetch`
- merchant_readiness: `likely strong, public evidence incomplete`
- catalog_readiness: `unknown`
- action_readiness: `unknown`
- measurement_readiness: `not measured`

## 6. Regional And Situational Context

G마켓은 한국 오픈마켓 맥락상 판매자·가격·재고·프로모션 변동성이 크다. AI가 정확한 답을 만들려면 상품 페이지보다 정책, 카테고리, 판매자 신뢰, 배송·반품 안내 같은 안정 정보 표면을 먼저 정리하는 편이 효과적이다.

## 7. Policy Risk Gate

| 항목 | 상태 | 근거 |
|---|---|---|
| robots_status | caution | 제한 허용형 robots와 challenge 동시 존재 |
| terms_status | unknown | 약관 검토 미실시 |
| privacy_status | pass | 공개 표면만 사용 |
| regulated_claims_status | pass | 규제 조언 없음 |
| brand_claims_status | caution | 실제 AI visibility 미측정 |
| commerce_eligibility_status | unknown | platform eligibility 미확인 |

## 8. Prioritized Remediation Plan

1. **AI 검색 봇 허용 정책 재설계**
   - `OAI-SearchBot`, `ChatGPT-User`, `Claude-SearchBot`, `Claude-User`, `PerplexityBot`을 명시적으로 검토한다.
   - GPTBot 허용과 검색 노출 readiness를 분리해서 문서화한다.

2. **안정 정보 페이지를 AI 인용 후보로 강화**
   - 반품, 배송, 판매자 신뢰, 고객보호, 멤버십 혜택 페이지를 answer-ready 구조로 정리한다.

3. **대표 상품/카테고리 schema 샘플링**
   - Cloudflare challenge 뒤 실제 렌더링 HTML에서 Product, Offer, BreadcrumbList, Organization schema를 검증한다.

4. **Prompt panel 기반 baseline 측정**
   - G마켓 브랜드 질의, 카테고리 추천 질의, 정책 질의를 나누어 ChatGPT, Perplexity, Google AI Overviews 캡처를 만든다.

## 9. Remaining Gaps And Next Verification

Cloudflare challenge를 우회하지 않고 공개 표면만 사용했으므로, 실제 사용자 브라우저 렌더링 결과와 검색엔진용 봇 처리 결과는 별도 검증이 필요하다.
