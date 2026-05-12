# Musinsa GEO-SEO 개별 감사 보고서

대상: https://www.musinsa.com/
분석일: 2026-05-12 KST
상태: 양호
GEO 점수: 78 / 100

## 1. 측정된 사실

| 항목 | 결과 |
|---|---|
| Homepage | `/`가 `/main/musinsa/recommend`로 308 redirect 후 HTTP/2 200 |
| HTML lang | `ko` |
| Title | `무신사` |
| Meta description | `패션의 모든 것, 다 무신사랑 해! ...` |
| Canonical | `https://www.musinsa.com/main/musinsa/recommend` |
| hreflang | `ko-KR`, `en-*`, `ja-JP`, `zh-TW`, `vi-VN` 등 다국어/지역 alternate 확인 |
| robots.txt | HTTP 200 plain text로 확인 |
| AI/search crawler policy | Applebot, OAI-SearchBot, ChatGPT-User, Claude-User, Claude-SearchBot, Perplexity-User 전면 허용. Googlebot/Yeti/Bing/GPTBot/ClaudeBot/PerplexityBot 등은 일부 path 제외 후 허용 |
| Sitemap | `https://www.musinsa.com/sitemap-musinsa-index.xml` 명시 |
| `/llms.txt` | HTTP/2 404 |

## 2. 해석

무신사는 4개 사이트 중 GEO 준비도가 가장 높다. robots.txt가 AI/search crawler를 그룹별로 분리해 명시하고, OAI-SearchBot, ChatGPT-User, Claude 계열, Perplexity 계열을 실제 이름으로 다룬다. 이는 AI 검색 노출을 의도적으로 관리하고 있다는 강한 신호다.

HTML에서도 canonical, meta description, hreflang이 확인되어 다국어 GEO의 기본 토대가 있다. 다만 `/llms.txt`는 404이며, 홈페이지 본문은 Next.js shell 형태로 얇게 보인다. AI 인용 가능성을 높이려면 브랜드/카테고리/정책 설명을 crawler가 쉽게 읽는 정적 설명 표면으로 강화하는 것이 좋다.

## 3. 영역별 점수

| 영역 | 점수 | 근거 |
|---|---:|---|
| AI 크롤러 접근 | 92 | robots.txt에서 주요 AI/search crawler를 명시 허용 |
| AI 인용 가능성 | 72 | meta/canonical/hreflang은 좋으나 homepage 본문 밀도는 낮음 |
| 콘텐츠 품질 | 70 | 대표 설명은 있으나 AI가 인용할 긴 설명/FAQ 표면은 추가 필요 |
| 기술 SEO | 84 | canonical, hreflang, sitemap, HTTPS 확인 |
| 스키마 | 60 | 이번 표면에서 JSON-LD 확인은 제한적. 별도 schema 감사 필요 |
| 플랫폼 최적화 | 88 | OpenAI/Claude/Perplexity/Google/Naver 계열 정책 분리 우수 |

## 4. 우선 조치

| 심각도 | 조치 | 담당 |
|---|---|---|
| HIGH | `/llms.txt`를 신설해 브랜드 설명, 주요 카테고리, 글로벌 사이트, sitemap, 정책 페이지를 명시 | SEO/개발 |
| MEDIUM | homepage 또는 canonical landing에 AI가 인용할 수 있는 정적 브랜드/카테고리 설명 블록 추가 | 콘텐츠/개발 |
| MEDIUM | Organization, WebSite, BreadcrumbList, ItemList/Product schema 재점검 | 개발/SEO |
| MEDIUM | hreflang cluster의 reciprocal linkage와 x-default 정책 검증 | 글로벌/SEO |
| LOW | robots.txt의 fully granted/partially granted 그룹을 정기적으로 versioning | SEO/인프라 |

## 5. 권장 `/llms.txt` 초안 구조

```text
# Musinsa

## About
Musinsa is a Korean fashion commerce platform...

## Key URLs
- Main: https://www.musinsa.com/main/musinsa/recommend
- Sitemap: https://www.musinsa.com/sitemap-musinsa-index.xml
- Global: https://global.musinsa.com/

## Allowed use
Summaries and search-grounded answers may cite public product, brand, category, and editorial pages according to robots.txt.
```

## 6. 재감사 조건

- `/llms.txt` 200 배포 후 AI crawler fetch 확인
- JSON-LD schema 별도 추출
- 주요 카테고리/브랜드 페이지 10개 샘플 인용 가능성 측정
