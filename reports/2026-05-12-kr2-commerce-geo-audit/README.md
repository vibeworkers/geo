# KR2 Commerce GEO Audit Summary

분석일: 2026-05-12 KST

분석 대상:

- https://www.coupang.com/
- https://www.gmarket.co.kr/
- https://www.musinsa.com/
- https://www.oliveyoung.co.kr/

## 적용한 스킬 기준

- Runtime skill: `geo-seo-skills-kr2`
- 실행 경로: `/geo audit` + `/geo report`
- 출력 레벨: L2/L3 혼합. 의사결정 요약은 L2, 기술 근거와 조치 항목은 L3 기준.
- 출력 언어: `ko`

## 증거 경계

이번 감사는 외부에서 비로그인 자동화 요청으로 확인 가능한 공개 표면만 측정했다. 쿠팡, 지마켓, 올리브영은 자동화 요청에 403 또는 Cloudflare/Akamai challenge를 반환했으므로, 본문 콘텐츠 품질, 내부 링크, 구조화 데이터의 실제 품질은 미측정으로 남긴다. 이 경우 점수는 “AI/검색/크롤러가 공개 표면을 안정적으로 읽을 수 있는가”에 보수적으로 반영했다.

## 기준 근거

- OpenAI crawler/user-agent guidance: https://platform.openai.com/docs/bots
- Anthropic crawler guidance: https://support.claude.com/en/articles/8896518-what-is-claudebot
- Perplexity robots.txt guidance: https://www.perplexity.ai/help-center/en/articles/10354969-how-does-perplexity-follow-robots-txt
- Google robots.txt interpretation: https://developers.google.com/search/reference/robots_txt
- Google crawler tokens including Google-Extended: https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers

## 종합 순위

| 순위 | 사이트 | GEO 상태 | 점수 | 핵심 판단 |
|---:|---|---|---:|---|
| 1 | Musinsa | 양호 | 78 | robots.txt가 주요 AI/search crawler를 명시 허용하고, hreflang/canonical/meta/sitemap 신호가 확인됨. llms.txt 부재가 주요 개선점. |
| 2 | Olive Young | 미흡 | 26 | Cloudflare challenge로 홈페이지, robots.txt, llms.txt 모두 자동화 접근이 차단됨. 실제 사용자 UX와 별개로 AI 크롤러 가시성 리스크가 큼. |
| 3 | Gmarket | 미흡 | 24 | Cloudflare managed challenge가 홈페이지/robots/llms 표면에 노출됨. challenge HTML은 noindex/nofollow라 진단 표면 자체가 불안정. |
| 4 | Coupang | 미흡 | 22 | Akamai Access Denied가 홈페이지/robots/llms 요청에 반환됨. 공개 크롤러 접근성 관점에서 가장 높은 리스크. |

## 공통 우선순위

| 우선순위 | 조치 | 대상 |
|---|---|---|
| CRITICAL | AI/search crawler가 `robots.txt`, homepage, canonical landing page를 challenge 없이 읽을 수 있는 allowlist 또는 bot policy 분리 | Coupang, Gmarket, Olive Young |
| HIGH | `/llms.txt` 제공 또는 명시적 미제공 정책 수립 | 4개 전체 |
| HIGH | AI crawler별 정책을 `robots.txt`에 명시: OAI-SearchBot, ChatGPT-User, GPTBot, Claude-SearchBot, Claude-User, ClaudeBot, PerplexityBot, Googlebot, Google-Extended, Yeti | 특히 Coupang, Gmarket, Olive Young |
| MEDIUM | Organization/WebSite/Breadcrumb/Product schema 품질 점검 | 4개 전체 |
| MEDIUM | 브랜드/카테고리 설명 페이지를 AI 인용 가능한 정적 본문으로 강화 | 4개 전체 |

## 파일 목록

- `coupang.md`
- `gmarket.md`
- `musinsa.md`
- `oliveyoung.md`
