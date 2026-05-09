# GEO Branch Performance Report Set

생성일: `2026-05-08`

## 산출물

| 파일 | 역할 |
| --- | --- |
| `01-main-clean-baseline.GEO-종합보고서.md` | clean `main` 기준 단독 리포트 |
| `02-beta.GEO-종합보고서.md` | `beta@2d896ac` 기준 단독 리포트 |
| `00-branch-comparison.GEO-비교보고서.md` | 두 단독 리포트를 기준으로 한 비교 리포트 |

## 근거 파일

- `data/branch-readiness.json`
- `data/site-http-head-snapshot.json`
- `data/browser-performance.json`
- `data/comparison.json` (원본 combined artifact)

임시 실행에서 생성된 대형 screenshot capture는 versioned evidence pack에
포함하지 않았다. 현재 보존본에서는 JSON/Markdown에 남긴 수치와 해석만 공식
근거로 사용한다.

## 비교 범위

이 산출물은 clean `main@a652637`과 `beta@2d896ac` surface 비교입니다. 초기 probe는 beta commit 직전에 수행됐고, 같은 GEO readiness surface가 `beta@2d896ac`로 고정됐습니다.
