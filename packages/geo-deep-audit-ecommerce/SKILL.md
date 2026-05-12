---
name: geo-deep-audit-ecommerce
description: >
  Use this skill when the user wants to reuse, inspect, extend, or turn the
  captured 2026-05-11 ecommerce GEO deep audit pack into evidence-grounded
  Korean deliverables, comparison tables, remediation roadmaps, scorecard
  summaries, or follow-up audit plans. The package preserves the raw Coupang,
  Gmarket, Musinsa, and Olive Young audit reports and separates observed
  public-surface evidence from hypotheses, recommendations, and future
  measurement requirements.
metadata:
  display-name: GEO Deep Audit Ecommerce
  short-description: Package ecommerce GEO audit evidence
---

# GEO Deep Audit Ecommerce

## Overview

This is a portable skill package for the ecommerce GEO deep audit evidence pack
captured on 2026-05-11. It turns the source reports into a repeatable workflow
for comparison, evidence review, executive summaries, roadmap extraction, and
follow-up measurement planning.

The raw source files under `raw/` are immutable evidence. Do not rewrite them.
Create derived summaries, tables, or recommendations from the copied raw files
and cite the exact source filename used.

## Working Source Of Truth

Primary working source:

- `raw/00_Executive_Summary.md`
- `raw/01_Coupang_Deep_GEO_Audit.md`
- `raw/02_Gmarket_Deep_GEO_Audit.md`
- `raw/03_Musinsa_Deep_GEO_Audit.md`
- `raw/04_OliveYoung_Deep_GEO_Audit.md`
- `raw/05_Crawler_Access_Matrix.md`
- `raw/06_Roadmap_and_Priorities.md`
- `raw/07_Methodology_Limitations.md`
- `raw/audit_scorecard.csv`

Project source of truth is the copied audit pack. Skill-packaging source of
truth is this `SKILL.md`, `references/`, `scripts/`, and `agents/openai.yaml`.

When future live checks are requested, use English-language primary sources
first for crawler, robots, search-platform, schema, and policy claims. Korean
web sources may support Korean market or local implementation context, but do
not treat Korean summaries as primary evidence when English official docs are
available.

## When To Use

Use this skill for:

- comparing Coupang, Gmarket, Musinsa, and Olive Young GEO readiness from the
  captured audit pack
- extracting scorecard summaries, rankings, top issues, or action priorities
- turning the audit into Korean executive reports, roadmap notes, or handoff
  checklists
- separating crawler access, citability, content quality, technical SEO,
  structured data, and platform optimization claims
- planning a follow-up audit that requires live evidence, server logs, crawler
  HTTP tests, schema extraction, or AI answer captures

Do not use this skill for:

- claiming current live GEO visibility without new observed-answer or referral
  evidence
- updating robots.txt, schema, or production site files directly
- treating the raw audit score as measured traffic, citation, referral, or
  conversion lift
- general ecommerce strategy unrelated to the captured GEO audit pack

## Workflow

1. **Classify the request**
   Entry: the user asks about this ecommerce audit pack or one of its target
   sites. Exit: choose one lane: `scorecard`, `site-report`, `crawler-matrix`,
   `roadmap`, `methodology`, or `follow-up-measurement`.

2. **Select the smallest source surface**
   Entry: the lane is known. Exit: read only the raw file(s) needed for the
   answer. Use `audit_scorecard.csv` for rankings and numeric comparisons;
   use site reports for site-specific reasoning; use methodology for evidence
   boundaries.

3. **Label evidence status**
   Entry: a claim is ready. Exit: label it as `captured audit finding`,
   `methodology assumption`, `recommendation`, or `requires live validation`.
   Do not collapse these labels.

4. **Generate the deliverable**
   Entry: the evidence labels are clear. Exit: produce the requested Korean
   output with concrete file references and no uncited upgrade in confidence.
   For scorecard-only work, prefer `scripts/summarize_scorecard.py`.

5. **Close with next action**
   Entry: the deliverable is complete. Exit: name the single next validation
   or implementation step, or state that no further action is required for the
   requested scope.

## Runtime Compatibility Gate

Closure status: `runtime-delta implemented`.

The shared portable core is in `SKILL.md`, `references/`, `scripts/`, and
`raw/`. The runtime-local artifact is `agents/openai.yaml`, which is treated as
this workspace's explicit OpenAI/Codex compatibility adapter. The package does
not require `cogarch`, hidden global paths, hidden session commands, external
credentials, or a live browser just to understand and use the captured audit
pack.

## Provider / Provenance vs Output Brand

Provider/provenance: user-provided ecommerce GEO deep audit evidence pack,
captured into this package as copied raw files.

Output brand: preserve the requested deliverable brand. If no brand is named,
produce neutral audit outputs. Do not rewrite the raw evidence into a
VibeWorkers-branded report unless the parent `geo` workflow or the user
explicitly asks for that output surface.

## Trigger Contract

Should trigger:

- "Summarize the 2026-05-11 ecommerce GEO audit ranking."
- "Compare Coupang and Musinsa from the deep audit pack."
- "Turn the ecommerce GEO audit into a remediation roadmap."
- "Which findings require live validation before we can claim improvement?"
- "Generate a Korean executive summary from the audit scorecard."

Should not trigger:

- "Crawl this unrelated URL and run a fresh GEO audit now."
- "Edit Coupang robots.txt in production."
- "Did our AI referral traffic increase after these changes?"
- "Make a generic ecommerce marketing plan with no reference to this audit."

With-skill expected behavior: preserve raw source files, use the smallest raw
source surface, label evidence confidence, and keep scorecard/readiness claims
separate from measured AI visibility or business outcomes.

## Code / LLM Boundary

Code-enforced:

- Parse `raw/audit_scorecard.csv` with `scripts/summarize_scorecard.py` for
  deterministic scorecard summaries.
- Do not mutate files under `raw/`.
- Do not infer live visibility, referrals, or conversions from readiness scores.

LLM-judged:

- Which raw file best answers the user's question.
- Whether a claim is a captured finding, a recommendation, or a live-validation
  requirement.
- How to phrase Korean deliverables naturally while preserving technical
  precision and evidence limits.

## Setup

No special bootstrap is required. The package is self-contained once this
directory is present in a supported skill root or repository checkout.

Optional scorecard summary:

```bash
python3 scripts/summarize_scorecard.py raw/audit_scorecard.csv
```

## Dependencies And Permissions

No external API credential is required.

The bundled script uses only Python 3 standard-library modules. Network access
is not required for packaged-source review. Network or browser access is only
needed for a new live follow-up audit and must be reported as a separate
validation step.

Write boundary: derived outputs may be written outside `raw/` when the user
asks for a report, roadmap, or follow-up artifact. The raw evidence files must
remain unchanged.

## Source And License Notes

This package is derived from the user-provided audit folder named
`geo_deep_audit_ecommerce_2026-05-11`.

The copied raw files are included for local workflow continuity and provenance.
They cite public site URLs and official crawler documentation inside
`raw/07_Methodology_Limitations.md`. The package itself does not grant rights
to republish third-party site content beyond the user's permitted workflow.

## References

- `references/glossary.md`: package-specific terminology.
- `references/concept-map.md`: source-to-output routing map.
- `references/evidence-boundary.md`: confidence labels and measurement limits.
- `references/source-index.md`: raw file inventory and use cases.

## Rubric

Must:

- preserve every file under `raw/` as immutable evidence
- cite the raw source filename for every site-specific or score-specific claim
- separate readiness, captured finding, recommendation, and live-validation
  requirements
- keep provider/provenance separate from output brand
- close Runtime Compatibility Gate as exactly `runtime-delta implemented`
- validate `agents/openai.yaml` and this `SKILL.md` with a skill validator
- run at least one deterministic scorecard test before declaring the package
  usable

Should:

- answer in Korean unless the user requests another language
- use natural Korean reconstruction rather than literal translation from source
  text
- prefer `audit_scorecard.csv` for ranking and numeric comparison
- use `07_Methodology_Limitations.md` before answering measurement or
  confidence questions
- use English primary/official sources first when future live verification is
  requested
