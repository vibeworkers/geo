#!/usr/bin/env python3

from __future__ import annotations

import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


SEMVER_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")


@dataclass(frozen=True, order=True)
class Version:
    major: int
    minor: int
    patch: int


def fail(message: str) -> None:
    print(f"[fail] {message}")
    raise SystemExit(1)


def ok(message: str) -> None:
    print(f"[ok] {message}")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing file: {path}")
    except OSError as exc:
        fail(f"could not read {path}: {exc}")


def git_output(repo_root: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", *args],
        cwd=repo_root,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        detail = completed.stderr.strip() or completed.stdout.strip()
        fail(f"git {' '.join(args)} failed: {detail}")
    return completed.stdout.strip()


def parse_version(raw: str) -> Version:
    match = SEMVER_RE.fullmatch(raw)
    if not match:
        fail("target version must match X.Y.Z without a leading v")
    return Version(*(int(part) for part in match.groups()))


def latest_release_tag(repo_root: Path) -> tuple[str, Version]:
    raw = git_output(repo_root, "tag", "--list", "--sort=-version:refname")
    for line in raw.splitlines():
        tag = line.strip()
        if not tag:
            continue
        if SEMVER_RE.fullmatch(tag):
            return tag, parse_version(tag)
    fail("no normal release tag found in git")


def ensure_branch_is_main(repo_root: Path) -> None:
    branch = git_output(repo_root, "rev-parse", "--abbrev-ref", "HEAD")
    if branch != "main":
        fail(f"release decision requires branch main, found {branch}")
    ok("branch is main")


def ensure_clean_worktree(repo_root: Path) -> None:
    status = git_output(repo_root, "status", "--porcelain")
    if status:
        fail("release decision requires a clean worktree")
    ok("worktree is clean")


def ensure_tag_does_not_exist(repo_root: Path, target_version: str) -> None:
    existing = git_output(repo_root, "tag", "--list", target_version)
    if existing:
        fail(f"target tag already exists: {target_version}")
    ok(f"target tag is new: {target_version}")


def classify_bump(latest: Version, target: Version) -> str:
    if latest.major == 0:
        if target == Version(0, latest.minor, latest.patch + 1):
            return "patch"
        if target == Version(0, latest.minor + 1, 0):
            return "minor"
        if target == Version(1, 0, 0):
            return "major"
        fail(
            "pre-1.0 release must be the next patch, the next minor, or 1.0.0"
        )

    if target == Version(latest.major, latest.minor, latest.patch + 1):
        return "patch"
    if target == Version(latest.major, latest.minor + 1, 0):
        return "minor"
    if target == Version(latest.major + 1, 0, 0):
        return "major"
    fail("target version does not match the next allowed semantic bump")


def extract_section_body(text: str, heading: str) -> str | None:
    pattern = re.compile(
        rf"(?ms)^## {re.escape(heading)}\n(.*?)(?=^## |\Z)"
    )
    match = pattern.search(text)
    return match.group(1) if match else None


def ensure_release_notes(changelog_text: str, target_version: str) -> None:
    target_section = re.search(
        rf"(?m)^## {re.escape(target_version)} - \d{{4}}-\d{{2}}-\d{{2}}$",
        changelog_text,
    )
    if target_section:
        ok(f"CHANGELOG contains a dated target section for {target_version}")
        return

    unreleased_body = extract_section_body(changelog_text, "Unreleased")
    if unreleased_body is None:
        fail("CHANGELOG must contain an Unreleased section or a dated target section")
    if not re.search(r"(?m)^- ", unreleased_body):
        fail("CHANGELOG Unreleased section must contain at least one bullet")
    ok("CHANGELOG contains non-empty Unreleased release notes")


def ensure_skill_validator_passes(repo_root: Path) -> None:
    script_path = repo_root / "scripts" / "check_geo_skill.py"
    completed = subprocess.run(
        ["python3", str(script_path)],
        cwd=repo_root,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        detail = (completed.stdout + completed.stderr).strip()
        fail(f"check_geo_skill.py failed: {detail}")
    ok("check_geo_skill.py passed")


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: check_geo_release.py <target-version>")

    repo_root = Path(__file__).resolve().parents[1]
    target_version_raw = sys.argv[1]
    changelog_path = repo_root / "CHANGELOG.md"
    protocol_path = repo_root / "references" / "versioning-protocol.md"

    target_version = parse_version(target_version_raw)
    latest_tag_raw, latest_version = latest_release_tag(repo_root)
    bump_kind = classify_bump(latest_version, target_version)

    if not protocol_path.exists():
        fail("missing versioning protocol")
    if not changelog_path.exists():
        fail("missing changelog")

    ensure_branch_is_main(repo_root)
    ensure_clean_worktree(repo_root)
    ensure_tag_does_not_exist(repo_root, target_version_raw)
    ok(f"latest release tag is {latest_tag_raw}")
    ok(f"target version {target_version_raw} is the next {bump_kind} bump")
    ensure_release_notes(read_text(changelog_path), target_version_raw)
    ensure_skill_validator_passes(repo_root)
    ok(f"release decision passed for {target_version_raw}")


if __name__ == "__main__":
    main()
