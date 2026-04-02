#!/usr/bin/env python3
"""Validate registry.json structure and content."""

import json
import sys


def main():
    try:
        with open("registry.json") as f:
            registry = json.load(f)
    except FileNotFoundError:
        print("ERROR: registry.json not found")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"ERROR: registry.json is not valid JSON: {e}")
        sys.exit(1)

    errors = []

    # Check top-level fields
    if registry.get("version") != "2.0":
        errors.append(f"Expected version '2.0', got '{registry.get('version')}'")

    if registry.get("standard") != "agent-skills-1.0":
        errors.append(
            f"Expected standard 'agent-skills-1.0', got '{registry.get('standard')}'"
        )

    total = registry.get("total_skills", 0)
    skills = registry.get("skills", [])
    domains = registry.get("domains", [])

    if total != len(skills):
        errors.append(f"total_skills ({total}) != actual skills count ({len(skills)})")

    # Validate each skill entry
    for i, s in enumerate(skills):
        if not s.get("id"):
            errors.append(f"Skill {i}: missing 'id'")
        if not s.get("name"):
            errors.append(f"Skill {i}: missing 'name'")
        if not s.get("description"):
            errors.append(f"Skill {i}: missing 'description'")
        elif len(s["description"]) > 250:
            errors.append(
                f"Skill {s.get('id', i)}: description exceeds 250 chars "
                f"({len(s['description'])})"
            )
        if not s.get("path", "").startswith("skills/"):
            errors.append(f"Skill {s.get('id', i)}: path doesn't start with 'skills/'")
        if not isinstance(s.get("disable_model_invocation"), bool):
            errors.append(
                f"Skill {s.get('id', i)}: disable_model_invocation is not boolean"
            )

    # Validate domain skill counts match
    domain_counts = {}
    for s in skills:
        d = s.get("domain", "")
        domain_counts[d] = domain_counts.get(d, 0) + 1

    for d in domains:
        actual = domain_counts.get(d["id"], 0)
        if actual != d["skill_count"]:
            errors.append(
                f"Domain {d['id']}: declared {d['skill_count']} skills, "
                f"found {actual}"
            )

    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        sys.exit(1)

    print(f"registry.json valid: {len(skills)} skills, {len(domains)} domains")


if __name__ == "__main__":
    main()
