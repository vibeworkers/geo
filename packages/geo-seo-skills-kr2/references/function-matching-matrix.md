# Function Matching Matrix

This matrix is the evidence contract for the root routing table. It maps each
user command to the subskill that executes it, the runtime required, and the
strongest evidence state it can produce without additional live platform output.

Evidence states follow `references/evidence-boundary.md`.

| Command | Subskill | Level | Runtime | Primary evidence basis | Maximum default evidence state | Output / decision |
|---|---|---|---|---|---|---|
| `/geo audit` | `geo-audit` | L1,L2,L3 | Core | WebFetch page, robots, sitemap, metadata, schema, content structure | Readiness + Heuristic | Site-level GEO readiness report |
| `/geo brand` | `geo-brand` | L1,L2,L3 | Core | Public page claims, brand positioning text, accessible search/context signals | Heuristic | Brand perception gap and CP input |
| `/geo content` | `geo-content` | L1,L2,L3 | Core | Content structure, authorship, freshness, helpful-content/E-E-A-T principles | Heuristic | Content quality and improvement plan |
| `/geo citability` | `geo-citability` | L1,L2,L3 | Core | Answer structure, entity clarity, sourceability, crawl readiness | Heuristic | AI citation readiness assessment |
| `/geo crawlers` | `geo-crawlers` | L1,L2,L3 | Core | `robots.txt`, headers, sitemap, crawler docs | Readiness | AI/search crawler access readiness |
| `/geo brands` | `geo-brand-mentions` | L1,L2,L3 | Core | Public mentions when fetched, otherwise prompted search evidence | Heuristic or Measured if URLs captured | Mention inventory |
| `/geo platforms` | `geo-platform-optimizer` | L1,L2,L3 | Core | Platform docs, bot map, page readiness signals | Readiness + Heuristic | Platform-specific readiness plan |
| `/geo report` | `geo-report` | L1,L2,L3 | Core | Aggregated subskill outputs | Same as weakest/strongest labelled inputs | Report assembly |
| `/geo technical` | `geo-technical` | L2,L3 | Core | robots, sitemap, canonical, status, headers, schema presence | Readiness | Technical SEO/GEO issue list |
| `/geo llmstxt` | `geo-llmstxt` | L2,L3 | Core | llms.txt proposal and site content inventory | Readiness + Heuristic | llms.txt draft and placement guidance |
| `/geo compare` | `geo-compare` | L2,L3 | Core | Same signals collected across compared URLs | Readiness + Heuristic | Comparative readiness gaps |
| `/geo schema` | `geo-schema` | L3 | Core | schema.org and Google structured data guidance | Readiness | JSON-LD detection/generation guidance |
| `/geo report-pdf` | `geo-report-pdf` | L3 | Extension | Local file rendering/runtime | Manual Fallback until file generated | PDF report artifact |
| `/geo proposal` | `geo-proposal` | L3 | Core | Audit findings and business-type mapping | Heuristic | Improvement proposal |
| `/geo prospect` | `geo-prospect` | L3 | Core/Extension | Fast public readiness signals across URLs | Readiness + Heuristic | Prospect scan summary |
| `/geo multilang` | `geo-multilang` | L2,L3 | Core | `hreflang`, localized URL structure, sitemap alternates | Readiness | Multilingual GEO diagnosis |
| `/geo lang-platform` | `geo-lang-platform` | L1,L2,L3 | Core | `lang-platform-map.md` plus `source-index.md` | Readiness + Heuristic | Language-specific platform plan |
| `/geo lang` | none | L1,L2,L3 | Core | Session variable | Not evidence-producing | Output language update |
| `/geo realtime` | `geo-realtime` | L3 | Extension | Captured browser/platform output, citation URLs, screenshots/logs | Measured if captured | Citation observation from stored output |
| `/geo tracker` | `geo-tracker` | L3 | Extension | Baseline files plus repeated measurements | Measured if source observations are stored | Time-series gap tracking |
| `/geo batch` | `geo-batch` | L3 | Extension | Repeated readiness scan across URLs | Readiness + Heuristic | Batch comparison |
| `/geo-code init` | `geo-code` | L3 | Extension | Local Node.js, Playwright, browser-citation, and CDP checks | Manual Fallback or Measured environment state | Extension environment check |
| `/geo-code pipeline` | `geo-code` | L3 | Extension | Ordered execution of audit, realtime, tracker, and optional CP inputs | Inherits each stage's evidence state | Automated extension pipeline |
| `/geo-code status` | `geo-code` | L3 | Extension | Local analysis files, baseline files, CP project presence | Measured if local files are observed | Local project status |

## Contract Rules

0. A claim is realistic only when it is tied to observed site data,
   official/standard documentation, or stored platform output. Without one of
   these, the command must downgrade the claim to `Heuristic` or `Manual Fallback`.
1. A command may not claim `Measured` unless it stores or prints direct observed platform output, citation URLs, logs, referrals, conversion data, or equivalent raw observations.
2. Readiness checks may recommend actions but may not claim that an AI platform will cite or rank the page.
3. Heuristic scores must be labelled as decision heuristics unless calibrated against external measurements.
4. Platform-specific claims must point to `source-index.md` or be marked `requires live verification`.
5. Runtime-specific commands must declare `Manual Fallback` when the current host cannot execute the required browser, filesystem, or shell operation.
