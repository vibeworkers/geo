# GEO Concept Map

## Project frame

- `representative_skill`: `SKILL.md`
- `default_mode`: `portable-baseline`
- `default_brand`: `VibeWorkers.net`, unless the user or confirmed source
  names a stronger brand
- `authors`: 김범수, 유수호, 고경만
- `contributors_display_label`: `VibeWorkers.net 의 컨트리뷰터: 김범수, 유수호, 고경만.`
- `prompt_language`: English for stored prompts, activation prompts, routing
  examples, and experiment prompts
- `runtime_adaptation_reference`: `references/runtime-adaptation.md`
- `conversation_language`: first-session user choice between Korean and English,
  applied only to LLM conversation
- `conversation_language_commands`: `geo language Korean`,
  `geo language English`, `$geo language Korean`, `$geo language English`
- `optional_overlay_rule`: confirmed user files or a confirmed local workspace
  outrank bundled references
- `execution_overlay_rule`: `skills/*` is a repo-local execution bundle and
  only participates after `local-overlay` is confirmed

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
| runtime adaptation surface | `references/runtime-adaptation.md` and any future runtime-local metadata surface | per-runtime invocation, metadata, and evidence-shaping guidance without changing the shared GEO contract |
| derived output | HTML, slides, export, build surface | final output only after the source is confirmed |
| workspace overlay | confirmed project notes, outlines, work folders, or asset directories | runtime-only project SoT, not a portability requirement |
| conversation language | Korean or English, selected at the first interaction of a new GEO session or changed by `geo language Korean|English` | applies only to LLM conversation |

## Routing edges

1. request about GEO concepts, structure, or lesson flow -> `framework-source`
2. request about editing a specific note or document -> `working-source`
3. request about proof, validation, or issue status -> `evidence-note`
4. request about reusable materials -> `asset-surface`
5. request about audit, crawler, schema, technical, compare, or report
   execution -> `execution-bundle`, but only after `skills/*` is confirmed
6. request about exports or HTML/slides -> `derived-deliverable`, but only
   after the upstream source lane is identified

## Preservation rule

- Do not assume a local overlay or hidden workspace path exists.
- Confirmed user or local working sources outrank bundled references.
- Confirm the local execution bundle before routing an execution-intent request.
- Keep stored prompts and routing examples in English.
- Apply the Korean/English choice only to conversational replies.
- Accept `geo language Korean|English` and `$geo language Korean|English` as
  mid-session conversation-only language changes.
- Keep one shared portable core; runtime adaptation may optimize invocation or
  evidence packaging, but must not replace source-order or overlay rules.
- Derived outputs should follow source changes, not replace them.
