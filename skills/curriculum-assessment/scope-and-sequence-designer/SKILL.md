---
# AGENT SKILLS STANDARD FIELDS (v2)
name: scope-and-sequence-designer
description: "Design a scope and sequence showing vertical and horizontal curriculum coherence across a programme or year. Use when building new programmes, restructuring subjects, or ensuring progression."
disable-model-invocation: false
user-invocable: true
effort: medium

# EXISTING FIELDS

skill_id: "curriculum-assessment/scope-and-sequence-designer"
skill_name: "Scope and Sequence Designer"
domain: "curriculum-assessment"
version: "1.0"
evidence_strength: "moderate"
evidence_sources:
  - "Bruner (1960) — The Process of Education: spiral curriculum and vertical coherence"
  - "Wiggins & McTighe (2005) — Understanding by Design: backwards design applied to programme-level planning"
  - "Bernstein (1999) — Vertical and horizontal discourse: hierarchical knowledge sequencing"
  - "Hattie (2009) — Visible Learning: curriculum coherence as a high-effect variable"
  - "Muller (2009) — Forms of knowledge and curriculum coherence: conceptual vs contextual coherence"
  - "Maton (2013) — Making semantic waves: cumulative knowledge-building across a programme"
  - "Schmidt, Wang & McKnight (2005) — Coherence of the intended, implemented, and attained curriculum"
  - "Duschl, Schweingruber & Shouse (2007) — Taking Science to School: learning progressions as programme architecture"
input_schema:
  required:
    - field: "subject_or_programme"
      type: "string"
      description: "Name and brief description of the subject or programme"
    - field: "developmental_bands"
      type: "string"
      description: "The band, year group, or stage structure used by the school or programme (e.g. Band A–D, Years 1–13, Foundation through Diploma, early childhood through upper secondary, or any other developmental architecture the school uses — this skill is not constrained to any particular system or age range)"
    - field: "intended_outcomes"
      type: "string"
      description: "The overarching goals students should reach by the end of the programme"
  optional:
    - field: "existing_units_or_competencies"
      type: "string"
      description: "Any existing units, competencies, or LTs already in place"
    - field: "knowledge_architecture_output"
      type: "string"
      description: "From curriculum-knowledge-architecture-designer if already run"
    - field: "time_available"
      type: "string"
      description: "Hours or lessons per week per band"
output_schema:
  type: "object"
  fields:
    - field: "knowledge_progression_map"
      type: "object"
      description: "For each knowledge type (hierarchical, horizontal, dispositional): how it develops across bands, what is introduced when, and what the prerequisite dependencies are between bands"
    - field: "vertical_coherence_check"
      type: "object"
      description: "For hierarchical knowledge: are prerequisites in place before each new concept is introduced? For horizontal knowledge: is sophistication of thinking increasing across bands? For dispositional knowledge: are development opportunities present and cumulative across the full programme?"
    - field: "horizontal_coherence_check"
      type: "object"
      description: "Within each band: is there appropriate balance between knowledge types? Are the units within the band connected or siloed?"
    - field: "sequencing_rationale"
      type: "object"
      description: "Explicit reasoning for why each major element is placed where it is, referenced to evidence about learning progressions"
    - field: "gaps_and_overlaps"
      type: "object"
      description: "Elements that are missing from the sequence, elements that are repeated without adding sophistication, and band transitions where students are likely to struggle"
    - field: "design_flags"
      type: "object"
      description: "Compound competencies that span multiple bands without clear progression logic, dispositional goals without sufficient knowledge prerequisites, and horizontal elements without explicit thinking development"
chains_well_with:
  - "curriculum-knowledge-architecture-designer"
  - "kud-knowledge-type-mapper"
  - "learning-target-authoring-guide"
  - "developmental-band-system-designer"
  - "backwards-design-unit-planner"
  - "competency-unpacker"
  - "learning-progression-builder"
  - "gap-analysis-from-student-work"
teacher_time: "15 minutes"
tags: ["scope-and-sequence", "curriculum-coherence", "vertical-coherence", "learning-progressions", "programme-design", "Bruner", "spiral-curriculum", "knowledge-types"]
---

# Scope and Sequence Designer

## What This Skill Does

Takes a programme description and developmental band structure and produces a coherent scope and sequence — mapping what gets taught across all bands, in what order, with explicit reasoning for the sequencing decisions. This skill works at any level of education: early childhood through upper secondary, undergraduate, professional development programmes, or any other staged learning architecture. Most scope and sequence documents are lists: topics assigned to year groups without coherent logic for why that topic sits there, what it builds on, or what it prepares students for. This skill produces a structured progression grounded in three knowledge types: hierarchical elements are sequenced by prerequisite logic so foundational knowledge is always in place before the next layer is introduced; horizontal elements are sequenced to build thinking sophistication progressively rather than repeating the same thinking moves at the same level year after year; dispositional elements are mapped as continuous threads with explicit identification of the knowledge prerequisites that must be in place before a disposition can meaningfully develop. The result is a programme where every element has a defensible reason for being where it is. AI is specifically valuable here because coherent programme design requires simultaneously tracking prerequisite chains across years, monitoring knowledge type balance within and across bands, and identifying gaps and overlaps that are invisible when looking at individual units in isolation — a level of systematic cross-referencing that is cognitively demanding and frequently skipped in real curriculum planning.

## Evidence Foundation

Bruner (1960) established the foundational principle of the spiral curriculum: key ideas should be revisited across year groups at increasing levels of sophistication, with each encounter building on prior encounters rather than repeating them. A scope and sequence that revisits a topic without increasing the cognitive demand is not a spiral — it is repetition. The spiral principle applies differently to the three knowledge types. Hierarchical knowledge spirals by adding new layers of complexity on top of secured foundations — fractions before algebra, cell biology before genetics. Horizontal knowledge spirals by increasing the sophistication of analytical thinking applied to recurring themes — a student who identifies perspectives at Band A should be evaluating and comparing analytical frameworks at Band D. Dispositional knowledge does not spiral in the same way — it develops continuously through enacted practice across the full programme, though the knowledge that supports dispositional expression deepens at each band.

Schmidt, Wang & McKnight (2005) analysed curriculum coherence across high-performing education systems and found that coherent curricula share three features: **focus** (fewer topics taught more deeply), **rigour** (appropriate challenge at each level), and **coherence** (topics connect logically within and across years). Systems that lack coherence — where topics appear and disappear without progression logic — consistently underperform. Their most significant finding for scope and sequence design is that coherence is not just a vertical property (does Band B build on Band A?) but also a horizontal property (do the elements within Band B connect to each other?). A programme can have perfect vertical sequencing and still lack coherence if the units within each band are isolated from each other.

Duschl, Schweingruber & Shouse (2007) developed the concept of **learning progressions**: empirically grounded descriptions of how student understanding develops across years, with each level building specifically on the previous one. Their work establishes that progression is not automatic — it requires deliberate curriculum design that matches what is taught to what students are ready to learn. Learning progressions are best documented for hierarchical knowledge domains (mathematics, early reading, some areas of science), where the prerequisite structure is well-researched. For horizontal and dispositional domains, progressions are less empirically established and must be constructed from developmental principles rather than from replicated research on specific learning sequences.

Wiggins & McTighe (2005) applied backwards design to programme-level planning: begin with the intended outcomes at the end of the programme, then work backwards to determine what must be in place at each stage to reach those outcomes. At the scope and sequence level, this means the final band's expectations determine what must be taught in every preceding band — not as direct preparation for a test, but as the knowledge and capability foundations that make the final outcomes achievable.

Bernstein (1999) and Muller (2009) establish the theoretical foundation for knowledge-type-specific sequencing. **Hierarchical knowledge** has an inherent sequencing logic: concepts must be taught in prerequisite order because later concepts genuinely depend on earlier ones. You cannot teach genetic inheritance before students understand cell division. **Horizontal knowledge** does not have prerequisite chains in the same way — different analytical lenses can be introduced in various orders — but it does have a sophistication progression: students should move from identifying perspectives to analysing through perspectives to evaluating and synthesising across perspectives. Sequencing horizontal knowledge by increasing analytical demand rather than by prerequisite dependency is one of the key distinctions this skill makes.

Maton (2013) adds the semantic wave concept: effective knowledge-building requires movement between abstract principles and concrete cases across a programme, not just within individual lessons. A scope and sequence that stays at the abstract level throughout produces disconnected theoretical knowledge; one that stays at the concrete level produces experience without conceptual development. Across a programme, the semantic profile should show increasing capacity to move between concrete and abstract — students at early bands work primarily with concrete cases and simple abstractions, while students at later bands should be able to operate fluently at multiple levels of abstraction and move between them deliberately.

Hattie (2009) identified curriculum coherence as a high-effect variable in student achievement. Programmes where students experience learning as a connected, cumulative journey produce better outcomes than programmes where each year feels like a fresh start with new content that does not obviously connect to what came before. This is the practical justification for investing in scope and sequence design: the coherence of the programme is a stronger predictor of student outcomes than the quality of any individual unit within it.

## Input Schema

The educator must provide:
- **Subject or programme:** Name and brief description. *e.g. "Wellbeing, REAL School Budapest" / "Science, Years 7–13" / "Interdisciplinary Humanities, Foundation through Diploma" / "Early Childhood Mathematics, ages 3–6"*
- **Developmental bands:** The band, year group, or stage structure. *e.g. "Bands A–D (approximately ages 5–15)" / "Years 7–13" / "Foundation, Intermediate, Advanced, Diploma" / "Nursery, Reception, Year 1, Year 2"*
- **Intended outcomes:** The overarching goals students should reach by the end of the programme. *e.g. "Students develop self-regulation, agency, care for others, and the scientific literacy to understand their own wellbeing" / "Students develop scientific reasoning, experimental design capability, and the knowledge base for further study at university level"*

Optional (injected by context engine if available):
- **Existing units or competencies:** Any existing units, competencies, or LTs already in place
- **Knowledge architecture output:** From curriculum-knowledge-architecture-designer if already run
- **Time available:** Hours or lessons per week per band

## Prompt

```
You are an expert in programme-level curriculum design, with deep knowledge of Bruner's (1960) spiral curriculum, Wiggins & McTighe's (2005) backwards design at the programme level, Bernstein's (1999) knowledge structures, Muller's (2009) forms of curriculum coherence, Maton's (2013) semantic wave concept, Schmidt, Wang & McKnight's (2005) research on curriculum coherence, Duschl, Schweingruber & Shouse's (2007) learning progressions, and Hattie's (2009) evidence on curriculum coherence as a predictor of student outcomes. You understand that different knowledge types require fundamentally different sequencing logic — hierarchical knowledge follows prerequisite chains, horizontal knowledge follows sophistication progressions, and dispositional knowledge develops as a continuous thread that requires sufficient domain knowledge to manifest meaningfully.

Your task is to produce a coherent scope and sequence for the following programme.

**Subject or programme:** {{subject_or_programme}}
**Developmental bands:** {{developmental_bands}}
**Intended outcomes:** {{intended_outcomes}}

The following optional context may or may not be provided. Use whatever is available; ignore any fields marked "not provided."

**Existing units or competencies:** {{existing_units_or_competencies}} — if provided, use as the starting point and evaluate coherence. If not provided, design from the intended outcomes.
**Knowledge architecture output:** {{knowledge_architecture_output}} — if provided, use the epistemic diagnosis as the foundation for sequencing decisions. If not provided, conduct a rapid knowledge architecture diagnosis as part of Step 1.
**Time available:** {{time_available}} — if provided, factor into pacing recommendations. If not provided, focus on sequencing logic without time constraints.

## The Three Sequencing Logics

You MUST sequence each knowledge type according to its own logic. Applying the wrong sequencing logic to a knowledge type produces incoherence.

**Hierarchical Knowledge — Prerequisite Sequencing (Bernstein, 1999)**
Hierarchical knowledge must be sequenced by prerequisite dependency. Concept B cannot be taught before Concept A if B genuinely depends on A. Map the full prerequisite chain across all bands. Identify where students are expected to use knowledge that has not yet been introduced — this is a sequencing error. Identify where the same content is repeated across bands without adding complexity — this is repetition, not spiral curriculum.

**Horizontal Knowledge — Sophistication Sequencing (Muller, 2009; Maton, 2013)**
Horizontal knowledge does not have strict prerequisites — different analytical lenses can be introduced in various orders. But the sophistication of thinking must increase across bands. Map a clear sophistication progression:
- **Emerging:** Students identify that different perspectives or approaches exist
- **Developing:** Students describe and compare perspectives, beginning to use them as analytical tools
- **Competent:** Students apply analytical frameworks to specific cases, evaluating their explanatory power
- **Extending:** Students synthesise across frameworks, critique their limitations, and construct their own analytical positions

If the same thinking demand is repeated across bands without increasing sophistication, this is not a spiral — it is a plateau.

**Dispositional Knowledge — Continuous Thread with Knowledge Prerequisites**
Dispositional knowledge develops across the full programme as a continuous thread — it is not "taught" in specific units and then finished. However, dispositions are not context-free: many dispositions require sufficient domain knowledge before they can meaningfully manifest. Self-regulation requires enough understanding of one's own cognitive and emotional processes to monitor them. Critical thinking requires enough domain knowledge to have something to think critically about. Ecological mindset requires enough scientific understanding to move beyond sentiment to informed action. For each dispositional element, identify the knowledge prerequisites that must be in place before the disposition can develop authentically at each band. A disposition listed at Band A that requires knowledge not introduced until Band C is a sequencing error — not because the disposition should be removed from Band A, but because the knowledge prerequisite must be introduced earlier, or the dispositional expectation at Band A must be calibrated to what students can actually do with the knowledge they have.

## Process

Follow these seven steps precisely. Each step produces a named section in the output.

**Step 1 — Knowledge Architecture Diagnosis.**
Before sequencing, identify what types of knowledge are present in this programme. If a knowledge architecture output is provided, use it. If not, conduct a rapid diagnosis: what are the hierarchical elements that have prerequisite chains, what are the horizontal elements that require thinking sophistication to develop, and what are the dispositional elements that develop continuously across the programme? List the major elements under each type. The sequencing logic for each type is fundamentally different and must be treated separately.

**Step 2 — Map Hierarchical Prerequisites Across Bands.**
For all hierarchical knowledge elements, establish the prerequisite chain explicitly. Which concepts must be in place before others can be introduced? Map these dependencies across the full band structure. Identify the earliest band at which each concept can be meaningfully introduced given what precedes it. Flag any element currently placed before its prerequisites are in place — this is a sequencing error that will produce gaps in student understanding.

**Step 3 — Map Horizontal Sophistication Progression.**
For all horizontal knowledge elements, describe what increasing sophistication looks like across bands. Students should not be doing the same thinking at the final band that they were doing at the first — the content may be similar but the analytical demand should be qualitatively different. For each horizontal element, specify: what does Emerging engagement look like, what does Developing engagement look like, what does Competent engagement look like, what does Extending engagement look like? Then place each band at the appropriate level of that progression.

**Step 4 — Map Dispositional Threads.**
For all dispositional elements, map them as continuous threads running across the full programme. Identify at which band each disposition can first meaningfully develop given the knowledge prerequisites required. A disposition cannot develop authentically before students have sufficient domain knowledge to enact it — identify those prerequisite thresholds explicitly. Mark where each disposition transitions from emerging to developing to deepening across the bands.

**Step 5 — Vertical Coherence Check.**
Read the full sequence from first band to last. For hierarchical elements: is every concept introduced after its prerequisites are secured? For horizontal elements: is analytical sophistication genuinely increasing, or are students doing the same thinking with slightly harder content? For dispositional elements: are development opportunities present throughout, or do they disappear in some bands? Flag every break in vertical coherence.

**Step 6 — Horizontal Coherence Check.**
Read each band independently. Is there appropriate balance between knowledge types within this band? Are the units within this band connected thematically or conceptually, or are they isolated topics that happen to share a timetable slot? Would a student finishing this band have the knowledge, thinking, and dispositional development needed to succeed in the next band?

**Step 7 — Produce Design Flags and Recommendations.**
Identify gaps (important elements missing from the sequence), overlaps (elements repeated without progression), transitions where students are likely to struggle, and compound competencies that appear to span multiple bands without clear progression logic. For each flag, provide a specific recommendation: where to move the element, how to add the missing prerequisite, or how to differentiate the element across bands to create genuine progression.

Return your output in this exact format:

## Scope and Sequence: [Programme Name]

**Programme:** [Summarised]
**Developmental bands:** [Band structure]
**Intended outcomes:** [Summarised]
**Time available:** [If provided; otherwise "Not specified"]

### 1. Knowledge Architecture Diagnosis

**Hierarchical elements:**
[List with brief description of each]

**Horizontal elements:**
[List with brief description of each]

**Dispositional elements:**
[List with brief description of each]

**Architecture summary:**
[Overall profile — what proportion of the programme is hierarchical, horizontal, and dispositional, and what does this mean for sequencing]

### 2. Hierarchical Prerequisite Map

| Concept | Prerequisites | Earliest Viable Band | Sequencing Notes |
|---|---|---|---|
| [Concept] | [What must come first] | [Band] | [Why here] |

**Prerequisite chain visualization:**
[Show the dependency chain across bands — which concepts build on which, and where the critical transitions are]

**Sequencing errors in existing curriculum:**
[If existing units/competencies provided: where elements are placed before their prerequisites. If not provided: "No existing curriculum provided for comparison."]

### 3. Horizontal Sophistication Progression

| Horizontal Element | Emerging (Band [first]) | Developing (Band [second]) | Competent (Band [third]) | Extending (Band [fourth]) |
|---|---|---|---|---|
| [Element] | [What thinking looks like] | [What thinking looks like] | [What thinking looks like] | [What thinking looks like] |

**Sophistication check:**
[Where is the progression genuinely increasing in analytical demand? Where is it repeating the same thinking with different content — plateau rather than spiral?]

### 4. Dispositional Threads

| Disposition | Knowledge Prerequisites | Earliest Meaningful Band | Progression Across Bands |
|---|---|---|---|
| [Disposition] | [What knowledge must be in place] | [Band] | [How it develops from emerging to deepening] |

**Knowledge-contingency flags:**
[Dispositions that require knowledge not yet introduced at the band where they are expected to develop]

### 5. Vertical Coherence Check

**Hierarchical coherence:**
[Are prerequisites in place at every transition? Flag breaks.]

**Horizontal coherence:**
[Is sophistication increasing? Flag plateaus.]

**Dispositional coherence:**
[Are development opportunities present throughout? Flag gaps.]

**Overall vertical coherence assessment:**
[Summary judgment: where is the programme coherent, and where does it break?]

### 6. Horizontal Coherence Check

**[Band name]:**
- Knowledge type balance: [Hierarchical / Horizontal / Dispositional proportions]
- Internal connections: [Are units within this band connected or siloed?]
- Readiness for next band: [Does this band prepare students for what follows?]

[Repeat for each band]

**Overall horizontal coherence assessment:**
[Summary judgment: which bands are well-balanced and connected, which are fragmented or imbalanced?]

### 7. Design Flags and Recommendations

**Gaps:**
[Elements missing from the sequence — with recommendation for where to add them]

**Overlaps:**
[Elements repeated without progression — with recommendation for how to differentiate across bands]

**Difficult transitions:**
[Band transitions where students are likely to struggle — with recommendation for bridging]

**Compound competencies:**
[Competencies that span multiple bands without clear progression logic — with recommendation for decomposition]

**Priority actions:**
[The 3–5 most important changes to make to improve programme coherence, in order of impact]

**Self-check before returning output:** Verify that (a) every hierarchical element has its prerequisites mapped explicitly, (b) every horizontal element has a four-level sophistication progression using the Emerging / Developing / Competent / Extending scale, (c) every dispositional element has its knowledge prerequisites identified, (d) the vertical coherence check flags specific breaks rather than offering generic assurance, (e) the horizontal coherence check examines each band independently, (f) design flags include specific recommendations not just identifications, and (g) the sequencing rationale references evidence about why elements are placed where they are.
```

## Example Output

**Scenario:** *Subject or programme: "Wellbeing, REAL School Budapest" / Developmental bands: "Bands A–D (approximately ages 5–15)" / Intended outcomes: "Students develop self-regulation, agency, care for others, and the scientific literacy to understand their own wellbeing" / Existing units or competencies: "Existing competencies: Self-Awareness & Regulation, Health Literacy & Habits, Reflective Thinking & Decision-Making, Social Awareness & Empathy, Communication & Collaboration. New competency being added: Wellbeing Science & Literacy (hierarchical knowledge of neuroscience, stress response, habits science)"*

---

## Scope and Sequence: Wellbeing, REAL School Budapest

**Programme:** Wellbeing — self-regulation, agency, care for others, scientific literacy for understanding own wellbeing
**Developmental bands:** Bands A–D (approximately ages 5–15)
**Intended outcomes:** Students develop self-regulation, agency, care for others, and the scientific literacy to understand their own wellbeing
**Time available:** Not specified

### 1. Knowledge Architecture Diagnosis

**Hierarchical elements:**
- **Wellbeing Science & Literacy** (new competency): Neuroscience of the stress response, brain structures involved in emotional processing, the HPA axis, cortisol and adrenaline pathways, the autonomic nervous system (sympathetic/parasympathetic), the physiological basis of calming techniques, habits science (cue-routine-reward loop, neuroplasticity), sleep science, nutrition and wellbeing connections
- **Health Literacy & Habits** (existing competency, partially hierarchical): Factual knowledge about physical health — nutrition basics, sleep hygiene, exercise science — that has right/wrong answers and prerequisite chains

**Horizontal elements:**
- **Reflective Thinking & Decision-Making** (existing competency): Analysing situations through multiple lenses, weighing competing considerations, evaluating the quality of one's own reasoning — thinking sophistication must increase across bands
- **Social Awareness & Empathy** (existing competency, partially horizontal): Understanding different perspectives, recognising that emotional responses are influenced by context, history, and interpretation — perspectival knowledge that deepens through analytical sophistication
- **Communication & Collaboration** (existing competency, partially horizontal): The quality of collaborative thinking, conflict resolution reasoning, and communication strategy must become more sophisticated, not just more frequent

**Dispositional elements:**
- **Self-Awareness & Regulation** (existing competency): Enacted self-regulation — noticing emotional escalation and choosing a response rather than reacting. This is a disposition, not a skill: it exists in patterns of behaviour over time, not in task performance
- **Agency** (intended outcome, not yet a named competency): The orientation toward taking purposeful action — not compliance and not defiance, but self-directed engagement with challenges. Develops as a continuous thread
- **Care for others** (intended outcome, not yet a named competency): The interpersonal disposition to notice and respond to others' wellbeing. Not the same as social awareness (which is partly horizontal knowledge) — care is enacted, not analysed
- **Health Literacy & Habits** (existing competency, partially dispositional): The habit dimension — actually maintaining routines that support wellbeing, as distinct from knowing what the routines should be

**Architecture summary:**
This programme is a **mixed architecture with a significant dispositional core and a new hierarchical strand**. The five existing competencies are primarily dispositional and horizontal — they describe ways of being and ways of thinking, not factual knowledge to be acquired. The addition of Wellbeing Science & Literacy introduces a genuinely hierarchical strand with prerequisite chains that must be respected. The central design challenge is connecting the hierarchical knowledge (neuroscience, stress science, habits science) to the dispositional goals (self-regulation, agency, care) — the science is not an end in itself but the knowledge foundation that makes the dispositions more informed, more intentional, and more effective. The sequencing must ensure that relevant science knowledge is in place at each band before the corresponding dispositional expectations assume students can draw on it.

### 2. Hierarchical Prerequisite Map

| Concept | Prerequisites | Earliest Viable Band | Sequencing Notes |
|---|---|---|---|
| Body awareness — identifying physical sensations associated with emotions (heart rate, breathing, muscle tension) | None — directly observable | Band A | Entry point for all wellbeing science. Children as young as 5 can learn to notice and name physical sensations. This is concrete, experiential knowledge that requires no abstract understanding. |
| Basic brain awareness — "the brain helps us feel emotions and make decisions" | Body awareness | Band A (late) | Age-appropriate simplification. Not neuroscience — just the concept that emotions have a physical basis in the brain. Prerequisite for later, more accurate models. |
| Emotions vocabulary — naming and distinguishing emotional states beyond basic categories | Body awareness | Band A–B | Builds on ability to notice physical sensations. Moves from "I feel bad" to "I feel frustrated because I expected to succeed." Vocabulary development is hierarchical — more nuanced terms build on basic ones. |
| Fight-flight-freeze response — the concept that the body has automatic responses to perceived threat | Body awareness, basic brain awareness | Band B | Requires understanding that the body responds physically to emotions. Introduces the idea of automatic (non-chosen) responses, which is prerequisite for understanding regulation as choosing a different response. |
| The amygdala and threat detection — the brain structure that detects potential threats rapidly | Fight-flight-freeze, basic brain awareness | Band C | Requires the concept of automatic threat responses. Introduces specific brain structures. Must be taught carefully to avoid the "amygdala controls emotions" misconception — the amygdala detects, it does not control. |
| The autonomic nervous system — sympathetic (activation) vs parasympathetic (recovery) | Fight-flight-freeze | Band C | Prerequisite for understanding why calming techniques work. Without this, techniques are just recipes — "breathe deeply because the teacher says so" rather than "diaphragmatic breathing activates the parasympathetic branch, which counteracts the stress response." |
| HPA axis — hypothalamus → pituitary → adrenal glands → cortisol | Amygdala and threat detection, autonomic nervous system | Band D | The full neuroendocrine pathway. Requires the concepts of threat detection and autonomic activation to make sense. This is the point at which students can understand the difference between acute stress (adrenaline, fast, adaptive) and chronic stress (cortisol, slow, harmful). |
| Acute vs chronic stress — different hormonal profiles, different physiological effects, different health implications | HPA axis | Band D | Requires the full pathway to understand why acute and chronic stress are physiologically different — not just "some stress is OK and some is bad" but the mechanism that makes them different. |
| Habits science — cue-routine-reward loop, neuroplasticity, habit formation and change | Basic brain awareness, body awareness | Band C | The cue-routine-reward loop is accessible at Band C. Neuroplasticity as a concept (the brain changes in response to repeated experience) provides the scientific basis for why habits form and can change. Prerequisite for informed habit design at Band D. |
| Sleep science — circadian rhythms, melatonin, sleep stages, impact of sleep on memory consolidation and emotional regulation | Autonomic nervous system, basic brain awareness | Band D | Requires understanding of the nervous system to explain why sleep is not just "rest" but an active physiological process. Connects to emotional regulation: sleep deprivation impairs prefrontal cortex function, reducing regulatory capacity. |

**Prerequisite chain visualization:**

```
Band A: Body awareness → Basic brain awareness → Emotions vocabulary
                                    ↓
Band B: Fight-flight-freeze response → [Emotions vocabulary continues developing]
                    ↓                           ↓
Band C: Amygdala & threat detection    Autonomic nervous system    Habits science
                    ↓                           ↓                       ↓
Band D: HPA axis ← ─ ─ ─ ─ ─ ─ ─ ─ ┘          Sleep science     [Habits deepens]
            ↓
        Acute vs chronic stress
```

**Sequencing errors in existing curriculum:**
The existing competencies do not include the Wellbeing Science & Literacy strand, so there is no existing hierarchical sequence to evaluate. However, the existing dispositional competencies (Self-Awareness & Regulation, Health Literacy & Habits) implicitly assume knowledge that is not currently taught. Students at Band C are expected to "select and apply strategies to manage emotional responses" (from existing LTs), but the science of why those strategies work (autonomic nervous system, parasympathetic activation) is not yet in the curriculum. This means students are selecting strategies based on teacher recommendation rather than scientific understanding — the strategy works, but the student does not know why, which limits their ability to adapt it to new situations. The addition of Wellbeing Science & Literacy addresses this gap.

### 3. Horizontal Sophistication Progression

| Horizontal Element | Emerging (Band A) | Developing (Band B) | Competent (Band C) | Extending (Band D) |
|---|---|---|---|---|
| Reflective Thinking & Decision-Making | **Identifies choices:** "I could do this or that." Describes what happened and what they chose. Reflection is descriptive and concrete — what I did, what happened next. | **Considers consequences:** "If I choose this, then..." Begins to think forward from choices. Reflection includes cause-effect reasoning — why something happened, not just what. | **Weighs competing considerations:** "This is better for X but worse for Y." Evaluates trade-offs. Reflection includes multiple perspectives and recognises that good decisions involve managing tensions, not finding perfect answers. | **Evaluates the quality of reasoning itself:** "My thinking was influenced by..." Analyses own reasoning processes, identifies biases and assumptions, and can articulate what would change their mind. Meta-reflective — thinking about thinking. |
| Social Awareness & Empathy (horizontal dimension) | **Recognises emotions in others:** "She looks sad." Identifies basic emotional states from observable cues. Perspective-taking is concrete — "how would I feel if that happened to me?" | **Understands that others may feel differently:** "He might feel differently about this than I do." Begins to recognise that emotional responses are shaped by individual experience and context — the same event does not produce the same emotion in everyone. | **Analyses how context shapes emotional response:** "She might be reacting that way because of what happened earlier." Understands that emotional responses have histories and contexts. Can consider how cultural, personal, and situational factors influence how people experience events. | **Evaluates the limits of empathy and perspective-taking:** "I can try to understand her perspective, but I can't fully know what it's like to be in her situation." Recognises that empathetic understanding is always partial, that projection of one's own experience onto others is a risk, and that genuine care sometimes means asking rather than assuming. |
| Communication & Collaboration (horizontal dimension) | **Takes turns, shares, listens when prompted:** Collaborative behaviour is present but requires teacher scaffolding. Communication is expressing needs and ideas — "I want..." / "I think..." | **Adjusts communication to the situation:** Begins to distinguish between contexts — how I talk to a friend vs how I present to the class. Collaboration includes role awareness — "in this group, I'm doing X." | **Navigates disagreement productively:** Can disagree with a peer's idea without personal conflict. Uses reasoning to support positions. Collaboration includes monitoring group dynamics — "we're getting stuck because we haven't heard from everyone." | **Facilitates and evaluates collaboration itself:** Can lead collaborative processes, identify when a group is dysfunctional and why, and adjust strategy. Evaluates the quality of collaborative outcomes — "we reached a decision, but did we consider all perspectives?" Communication includes audience awareness and rhetorical choice. |

**Sophistication check:**
The progressions above represent genuine increases in analytical demand, not just repetition with harder content. The key transitions to monitor:
- **Band A → B transition** for Reflective Thinking: moving from describing what happened to reasoning about causes and consequences. This is the shift from narrative to analytical, and some students will need explicit scaffolding to make it.
- **Band B → C transition** for Social Awareness: moving from "others feel differently" to "context explains why they feel differently." This requires enough psychological and social knowledge to reason about context — if the horizontal thinking outpaces the knowledge base, students will produce superficial contextual reasoning.
- **Band C → D transition** for all three elements: the shift to meta-level thinking (thinking about thinking, evaluating the quality of empathy, evaluating the quality of collaboration) is qualitatively demanding and requires explicit teaching of what meta-level reasoning looks like. Without modelling, students will stay at the Band C level with more complex content — a plateau, not a progression.

### 4. Dispositional Threads

| Disposition | Knowledge Prerequisites | Earliest Meaningful Band | Progression Across Bands |
|---|---|---|---|
| Self-Awareness & Regulation | **Band A:** Body awareness (can notice physical sensations). **Band B:** Fight-flight-freeze (understands that reactions are automatic, not chosen). **Band C:** Autonomic nervous system (understands WHY calming techniques work). **Band D:** HPA axis, acute vs chronic stress (can distinguish between adaptive and harmful stress and calibrate response accordingly). | Band A (in emergent form — with body awareness only) | **Band A:** Notices emotions through physical sensations; begins to use simple calming strategies (deep breaths, counting) because the teacher taught them. **Band B:** Understands that some reactions are automatic; begins to recognise the moment between trigger and response as a choice point. **Band C:** Understands the physiological basis of regulation strategies; selects techniques based on the type of arousal (parasympathetic activation for anxiety, movement for frustration). Regulation becomes informed, not just practised. **Band D:** Distinguishes between acute stress (useful — can be reframed) and chronic stress (harmful — requires systemic change, not just technique). Regulation includes recognising when individual strategies are insufficient and seeking support or changing the situation. |
| Agency | **Band A:** None — agency begins as "I can make choices." **Band B:** Reflective thinking at the Developing level (can consider consequences of choices). **Band C:** Reflective thinking at the Competent level (can weigh competing considerations). **Band D:** Meta-reflective capacity (can evaluate own decision-making processes). | Band A (in emergent form) | **Band A:** Makes choices within structured options provided by the teacher. Experiences the connection between choice and outcome. **Band B:** Initiates action on self-identified goals within a supported framework. Begins to plan and adjust. **Band C:** Designs and pursues self-directed projects with increasing independence. Navigates setbacks with developing resilience — can identify what went wrong and adjust approach. **Band D:** Takes purposeful action on self-identified problems with sustained commitment. Evaluates own agency patterns — recognises when they are defaulting to compliance or avoidance and can redirect. Agency is reflective and self-aware, not just active. |
| Care for others | **Band A:** Basic emotions vocabulary (can recognise when others are upset). **Band B:** Understanding that others feel differently (can recognise that their response may differ from what the other person needs). **Band C:** Contextual understanding of emotional responses (can consider why someone is struggling, not just that they are). **Band D:** Understanding the limits of empathy (can offer care without assuming they know what the other person needs). | Band A (in emergent form) | **Band A:** Notices when peers are upset and responds with simple kindness — offering comfort, including someone who is left out. Prompted by teacher modelling. **Band B:** Begins to ask what others need rather than assuming. Recognises that care sometimes means giving space, not just giving attention. **Band C:** Considers the context behind others' struggles. Care becomes more nuanced — responds differently to a friend who is upset about a grade vs a friend who is upset about a family situation. **Band D:** Offers care while respecting others' autonomy. Recognises that wanting to help is not the same as being helpful. Can identify when care requires action, when it requires presence, and when it requires stepping back. |
| Health Literacy & Habits (dispositional dimension) | **Band A:** Body awareness, basic understanding that some actions help you feel well. **Band B:** Basic health knowledge (sleep, nutrition, exercise). **Band C:** Habits science (cue-routine-reward, neuroplasticity). **Band D:** Sleep science, stress science — understanding the physiological basis of habits and their connection to emotional and cognitive function. | Band A (in emergent form — "things that help me feel good") | **Band A:** Identifies activities that make them feel well or unwell. Begins simple routines with teacher support (morning check-in, movement breaks). **Band B:** Understands the connection between health behaviours and how they feel and learn. Begins to maintain personal routines with decreasing teacher prompting. **Band C:** Designs personal wellbeing routines based on habits science — can identify the cue, routine, and reward structure of their own habits and deliberately modify them. **Band D:** Maintains and adjusts wellbeing practices based on self-monitoring. Understands why habits are physiologically powerful (neuroplasticity) and why they are difficult to change. Can distinguish between evidence-based wellbeing practices and wellness industry claims that lack evidence. |

**Knowledge-contingency flags:**
- **Self-Awareness & Regulation at Band C** currently expects students to "select and apply strategies to manage emotional responses in different situations." This is only meaningful if the autonomic nervous system content (why techniques work) has been taught. If Wellbeing Science & Literacy is introduced at Band C but regulation expectations already exist at Band C, there is a timing question: the science must precede the expectation, not run in parallel. **Recommendation:** Introduce autonomic nervous system content in the first term of Band C; adjust regulation expectations to reflect informed strategy selection from the second term onward.
- **Health Literacy & Habits at Band D** expects students to evaluate wellness claims against evidence. This requires not just habits science (Band C) but also basic scientific reasoning about evidence — controlled studies, correlation vs causation, sample size. If this scientific reasoning is not taught elsewhere in the curriculum, it must be included in the Wellbeing Science & Literacy strand. **Recommendation:** Check whether the science curriculum covers basic experimental design and evidence evaluation by Band D. If not, add a brief unit on "evaluating health claims" to the Wellbeing Science & Literacy strand at Band D.
- **Agency at Band D** expects meta-reflective capacity — evaluating one's own decision-making processes. This requires the Reflective Thinking & Decision-Making competency to be at the Extending level. If a student's reflective thinking is still at the Competent level (Band C), their agency at Band D will be enacted but not reflective. **Recommendation:** This is a horizontal-to-dispositional dependency. Ensure that the Reflective Thinking progression is on track before assuming Agency at Band D can be fully meta-reflective.

### 5. Vertical Coherence Check

**Hierarchical coherence:**
The proposed Wellbeing Science & Literacy prerequisite chain is coherent: body awareness (A) → fight-flight-freeze (B) → amygdala, autonomic nervous system, habits science (C) → HPA axis, acute vs chronic stress, sleep science (D). Each concept builds on the previous, and no concept is introduced before its prerequisites are in place. The one risk is **density at Band C**: three new hierarchical concepts (amygdala, autonomic nervous system, habits science) are introduced simultaneously. If time is limited, the autonomic nervous system should be prioritised over the other two, because it is the prerequisite for understanding why calming techniques work — which directly supports the Self-Awareness & Regulation competency at Band C.

**Horizontal coherence:**
Reflective Thinking, Social Awareness (horizontal dimension), and Communication & Collaboration all show genuine sophistication increases across bands. The critical transition to monitor is **Band C → D**, where all three shift to meta-level thinking. If this transition is not explicitly taught — if teachers assume students will naturally begin thinking about their thinking — it will not happen for most students. **Recommendation:** Include explicit teaching of meta-reflective skills at the start of Band D, modelling what it looks like to evaluate one's own reasoning, empathetic responses, and collaborative contributions.

**Dispositional coherence:**
All four dispositional threads (Self-Regulation, Agency, Care, Habits) are present across all four bands with increasing expectations. No dispositional thread disappears at any band. However, there is a risk at **Band B** that the dispositional threads are developing based on teacher modelling and practice alone, without sufficient knowledge support. Band B introduces fight-flight-freeze but the other hierarchical content is minimal. This means Self-Regulation at Band B is largely practice-based ("use these techniques because they work") rather than knowledge-informed ("use these techniques because they activate the parasympathetic nervous system"). This is developmentally appropriate for Band B — the knowledge base will arrive at Band C — but teachers must understand that Band B regulation is experiential, not scientific, and that the transition to informed regulation happens at Band C.

**Overall vertical coherence assessment:**
The programme is vertically coherent with two areas requiring attention: (1) the density of new hierarchical content at Band C, which may require careful pacing, and (2) the Band C → D transition for horizontal elements, which requires explicit teaching of meta-level thinking rather than assuming it will emerge.

### 6. Horizontal Coherence Check

**Band A:**
- Knowledge type balance: Primarily dispositional and concrete experiential. Hierarchical content is minimal (body awareness, basic brain awareness, emotions vocabulary). Horizontal content is at the Emerging level (identifying choices, recognising emotions in others). This balance is developmentally appropriate — Band A students learn primarily through experience and practice.
- Internal connections: Strong. Body awareness connects to emotions vocabulary connects to noticing others' emotions connects to simple regulation strategies. The competencies are naturally linked through the embodied experience of emotions.
- Readiness for next band: Students leaving Band A should be able to name emotions, notice physical sensations associated with them, and use simple calming strategies. This prepares them for the fight-flight-freeze concept at Band B.

**Band B:**
- Knowledge type balance: Dispositional threads continue. Hierarchical content adds fight-flight-freeze. Horizontal content moves to Developing level. Balance is appropriate but the hierarchical strand is thin — only one new concept. This is acceptable if the concept is taught with sufficient depth.
- Internal connections: Moderate. The fight-flight-freeze concept connects to Self-Regulation (understanding that reactions are automatic) and to Social Awareness (understanding that others' reactions are also automatic). But the connection between the scientific concept and the dispositional practice needs to be made explicit by teachers — it is not self-evident to Band B students.
- Readiness for next band: Students leaving Band B should understand that emotional reactions have an automatic physiological component, should be able to consider consequences of choices, and should be beginning to recognise that others experience situations differently. This prepares them for the more demanding content at Band C.

**Band C:**
- Knowledge type balance: The most demanding band. Three new hierarchical concepts (amygdala, autonomic nervous system, habits science), horizontal elements at Competent level (weighing competing considerations, analysing contextual influences on emotion, navigating disagreement), and dispositional expectations that now assume informed, science-based practice. Risk of overload.
- Internal connections: Potentially strong but complex. The autonomic nervous system content directly supports informed self-regulation. Habits science directly supports the habits competency. The horizontal progression in Reflective Thinking supports the agency competency. But these connections span competencies — if competencies are taught in isolation (one unit on regulation, one on habits, one on reflective thinking), students may not see the connections. **Recommendation:** Design at least one cross-competency unit at Band C that explicitly connects the science to the dispositions — e.g. a project where students design a personal regulation toolkit based on their understanding of the autonomic nervous system.
- Readiness for next band: Students leaving Band C should have the scientific foundation for Band D's more advanced content and should be practising informed self-regulation and evidence-based habits. The gap to Band D is primarily in the shift to meta-level thinking (horizontal) and in the advanced neuroscience (HPA axis, acute vs chronic stress).

**Band D:**
- Knowledge type balance: All three types at their most demanding levels. Hierarchical content reaches full complexity (HPA axis, acute vs chronic stress, sleep science). Horizontal content reaches Extending level (meta-reflective thinking, evaluating limits of empathy, facilitating collaboration). Dispositional expectations require fully informed, self-directed practice. This band has the most cognitive demand and the most content.
- Internal connections: The strongest potential connections in the programme. Understanding the HPA axis connects directly to understanding why chronic stress is harmful, which connects to the habits competency (maintaining wellbeing routines), which connects to agency (taking purposeful action to protect one's own wellbeing), which connects to care for others (recognising when others are experiencing chronic stress and responding appropriately). If these connections are made explicit, Band D is a powerful synthesis. If they are taught as separate units, it fragments.
- Readiness for programme completion: Students completing Band D should be able to explain the neuroscience of their own stress response, regulate using science-informed strategies, maintain evidence-based wellbeing practices, exercise reflective agency, and care for others with nuance and respect for autonomy. This meets the programme's intended outcomes.

**Overall horizontal coherence assessment:**
Bands A and B are well-balanced with manageable content loads. Band C is the critical pressure point — high content density with complex cross-competency connections. Band D is demanding but potentially the most coherent if the connections between science, thinking, and dispositions are made explicit. The primary recommendation is to ensure Band C has sufficient time allocation and that at least one unit at Band C explicitly bridges the science-to-disposition connection.

### 7. Design Flags and Recommendations

**Gaps:**
- **Scientific reasoning about evidence** is required at Band D (evaluating wellness claims) but is not included in the Wellbeing Science & Literacy strand. Students need to understand what counts as evidence for a health claim — controlled studies, sample size, correlation vs causation. Either add this to the wellbeing programme or verify it is covered in the science curriculum by Band D.
- **Agency is not currently a named competency.** The intended outcomes include agency, and the dispositional thread analysis maps it across all four bands, but it does not appear in the existing competency structure. **Recommendation:** Either add Agency as a sixth competency or ensure it is explicitly embedded within Self-Awareness & Regulation and Reflective Thinking & Decision-Making — but if embedded, it must be named and tracked, not assumed.
- **Care for others is not currently a named competency.** Same issue as agency. The Social Awareness & Empathy competency covers the horizontal knowledge dimension (understanding perspectives) but not the dispositional dimension (enacted care). **Recommendation:** Either add Care as a competency or split Social Awareness & Empathy into a horizontal strand (analytical) and a dispositional strand (enacted).

**Overlaps:**
- **Self-Awareness & Regulation** and **Health Literacy & Habits** overlap in the area of "strategies for managing wellbeing." Both competencies include elements of recognising what works for you and applying it. The distinction — regulation is about emotional responses in the moment, habits are about sustained routines — must be made explicit to teachers, or the same content will be taught twice under different competency names. **Recommendation:** Define the boundary clearly: Self-Awareness & Regulation covers in-the-moment emotional response; Health Literacy & Habits covers ongoing routines and practices. Where they overlap (e.g. a breathing technique used both as an in-the-moment strategy and as a daily practice), name the overlap explicitly.
- **Reflective Thinking & Decision-Making** and the meta-reflective dimension of **Self-Awareness & Regulation** at Band D overlap. Reflecting on one's own emotional regulation patterns IS reflective thinking. **Recommendation:** At Band D, design assessment tasks that integrate both competencies rather than assessing them separately — a reflective portfolio on personal regulation development would serve both.

**Difficult transitions:**
- **Band B → C** is the most significant transition in the programme. Students move from experiential, practice-based wellbeing learning to science-informed, analytically demanding learning. Three new hierarchical concepts, a step up in horizontal thinking sophistication, and the expectation of informed rather than practised dispositional engagement. Students who were confident at Band B may struggle at Band C if the transition is abrupt. **Recommendation:** Begin Band C with a bridging unit that connects Band B's experiential knowledge to the new scientific content — e.g. "You already know that deep breathing calms you down. Now we're going to learn WHY it works — and that understanding will help you choose the right technique for different situations."
- **Band C → D** for horizontal elements: the shift to meta-level thinking (thinking about thinking, evaluating empathy, evaluating collaboration) is a qualitative leap that many students will not make spontaneously. **Recommendation:** Explicit modelling of meta-reflective thinking at the start of Band D. Show students what it looks like to evaluate one's own reasoning process, not just one's conclusions.

**Compound competencies:**
- **Health Literacy & Habits** is compound across knowledge types: it includes hierarchical knowledge (nutrition, sleep, exercise science), horizontal thinking (evaluating health claims), and dispositional practice (maintaining routines). The same competency is being sequenced by three different logics simultaneously. **Recommendation:** Consider splitting into Health Knowledge (hierarchical — assessed by knowledge tests and structured responses) and Wellbeing Practice (dispositional — assessed through self-reflection and developmental conversation). Alternatively, keep it as one competency but ensure that the assessment approach is differentiated by knowledge type — the factual knowledge is assessed differently from the enacted habits.

**Priority actions (in order of impact):**
1. **Ensure autonomic nervous system content is taught at the START of Band C** before regulation expectations assume students understand why techniques work. This is the highest-impact sequencing decision because it transforms regulation from practice-based to science-informed.
2. **Design a cross-competency bridging unit at the start of Band C** that connects experiential Band B learning to scientific Band C content. This manages the most difficult transition in the programme.
3. **Add scientific reasoning about evidence** (what counts as a valid health claim) to the Wellbeing Science & Literacy strand at Band D, or verify it is covered in the science curriculum.
4. **Make Agency and Care for Others explicitly named and tracked** — either as separate competencies or as clearly identified strands within existing competencies. Unnamed intended outcomes are not assessed and tend to be neglected.
5. **Define the boundary between Self-Awareness & Regulation and Health Literacy & Habits** explicitly for teachers, so both competencies are taught with clear scope rather than overlapping coverage.

---

## Known Limitations

1. **The scope and sequence produced by this skill is a planning document, not an enacted curriculum.** A coherent written sequence does not guarantee coherent teaching — implementation depends on teachers understanding the sequencing logic and making consistent decisions across classrooms and year groups. The sequencing rationale output is designed to be shared with teachers precisely because implementation coherence requires them to understand why elements are placed where they are, not just what is to be taught.

2. **Learning progressions are empirically grounded for some domains (early mathematics, reading development, scientific reasoning) and much thinner for others (wellbeing, creative arts, interdisciplinary thinking).** Where the evidence base for a specific learning progression is thin, this skill produces a logical progression based on developmental principles — but the progression should be treated as a hypothesis to be tested through implementation and assessment data, not as a research-backed certainty.

3. **This skill produces a recommended sequence; it cannot enforce it.** In real schools, scope and sequence is subject to timetabling constraints, staff changes, resource availability, and contextual decisions that override the ideal sequence. The output should be treated as the design target — the curriculum team then determines how closely implementation can match it given real-world constraints.

4. **The three-type knowledge framework used for sequencing is a simplification.** Real knowledge elements often sit on boundaries between types, and the sequencing logic for boundary cases requires professional judgment that this skill can prompt but not replace. Where elements are classified as primarily one type for sequencing purposes, the classification should be made explicit so teachers understand the reasoning.

5. **Scope and sequence design is never finished.** As students move through the programme, assessment data will reveal where the sequence is working and where it is producing gaps or struggles. The scope and sequence designer produces the best available plan given current knowledge — it should be reviewed and revised at least annually using real student outcome data. The gap-analysis-from-student-work skill is the natural tool for feeding that data back into sequence revision.
