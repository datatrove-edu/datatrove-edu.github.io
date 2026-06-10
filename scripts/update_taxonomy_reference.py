#!/usr/bin/env python3
"""Regenerate reference files listing taxonomy values currently in use.

Run this after adding new tags/topics/functions/math_topics to entries.
Writes data/allowed_tags.yaml, data/allowed_topics.yaml,
data/allowed_functions.yaml and data/allowed_math_topics.yaml — each a sorted
list of values already used somewhere, for collaborators to check before
inventing a new (possibly duplicate) value. These files are reference-only
and are not enforced by CI.
"""
import glob
import os
import re

import yaml

FIELDS = ["tags", "topics", "functions", "math_topics"]
OUTPUT_DIR = "data"


def collect_values():
    values = {field: set() for field in FIELDS}
    for path in glob.glob("content/entries/*/index.md"):
        text = open(path, encoding="utf-8").read()
        m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
        if not m:
            continue
        fm = yaml.safe_load(m.group(1)) or {}
        for field in FIELDS:
            values[field].update(fm.get(field, []) or [])
    return {field: sorted(v) for field, v in values.items()}


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    values = collect_values()
    for field, items in values.items():
        out_path = os.path.join(OUTPUT_DIR, f"allowed_{field}.yaml")
        with open(out_path, "w", encoding="utf-8") as f:
            yaml.dump(items, f, default_flow_style=False, allow_unicode=True)
        print(f"Wrote {out_path} ({len(items)} values)")


if __name__ == "__main__":
    main()
