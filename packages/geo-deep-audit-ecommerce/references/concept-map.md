# GEO Deep Audit Ecommerce Concept Map

## Scope

This map routes the captured ecommerce GEO audit pack from immutable raw source
to reusable outputs.

## Paths

- User asks ranking -> read `raw/audit_scorecard.csv` -> summarize overall,
  grade, top issue, and top action -> output scorecard view.
- User asks site comparison -> read `raw/audit_scorecard.csv` plus matching
  site reports -> separate numeric score from qualitative evidence -> output
  comparison.
- User asks crawler policy -> read `raw/05_Crawler_Access_Matrix.md` and the
  relevant site report -> label as captured audit finding unless refreshed
  live.
- User asks roadmap -> read `raw/06_Roadmap_and_Priorities.md` plus the
  executive summary -> produce phased action plan.
- User asks confidence or "did it work" -> read
  `raw/07_Methodology_Limitations.md` -> separate readiness from observed
  answer, observed citation, referral, and conversion evidence.
- User asks for a new live audit -> use this package as historical baseline ->
  require fresh current evidence before updating claims.

## Package Boundary

`SKILL.md` owns trigger, workflow, gates, and final checks.
`references/` owns terminology and confidence boundaries.
`scripts/` owns deterministic parsing of packaged data.
`raw/` owns copied evidence and must not be edited.
`agents/openai.yaml` is the OpenAI/Codex local compatibility adapter.
