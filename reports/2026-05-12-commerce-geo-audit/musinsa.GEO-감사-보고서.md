# 무신사 GEO-SEO 감사 보고서

report_id: `geo-commerce-musinsa-2026-05-12`  
generated_at: `2026-05-12 Asia/Seoul`  
scope: `https://www.musinsa.com/` 공개 웹 표면  
score_type: `mixed`  
evidence_label: `readiness_signal + heuristic_signal`  
confidence: `high`  
evidence_path: `reports/2026-05-12-commerce-geo-audit/evidence/musinsa.json`  
last_verified: `2026-05-12`  
measurement_status: `not measured`  
commerce_status: `merchant/catalog likely ready, schema/action measurement incomplete`  
private_surface_status: `public only`  
regional_context: `named region: Korea + global hreflang surfaces`  
policy_risk: `pass`

## 1. Executive Conclusion

무신사는 네 사이트 중 GEO readiness가 가장 좋다. 홈페이지는 `200`으로 접근 가능했고, `robots.txt`는 AI 검색·사용자 요청 봇을 명시적으로 허용한다. 특히 `OAI-SearchBot`, `ChatGPT-User`, `Claude-User`, `Claude-SearchBot`을 fully granted로 둔 점은 AI 검색 readiness에 유리하다.

다만 `llms.txt`는 없고, 홈페이지 공개 HTML에서 JSON-LD가 발견되지 않았다. 즉 crawler access는 강하지만, AI가 인용하기 좋은 구조화 요약·상품/조직 schema 표면은 보강 여지가 크다.

종합 GEO 점수: **62/100 — 양호**

| 영역 | 점수 | 상태 |
|---|---:|---|
| AI 크롤러 접근 | 78 | 좋음 |
| AI 인용 가능성 | 62 | 양호 |
| 콘텐츠 품질 | 56 | 주의 |
| 기술 SEO | 66 | 양호 |
| 스키마 마크업 | 30 | 위험 |
| 플랫폼 최적화 | 70 | 양호 |

## 2. Scope And Evidence

| 확인 대상 | 관측 |
|---|---|
| 홈페이지 | `200`, 최종 URL `/main/musinsa/recommend`, 응답 약 627ms |
| `/robots.txt` | `200`, AI 검색·사용자 요청 봇 허용 |
| `/llms.txt` | `404` |
| `/sitemap.xml` | `404` |
| `/sitemap_index.xml` | `404`; robots에 `https://www.musinsa.com/sitemap-musinsa-index.xml` 명시 |
| JSON-LD | 공개 HTML 기준 0개 |
| canonical/hreflang | canonical과 다국가 `hreflang` 다수 확인 |

## 3. Platform Truth And Access Profile

무신사의 `robots.txt`는 다음 구조다.

- Fully Granted: `OAI-SearchBot`, `ChatGPT-User`, `Claude-User`, `Claude-SearchBot`, 일부 social/user fetcher
- Partially Granted: `Googlebot`, `Bingbot`, `GPTBot`, `Google-Extended`, `ClaudeBot`, `PerplexityBot` 등
- Blocked: 기타 `User-agent: *`

이 구조는 AI 검색 노출과 학습/grounding 제어를 비교적 잘 분리한다. OpenAI Search, Claude Search, 사용자 요청 기반 fetcher를 허용한 것은 GEO 관점에서 강점이다.

## 4. Measurement Status

실제 AI 답변·citation은 측정하지 않았다. 현재 점수는 readiness다. 실제 성과 확인에는 동일 prompt panel로 ChatGPT, Perplexity, Google AI Overviews, Claude Search 캡처가 필요하다.

## 5. Commerce And Action Status

무신사는 catalog와 commerce UX가 강한 편으로 추정되지만, 공개 홈페이지 수집만으로 상품 schema와 checkout/action eligibility를 증명할 수 없다.

판정:

- product_identity: `strong`
- schema_readiness: `weak on captured homepage`
- merchant_readiness: `likely strong`
- catalog_readiness: `likely strong, feed not captured`
- action_readiness: `unknown`
- measurement_readiness: `not measured`

## 6. Regional And Situational Context

무신사는 한국 패션 커머스이면서 글로벌 도메인·hreflang 표면도 갖는다. 따라서 한국어 브랜드/카테고리 질의와 영어 글로벌 패션 질의를 분리해 GEO 성과를 측정해야 한다.

## 7. Policy Risk Gate

| 항목 | 상태 | 근거 |
|---|---|---|
| robots_status | pass | AI 검색·사용자 요청 봇 명시 허용 |
| terms_status | unknown | 약관 검토 미실시 |
| privacy_status | pass | 공개 표면만 사용 |
| regulated_claims_status | pass | 규제 조언 없음 |
| brand_claims_status | caution | 실제 AI visibility 미측정 |
| commerce_eligibility_status | unknown | platform transaction eligibility 미확인 |

## 8. Prioritized Remediation Plan

1. **`llms.txt` 생성**
   - 주요 브랜드 설명, 카테고리 URL, 스타일/매거진/정책 URL, sitemap 링크를 포함한다.
   - 단, `llms.txt`는 ingestion 보장 신호가 아니라 AI 안내 heuristic으로 표시한다.

2. **Organization/WebSite/Product schema 보강**
   - 홈페이지에는 Organization/WebSite, 상품 상세에는 Product/Offer/AggregateRating, 카테고리에는 ItemList/BreadcrumbList를 검토한다.

3. **sitemap 표준 노출 정리**
   - robots에는 `sitemap-musinsa-index.xml`이 있으므로 `/sitemap.xml` 또는 `/sitemap_index.xml` 접근 경로도 안내 페이지나 리디렉션으로 연결할지 검토한다.

4. **한국어·글로벌 prompt panel 분리 측정**
   - 한국어: 브랜드, 카테고리, 배송/반품, 스타일 추천.
   - 영어: global Musinsa, Korean fashion store, K-fashion product discovery.

## 9. Remaining Gaps And Next Verification

대표 상품 URL 10개, 카테고리 URL 5개, 매거진/스타일 콘텐츠 URL 5개를 추가 샘플링하면 schema와 citability 점수의 신뢰도를 높일 수 있다.
