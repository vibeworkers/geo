# GEO Benchmark Builder Replay Report

생성일: `2026-05-09`

## 목적

`2026-05-08-haegyung-main-vs-beta` 보존본에 대해 canonical builder를 실제로
실행하고, fresh output dir 기준으로 report/data/provenance surface가 재현되는지
검증한다.

## 실제 실행 명령

```bash
python3 scripts/rebuild_geo_benchmark_pack.py \
  reports/benchmarks/2026-05-08-haegyung-main-vs-beta \
  --output-dir /private/var/folders/mx/qvzhz0111sj2797v5xbm8n1w0000gn/T/tmp.gKQxf4n3Hk
```

```bash
python3 - <<'PY' /private/var/folders/mx/qvzhz0111sj2797v5xbm8n1w0000gn/T/tmp.gKQxf4n3Hk
from pathlib import Path
import filecmp, sys
base=Path('reports/benchmarks/2026-05-08-haegyung-main-vs-beta')
out=Path(sys.argv[1])
files=[
  'run-manifest.template.json',
  'run-manifest.json',
  'data/comparison.json',
  'data/branch-readiness.json',
  'data/site-http-head-snapshot.json',
  'data/browser-performance.json',
  'all-function-benchmarks/benchmark-index.json',
  'all-function-benchmarks/GEO-all-functions-benchmark-comparison.md',
  'per-target-reports/00-branch-comparison.GEO-비교보고서.md',
  'per-target-reports/01-main-clean-baseline.GEO-종합보고서.md',
  'per-target-reports/02-beta.GEO-종합보고서.md',
  'GEO-benchmark-report-main-vs-beta.ko.md',
]
for p in sorted((base/'all-function-benchmarks/reports').glob('*.benchmark.md')):
    files.append(str(p.relative_to(base)))
mismatches=[]
missing=[]
for rel in files:
    lhs=base/rel
    rhs=out/rel
    if not rhs.exists():
        missing.append(rel)
        continue
    if not filecmp.cmp(lhs, rhs, shallow=False):
        mismatches.append(rel)
print('checked_files=', len(files))
print('missing_files=', len(missing))
print('mismatch_count=', len(mismatches))
PY
```

## 실행 결과 요약

- builder 실행: `exit=0`
- checked files: `26`
- missing files: `0`
- mismatch count: `0`
- JSON parse: `json-ok 6`
- `git diff --check`: pass

## Before vs To Be

| 항목 | Before | 실제 실행 결과 | To Be |
| --- | --- | --- | --- |
| canonical builder 존재 | `derive_benchmark_audit_views.py`만 있어 split JSON 재생성만 가능 | `scripts/rebuild_geo_benchmark_pack.py`가 fresh output dir에 full benchmark report/data surface를 재생성 | 이후 같은 benchmark pack은 builder 1개로 replay |
| fresh output dir replay | report markdown만 부분 생성되고 source/provenance artifact는 누락 | `data/comparison.json`, `data/browser-performance.json`, `run-manifest.json`, `run-manifest.template.json`까지 함께 복사/재생성 | 감사자는 output dir 하나만 열어도 근거 경로를 따라갈 수 있음 |
| preserved artifact exact replay | criteria/order/rounding 차이로 exact match 불가 | checked files `26`, missing `0`, mismatch `0` | historical pack replay는 exact-match 기준으로 유지 |
| branch/site/order methodology | 일부 report는 split view와 combined artifact ordering이 엇갈려 builder로는 보존본을 그대로 만들 수 없었음 | branch report order, top-level order, per-skill criteria/new reference order를 historical methodology로 고정 | future drift가 생기면 preserved methodology delta를 명시적으로 버전업 |
| output contract reconstruction | multi-output skill의 contract가 첫 번째 markdown token만 잡혀 과소복원 | `geo-prospect`, `geo-report`, `geo-report-pdf`는 preserved output contract를 exact replay | 다중 산출물 skill은 builder spec에 contract rule을 유지 |
| process discoverability | README와 remediation note에서 full-pack replay 경로가 바로 보이지 않음 | root README와 remediation checklist에 canonical builder command를 연결 | 다음 운영자는 문서 entrypoint에서 바로 재생성 가능 |

## 남은 한계

- 이 builder는 **보존본 replay** 도구다. 즉 `2026-05-08` 산출물을 historical
  methodology 그대로 재현한다.
- 따라서 measured target과 reported target 사이의 historical normalization
  note 자체를 제거하지는 않는다. 그 한계는 `run-manifest.json`과 process
  remediation note에 그대로 남겨둔다.
- 새 benchmark date를 생성하는 범용 pipeline은 아직 별도 설계가 필요하다.

## 판정

canonical builder gap은 이번 실행으로 닫혔다. 현재 benchmark pack은 split audit
view 재생성뿐 아니라, fresh output dir 기준 report/data/provenance surface를
exact replay 가능한 상태다.
