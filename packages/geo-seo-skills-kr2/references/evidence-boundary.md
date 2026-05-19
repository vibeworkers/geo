# Evidence Boundary

This package separates four evidence states. Internal package tables may route
work and organize judgment, but they do not count as the evidence basis for a
claim unless they point to external standards, official documentation, academic
literature, technical reports, or clearly labelled local-market sources in
`source-index.md`.

## External Evidence Rule

Treat external, technically defensible evidence as the foundation:

- Standards and protocols: normative engineering basis.
- Official platform documentation: crawler identity, product behavior, and
  webmaster controls.
- Academic or empirical technical studies: mechanism, limitation, and
  measurement design.
- Expert technical reports: secondary interpretation only.
- Korean/local sources: local context or implementation reference unless the
  claim is specifically about a Korean institution, Korean product, or Korean
  market behavior.

## Measured

Use only when the workflow captured platform output, citation URLs, logs,
referrals, conversion data, or another directly observed result.

## Readiness

Use when the workflow verified crawler access, schema, metadata, hreflang,
`llms.txt`, sitemap, page structure, or similar setup signals.

## Heuristic

Use when the workflow infers likely AI usefulness from content quality,
authority signals, answer structure, or platform expectations without direct
measurement. Heuristic scores are decision aids, not measured AI visibility.

## Manual Fallback

Use when the runtime cannot execute a required local or browser-based check and
the user must perform the check outside the package.

Do not upgrade readiness or heuristic evidence into measured visibility.

## Required Output Labels

Every audit or report must identify which findings are `Measured`, `Readiness`,
`Heuristic`, or `Manual Fallback`. If the runtime cannot capture direct
platform output, the report must say so instead of implying AI citation,
ranking, or visibility was measured.
