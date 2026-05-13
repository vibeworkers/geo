# 4개 커머스 사이트 GEO 개별 감사 요약

- 감사일: 2026-05-12
- 대상: Coupang, Gmarket, Musinsa, Olive Young
- 범위: 홈페이지 초기 HTML, robots.txt, sitemap.xml, llms.txt, 기본 메타/구조화 데이터 신호
- 근거 경계: 이 감사는 `Measured AI visibility`가 아니라, 접근 가능한 공개 신호에
  기반한 `Readiness + Heuristic` 감사이다. 실제 ChatGPT·Claude·Perplexity·Gemini·
  NAVER AI 인용 여부는 별도 `/geo realtime` 또는 플랫폼 출력 캡처가 있어야
  `Measured`로 승격된다.

| 사이트 | GEO 준비도 점수 | 개별 리포트 |
|---|---:|---|
| Coupang | 0/100 | `coupang.GEO-audit-report.md` |
| Gmarket | 0/100 | `gmarket.GEO-audit-report.md` |
| Musinsa | 86/100 | `musinsa.GEO-audit-report.md` |
| Olive Young | 29/100 | `oliveyoung.GEO-audit-report.md` |

## 공통 우선순위

1. `llms.txt` 또는 AI crawler guidance의 도입 여부를 명확히 결정한다.
2. Sitemap, canonical, structured data를 초기 접근 가능한 형태로 정렬한다.
3. 브랜드와 카테고리 단위의 인용 가능한 요약 페이지를 강화한다.
4. AI bot 접근 정책을 robots.txt에서 의도적으로 관리한다.

## Evidence-state 분리

| Evidence state | 이번 감사에서의 의미 |
|---|---|
| Measured | 이번 요약에는 직접 AI 플랫폼 출력, citation URL, referral log가 포함되지 않음 |
| Readiness | 홈페이지 HTML, robots.txt, sitemap.xml, llms.txt, metadata, structured data 접근성 |
| Heuristic | 콘텐츠/브랜드/카테고리 페이지가 AI 답변에 쓰이기 쉬운 구조인지에 대한 공학적 판단 |
| Manual fallback | 로그인, 차단, 봇 방어, 런타임 제한으로 직접 확인이 필요한 항목 |

점수는 `heuristic readiness score`이며, 실제 AI 노출률·인용률·랭킹을 의미하지 않는다.
