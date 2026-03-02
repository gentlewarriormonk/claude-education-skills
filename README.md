# Education Skill Library

An open-source library of 100 evidence-based Claude skills that turn education research into structured, immediately usable outputs for curriculum design, lesson planning, and assessment — designed to work today for any educator with access to Claude, and engineered from the ground up for AI agent orchestration.

## Why This Exists

Two things make this library unusual, and they are both deliberate.

**First: every skill works right now.** Any educator with access to Claude can open a skill file, copy the prompt, fill in the input fields, and get a structured, evidence-grounded output in minutes. No API key. No technical setup. No dependencies. The skills encode research — retrieval practice, cognitive load theory, formative assessment, dialogic teaching, self-regulated learning, and much more — so that an educator using a skill gets the benefit of deep knowledge of the evidence base, even if they have never read the original studies.

**Second: the library is built for machines, not just humans.** Every skill file opens with a machine-readable YAML schema header that defines the skill's inputs, outputs, evidence strength, chaining relationships, and tags. This means the entire library can be parsed programmatically — by AI agents, MCP servers, orchestration frameworks, or any system that needs to discover, select, and invoke education-specific capabilities. The composable output schemas mean one skill's output can feed directly into another skill's input. This was not added later. It is the architecture.

Together, these two properties mean the library is useful today and ready for the systems being built tomorrow.

## Try It Now

Pick a skill. Copy the prompt. Fill in the fields. Here is what that looks like with the **Spaced Practice Schedule Builder** (`memory-learning-science/02-spaced-practice-scheduler.md`):

**You provide:**
- **Topics:** Cell structure, Cell transport, Cell division, Enzymes, Biological molecules
- **Timeline:** 8-week term, starting 3 February
- **Lessons per week:** 3

**Claude returns:** A complete week-by-week schedule showing when to teach new content and when to revisit previous topics at expanding intervals — with specific retrieval activities for each review slot (not "review cells" but "draw and label the cell membrane from memory, then check against your notes"). The schedule follows Cepeda et al.'s (2006) meta-analysis on optimal spacing intervals, includes interleaving across topics, and comes with practical guidance on what to do when review reveals gaps.

That is one skill. There are 100.

## The 14 Domains

| # | Domain | Skills | Focus |
|---|--------|--------|-------|
| 1 | [Memory & Learning Science](memory-learning-science/) | 8 | Retrieval practice, spacing, interleaving, cognitive load, dual coding, elaborative interrogation, feedback |
| 2 | [Self-Regulated Learning & Metacognition](self-regulated-learning/) | 5 | Self-regulation scaffolds, metacognitive prompts, goal-setting, study strategy selection, error analysis |
| 3 | [Explicit & Direct Instruction](explicit-instruction/) | 5 | Gradual release sequences, checking for understanding, lesson openings, think-alouds, practice design |
| 4 | [Questioning, Discussion & Dialogue](questioning-discussion/) | 4 | Socratic questioning, discussion protocols, dialogic teaching moves, hinge questions |
| 5 | [Literacy, Writing & Critical Thinking](literacy-critical-thinking/) | 7 | Argument structure, disciplinary writing, reading comprehension, source evaluation, text complexity, media literacy, critical thinking |
| 6 | [EAL/D & Language Development](eal-language-development/) | 5 | Language demand analysis, vocabulary tiering, scaffolded task modification, sentence frames, sheltered instruction |
| 7 | [Curriculum Design & Assessment](curriculum-assessment/) | 9 | Backwards design, competency unpacking, rubric generation, assessment validity, formative assessment, differentiation, gap analysis, learning progressions, PBL |
| 8 | [Wellbeing, Motivation & Student Agency](wellbeing-motivation-agency/) | 12 | Motivation diagnostics, self-efficacy, wellbeing-learning connections, agency scaffolds, belonging, and related practices |
| 9 | [Professional Learning & Teacher Development](professional-learning/) | 7 | Lesson observation, reflective practice, PD session design, data interpretation, and related practices |
| 10 | [Global & Cross-Cultural Pedagogies](global-cross-cultural-pedagogies/) | 9 | Variation theory, CPA sequences, phenomenon-based learning, culturally responsive teaching, Ubuntu, place-based inquiry, Reggio documentation, emergent projects, cross-cultural validity |
| 11 | [Environmental & Experiential Learning](environmental-experiential-learning/) | 6 | Outdoor learning, biophilic design, ecological inquiry, experiential learning cycles, interdisciplinary connections, service learning |
| 12 | [AI Learning Science](ai-learning-science/) | 14 | Adaptive hints, erroneous examples, digital worked examples, spacing algorithms, AI feedback, tutoring dialogue, learning analytics, collaborative learning, cognitive tutoring, self-explanation, metacognitive monitoring, productive failure, worked example transitions, formative assessment loops |
| 13 | [Montessori & Alternative Evidence-Based Approaches](montessori-alternative-approaches/) | 4 | Three-part lessons, prepared environment design, mixed-age learning, uninterrupted work cycles |
| 14 | [Original Frameworks](original-frameworks/) | 5 | SEEDS regenerative inquiry, developmental band systems, learning target authoring, rubric logic, self-determined project design |

## What Makes This Different

**Evidence is the filter.** Every skill is grounded in named research — specific authors, specific studies, specific findings. Where original practitioner frameworks are included (Domain 14), they are clearly labelled with honest evidence strength ratings. The library does not claim more than the research supports.

**Rigour includes knowing what to exclude.** Frameworks that lack empirical support — including learning styles, VAK, neuromyths, and similar widely-circulated but poorly-evidenced approaches — are not included. The library documents what is excluded and why in [EXCLUSIONS.md](EXCLUSIONS.md). This is a feature for any school trying to separate evidence from convention.

**Built by an educator.** This library was built by someone who has spent 20 years designing and teaching in international schools across 27 countries — not by someone who read about teaching. The pedagogical judgements embedded in every prompt, every output structure, and every known limitations section reflect real classroom experience.

**Designed for orchestration from day one.** YAML schema headers, typed input and output fields, chaining metadata, and composable outputs are built into every skill. This is not a prompt collection with metadata bolted on. It is a skill library engineered for programmatic use.

## Architecture

The library is Layer 1 of a three-layer system. See [ARCHITECTURE.md](ARCHITECTURE.md) for the full design.

**Layer 1 — Skill Library** (this repository, built and available now): 100 skills across 14 domains. Each skill encodes a specific, evidence-grounded instructional or curriculum design decision. Works standalone today.

**Layer 2 — Context Engine** (in development): Holds persistent information about students, classes, curriculum sequences, and assessment history. When connected, skill outputs become personalised — not generic advice about retrieval practice, but a specific retrieval schedule for this class based on what they have already learned and been assessed on.

**Layer 3 — Orchestrator** (in development): Allows an educator to state a high-level goal — "Design a 6-week unit on climate change for my Year 8 class" — and receive a complete, personalised plan assembled from multiple skills. The educator reviews, edits, and approves. The orchestrator proposes; the educator decides.

The library is complete and useful right now. The architecture shows where it is going.

## Credit

Built by **Gareth Manning** — educator, curriculum designer, and learning systems designer. 20 years of international education experience across 27 countries.

Follow the thinking: [garethmanning.substack.com](https://garethmanning.substack.com)

## Licence

[CC BY-SA 4.0](LICENSE). Open. Forkable. Share alike.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for inclusion criteria. The standard is high intentionally — every skill must be grounded in named evidence, honestly rated, and practically useful. The library's value depends on its rigour.
