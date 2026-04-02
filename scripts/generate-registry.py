#!/usr/bin/env python3
"""Generate registry.json from skills/ directory SKILL.md frontmatter."""

import yaml
import json
import glob
import os
from datetime import datetime, timezone
from collections import Counter


DOMAIN_LABELS = {
    "ai-learning-science": "AI & Learning Science",
    "curriculum-assessment": "Curriculum & Assessment",
    "eal-language-development": "EAL & Language Development",
    "environmental-experiential-learning": "Environmental & Experiential Learning",
    "explicit-instruction": "Explicit Instruction",
    "global-cross-cultural-pedagogies": "Global & Cross-Cultural Pedagogies",
    "literacy-critical-thinking": "Literacy & Critical Thinking",
    "memory-learning-science": "Memory & Learning Science",
    "montessori-alternative-approaches": "Montessori & Alternative Approaches",
    "original-frameworks": "Original Frameworks",
    "professional-learning": "Professional Learning",
    "questioning-discussion": "Questioning & Discussion",
    "self-regulated-learning": "Self-Regulated Learning",
    "wellbeing-motivation-agency": "Wellbeing, Motivation & Agency",
}


def parse_skill(path):
    with open(path) as f:
        content = f.read()

    if not content.startswith("---"):
        raise ValueError(f"{path}: no YAML frontmatter")

    end = content.index("---", 3)
    fm = yaml.safe_load(content[3:end])

    parts = path.split(os.sep)
    domain = parts[-3]
    slug = parts[-2]

    chains_with = fm.get("chains_well_with", [])
    if isinstance(chains_with, str):
        chains_with = [chains_with]

    return {
        "id": f"{domain}/{slug}",
        "name": fm.get("name", slug),
        "display_name": fm.get("skill_name", slug),
        "domain": domain,
        "description": fm.get("description", ""),
        "disable_model_invocation": fm.get("disable-model-invocation", False),
        "evidence_strength": fm.get("evidence_strength", ""),
        "tags": fm.get("tags", []),
        "teacher_time": fm.get("teacher_time", ""),
        "chains_with": chains_with,
        "chain_edges": {
            "receives_from": [],
            "feeds_into": [],
            "output_field": None,
            "input_field": None,
        },
        "path": path,
    }


def main():
    skills = []
    for path in sorted(glob.glob("skills/**/SKILL.md", recursive=True)):
        skills.append(parse_skill(path))

    domain_counts = Counter(s["domain"] for s in skills)
    domains = []
    for domain_id in sorted(domain_counts.keys()):
        domains.append(
            {
                "id": domain_id,
                "label": DOMAIN_LABELS.get(domain_id, domain_id),
                "skill_count": domain_counts[domain_id],
            }
        )

    registry = {
        "version": "2.0",
        "generated": datetime.now(timezone.utc).isoformat(),
        "standard": "agent-skills-1.0",
        "total_skills": len(skills),
        "domains": domains,
        "skills": skills,
    }

    with open("registry.json", "w") as f:
        json.dump(registry, f, indent=2)

    print(f"registry.json generated: {len(skills)} skills, {len(domains)} domains")


if __name__ == "__main__":
    main()
