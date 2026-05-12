# 2026-05-12 Commerce GEO Audit

이 폴더는 `main` 브랜치 기준으로 수행한 네 개 한국 커머스 사이트의 GEO 감사 산출물이다.

## Targets

- `https://www.coupang.com/`
- `https://www.gmarket.co.kr/`
- `https://www.musinsa.com/`
- `https://www.oliveyoung.co.kr/`

## Artifacts

| 파일 | 역할 |
|---|---|
| `GEO-종합보고서.md` | 네 사이트 비교, 공통 우선순위, 측정 경계 |
| `coupang.GEO-감사-보고서.md` | 쿠팡 개별 감사 |
| `gmarket.GEO-감사-보고서.md` | G마켓 개별 감사 |
| `musinsa.GEO-감사-보고서.md` | 무신사 개별 감사 |
| `oliveyoung.GEO-감사-보고서.md` | 올리브영 개별 감사 |
| `evidence/*.json` | 공개 HTTP 수집 원자료 |

## Boundary

이 감사는 `readiness_signal + heuristic_signal` 기준이다. 실제 AI 답변, citation, referral, conversion은 측정하지 않았다.

로그인, 앱, 내부 feed, 광고/검색 콘솔, 서버 로그, 주문·전환 데이터는 사용하지 않았다.
