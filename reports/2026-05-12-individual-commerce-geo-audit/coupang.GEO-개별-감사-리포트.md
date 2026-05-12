# Coupang GEO 개별 감사 리포트

## 메타데이터

- report_id: commerce-geo-individual-coupang-2026-05-12
- generated_at: 2026-05-12T13:18:05.427570+00:00
- scope: https://www.coupang.com/
- score_type: readiness
- evidence_label: live_public_surface_capture
- confidence: low
- evidence_path: `reports/2026-05-12-individual-commerce-geo-audit/evidence/coupang.json`
- last_verified: 2026-05-12
- measurement_status: not measured
- commerce_status: product/schema only
- private_surface_status: public only
- regional_context: named region: Korea / Korean ecommerce
- policy_risk: caution

## Executive Conclusion

- 준비도 점수: 35/100
- 검색/AI crawler 접근 준비: 제한 또는 미확인
- 루트 HTML merchant schema: 미확인
- 이 점수는 public crawl/readiness 점수이며, AI 답변 노출·citation·referral·conversion 성과가 측정됐다는 뜻이 아니다.

## Scope And Evidence

- robots.txt: `https://www.coupang.com/robots.txt` status=`403`
- homepage: `https://www.coupang.com/` status=`403`
- homepage server: AkamaiGHost
- challenge signal: 18.4d88fe79.1778591885.144eda69
- title: Access Denied
- meta description: 미확인
- canonical: 미확인
- JSON-LD types: 미확인
- sitemap count from robots.txt: 0

## Platform Truth And Access Profile

| agent | robots 기준 루트 접근 |
| --- | --- |
| `Googlebot` | 미확인 |
| `OAI-SearchBot` | 미확인 |
| `GPTBot` | 미확인 |
| `ChatGPT-User` | 미확인 |
| `ClaudeBot` | 미확인 |
| `Claude-SearchBot` | 미확인 |
| `Claude-User` | 미확인 |

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

1. 홈페이지 HTTP 접근이 4xx/5xx 또는 네트워크 오류로 확인되어 public fetch 안정성이 낮음
2. robots.txt를 정상 판독하지 못해 crawler control 증거가 불완전함
3. OAI-SearchBot의 루트 URL 접근이 robots 기준 허용으로 확인되지 않음
4. Claude-SearchBot의 루트 URL 접근이 robots 기준 허용으로 확인되지 않음

## Remaining Gaps And Next Verification

- 상품 상세 URL 10개 이상에서 Product/Offer/price/availability/shipping/return markup을 샘플링한다.
- robots 정책 변경 후 최소 24시간 이상 경과한 뒤 OpenAI/Anthropic crawler 접근을 로그로 재확인한다.
- AI answer/citation 결과는 readiness와 별도 evidence set으로 저장한다.
