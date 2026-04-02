# Claude Education Skills Library

## Install

```
/plugin install GarethManning/claude-education-skills
```
Or browse the [Skills Directory](https://claude.ai) to install individual domain bundles.

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-1.0-blue)](https://agentskills.io)
[![Skills](https://img.shields.io/badge/skills-107-blue)](https://github.com/GarethManning/claude-education-skills)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Last Commit](https://img.shields.io/github/last-commit/GarethManning/claude-education-skills)](https://github.com/GarethManning/claude-education-skills/commits/main)

An open-source library of 106 evidence-based Claude skills for curriculum design, lesson planning, and assessment — usable today by any educator with access to Claude, and engineered for AI agent orchestration.

---

**👩‍🏫 I'm an educator — [start here →](#try-it-now)**
No setup required. Copy a prompt, paste into Claude, get structured output.

**🛠️ I'm a developer or AI builder — [start here →](#architecture)**
YAML schemas, typed inputs and outputs, chaining metadata, [live MCP server](#mcp-server).

---

## Who This Is For

- **Classroom teachers** who want evidence-based lesson and assessment design without hours of research
- **University lecturers and professors** who received little or no teacher training and want practical, research-grounded support for their teaching
- **Curriculum designers and heads of learning** building programmes, units, and assessments
- **School leaders in innovative and alternative education contexts** — international schools, Montessori, project-based, democratic and nature-based schools
- **Innovators reimagining education** — people building new school models, alternative programmes, and next-generation learning environments. Evidence-based constraints don't limit creative redesign of education; they deepen it.
- **EdTech developers and AI builders** who need a structured, programmatically accessible education knowledge layer
- **Education researchers** interested in how evidence translates into AI-mediated practice

---

## Why This Exists

AI is arriving in education fast. Whether it improves learning outcomes or simply scales mediocre practice depends almost entirely on what it is built on.

Most AI education tools are built on convention, habit, and assumption — on what educators have always done, rather than on what the research says actually works. Learning styles. Rigid lesson structures. Wellbeing programmes disconnected from learning theory. As AI expands in education, so does the risk of scaling ineffective practice.

This library exists to build something different: a credible, rigorous foundation for AI in education. One that is anchored in named research, honest about its limitations, and designed especially for the educators working at the frontier — building the next generation of schools, not optimising existing ones.

The potential is real. Personalised, evidence-grounded learning support at a scale that was never previously possible. But only if what is powering it is the actual evidence.

The benefit is not only personalised learning. It is teaching quality and workload. An educator who would otherwise spend hours researching, designing, and second-guessing gets structured, evidence-grounded support in minutes — which means more time for the parts of teaching that only a human can do.

That is one use case. The same library can power school-wide curriculum audits, personalised professional development pathways for teachers, or orchestrated end-of-term assessment reviews. The skills are the foundation. The architecture below describes the layers that make this possible.

---

## Try It Now

No API key. No technical setup. No dependencies.

1. Open any skill file in the repository
2. Copy the prompt block
3. Paste it into Claude and fill in the fields for your class or context

**Here is what that looks like.** Open `memory-learning-science/02-spaced-practice-scheduler.md` and provide:

- Topics: Cell structure, Cell transport, Cell division, Enzymes, Biological molecules
- Timeline: 8-week term, starting 3 February
- Lessons per week: 3

**Claude returns:** A complete week-by-week schedule showing when to teach new content and when to revisit previous topics at expanding intervals — with specific retrieval activities for each review slot (not "review cells" but "draw and label the cell membrane from memory, then check against your notes"). The schedule follows Cepeda et al.'s (2006) meta-analysis on optimal spacing intervals, includes interleaving across topics, and comes with practical guidance on what to do when review reveals gaps.

That is one skill. There are 106.

---

## What Makes This Different

**Evidence is the filter — including knowing what to exclude.**
Every skill is grounded in named research: specific authors, specific studies, specific findings. Frameworks that lack empirical support — including learning styles, VAK, and other widely-circulated but poorly-evidenced approaches — are not included. The library documents exactly what was excluded and why in [EXCLUSIONS.md](EXCLUSIONS.md). For any school or faculty trying to separate evidence from convention, that document is worth reading on its own.

**Evidence strength is rated transparently.**

| Rating | What it means |
|--------|--------------|
| **Strong** | Multiple meta-analyses or systematic reviews with consistent findings |
| **Moderate** | Solid experimental evidence with some contextual variation |
| **Emerging** | Promising research base with limited replication or practitioner translation |
| **Original** | Practitioner framework; clearly labelled, not claimed as research-backed |

Where original frameworks are included (Domain 14), they are labelled honestly. One important limitation: the skills encode research-grounded prompts, but the prompts themselves have not been empirically validated as AI interventions. That work is ongoing.

**Built by an educator with 20 years of international school experience.**
The pedagogical judgements embedded in every prompt, every output structure, and every known-limitations section reflect real classroom and curriculum design practice — not a reading of the literature.

**Designed for orchestration from day one.**
YAML schema headers, typed input and output fields, chaining metadata, and composable outputs are built into every skill. This is not a prompt collection with metadata bolted on. It is a skill library engineered for programmatic use.

---

## The 14 Domains

| # | Domain | Skills | Focus |
|---|--------|--------|-------|
| 1 | **Memory & Learning Science** | 8 | Retrieval practice, spacing, interleaving, cognitive load, dual coding, elaborative interrogation, feedback |
| 2 | **Self-Regulated Learning & Metacognition** | 5 | Self-regulation scaffolds, metacognitive prompts, goal-setting, study strategy selection, error analysis |
| 3 | **Explicit & Direct Instruction** | 5 | Gradual release sequences, checking for understanding, lesson openings, think-alouds, practice design |
| 4 | **Questioning, Discussion & Dialogue** | 4 | Socratic questioning, discussion protocols, dialogic teaching moves, hinge questions |
| 5 | **Literacy, Writing & Critical Thinking** | 7 | Argument structure, disciplinary writing, reading comprehension, source evaluation, text complexity, media literacy, critical thinking |
| 6 | **EAL/D & Language Development** | 5 | Language demand analysis, vocabulary tiering, scaffolded task modification, sentence frames, sheltered instruction |
| 7 | **Curriculum Design & Assessment** | 13 | Backwards design, competency unpacking, rubric generation, assessment validity, formative assessment, differentiation, gap analysis, learning progressions, PBL |
| 8 | **Wellbeing, Motivation & Student Agency** | 12 | Motivation diagnostics, self-efficacy, wellbeing-learning connections, agency scaffolds, belonging, and related practices |
| 9 | **Professional Learning & Teacher Development** | 9 | Lesson observation, reflective practice, PD session design, data interpretation, and related practices |
| 10 | **Global & Cross-Cultural Pedagogies** | 9 | Variation theory, CPA sequences, phenomenon-based learning, culturally responsive teaching, Ubuntu, place-based inquiry, Reggio documentation, emergent projects, cross-cultural validity |
| 11 | **Environmental & Experiential Learning** | 6 | Outdoor learning, biophilic design, ecological inquiry, experiential learning cycles, interdisciplinary connections, service learning |
| 12 | **AI Learning Science** | 14 | Adaptive hints, erroneous examples, digital worked examples, spacing algorithms, AI feedback, tutoring dialogue, learning analytics, collaborative learning, cognitive tutoring, self-explanation, metacognitive monitoring, productive failure, worked example transitions, formative assessment loops |
| 13 | **Montessori & Alternative Evidence-Based Approaches** | 4 | Three-part lessons, prepared environment design, mixed-age learning, uninterrupted work cycles |
| 14 | **Original Frameworks** | 5 | SEEDS regenerative inquiry, developmental band systems, learning target authoring, rubric logic, self-determined project design |

---

## Architecture

The library is Layer 1 of a three-layer system. See [ARCHITECTURE.md](ARCHITECTURE.md) for the full design.

**Layer 1 — Skill Library** (this repository, complete and available now)
106 skills across 14 domains. Each skill encodes a specific, evidence-grounded instructional or curriculum design decision. Works standalone today.

**Layer 2 — Context Engine** *(in design)*
Holds persistent information about students, classes, curriculum sequences, and assessment history. When connected, skill outputs become personalised — not generic advice about retrieval practice, but a specific retrieval schedule for this class based on what they have already learned and been assessed on.

**Layer 3 — Orchestrator** *(in design)*
Allows an educator to state a high-level goal — "Design a 6-week unit on climate change for my Year 8 class" — and receive a complete, personalised plan assembled from multiple skills. The orchestrator proposes; the educator decides.

### For developers: the YAML schema

Every skill opens with a machine-readable header. Here is a real example:

```yaml
---
skill_id: "memory-learning-science/spaced-practice-scheduler"
skill_name: "Spaced Practice Schedule Builder"
domain: "memory-learning-science"
version: "1.0"
evidence_strength: "strong"
evidence_sources:
  - "Cepeda et al. (2006) — Meta-analysis of 254 studies on distributed practice"
  - "Kornell & Bjork (2008) — Spacing and interleaving effects on learning"
  - "Dunlosky et al. (2013) — Distributed practice rated high-utility learning strategy"
input_schema:
  required:
    - field: "topics"
      type: "array"
      description: "List of topics or concepts to be spaced across the schedule"
    - field: "timeline"
      type: "string"
      description: "Available teaching period (e.g. '6-week half-term')"
    - field: "lessons_per_week"
      type: "integer"
      description: "Number of lessons per week for this subject"
  optional:
    - field: "assessment_date"
      type: "string"
      description: "From context engine: summative assessment date"
    - field: "student_profiles"
      type: "array"
      description: "From context engine: class-level retention data from prior assessments"
output_schema:
  type: "object"
  fields:
    - field: "schedule"
      type: "array"
      description: "Week-by-week schedule of new teaching and spaced review slots"
    - field: "review_activity_suggestions"
      type: "array"
      description: "Specific retrieval activities for each review slot"
    - field: "teacher_guidance"
      type: "string"
      description: "Implementation guidance and how to handle gaps"
chains_well_with:
  - "retrieval-practice-generator"
  - "formative-assessment-technique-selector"
  - "interleaving-unit-planner"
teacher_time: "5 minutes"
tags: ["spacing", "memory", "planning", "forgetting-curve", "distributed-practice"]
---
```

An orchestrator calls `search_skills("retrieval practice")`, gets back candidates, calls `get_skill` on the best match, and injects the prompt into its workflow.

### MCP Server

The skill library is available as a live MCP server. Any MCP-compatible client can discover, search, and invoke all 107 skills programmatically.

**Production URL:** `https://mcp-server-sigma-sooty.vercel.app/mcp`

Connect from Claude.ai by adding the URL under **Integrations > MCP Servers**. Connect from Claude Desktop:

```json
{
  "mcpServers": {
    "education-skills": {
      "type": "streamable-http",
      "url": "https://mcp-server-sigma-sooty.vercel.app/mcp"
    }
  }
}
```

The server exposes:
- **111 tools** (107 skills + 4 discovery tools: `list_skills`, `find_skills`, `suggest_skills`, `get_skill_details`)
- **107 prompts** (for clients that surface MCP prompts)

Source code, local setup, and development instructions: [`mcp-server/`](mcp-server/)

### Roadmap

| Feature | Status |
|---------|--------|
| Layer 1 — Skill Library (107 skills) | ✅ Complete |
| MCP Server (111 tools, live) | ✅ Complete |
| Layer 2 — Context Engine | 🔵 In design |
| Layer 3 — Orchestrator | 🔵 In design |

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for inclusion criteria. The standard is high intentionally — every skill must be grounded in named evidence, honestly rated, and practically useful. The library's value depends on its rigour.

---

## Credit

Built by [Gareth Manning](https://substack.com/@garethmanning) — educator, curriculum designer, and learning systems designer. 20 years of international education experience across 27 countries.

## Licence

[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Open. Forkable. Share alike.
