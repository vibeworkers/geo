# Musinsa GEO 심층 감사 리포트

**대상 URL:** https://www.musinsa.com/  
**분석일:** 2026-05-11  
**판정:** 양호+  
**종합 GEO 점수:** 75/100

---

## 1. 결론

무신사는 4개 사이트 중 **GEO 대응 신호가 가장 강합니다.** robots.txt에 OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Perplexity-User를 완전 허용하고, GPTBot, Google-Extended, ClaudeBot, PerplexityBot 등을 부분 허용합니다. robots.txt 상단에 최근 갱신일도 표기되어 있어 AI crawler 정책을 의식적으로 관리하고 있을 가능성이 큽니다.

무신사의 가장 큰 강점은 단순 상품몰이 아니라 **브랜드 스토리, 연혁, 뉴스룸, 문화 콘텐츠**를 가지고 있다는 점입니다. 이는 AI가 무신사를 “패션 커머스/플랫폼/브랜드 생태계”로 설명하기 좋은 근거가 됩니다.

약점은 `www.musinsa.com` 루트가 글로벌 위치 선택 페이지로 리다이렉트되고, 일부 상품/브랜드 리스트 페이지가 공개 텍스트 추출에서 비어 보인다는 점입니다. 즉, robots 정책은 강하지만 실제 콘텐츠 접근성은 경로별 검증이 필요합니다.

---

## 2. 점수 요약

| 영역 | 점수 | 상태 | 판단 |
|---|---:|---|---|
| AI 크롤러 접근 | 88 | 우수 | 주요 AI 검색/학습 봇을 가장 세밀하게 구분. |
| AI 인용 가능성 | 72 | 양호 | About/Newsroom/History는 강함. 상품 표면은 추가 검증 필요. |
| 콘텐츠 품질/E-E-A-T | 82 | 우수 | 연혁, 브랜드 맥락, 뉴스룸 문서가 풍부. |
| 기술 SEO | 69 | 양호- | sitemap·robots 우수. 루트 리다이렉트/JS 표면은 리스크. |
| 구조화 데이터 | 50 | 보통 | JSON-LD 실검증 필요. Organization/Article/Product 확장 권고. |
| 플랫폼 최적화 | 82 | 우수 | ChatGPT Search, Claude Search, Perplexity 대응이 가장 좋음. |

---

## 3. 주요 근거

### 3-1. robots.txt 구조

무신사 robots.txt는 세 그룹으로 분리됩니다.

- Fully Granted: Applebot, facebookexternalhit, Twitterbot, OAI-SearchBot, ChatGPT-User, Claude-User, Claude-SearchBot, Perplexity-User
- Partially Granted: Googlebot, NaverBot, Bingbot, GPTBot, Google-Extended, ClaudeBot, PerplexityBot, Amazonbot 등
- Blocked: 기타 모든 봇

**해석:**
- AI 검색용 봇과 학습용 봇을 구분해 관리합니다.
- 공개 표면은 열고, 인증·마이페이지·좋아요·쿠폰 등 개인화/민감 경로는 차단합니다.
- 이 구조는 이번 4개 사이트 중 가장 GEO 친화적입니다.

### 3-2. 콘텐츠 표면

무신사 뉴스룸과 회사 소개/연혁 페이지는 날짜, 서비스명, 사업 확장, 브랜드 성장 맥락을 제공합니다. 이는 AI가 무신사를 단순 쇼핑몰이 아니라 “패션 플랫폼/문화 커머스/브랜드 생태계”로 이해하는 데 유리합니다.

**해석:**
- AI 인용에 필요한 문맥 콘텐츠가 존재합니다.
- 상품 DB만 있는 사이트보다 브랜드 인식·권위 신호가 강합니다.
- 다만 실제 상품/브랜드 페이지가 JS 렌더링 중심이면 검색형 AI가 충분히 읽지 못할 수 있습니다.

---

## 4. RPD/CTA 판단

### Cues
- robots.txt에 2025-10-24 갱신 표기.
- OAI-SearchBot, Claude-SearchBot, Perplexity-User 명시 허용.
- GPTBot, Google-Extended, ClaudeBot, PerplexityBot 부분 허용.
- About/History/Newsroom 콘텐츠 풍부.
- 일부 루트/상품 표면 추출 제한.

### Assessment
무신사는 GEO의 기술 접근 조건은 상당히 앞서 있습니다. 다음 경쟁력은 “AI가 인용할 만한 패션 지식/브랜드 지식/카테고리 지식”을 얼마나 구조화하느냐입니다.

### Simulation
- ChatGPT Search나 Perplexity가 무신사 관련 질의에서 공식 무신사 콘텐츠를 인용할 가능성이 높습니다.
- “무신사란?”, “무신사 브랜드”, “무신사 글로벌”, “무신사 스탠다드” 같은 브랜드 질의에는 강합니다.
- “남자 겨울 코트 추천”, “러닝화 브랜드 비교” 같은 상품/카테고리 질의에서는 페이지 렌더링·스키마·FAQ 구조가 결과를 좌우할 수 있습니다.

### Risks
1. robots 정책은 우수하지만 JS-heavy 상품 표면이 AI 추출을 제한할 수 있음.
2. 브랜드 콘텐츠는 강하나 상품·카테고리별 answer-ready 구조가 부족하면 커머스 전환형 AI 답변에서 약해질 수 있음.

### Next action
기술 접근성 검증을 상품/브랜드/카테고리 핵심 URL 단위로 확장하고, 카테고리별 AI 답변용 콘텐츠를 구축해야 합니다.

---

## 5. 권장 개선안

### 즉시 조치

- 핵심 URL 30개에 대해 AI crawler별 접근 테스트: OAI-SearchBot, GPTBot, Claude-SearchBot, PerplexityBot, Googlebot.
- `www.musinsa.com` 루트 리다이렉트가 한국 사용자·AI crawler에게 어떤 canonical 신호를 주는지 확인.
- 상품/브랜드 페이지에서 서버 응답 HTML에 최소 핵심 텍스트가 포함되는지 점검.

### 단기 조치

- `/llms.txt` 구축: 회사소개, 뉴스룸, 브랜드, 카테고리, 랭킹, 매거진, 스타일 콘텐츠, sitemap 링크.
- 뉴스룸 Article/NewsArticle JSON-LD 검증.
- 브랜드 페이지 Organization/Brand/ProductGroup/BreadcrumbList 구조화.
- 카테고리별 FAQ: “무신사에서 브랜드를 찾는 방법”, “무신사 랭킹 기준”, “무신사 스탠다드란?”

### 중장기 조치

- AI 패션 가이드 허브 구축: 코디, 사이즈, 시즌 트렌드, 브랜드 비교, 소재 설명.
- 무신사 내부 콘텐츠와 외부 언론/커뮤니티 언급을 연결하는 sameAs/brand graph 정비.

---

## 6. 최종 판정

무신사는 이번 비교군에서 GEO 준비도가 가장 높습니다. 이미 crawler gate는 열려 있습니다. 다음 과제는 **열린 문을 통해 AI가 읽을 수 있는 구조화된 지식 자산을 얼마나 잘 배치하느냐**입니다.

