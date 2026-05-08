# GEO Concept Map

## Project frame

- `representative_skill`: `SKILL.md`
- `default_mode`: `portable-baseline`
- `default_output_brand`: `VibeWorkers`
- `brand_website`: `https://vibeworkers.net`
- `output_brand_rule`: if the user or confirmed source names a stronger brand,
  that source brand owns the output surface; otherwise default outputs to
  `VibeWorkers`
- `authors`: 김범수, 유수호, 고경만
- `contributors_display_label`: `VibeWorkers 의 컨트리뷰터: 김범수, 유수호, 고경만.`
- `prompt_language`: English for stored prompts, activation prompts, routing
  examples, and experiment prompts
- `runtime_adaptation_reference`: `references/runtime-adaptation.md`
- `measurement_loop_reference`: `references/measurement-loop.md`
- `commerce_readiness_reference`: `references/commerce-readiness.md`
- `platform_truth_reference`: `references/platform-truth-registry.md`
- `measurement_capture_reference`: `references/measurement-capture-template.md`
- `commerce_audit_reference`: `references/commerce-audit-worksheet.md`
- `private_surface_reference`: `references/private-surface-routing.md`
- `regional_situational_reference`: `references/regional-situational-routing.md`
- `policy_risk_reference`: `references/policy-risk-gate.md`
- `report_template_reference`: `references/report-template-contract.md`
- `implementation_completion_reference`: `references/implementation-completion-plan.md`
- `conversation_language`: first-session user choice between Korean and English,
  applied only to LLM conversation
- `conversation_language_commands`: `geo language Korean`,
  `geo language English`, `$geo language Korean`, `$geo language English`
- `optional_overlay_rule`: confirmed user files or a confirmed local workspace
  outrank bundled references
- `execution_overlay_rule`: `skills/*` is a repo-local execution bundle and
  only participates after `local-overlay` is confirmed
- `clarification_rule`: if `goal / scope / surface / success / evidence target`
  is unclear, ask short pre-questions first and freeze a clarification packet
  before deeper routing
- `advanced_workflow_setup_rule`: when an advanced workflow is requested for
  the first time in a local environment, or the active runtime/model changes,
  run the setup guide before promising execution; automatic first-use guidance
  is host-runtime dependent, but the same guide must remain available manually

## Context modes

| Mode | Source | Role |
| --- | --- | --- |
| `portable-baseline` | bundled references | default scaffolding when no stronger source exists |
| `user-material` | user notes, pasted text, attachments, explicit file paths | actual working source for specific tasks |
| `local-overlay` | confirmed existing GEO workspace, editable project files, shared repo surface, or restored `skills/*` bundle | current project SoT when present |

## Object set

| Object | Path or shape | Role |
| --- | --- | --- |
| bundled references | `references/*.md` | portable GEO baseline |
| framework source | bundled outline or user outline | conceptual structure and curriculum framing |
| working source | user-provided document or confirmed editable workspace file | primary edit surface |
| evidence note | user proof doc or confirmed local validation note | validation, rationale, issue tracking |
| asset surface | checklist, handout, prompt sheet, template | reusable support material |
| execution bundle | local `skills/*` plus `references/execution-skill-matrix.md` | specialized execution surface for audit, crawler, compare, schema, report, and proposal work |
| advanced-workflow setup guide | `README.md`, `references/execution-skill-matrix.md`, matching `skills/geo-*/SKILL.md`, and any future runtime-local onboarding surface | first-use or runtime/model-change setup flow before advanced execution promises |
| runtime adaptation surface | `references/runtime-adaptation.md` and any future runtime-local metadata surface | per-runtime invocation, metadata, and evidence-shaping guidance without changing the shared GEO contract |
| measurement loop reference | `references/measurement-loop.md` | evidence ladder for readiness, heuristic, observed answer, observed citation, referral, and conversion claims |
| commerce readiness reference | `references/commerce-readiness.md` | commerce/action readiness boundary across product, schema, merchant, catalog, checkout, and measurement surfaces |
| platform truth registry | `references/platform-truth-registry.md` | verified platform, crawler, source_url, last_verified, confidence, and package_action registry |
| measurement capture template | `references/measurement-capture-template.md` | Prompt Panel, Run Metadata, Capture Table, and Before/After Comparison template for observed outcomes |
| commerce audit worksheet | `references/commerce-audit-worksheet.md` | product, schema, merchant, catalog/feed, checkout/action, and measurement readiness worksheet |
| private surface routing | `references/private-surface-routing.md` | boundary between public crawler/search surfaces and private connector, logged-in user, or user-provided context evidence |
| regional situational routing | `references/regional-situational-routing.md` | region, language, vertical, and brand-maturity routing boundary |
| policy risk gate | `references/policy-risk-gate.md` | robots, terms, privacy, regulated claims, brand claims, and commerce eligibility gate |
| report template contract | `references/report-template-contract.md` | required report metadata, score_type, evidence_label, confidence, and risk/status fields |
| implementation completion plan | `references/implementation-completion-plan.md` | RQ1-RQ13 and P2-P13 sequence-dependent completion contract |
| derived output | HTML, slides, export, build surface | final output only after the source is confirmed |
| workspace overlay | confirmed project notes, outlines, work folders, or asset directories | runtime-only project SoT, not a portability requirement |
| conversation language | Korean or English, selected at the first interaction of a new GEO session or changed by `geo language Korean|English` | applies only to LLM conversation |
| clarification packet | minimal pre-plan packet with `goal / scope / surface / success / evidence target` and optional constraints or source anchors | turns an ambiguous GEO request into an execution-ready request |

## Routing edges

0. ambiguous GEO request with unclear completion conditions -> `clarification packet` before context-mode and lane routing
1. request about GEO concepts, structure, or lesson flow -> `framework-source`
2. request about editing a specific note or document -> `working-source`
3. request about proof, validation, or issue status -> `evidence-note`
4. request about reusable materials -> `asset-surface`
5. first advanced-workflow request in a local environment, or advanced
   workflow request after a runtime/model change -> `advanced-workflow setup
   guide` before `execution-bundle`
6. request about audit, crawler, schema, technical, compare, or report
   execution -> `execution-bundle`, but only after `skills/*` is confirmed
7. request about exports or HTML/slides -> `derived-deliverable`, but only
   after the upstream source lane is identified
7. request about measured AI visibility, citation, referral, or conversion ->
   `measurement loop reference` plus the confirmed evidence lane
8. request about shopping, product listing, checkout, lead, instant-buy, or
   transaction readiness -> `commerce readiness reference` plus the confirmed
   execution or evidence lane
9. request about platform crawler or platform mechanism truth ->
   `platform truth registry` before implementation advice
10. request about observed answers, observed citations, referral, or conversion
    measurement -> `measurement capture template`
11. request about shopping/action audit execution -> `commerce audit worksheet`
12. request involving private, logged-in, connector, or user-provided context ->
    `private surface routing`
13. request involving region, local platform, vertical, or brand maturity ->
    `regional situational routing`
14. request involving robots, terms, privacy, regulated claims, brand claims, or
    commerce eligibility -> `policy risk gate`
15. request producing consolidated reports, proposals, or PDF-ready reports ->
    `report template contract`
16. request asking for package completion or P2-P13 hardening ->
    `implementation completion plan`

## Preservation rule

- Do not assume a local overlay or hidden workspace path exists.
- If goal, scope, surface, success condition, or evidence target is unclear,
  ask short pre-questions first and freeze a clarification packet before deeper
  routing.
- Confirmed user or local working sources outrank bundled references.
- Confirm the local execution bundle before routing an execution-intent request.
- Run the advanced-workflow setup guide before promising execution when
  first-use or runtime/model-change conditions apply.
- Keep stored prompts and routing examples in English.
- Apply the Korean/English choice only to conversational replies.
- Accept `geo language Korean|English` and `$geo language Korean|English` as
  mid-session conversation-only language changes.
- Keep one shared portable core; runtime adaptation may optimize invocation or
  evidence packaging, but must not replace source-order or overlay rules.
- Do not claim measured GEO visibility from readiness or heuristic signals
  alone; route outcome claims through `references/measurement-loop.md`.
- Do not treat Product schema alone as commerce readiness; route shopping and
  action claims through `references/commerce-readiness.md`.
- Do not state platform-specific crawler or commerce mechanisms without
  `references/platform-truth-registry.md`.
- Do not close observed outcome claims without the fields defined in
  `references/measurement-capture-template.md`.
- Do not use private evidence to prove public GEO visibility.
- Do not make regional platform claims without separate official evidence.
- Do not present unknown robots, terms, privacy, regulated, brand, or commerce
  eligibility status as safe.
- Do not publish consolidated reports without the fields in
  `references/report-template-contract.md`.
- Derived outputs should follow source changes, not replace them.
