# Architecture

The Education Skill Library is Layer 1 of a three-layer system designed for progressive enhancement — each layer adds capability without requiring changes to the layers below.

---

## Layer 1: Skills (this library)

Atomic, callable units. Each skill takes a defined input, applies evidence-based processing, and returns a structured output.

### Design principles

- **Standalone and composable.** Every skill works when a teacher invokes it directly. Every skill also works when an orchestrator chains it with other skills.
- **Machine-readable schema.** Every skill file begins with a YAML header that defines inputs, outputs, evidence strength, and chaining relationships. This enables automated discovery, selection, and sequencing.
- **Evidence encoded in the prompt.** The research criteria are inside the prompt itself — Claude evaluates its own output against named research standards, not just against plausibility.
- **Context-engine ready.** Input schemas include optional fields that the context engine can inject. Skills produce high-quality generic output without context; they produce tailored output with it.

### Schema header format

Every skill file begins with a YAML front matter block containing:

```yaml
---
skill_id: "domain/skill-name"
skill_name: "Human-Readable Name"
domain: "domain-name"
version: "1.0"
evidence_strength: "strong"        # strong | moderate | emerging
evidence_sources: [...]            # Specific citations with dates
input_schema:
  required: [...]                  # What the teacher must provide
  optional: [...]                  # What the context engine can inject
output_schema:
  type: "object"
  fields: [...]                    # Structured output description
chains_well_with: [...]            # Related skill IDs
teacher_time: "X minutes"         # Time to use this skill
tags: [...]                        # For discovery and filtering
---
```

### File structure

```
education-skills/
  README.md
  EVIDENCE.md
  EXCLUSIONS.md
  ARCHITECTURE.md
  LICENSE
  schemas/
    skill-schema.yaml
  memory-learning-science/         # Domain 1: 8 skills
  self-regulated-learning/         # Domain 2: 5 skills
  explicit-instruction/            # Domain 3: 5 skills
  questioning-discussion/          # Domain 4: 4 skills
  literacy-critical-thinking/      # Domain 5: 7 skills
  eal-language-development/        # Domain 6: 5 skills
  curriculum-assessment/           # Domain 7: 9 skills
  wellbeing-motivation-agency/     # Domain 8: 5 skills
  professional-learning/           # Domain 9: 4 skills
```

---

## Layer 2: Context Engine (not built yet)

The layer that makes outputs specific rather than generic. When connected, a skill doesn't just know "Year 8 EAL students" — it knows *these* students.

### What the context engine provides

- **Student profiles:** language proficiency levels, prior knowledge gaps, working memory profiles, learning preferences (evidence-based, not learning styles), IEP/504 accommodations
- **Curriculum data:** what's been taught, what's coming, scope and sequence, standards alignment
- **Assessment data:** recent results, growth trajectories, specific gaps identified
- **School context:** competency framework, reporting system, assessment calendar, house/pastoral structure
- **Class context:** group dynamics, seating, timetable constraints

### How it connects to skills

Context engine data flows into skills through the `optional` fields in each skill's input schema. Skills are designed to use this data when available and produce quality output without it.

```
Teacher input (required fields)
       +
Context engine data (optional fields)
       ↓
    Skill prompt
       ↓
  Tailored output
```

---

## Layer 3: Orchestrator (not built yet)

An agent that receives a high-level teacher goal and fulfils it by selecting, sequencing, and chaining skills.

### Example orchestration

**Teacher goal:** "Design a 6-week climate change unit for my Year 9 science class"

**Orchestrator sequence:**
1. Query context engine for: class profile, curriculum requirements, prior learning, upcoming assessments
2. Invoke `curriculum-assessment/backwards-design-unit-planner` with curriculum standards
3. For each lesson, invoke `explicit-instruction/lesson-opening-designer`
4. Invoke `memory-learning-science/spaced-practice-scheduler` across the 6-week timeline
5. Invoke `memory-learning-science/interleaving-unit-planner` to restructure topic sequence
6. Invoke `curriculum-assessment/rubric-generator` for the summative assessment
7. Invoke `eal-language-development/language-demand-analyser` for EAL students
8. Present complete unit plan for teacher review and modification

### Orchestrator design principles

- **Teacher approval gates.** The orchestrator proposes; the teacher decides. No autonomous action on student-facing outputs.
- **Skill chaining via schemas.** The orchestrator reads `output_schema` from one skill and matches it to `input_schema` of the next. The `chains_well_with` field provides hints but the orchestrator can discover novel chains.
- **Transparency.** The teacher can see which skills were invoked, in what order, with what inputs. No black box.

---

## Build Sequence

1. **Phase 1** (complete): Builder brief and architecture design
2. **Phase 2** (current): Build all 52 skills as markdown files with YAML headers
3. **Phase 3**: Test against real classrooms — D2R programme and wellbeing class
4. **Phase 4**: Build the orchestrator agent
5. **Phase 5**: Context engine integration (Kaku)

---

*This architecture is designed so that each layer adds value independently. The skills work now. The context engine makes them better. The orchestrator makes them effortless.*
