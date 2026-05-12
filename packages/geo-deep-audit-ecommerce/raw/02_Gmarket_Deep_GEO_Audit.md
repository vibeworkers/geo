# Gmarket GEO 심층 감사 리포트

**대상 URL:** https://www.gmarket.co.kr/  
**분석일:** 2026-05-11  
**판정:** 보통  
**종합 GEO 점수:** 53/100

---

## 1. 결론

G마켓은 쿠팡보다 AI 접근에 한 발 더 나아가 있습니다. robots.txt에서 GPTBot을 명시하고 `/n`, `/e` 경로를 허용합니다. 그러나 이는 **학습용 GPTBot 중심의 제한 허용**에 가깝고, ChatGPT Search용 OAI-SearchBot, Claude-SearchBot, PerplexityBot, Google-Extended 등은 명시되어 있지 않습니다.

G마켓의 강점은 **상품 랭킹·가격·할인·배송 정보가 공개 텍스트로 잘 드러난다**는 점입니다. 약점은 **AI 검색 플랫폼별 봇 분리와 브랜드 설명/인용용 구조가 부족하다**는 점입니다.

---

## 2. 점수 요약

| 영역 | 점수 | 상태 | 판단 |
|---|---:|---|---|
| AI 크롤러 접근 | 49 | 보통- | GPTBot 일부 허용. OAI/Claude/Perplexity 계열 미흡. |
| AI 인용 가능성 | 58 | 보통 | 상품 랭킹 텍스트는 좋으나 답변형 콘텐츠 부족. |
| 콘텐츠 품질/E-E-A-T | 64 | 양호- | 상품명·가격·혜택 정보 노출 양호. 신뢰/브랜드 설명 강화 필요. |
| 기술 SEO | 58 | 보통 | 공개 텍스트성은 좋으나 sitemap/스키마/동적 표면 검증 필요. |
| 구조화 데이터 | 35 | 미확인/미흡 | Product/Breadcrumb/Organization JSON-LD 실검증 필요. |
| 플랫폼 최적화 | 45 | 보통- | Google/Bing/Naver 기반은 가능. ChatGPT Search·Perplexity·Claude 약함. |

---

## 3. 주요 근거

### 3-1. robots.txt 구조

robots.txt는 기본적으로 `User-agent: * Disallow: /`를 선언한 뒤, GoogleBot, BingBot, Yeti, Daumoa, Twitterbot, GPTBot, AdsBot-Google, Ads-Naver에 대해 `Crawl-delay: 1`, `Allow: /n`, `Allow: /e`를 제공합니다.

**해석:**
- GPTBot은 일부 공개 경로 접근이 가능합니다.
- 그러나 ChatGPT Search에 중요한 OAI-SearchBot이 보이지 않습니다.
- PerplexityBot, Claude-SearchBot, ClaudeBot, Google-Extended도 별도 정책이 없습니다.
- AI 검색 인용보다는 전통 검색/광고/일부 학습 허용 구조에 가깝습니다.

### 3-2. 공개 콘텐츠 표면

홈 페이지에서 “지금 제일 잘 나가는 상품”과 순위형 상품 목록, 상품명, 가격, 할인율, 멤버십 혜택, 배송 정보가 텍스트로 추출됩니다.

**해석:**
- 상품 추천형 AI 질의에 사용할 수 있는 원천 정보가 존재합니다.
- 하지만 제품별 FAQ, 카테고리 설명, 비교 기준, 공식 구매 가이드가 구조화되어 있지 않으면 AI가 단순 가격 목록 이상으로 인용하기 어렵습니다.

---

## 4. RPD/CTA 판단

### Cues
- GPTBot 명시 허용.
- 허용 경로가 `/n`, `/e`로 제한됨.
- 상품 랭킹·가격 정보의 텍스트 노출이 좋음.
- OAI-SearchBot, Claude-SearchBot, PerplexityBot 미확인.

### Assessment
G마켓은 AI 학습/검색을 완전히 닫은 사이트는 아닙니다. 하지만 봇 정책이 플랫폼별로 충분히 분리되어 있지 않아, “AI 검색 답변에 인용되는 쇼핑몰”로는 아직 약합니다.

### Simulation
- GPTBot 기반 장기 학습 신호는 일부 발생할 수 있습니다.
- ChatGPT Search/Perplexity/Claude Search의 직접 인용은 제한될 수 있습니다.
- 상품 랭킹 페이지가 AI에 읽히면 가격/혜택 정보는 강점이 됩니다.

### Risks
1. 실시간 AI 검색에서 G마켓 원문보다 가격비교/블로그/제휴 콘텐츠가 더 많이 인용될 수 있음.
2. 상품 데이터는 풍부하지만 브랜드와 카테고리 설명이 약하면 AI가 G마켓의 차별성을 설명하지 못함.

### Next action
GPTBot 중심 허용에서 AI 검색 플랫폼별 허용 구조로 전환해야 합니다.

---

## 5. 권장 개선안

### 즉시 조치

```txt
User-agent: OAI-SearchBot
Allow: /n
Allow: /e

User-agent: PerplexityBot
Allow: /n
Allow: /e

User-agent: Claude-SearchBot
Allow: /n
Allow: /e

User-agent: Google-Extended
Allow: /n
Allow: /e
```

단, 로그인·결제·장바구니·개인화·내 계정 경로는 계속 차단해야 합니다.

### 단기 조치

- `/llms.txt` 생성: 홈, 베스트, 카테고리, 이벤트, 판매자센터, 고객센터, 회사정보, sitemap 링크 포함.
- 카테고리별 AI 답변용 설명 추가: “G마켓 베스트란?”, “스마일배송/스마일클럽 혜택”, “G마켓 상품 랭킹 산정 기준”.
- Product/Offer/BreadcrumbList/Organization JSON-LD 검증.

### 중장기 조치

- 카테고리별 “구매 가이드” 콘텐츠 생성: 노트북, 생필품, 패션, 식품 등.
- AI 쇼핑 질의별 실제 노출 추적: ChatGPT Search, Perplexity, Gemini, Copilot.

---

## 6. 최종 판정

G마켓은 상품 정보 텍스트성에서 쿠팡보다 GEO 전환 여지가 조금 더 잘 보입니다. 그러나 현재 구조는 “AI가 상품을 읽을 수 있다” 수준이지, “AI가 G마켓을 신뢰 가능한 쇼핑 답변 출처로 선택한다” 수준은 아닙니다.

