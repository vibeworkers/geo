# GEO Runtime Adaptation

Use this reference when the request is about Codex, Claude, and Gemini
adaptation behavior for `geo`.

## Shared Portable Core

Keep one shared portable GEO core in `SKILL.md`.

Do not import the full CogArch multi-tool topology into `geo` just to express
runtime differences.

Runtime adaptation must not replace context modes, source-order rules, language
policy, brand defaults, author attribution, or `skills/*` confirmation.

## Runtime Adaptation Matrix

| Runtime | Adapt here | Keep shared |
| --- | --- | --- |
| Codex / OpenAI | explicit invocation examples, `agents/openai.yaml`, file-path-grounded workspace evidence, response compression shaped for Codex closeouts | routing contract, context modes, source order, brand and author rules |
| Claude | concise invocation wording, lane restatement, optional runtime-local install note if a Claude surface is added later | routing contract, context modes, source order, brand and author rules |
| Gemini | concise context packet, next-action restatement, optional runtime-local install note if a Gemini surface is added later | routing contract, context modes, source order, brand and author rules |

Runtime adaptation may optimize invocation wording, metadata, evidence
packaging, or installation notes.

## Authoring Rule

Update the shared contract first when a rule applies to every runtime.

Create or edit a runtime-local surface only when the delta belongs to invocation
syntax, native metadata, installation guidance, or response-shaping needs.

Do not fork the whole skill package unless `geo` itself later becomes a
cross-tool installer or topology owner.

## Validation Hook

`scripts/check_geo_skill.py` validates that the shared contract and this
runtime-adaptation reference stay aligned.
