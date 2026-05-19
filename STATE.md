# STATE.md — education-agent-skills

**Last updated:** 2026-05-19 (Session 7)

## What was done

Added 5 H3Uni skills across two domains:

**systems-thinking:**
1. **systems-thinking/hexagon-complexity-mapper** — Guides students through hexagon mapping: factors placed on tiles where adjacency signals a claimed relationship. Critical principle: adjacency IS the meaning-making gesture, not sorting or categorisation. Evidence: Hodgson (1992), Meadows (2008), Senge (1990), H3Uni guides. evidence_strength: emerging.

**original-frameworks:**
2. **original-frameworks/scoping-for-transformative-learning-inquiry** — Defines inquiry scope before any mapping begins. Output: scoping statement in format "We are exploring [what] from the perspective of [who] so that we can [purpose]." Evidence: H3Uni Scoping method, Fazey et al. (2018), Rajagopalan & Midgley (2015). evidence_strength: emerging.
3. **original-frameworks/three-horizons-learning-transition-mapper** — Maps H1 (current pattern under strain) → H3 (preferred future) → H2 (innovations sorted as H2+ or H2-). Critical sequence enforced: never H1 → H2 → H3. Evidence: Curry & Hodgson (2008), Sharpe et al. (2016), Sharpe & Hodgson (2019), H3Uni guides. evidence_strength: emerging.
4. **original-frameworks/dilemma-navigation-for-education-design** — Navigates genuine dilemmas (both/and integration, not winner-picking). Critical distinction: dilemmas have legitimate value on both sides; problems have solutions. Evidence: H3Uni Dilemma Navigation, Johnson (1992), Hampden-Turner (1990). evidence_strength: emerging.
5. **original-frameworks/multi-perspective-decision-wheel** — Examines decisions through 4–6 perspectives (each with: sees, misses, asks, contributes), names tensions, synthesises insights, and produces a next responsible step. Evidence: H3Uni Wheel of Wisdom, Midgley (2000), Rajagopalan & Midgley (2015). evidence_strength: emerging.

Also:
- README badge updated: 147 → 152 skills
- README domain table updated: rows 4 (4→5), 7 (15→13), 9 (9→10), 15 (11→17), 18 (5→8); descriptions updated for original-frameworks and systems-thinking rows
- README MCP tool count updated: 149 → 156 tools, 145 → 152 prompts
- CLAUDE.md updated: 147 → 152 skills
- llms.txt updated: 131 → 152 skills, 17 → 19 domains; all 19 domain rows with correct counts

## What was verified (Session 7)

- `python3 scripts/generate-registry.py`: 152 skills, 19 domains
- `python3 scripts/validate-skills.py`: 152 skills, 0 errors, 4 pre-existing warnings (line-length on unrelated skills)
- `python3 scripts/validate-registry.py`: 152 skills, 19 domains — valid
- `npx playwright test`: 20/20 pass
- `cd mcp-server && npm run bundle-skills`: 152 skills bundled
- `cd mcp-server && npm run build && npm test`: 16/16 pass

## Session 6 summary (2026-05-18)

Added 2 orchestrator skills (assessment-design-orchestrator, inclusive-design-orchestrator). Registry at 147 skills. Committed: b88d3b8.

## Chain targets verified

Assessment Design Orchestrator:
- formative-assessment-technique-selector ✓
- assessment-validity-checker ✓
- gap-analysis-from-student-work ✓
- differentiation-adapter ✓
- self-regulation-scaffold-generator ✓
- inclusive-design-orchestrator ✓ (created this session)
- udl-barrier-anticipator ✓

Inclusive Design Orchestrator:
- udl-lesson-auditor ✓
- udl-options-designer ✓
- udl-barrier-anticipator ✓
- differentiation-adapter ✓
- assessment-design-orchestrator ✓ (created this session)
- language-demand-analyser ✓
- scaffolded-task-modifier ✓

## What's next

- Systems-thinking orchestrator: systems-thinking domain now has 8 skills (iceberg, aspirational iceberg, hexagon complexity mapper, leverage-response design, mental model mapper, agency circles, ladder of inference, wellbeing impact mapper). A composite orchestrator linking these into a full inquiry arc is the logical next step (separate from the existing compassionate-systems-awareness-orchestrator which covers a subset).
- Perspective-taking designer (questioning-discussion) has natural cross-domain chains with historical-thinking — worth formalising.
- The assessment-design-orchestrator and inclusive-design-orchestrator now cross-chain with each other, making a combined "accessible assessment design" flow possible as a future composite skill.
