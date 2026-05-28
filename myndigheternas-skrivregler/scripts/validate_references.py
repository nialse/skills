#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

from pathlib import Path
import json
import re
import sys

root = Path(__file__).resolve().parents[1]
source_path = root / "references" / "source-map.md"
problems = []

for path in sorted(root.rglob("*.md")):
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if re.match(r"^(https?|mailto):", target) or target.startswith("#"):
            continue
        target_path = target.split("#", 1)[0]
        if target_path and not (path.parent / target_path).exists():
            problems.append(
                {
                    "type": "missing_link",
                    "file": str(path.relative_to(root)),
                    "target": target,
                }
            )

if not source_path.exists():
    problems.append({"type": "missing_source_map", "file": "references/source-map.md"})
else:
    source_text = source_path.read_text(encoding="utf-8")
    defined_ids = set(re.findall(r"\b[DSR]\d+\b", source_text))
    for path in sorted(root.rglob("*.md")):
        if path == source_path:
            continue
        refs = set(re.findall(r"\b[DSR]\d+\b", path.read_text(encoding="utf-8")))
        for ref in sorted(refs - defined_ids, key=lambda item: (item[0], int(item[1:]))):
            problems.append(
                {
                    "type": "unknown_rule_id",
                    "file": str(path.relative_to(root)),
                    "id": ref,
                }
            )

result = {
    "skill": root.name,
    "markdown_files_checked": len(list(root.rglob("*.md"))),
    "problems": problems,
}

print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(1 if problems else 0)
