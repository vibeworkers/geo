# AI Crawler Access Matrix

**분석일:** 2026-05-11  
**범위:** 공개 robots.txt 기준. 실제 접근은 WAF, IP allowlist, CDN, JS rendering, HTTP status에 따라 달라질 수 있음.

---

## 1. 봇별 접근성 요약

| Bot / Token | 용도 | Coupang | Gmarket | Musinsa | Olive Young |
|---|---|---|---|---|---|
| Googlebot | Google Search/AI Overviews 기반 | 부분 허용 | `/n`, `/e` 허용 | 부분 허용 | 경로 제한 허용 |
| Bingbot | Bing/Copilot 기반 | 부분 허용 | `/n`, `/e` 허용 | 부분 허용 | 미명시 또는 간접 확인 필요 |
| GPTBot | OpenAI training | 기본 차단 가능 | `/n`, `/e` 허용 | 부분 허용 | 경로 제한 허용 |
| OAI-SearchBot | ChatGPT Search | 기본 차단 가능 | 기본 차단 가능 | 완전 허용 | 경로 제한 허용 |
| ChatGPT-User | 사용자 요청 fetch | 기본 차단 가능 | 기본 차단 가능 | 완전 허용 | 미명시 또는 OAI 계열 별도 검토 필요 |
| ClaudeBot | Anthropic training | 기본 차단 가능 | 기본 차단 가능 | 부분 허용 | 경로 제한 허용 |
| Claude-SearchBot | Claude Search | 기본 차단 가능 | 기본 차단 가능 | 완전 허용 | 경로 제한 허용 |
| Claude-User | 사용자 요청 fetch | 기본 차단 가능 | 기본 차단 가능 | 완전 허용 | 미명시 |
| PerplexityBot | Perplexity search index | 기본 차단 가능 | 기본 차단 가능 | 부분 허용 | 경로 제한 허용 |
| Perplexity-User | 사용자 요청 fetch | 기본 차단 가능 | 기본 차단 가능 | 완전 허용 | 미명시 |
| Google-Extended | Gemini training/grounding control | 기본 차단 가능 | 기본 차단 가능 | 부분 허용 | 경로 제한 허용 |
| GrokBot/xAI-Grok/Grok-DeepSearch | Grok 계열 | 기본 차단 가능 | 기본 차단 가능 | 미명시/간접 | 미명시 |

---

## 2. 해석

### Coupang
전통 검색엔진은 세밀하게 열려 있지만, AI 전용 봇은 대부분 `User-agent: * Disallow: /`의 영향을 받을 가능성이 큽니다. ChatGPT Search와 Perplexity 같은 AI 검색 플랫폼에 공식 원문이 인용되는 길이 좁습니다.

### Gmarket
GPTBot을 일부 열었다는 점은 긍정적입니다. 그러나 OpenAI의 검색용 봇인 OAI-SearchBot과 Claude/Perplexity 검색용 봇이 보이지 않아 실시간 AI 검색 인용성은 약합니다.

### Musinsa
가장 선진적인 설계입니다. 검색용·사용자 요청형·학습형 봇을 구분하고, 민감 경로만 제외하는 구조입니다.

### Olive Young
AI 봇을 넓게 명시한 점은 강점입니다. 공개 상품/검색/기획전/회사 경로를 열고 거래·개인화 경로를 닫는 균형형 구조입니다.

---

## 3. 권장 robots 정책 패턴

```txt
# Search exposure bots — allow public content
User-agent: OAI-SearchBot
Allow: /products/
Allow: /categories/
Allow: /search/
Disallow: /cart/
Disallow: /mypage/
Disallow: /order/

User-agent: PerplexityBot
Allow: /products/
Allow: /categories/
Allow: /search/
Disallow: /cart/
Disallow: /mypage/
Disallow: /order/

User-agent: Claude-SearchBot
Allow: /products/
Allow: /categories/
Allow: /search/
Disallow: /cart/
Disallow: /mypage/
Disallow: /order/

# Training / grounding bots — choose business policy
User-agent: GPTBot
Allow: /public-content/
Disallow: /members-only/

User-agent: Google-Extended
Allow: /public-content/
Disallow: /members-only/
```

