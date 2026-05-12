# 한국 주요 커머스 4개사 GEO 통합 보고서

report_id: `geo-commerce-four-sites-integrated-2026-05-12`  
generated_at: `2026-05-12 Asia/Seoul`  
scope: `Coupang, Gmarket, Musinsa, Olive Young public web surfaces`  
score_type: `mixed + readiness`  
evidence_label: `integrated synthesis from mixed audit and live_public_surface_capture`  
confidence: `medium`  
evidence_path: `reports/2026-05-12-commerce-geo-audit/evidence/summary.json + reports/2026-05-12-individual-commerce-geo-audit/evidence/summary.json`  
last_verified: `2026-05-12`  
measurement_status: `not measured`  
commerce_status: `product/schema only partly observed; merchant/catalog/action eligibility not proven`  
private_surface_status: `public only`  
regional_context: `named region: Korea, Korean commerce`  
policy_risk: `caution`

## 1. Executive Conclusion

이번 통합 보고서는 기존 `mixed` GEO 감사와 후속 `live_public_surface_capture` 개별 감사를 한 문서로 정리한 결과다. 핵심 결론은 두 가지다.

첫째, `mixed` 감사 기준의 우선순위는 여전히 `무신사 > 올리브영 > 쿠팡 > G마켓`이다. 둘째, 후속 live capture 기준으로는 무신사만 공개 HTTP와 `robots.txt`가 모두 안정적으로 확인되었고, 나머지 세 사이트는 `403` 또는 challenge 때문에 public crawler readiness를 확정할 수 없었다.

따라서 지금 단계의 정확한 판정은 “무신사는 공개 GEO 준비도가 상대적으로 높고, 쿠팡·G마켓·올리브영은 봇 정책 또는 bot defense 실제 동작 검증이 선행되어야 한다”이다. 이 문서는 AI 답변 노출, citation, referral, conversion 성과 보고서가 아니다.

## 2. Source Inventory

이번 통합에 포함한 문서:

- `reports/2026-05-12-commerce-geo-audit/GEO-종합보고서.md`
- `reports/2026-05-12-commerce-geo-audit/coupang.GEO-감사-보고서.md`
- `reports/2026-05-12-commerce-geo-audit/gmarket.GEO-감사-보고서.md`
- `reports/2026-05-12-commerce-geo-audit/musinsa.GEO-감사-보고서.md`
- `reports/2026-05-12-commerce-geo-audit/oliveyoung.GEO-감사-보고서.md`
- `reports/2026-05-12-commerce-geo-audit/evidence/summary.json`
- `reports/2026-05-12-individual-commerce-geo-audit/README.md`
- `reports/2026-05-12-individual-commerce-geo-audit/coupang.GEO-개별-감사-리포트.md`
- `reports/2026-05-12-individual-commerce-geo-audit/gmarket.GEO-개별-감사-리포트.md`
- `reports/2026-05-12-individual-commerce-geo-audit/musinsa.GEO-개별-감사-리포트.md`
- `reports/2026-05-12-individual-commerce-geo-audit/oliveyoung.GEO-개별-감사-리포트.md`
- `reports/2026-05-12-individual-commerce-geo-audit/evidence/summary.json`

문서 성격은 서로 다르다.

| 문서군 | score_type | 의미 |
| --- | --- | --- |
| `commerce-geo-audit/*감사-보고서.md` | `mixed` | readiness signal과 heuristic signal을 함께 쓴 해석 보고서 |
| `individual-commerce-geo-audit/*개별-감사-리포트.md` | `readiness` | 2026-05-12 live public capture 중심 후속 점검 |
| 두 `summary.json` | evidence | 통합 요약과 개별 수치의 근거 JSON |

## 3. Integrated Scoreboard

| 사이트 | 기존 mixed 종합 점수 | 기존 판정 | 후속 readiness 점수 | live homepage | live robots | OAI-SearchBot | Claude-SearchBot | 통합 해석 |
| --- | ---: | --- | ---: | --- | --- | --- | --- | --- |
| 쿠팡 | 40 | 보통 하단 | 35 | 403 | 403 | 미확인 | 미확인 | 브랜드/상거래 규모는 강하지만 public crawler readiness는 매우 불리 |
| G마켓 | 39 | 미흡 상단 | 35 | 403 | 403 | 미확인 | 미확인 | challenge와 제한 허용 robots 해석이 모두 보수적으로 남음 |
| 무신사 | 62 | 양호 | 90 | 200 | 200 | 허용 | 허용 | 네 사이트 중 공개 GEO 준비도가 가장 명확하게 확인됨 |
| 올리브영 | 53 | 보통 | 35 | 403 | 403 | 미확인 | 미확인 | robots 의도는 비교적 GEO 친화적이지만 live public fetch는 막힘 |

## 4. 2026-05-12 Live Public Capture 후속 점검

이 장은 `reports/2026-05-12-individual-commerce-geo-audit/*`의 핵심 본문을 통합 보고서 안으로 직접 끌어온 부분이다. 여기서 쓰는 점수는 모두 `score_type=readiness`, `evidence_label=live_public_surface_capture`다.

### Coupang live capture

- 준비도 점수: `35/100`
- 검색/AI crawler 접근 준비: 제한 또는 미확인
- homepage: `403`
- robots.txt: `403`
- homepage server: `AkamaiGHost`
- challenge signal: `18.4d88fe79.1778591885.144eda69`
- title: `Access Denied`
- OAI-SearchBot: 미확인
- Claude-SearchBot: 미확인
- root merchant schema: 미확인

핵심 blocker:

1. 홈페이지 HTTP 접근이 `4xx/5xx` 또는 네트워크 오류로 확인되어 public fetch 안정성이 낮음
2. `robots.txt`를 정상 판독하지 못해 crawler control 증거가 불완전함
3. `OAI-SearchBot`의 루트 URL 접근이 robots 기준 허용으로 확인되지 않음
4. `Claude-SearchBot`의 루트 URL 접근이 robots 기준 허용으로 확인되지 않음

### Gmarket live capture

- 준비도 점수: `35/100`
- 검색/AI crawler 접근 준비: 제한 또는 미확인
- homepage: `403`
- robots.txt: `403`
- homepage server: `cloudflare`
- challenge signal: `challenge`
- title: `G마켓 - 쇼핑을 바꾸는 쇼핑`
- OAI-SearchBot: 미확인
- Claude-SearchBot: 미확인
- root merchant schema: 미확인

핵심 blocker:

1. 홈페이지 HTTP 접근이 `4xx/5xx` 또는 네트워크 오류로 확인되어 public fetch 안정성이 낮음
2. `robots.txt`를 정상 판독하지 못해 crawler control 증거가 불완전함
3. `OAI-SearchBot`의 루트 URL 접근이 robots 기준 허용으로 확인되지 않음
4. `Claude-SearchBot`의 루트 URL 접근이 robots 기준 허용으로 확인되지 않음

### Musinsa live capture

- 준비도 점수: `90/100`
- 검색/AI crawler 접근 준비: 가능
- homepage: `200`
- robots.txt: `200`
- final homepage: `https://www.musinsa.com/main/musinsa/recommend`
- title: `무신사`
- meta description: `패션의 모든 것, 다 무신사랑 해! ...`
- OAI-SearchBot: 허용
- Claude-SearchBot: 허용
- root merchant schema: 미확인
- sitemap count from robots.txt: `1`

핵심 blocker:

1. 수집된 루트 HTML에서 `Product/Offer` 계열 merchant schema가 확인되지 않음

### Olive Young live capture

- 준비도 점수: `35/100`
- 검색/AI crawler 접근 준비: 제한 또는 미확인
- homepage: `403`
- robots.txt: `403`
- homepage server: `cloudflare`
- title: `잠시만 기다려 주세요 - 올리브영`
- OAI-SearchBot: 미확인
- Claude-SearchBot: 미확인
- root merchant schema: 미확인

핵심 blocker:

1. 홈페이지 HTTP 접근이 `4xx/5xx` 또는 네트워크 오류로 확인되어 public fetch 안정성이 낮음
2. `robots.txt`를 정상 판독하지 못해 crawler control 증거가 불완전함
3. `OAI-SearchBot`의 루트 URL 접근이 robots 기준 허용으로 확인되지 않음
4. `Claude-SearchBot`의 루트 URL 접근이 robots 기준 허용으로 확인되지 않음

공통 경계:

- 이 장의 결과는 `public crawl/readiness` 점수다.
- AI 답변 노출, citation, referral, conversion 성과는 측정하지 않았다.
- 상품 상세 템플릿 전체의 `Product/Offer` 품질은 루트 URL만으로 확정하지 않는다.

## 5. Site Synthesis

### 쿠팡

- `mixed` 감사는 Akamai 기반 강한 접근 통제와 제한 허용형 `robots`를 근거로 낮은 GEO readiness를 평가했다.
- 후속 live capture에서도 홈페이지와 `robots.txt`가 모두 `403`이어서, `OAI-SearchBot`과 `Claude-SearchBot` 허용 여부를 public evidence만으로는 확인하지 못했다.
- 통합 결론: 검색/AI용 봇 정책을 기존 검색엔진 정책과 별도로 재설계하지 않으면 GEO 개선 여지가 작다.

### G마켓

- `mixed` 감사는 Cloudflare challenge와 제한 허용형 `robots` 구조를 근거로 네 사이트 중 최하위권으로 판단했다.
- 후속 live capture도 홈페이지와 `robots.txt`가 모두 `403`이었다.
- 통합 결론: 문제의 핵심은 단순 schema 부족보다 challenge와 verified crawler 통과 정책의 불일치 가능성이다.

### 무신사

- `mixed` 감사와 후속 live capture가 같은 방향을 가리킨다.
- `robots.txt`에서 `OAI-SearchBot`, `ChatGPT-User`, `Claude-SearchBot`, `Claude-User`를 허용했고, homepage와 `robots.txt` 모두 `200`으로 확인됐다.
- 다만 공개 homepage HTML에는 `Product/Offer` 계열 schema가 잡히지 않았다.
- 통합 결론: 접근 정책은 가장 앞서 있지만, AI 인용 품질과 shopping eligibility 쪽 구조화 표면은 더 보강할 여지가 있다.

### 올리브영

- `mixed` 감사는 브라우저 기준 `robots` 정책이 AI/검색 봇에 우호적일 가능성을 포착했다.
- 반면 후속 live capture에서는 홈페이지와 `robots.txt`가 모두 `403`이었다.
- 통합 결론: 문서상 허용 의도와 실제 public bot access 사이에 간극이 있을 수 있어, allowlist와 challenge 예외 규칙 검증이 우선이다.

## 6. Mixed 감사와 Live Capture를 함께 읽는 법

사이트별로 두 증거군은 같은 뜻이 아니다.

| 증거군 | 질문 | 강점 | 한계 |
| --- | --- | --- | --- |
| `mixed` 감사 | 이 사이트가 GEO 관점에서 구조적으로 어디가 약한가 | 해석과 우선순위가 풍부함 | heuristic이 포함됨 |
| `live_public_capture` | 오늘 public HTTP 기준으로 실제로 어디까지 잡히는가 | 2026-05-12 시점 공개 접근성 증거가 명확함 | challenge/차단 환경에서는 확인 범위가 좁음 |

따라서 통합 판단 규칙은 다음이 맞다.

1. `mixed` 감사가 높아도 live capture가 막히면 public crawler readiness는 보수적으로 읽는다.
2. live capture가 좋더라도 observed answer/citation이 없으면 visibility 성과로 올려 말하지 않는다.
3. 두 증거군이 같은 방향이면 우선순위 확신도를 높이고, 다르면 bot policy 또는 challenge 동작을 추가 검증한다.

## 7. Cross-Site Patterns

네 사이트를 합치면 공통 패턴이 보인다.

1. `robots` 정책과 실제 public fetch 결과를 분리해 읽어야 한다.
2. `GPTBot` 허용은 `OAI-SearchBot` 허용과 같은 뜻이 아니다.
3. 상품 상세 판매 능력과 AI shopping/action readiness는 별개다.
4. homepage 기준 공개 HTML에서는 네 사이트 모두 `Product/Offer` 계열 schema 확인이 약했다.
5. 측정 부재가 가장 큰 한계다. 현재는 readiness와 heuristic만 있고 observed answer/citation은 없다.

## 8. Evidence Boundary

이 통합 보고서가 말할 수 있는 것:

- 2026-05-12 시점 public web surface 기준으로 어떤 사이트가 더 열려 있었는지
- `robots.txt`, challenge, homepage HTTP, basic HTML metadata가 어떤 상태였는지
- 어떤 사이트가 다음 검증 라운드 우선순위가 높은지

이 통합 보고서가 말할 수 없는 것:

- ChatGPT Search, Claude Search, Google AI Overviews에서 실제로 어떤 사이트가 더 자주 인용되는지
- AI 유입이 장바구니, 주문, 전환으로 이어지는지
- 내부 feed, Search Console, merchant center, analytics, server log 기준의 실제 commerce eligibility

## 9. Prioritized Next Actions

1. 무신사는 상품 상세/카테고리/정책 URL 샘플링으로 schema와 citability 검증을 다음 단계로 바로 진행한다.
2. 쿠팡, G마켓, 올리브영은 verified crawler가 challenge 없이 통과하는지부터 확인한다.
3. 네 사이트 공통으로 prompt panel baseline을 만들어 `observed_answer`와 `observed_citation` 증거를 추가한다.
4. commerce 측정으로 넘어가려면 analytics 또는 server log 기반 `referral_signal`, `conversion_signal` 증거 체인을 연결한다.

## 10. Deliverable Map

- 기존 해석 중심 종합 문서: [GEO-종합보고서.md](</Volumes/Extend/Projects/DevWorkspace/geo/reports/2026-05-12-commerce-geo-audit/GEO-종합보고서.md>)
- 후속 live capture 요약: [README.md](</Volumes/Extend/Projects/DevWorkspace/geo/reports/2026-05-12-individual-commerce-geo-audit/README.md>)
- 개별 mixed 감사: [coupang.GEO-감사-보고서.md](</Volumes/Extend/Projects/DevWorkspace/geo/reports/2026-05-12-commerce-geo-audit/coupang.GEO-감사-보고서.md>), [gmarket.GEO-감사-보고서.md](</Volumes/Extend/Projects/DevWorkspace/geo/reports/2026-05-12-commerce-geo-audit/gmarket.GEO-감사-보고서.md>), [musinsa.GEO-감사-보고서.md](</Volumes/Extend/Projects/DevWorkspace/geo/reports/2026-05-12-commerce-geo-audit/musinsa.GEO-감사-보고서.md>), [oliveyoung.GEO-감사-보고서.md](</Volumes/Extend/Projects/DevWorkspace/geo/reports/2026-05-12-commerce-geo-audit/oliveyoung.GEO-감사-보고서.md>)
- 개별 live 감사: [coupang.GEO-개별-감사-리포트.md](</Volumes/Extend/Projects/DevWorkspace/geo/reports/2026-05-12-individual-commerce-geo-audit/coupang.GEO-개별-감사-리포트.md>), [gmarket.GEO-개별-감사-리포트.md](</Volumes/Extend/Projects/DevWorkspace/geo/reports/2026-05-12-individual-commerce-geo-audit/gmarket.GEO-개별-감사-리포트.md>), [musinsa.GEO-개별-감사-리포트.md](</Volumes/Extend/Projects/DevWorkspace/geo/reports/2026-05-12-individual-commerce-geo-audit/musinsa.GEO-개별-감사-리포트.md>), [oliveyoung.GEO-개별-감사-리포트.md](</Volumes/Extend/Projects/DevWorkspace/geo/reports/2026-05-12-individual-commerce-geo-audit/oliveyoung.GEO-개별-감사-리포트.md>)

현재 기준 의사결정 문서로는 이 `GEO-통합보고서.md`를 우선 보고, 세부 근거는 각 개별 보고서와 JSON evidence로 내려가는 구조가 가장 실용적이다.
