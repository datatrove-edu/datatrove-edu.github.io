#!/usr/bin/env python3
import os, sys, yaml, re

ALLOW_PATH = "data/allowed-tags.yaml"
CONTENT_DIR = "content"

with open(ALLOW_PATH, "r", encoding="utf-8") as f:
    allowed = set(yaml.safe_load(f)["allowed"])

def front_matter(path):
    with open(path, "r", encoding="utf-8") as f:
        txt = f.read()
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", txt, re.S)
    if not m:
        return {}
    return yaml.safe_load(m.group(1)) or {}

bad = []
for root, _, files in os.walk(CONTENT_DIR):
    for name in files:
        if not name.endswith(".md"):
            continue
        p = os.path.join(root, name)
        fm = front_matter(p)
        tags = fm.get("tags", []) or []
        illegal = [t for t in tags if t not in allowed]
        if illegal:
            bad.append((p, illegal))

if bad:
    print("❌ Invalid tags detected (not in data/allowed-tags.yaml):")
    for p, illegal in bad:
        print(f" - {p}: {', '.join(illegal)}")
    sys.exit(1)

print("✅ Tags OK")
