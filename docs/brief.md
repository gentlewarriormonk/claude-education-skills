# Education Skill Library — Builder Brief v3
*For Claude Code. Read this entire document before writing a single skill.*
*Revised: March 2026 — expanded scope, three-layer architecture, orchestration-ready design.*

---

## Vision

A curated library of Claude skills for educators — the most rigorous, evidence-grounded, practically useful curriculum intelligence system that exists. Not a prompt library. Not a chatbot collection. A **doing engine**: atomic, composable skills that produce concrete, immediately usable outputs, designed from the start to work alone (teacher-invoked) and together (agent-orchestrated).

Eventually, this library becomes the intelligence layer inside Kaku. Right now, it's the most valuable open-source contribution to education technology that can be built with Claude today.

**Licence:** CC BY-SA 4.0. Open. Forkable. Contributions must meet inclusion criteria.

---

## The Three-Layer Architecture

Understanding this architecture is essential before building anything.

### Layer 1: Skills (what you're building now)
Atomic, callable units. Each skill takes a defined input, applies evidence-based processing, and returns a structured output. Skills are the primitives. They must work standalone AND be composable — designed so outputs from one skill can be inputs to another.

### Layer 2: Context Engine (Kaku's data layer — not built yet)
The layer that makes outputs specific rather than generic. When connected, a skill doesn't just know "Year 8 EAL students" — it knows *these* students: their language proficiency levels, prior knowledge gaps from last term's assessments, working memory profiles, what's been taught, what's coming, which competency framework the school uses, what the reporting system requires.

Without the context engine: outputs are high-quality generic templates.
With the context engine: outputs are tailored to specific students, specific curriculum, specific school.

Design skills so the context engine can inject additional context as optional parameters — don't assume generic, don't require specific.

### Layer 3: Orchestrator (not built yet)
An agent that receives a high-level teacher goal ("design a 6-week climate change unit for this class"), queries the context engine, selects and sequences the right skills, chains their outputs, and presents a complete result for teacher review and feedback.

**The orchestration-ready requirement:** Every skill must have a machine-readable schema header so the orchestrator can discover, select, and chain skills automatically. Build this now. Build the orchestrator later.

---

## The Three Tensions (unchanged — still the core design constraint)

Every skill sits at the intersection of three competing demands. Lose any one and the skill fails.

**1. Rigour (the learning scientist's demand)**
Every claim must be grounded in replicable, peer-reviewed evidence. Name the source. If the evidence is thin or contested, the skill either gets cut or explicitly flags it in Known Limitations. The cone of experience, learning styles, brain gym, left/right brain dominance, multiple intelligences as a *teaching style* prescription — these are not thin evidence, they are **debunked**. They don't get footnotes. They get excluded.

**2. Usability (the teacher's demand)**
A teacher has 20 minutes. A specific class. A specific problem. Inputs must be things they actually know. Outputs must be copy-pasteable or directly actionable. If the teacher needs to do significant further thinking to use the output, the skill has failed.

**3. Specificity (the prompt engineer's demand)**
Precise input schema. Explicit output format. Enough constraint that two teachers with similar inputs get consistently structured, high-quality outputs. No vague prompts producing vague outputs.

---

## Inclusion Criteria

A skill earns its place only if it meets **all three**:

1. **Evidenced** — grounded in a named, well-established research tradition. Not "research shows." *Which* research. *Who.*
2. **Concrete output** — produces something specific and usable. Not suggestions. Not advice. A *thing* the teacher can use.
3. **High expertise threshold** — would take significant time or specialist knowledge to do well without AI.

---

## The Explicit Exclusion List

These are debunked, poorly evidenced, or so generic they fail the expertise threshold. Do not include, reference, or allude to:

- **Learning styles (VARK, Dunn & Dunn, etc.)** — no credible evidence that matching teaching to preferred learning style improves outcomes. Pashler et al. (2008) systematic review is definitive.
- **Cone of Learning / Learning Pyramid** — misattributed to Edgar Dale, who never made the percentage claims. The "10% from reading, 90% from teaching others" figures are fabricated. Completely.
- **Brain Gym** — no neurological basis. Pseudoscience marketed to schools.
- **Left brain / right brain dominance as teaching framework** — debunked by neuroimaging research. Nielsen et al. (2013).
- **Multiple Intelligences as teaching prescription** — Gardner's MI theory describes intelligence, not learning. The "teach to each student's intelligence type" application is not supported by evidence. Gardner himself has objected to this use.
- **Bloom's Taxonomy as a hierarchy of quality** — Bloom's is a classification system, not a hierarchy where "higher-order" tasks are always better. Misuse of Bloom's is endemic. Use it precisely or not at all.
- **Growth Mindset interventions as currently implemented** — Dweck's research is real; the school implementation literature shows weak and inconsistent effects at scale. If used, caveat heavily.
- **Grit as a teachable trait** — Duckworth's work is interesting but the interventions designed to build grit in schools have very weak evidence.
- **VAK (Visual/Auditory/Kinaesthetic) learning** — variant of learning styles. Same problem. Excluded.
- **Most "21st Century Skills" frameworks** — often vague, weakly evidenced, and produce generic suggestions. Only include if the specific skill (e.g., lateral reading from Wineburg) has its own strong evidence base.

---

## Machine-Readable Schema Header

Every skill file must begin with this YAML header before the human-readable content. This enables orchestration.

```yaml
---
skill_id: "learning-science/retrieval-practice-generator"
domain: "learning-science"
name: "Retrieval Practice Question Generator"
version: "1.0"
evidence_strength: "strong"        # strong | moderate | emerging | practitioner
requires_context_engine: false     # true = needs Kaku data layer to be useful
chains_well_with:
  - "learning-science/spaced-practice-scheduler"
  - "assessment/formative-question-bank"
input_type: "topic + year_group + prior_knowledge_level"
output_type: "structured_question_set"
tags: ["retrieval", "memory", "formative-assessment"]
---
```

**Field definitions:**
- `evidence_strength`: strong = multiple meta-analyses; moderate = consistent RCTs; emerging = promising early research; practitioner = field-tested, no formal research base
- `requires_context_engine`: if true, this skill needs student/curriculum data to produce useful output. Mark honestly — don't pretend a skill works generically if it doesn't.
- `chains_well_with`: skill_ids this skill's output can feed into as inputs

---

## Skill File Template

```markdown
---
[YAML header as above]
---

# [Skill Name]

## What This Skill Does
[1-2 sentences. What concrete output does this produce? Start with the output, not the process.
Why AI help is specifically valuable here — not just "saves time" but what expertise it encodes.]

## Evidence Foundation
[3-5 sentences. Specific research tradition. Key findings. Specific citations with dates. If evidence is contested or implementation effects differ from lab effects, say so here.]

## Input Schema

The teacher must provide:
- **[Field]:** [Description. Example in italics: *e.g. "photosynthesis" / "the water cycle" / "quadratic equations"*]

Optional (injected by context engine if available):
- **[Field]:** [Description]

## Prompt

[The actual Claude prompt. Must include:]
- [Expert role framing with specific expertise]
- [The evidence-based criteria Claude applies to evaluate its own output]
- [Explicit output format: structure, headers, length, what to include and exclude]
- [Input placeholders: {{double_brackets}}]
- [A self-check instruction]

## Example Output

[A realistic, high-quality example for a specific scenario.]

## Known Limitations

[1-3 honest, specific statements.]
```

---

## Build Sequence

- Phase 1 (now): Build the brief and architecture (this document).
- Phase 2 (Claude Code): Build all skills as markdown files with YAML headers and full template.
- Phase 3 (testing): Test against D2R programme and wellbeing class.
- Phase 4 (orchestrator): After skills are stable and tested, build the orchestrator agent.
- Phase 5 (Kaku): Context engine integration.

---

## Build Instructions for Claude Code

**For each skill, in this order:**

1. Research the evidence base. Write 3-5 specific citations with dates.
2. Write the YAML schema header.
3. Write the input schema.
4. Write the prompt. Evidence-based criteria must be *inside* the prompt.
5. Write a realistic example output.
6. Write Known Limitations.

**Hard rules:**
- Never use "research shows" without naming who and what.
- Never produce outputs that are lists of suggestions without structure.
- If the evidence base is contested, say so in Known Limitations.
- If a skill overlaps with the exclusion list, flag it.
- Build Domain 1 completely, then review before continuing.

---

## The 106 Skills Across 14 Domains

### Domain 1: Memory & Learning Science (10 skills)

1. Retrieval Practice Question Generator
2. Spaced Practice Schedule Builder
3. Interleaving Unit Planner
4. Cognitive Load Analyser
5. Worked Example Designer
6. Desirable Difficulty Task Designer
7. Elaborative Interrogation Prompt Generator
8. Self-Explanation Protocol Designer
9. Dual Coding Activity Designer
10. Prior Knowledge Activation Designer

### Domain 2: Formative Assessment & Feedback (8 skills)

1. Exit Ticket Designer
2. Hinge Question Designer
3. Feedback Quality Analyser
4. Live Observation Note Converter
5. Misconception Diagnostic Designer
6. Success Criteria Generator
7. Peer Assessment Protocol Designer
8. Whole-Class Feedback Template

### Domain 3: Curriculum Design (8 skills)

1. Backwards Design Unit Planner
2. Concept Map Generator
3. Prerequisite Knowledge Mapper
4. Transfer Task Designer
5. Threshold Concept Identifier
6. Curriculum Coherence Analyser
7. Cross-Curricular Connection Finder
8. Spiral Curriculum Planner

### Domain 4: Differentiation & Inclusion (8 skills)

1. Tiered Task Designer
2. EAL Scaffold Generator
3. Worked Example Adaptation Tool (SEN)
4. Universal Design for Learning Checklist
5. Gifted Extension Task Designer
6. Reading Level Adaptor
7. Sensory Processing Accommodation Designer
8. Executive Function Scaffold Designer

### Domain 5: Questioning & Discussion (7 skills)

1. Socratic Seminar Question Designer
2. Bloom's Question Spectrum Builder
3. Cold Call Protocol Designer
4. Think-Pair-Share Optimiser
5. Discussion Facilitation Guide
6. Philosophical Enquiry Prompt Generator
7. Accountable Talk Stem Generator

### Domain 6: Metacognition & Self-Regulation (8 skills)

1. Implementation Intention Designer
2. Self-Regulation Strategy Selector
3. Metacognitive Reflection Prompt Generator
4. Goal-Setting Protocol Designer
5. Study Strategy Recommender
6. Affect Regulation Activity Designer
7. Attention Management Protocol
8. Self-Assessment Rubric Designer

### Domain 7: Project-Based Learning (7 skills)

1. Driving Question Designer
2. Project Milestone Planner
3. Authentic Audience Identifier
4. PBL Rubric Generator
5. Entry Event Designer
6. Exhibition Planning Guide
7. PBL Reflection Protocol

### Domain 8: Wellbeing & Positive Education (8 skills)

1. PERMA-Based Lesson Designer
2. Strengths-Based Feedback Generator
3. Psychological Safety Audit
4. Belonging Activity Designer
5. Stress & Anxiety Psychoeducation Sequence
6. Mindfulness Integration Designer
7. Gratitude Practice Designer
8. Purpose & Ikigai Exploration Sequence

### Domain 9: Professional Learning & Coaching (7 skills)

1. Instructional Coaching Conversation Guide
2. Lesson Study Protocol Designer
3. Video Analysis Protocol
4. Peer Observation Framework
5. Professional Learning Community Facilitator Guide
6. Teacher Reflection Prompt Generator
7. Student Data Interpretation Guide

### Domain 10: Media Literacy & Critical Thinking (8 skills)

1. Lateral Reading Protocol Designer
2. SIFT Framework Lesson Designer
3. Source Credibility Analyser
4. Argument Mapping Tool
5. Logical Fallacy Identifier
6. Claim-Evidence-Reasoning Designer
7. Bias Detection Activity Designer
8. Misinformation Inoculation Lesson Designer

### Domain 11: Entrepreneurial & Agency Skills (7 skills)

1. Ikigai Exploration Sequence
2. Design Thinking Sprint Designer
3. Prototyping Protocol Designer
4. Pitch Feedback Protocol
5. Opportunity Identification Activity
6. Risk Tolerance Activity Designer
7. Agency Self-Assessment Designer

### Domain 12: AI-Enhanced Learning Design (7 skills)

1. Adaptive Hint Sequence Designer
2. Erroneous Example Designer
3. Digital Worked Example Sequence
4. Individual Spacing Algorithm Explainer
5. AI Feedback Design Principles
6. Intelligent Tutoring Dialogue Designer
7. Learning Analytics Interpretation Guide

### Domain 13: Montessori & Alternative Evidence-Based Approaches (4 skills)

1. Three-Part Lesson Designer (Montessori)
2. Prepared Environment Designer
3. Mixed-Age Learning Task Designer
4. Uninterrupted Work Cycle Designer

### Domain 14: D2R, SEEDS & Gareth's Original Frameworks (8 skills)

> ⚠️ **This domain requires a dedicated briefing session with Gareth Manning before building. Do not approximate or infer from names alone. Wait for the briefing.**

Every skill in this domain must begin its "What This Skill Does" section with:
*"This skill encodes an original practitioner framework developed by Gareth Manning at REAL School Budapest. Unlike skills in other domains, it is not drawn from peer-reviewed research traditions. It is grounded in 20 years of international education experience and is being actively tested in real classroom contexts."*

1. 7-Stage D2R Project Cycle Designer
2. SEEDS Observation & Documentation Protocol
3. Developmental Band Competency Designer
4. Curriculum Outcome Decomposition Tool
5. Coherent Rubric Logic Builder
6. D2R Assessment Evidence Mapper
7. Habit Design Curriculum Sequence
8. Competency Framework to Developmental Band Mapper

---

## Supporting Files to Build After All 14 Domains

1. **README.md** — leads with "works right now, any teacher with Claude can use this today."
2. **ARCHITECTURE.md** — reframe as "composable and extensible."
3. **IMPLEMENTATIONS.md** — Strive, Hippo, Ren, Kaku connections.
4. **CONTRIBUTING.md** — inclusion criteria for external contributors.
5. **MCP server** (new repo: `claude-education-skills-mcp`) — exposes skills as callable Claude tools. MIT licence.

---

*Brief last updated: March 2026 — v3. Domains 10–14 added.*
