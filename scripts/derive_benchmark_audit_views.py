#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path


BRANCH_DERIVATION_PURPOSE = (
    "audit split view of branch readiness from the preserved combined "
    "comparison artifact"
)

SITE_DERIVATION_PURPOSE = (
    "audit split view of live site HTTP, head, structure, and crawler-access "
    "evidence from the preserved combined comparison artifact"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Derive audit-only branch and site split JSON views from a preserved "
            "benchmark comparison.json artifact."
        )
    )
    parser.add_argument(
        "comparison_json",
        type=Path,
        help="Path to the combined comparison.json artifact.",
    )
    parser.add_argument(
        "--branch-output",
        type=Path,
        help="Optional output path for branch-readiness.json.",
    )
    parser.add_argument(
        "--site-output",
        type=Path,
        help="Optional output path for site-http-head-snapshot.json.",
    )
    parser.add_argument(
        "--derived-at",
        default=date.today().isoformat(),
        help="Date label to record in the derived artifacts. Defaults to today.",
    )
    return parser.parse_args()


def load_comparison(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    required_keys = {"target", "branches", "site"}
    missing = required_keys.difference(data)
    if missing:
        missing_list = ", ".join(sorted(missing))
        raise SystemExit(f"[error] comparison artifact missing keys: {missing_list}")
    return data


def source_artifact_label(path: Path) -> str:
    if path.parent.name:
        return f"{path.parent.name}/{path.name}"
    return path.name


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    args = parse_args()
    comparison_path = args.comparison_json
    comparison = load_comparison(comparison_path)
    source_artifact = source_artifact_label(comparison_path)

    branch_output = args.branch_output or comparison_path.with_name(
        "branch-readiness.json"
    )
    site_output = args.site_output or comparison_path.with_name(
        "site-http-head-snapshot.json"
    )

    branch_payload = {
        "source_artifact": source_artifact,
        "derived_at": args.derived_at,
        "derivation_purpose": BRANCH_DERIVATION_PURPOSE,
        "target": comparison["target"],
        "branches": comparison["branches"],
    }
    site_payload = {
        "source_artifact": source_artifact,
        "derived_at": args.derived_at,
        "derivation_purpose": SITE_DERIVATION_PURPOSE,
        "site": comparison["site"],
    }

    write_json(branch_output, branch_payload)
    write_json(site_output, site_payload)

    print(f"[ok] wrote {branch_output}")
    print(f"[ok] wrote {site_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
