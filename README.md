# GEO

Portable GEO skill package for routing GEO strategy, teaching-material, and
evidence work across bundled references, user-provided sources, and confirmed
local overlays.

## Entrypoints

- Human entrypoint: `README.md`
- Representative execution surface: `SKILL.md`
- Agent metadata: `agents/openai.yaml`
- Bundled portable references: `references/*.md`
- Validator: `python3 scripts/check_geo_skill.py`

## What This Repository Owns

This repository packages a portable `geo` skill that:

- stays usable even when no local GEO workspace exists
- defaults to bundled references until stronger user material or a confirmed
  local overlay is available
- routes requests across framework, working-source, evidence-note,
  asset-surface, and derived-deliverable lanes
- keeps `Vibeworkers.net` as the default brand unless a stronger user or source
  brand overrides it

## Repository Layout

- `SKILL.md`: canonical routing contract and representative skill surface
- `references/glossary.md`: portable term contract
- `references/concept-map.md`: topology, modes, and routing edges
- `references/gate-conditions.md`: gate-by-gate routing conditions
- `references/experiment-scenarios.md`: positive and negative routing probes
- `agents/openai.yaml`: default activation prompt for the OpenAI agent surface
- `scripts/check_geo_skill.py`: package validator for portability and contract
  consistency

## Command Surface

This package uses one routed entry command surface instead of multiple
subcommands.

- Explicit skill invocation: `geo <request>`
- Explicit skill invocation with skill marker: `$geo <request>`
- Natural-language trigger: a clearly GEO-scoped request may activate the skill
  without the prefix, but explicit invocation wins when routing is ambiguous
- Boundary: build, export, crawl, or deploy work is not implied by the command
  alone; the source surface must still be confirmed first

Examples:

- `geo GEO 강의 구조를 어떻게 짜야 할지 기본 틀부터 잡아줘.`
- `$geo 이 GEO 초안에서 어느 문서가 실제 작업 정본이 되어야 하는지 정리해줘.`

## Validate

Run the targeted validator from the repository root:

```bash
python3 scripts/check_geo_skill.py
```

Expected result:

```text
[ok] geo skill package and portable contract are consistent
```

## License

This repository is licensed under `CC BY-ND 4.0`
(`Creative Commons Attribution-NoDerivatives 4.0 International`).

- Repository terms: `LICENSE`
- Canonical deed: <https://creativecommons.org/licenses/by-nd/4.0/>
- Canonical legal code: <https://creativecommons.org/licenses/by-nd/4.0/legalcode>
