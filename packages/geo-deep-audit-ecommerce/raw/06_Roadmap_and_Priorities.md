# 국내 이커머스 GEO 개선 로드맵

**분석일:** 2026-05-11

---

## 1. 결론

4개 사이트의 개선 방향은 동일하지 않습니다.

- **Coupang:** AI 봇 접근 정책부터 열어야 합니다.
- **Gmarket:** GPTBot 일부 허용을 AI 검색 플랫폼 전체로 확장해야 합니다.
- **Musinsa:** 이미 열려 있는 접근성을 상품/브랜드/카테고리 지식 자산으로 전환해야 합니다.
- **Olive Young:** 상품 데이터 구조화와 뷰티 카테고리 answer-ready 콘텐츠가 핵심입니다.

---

## 2. 우선순위별 실행 계획

### Sprint 1 — 즉시 처리, 1~2주

| 대상 | 작업 | 담당 | 난이도 | 기대 효과 |
|---|---|---|---|---|
| Coupang | OAI-SearchBot, PerplexityBot, Claude-SearchBot 공개 경로 허용안 작성 | SEO/DevOps | 낮음~보통 | AI 검색 접근성 회복 |
| Gmarket | GPTBot 외 AI 검색 봇 정책 추가 | SEO/DevOps | 낮음 | ChatGPT Search/Perplexity 노출 가능성 확대 |
| Musinsa | 핵심 URL 30개 AI crawler 접근 테스트 | SEO/FE | 보통 | robots 정책이 실제 콘텐츠 접근으로 이어지는지 검증 |
| Olive Young | 핵심 상품/카테고리 URL 접근성 테스트 | SEO/FE | 보통 | JS/dynamic 리스크 확인 |
| 전 사이트 | `/llms.txt` 초안 작성 | SEO/콘텐츠/DevOps | 낮음 | AI가 중요 공개 URL을 파악 |

### Sprint 2 — 단기 처리, 3~4주

| 대상 | 작업 | 담당 | 난이도 | 기대 효과 |
|---|---|---|---|---|
| 전 사이트 | Organization + sameAs JSON-LD 검증 | FE/SEO | 낮음 | 브랜드 정체성 명확화 |
| 전 사이트 | Product/Offer/BreadcrumbList JSON-LD 검증 | FE/SEO | 보통 | 상품형 AI 답변 인용성 강화 |
| Musinsa | 뉴스룸 Article/NewsArticle 스키마 정비 | FE/PR | 낮음 | 브랜드·뉴스 인용성 강화 |
| Olive Young | 뷰티 상품 FAQPage/HowTo 스키마 시범 적용 | FE/콘텐츠 | 보통 | 뷰티 질의 답변성 강화 |
| Gmarket | 베스트/이벤트/카테고리 설명 문단 추가 | 콘텐츠 | 보통 | 상품 목록을 해석 가능한 콘텐츠로 변환 |

### Sprint 3 — 중장기 처리, 1~3개월

| 대상 | 작업 | 담당 | 난이도 | 기대 효과 |
|---|---|---|---|---|
| Coupang | 로켓배송/와우/반품정책 AI 답변 허브 구축 | 콘텐츠/브랜드 | 보통 | 쿠팡 서비스 정의 선점 |
| Gmarket | 카테고리별 구매 가이드 구축 | 콘텐츠/MD | 보통 | 추천·비교형 AI 질의 대응 |
| Musinsa | AI 패션 가이드 허브 구축 | 콘텐츠/브랜드 | 보통~높음 | 패션 지식 출처화 |
| Olive Young | 피부 타입/성분/사용법별 구매 가이드 | 콘텐츠/MD | 보통~높음 | 뷰티 AI 답변 선점 |
| 전 사이트 | 월간 AI 플랫폼 질의 모니터링 | SEO/GEO | 보통 | ROI 추적과 개선 루프 구축 |

---

## 3. 우선 적용해야 할 질의 세트

### Coupang
- 쿠팡 로켓배송이란?
- 쿠팡 와우 멤버십 혜택은?
- 쿠팡 반품 정책은?
- 쿠팡 로켓프레시와 일반배송 차이는?

### Gmarket
- G마켓 베스트 상품은 어떻게 정해지나?
- G마켓 스마일배송이란?
- G마켓에서 노트북을 고를 때 기준은?
- G마켓 할인/쿠폰 혜택은 어떻게 확인하나?

### Musinsa
- 무신사는 어떤 플랫폼인가?
- 무신사 스탠다드란?
- 무신사에서 브랜드를 찾는 방법은?
- 2026년 남성 패션 트렌드 추천은?

### Olive Young
- 올리브영에서 민감성 피부 선크림 추천은?
- 올리브영 베스트 상품은 어떻게 보나?
- 클렌징폼 고르는 기준은?
- 성분별 스킨케어 상품 선택 기준은?

---

## 4. 운영 지표

| 지표 | 측정 방법 | 주기 |
|---|---|---|
| AI crawler 접근 성공률 | 핵심 URL × 봇별 HTTP 접근 테스트 | 월 1회 |
| ChatGPT Search 인용률 | 표준 질의 20개 수동/자동 테스트 | 월 1회 |
| Perplexity 인용률 | 출처 포함 여부 확인 | 월 1회 |
| Gemini/Copilot 노출률 | 브랜드/상품/카테고리 질의 테스트 | 월 1회 |
| 스키마 유효성 | Rich Results Test / schema validator | 배포 전후 |
| llms.txt 최신성 | URL 목록/업데이트 날짜 확인 | 월 1회 |

