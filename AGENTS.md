# GEO Root Guidelines

This root is the portable GEO skill package checkout. Keep root guidance
focused on the portable routing contract, bundled reference integrity, and the
optional advanced subskill bundle.

Representative surface: `SKILL.md`

## Structure & Scope

- `README.md` defines the portable package purpose and advanced workflow entry.
- `SKILL.md` is the representative skill surface and routing contract.
- `references/` holds the bundled baseline source of truth.
- `skills/` holds optional advanced execution subskills.
- `agents/openai.yaml` holds runtime metadata.

## Working Rules

- Keep the portable routing contract in `SKILL.md` and do not fork it into
  hidden machine-local assumptions.
- Route advanced execution work only when the needed subskill exists under
  `skills/`.
- Keep the bundled references and runtime metadata aligned with `SKILL.md`.

## Build, Test, and Validation

- Run `python3 scripts/check_geo_skill.py` after contract or reference changes.
- Use `python3 scripts/check_geo_release.py <target-version>` only for release
  decisions on a clean `main` branch.
- Prefer the smallest validation command that matches the surface you changed.
