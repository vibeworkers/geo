# Musinsa GEO 개별 감사 리포트

## 메타데이터

- report_id: commerce-geo-individual-musinsa-2026-05-12
- generated_at: 2026-05-12T13:18:06.095279+00:00
- scope: https://www.musinsa.com/
- score_type: readiness
- evidence_label: live_public_surface_capture
- confidence: medium
- evidence_path: `reports/2026-05-12-individual-commerce-geo-audit/evidence/musinsa.json`
- last_verified: 2026-05-12
- measurement_status: not measured
- commerce_status: product/schema only
- private_surface_status: public only
- regional_context: named region: Korea / Korean ecommerce
- policy_risk: caution

## Executive Conclusion

- 준비도 점수: 90/100
- 검색/AI crawler 접근 준비: 가능
- 루트 HTML merchant schema: 미확인
- 이 점수는 public crawl/readiness 점수이며, AI 답변 노출·citation·referral·conversion 성과가 측정됐다는 뜻이 아니다.

## Scope And Evidence

- robots.txt: `https://www.musinsa.com/robots.txt` status=`200`
- homepage: `https://www.musinsa.com/main/musinsa/recommend` status=`200`
- homepage server: cloudflare
- challenge signal: 미확인
- title: 무신사
- meta description: 패션의 모든 것, 다 무신사랑 해! 무신사에서 다양한 혜택과 스타일 팁을 확인해보세요.
- canonical: https://www.musinsa.com/main/musinsa/recommend
- JSON-LD types: 미확인
- sitemap count from robots.txt: 1

## Platform Truth And Access Profile

| agent | robots 기준 루트 접근 |
| --- | --- |
| `Googlebot` | 허용 |
| `OAI-SearchBot` | 허용 |
| `GPTBot` | 허용 |
| `ChatGPT-User` | 허용 |
| `ClaudeBot` | 허용 |
| `Claude-SearchBot` | 허용 |
| `Claude-User` | 허용 |

공식 기준: OpenAI는 `OAI-SearchBot`을 ChatGPT Search 노출 관리 표면으로, `GPTBot`을 학습 crawler 표면으로, `ChatGPT-User`를 사용자 요청 fetcher로 분리한다. Google merchant listing은 `Product`와 `Offer` structured data 및 Search Console 검증을 요구한다. Anthropic은 `ClaudeBot`, `Claude-SearchBot`, `Claude-User`를 용도별로 분리한다.

근거 URL:

- OpenAI crawlers: https://developers.openai.com/api/docs/bots
- Google crawlers: https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers
- Google merchant listing structured data: https://developers.google.com/search/docs/appearance/structured-data/merchant-listing
- Anthropic crawler controls: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler

## Measurement Status

- observed_answer: 미측정
- observed_citation: 미측정
- referral_signal: 미측정
- conversion_signal: 미측정
- 필요한 다음 측정: 동일 query set으로 ChatGPT Search/Google AI/Perplexity/Claude 결과 캡처, Search Console merchant listing report, 서버 로그의 AI crawler hit, referral UTMs.

## Commerce / Action Status

- 루트 URL만 수집했으므로 상품 상세 템플릿 전체의 Product/Offer 품질은 확정하지 않는다.
- merchant listing readiness는 상품 상세 URL 샘플, 가격/재고/배송/반품 필드, canonical, robots 접근성을 별도 검증해야 한다.

## Policy Risk Gate

- public evidence only 기준으로 작성했다.
- robots.txt 허용은 visibility 보장이 아니며, 차단/미확인은 원인 분석이 필요한 risk로만 취급한다.

## Prioritized Remediation Plan

1. 수집된 루트 HTML에서 Product/Offer 계열 merchant schema가 확인되지 않음

## Remaining Gaps And Next Verification

- 상품 상세 URL 10개 이상에서 Product/Offer/price/availability/shipping/return markup을 샘플링한다.
- robots 정책 변경 후 최소 24시간 이상 경과한 뒤 OpenAI/Anthropic crawler 접근을 로그로 재확인한다.
- AI answer/citation 결과는 readiness와 별도 evidence set으로 저장한다.
