# Methodology and Limitations

**분석일:** 2026-05-11

---

## 1. 방법론

이번 감사는 공개 웹 표면에서 확인 가능한 자료를 기준으로 진행했습니다.

평가 범위:

1. **AI 크롤러 접근성** — robots.txt 기준으로 GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-SearchBot, PerplexityBot, Google-Extended, Bingbot 등 확인.
2. **AI 인용 가능성** — AI가 직접 답변으로 사용할 수 있는 정의, 설명, FAQ, 제품 정보, 신뢰 신호 확인.
3. **콘텐츠 품질/E-E-A-T** — 회사 정보, 저자/조직 정보, 날짜, 상품 설명, 외부 신뢰 신호, 고객 보호 안내 확인.
4. **기술 SEO** — sitemap, robots, 공개 텍스트 추출성, 리다이렉트, JS 의존 가능성, 구조화 데이터 검증 필요성 확인.
5. **플랫폼 최적화** — ChatGPT Search, Perplexity, Claude Search, Gemini/Google, Bing/Copilot, Grok 관점으로 해석.

종합 점수는 다음 가중치를 사용했습니다.

```txt
GEO 점수 =
  AI 인용 가능성 × 0.25
+ AI 크롤러 접근 × 0.20
+ 콘텐츠 품질 × 0.20
+ 기술 SEO × 0.15
+ 구조화 데이터 × 0.10
+ 플랫폼 최적화 × 0.10
```

---

## 2. 등급 기준

| 점수 | 등급 | 의미 |
|---:|---|---|
| 80–100 | 우수 | AI 검색 최적화 상위 수준 |
| 60–79 | 양호 | 기본 최적화 완료, 일부 개선 필요 |
| 40–59 | 보통 | 주요 개선 과제 다수 존재 |
| 20–39 | 미흡 | 즉각 조치 필요 |
| 0–19 | 위험 | AI 검색에서 거의 노출되기 어려움 |

---

## 3. 한계

이번 리포트는 “공개 접근 가능한 표면” 기준의 심층 감사입니다. 다음은 별도 실측이 필요합니다.

- 실제 ChatGPT Search, Perplexity, Gemini, Copilot, Grok에서의 질의별 인용 여부
- 서버 로그 기준 AI crawler 실제 방문 여부
- WAF/CDN/IP allowlist에 따른 봇 접근 차단 여부
- Core Web Vitals 실측값
- HTML 원문 전체의 JSON-LD 스키마 블록 검증
- 대규모 상품/카테고리 URL 샘플링
- 가격/재고 변동 데이터가 AI에 노출되는 정책 리스크

---

## 4. 근거 URL 목록

### 대상 사이트

- https://www.coupang.com/
- https://www.coupang.com/robots.txt
- https://www.gmarket.co.kr/
- https://www.gmarket.co.kr/robots.txt
- https://www.musinsa.com/
- https://www.musinsa.com/robots.txt
- https://www.oliveyoung.co.kr/
- https://www.oliveyoung.co.kr/robots.txt

### 봇/검색 플랫폼 공식 문서

- OpenAI crawler documentation: https://developers.openai.com/api/docs/bots
- Perplexity crawler documentation: https://docs.perplexity.ai/docs/resources/perplexity-crawlers
- Perplexity robots.txt help: https://www.perplexity.ai/help-center/en/articles/10354969-how-does-perplexity-follow-robots-txt
- Google common crawlers and Google-Extended: https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers

---

## 5. 다음 정밀 감사 조건

정밀 감사를 “완성본”으로 올리려면 아래 데이터가 필요합니다.

1. 각 사이트별 핵심 URL 50~100개 목록
2. AI crawler별 실제 HTTP status 테스트 결과
3. sitemap 전체 파싱 결과
4. JSON-LD schema 추출 결과
5. ChatGPT Search/Perplexity/Gemini/Copilot/Grok 질의 결과 캡처
6. 서버 로그 또는 WAF 로그에서 AI 봇 방문 확인

