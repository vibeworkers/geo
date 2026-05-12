# GEO Execution Skill Matrix

This repository includes an optional local execution bundle under `skills/*`.

`SKILL.md` remains the representative `geo` router. Execution-intent requests
should route through the matching subskill only after `skills/*` is confirmed.
Each subskill below owns its own setup, permission, access-profile, and output
contract. A subskill must remain usable without `cogarch`, `~/.cogarch`,
`OPERATIONS.md`, or a hidden level session state.
Subskill examples should describe direct inputs or plain-language requests, not
a separate `/geo ...` slash-command surface.

## How to enable these workflows

Treat this section as the advanced-workflow setup guide.

Run this guide the first time an advanced workflow is requested in a local
environment.

Run the same guide again when the active runtime or model changes.

If your runtime can host native first-use onboarding, the same guide may
appear automatically there. Otherwise, follow these steps manually.

- Use a GEO checkout or installation that includes the local `skills/*` bundle.
- In this repository checkout, the bundle is already included under `skills/`.
- Start with the representative `geo` entrypoint, then ask for a concrete
  audit, crawler, `llms.txt`, schema, compare, report, proposal, prospect, or
  technical review task.
- If you already know the exact workflow owner, you can open that subskill
  directly and follow its local setup and output contract.
- If a workflow needs extra tools or export steps, read the matching subskill's
  `SKILL.md`.

## User-level output guide

Use `references/user-level-workflow-guide.md` when a workflow must adapt the
same finding for a manager, operator, or builder.

The guide preserves the earlier practical onboarding pattern:

- `L1` manager output uses business language and handoff notes for another
  team.
- `L2` operator output uses CMS, hosting, file, and verification steps.
- `L3` builder output uses code, schema, CLI checks, automation, and export
  commands.

The profile only changes explanation and action packaging. It must not reduce
analysis depth, bypass clarification-first intake, or turn readiness evidence
into a measured visibility claim.

## Troubleshooting

- If no advanced workflow is available, verify that `skills/*` is present in
  the same GEO installation or checkout.
- If you copied only the representative docs, reinstall from a GEO package that
  also includes `skills/*`.
- If you do not know which workflow owner to choose, start with `geo <request>`
  or `$geo <request>` and let the representative router select the matching
  subskill.
- If GEO asks clarification questions first, answer them before expecting an
  execution subskill to run.
- If you switched to a different runtime or model, rerun the setup guide
  before expecting the same workflow to continue with unchanged hints or
  permissions.
- If a subskill needs extra tools, network access, credentials, or export
  steps, open that subskill's `SKILL.md` and follow its local contract.
- If your runtime has no automatic setup-guide onboarding, use this matrix plus
  the matching subskill docs manually; advanced workflows do not depend on
  hidden global files or hidden session-state commands.

## Standalone execution subskills

| Skill | Primary use | Typical trigger | Local profile | Typical output |
| --- | --- | --- | --- | --- |
| `geo-audit` | full GEO + SEO audit across crawler, citability, content, technical, and platform signals | `전체 감사`, `사이트 분석`, `audit` | `L1/L2/L3` | `GEO-감사-보고서.md` |
| `geo-brand-mentions` | external brand mention visibility across media, communities, and AI-visible sources | `브랜드 언급`, `brand mentions` | `L1/L2/L3` | mention visibility assessment |
| `geo-citability` | AI citation likelihood for answer-ready, authoritative pages | `인용 가능성`, `citability` | `L1/L2/L3` | citation score and gaps |
| `geo-compare` | side-by-side GEO gap analysis versus competitors | `경쟁사 비교`, `compare` | `L2/L3` | comparative gap analysis |
| `geo-content` | content quality and E-E-A-T review | `콘텐츠 품질`, `E-E-A-T`, `content` | `L1/L2/L3` | content trust findings |
| `geo-crawlers` | robots, bot access, `llms.txt`, and crawlability review | `크롤러`, `robots.txt`, `crawlers` | `L1/L2/L3` | crawler access findings |
| `geo-llmstxt` | `llms.txt` audit and generation template | `llms.txt`, `llmstxt` | `L2/L3` | `llms.txt` recommendation or template |
| `geo-platform-optimizer` | platform-specific exposure review for Google AI Overviews, Perplexity, ChatGPT, Copilot, and Grok | `플랫폼 최적화`, `platform` | `L1/L2/L3` | platform scorecard |
| `geo-proposal` | client or internal improvement proposal from GEO findings | `제안서`, `proposal` | `L3` | sprint roadmap proposal |
| `geo-prospect` | lightweight prospect scan for sales or consulting discovery | `잠재 고객`, `prospect` | `L3` | prospect scan summary |
| `geo-report` | consolidated GEO report synthesis from individual findings | `보고서`, `report`, `요약` | `L1/L2/L3` | consolidated roadmap report |
| `geo-report-pdf` | print-ready markdown packaging for PDF delivery | `PDF 보고서`, `report-pdf` | `L3` | PDF-oriented report markdown |
| `geo-schema` | JSON-LD schema generation and validation | `스키마`, `JSON-LD`, `schema` | `L3` | `GEO-스키마-[도메인].md` |
| `geo-technical` | technical SEO diagnosis and remediation guidance | `기술 SEO`, `Core Web Vitals`, `technical` | `L2/L3` | technical remediation notes |

## Routing rules

1. Use the representative `geo` entrypoint first unless you already know the
   exact subskill owner you need.
2. Choose `portable-baseline`, `user-material`, or `local-overlay`.
3. If the request is execution-intent and `skills/*` is present, map it to the
   matching subskill above.
4. If the execution bundle is absent, do not promise the audit/report/schema
   workflow from the portable baseline alone.
5. Keep generated reports and exports downstream from the execution subskill
   that produced or justified them.

## Reference-guided extensions

These references do not add new standalone subskills. They constrain how the
existing subskills should report outcome and commerce/action claims.

| Reference | Use with | Purpose |
| --- | --- | --- |
| `references/measurement-loop.md` | `geo-audit`, `geo-brand-mentions`, `geo-citability`, `geo-compare`, `geo-platform-optimizer`, `geo-report`, `geo-proposal` | separate readiness, heuristic, observed answer, observed citation, referral, and conversion evidence |
| `references/commerce-readiness.md` | `geo-schema`, `geo-platform-optimizer`, `geo-report`, `geo-proposal`, `geo-technical` | separate product/schema readiness from merchant, catalog, checkout, action, and measurement readiness |
| `references/platform-truth-registry.md` | `geo-crawlers`, `geo-platform-optimizer`, `geo-compare`, `geo-prospect`, `geo-report` | source platform crawler and commerce mechanism claims from source_url, last_verified, confidence, and package_action |
| `references/measurement-capture-template.md` | `geo-audit`, `geo-brand-mentions`, `geo-citability`, `geo-platform-optimizer`, `geo-report`, `geo-proposal` | make observed_answer, observed_citation, referral_signal, and conversion_signal captures repeatable |
| `references/commerce-audit-worksheet.md` | `geo-schema`, `geo-platform-optimizer`, `geo-technical`, `geo-report`, `geo-proposal` | audit product, schema, merchant, catalog/feed, checkout/action, and measurement readiness |
| `references/private-surface-routing.md` | `geo-audit`, `geo-brand-mentions`, `geo-platform-optimizer`, `geo-report`, `geo-proposal` | separate public crawler/search from private connector, logged-in user, and user-provided context evidence |
| `references/regional-situational-routing.md` | `geo-audit`, `geo-compare`, `geo-platform-optimizer`, `geo-prospect`, `geo-report`, `geo-proposal` | adapt recommendations by region, language, vertical, brand maturity, and source-pack availability |
| `references/policy-risk-gate.md` | `geo-crawlers`, `geo-content`, `geo-platform-optimizer`, `geo-report`, `geo-proposal`, `geo-technical` | check robots, terms, privacy, regulated claims, brand claims, and commerce eligibility before recommendations |
| `references/report-template-contract.md` | `geo-report`, `geo-report-pdf`, `geo-proposal`, `geo-audit` | require score_type, evidence_label, confidence, measurement_status, commerce_status, private_surface_status, regional_context, and policy_risk |
| `references/implementation-completion-plan.md` | `geo`, `geo-report`, `geo-proposal` | close P2-P13 hardening with all_must_passed or failed_must_queue evidence |

Use these references when the request asks whether GEO "worked", whether an AI
platform cites a brand, whether shopping/action readiness exists, or whether a
product/schema change can support commerce outcomes. Use the report and
completion contracts when the user asks for a consolidated handoff or
whole-system completion judgment.
