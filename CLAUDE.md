# Claude Education Skills Library — Claude Code Entry Point

## What this is
131 evidence-based education skills across 17 domains for curriculum design, lesson planning, and assessment. CC BY-SA 4.0. 213 stars, 42 forks. Includes a live MCP server at mcp-server-sigma-sooty.vercel.app/mcp and a CoWork plugin (.claude-plugin/).

## Stack
TypeScript (77.9%), Python (16.7%). Playwright for testing. Skills are structured markdown (SKILL.md) with YAML frontmatter. MCP server in mcp-server/ subdirectory. CI via GitHub Actions.

## Test
`npx playwright test`

## Read at session start
1. STATE.md — current build state. If it doesn't exist, note its absence and proceed. Do not create one from guesses — create it at session end from verified work.
2. This file
3. README.md — installation methods, skill format, architecture
4. ARCHITECTURE.md — three-layer system design
5. EVIDENCE.md — evidence strength ratings and methodology
6. EXCLUSIONS.md — what was deliberately excluded and why

## Critical build workflow
After adding or editing ANY skill, these three steps are mandatory before committing:
1. `python3 scripts/generate-registry.py` — regenerates registry.json
2. `cd mcp-server && npm run bundle-skills && cd ..` — rebuilds mcp-server/src/skills.json
3. Stage all three files: the SKILL.md, registry.json, AND mcp-server/src/skills.json
CI will fail if the bundle is out of sync with the skills. The MCP server serves a pre-built snapshot — unbundled changes will NOT appear on the live server even after Vercel redeploy.

## 17 domains
ai-learning-science, ai-literacy, curriculum-alignment, curriculum-assessment, eal-language-development, environmental-experiential-learning, explicit-instruction, global-cross-cultural-pedagogies, historical-thinking, literacy-critical-thinking, memory-learning-science, montessori-alternative-approaches, original-frameworks, professional-learning, questioning-discussion, self-regulated-learning, wellbeing-motivation-agency

## Key conventions
- Every skill must cite named research — no skills without evidence grounding
- Evidence strength rated: strong, moderate, emerging, or original (honestly labelled)
- YAML schema headers mandatory: skill_id, domain, evidence_strength, evidence_sources, input_schema, output_schema, chains_well_with
- Skills live in skills/<domain>/<skill-name>/SKILL.md
- Original frameworks (Domain 15) clearly labelled as practitioner-originated

## Commit
`git add -A && git commit -m "[description]" && git push`

## STATE.md
Maintain at repo root. Update at session end: what was done, what was verified, what's next. Commit STATE.md separately from feature work.
