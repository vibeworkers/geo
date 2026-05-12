# 국내 이커머스 4개 사이트 GEO 심층 감사 요약

**분석일:** 2026-05-11  
**대상:** Coupang, Gmarket, Musinsa, Olive Young  
**분석 범위:** 공개 웹 표면 기준의 GEO 2차 심층 감사 — robots.txt, AI crawler access, 공개 페이지 텍스트성, 인용 가능성, 콘텐츠 신뢰 신호, 기술 SEO 리스크, 플랫폼별 노출 가능성.

---

## 1. 결론

이번 2차 심층 감사의 핵심 결론은 명확합니다.

> **무신사는 GEO를 의식한 robots.txt 설계를 이미 실행하고 있고, 올리브영은 AI 봇 접근을 넓게 열어둔 상태입니다. 반면 쿠팡과 G마켓은 여전히 전통 검색엔진 중심의 robots 정책에 가깝습니다.**

| 순위 | 사이트 | 종합 GEO 점수 | 등급 | 핵심 판정 |
|---:|---|---:|---|---|
| 1 | Musinsa | 75 | 양호+ | AI 검색 봇을 명시적으로 허용. 브랜드/히스토리/뉴스룸 콘텐츠가 강함. 다만 상품·홈 주요 표면의 JS/리다이렉트 리스크 존재. |
| 2 | Olive Young | 70 | 양호 | GPTBot, OAI-SearchBot, PerplexityBot, ClaudeBot, Google-Extended 등을 경로 제한 방식으로 허용. 상품 페이지 정보성은 좋으나 홈·동적 페이지 접근성은 검증 필요. |
| 3 | Gmarket | 53 | 보통 | GPTBot은 일부 경로에 허용하나 OAI-SearchBot/Perplexity/Claude 계열이 약함. 상품 랭킹 텍스트 노출은 장점. |
| 4 | Coupang | 52 | 보통 | Google/Naver/Bing 중심. `User-agent: * Disallow: /` 구조로 AI-specific 봇 다수가 기본 차단될 가능성이 큼. 브랜드 신뢰는 강하지만 AI 검색 인용 경로가 좁음. |

---

## 2. 이번 재감사에서 달라진 판단

1차 감사는 robots.txt 중심의 빠른 비교였습니다. 이번 2차 감사는 다음을 추가했습니다.

- AI 봇별 접근 매트릭스: OpenAI, Claude, Perplexity, Google/Gemini, Bing/Copilot, Grok/xAI 관점
- 공개 페이지 텍스트성 확인: 홈, 브랜드/회사 정보, 뉴스룸, 상품/검색 표면
- 인용 가능성 평가: 직접 답변 구조, 출처 명확성, 신뢰 신호, 콘텐츠 깊이
- 이커머스 특수 리스크: 장바구니·마이페이지 보호와 공개 상품/카테고리 노출의 균형
- 실행 로드맵: robots.txt, llms.txt, 스키마, 상품 FAQ, 브랜드 지식 그래프, AI 플랫폼별 질의 테스트

---

## 3. 핵심 발견

### A. robots.txt가 이미 GEO 경쟁력의 분기점이다

- **Musinsa:** OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Perplexity-User는 완전 허용. GPTBot, Google-Extended, ClaudeBot, PerplexityBot 등은 부분 허용.
- **Olive Young:** 주요 AI 봇을 명시하고 상품·검색·기획전·회사 경로를 허용. 다만 `Crawl-delay: 5`와 제한 경로가 있어 속도·깊이 검증 필요.
- **Gmarket:** GPTBot이 `/n`, `/e`만 접근 가능. ChatGPT Search·Claude Search·Perplexity 검색 봇 명시는 부족.
- **Coupang:** Google/Naver/Bing/Daum 외 다른 봇은 `User-agent: * Disallow: /`에 걸릴 가능성이 큼.

### B. “AI가 읽기 좋은 콘텐츠”는 무신사가 가장 강하다

무신사는 회사 소개, 연혁, 뉴스룸 형태의 문맥 콘텐츠가 존재합니다. 이는 단순 상품 DB보다 AI가 브랜드를 설명하고 인용하기 좋은 구조입니다.

### C. 올리브영은 상품 정보 표면이 강하지만 동적 렌더링 리스크가 있다

상품 페이지에는 브랜드, 상품명, 가격, 배송, 재고 확인, 리뷰/Q&A, 상품정보 섹션이 잘 노출됩니다. 다만 홈 표면은 공개 텍스트 추출이 제한되어 JS 렌더링·서버 사이드 노출 여부 확인이 필요합니다.

### D. 쿠팡은 브랜드 신뢰·트래픽은 강하지만 GEO 접근 정책이 보수적이다

쿠팡은 회사 정보, 고객센터, 소비자 보호 안내, 카테고리 구조가 강하지만 ChatGPT Search/Perplexity/Claude Search 측면의 직접 인용 접근성은 약합니다.

### E. G마켓은 상품 랭킹 텍스트성은 좋지만 AI 플랫폼별 봇 분리가 부족하다

G마켓 홈은 상품명·가격·할인·멤버십 정보가 텍스트로 잘 드러납니다. 그러나 AI 검색용 봇과 학습용 봇을 분리해 관리하는 현대적 GEO 구조는 아직 약합니다.

---

## 4. 실행 우선순위 요약

| 우선순위 | 대상 | 조치 | 기대 효과 |
|---:|---|---|---|
| 1 | Coupang, Gmarket | OAI-SearchBot, PerplexityBot, Claude-SearchBot, Google-Extended 정책을 명시적으로 설계 | ChatGPT Search, Perplexity, Claude 검색 인용 가능성 회복 |
| 2 | 전 사이트 | `/llms.txt`와 선택적 `/llms-full.txt` 구축 | AI가 중요한 공개 페이지를 빠르게 파악 |
| 3 | 전 사이트 | 공개 상품·브랜드·카테고리 페이지에 Product, BreadcrumbList, Organization, FAQPage JSON-LD 검증 | AI 인용·쇼핑형 답변 구조화 |
| 4 | Musinsa, Olive Young | JS-heavy/리다이렉트 표면을 AI crawler 관점에서 재검증 | 좋은 robots 정책이 실제 콘텐츠 접근으로 이어지는지 확인 |
| 5 | 전 사이트 | “AI 답변용 브랜드 팩트 페이지” 생성 | 브랜드 정의·카테고리·대표 상품·신뢰 근거를 AI가 안정적으로 인용 |

---

## 5. 보고서 구성

- `01_Coupang_Deep_GEO_Audit.md`
- `02_Gmarket_Deep_GEO_Audit.md`
- `03_Musinsa_Deep_GEO_Audit.md`
- `04_OliveYoung_Deep_GEO_Audit.md`
- `05_Crawler_Access_Matrix.md`
- `06_Roadmap_and_Priorities.md`
- `07_Methodology_Limitations.md`
- `audit_scorecard.csv`

