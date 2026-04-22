# Agent Skills Developer Guide

This document is for developers and AI builders who want to consume, orchestrate, or extend the Claude Education Skills Library programmatically.

---

## Installation

### As a Claude Code Plugin

```
/plugin install GarethManning/claude-education-skills
```

This makes all 107 skills available in your Claude Code session. Skills with `disable-model-invocation: false` will auto-activate when conversation context matches their trigger descriptions. Skills with `disable-model-invocation: true` must be invoked explicitly.

### From Source

```bash
git clone https://github.com/GarethManning/claude-education-skills.git
```

The `plugin.json` manifest at the repo root declares the plugin metadata. The `skills/` directory contains all skill files. The `registry.json` file provides the machine-readable index.

---

## registry.json

The registry is the primary programmatic interface to the library. It is generated from SKILL.md frontmatter by `scripts/generate-registry.py`.

### Structure

```json
{
  "version": "2.0",
  "generated": "<ISO timestamp>",
  "standard": "agent-skills-1.0",
  "total_skills": 107,
  "domains": [
    { "id": "memory-learning-science", "label": "Memory & Learning Science", "skill_count": 8 }
  ],
  "skills": [
    {
      "id": "memory-learning-science/spaced-practice-scheduler",
      "name": "spaced-practice-scheduler",
      "display_name": "Spaced Practice Schedule Builder",
      "domain": "memory-learning-science",
      "description": "<250-char description>",
      "disable_model_invocation": false,
      "evidence_strength": "strong",
      "tags": ["spacing", "memory", "planning"],
      "teacher_time": "5 minutes",
      "chains_with": ["retrieval-practice-generator", "interleaving-unit-planner"],
      "chain_edges": {
        "receives_from": [],
        "feeds_into": [],
        "output_field": null,
        "input_field": null
      },
      "path": "skills/memory-learning-science/spaced-practice-scheduler/SKILL.md"
    }
  ]
}
```

### Consuming the Registry

```python
import json

with open('registry.json') as f:
    registry = json.load(f)

# Find skills by domain
science_skills = [s for s in registry['skills'] if s['domain'] == 'memory-learning-science']

# Find skills by tag
spacing_skills = [s for s in registry['skills'] if 'spacing' in s['tags']]

# Find skills that chain with a given skill
chains = [s for s in registry['skills'] if 'spaced-practice-scheduler' in s['chains_with']]

# Filter to auto-activatable skills only
auto_skills = [s for s in registry['skills'] if not s['disable_model_invocation']]
```

### Keeping the Registry in Sync

```bash
python3 scripts/generate-registry.py
```

CI validates that `registry.json` matches the current SKILL.md files on every push and PR.

---

## Building an Orchestrator

The library is designed as Layer 1 of a three-layer architecture:

### Layer 1 — Skills (this repository)

107 self-contained pedagogical skills. Each skill takes structured input, applies evidence-based reasoning, and returns structured output. Skills work independently — no dependencies, no state.

### Layer 2 — Context Engine

Sits between the orchestrator and skills. Holds persistent information: student profiles, class data, curriculum sequences, assessment history, school context. When a skill is called through the context engine, optional input fields are automatically populated with relevant context, producing personalised rather than generic output.

### Layer 3 — Orchestrator

Receives a high-level educator goal (e.g. "Design a 6-week unit on climate change for Year 8") and:

1. Queries the context engine for relevant student and curriculum data
2. Selects and sequences appropriate skills using the registry
3. Chains skill outputs into a coherent plan
4. Presents the result for educator review and approval

The `chains_with` array in each registry entry provides explicit chaining hints. The orchestrator can also discover novel chains by matching output schemas to input schemas across the library.

---

## Chaining Graph

The `chain_edges` object in each skill entry is a placeholder for typed chain edges:

- `receives_from`: skills whose output feeds into this skill's input
- `feeds_into`: skills that consume this skill's output
- `output_field`: the specific output field that feeds downstream
- `input_field`: the specific input field that receives upstream data

All values are null in v2. These will be populated in a dedicated chaining design session that maps the full graph of typed data flow between skills. The untyped `chains_with` array provides directional hints in the interim.

---

## Projects and Skills

In Claude Code, **Projects** provide static context (class profiles, curriculum documents, school policies) while **Skills** provide dynamic pedagogical activation. They work together:

- A Project might contain: "Year 8 Science class, 28 students, 4 EAL learners, IB MYP curriculum, inquiry-based school"
- When a teacher asks for help within that Project, Skills auto-activate based on the conversation: the `language-demand-analyser` fires when EAL support is discussed, the `backwards-design-unit-planner` fires when unit planning begins
- The Project context enriches skill inputs; the Skills provide evidence-based structure to the outputs

This separation means skills are reusable across any project context, while projects provide the specificity that makes skill outputs actionable.
