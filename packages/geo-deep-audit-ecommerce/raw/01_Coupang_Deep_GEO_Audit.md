# Coupang GEO 심층 감사 리포트

**대상 URL:** https://www.coupang.com/  
**분석일:** 2026-05-11  
**판정:** 보통  
**종합 GEO 점수:** 52/100

---

## 1. 결론

쿠팡은 전통 검색엔진 SEO 관점에서는 강한 기반을 갖고 있으나, **GEO 관점에서는 AI-specific crawler 접근 정책이 지나치게 보수적**입니다. 특히 `User-agent: * Disallow: /`가 마지막에 존재하고, OpenAI의 OAI-SearchBot, Anthropic의 Claude-SearchBot, PerplexityBot, Google-Extended 등이 별도로 명시되어 있지 않아, 주요 AI 검색 플랫폼의 자동 인용 가능성이 낮습니다.

즉, 쿠팡의 문제는 “사이트 신뢰가 낮다”가 아닙니다. 오히려 브랜드·상품·배송·고객 보호 신호는 매우 강합니다. 문제는 **AI가 공개 콘텐츠를 안전하게 읽고 인용하도록 설계된 별도 통로가 부족하다**는 점입니다.

---

## 2. 점수 요약

| 영역 | 점수 | 상태 | 판단 |
|---|---:|---|---|
| AI 크롤러 접근 | 38 | 미흡+ | Google/Naver/Bing/Daum 위주. AI 검색 봇 다수 기본 차단 가능성. |
| AI 인용 가능성 | 55 | 보통 | 브랜드·카테고리·상품 표면은 강하지만 AI 답변형 콘텐츠는 약함. |
| 콘텐츠 품질/E-E-A-T | 66 | 양호- | 회사 정보, 고객센터, 소비자보호 신호가 강함. |
| 기술 SEO | 62 | 양호- | sitemap 명시, 주요 검색엔진 허용. 단 AI 봇·동적 표면 검증 필요. |
| 구조화 데이터 | 35 | 미확인/미흡 | JSON-LD Product/Organization/FAQ 검증 필요. |
| 플랫폼 최적화 | 42 | 보통- | Google/Bing 기반은 강하나 ChatGPT Search·Perplexity·Claude 검색 경로 취약. |

---

## 3. 주요 근거

### 3-1. robots.txt 구조

관찰된 정책은 Googlebot, NaverBot/Yeti, Bingbot, Daum/Daumoa에 대해 상품·카테고리·검색·캠페인 경로를 허용하고, 장바구니·주문·vendor 관련 경로는 차단하는 구조입니다. 마지막에는 모든 기타 봇에 대해 `Disallow: /`가 선언되어 있습니다.

**해석:**
- 공개 상품·카테고리 페이지를 전통 검색엔진에는 노출합니다.
- 그러나 AI 전용 검색/학습 봇을 별도 그룹으로 열어두지 않았습니다.
- OAI-SearchBot, GPTBot, ClaudeBot, Claude-SearchBot, PerplexityBot, Google-Extended가 별도 허용되지 않으면 기본 차단될 가능성이 큽니다.

### 3-2. 공개 페이지 신뢰 신호

홈 표면에서는 쿠팡플레이, 로켓배송, 로켓프레시, 쿠팡비즈, 로켓직구, 골드박스 등 핵심 서비스와 카테고리가 확인됩니다. 푸터에는 회사명, 대표자, 주소, 사업자등록번호, 통신판매업 신고, 고객센터, 소비자보호 안내 등 신뢰 신호가 존재합니다.

**해석:**
- 브랜드 실체성과 거래 신뢰도는 높습니다.
- AI가 “쿠팡은 어떤 서비스인가?”에 답할 근거는 충분합니다.
- 그러나 AI 검색이 직접 접근하지 못하면 이 신뢰 신호가 AI 응답에 반영되기 어렵습니다.

---

## 4. RPD/CTA 판단

### Cues
- 전통 검색엔진별로 세밀한 Allow/Disallow가 존재.
- `User-agent: * Disallow: /`가 존재.
- OpenAI/Claude/Perplexity/Gemini 관련 봇 명시가 부족.
- 공개 회사 정보와 소비자 보호 문구는 풍부.

### Assessment
쿠팡은 “검색엔진 최적화 + 봇 방어” 모델에 가깝습니다. GEO 시대에는 공개 상품/브랜드 정보를 AI가 인용할 수 있게 하되, 주문·장바구니·마이페이지·가격 정책 민감 경로는 계속 차단하는 분리 전략이 필요합니다.

### Simulation
- 지금 상태를 유지하면 Google/Bing 기반 검색 노출은 유지됩니다.
- ChatGPT Search, Perplexity, Claude Search에서 쿠팡 원문 인용은 제한될 수 있습니다.
- 사용자는 AI에서 쿠팡 상품군을 비교할 때 쿠팡 원문보다 제3자 리뷰·블로그·가격비교 페이지를 더 자주 보게 될 수 있습니다.

### Risks
1. AI 플랫폼 내 쇼핑 답변에서 쿠팡 원문 인용이 줄어들 수 있음.
2. 외부 중개 사이트가 쿠팡의 상품·배송·멤버십 설명을 대신 정의할 수 있음.

### Next action
AI-specific robots 정책을 “검색 허용 / 학습 선택 / 거래 경로 보호” 구조로 재설계해야 합니다.

---

## 5. 권장 개선안

### 즉시 조치

```txt
# AI search crawlers — public commerce surfaces only
User-agent: OAI-SearchBot
Allow: /vp/products/
Allow: /np/categories/
Allow: /np/search?q=*
Allow: /np/campaigns/
Disallow: /vm/cart/
Disallow: /vm/direct-orders/
Disallow: /vendor-items/

User-agent: PerplexityBot
Allow: /vp/products/
Allow: /np/categories/
Allow: /np/search?q=*
Allow: /np/campaigns/
Disallow: /vm/cart/
Disallow: /vm/direct-orders/
Disallow: /vendor-items/

User-agent: Claude-SearchBot
Allow: /vp/products/
Allow: /np/categories/
Allow: /np/search?q=*
Allow: /np/campaigns/
Disallow: /vm/cart/
Disallow: /vm/direct-orders/
Disallow: /vendor-items/
```

### 단기 조치

- `/llms.txt` 생성: 카테고리, 로켓배송, 로켓프레시, 로켓와우, 쿠팡비즈, 고객센터, 회사소개, sitemap 링크 포함.
- 공개 상품 페이지에 Product, Offer, AggregateRating, BreadcrumbList JSON-LD 검증.
- “쿠팡 공식 브랜드/서비스 설명 페이지”를 AI 답변용으로 구성.

### 중장기 조치

- AI 쇼핑 질의 세트 구축: “쿠팡 로켓배송이란?”, “쿠팡 와우 멤버십 혜택”, “쿠팡 반품 정책” 등.
- ChatGPT Search/Perplexity/Gemini/Copilot에서 실제 인용 여부를 월 1회 추적.

---

## 6. 최종 판정

쿠팡은 GEO 잠재력은 매우 높지만, 현재 robots 정책은 **AI 검색에서 스스로를 보수적으로 닫는 구조**입니다. 경쟁사가 AI 봇 허용과 answer-ready 콘텐츠를 먼저 정비하면, 쿠팡은 브랜드 인지도 대비 AI 인용 점유율에서 손해를 볼 가능성이 있습니다.

