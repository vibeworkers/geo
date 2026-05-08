# GEO Benchmark Evidence Pack: haegyung.com main vs beta

Date: `2026-05-08`

This directory preserves the Korean benchmark report and source metrics for the
`main` vs `beta` GEO readiness comparison against `https://haegyung.com`.

## Main Report

- `GEO-benchmark-report-main-vs-beta.ko.md`

## Source Metrics

- `data/comparison.json`: branch readiness, HTTP/head/structure snapshot, and
  validator timing
- `data/browser-performance.json`: desktop and mobile browser probe timings
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
