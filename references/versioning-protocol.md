# GEO Versioning Protocol

## Scope

This repository versions one portable GEO package.
The version applies to the documented package contract as a whole, not to one
file in isolation.

The public package surface for versioning purposes is:

- `README.md`
- `SKILL.md`
- `agents/openai.yaml`
- `references/*.md`
- `skills/*/SKILL.md`
- `scripts/check_geo_skill.py`
- `scripts/check_geo_release.py`
- `LICENSE`
- `CHANGELOG.md`

In Semantic Versioning terms, this documented package contract is the public
API for the repository.
`README.md` is the human entrypoint for that public API and should be refreshed
when release-impacting contract surfaces change.

## Canonical Version Sources

Read version state in this order:

1. git tag on the release commit
2. matching section in `CHANGELOG.md`
3. the release commit on `main`

If these sources disagree, the git tag wins.

## Tag Format and Tag Type

- Tag format: `X.Y.Z` without a leading `v`
- Pre-release format: `X.Y.Z-rc.N` or `X.Y.Z-beta.N`
- New release tags should be annotated tags
- Released tags are immutable and must never be moved or rewritten

Historical tags `0.0.1` through `0.0.4` predate this protocol and remain
immutable even though they mix annotated and lightweight tag styles.

## Branch Roles

- `main` is the release line
- `codex/<topic>` is the default short-lived working branch shape for
  non-trivial changes
- final release tags are created only from validated commits already on `main`
- experimental or review branches may use pre-release tags, but normal release
  tags must wait for `main`

## Pre-1.0 Policy

This package is still in the `0.y.z` phase.
Start the protocol-governed line at `0.1.0`.

Use `0.Y.Z` with these rules:

- bump `Z` for backward-compatible clarifications and fixes that do not require
  consumers to change invocation, expected outputs, required files, routing
  decisions, or release procedures
- bump `Y` and reset `Z` to `0` when the public package contract changes in a
  way that consumers, maintainers, or downstream automations need to notice

Treat the following as `minor` changes while the major version is zero:

- adding, removing, or renaming bundled references
- adding, removing, or renaming execution subskills under `skills/*`
- changing the routed command surface or conversation-language commands
- changing prompt-language, brand-default, or routing-lane rules
- changing validator-enforced required files, required sections, or required
  phrases
- changing the release checklist or version source priority

Treat the following as `patch` changes while the major version is zero:

- wording clarification without contract meaning drift
- typo fixes
- validator fixes that only repair incorrect enforcement of the existing
  contract
- changelog corrections that do not alter the meaning of a released version

## 1.0.0 Promotion Rule

Promote to `1.0.0` when all of the following are true:

- the routed `geo` entry command and language commands are considered stable
- the representative package layout is expected to remain compatible for
  downstream use
- the restored execution bundle set is intentionally curated instead of still
  moving rapidly
- validator rules are stable enough that consumers can depend on them as a
  published contract

Once `1.0.0` exists, follow standard Semantic Versioning:

- major for incompatible public contract changes
- minor for backward-compatible additions
- patch for backward-compatible fixes

## Release Checklist

1. Identify the highest changed public surface in this repository.
2. Choose the next version according to this protocol.
3. Update `CHANGELOG.md` in the same change set as the release-impacting
   changes.
4. Refresh `README.md` in the same change set when entrypoints, defaults,
   required references/scripts, or other release-impacting human-facing
   contract surfaces changed.
5. Run `python3 scripts/check_geo_skill.py`.
6. Review the staged diff to confirm the release scope matches the chosen bump.
7. Merge the validated change to `main`.
8. Create an annotated tag that matches the changelog heading.

## Release Decision Gate

Release judgment is not discretionary in this repository.
A release decision is valid only if `python3 scripts/check_geo_release.py
<target-version>` passes from the repository root.

No exception, waiver, verbal approval, or ad hoc interpretation can replace
this gate.
If the gate fails, the release decision is `blocked`, not `approved with
caveats`.

The release decision gate validates at least these conditions:

- current branch is `main`
- the worktree is clean
- the target version matches `X.Y.Z` without a leading `v`
- the target version is the next allowed bump from the latest normal release
  tag under this protocol
- `CHANGELOG.md` contains either a dated target section or non-empty
  `Unreleased` notes
- `README.md` is updated when release-impacting entrypoint or contract surfaces
  changed since the latest normal release tag
- `python3 scripts/check_geo_skill.py` passes

This gate is for normal release approval.
Pre-release experimentation such as `-rc.N` or `-beta.N` does not count as
final release approval.

## Non-Release Changes

Do not create a new version for work that never becomes part of the repository
contract, such as local scratch notes, abandoned experiments, or unmerged
review branches.

## Historical Baseline

The pre-protocol release history currently visible in git is:

- `0.0.1`: initial documentation release
- `0.0.2`: routed command surface documentation
- `0.0.3`: bilingual README support
- `0.0.4`: restored execution bundle and language controls

The next release after adopting this protocol should start at `0.1.0`, not at
`0.0.5`.

## Reference

- Semantic Versioning 2.0.0: <https://semver.org/>
