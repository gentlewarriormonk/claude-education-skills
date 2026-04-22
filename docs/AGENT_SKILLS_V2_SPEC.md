# Education Skills Library — Agent Skills v2 Upgrade Spec
**For Claude Code. Read this entire document before writing a single line of code.**

---

## Overview

This spec upgrades the Claude Education Skills Library from a custom MCP-served skill collection into a fully Agent Skills open standard–compliant plugin. The outcome: any Claude user can install all 106 skills with one command, skills auto-activate when relevant without being explicitly invoked, and the library becomes distributable across any Agent Skills–compatible AI tool.

## Repo

`~/Documents/Github/claude-education-skills`

Work on branch `feature/agent-skills-v2`. Do not merge to main without human review of REVIEW.md (generated in Phase 2).

## Non-negotiables

- Zero content loss. Every word of every skill's existing YAML and markdown is preserved.
- Full backward compatibility. The existing MCP server continues to work unchanged.
- Do not modify domain names, skill names, evidence sources, input/output schemas, or chains_well_with metadata.
- SKILL.md content length: keep under 500 lines per file. If any current skill file exceeds this, note it in the log but do not truncate.
- Remove `.DS_Store` from the repo during Phase 1 and add it to `.gitignore`.

---

## Current Structure

```
claude-education-skills/
├── ai-learning-science/           ← domain folder
│   └── skill-name.md              ← flat skill files
├── curriculum-assessment/
│   └── skill-name.md
├── ... (14 domain folders total)
├── ARCHITECTURE.md
├── EVIDENCE.md
├── EXCLUSIONS.md
├── IMPLEMENTATIONS.md
├── README.md
└── llms.txt
```

## Target Structure

```
claude-education-skills/
├── skills/                                          ← NEW: plugin skills root
│   ├── ai-learning-science/                         ← domain preserved as subdirectory
│   │   └── adaptive-hint-sequence-designer/         ← NEW: skill folder
│   │       └── SKILL.md                             ← migrated from domain/skill.md
│   ├── curriculum-assessment/
│   │   └── backwards-design-unit-planner/
│   │       └── SKILL.md
│   └── ... (all 14 domains, all 106 skills)
├── registry.json                                    ← NEW: machine-readable skill index
├── plugin.json                                      ← NEW: plugin manifest
├── ARCHITECTURE.md                                  ← updated
├── AGENT_SKILLS.md                                  ← NEW: developer guide
├── EVIDENCE.md
├── EXCLUSIONS.md
├── IMPLEMENTATIONS.md
├── README.md                                        ← updated
├── llms.txt
└── .gitignore                                       ← updated to include .DS_Store
```

---

## Phase 1 — Structural Migration

**Goal:** Move all 106 skill files from `domain/skill-name.md` to `skills/domain/skill-name/SKILL.md` with zero content changes.

### Steps

1. **Inventory current state.** Before touching anything, write a `migration-log.md` in the repo root listing every skill file found, its path, and its character count. This is your ground truth for verification.

2. **Create the `skills/` directory structure.** For each existing `domain-name/skill-name.md`:
   - Create `skills/domain-name/skill-name/` directory
   - Move the file to `skills/domain-name/skill-name/SKILL.md`
   - The skill name slug is derived from the filename (remove `.md` extension, keep hyphens)

3. **Verify zero content loss.** After migration, for every file in `migration-log.md`, confirm:
   - The file exists at the new path
   - The character count matches exactly
   - The YAML frontmatter is intact (check for `---` opening marker)

4. **Clean up.** Remove `.DS_Store` from the repo. Add to `.gitignore` if not already present. Remove empty domain folders at the root (they should all be empty after migration).

5. **Write verification report.** Append to `migration-log.md`: total files migrated, any failures, any files skipped.

### Tests

```bash
# Count skills before (run before migration)
find . -name "*.md" -path "./*-*/*.md" | grep -v "skills/" | wc -l

# Count skills after (must match)
find skills/ -name "SKILL.md" | wc -l

# Check no orphaned .md files in old locations
find . -name "*.md" -not -path "./skills/*" -not -name "README.md" \
  -not -name "ARCHITECTURE.md" -not -name "EVIDENCE.md" \
  -not -name "EXCLUSIONS.md" -not -name "IMPLEMENTATIONS.md" \
  -not -name "migration-log.md" -not -name "AGENT_SKILLS.md"
# Expected: only root-level docs, no domain/skill files
```

### Stop condition

Stop here and report results. Do not proceed to Phase 2 until skill count matches and zero content loss is confirmed. Output: "Phase 1 complete. N skills migrated. Zero content loss confirmed." or a specific error report.

---

## Phase 2 — Progressive Disclosure Frontmatter

**Goal:** Add Agent Skills standard frontmatter to every SKILL.md. Generate all 106 descriptions into a REVIEW.md file for human review. Do NOT merge descriptions into SKILL.md files until human has reviewed and approved REVIEW.md.

### The Exact Frontmatter Fields to Add

These fields are added to the **top** of every SKILL.md's existing YAML frontmatter block. The existing YAML (skill_id, skill_name, domain, version, evidence_strength, evidence_sources, input_schema, output_schema, chains_well_with, tags, teacher_time) is preserved completely below these new fields.

```yaml
---
# AGENT SKILLS STANDARD FIELDS (new in v2)
name: skill-name-slug                    # lowercase, hyphens only, max 64 chars — derived from directory name
description: "..."                       # SEE DESCRIPTION RULES BELOW — max 250 chars
disable-model-invocation: false          # SEE INVOCATION RULES BELOW
user-invocable: true                     # default true; set false only for pure background knowledge
effort: medium                           # default for all education skills

# EXISTING FIELDS (preserved exactly as-is)
skill_id: "..."
skill_name: "..."
# ... rest of existing YAML unchanged
---
```

### Description Rules (Critical — read carefully)

**Format:** `[Active verb] [what it produces] for [context]. Use when [specific trigger scenario].`

**Hard constraints:**
- Maximum 250 characters — this is enforced by the platform and truncated if exceeded
- Front-load trigger keywords — the platform can shorten from the end, never from the front
- Use teacher language, not academic language
- Must be specific enough that a false activation would feel wrong, not just irrelevant

**Quality test:** Read the description and ask: *If a teacher typed this as a search query, would this skill be the right result? And if this skill activated mid-conversation because these words appeared, would it feel helpful or intrusive?*

**Examples of good descriptions:**
- `"Design a spaced retrieval schedule for any topic list and timeline. Use when planning units, term sequences, or revision programmes."`
- `"Generate a cascading hint sequence for a problem type, revealing progressively without giving answers. Use when designing tutoring dialogues or scaffolded worksheets."`
- `"Analyse the language demands of a classroom task for EAL/D students. Use when adapting tasks, planning support, or assessing accessibility."`

**Examples of bad descriptions:**
- `"Facilitates the application of distributed practice principles to instructional scheduling."` — academic, not trigger-first
- `"Spaced practice."` — too short, no action verb, no trigger
- `"Help teachers design better lessons using evidence-based approaches."` — too broad, will trigger on everything

### Invocation Rules

Set `disable-model-invocation: true` for skills that:
- Require significant student-specific data that won't be present in most conversations (example: `individual-spacing-algorithm-explainer` needs prior performance data)
- Are in Domain 14 (original frameworks) — these are contextually specific enough that auto-activation will misfire
- Have triggers so broad they would activate constantly (example: `formative-assessment-technique-selector`)

Set `disable-model-invocation: false` (default) for all other skills.

When uncertain, default to `false` — a human reviewer will catch over-broad triggers in REVIEW.md.

### What to Generate: REVIEW.md Format

Write a single `REVIEW.md` file at the repo root with the following structure. This is the file the human reviews. Do not apply descriptions to SKILL.md files yet.

```markdown
# Skills Description Review — Agent Skills v2

**Instructions for reviewer:**
- Each entry shows the proposed description and invocation setting.
- Edit directly in this file if any description is wrong, too broad, too narrow, or violates the format rules.
- Delete the ❓ marker on any line you want to flag for discussion.
- When satisfied with all 106 entries, confirm and descriptions will be applied.

---

## Domain: memory-learning-science (8 skills)

### spaced-practice-scheduler
**Proposed description:**
"Design a spaced retrieval schedule for any topic list and timeline. Use when planning units, term sequences, or revision programmes."
**Character count:** 127 ✅
**disable-model-invocation:** false
**Rationale:** Triggers are specific (revision planning, spacing), unlikely to misfire.

---

### retrieval-practice-generator
...
```

Each entry must include:
- Proposed description (in quotes)
- Character count with ✅ (≤250) or ❌ (>250)
- `disable-model-invocation` value
- One-line rationale for the invocation setting

Group by domain in the same order as the existing repo. Include all 14 domains.

### How to Generate Good Descriptions

For each skill, use the following inputs to generate the description:
1. The `skill_name` field
2. The `domain` field
3. The `tags` array
4. The `input_schema.required` fields (what does a teacher need to provide?)
5. The `chains_well_with` list (what workflow does this skill belong to?)

The description should capture: *what the skill produces* + *the specific situation where it's useful*.

### Tests for Phase 2

```python
# Run this to validate all descriptions in REVIEW.md before human review
import re

with open('REVIEW.md') as f:
    content = f.read()

# Find all proposed descriptions
descriptions = re.findall(r'\*\*Proposed description:\*\*\n"([^"]+)"', content)
print(f"Found {len(descriptions)} descriptions")
assert len(descriptions) == 106, f"Expected 106, got {len(descriptions)}"

for i, desc in enumerate(descriptions):
    assert len(desc) <= 250, f"Description {i+1} exceeds 250 chars: {len(desc)} chars"
    assert desc[0].isupper(), f"Description {i+1} doesn't start with capital letter"

print("All 106 descriptions valid (length and format checks passed)")
```

### Stop Condition

Generate REVIEW.md and stop. Output: "Phase 2 complete. REVIEW.md generated with 106 skill descriptions. Please review REVIEW.md and confirm before Phase 3 proceeds." 

**Do not proceed to Phase 3 without explicit human confirmation.**

---

## Phase 3 — Apply Approved Descriptions

**This phase runs only after human has reviewed and confirmed REVIEW.md.**

### Steps

1. Parse approved descriptions from REVIEW.md (use the final state of the file, incorporating any human edits).

2. For each skill, add the new frontmatter fields to the top of the existing YAML block in SKILL.md:
   - `name`: derived from directory name
   - `description`: from approved REVIEW.md
   - `disable-model-invocation`: from approved REVIEW.md
   - `user-invocable: true` (default for all)
   - `effort: medium` (default for all)

3. Verify the YAML is still valid in every file after modification.

### Tests

```bash
# Validate YAML is parseable in all SKILL.md files
python3 -c "
import yaml, glob, sys
errors = []
for f in glob.glob('skills/**/**/SKILL.md', recursive=True):
    with open(f) as fh:
        content = fh.read()
    # Extract frontmatter
    if content.startswith('---'):
        end = content.index('---', 3)
        fm = content[3:end]
        try:
            yaml.safe_load(fm)
        except Exception as e:
            errors.append(f'{f}: {e}')
if errors:
    for e in errors: print(e)
    sys.exit(1)
print(f'All SKILL.md files have valid YAML frontmatter')
"
```

---

## Phase 4 — Registry Manifest

**Goal:** Generate `registry.json` — the machine-readable skill index that enables progressive disclosure.

### registry.json Schema

```json
{
  "version": "2.0",
  "generated": "<ISO timestamp>",
  "standard": "agent-skills-1.0",
  "total_skills": 106,
  "domains": [
    {
      "id": "memory-learning-science",
      "label": "Memory & Learning Science",
      "skill_count": 8
    }
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

**Note on `chain_edges`:** The `output_field` and `input_field` values are intentionally null in v2. These are placeholder slots for typed chain edges that will be filled in a separate chaining design session. Do not attempt to infer these values — leave as null.

### Generation

Write a Python script `scripts/generate-registry.py` that:
1. Walks the `skills/` directory
2. Reads the YAML frontmatter from each SKILL.md
3. Extracts the required fields
4. Writes `registry.json`

The script should be runnable standalone and is added to CI to keep registry in sync.

### Tests

```python
import json

with open('registry.json') as f:
    registry = json.load(f)

assert registry['total_skills'] == 106
assert len(registry['skills']) == 106
assert all(len(s['description']) <= 250 for s in registry['skills'])
assert all(s['path'].startswith('skills/') for s in registry['skills'])
print("registry.json valid")
```

---

## Phase 5 — Plugin Manifest

**Goal:** Create `plugin.json` to make the library installable as a Claude Code plugin.

### plugin.json Schema

```json
{
  "name": "claude-education-skills",
  "display_name": "Claude Education Skills Library",
  "version": "2.0.0",
  "description": "106 evidence-based pedagogical skills for educators. Curriculum design, assessment, learning science, wellbeing, professional learning, and more.",
  "author": "Gareth Manning",
  "homepage": "https://github.com/GarethManning/claude-education-skills",
  "license": "CC BY-SA 4.0",
  "skills": "skills/",
  "min_claude_version": "claude-sonnet-4-6"
}
```

### Tests

```bash
# Validate plugin.json is valid JSON
python3 -c "import json; json.load(open('plugin.json')); print('plugin.json valid')"

# Confirm skills directory is referenced correctly
python3 -c "
import json, os
p = json.load(open('plugin.json'))
assert os.path.isdir(p['skills']), f\"Skills dir not found: {p['skills']}\"
print('Plugin skills directory exists')
"
```

---

## Phase 6 — Documentation Updates

### README.md

Add at the top of the README (before existing content):

```markdown
## Install

```
/plugin install GarethManning/claude-education-skills
```
Or browse the [Skills Directory](https://claude.ai) to install individual domain bundles.

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-1.0-blue)](https://agentskills.io)
[![Skills](https://img.shields.io/badge/skills-106-blue)](https://github.com/GarethManning/claude-education-skills)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
```

### ARCHITECTURE.md

Add a new section titled "Agent Skills Compliance (v2)" describing:
- The plugin structure
- The progressive disclosure mechanism (metadata-first loading)
- The registry.json and what it enables
- The typed chain edges (null in v2, to be filled in chaining design session)
- The conflict resolution rule: when multiple skills auto-activate, surface as suggestions, never auto-fire more than one

### AGENT_SKILLS.md (new file)

Create a new file for the developer/AI builder audience covering:
- How to install the plugin
- How the registry.json works and how to consume it programmatically
- How to build an orchestrator on top of this library
- The chaining graph structure (including the null placeholders and what they'll become)
- The three-layer architecture (Skills → Context Engine → Orchestrator)
- How Projects and Skills work together (Projects for static class context, Skills for dynamic pedagogical activation)

---

## Phase 7 — CI and Final Validation

### .github/workflows/validate.yml

Create a GitHub Actions workflow that runs on every push to main and every PR:

```yaml
name: Validate Skills Library
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install pyyaml
      - name: Count skills
        run: |
          COUNT=$(find skills/ -name "SKILL.md" | wc -l)
          echo "Skills found: $COUNT"
          [ "$COUNT" -eq 106 ] || (echo "Expected 106 skills, found $COUNT" && exit 1)
      - name: Validate YAML frontmatter
        run: python3 scripts/validate-skills.py
      - name: Validate registry.json
        run: python3 scripts/validate-registry.py
      - name: Check registry is in sync
        run: |
          python3 scripts/generate-registry.py
          git diff --exit-code registry.json || (echo "registry.json is out of sync — run scripts/generate-registry.py" && exit 1)
```

### scripts/validate-skills.py

Write a validation script that checks every SKILL.md for:
- Valid YAML frontmatter
- `name` field present and valid (lowercase, hyphens, max 64 chars)
- `description` field present and ≤250 chars
- `disable-model-invocation` is boolean
- Existing required fields still present: `skill_id`, `skill_name`, `domain`, `evidence_strength`
- File is under 500 lines (warn, don't fail)

### Final Manual Test Battery

After all phases complete, run these five tests manually and report results:

1. **Install test:** In a fresh Claude Code session, run `/plugin install GarethManning/claude-education-skills` (or install from local path). Confirm skills appear in `/` menu.

2. **Auto-activation test:** Say "I need to plan revision sessions for my Year 9 class over the next 6 weeks." Confirm `spaced-practice-scheduler` activates or is surfaced as a suggestion.

3. **Direct invocation test:** Run `/backwards-design-unit-planner` directly. Confirm it runs and produces expected output.

4. **Registry test:** Confirm `registry.json` is valid JSON, has 106 skills, and all descriptions are ≤250 chars.

5. **Backward compatibility test:** Make a test call to the existing MCP server (`mcp-server-sigma-sooty.vercel.app/mcp`) using `list_skills`. Confirm it still returns results (MCP server is a separate repo — this test just confirms the migration hasn't broken anything the MCP server expects from the repo).

---

## Execution Order Summary

```
Phase 1: Structural Migration         → STOP: confirm skill count + zero content loss
Phase 2: Generate descriptions        → STOP: human reviews REVIEW.md
Phase 3: Apply approved descriptions  → runs after human confirms REVIEW.md
Phase 4: Registry manifest            → automated
Phase 5: Plugin manifest              → automated  
Phase 6: Documentation                → automated
Phase 7: CI + final validation        → automated, then manual test battery
```

Phases 3–7 can run continuously once Phase 2 is approved.

---

## What is Out of Scope for This Session

- MCP server updates (separate repo — `mcp-server-sigma-sooty.vercel.app/mcp` — separate Claude Code session)
- Typed chain edge values (null placeholders only — requires separate chaining design session)
- New skills or domain additions
- Harness templates
- Layer 2 (Context Engine) or Layer 3 (Orchestrator) work

---

## Definition of Done

The session is complete when:
- [ ] All 106 skills exist at `skills/domain/skill-name/SKILL.md`
- [ ] All 106 skills have valid Agent Skills frontmatter including approved descriptions
- [ ] `registry.json` generated and valid
- [ ] `plugin.json` created
- [ ] CI workflow passes
- [ ] All 5 manual tests pass
- [ ] REVIEW.md human-reviewed and descriptions applied
- [ ] No regressions in existing MCP server (backward compat test passes)
- [ ] Playwright test suite written covering: skill discovery, direct invocation, registry validation, plugin manifest validation
- [ ] PR opened on `feature/agent-skills-v2` ready for merge review

---

*Spec version: 1.0 — April 2026*
*Do not begin execution until you have read this document in full.*
