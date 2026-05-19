# Changelog

All notable changes to this portable GEO package are recorded here.

Tag format: `X.Y.Z` without a leading `v`.
Historical note: `0.0.1` through `0.0.4` predate the formal protocol in
`references/versioning-protocol.md` and remain immutable.

## Unreleased

## 0.11.0 - 2026-05-19

- Added `references/cogarch-alignment.md` as a portable governance alignment
  contract that borrows evidence closure, owner split, actor-first handoff, and
  knowledge-packet discipline without introducing a runtime dependency on
  `cogarch`, `~/.cogarch`, or `OPERATIONS.md`.
- Expanded the GEO report contract with a claim-boundary ledger and
  actor-first handoff section so measured facts, interpretation, assumptions,
  unknowns, and next-action ownership stay separable.
- Wired the new alignment reference into `SKILL.md`, `README.md`,
  `references/execution-skill-matrix.md`, and `scripts/check_geo_skill.py`.
- Added `references/sequence-dependent-autopilot.md` so all-in requests such
  as `전부 해줘`, `전체 진행`, and `do everything` run through an ordered
  dependency graph, phase verification, ledger recording, and completion
  judgment instead of stopping at a plan.
- Added validator-backed organic capability composition for
  `packages/geo-deep-audit-ecommerce/` and `packages/geo-seo-skills-kr2/`, and
  wired the root validator to delegate to those package contracts.
- Added explicit `fixed / flexible / decisional` classification sections to the
  deep-audit-ecommerce and KR2 package surfaces so package-level source of
  truth, runtime judgment, and evidence boundaries are predictable.
- Removed machine-local KR2 `00_tunnel` path assumptions from capability docs
  and replaced them with the `GEO_TUNNEL_ROOT` runtime hint plus validator
  enforcement.

## 0.10.0 - 2026-05-12

- Added a user-level workflow guide distilled from the older
  `geo-seo-skills-kr` onboarding docs, preserving manager/operator/builder
  output guidance without restoring hidden slash-command session state.
- Added platform-truth, measurement-loop, commerce-readiness, private-surface,
  regional/situational, policy-risk, report-template, and implementation
  completion reference contracts so GEO claims separate readiness, heuristic,
  observed answer/citation, referral, conversion, and unresolved risk.
- Corrected platform crawler guidance for OpenAI, Google, and Anthropic:
  `OAI-SearchBot`, `GPTBot`, `ChatGPT-User`, `ClaudeBot`,
  `Claude-SearchBot`, and `Claude-User` are separated by role; `Googlebot`
  remains the Google Search crawler surface, while `Google-Extended` is not
  treated as a Google Search inclusion or ranking control.
- Marked Grok-related crawler controls as requiring first-party verification
  before platform-specific implementation advice.
- Aligned audit, crawler, platform optimizer, schema, prospect, proposal,
  report, and PDF-report subskills around confidence labels, evidence paths,
  report metadata, commerce/action readiness, and no-overclaim boundaries.
- Expanded `scripts/check_geo_skill.py` to validate the new reference contracts,
  subskill reference wiring, portability scans, and stale platform-truth
  regressions.

## 0.9.1 - 2026-05-08

- Clarified that GEO release versions always use the three-part `X.Y.Z` form,
  and that the active pre-1.0 line is still a three-part `0.Y.Z` structure.

## 0.9.0 - 2026-05-08

- Refined the versioning boundary so auxiliary GitHub-sharing and social-preview
  surfaces do not automatically force a `minor` bump when the routed GEO
  contract, required portable artifacts, runtime adaptation, and release
  procedure remain unchanged.

## 0.8.0 - 2026-05-07

- Added English and Korean introduction images to `README.md`, plus a
  Pages-ready `docs/` sharing surface with Open Graph and schema.org metadata
  for GitHub-hosted project previews.

## 0.7.0 - 2026-05-07

- Reframed the README summary around the GEO problems this package helps solve,
  and added clearer user-facing guidance for runtime compatibility plus
  model-specific setup and optimization hints.

## 0.6.0 - 2026-05-07

- Added a short user-facing capability summary and a concise system overview to
  `README.md`, including a feature-list style summary plus
  `generateSkill`/Cognitive-Architecture based system notes and the
  representative GEO routing structure.

## 0.5.0 - 2026-05-07

- Clarified that `VibeWorkers` is the default GEO output brand and
  `https://vibeworkers.net` is the brand website; outputs use a stronger user
  or confirmed source brand only when that source owns the deliverable.
- Aligned `README.md`, `SKILL.md`, `agents/openai.yaml`, bundled references,
  and `scripts/check_geo_skill.py` around the corrected default-brand and brand
  website contract.

## 0.4.0 - 2026-05-07

- Added user-facing runtime compatibility guidance to `README.md` so
  Codex/ChatGPT, Claude, and Gemini users can see the shared GEO contract and
  current runtime-specific boundary at first read.
- Clarified in `SKILL.md`, `references/runtime-adaptation.md`, and
  `scripts/check_geo_skill.py` that the current shipped runtime-local surface
  is `agents/openai.yaml`, while Claude/Gemini first-use onboarding remains
  optional and host-runtime dependent.
- Added advanced-workflow troubleshooting guidance to `README.md` and
  `references/execution-skill-matrix.md` so users can recover when `skills/*`,
  workflow selection, clarification questions, or local setup requirements block
  execution.
- Reframed advanced-workflow setup as a guide-style first-run feature that runs
  before execution in a local environment and reruns when the active runtime or
  model changes, with manual fallback when host-native onboarding is absent.
- Softened `README.md` advanced-workflow wording so the root guide stays
  user-facing while stronger hidden-dependency and runtime-contract language
  remains in `SKILL.md` and `references/execution-skill-matrix.md`.

## 0.3.0 - 2026-05-07

### Changed

- Refocused `README.md` on user-facing project introduction and usage guidance.
- Removed maintainer-oriented release and internal routing detail from
  `README.md`.
- Added user-facing setup guidance for enabling advanced workflows from the
  bundled `skills/*` execution bundle.
- Declared that `skills/geo-*` subskills are standalone workflow owners routed
  by `geo`, not `cogarch`-dependent plugins.
- Removed hidden `/geo level` session-state dependence from the restored
  execution subskill contract.
- Removed leftover `/geo ...` slash-command examples from restored execution
  subskills so they now describe direct inputs or plain-language GEO requests.
- Imported a clarification-first pre-question intake so `geo` now locks
  completion conditions before planning ambiguous requests.
- Updated `scripts/check_geo_skill.py` so README validation now enforces the
  user-facing intro and usage contract.
- Expanded `README.md` with step-by-step installation, feature-by-feature
  usage guidance, workflow timing examples, and package provenance for the
  private `generateSkill` creation workflow.
- Changed the repository license from `CC BY-ND 4.0` to `CC BY-NC-ND 4.0` and
  aligned `LICENSE`, `README.md`, `SKILL.md`, and validator expectations.

## 0.2.0 - 2026-05-06

### Added

- Added `references/runtime-adaptation.md` to separate shared GEO routing rules
  from runtime-specific Codex, Claude, and Gemini adaptation guidance.

### Changed

- Documented the human-entrypoint rule so `README.md` must be refreshed when
  release-impacting entrypoint or contract surfaces change.
- Expanded `README.md` so the project introduction now explains the GEO
  package purpose, background, core capabilities, and representative use cases
  in both English and Korean.
- Standardized the default brand token as `VibeWorkers.net` and aligned the
  contributor provenance label across the bundled contract surfaces.
- Expanded `scripts/check_geo_skill.py` so the validator now enforces the
  runtime-adaptation reference and contributor-display contract.

## 0.1.0 - 2026-05-06

### Added

- Formal versioning protocol for the portable GEO package under
  `references/versioning-protocol.md`.
- Mandatory release-decision gate script under
  `scripts/check_geo_release.py`.

### Changed

- `README.md` now points to the versioning protocol and release history.
- `scripts/check_geo_skill.py` now validates the presence of the versioning
  protocol, changelog anchors, and release gate script.
- Release approval now requires the protocol gate unconditionally.

## 0.0.4 - 2026-05-06

### Changed

- Restored the repo-local GEO execution bundle under `skills/*`.
- Added `references/execution-skill-matrix.md` and aligned the representative
  surfaces with the restored execution bundle.
- Expanded the validator and language-control documentation across the package
  surfaces.

## 0.0.3 - 2026-05-06

### Changed

- Added bilingual README support so the human entrypoint remains English first
  and Korean second.

## 0.0.2 - 2026-05-06

### Changed

- Documented the routed `geo` command surface and clarified invocation
  behavior.

## 0.0.1 - 2026-05-06

### Added

- Prepared the initial documentation release with `README.md`, `SKILL.md`,
  `LICENSE`, and `scripts/check_geo_skill.py`.
