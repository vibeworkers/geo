# GEO Benchmark Evidence Pack: haegyung.com main vs beta

Date: `2026-05-08`

This directory preserves the Korean benchmark report and source metrics for the
`main` vs `beta` GEO readiness comparison against `https://haegyung.com`.

## Main Report

- `GEO-benchmark-report-main-vs-beta.ko.md`
- `benchmark-process-remediation-checklist.ko.md`
- `benchmark-process-builder-replay-20260509.ko.md`
- `haegyung-observed-outcome-baseline.ko.md`
- `observed-outcomes/README.md`
- `run-manifest.json`
- `run-manifest.template.json`

## Source Metrics

- `data/comparison.json`: branch readiness, HTTP/head/structure snapshot, and
  validator timing
- `data/branch-readiness.json`: audit split view of the branch-readiness lane
- `data/site-http-head-snapshot.json`: audit split view of the live site
  snapshot lane
- `data/browser-performance.json`: desktop and mobile browser probe timings
- `run-manifest.json`: retrofilled provisional provenance manifest for this
  preserved benchmark pack
- `run-manifest.template.json`: next-run provenance template for benchmark
  reproduction
- `all-function-benchmarks/benchmark-index.json`: 14-function GEO benchmark
  index
- `all-function-benchmarks/GEO-all-functions-benchmark-comparison.md`: Korean
  all-function comparison summary
- `all-function-benchmarks/reports/*.benchmark.md`: per-function benchmark
  reports
- `per-target-reports/*.md`: per-target branch reports

## Versioning Note

The report is a readiness benchmark artifact. It does not claim observed AI
answer visibility, observed citation inclusion, referral traffic, conversion,
or official Core Web Vitals results.

Large full-page visual captures from the temporary run were intentionally not
committed to keep the portable skill package lightweight. The preserved JSON
and Markdown files contain the measured values used by the report.

## Process Audit Note

See `benchmark-process-remediation-checklist.ko.md` for the benchmark-process
review, immediate remediation applied to this preserved evidence pack, and the
required controls for the next run.

The audit split views can be regenerated from `data/comparison.json` with
`python3 scripts/derive_benchmark_audit_views.py`.

The canonical benchmark-pack replay command is
`python3 scripts/rebuild_geo_benchmark_pack.py reports/benchmarks/2026-05-08-haegyung-main-vs-beta --output-dir <target-dir>`.
See `benchmark-process-builder-replay-20260509.ko.md` for the actual replay
evidence and the before vs to be table.

See `haegyung-observed-outcome-baseline.ko.md` for the follow-up measurement
lane boundary. It keeps the current `beta 100/100` result scoped to readiness
until observed answer or citation captures exist.

The first observed-outcome scaffold lives under `observed-outcomes/`. It stores
the prompt panel, pending named-platform capture matrix, and public search
precheck evidence without upgrading the report to observed visibility.
