# Olive Young GEO-SEO 개별 감사 보고서

대상: https://www.oliveyoung.co.kr/
분석일: 2026-05-12 KST
상태: 미흡
GEO 점수: 26 / 100

## 1. 측정된 사실

| 항목 | 결과 |
|---|---|
| Homepage HEAD | HTTP/2 403 |
| Edge/WAF | Cloudflare |
| Challenge signal | `cf-mitigated: challenge` |
| Homepage body | `잠시만 기다려 주세요 - 올리브영` challenge page |
| `/robots.txt` | Cloudflare challenge HTML 반환 |
| `/llms.txt` | HTTP/2 403 challenge |
| 콘텐츠/메타 태그 측정 | 차단으로 미측정 |

## 2. 해석

올리브영은 자동화 요청에 대해 사용자 친화적인 한국어 challenge page를 반환하지만, GEO 관점에서는 실제 사이트 콘텐츠 대신 보안 확인 페이지가 노출된다. AI 검색/크롤러가 대표 URL, robots.txt, llms.txt를 안정적으로 읽을 수 없으면 브랜드/상품/카테고리 지식이 AI 답변에 반영될 가능성이 낮아진다.

이 상태에서 콘텐츠 품질이나 schema 품질을 단정할 수 없다. 먼저 crawler 정책 표면을 안정화한 뒤 실제 페이지 구조를 재감사해야 한다.

## 3. 영역별 점수

| 영역 | 점수 | 근거 |
|---|---:|---|
| AI 크롤러 접근 | 10 | homepage/robots/llms 모두 Cloudflare challenge |
| AI 인용 가능성 | 18 | 대표 콘텐츠가 아니라 challenge page가 노출됨 |
| 콘텐츠 품질 | 42 | 콘텐츠 미측정. 브랜드 규모 기본값만 반영 |
| 기술 SEO | 30 | HTTPS/WAF는 있으나 crawler 정책 표면이 차단됨 |
| 스키마 | 20 | HTML 접근 차단으로 확인 불가 |
| 플랫폼 최적화 | 30 | verified bot/AI bot 정책 분리 필요 |

## 4. 우선 조치

| 심각도 | 조치 | 담당 |
|---|---|---|
| CRITICAL | `/robots.txt`를 challenge 없이 제공하도록 Cloudflare rule 분리 | 인프라/보안 |
| CRITICAL | verified search bot과 AI crawler에 대한 allowlist/managed challenge 예외 정책 설계 | 인프라/SEO |
| HIGH | `/llms.txt` 제공 여부 결정 및 배포 | SEO/콘텐츠 |
| HIGH | 브랜드/카테고리 설명 페이지를 AI 인용 가능한 정적 본문으로 보강 | 콘텐츠/개발 |
| MEDIUM | 차단 해제 후 schema, canonical, sitemap, product listing 구조 재감사 | 개발/SEO |

## 5. 재감사 조건

- `https://www.oliveyoung.co.kr/robots.txt`가 challenge 없이 robots text로 응답
- homepage 또는 canonical landing page가 crawler 정책상 200 응답
- `/llms.txt`의 200 또는 의도된 404 정책 확정
