# GEO Concept Map

## Project frame

- `representative_skill`: `SKILL.md`
- `default_mode`: `portable-baseline`
- `default_brand`: `Vibeworkers.net`, unless the user or confirmed source
  names a stronger brand
- `optional_overlay_rule`: confirmed user files or a confirmed local workspace
  outrank bundled references

## Context modes

| Mode | Source | Role |
| --- | --- | --- |
| `portable-baseline` | bundled references | default scaffolding when no stronger source exists |
| `user-material` | user notes, pasted text, attachments, explicit file paths | actual working source for specific tasks |
| `local-overlay` | confirmed existing GEO workspace, editable project files, or shared repo surface | current project SoT when present |

## Object set

| Object | Path or shape | Role |
| --- | --- | --- |
| bundled references | `references/*.md` | portable GEO baseline |
| framework source | bundled outline or user outline | conceptual structure and curriculum framing |
| working source | user-provided document or confirmed editable workspace file | primary edit surface |
| evidence note | user proof doc or confirmed local validation note | validation, rationale, issue tracking |
| asset surface | checklist, handout, prompt sheet, template | reusable support material |
| derived output | HTML, slides, export, build surface | final output only after the source is confirmed |
| workspace overlay | confirmed project notes, outlines, work folders, or asset directories | runtime-only project SoT, not a portability requirement |

## Routing edges

1. request about GEO concepts, structure, or lesson flow -> `framework-source`
2. request about editing a specific note or document -> `working-source`
3. request about proof, validation, or issue status -> `evidence-note`
4. request about reusable materials -> `asset-surface`
5. request about exports or HTML/slides -> `derived-deliverable`, but only
   after the upstream source lane is identified

## Preservation rule

- Do not assume a local overlay or hidden workspace path exists.
- Confirmed user or local working sources outrank bundled references.
- Derived outputs should follow source changes, not replace them.
