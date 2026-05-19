#!/usr/bin/env python3
"""Validate the public WPS gongwen skills package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
REFERENCES_DIR = ROOT / "references"
EVALS_FILE = ROOT / "evals" / "evals.json"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def read(path: Path) -> str:
    if not path.exists():
        fail(f"missing {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str, path: Path) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)} missing YAML frontmatter")
    try:
        _, raw, _ = text.split("---\n", 2)
    except ValueError:
        fail(f"{path.relative_to(ROOT)} malformed YAML frontmatter")
    meta: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"')
    return meta


def main() -> int:
    skill_paths = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    if not skill_paths:
        fail("no skills found")

    evals = json.loads(read(EVALS_FILE))
    eval_skills = {case["skill"] for case in evals.get("evals", [])}
    seen_names: set[str] = set()

    for path in skill_paths:
        text = read(path)
        meta = parse_frontmatter(text, path)
        for key in ("name", "description", "type", "version", "category"):
            if not meta.get(key):
                fail(f"{path.relative_to(ROOT)} missing frontmatter key: {key}")
        if meta["type"] != "skill":
            fail(f"{path.relative_to(ROOT)} type must be skill")
        if meta["name"] in seen_names:
            fail(f"duplicate skill name: {meta['name']}")
        seen_names.add(meta["name"])
        if meta["name"] != path.parent.name:
            fail(f"{path.relative_to(ROOT)} name must match directory")
        if len(meta["description"]) < 80:
            fail(f"{path.relative_to(ROOT)} description too weak for trigger matching")
        if meta["name"] not in eval_skills:
            fail(f"{meta['name']} has no eval coverage")
        ref_path = REFERENCES_DIR / f"{meta['name']}.md"
        if not ref_path.exists():
            fail(f"{meta['name']} missing matching reference file")
        if not re.search(r"PASS / PARTIAL / BLOCKED|Native control status", text):
            fail(f"{meta['name']} missing status output contract")

    print(f"PASS: {len(skill_paths)} skills validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
