# GEO Gate Conditions

## Gate 0: Conversation language selection

- Entry condition: a new GEO session starts and no conversation language has
  been selected, or the user invokes `geo language Korean`,
  `geo language English`, `$geo language Korean`, or `$geo language English`.
- Exit condition: the user chooses exactly one option, Korean or English, or
  the valid language command immediately switches the conversation language.
- Fail condition: the language choice is applied to stored prompts, routing
  examples, source evidence, code, or schema snippets instead of conversation
  only.

## Gate 1: GEO-domain trigger

- Entry condition: the request is about GEO strategy, GEO teaching material,
  GEO evidence, GEO assets, or GEO deliverables.
- Exit condition: the request is accepted into a GEO routing flow.
- Fail condition: the request is unrelated to GEO or belongs to a different
  design/system domain.

## Gate 2: Clarification-first intake

- Entry condition: GEO-domain trigger passed and goal, scope, working surface,
  success condition, or evidence target is still unclear.
- Exit condition: the smallest pre-question set is asked and a clarification
  packet with `goal / scope / surface / success / evidence target` is locked.
- Fail condition: deeper routing, edits, or execution promises start before the
  request becomes execution-ready.

## Gate 3: Context mode selection

- Entry condition: GEO-domain trigger passed and the request is execution-ready,
  either directly or through Gate 2.
- Exit condition: the request is classified as `portable-baseline`,
  `user-material`, or `local-overlay`.
- Fail condition: the response assumes a local workspace or misses a stronger
  user-provided source.

## Gate 4: Owning surface selection

- Entry condition: context mode is known.
- Exit condition: the request is mapped to `framework-source`,
  `working-source`, `evidence-note`, `asset-surface`, `execution-bundle`, or
  `derived-deliverable`.
- Fail condition: the request mixes surfaces without a lead lane.

## Gate 5: Source-order protection

- Entry condition: an owning surface is selected.
- Exit condition: the workflow preserves `confirmed working source ->
  supporting evidence or framework -> derived output`.
- Fail condition: the workflow jumps straight to an export or invents a source.

## Gate 6: Derived-output readiness

- Entry condition: the request touches `execution-bundle` or a
  `derived-deliverable`.
- Exit condition: if this is the first advanced-workflow request in the local
  environment, or the active runtime or model changed, the advanced-workflow
  setup guide is run or the manual guide path is surfaced first; then the
  matching local subskill or build/export preconditions are either confirmed or
  explicitly marked as missing.
- Fail condition: the response promises a refresh without checking
  prerequisites, skips the setup-guide pass when first-use or runtime/model
  change conditions apply, or claims a local execution workflow without
  confirming `skills/*`.

## Gate 7: Evidence closure

- Entry condition: the answer or change plan is ready.
- Exit condition: at least one confirmed source surface proves the claim.
- Fail condition: the response closes with generic GEO commentary only.

## Gate 8: Measurement confidence boundary

- Entry condition: the request asks whether GEO worked, whether an AI answer
  includes or cites a brand/page, or whether referral/conversion changed.
- Exit condition: the claim is labeled with the evidence ladder in
  `references/measurement-loop.md`: readiness, heuristic, observed answer,
  observed citation, referral, or conversion.
- Fail condition: readiness scores, crawler access, schema validity, or
  `llms.txt` presence are reported as measured AI visibility.

## Gate 9: Commerce/action readiness boundary

- Entry condition: the request touches shopping, product listings, checkout,
  lead generation, instant-buy, or transaction/action readiness.
- Exit condition: the answer separates product, schema, merchant, catalog,
  checkout/action, and measurement readiness using
  `references/commerce-readiness.md`.
- Fail condition: Product schema alone is treated as commerce readiness or as
  proof of platform transaction eligibility.

## Gate 10: Private surface boundary

- Entry condition: the request uses logged-in browsing, private connector data,
  user-provided files, personalized context, or evidence that is not public.
- Exit condition: the answer separates public crawler, public search, private
  connector, logged-in user, and user-provided context surfaces using
  `references/private-surface-routing.md`.
- Fail condition: private connector or logged-in evidence is used as proof of
  public GEO visibility.

## Gate 11: Regional/situational boundary

- Entry condition: the request names a region, language market, local platform,
  regulated vertical, or brand maturity condition.
- Exit condition: the answer uses `references/regional-situational-routing.md`
  and regional or vertical claims must use a confirmed source pack.
- Fail condition: platform-specific Naver, Kakao, Daum, or regulated-vertical
  mechanisms are invented from the portable baseline alone.

## Gate 12: Policy risk boundary

- Entry condition: the recommendation touches crawler directives, scraping,
  private evidence, regulated topics, brand claims, or transaction eligibility.
- Exit condition: robots, terms, privacy, regulated claims, brand claims, and
  commerce eligibility are checked with `references/policy-risk-gate.md`.
- Fail condition: unknown policy status is presented as safe or approved.

## Gate 13: Whole-system completion boundary

- Entry condition: the request asks for broad hardening, multi-surface
  implementation, package completion, or a final completion judgment.
- Exit condition: the report records `system_scope`,
  `completion_rubric_path_or_inline`, `current_score`, `all_must_passed` or
  `failed_must_queue`, `verification_set`, and `report_artifact_path`.
- Fail condition: completion is declared while a Must condition has no
  evidence.
