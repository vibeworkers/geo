# User-Level Workflow Guide

Use this reference when an advanced execution workflow needs to explain the
same GEO finding to different operator profiles.

This guide preserves the practical onboarding material from the earlier
`geo-seo-skills-kr` package, but adapts it to the current portable `geo`
contract:

- start from `geo <request>` or `$geo <request>`, not a separate slash-command
  session surface
- keep `SKILL.md` as the representative router
- route execution work only after `skills/*` is confirmed
- keep measured outcome, commerce, private-surface, regional, and policy-risk
  claims inside their reference gates

## Profiles

The execution bundle may shape output for three local profiles.

| Profile | User type | Output style |
| --- | --- | --- |
| `L1` manager | marketing, content, or business owner with no code access | business language, decision impact, and request notes for operators or developers |
| `L2` operator | webmaster, CMS operator, FTP/cPanel user, or site maintainer | step-by-step CMS, file, hosting, and verification guidance |
| `L3` builder | developer, technical consultant, or automation owner | technical specification, code snippets, CLI checks, schema, and export commands |

The analytical depth should stay the same across profiles. Only explanation,
handoff format, and implementation detail should change.

## Recommended First Run

For a first local execution pass, use a full audit before drilling into
individual workflows:

```text
geo audit https://example.com for GEO and AI visibility.
```

Then route follow-up work by profile:

| Profile | Recommended sequence |
| --- | --- |
| `L1` manager | audit, brand mentions, platform visibility, consolidated report |
| `L2` operator | audit, technical review, crawler access, `llms.txt`, competitor compare, checklist report |
| `L3` builder | prospect scan, audit, technical review, schema, `llms.txt`, proposal, PDF package |

If the request is broad and the goal, surface, success condition, or evidence
target is unclear, run the clarification-first intake in `SKILL.md` before
starting execution.

## Profile-Specific Output Rules

### L1 manager

Use this profile when the user needs to decide what to ask another team to do.

Prefer:

- status language such as `good`, `watch`, `risk`, or `blocked`
- top three immediate actions
- business impact and priority
- handoff notes for operators, developers, content teams, or PR teams

Avoid:

- making the user read raw robots rules, schema blocks, or server config unless
  those details are part of a handoff note
- implying that a readiness score proves observed AI visibility

When an L1 user asks for an L2/L3-only workflow, offer a handoff note instead
of treating the request as impossible. The note should include:

- requested task
- reason
- target URL or file path
- acceptance check
- priority
- owner profile

Example:

```text
[Handoff] llms.txt setup request

Task: create and publish an llms.txt file at the site root.
Reason: AI crawlers need a concise public guide to the site's important pages.
Target: https://example.com/llms.txt
Acceptance check: the URL returns HTTP 200 with text/plain or readable markdown.
Priority: high
Owner profile: L2 operator or L3 builder
```

### L2 operator

Use this profile when the user can change CMS, hosting, FTP, cPanel, or
site-root files but may not own application code.

Prefer:

- exact files and paths, such as `/robots.txt`, `/llms.txt`, sitemap locations,
  CMS settings, or plugin configuration
- before/after examples
- verification URLs and simple HTTP checks
- rollback notes when a change affects crawl permissions

Keep technical claims inside the right evidence boundary. For example,
publishing `llms.txt` improves LLM-facing guidance readiness, but it does not
prove that a platform has cited the site.

### L3 builder

Use this profile when the user can change source code, server config,
automation, or delivery pipelines.

Prefer:

- JSON-LD, HTML, server config, CLI commands, and scripts
- validation steps such as schema validators, curl checks, sitemap checks, and
  report regeneration
- implementation priority by risk, effort, and expected readiness impact
- export tooling guidance for reports and PDF-oriented markdown

When code or scripts are included, keep them subordinate to the specific
workflow owner under `skills/geo-*`.

## Environment Notes

The older package distinguished Claude Code from Claude web usage. In the
portable package, treat that distinction as a runtime-local execution detail:

| Environment style | Practical implication |
| --- | --- |
| local code/runtime shell | can run HTTP probes, parse HTML, collect files, save markdown reports, and batch scan domains |
| chat-only or web-fetch runtime | can inspect fetched pages and produce guidance, but may need manual checks for HTTP status, PageSpeed, rich-results validation, and PDF conversion |

Do not let environment convenience weaken the evidence label. If a result is
manual, heuristic, or unmeasured, label it that way.

## Common Workflow Interpretation

| Workflow | L1 framing | L2 framing | L3 framing |
| --- | --- | --- | --- |
| `geo-audit` | current AI search readiness and top team requests | prioritized site checklist | full technical scorecard and implementation matrix |
| `geo-crawlers` | whether AI services can reach the site | robots and `llms.txt` file edits | crawler policy, HTTP probes, and access matrix |
| `geo-citability` | whether content is likely to be useful in answers | CMS/content structure fixes | schema, answer blocks, and technical citation signals |
| `geo-content` | trust and clarity of the content | author, date, headings, and CMS cleanup | E-E-A-T, metadata, schema, and content quality checks |
| `geo-brand-mentions` | how AI-visible sources recognize the brand | sameAs and profile consistency | entity graph, Organization/Person schema, and evidence capture |
| `geo-platform-optimizer` | where the brand may appear weak across AI platforms | platform-specific setup checklist | platform signal matrix and source-verified mechanism notes |
| `geo-technical` | developer/operator request list | hosting, CMS, sitemap, HTTPS, and header fixes | rendering, indexability, performance, and server remediation |
| `geo-llmstxt` | request to publish AI-facing site guidance | create or update site-root guidance files | generate, validate, and publish `llms.txt` or `llms-full.txt` |
| `geo-compare` | competitor gap summary | side-by-side checklist | site-config vs page-content gap matrix |
| `geo-schema` | request structured data implementation | developer handoff only | JSON-LD generation, insertion, and validation |
| `geo-prospect` | sales opportunity and improvement gap | not primary | lightweight batch scan and proposal lead-in |
| `geo-proposal` | roadmap summary | operator checklist support | sprint roadmap, scope, effort, and verification plan |
| `geo-report` | executive or team summary | work-tracking checklist | consolidated technical report |
| `geo-report-pdf` | delivery-ready report package | not primary | PDF-oriented markdown and conversion commands |

## Output Files

Local execution workflows may create markdown outputs such as:

| Workflow | Typical output |
| --- | --- |
| `geo-audit` | `GEO-감사-보고서.md` |
| `geo-content` | `GEO-콘텐츠-분석.md` |
| `geo-citability` | `GEO-인용가능성-분석.md` |
| `geo-crawlers` | `GEO-크롤러-분석.md` |
| `geo-report` | `GEO-종합보고서.md` |
| `geo-proposal` | `GEO-제안서-[domain]-[date].md` |
| `geo-report-pdf` | PDF-oriented markdown plus runtime-specific conversion guidance |

The output file is a downstream deliverable. The source evidence, report
metadata, and relevant reference gates still own the claim boundary.
