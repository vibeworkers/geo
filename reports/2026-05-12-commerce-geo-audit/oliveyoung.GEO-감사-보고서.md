# 올리브영 GEO-SEO 감사 보고서

report_id: `geo-commerce-oliveyoung-2026-05-12`  
generated_at: `2026-05-12 Asia/Seoul`  
scope: `https://www.oliveyoung.co.kr/` 공개 웹 표면  
score_type: `mixed`  
evidence_label: `readiness_signal + heuristic_signal`  
confidence: `medium`  
evidence_path: `reports/2026-05-12-commerce-geo-audit/evidence/oliveyoung.json`  
last_verified: `2026-05-12`  
measurement_status: `not measured`  
commerce_status: `merchant/catalog likely ready, public crawler/action readiness 제한`  
private_surface_status: `public only`  
regional_context: `named region: Korea, beauty/health commerce`  
policy_risk: `caution`

## 1. Executive Conclusion

올리브영은 브랜드·카테고리 측면의 AI citation 잠재력은 크지만, 공개 HTTP 수집에서는 Cloudflare challenge/대기 페이지가 반환되어 기술 접근성 점수가 낮다. 브라우저로 확인되는 `robots.txt`는 `User-agent: *`를 차단하면서도 Googlebot, Bingbot, GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-SearchBot, Claude-User, PerplexityBot 등에 주요 쇼핑 경로를 허용하는 구조다.

따라서 정책 설계 자체는 GEO 친화적인 부분이 있으나, 실제 AI crawler가 challenge 없이 대표 상품·카테고리·정책 정보를 안정적으로 가져가는지는 별도 검증이 필요하다.

종합 GEO 점수: **53/100 — 보통**

| 영역 | 점수 | 상태 |
|---|---:|---|
| AI 크롤러 접근 | 62 | 양호 |
| AI 인용 가능성 | 54 | 주의 |
| 콘텐츠 품질 | 52 | 주의 |
| 기술 SEO | 40 | 주의 |
| 스키마 마크업 | 28 | 위험 |
| 플랫폼 최적화 | 56 | 주의 |

## 2. Scope And Evidence

| 확인 대상 | 관측 |
|---|---|
| 홈페이지 | `403`, Cloudflare challenge, 제목 `잠시만 기다려 주세요 - 올리브영` |
| `/robots.txt` | 로컬 수집 `403`; 브라우저 확인 시 AI/검색 봇별 주요 경로 허용 정책 |
| `/llms.txt` | `403` |
| `/sitemap.xml` | `403` |
| JSON-LD | 공개 HTTP 수집 기준 0개 |

## 3. Platform Truth And Access Profile

올리브영의 robots 정책은 일반 접근을 막으면서도 주요 AI·검색 봇에 `/store/main/main.do`, `/store/goods`, `/store/display`, `/store/planshop` 등 쇼핑 핵심 경로를 허용하는 것으로 확인된다. 이는 `검색/상품 발견 readiness`를 의식한 구조로 볼 수 있다.

단, Cloudflare challenge가 실제 AI 검색용 crawler에도 적용되면 robots 허용만으로는 충분하지 않다. crawler allowlist, bot verification, 캐시/렌더링 정책을 함께 봐야 한다.

## 4. Measurement Status

실제 AI 답변·citation·referral·conversion은 측정하지 않았다. 현재 판단은 readiness와 heuristic이다.

## 5. Commerce And Action Status

올리브영은 뷰티·헬스 카테고리 특성상 product identity, 성분/사용법, 리뷰, 배송/반품, 오프라인 매장 정보가 AI 답변 품질에 직접 영향을 준다. Product schema만이 아니라 성분·주의사항·리뷰·정책 정보의 구조화가 중요하다.

판정:

- product_identity: `strong`
- schema_readiness: `unknown/weak from captured homepage`
- merchant_readiness: `likely strong`
- catalog_readiness: `unknown`
- action_readiness: `unknown`
- measurement_readiness: `not measured`

## 6. Regional And Situational Context

한국 H&B 커머스는 제품 효능·성분·건강 관련 표현이 규제 리스크와 연결될 수 있다. GEO 콘텐츠 개선은 “구매 추천”보다 “공식 제품 정보, 성분, 사용법, 배송/교환 정책”처럼 검증 가능한 사실 표면부터 진행해야 한다.

## 7. Policy Risk Gate

| 항목 | 상태 | 근거 |
|---|---|---|
| robots_status | caution | 주요 봇 허용 정책과 challenge가 함께 존재 |
| terms_status | unknown | 약관 검토 미실시 |
| privacy_status | pass | 공개 표면만 사용 |
| regulated_claims_status | caution | 뷰티/헬스 효능 표현은 검수 필요 |
| brand_claims_status | caution | 실제 AI visibility 미측정 |
| commerce_eligibility_status | unknown | platform transaction eligibility 미확인 |

## 8. Prioritized Remediation Plan

1. **AI crawler allowlist와 challenge 정책의 실제 동작 검증**
   - robots 허용 대상이 Cloudflare에서 challenge 없이 통과하는지 확인한다.

2. **성분·사용법·주의사항 중심 answer-ready 페이지 강화**
   - 제품 상세의 핵심 사실을 HTML 본문과 schema에 일관되게 노출한다.

3. **Product/Offer/Review/Breadcrumb schema 샘플 검증**
   - 대표 상품군에서 JSON-LD 또는 microdata 존재와 렌더링 후 유효성을 확인한다.

4. **뷰티/헬스 정책 리스크 가드**
   - 효능·의학적 표현은 공식 제품 설명과 법무/컴플라이언스 승인 문구를 기준으로 한다.

## 9. Remaining Gaps And Next Verification

대표 상품 URL, 브랜드관, 카테고리, 매장 안내, 배송/반품 정책 페이지를 추가 샘플링해야 한다. 특히 Cloudflare challenge가 AI 검색용 verified crawler에 어떻게 적용되는지 확인해야 점수 신뢰도를 높일 수 있다.
