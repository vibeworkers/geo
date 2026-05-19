# beta 유기적 통합 설계

검토 기준일: 2026-05-13 KST

## 결론

`beta`는 `beta-A`와 `beta-B`를 개별 패키지로 병렬 배치한 브랜치가 아니다.
`geo` 하나의 실행 시스템 안에서 `beta-A`의 운영 계약과 `beta-B`의 KR2 실행
능력을 결합한 통합 브랜치다.

## 의미 구조

```text
geo
  core operating contract
    source priority
    context mode
    routing
    sequence-dependent autopilot
    evidence ledger
    report contract

  capability: deep-audit-ecommerce
    ecommerce / commerce readiness
    product, schema, merchant, catalog, checkout/action, measurement 판단

  capability: kr2
    Korean / multilingual / platform / crawler / AI readiness
    realtime, tracker, batch, geo-code 확장
```

물리 폴더는 유지보수 경계다. 사용자 경험과 실행 판단에서는 하나의 `geo`
시스템으로 동작해야 한다.

## 통합 규칙

- root `SKILL.md`는 대표 surface로 남는다.
- `beta-A`는 별도 기능이 아니라 `geo` 전체의 실행 엔진이다.
- `beta-B`는 별도 제품이 아니라 `geo` 안의 KR2 판단 능력이다.
- `deep-audit-ecommerce`는 `geo` 안의 commerce 도메인 판단 능력이다.
- 통합이 우선이다. deep-audit 보고서와 KR2 보고서를 각각 보존하는 것은
  필수 조건이 아니며, 단일 판단에 필요한 근거만 통합 흐름으로 흡수한다.
- 같은 요청 안에서 deep-audit과 KR2가 모두 필요하면 하나의 evidence ledger와
  하나의 report contract를 사용한다.
- KR2가 ecommerce 사이트를 다룰 때는 deep-audit commerce rubric을 불러온다.
- ecommerce audit이 한국어, 다국어, 플랫폼, crawler, realtime, tracking 문제를
  다룰 때는 KR2 evidence boundary와 source index를 불러온다.
- `Measured`는 직접 관측값이 있을 때만 허용한다.
- `Readiness`와 `Heuristic`은 실제 AI 노출, 인용, 순위 상승으로 승격하지 않는다.

## beta 성공 기준

- 기존 `main`의 deep-audit-ecommerce 효과가 통합 workflow 안에서 호출된다.
- `beta-A`의 sequence-dependent autopilot, completion gate, CogArch-compatible
  reasoning contract가 통합 판단의 실행 엔진으로 작동한다.
- `beta-B`의 KR2 package, 21개 subskill, source index, function matrix, evidence
  checker가 통합 판단의 근거와 실행 능력으로 작동한다.
- 두 capability가 별도 closeout을 만들지 않고 하나의 `geo` 판단 흐름으로 닫힌다.
- `cogarch`는 alignment reference일 뿐 portable 실행 필수조건이 아니다.
