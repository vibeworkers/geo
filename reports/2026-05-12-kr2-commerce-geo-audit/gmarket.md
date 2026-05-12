# Gmarket GEO-SEO 개별 감사 보고서

대상: https://www.gmarket.co.kr/
분석일: 2026-05-12 KST
상태: 미흡
GEO 점수: 24 / 100

## 1. 측정된 사실

| 항목 | 결과 |
|---|---|
| Homepage HEAD | HTTP/2 403 |
| Edge/WAF | Cloudflare |
| Challenge signal | `cf-mitigated: challenge` |
| Homepage body | Cloudflare `Just a moment...` page |
| Challenge meta | `robots` = `noindex,nofollow` on challenge page |
| `/robots.txt` | Cloudflare challenge HTML 반환 |
| `/llms.txt` | HTTP/2 403 challenge |
| 콘텐츠/메타 태그 측정 | 차단으로 미측정 |

## 2. 해석

지마켓은 Cloudflare challenge가 robots.txt와 llms.txt에도 노출된다. 특히 challenge HTML에 `noindex,nofollow`가 포함되어 있어, 검색/AI crawler가 challenge 표면만 보게 되면 실제 사이트가 아니라 차단 페이지를 해석할 위험이 있다.

이 문제는 “콘텐츠가 나쁘다”는 결론이 아니라 “공개 기계 접근 표면이 불안정하다”는 결론이다. GEO에서는 모델이 사이트를 직접 읽거나 검색 색인을 통해 참조할 수 있어야 하는데, 현재 관측값은 첫 관문에서 막힌다.

## 3. 영역별 점수

| 영역 | 점수 | 근거 |
|---|---:|---|
| AI 크롤러 접근 | 8 | homepage/robots/llms 모두 Cloudflare challenge |
| AI 인용 가능성 | 15 | 실제 본문 대신 challenge page가 노출됨 |
| 콘텐츠 품질 | 40 | 콘텐츠 미측정. 대형 커머스 기본값만 반영 |
| 기술 SEO | 25 | HTTPS/WAF는 있으나 crawler 정책 표면이 challenge 처리됨 |
| 스키마 | 20 | HTML 접근 차단으로 확인 불가 |
| 플랫폼 최적화 | 25 | Cloudflare bot policy 분리가 필요 |

## 4. 우선 조치

| 심각도 | 조치 | 담당 |
|---|---|---|
| CRITICAL | `/robots.txt`와 주요 landing page를 Cloudflare managed challenge 대상에서 제외하거나 verified bot 정책으로 분리 | 인프라/보안 |
| CRITICAL | challenge HTML이 검색/AI crawler의 대표 응답이 되지 않도록 bot allowlist 테스트 | 인프라/SEO |
| HIGH | AI crawler user-agent별 allow/disallow 정책을 robots.txt에 명시 | SEO |
| HIGH | `/llms.txt` 신설 또는 정책적 404 확정 | SEO/콘텐츠 |
| MEDIUM | 차단 해제 후 title/meta/canonical/schema/product listing 구조 재감사 | 개발/SEO |

## 5. 재감사 조건

- `https://www.gmarket.co.kr/robots.txt`가 challenge 없이 robots text로 응답
- homepage가 crawler 정책상 200 또는 canonical redirect 반환
- Cloudflare bot rules에서 Googlebot/Yeti/OAI-SearchBot/Claude/Perplexity 계열 동작이 분리 검증됨
