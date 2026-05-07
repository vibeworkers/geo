# GEO Runtime Adaptation

Use this reference when the request is about Codex, Claude, and Gemini
adaptation behavior for `geo`.

## Shared Portable Core

Keep one shared portable GEO core in `SKILL.md`.

Do not import the full CogArch multi-tool topology into `geo` just to express
runtime differences.

Runtime adaptation must not replace context modes, source-order rules, language
policy, default output-brand rules, output-brand ownership rules, author
attribution, or `skills/*` confirmation.

## Runtime Adaptation Matrix

| Runtime | Adapt here | Keep shared |
| --- | --- | --- |
| Codex / OpenAI | explicit invocation examples, `agents/openai.yaml`, file-path-grounded workspace evidence, response compression shaped for Codex closeouts | routing contract, context modes, source order, default output brand `VibeWorkers`, website `https://vibeworkers.net`, output-brand override boundary, author rules |
| Claude | concise invocation wording, lane restatement, optional runtime-local install note if a Claude surface is added later | routing contract, context modes, source order, default output brand `VibeWorkers`, website `https://vibeworkers.net`, output-brand override boundary, author rules |
| Gemini | concise context packet, next-action restatement, optional runtime-local install note if a Gemini surface is added later | routing contract, context modes, source order, default output brand `VibeWorkers`, website `https://vibeworkers.net`, output-brand override boundary, author rules |

Runtime adaptation may optimize invocation wording, metadata, evidence
packaging, or installation notes.

## Current Shipped Runtime Surfaces

- Codex / OpenAI: `agents/openai.yaml` is bundled today.
- Claude: no runtime-local surface is bundled in this repository yet, so use
  the shared contract in `README.md` and `SKILL.md`.
- Gemini: no runtime-local surface is bundled in this repository yet, so use
  the shared contract in `README.md` and `SKILL.md`.

## First-Use Runtime-Local Onboarding

Runtime-local first-use onboarding may be added only when a runtime exposes a
native metadata, extension, or skill slot.

Use that onboarding as the advanced-workflow setup guide for the first advanced
workflow request in a local environment.

Rerun the same guide when the active runtime or model changes, because
runtime-local hints, permissions, and export steps may differ.

It may add a short first-use guide, invocation wording, installation hints, or
response-shaping help.

If the runtime cannot surface that trigger or runtime/model identity natively,
keep the same setup guide manual in `README.md`,
`references/execution-skill-matrix.md`, and the matching subskill contract.

It must not replace the shared `geo` contract or require `cogarch`, hidden
global files, or a hidden local path.

The shared portable package must remain usable even when no runtime-local
onboarding surface exists.

## Authoring Rule

Update the shared contract first when a rule applies to every runtime.

Create or edit a runtime-local surface only when the delta belongs to invocation
syntax, native metadata, installation guidance, or response-shaping needs.

Do not fork the whole skill package unless `geo` itself later becomes a
cross-tool installer or topology owner.

## Validation Hook

`scripts/check_geo_skill.py` validates that the shared contract and this
runtime-adaptation reference stay aligned.
