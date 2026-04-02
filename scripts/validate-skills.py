#!/usr/bin/env python3
"""Validate all SKILL.md files have correct Agent Skills v2 frontmatter."""

import yaml
import glob
import re
import sys


def validate_skill(path):
    errors = []
    warnings = []

    with open(path) as f:
        content = f.read()

    # Check line count
    line_count = content.count("\n") + 1
    if line_count > 500:
        warnings.append(f"File is {line_count} lines (over 500-line guideline)")

    # Check YAML frontmatter exists
    if not content.startswith("---"):
        errors.append("No YAML frontmatter (missing opening ---)")
        return errors, warnings

    try:
        end = content.index("---", 3)
    except ValueError:
        errors.append("No closing --- for YAML frontmatter")
        return errors, warnings

    fm_text = content[3:end]
    try:
        fm = yaml.safe_load(fm_text)
    except yaml.YAMLError as e:
        errors.append(f"Invalid YAML: {e}")
        return errors, warnings

    if not isinstance(fm, dict):
        errors.append("YAML frontmatter is not a mapping")
        return errors, warnings

    # Agent Skills v2 required fields
    name = fm.get("name")
    if not name:
        errors.append("Missing 'name' field")
    elif not re.match(r"^[a-z0-9-]+$", name):
        errors.append(f"'name' contains invalid chars: {name}")
    elif len(name) > 64:
        errors.append(f"'name' exceeds 64 chars: {len(name)}")

    desc = fm.get("description")
    if not desc:
        errors.append("Missing 'description' field")
    elif len(desc) > 250:
        errors.append(f"'description' exceeds 250 chars: {len(desc)}")

    disable = fm.get("disable-model-invocation")
    if disable is None:
        errors.append("Missing 'disable-model-invocation' field")
    elif not isinstance(disable, bool):
        errors.append(f"'disable-model-invocation' is not boolean: {type(disable)}")

    # Existing required fields
    for field in ["skill_id", "skill_name", "domain", "evidence_strength"]:
        if field not in fm:
            errors.append(f"Missing existing field: '{field}'")

    return errors, warnings


def main():
    paths = sorted(glob.glob("skills/**/SKILL.md", recursive=True))
    if not paths:
        print("ERROR: No SKILL.md files found")
        sys.exit(1)

    total_errors = 0
    total_warnings = 0

    for path in paths:
        errors, warnings = validate_skill(path)
        if errors:
            for e in errors:
                print(f"ERROR  {path}: {e}")
            total_errors += len(errors)
        if warnings:
            for w in warnings:
                print(f"WARN   {path}: {w}")
            total_warnings += len(warnings)

    print(f"\nValidated {len(paths)} SKILL.md files")
    print(f"Errors: {total_errors}, Warnings: {total_warnings}")

    if total_errors > 0:
        sys.exit(1)

    print("All SKILL.md files pass validation")


if __name__ == "__main__":
    main()
