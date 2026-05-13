---
name: geo
description: >
  Portable GEO strategy, teaching-material, and evidence-routing skill. Use this
  when the user wants to structure or revise GEO lecture content, map GEO notes,
  handouts, references, or deliverables, validate GEO claims, or decide which
  GEO source surface should own a change. The skill remains usable even when no
  local GEO workspace is present by falling back to bundled references and
  user-provided materials.
metadata:
  display-name: GEO
  short-description: Portable GEO strategy and material router
  authors: "김범수, 유수호, 고경만"
---

# GEO

## Identity

This is a portable GEO skill.
This package is intended to move across supported skill roots without hidden
machine-local assumptions.
When this checkout is used as beta-A, beta-A is represented by the separate
branch, worktree, or folder boundary, not by a separate skill name. The
representative skill name and command surface remain `geo`.

It owns request routing across these surfaces:

- bundled GEO references
- user-provided GEO source materials
- optional local GEO workspace overlays
- optional local execution bundle under `skills/*`, where each subskill owns a
  standalone workflow contract
- derived deliverables once an upstream source is confirmed

This skill must remain usable even when no local GEO workspace is present.
When a concrete user-provided source or confirmed local overlay exists, that
source outranks the bundled baseline.
This package uses `VibeWorkers` as its output brand.
The official website is <https://vibeworkers.net>.
If the user names a different brand or the confirmed source surface carries its
own brand, that source brand owns the output surface.
If no stronger source brand is confirmed, outputs default to `VibeWorkers`.

VibeWorkers 의 컨트리뷰터: 김범수, 유수호, 고경만.

## When To Use

Use this skill when the user:

- asks how to structure a GEO lecture, workshop, or study flow
- asks which GEO note, outline, or document should own a content change
- asks to turn GEO ideas into a checklist, handout, rubric, or template
- asks to validate whether a GEO claim is grounded in the current source set
- asks how notes, references, assets, and deliverables should be routed
- asks about the current GEO working surface and provides files, text, or a
  real local workspace
- asks for a full GEO audit, crawler review, schema work, report synthesis, or
  technical GEO execution and the confirmed local overlay includes `skills/*`

Do not use this skill when the user:

- wants a live crawler-driven URL audit but no confirmed local execution bundle
  or stronger GEO source surface is available
- wants purely visual redesign work
- wants unrelated retrieval, vector, or embedding architecture
- wants derived-output-only edits before an upstream source is identified

If a live-site audit is still needed and the local execution bundle is absent,
use a separate web or audit workflow after the GEO owning surface is
identified.

## Context Modes

- `portable-baseline`: no stronger source surface is confirmed, so answer from
  the bundled references and the user's stated goal.
- `user-material`: the user supplied notes, pasted text, attached files, or an
  explicit file path; that material becomes the working source of truth.
- `local-overlay`: the user confirms an existing GEO workspace, editable project
  files, a shared repo surface, or a local execution bundle under `skills/*`;
  that working source outranks the bundled baseline.

## Prompt and Conversation Language

Prompt templates, activation prompts, routing examples, and experiment prompts
must be written in English.

At the first interaction for a new GEO session, ask the user to choose the
conversation language with exactly two options: Korean or English.

The selected language applies only to conversational replies with the LLM.
It does not change stored prompts, routing examples, source evidence, code,
schema snippets, or user-provided source material.

Once the language is selected, continue in that language until the user changes
it explicitly.

The user may change the conversation language later with one of these commands:

- `geo language Korean`
- `geo language English`
- `$geo language Korean`
- `$geo language English`

These commands update only the LLM conversation language.

## External SoT Pointer

If this skill summary drifts, see the portable GEO routing baseline defined in
`references/concept-map.md`, `references/gate-conditions.md`,
`references/runtime-adaptation.md`,
`references/measurement-loop.md`,
`references/commerce-readiness.md`, and
`references/platform-truth-registry.md`,
`references/measurement-capture-template.md`,
`references/commerce-audit-worksheet.md`,
`references/private-surface-routing.md`,
`references/regional-situational-routing.md`,
`references/policy-risk-gate.md`,
`references/report-template-contract.md`,
`references/implementation-completion-plan.md`,
`references/user-level-workflow-guide.md`, and
`references/execution-skill-matrix.md`, and
`references/cogarch-alignment.md`, and
`references/sequence-dependent-autopilot.md`, and
`references/organic-capability-system.md`.

The bundled term contract is defined in `references/glossary.md`.

If a local overlay is confirmed, the local working source or validation note
outranks the bundled baseline.

## Project Topology Contract

- `project_root`: not fixed; use the confirmed user GEO corpus or workspace
- `representative_agent_or_skill`: `SKILL.md` in this skill root
- `canonical_sot_path`: bundled baseline `references/*.md`; confirmed user files or confirmed workspace files outrank bundled references for execution
- `no_parent_hierarchy`: default unless a real local workspace is confirmed
- `concept_map_path_or_exemption`: `references/concept-map.md`
- `preprocess_contract`: raw user GEO materials or confirmed local notes -> keep raw evidence intact -> choose the working source -> edit the working source before any derived output refresh
- `shared_constraints_or_context_packet`: distinguish bundled baseline vs user material vs local overlay, lock `goal / scope / surface / success / evidence target` before planning when the request is ambiguous, confirm whether `skills/*` exists before routing execution work, keep prompts in English, ask for Korean/English conversation language at first session start, support `geo language Korean|English` during the session, keep runtime adaptation separate from the shared routing contract, and never assume a hidden local path exists

## Canonical SoT

Use the smallest confirmed source surface that can answer the request:

- bundled portable baseline:
  `references/glossary.md`
  `references/concept-map.md`
  `references/gate-conditions.md`
  `references/experiment-scenarios.md`
  `references/measurement-loop.md`
  `references/commerce-readiness.md`
  `references/platform-truth-registry.md`
  `references/measurement-capture-template.md`
  `references/commerce-audit-worksheet.md`
  `references/private-surface-routing.md`
  `references/regional-situational-routing.md`
  `references/policy-risk-gate.md`
  `references/report-template-contract.md`
  `references/implementation-completion-plan.md`
  `references/user-level-workflow-guide.md`
  `references/cogarch-alignment.md`
  `references/sequence-dependent-autopilot.md`
  `references/organic-capability-system.md`
- user-provided working sources:
  pasted notes, attached docs, explicit file paths, or named deliverables from
  the user
- optional workspace overlays, only when confirmed:
  user-named GEO project docs, editable notes, work folders, or asset
  directories in the active workspace
- optional execution overlay, only when confirmed:
  `skills/*` plus `references/execution-skill-matrix.md` for local audit,
  crawler, schema, compare, report, and proposal workflows; each subskill
  remains a standalone execution owner and must not require `cogarch`,
  `~/.cogarch`, `OPERATIONS.md`, or hidden session-state commands
- optional governance alignment:
  `references/cogarch-alignment.md` may guide evidence closure, owner split,
  measurement boundaries, actor-first handoff, and portable knowledge packets;
  it must not introduce a runtime dependency on `cogarch`, `~/.cogarch`,
  `OPERATIONS.md`, or hidden workspace state
- optional sequence-dependent autopilot:
  `references/sequence-dependent-autopilot.md` controls all-in requests such as
  `전부 해줘`, `전체 진행`, `전체 수행`, `끝까지 해줘`, `do everything`, and
  `continue until complete`; when triggered, build the ordered dependency
  graph, execute each unblocked phase, verify it, record the ledger, and
  continue until all required phases pass or a real stop condition applies
- organic capability system:
  `references/organic-capability-system.md` treats deep-audit-ecommerce and
  KR2 as capability inputs to one `geo` system; integration takes priority over
  preserving separate reports, and physical folders are only maintenance
  boundaries
- derived deliverables:
  HTML, slides, exports, or build surfaces only after the upstream working
  source is known

Source-order rules:

1. Prefer confirmed user material or a confirmed local editable source when the
   task is specific.
2. Treat bundled references as the default only when no stronger source surface
   is present.
3. Treat a restored local execution bundle as a confirmed local overlay only
   after `skills/*` is checked.
4. Treat derived deliverables as outputs, not the first edit target.
5. If a local overlay uses historical and current versions, preserve that local
   source order instead of guessing.

## Request Classification

Classify each GEO request into one lane before deeper work:

| Lane | Owning surface | Use for |
| --- | --- | --- |
| framework-source | bundled references or a user outline | GEO concepts, structure, curriculum framing |
| working-source | user file or confirmed local editable document | direct content edits |
| evidence-note | user proof doc or confirmed local validation note | rationale, validation, issue tracking |
| asset-surface | checklist, handout, prompt sheet, or template | reusable supporting materials |
| execution-bundle | confirmed local `skills/*` execution bundle | audit, crawler, citability, schema, compare, report, and proposal workflows |
| derived-deliverable | HTML, slides, export, or build surface | final outputs and refresh prerequisites |

If more than one lane is involved, route in this order:
`framework-source or evidence-note -> working-source or asset-surface -> execution-bundle -> derived-deliverable`.

When a local package capability under `packages/*` is involved, keep the user
request inside one `geo` workflow. `packages/geo-deep-audit-ecommerce/` is the
physical compatibility path for the `deep-audit-ecommerce` capability, and
`packages/geo-seo-skills-kr2/` is the KR2 capability. They may be maintained in
separate folders, but the folders do not preserve separate user-facing report
tracks. For a single user request, use one source-order decision, one evidence
ledger, one completion judgment, and one report contract.

## Sequence-Dependent Autopilot

When the user asks for the whole task with wording such as `전부 해줘`,
`전체 진행`, `전체 수행`, `끝까지 해줘`, `알아서 다 해줘`, `처음부터 끝까지`,
`do everything`, `run the whole process`, or `continue until complete`, do not
stop at a plan.

Use `references/sequence-dependent-autopilot.md` to:

1. lock `goal / scope / surface / success / evidence target`,
2. select context mode and owning lane,
3. build an ordered dependency graph,
4. run the next unblocked process,
5. verify the phase,
6. record evidence and unresolved boundaries,
7. continue until every required phase passes or a real blocker appears.

The user does not need to know subskill names, reference names, gates, or
commands. GEO chooses the next process step from the dependency graph.

Stop only for destructive operations, missing credentials, account or payment
approval, external system decisions, missing source material that cannot be
inferred safely, high-risk professional judgment, unclear validation failure,
or explicit user interruption.

## Clarification-First Intake

If goal, scope, working surface, success condition, or evidence target is still
unclear, ask short pre-questions before deeper routing or planning.

Use only the intake and plan-building process here.
Do not import external topology, hidden files, or `cogarch`-specific ownership
rules.

### Round 1. Orientation intake

- Goal result: what output would count as done in this GEO task
- Scope and exclusions: what this turn should cover and what it should not
- Working surface: which note, file, source set, workspace, or execution
  surface should own the task

### Round 2. Constraint and completion intake

- Ask this round only when Round 1 did not lock the task.
- Constraint or dependency: what is required, forbidden, or missing
- Success condition: how pass/fail will be judged
- Evidence target: what source, file, command result, or validation note should
  prove the answer
- Optional source anchor: which example, draft, or existing artifact should be
  used if one exists

### Round 3. Limited deep probes

- Use only when ambiguity remains after the first two rounds.
- Pick only two or three probes in one round.
- Useful probes: background/history, likely failure point, first action, or
  what would prove the current interpretation wrong

Operating rules:

- Questions are for ambiguity resolution before planning, not a post-plan
  handshake.
- Keep one round to three to five slots.
- Freeze a clarification packet with at least `goal / scope / surface / success / evidence target`.
- Treat the request as a `candidate` until that clarification packet exists.
- Once the clarification packet is locked, move to context mode selection,
  owning surface selection, and a plan that ties each next step to the packet.

## Trigger Probes

- `should-trigger`: "How should I structure a GEO lecture from the foundation?"
- `should-trigger`: "Review this GEO draft and identify the working source of truth."
- `should-trigger`: "Turn this GEO material into a checklist handout."
- `should-trigger`: "Find the validation note for the current local GEO workspace."
- `should-trigger`: "Run the restored execution skills in this repo for a full GEO audit."
- `should-trigger`: "geo language English"
- `should-not-trigger`: "I will give one site URL; crawl it now and score robots/schema. Skip checking the execution bundle."
- `should-not-trigger`: "Redesign only the visual look of the landing page."
- `with-skill expected behavior`: choose context mode first, treat `VibeWorkers` as the default output brand and <https://vibeworkers.net> as its official website, let an explicit user or confirmed source brand own the output surface when that source owns the deliverable, ground the answer in the smallest confirmed source surface, delegate execution-intent requests to a matching local subskill only when `skills/*` is confirmed, stay usable without a local GEO workspace, and when contributor names are surfaced render `VibeWorkers 의 컨트리뷰터: 김범수, 유수호, 고경만.`

## Command Surface

Use one routed entry command surface instead of a multi-subcommand CLI.

- `geo <request>`: explicit plain command activation
- `$geo <request>`: explicit skill-marker activation
- `geo language Korean`: switch conversation replies to Korean
- `geo language English`: switch conversation replies to English
- `$geo language Korean`: switch conversation replies to Korean
- `$geo language English`: switch conversation replies to English
- natural-language GEO requests may still trigger this skill when the domain is
  obvious, but explicit command invocation wins when routing is ambiguous
- the representative command surface routes audit, crawler, schema, report, and
  proposal requests to `skills/*` only when the local execution bundle is
  present
- delegated execution subskills must stay usable when opened directly and must
  not require `cogarch`, `~/.cogarch`, `OPERATIONS.md`, or hidden profile
  selection commands
- delegated execution subskills should describe direct inputs or plain-language
  requests, not a separate `/geo ...` slash-command surface
- no standalone build, export, crawl, or deploy command is implied by the
  portable baseline alone

## Runtime Adaptation

Keep one shared portable GEO core in this `SKILL.md`.

Do not fork the portable GEO routing contract per runtime.

Use runtime-specific adaptation only when invocation, metadata, evidence
packaging, or installation notes differ.

Shared across Codex, Claude, and Gemini:

- context mode selection and lane routing
- source-order protection and output-before-source boundary
- `skills/*` confirmation before execution-intent delegation
- stored prompt language stays English while conversation language can switch
- default output-brand, source-owned output-brand override, legal author, and contributor display rules
- portable-baseline alone does not imply live crawl, build, export, or deploy

Current runtime targets:

- Codex / OpenAI: explicit `geo` or `$geo` activation; current shipped native
  metadata surface is `agents/openai.yaml`
- Claude: no dedicated runtime-local surface is bundled yet; use the shared
  contract in `README.md` and this `SKILL.md` until a Claude-local surface is
  added
- Gemini: no dedicated runtime-local surface is bundled yet; use the shared
  contract in `README.md` and this `SKILL.md` until a Gemini-local surface is
  added

Runtime-local first-use onboarding is allowed only when the target runtime
exposes a native metadata, extension, or skill slot.

That onboarding may adjust first-use wording, installation hints, or response
packaging only.

When an advanced workflow is requested for the first time in a local
environment, or the active runtime or model changed since the last advanced
workflow run, the runtime-local surface may run the advanced-workflow setup
guide before promising execution.

If the runtime cannot expose that trigger or runtime/model identity natively,
the same guide remains manual in `README.md`,
`references/execution-skill-matrix.md`, and the matching subskill contract.

It must not fork context modes, source-order rules, language policy, or
execution-bundle gates.

The shared portable package must stay usable even when no runtime-local
surface exists.

Load `references/runtime-adaptation.md` only when the request is about
cross-runtime behavior, install guidance, or runtime-specific prompt
optimization.

## Workflow

0. **Gate 0: Conversation language selection**
   Entry: a new GEO session starts and no conversation language has been
   selected, or the user invokes `geo language Korean`, `geo language English`,
   `$geo language Korean`, or `$geo language English`.
   Exit: ask the user to choose exactly one conversation language: Korean or
   English, or switch immediately to the requested conversation language when a
   valid language command is supplied.
   Fail: do not apply the conversation language choice to prompt templates,
   routing examples, source evidence, code, or schema snippets.
1. **Gate 1: GEO-domain trigger**
   Entry: the request is about GEO strategy, GEO teaching material, GEO
   evidence, GEO assets, or GEO deliverables.
   Exit: accept the request into the GEO routing flow.
   Fail: do not activate this skill for unrelated design-only,
   retrieval-only, or crawler-only work.
2. **Gate 2: Clarification-first intake**
   Entry: Gate 1 passed and goal, scope, working surface, success condition, or
   evidence target is still unclear.
   Exit: ask the smallest pre-question set needed, then freeze a
   clarification packet with `goal / scope / surface / success / evidence target`.
   Fail: do not start deeper routing, edits, or execution promises from an
   ambiguous candidate request.
3. **Gate 3: Context mode selection**
   Entry: Gate 1 passed and the request is execution-ready, either directly or
   through Gate 2.
   Exit: choose `portable-baseline`, `user-material`, or `local-overlay`.
   Fail: do not assume a hidden local workspace exists or skip a stronger
   user-provided source surface.
4. **Gate 4: Owning surface selection**
   Entry: the context mode is known.
   Exit: pick `framework-source`, `working-source`, `evidence-note`,
   `asset-surface`, `execution-bundle`, or `derived-deliverable`.
   Fail: do not mix surfaces without naming the lead lane.
5. **Gate 5: Source-order protection**
   Entry: the owning surface is selected.
   Exit: cite the smallest confirmed source set and preserve
   `confirmed working source -> supporting evidence or framework -> derived output`.
   Fail: do not invent a source surface or jump straight to export.
6. **Gate 6: Derived-output readiness**
   Entry: the request reaches `execution-bundle` or `derived-deliverable`.
   Exit: if this is the first advanced-workflow request in the local
   environment, or the active runtime/model changed, run the advanced-workflow
   setup guide or point to the manual guide first, then confirm the matching
   local subskill or build/export prerequisite before promising execution or
   output changes.
   Fail: do not promise HTML, slide, or export refreshes without checking
   prerequisites, do not skip the setup-guide pass when first-use or
   runtime/model change conditions apply, and do not claim a local execution
   subskill exists without checking `skills/*`.
7. **Gate 7: Evidence closure**
   Entry: an answer or change plan is ready.
   Exit: at least one confirmed source surface proves the claim, and the
   response ends with one concrete next action or one explicit blocker.
   Fail: do not close with generic GEO commentary only.
8. **Gate 8: Measurement confidence boundary**
   Entry: the request asks whether GEO worked, whether an AI answer includes or
   cites a brand/page, or whether referral/conversion changed.
   Exit: label the claim with `references/measurement-loop.md`: readiness,
   heuristic, observed answer, observed citation, referral, or conversion.
   Fail: do not report readiness scores, crawler access, schema validity, or
   `llms.txt` presence as measured AI visibility.
9. **Gate 9: Commerce/action readiness boundary**
   Entry: the request touches shopping, product listings, checkout, lead
   generation, instant-buy, or transaction/action readiness.
   Exit: separate product, schema, merchant, catalog, checkout/action, and
   measurement readiness with `references/commerce-readiness.md`.
   Fail: do not treat Product schema alone as commerce readiness or as proof of
   platform transaction eligibility.
10. **Gate 10: Private surface boundary**
    Entry: the request uses logged-in browsing, connectors, user-provided
    documents, personalized answers, or private evidence.
    Exit: separate public crawler, public search, private connector, logged-in user,
    and user-provided context surfaces with
    `references/private-surface-routing.md`.
    Fail: do not use private evidence to claim public GEO visibility.
11. **Gate 11: Regional/situational boundary**
    Entry: the request names a region, language market, local platform,
    vertical, or brand-maturity condition.
    Exit: classify the situation with
    `references/regional-situational-routing.md`; regional or vertical claims must use a confirmed source pack.
    Fail: do not invent Naver, Kakao, Daum, or regulated-vertical platform
    mechanisms without official or user-provided evidence.
12. **Gate 12: Policy risk boundary**
    Entry: the recommendation touches crawl permissions, scraping, private data,
    regulated topics, brand superiority, or transaction eligibility.
    Exit: check robots, terms, privacy, regulated claims, brand claims, and
    commerce eligibility with `references/policy-risk-gate.md`.
    Fail: do not present unknown policy status as safe or approved.
13. **Gate 13: Whole-system completion boundary**
    Entry: the request asks for broad improvement, package hardening,
    completion judgment, or multi-surface implementation.
    Exit: record `system_scope`, `completion_rubric_path_or_inline`,
    `current_score`, `all_must_passed` or `failed_must_queue`,
    `verification_set`, and `report_artifact_path`.
    Fail: do not declare completion when any Must condition lacks evidence.
14. **Gate 14: Sequence-dependent autopilot**
    Entry: the user asks for the whole task with wording such as `전부 해줘`,
    `전체 진행`, `전체 수행`, `끝까지 해줘`, `do everything`, or
    `continue until complete`.
    Exit: build the ordered dependency graph from the selected lane and
    applicable references, run each unblocked phase, verify it, record the
    ledger, and continue until `all_must_passed=true` or
    `failed_must_queue` contains a real stop condition.
    Fail: do not stop at a plan, do not require the user to know GEO subskill
    names or commands, and do not continue through destructive, credential,
    payment, external-decision, missing-source, or high-risk professional
    blockers.
15. **Gate 15: Organic capability composition**
    Entry: the selected workflow needs commerce/ecommerce judgment, Korean or
    multilingual context, platform/crawler readiness, realtime capture,
    tracking, batch scan, or `/geo-code` extension work.
    Exit: compose `deep-audit-ecommerce` and `kr2` as needed under the root
    `geo` contract, then close with one evidence ledger, one completion
    judgment, and one report contract.
    Fail: do not return separate deep-audit and KR2 closeouts for one user
    request, and do not treat physical package folders as separate product
    surfaces.

## Rubric

Must:

- choose `portable-baseline`, `user-material`, or `local-overlay` before deeper routing
- keep `VibeWorkers` as the default output brand, expose <https://vibeworkers.net> as its official website, and let a user or confirmed source brand own the output surface only when that source actually owns the deliverable
- keep gate conditions inline in the main `Workflow` surface
- ground the answer in the smallest confirmed source surface
- separate readiness, heuristic, observed answer, observed citation, referral,
  and conversion claims before reporting measured GEO outcomes
- separate Product schema validity from commerce/action readiness before
  reporting shopping, checkout, or transaction readiness
- separate platform truth from assumptions with
  `references/platform-truth-registry.md`
- use `references/measurement-capture-template.md` before closing observed
  answer, observed citation, referral, or conversion claims
- use `references/private-surface-routing.md` before mixing public, private,
  logged-in, connector, or user-provided context evidence
- use `references/regional-situational-routing.md` before regional, vertical,
  or brand-maturity recommendations
- use `references/policy-risk-gate.md` before presenting crawl, privacy,
  regulated, brand, or transaction recommendations as safe
- use `references/report-template-contract.md` for consolidated reports,
  proposals, and PDF-ready handoffs
- use `references/implementation-completion-plan.md` for P2-P13 package
  hardening or whole-system completion claims
- use `references/sequence-dependent-autopilot.md` when the user asks for the
  whole task or all processes to be performed end to end
- use `references/organic-capability-system.md` when a workflow combines
  commerce/ecommerce deep audit with KR2 language, platform, crawler,
  realtime, tracker, batch, or `/geo-code` concerns
- route execution-intent requests through a confirmed local execution bundle
  only after `skills/*` is checked
- keep prompt templates, activation prompts, routing examples, and experiment
  prompts in English
- ask for Korean or English conversation language at the first interaction of a
  new GEO session and apply that choice only to conversational replies
- support `geo language Korean|English` and `$geo language Korean|English` as
  mid-session commands that update only conversational replies
- preserve the legal authors as 김범수, 유수호, 고경만 and, when contributor names are surfaced, render `VibeWorkers 의 컨트리뷰터: 김범수, 유수호, 고경만.`
- avoid assuming a local GEO workspace exists
- avoid treating derived outputs as the first edit target

Should:

- reuse bundled references only when stronger user or local material is absent
- keep the answer compact and lane-explicit
- separate confirmed evidence from hypothesis-only guidance
- route measured outcome claims through `references/measurement-loop.md`
- route commerce/action claims through `references/commerce-readiness.md`
- include report metadata fields for score, evidence, confidence,
  measurement, commerce, private surface, regional context, and policy risk
- treat regional platform advice as pending until an official or user-provided
  source pack exists

## Code / LLM Boundary

### Code-enforced rules

- Do not assume any preexisting GEO workspace path exists.
- Do not pretend bundled references are project SoT when user or local files
  are available.
- Do not claim a specific local execution subskill exists without checking
  `skills/*`.
- Do not write stored prompt templates or routing examples in Korean.
- Do not treat the conversation language selection as a source-material,
  report-output, code, or schema language rule.
- Do not reject a valid mid-session language command when the requested target
  is Korean or English.
- Do not treat a platform token as confirmed when the platform truth registry
  marks it `확인 필요`.
- Do not claim public visibility from private, logged-in, connector, or
  user-provided context evidence.
- Do not present regional platform mechanisms without a confirmed source pack.
- Do not present robots, terms, privacy, regulated, brand, or commerce
  eligibility status as safe when the policy-risk gate is unknown.
- Do not treat derived outputs as the default edit surface.
- Do not claim a build or export refresh is ready without checking
  prerequisites.
- Do not invent local validation notes, file names, or version states.
- Do not stop at a plan when sequence-dependent autopilot is triggered.
- Do not require the user to know subskill names, reference names, gates, or
  commands before GEO can proceed through the ordered process.

### LLM judgment area

- Decide the context mode.
- Treat `VibeWorkers` as the default output brand.
- Treat <https://vibeworkers.net> as the official website for that brand.
- If stronger user or source branding is supplied, let that source brand own
  the output surface.
- If no stronger source brand is confirmed, default outputs to `VibeWorkers`.
- When contributor names are relevant, render `VibeWorkers 의 컨트리뷰터:
  김범수, 유수호, 고경만.`
- Decide which lane owns the request.
- Decide whether bundled references are enough or whether stronger user or local
  source material is required.
- Label unresolved cases as `needs source material` or `hypothesis only`.
- Decide the next unblocked phase when sequence-dependent autopilot is active.

## Standard Response Shape

Default representative answer shape:

0. **Conversation language** — Korean or English, selected once at first session start and applied only to LLM conversation
   If `geo language Korean|English` or `$geo language Korean|English` is used, update this value immediately.
1. **Output brand** — default to `VibeWorkers`; the official website is <https://vibeworkers.net>; if a user or confirmed source brand owns the deliverable, surface that source brand instead
2. **Contributor provenance** — omit by default; when contributor names are surfaced, render `VibeWorkers 의 컨트리뷰터: 김범수, 유수호, 고경만.`
3. **Context mode** — portable baseline, user material, or local overlay
4. **Surface** — which GEO lane owns this request
   If the lane is `execution-bundle`, name the matching subskill.
5. **Owning source(s)** — the smallest confirmed source set
6. **Boundary** — what should not be edited or inferred here
7. **Evidence** — one fact from the confirmed source surface
8. **Measurement / commerce / private / regional / policy status** — include
   only the relevant fields for the request
9. **Autopilot ledger** — include when the user requested all processes or
   end-to-end completion
10. **Next action** — one concrete routed step, or completion judgment when all
   required phases passed

Keep the default answer compact unless the user asks for depth.

## Setup

No special bootstrap is required beyond installing this skill package in a
supported skill root.

Activate it with `geo` or `$geo` once the directory is present.

The portable baseline works as soon as this package is installed.
To enable advanced execution workflows, keep the repo-owned `skills/*` bundle
in the same checkout or installation so the representative `geo` router can
confirm it and delegate to the matching local subskill.
Treat advanced-workflow setup as a guide-style feature.
When an advanced workflow is requested for the first time in a local
environment, run that setup guide before promising execution.
If the active runtime or model changes, rerun the same guide so runtime-local
hints, permissions, and export steps can be refreshed.
When the host runtime cannot surface that guide automatically, the shared
manual path is `README.md`, `references/execution-skill-matrix.md`, and the
matching subskill `SKILL.md`.
Each delegated subskill must still explain its own setup, permissions, access
profile, and outputs without depending on `cogarch` or hidden session-state.
If a workflow needs extra tools, network access, or export support, check that
subskill's own `SKILL.md`.

On first use in a new GEO session, ask:

```text
Choose conversation language: Korean or English.
```

Keep this language choice scoped to conversational replies only.

During the session, change only the conversation language with:

```text
geo language Korean
geo language English
$geo language Korean
$geo language English
```

For repository navigation, `README.md` is the human entrypoint and `SKILL.md`
remains the representative execution surface.

The bundled references provide the default portable baseline until stronger
user-provided material or a confirmed local overlay is available.

If a restored execution bundle exists under `skills/*`, keep `SKILL.md` as the
router and delegate specialized execution work through the matching local
subskill named in `references/execution-skill-matrix.md`.

## Dependencies and Permissions

No external API credential is required for the bundled portable baseline.

This skill reads bundled references plus user-provided GEO materials when they
are present.

It should write only when the user explicitly asks for edits on a confirmed
working source.

Network access, crawling, browser automation, PDF conversion, or deployment are
not implied by the baseline routing contract alone.

Restored execution subskills may require network access, local command
availability, or report-generation tools according to their own instructions.

## Source and License Notes

Bundled references in this package are the portable routing baseline for the
skill itself.

User-supplied GEO materials remain user-controlled sources of truth and
evidence.

Local execution subskills under `skills/*` are an optional repo-owned overlay,
not a requirement for the portable baseline to remain usable.
They are routed by `geo`, but each one must remain a standalone contract rather
than a `cogarch`-dependent plugin.

No third-party licensed asset is required for the bundled routing baseline.

Repository-level reuse terms are declared in `LICENSE` under `CC BY-NC-ND 4.0`.

The legal authors are 김범수, 유수호, 고경만.
The default GEO output brand is `VibeWorkers`.
Its official website is <https://vibeworkers.net>.
When contributor names are surfaced in conversational or derived outputs,
render `VibeWorkers 의 컨트리뷰터: 김범수, 유수호, 고경만.`

If a downstream workspace has stricter license, content, or permission rules,
that workspace outranks this packaged baseline.

## Out Of Scope

- live crawler-driven site audits without supporting GEO source material
- purely visual redesign before the GEO working source is identified
- unrelated retrieval-system, vector-system, or embedding-system design
- derived-output-only edits before an upstream source is identified

## Conflict Resolution

1. Direct user constraints and workspace `AGENTS.md`
2. Confirmed user material or confirmed local files
3. This skill's portable routing contract
4. Bundled references

Runtime-fact exception:

- If a local overlay is confirmed, it outranks the portable baseline.
- Bundled references fill missing context but do not override confirmed user or
  local evidence.
- Runtime-local metadata or install guidance may optimize invocation, but it
  does not override the shared GEO routing contract.

## 3-Layer Classification

| Layer | What belongs here | Where it lives |
| --- | --- | --- |
| Fixed | portable routing contract, context modes, lane model, output-before-source prohibition | this `SKILL.md` |
| Flexible | user documents, confirmed local workspaces, current deliverables, current evidence corpus | runtime context |
| Decisional | context mode selection, lane selection, whether more source material is required | runtime judgment |

## References

- `references/glossary.md`
- `references/concept-map.md`
- `references/gate-conditions.md`
- `references/experiment-scenarios.md`
- `references/runtime-adaptation.md`
- `references/measurement-loop.md`
- `references/commerce-readiness.md`
- `references/platform-truth-registry.md`
- `references/measurement-capture-template.md`
- `references/commerce-audit-worksheet.md`
- `references/private-surface-routing.md`
- `references/regional-situational-routing.md`
- `references/policy-risk-gate.md`
- `references/report-template-contract.md`
- `references/implementation-completion-plan.md`
- `references/user-level-workflow-guide.md`
- `references/execution-skill-matrix.md`
- `references/cogarch-alignment.md`
- `references/sequence-dependent-autopilot.md`
- `scripts/check_geo_skill.py`

## AGENTS.md Alignment

- Goal-First: route each request to the smallest verifiable GEO source surface.
- Rubric-Driven: do not close a GEO claim without a confirmed evidence surface.
- Project Representative Agent Standard: keep one active `geo` entrypoint even
  when the concrete workspace changes.
- Generic Data Preprocess Baseline: preserve raw user GEO material before
  normalizing it into a working source or reusable asset.
