# Changelog

All notable changes to this portable GEO package are recorded here.

Tag format: `X.Y.Z` without a leading `v`.
Historical note: `0.0.1` through `0.0.4` predate the formal protocol in
`references/versioning-protocol.md` and remain immutable.

## Unreleased

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
