#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def summarize(path: Path) -> dict[str, object]:
    rows = load_rows(path)
    ranked = sorted(rows, key=lambda row: int(row["overall"]), reverse=True)
    return {
        "source": str(path),
        "site_count": len(ranked),
        "ranking": [
            {
                "rank": index + 1,
                "site": row["site"],
                "url": row["url"],
                "overall": int(row["overall"]),
                "grade": row["grade"],
                "top_issue": row["top_issue"],
                "top_action": row["top_action"],
            }
            for index, row in enumerate(ranked)
        ],
        "score_fields": [
            "crawler_access",
            "citability",
            "content_quality",
            "technical_seo",
            "structured_data",
            "platform_optimization",
        ],
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: summarize_scorecard.py <audit_scorecard.csv>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"Scorecard not found: {path}", file=sys.stderr)
        return 1
    print(json.dumps(summarize(path), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
