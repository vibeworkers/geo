# Changelog

All notable changes to this portable GEO package are recorded here.

Tag format: `X.Y.Z` without a leading `v`.
Historical note: `0.0.1` through `0.0.4` predate the formal protocol in
`references/versioning-protocol.md` and remain immutable.

## Unreleased

No unreleased changes.

## 0.2.0 - 2026-05-06

### Added

- Added `references/runtime-adaptation.md` to separate shared GEO routing rules
  from runtime-specific Codex, Claude, and Gemini adaptation guidance.

### Changed

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
