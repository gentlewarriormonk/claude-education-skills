# Education Skill Library — Builder Brief v2
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
skill_name: "Retrieval Practice Question Generator"
domain: "learning-science"
version: "1.0"
evidence_strength: "strong"  # strong | moderate | emerging
evidence_sources:
  - "Roediger & Butler (2011) — The critical role of retrieval practice in long-term retention"
  - "Karpicke & Roediger (2008) — The critical importance of retrieval for learning"
  - "Rowland (2014) — The effect of testing versus restudy on retention"
input_schema:
  required:
    - field: "topic"
      type: "string"
      description: "The specific concept or skill students need to retrieve"
    - field: "student_level"
      type: "string"
      description: "Age/year group and approximate prior knowledge level"
    - field: "question_count"
      type: "integer"
      description: "Number of questions to generate"
  optional:
    - field: "student_profiles"
      type: "array"
      description: "From context engine: language levels, prior knowledge gaps"
    - field: "competency_framework"
      type: "string"
      description: "From context engine: school's assessment framework"
output_schema:
  type: "object"
  fields:
    - field: "questions"
      type: "array"
      description: "List of retrieval questions with type labels"
    - field: "spacing_recommendation"
      type: "string"
      description: "When to use these questions relative to original learning"
    - field: "answer_notes"
      type: "string"
      description: "Key points for correct answers"
chains_well_with:
  - "spaced-practice-scheduler"
  - "formative-assessment-designer"
  - "gap-analysis-from-student-work"
teacher_time: "3 minutes"
tags: ["retrieval", "memory", "assessment", "spaced-practice"]
---
```

---

## Skill Template

```markdown
---
[YAML schema header as above]
---

# [Skill Name]

## What This Skill Does

[2-3 sentences. Problem solved. Output produced. Why AI help is specifically valuable here — not just "saves time" but what expertise it encodes.]

## Evidence Foundation

[3-5 sentences. Specific research tradition. Key findings. Specific citations with dates. If evidence is contested or implementation effects differ from lab effects, say so here.]

## Input Schema

The teacher must provide:
- **[Field]:** [Description. Example in italics: *e.g. "photosynthesis" / "the water cycle" / "quadratic equations"*]

Optional (injected by context engine if available):
- **[Field]:** [Description]

## Prompt

[The actual Claude prompt. Must include:]
- [Expert role framing with specific expertise — not "you are a helpful teacher" but "you are an expert in cognitive psychology specialising in memory consolidation"]
- [The evidence-based criteria Claude applies to evaluate its own output — make the research explicit *inside* the prompt]
- [Explicit output format: structure, headers, length, what to include and exclude]
- [Input placeholders: {{double_brackets}} for required fields]
- [Optional field handling: list ALL optional fields with their {{placeholder}} and a plain-English fallback instruction — e.g. "**Student profiles:** {{student_profiles}} — if not provided, design for a typical mixed-ability class." Do NOT use Handlebars conditionals ({{#if}}...{{/if}}) — Claude cannot parse these natively. Instead, present all optional fields in a block prefaced by "The following optional context may or may not be provided. Use whatever is available; ignore any fields marked 'not provided.'"]
- [A self-check instruction: "Before returning output, verify that each question requires genuine reconstruction not just recognition"]

## Example Output

[A realistic, high-quality example for a specific scenario. This is the quality bar. If this example wouldn't impress a senior teacher or learning scientist, the prompt needs more work.]

## Known Limitations

[1-3 honest, specific statements. Where does this skill underperform? What teacher judgment does it require? What contexts is it unsuitable for?]
```

---

## The Expanded Skill List — 52 Skills Across 7 Domains

*Research basis for each domain noted. Build Domain 1 first, review quality before continuing.*

---

### Domain 1: Memory & Learning Science
*Core evidence base: cognitive psychology of learning — Roediger, Bjork, Ebbinghaus, Sweller, Hattie. The most tightly evidenced domain. Build first.*

1. **Retrieval Practice Question Generator** — generates questions that force genuine reconstruction, not recognition. Distinguishes free recall, cued recall, and recognition types. Includes spacing recommendation. *Evidence: Roediger & Butler (2011), Karpicke & Roediger (2008), Rowland meta-analysis (2014). Effect sizes consistently 0.5–1.0.*

2. **Spaced Practice Schedule Builder** — takes a topic list and learning timeline, generates optimised review schedule with rationale. *Evidence: Ebbinghaus forgetting curve (1885/1913), Cepeda et al. (2006) meta-analysis of 254 studies, Kornell & Bjork (2008). Effect size ~0.6.*

3. **Interleaving Unit Planner** — restructures a blocked topic sequence to interleave related but distinct concepts, explains the desirable difficulty principle to teacher. *Evidence: Kornell & Bjork (2008), Rohrer et al. (2015), Taylor & Rohrer (2010). Note: interleaving feels harder and students often rate it worse — this is a feature, not a bug.*

4. **Cognitive Load Analyser** — evaluates a task, instruction, or resource for intrinsic (complexity), extraneous (unnecessary), and germane (schema-building) load. Produces specific modification suggestions. *Evidence: Sweller (1988, 1994), Paas & van Merriënboer (1994), Sweller et al. (2019) updated theory.*

5. **Worked Example Designer with Completion Fading** — designs a scaffold sequence from full worked example → completion problem → independent practice for a specific skill. *Evidence: Sweller & Cooper (1985), Atkinson et al. (2000), Renkl (2014). Especially effective for novice learners.*

6. **Elaborative Interrogation Prompt Generator** — generates "why?" and "how does this connect to?" prompts that deepen encoding. *Evidence: Pressley et al. (1992), Woloshyn et al. (1994). More effective than re-reading. Effect size ~0.59.*

7. **Feedback Quality Analyser & Rewriter** — evaluates teacher or peer feedback text against Hattie & Timperley's four-level model (task, process, self-regulation, self). Rewrites feedback to improve level and specificity. *Evidence: Hattie & Timperley (2007), highest effect size intervention in education research (~0.73).*

8. **Dual Coding Designer** — takes a verbal explanation and designs a complementary visual representation (diagram type, spatial layout, annotation strategy). *Evidence: Paivio (1986) dual coding theory, Clark & Paivio (1991). Not to be confused with learning styles — this is about *complementary* representations, not *preferred* modality.*

---

### Domain 2: Self-Regulated Learning & Metacognition
*Core evidence base: Zimmerman, Pintrich, Flavell, Veenman, Hattie & Donoghue. SRL is among the highest-leverage interventions in education research.*

9. **Self-Regulation Scaffold Generator** — produces phase-appropriate SRL supports (goal-setting, strategy selection, monitoring prompts, reflection) for a specific task and age group. *Evidence: Zimmerman (2000, 2002) cyclical SRL model, Pintrich (2000). SRL interventions: effect size ~0.69.*

10. **Metacognitive Prompt Library** — generates calibrated metacognitive prompts for a specific task (monitoring comprehension, evaluating strategy effectiveness, detecting errors). *Evidence: Flavell (1979), Veenman et al. (2006), Hattie meta-analysis on metacognitive strategies.*

11. **Goal-Setting Protocol Designer** — generates a structured goal-setting protocol (proximal, specific, process-focused) for a unit or project. *Evidence: Locke & Latham (1990) goal-setting theory, Zimmerman & Bandura (1994) on self-efficacy and goal proximity.*

12. **Study Strategy Selector & Guide** — analyses a learning task and recommends the most evidence-supported study strategy, with explicit instruction guide. *Evidence: Dunlosky et al. (2013) — landmark review rating 10 study techniques. Highlights retrieval practice and distributed practice as highest utility; dismisses highlighting, rereading, summarising as low utility.*

13. **Error Analysis Protocol** — structures analysis of student errors to distinguish procedural errors, conceptual misunderstandings, and careless mistakes. Generates targeted follow-up. *Evidence: Borasi (1994) on error as learning opportunity, Black & Wiliam (1998) formative assessment.*

---

### Domain 3: Explicit & Direct Instruction
*Core evidence base: Rosenshine, Engelmann, Hattie, Slavin. Direct instruction is the most replicated high-effect intervention in education, especially for foundational skills.*

14. **Explicit Instruction Sequence Builder (I Do / We Do / You Do)** — generates a complete gradual release sequence for a specific skill. *Evidence: Rosenshine's Principles of Instruction (2012), Pearson & Gallagher (1983) gradual release model. Effect size consistently high.*

15. **Checking for Understanding Protocol Designer** — generates a set of CFU techniques appropriate for a specific lesson stage, including cold calling scripts, mini-whiteboards, exit tickets, hinge questions. *Evidence: Rosenshine (2012) Principle 6, Wiliam (2011) on formative assessment techniques.*

16. **Lesson Opening Designer** — generates an evidence-based lesson opening: retrieval hook, prior knowledge activation, learning intention framing. *Evidence: Rosenshine (2012) Principle 1, Ausubel (1960) on advance organisers, Marzano (2007).*

17. **Think-Aloud Script Generator** — scripts a teacher think-aloud that makes expert cognitive processes visible for a specific task (problem-solving, reading, writing). *Evidence: Bereiter & Scardamalia (1987), Wilhelm (2001), Ericsson & Simon (1993) verbal protocol analysis.*

18. **Practice Problem Sequence Designer** — designs a practice problem sequence that follows principles of distributed difficulty, scaffold reduction, and format variation. *Evidence: Rosenshine (2012) Principles 5 & 8, Rohrer (2009) on practice.*

---

### Domain 4: Questioning, Discussion & Dialogue
*Core evidence base: Mercer, Alexander, Michaels, Paul & Elder, Resnick. Dialogic teaching has strong evidence, especially in comprehension and reasoning.*

19. **Socratic Questioning Sequence Generator** — generates a progression of questions to develop a concept through dialogue, distinguishing Socratic from leading questions. *Evidence: Paul & Elder (2008) critical thinking framework, Chin (2007) teacher questioning in science.*

20. **Discussion Protocol Selector & Facilitation Guide** — selects appropriate protocol (Socratic seminar, Harkness, fishbowl, think-pair-share, Philosophic Chairs) with facilitation guide and teacher moves. *Evidence: Resnick et al. (2015) accountable talk research, Michaels et al. (2008).*

21. **Dialogic Teaching Move Generator** — takes a specific student response and generates high-quality teacher follow-up moves (revoicing, pressing, inviting, challenging). *Evidence: Mercer (2000) interthinking, Alexander (2008) dialogic teaching, Michaels et al. (2008).*

22. **Hinge Question Designer** — creates a single multiple-choice question that efficiently reveals student understanding and reveals specific misconceptions, with diagnostic key. *Evidence: Wiliam (2011), Christodoulou (2017) on hinge questions. Requires careful distractor design.*

---

### Domain 5: Literacy, Writing & Critical Thinking
*Core evidence base: Graham & Perin, Duke & Pearson, Wineburg, Toulmin, genre pedagogy / systemic functional linguistics.*

23. **Argument Structure Scaffold Generator** — produces a genre-specific argument scaffold (Toulmin, PEEL, historical argument, scientific claim-evidence-reasoning). *Evidence: Toulmin (1958) on argument structure, Graham & Perin (2007) Writing Next synthesis.*

24. **Disciplinary Writing Scaffold** — produces a scaffold for a specific disciplinary genre (lab report, historical argument, literary analysis, mathematical explanation). *Evidence: Systemic functional linguistics / genre pedagogy — Halliday, Martin, Christie. Writing in disciplines is not generic.*

25. **Reading Comprehension Strategy Selector** — identifies appropriate comprehension strategies for a specific text type and reader challenge, with implementation guide. *Evidence: Pressley et al. (2002), Duke & Pearson (2002), National Reading Panel (2000). Note: strategy instruction is most effective for intermediate/advanced readers; beginners need decoding first.*

26. **Source Credibility Evaluation Protocol** — generates a structured lateral reading protocol for evaluating a specific source type. *Evidence: Wineburg & McGrew (2017, 2019) — lateral reading outperforms vertical reading for source evaluation. SIFT method operationalises the research.*

27. **Text Complexity Analyser & Scaffold Designer** — evaluates a text for qualitative and quantitative complexity, generates appropriate before/during/after scaffolds. *Evidence: CCSS text complexity model (quantitative + qualitative + reader/task), Shanahan et al. on text complexity.*

28. **Media Literacy Deconstruction Protocol** — generates a structured analysis framework for a specific media type (advertisement, news article, social media post, film). *Evidence: Hobbs (2010), Buckingham (2003), media literacy research traditions.*

29. **Critical Thinking Task Designer** — designs a task requiring genuine critical evaluation (not just comprehension), with criteria for distinguishing critical from surface response. *Evidence: Paul & Elder (2008), Facione (1990) Delphi report on critical thinking. Note: "critical thinking skills" cannot be taught generically — they are domain-specific.*

---

### Domain 6: EAL/D & Language Development
*Core evidence base: Cummins, Gibbons, Beck et al., Krashen (with appropriate caveats), Vygotsky. Note: Krashen's Input Hypothesis is influential but contested — use with caveats.*

30. **Language Demand Analyser** — identifies the language demands of a task across four dimensions: vocabulary (Tier 1/2/3), grammar (complexity, tense, voice), discourse (text structure, cohesion), and genre (purpose, audience, format). Suggests scaffolds for each. *Evidence: Cummins (1981, 2000) BICS/CALP framework, Gibbons (2002, 2015).*

31. **Vocabulary Tiering Tool** — takes a text or topic, tiers all vocabulary (Tier 1: everyday, Tier 2: academic, Tier 3: technical), generates teaching sequence prioritising Tier 2. *Evidence: Beck, McKeown & Kucan (2002, 2013). Tier 2 vocabulary is the highest-leverage intervention for academic language development.*

32. **Scaffolded Task Modifier** — adapts a task for a specific language proficiency level while *explicitly maintaining* cognitive demand. *Evidence: Gibbons (2002) on scaffolding that challenges rather than simplifies, Cummins quadrant model. The key risk is scaffolding cognitive demand away, not just language — this skill guards against that.*

33. **Academic Language Sentence Frame Generator** — generates sentence frames and discourse markers appropriate for a specific task type and proficiency level. *Evidence: Gibbons (2015), Zwiers (2014) academic language toolkit.*

34. **Sheltered Instruction Lesson Modifier** — adapts a content lesson using SIOP model principles: content objectives, language objectives, building background, comprehensible input, interaction, practice. *Evidence: Echevarría, Vogt & Short (2008) SIOP model. Strongest evidence base for content-area EAL instruction.*

---

### Domain 7: Curriculum Design & Assessment
*Core evidence base: Wiggins & McTighe, Black & Wiliam, Wiliam, Brookhart, Marzano, Hattie & Timperley.*

35. **Competency Unpacker** — takes a standard, learning objective, or competency descriptor and unpacks it into: observable indicators, prerequisite knowledge, common misconceptions, and success criteria at multiple levels. *Evidence: Wiggins & McTighe (1998, 2005) UbD, Marzano & Kendall (2007).*

36. **Backwards Design Unit Planner** — generates a Stage 1–2–3 UbD unit structure from desired outcomes: enduring understandings, essential questions, assessment evidence, learning plan. *Evidence: Wiggins & McTighe (1998, 2005). One of the most replicated curriculum design frameworks.*

37. **Criterion-Referenced Rubric Generator** — produces a rubric from a learning objective and task description: 4 criteria, 4 performance levels, descriptive (not evaluative) language. *Evidence: Brookhart (2013), Andrade (2000, 2013). Research on rubric design: descriptive language outperforms evaluative labels.*

38. **Assessment Validity Checker** — evaluates a proposed assessment against validity (does it measure what it claims?), reliability (would different markers agree?), and authenticity (meaningful task). Flags specific threats to validity. *Evidence: Wiliam (2011), Messick (1989) unified validity framework.*

39. **Formative Assessment Technique Selector** — selects the most appropriate formative assessment technique for a specific learning moment (during instruction, end of task, between lessons), with implementation guide. *Evidence: Black & Wiliam (1998), Wiliam (2011) — formative assessment has one of the highest effect sizes in education research (~0.66).*

40. **Differentiation Adapter** — adapts a task for a specific learner profile (extension, support, EAL, ADHD, dyslexia) while maintaining the same learning intention. *Evidence: Tomlinson (2001), UDL framework (Rose & Meyer, 2002). Note: differentiation by learning style is excluded — differentiation by readiness, interest, and learning profile is supported.*

41. **Gap Analysis from Student Work** — analyses a student work sample against rubric criteria, identifies specific gaps, generates targeted next teaching steps rather than generic feedback. *Evidence: Black & Wiliam (1998), Hattie & Timperley (2007).*

42. **Learning Progression Builder** — maps the learning progressions from novice to expert for a specific skill domain, identifying prerequisite relationships and common stuck points. *Evidence: learning progressions research — Heritage (2008), Popham (2007).*

43. **Project Brief Designer (PBL)** — generates a project brief with driving question, real-world connection, milestones, and assessment criteria using PBL design principles. *Evidence: Barron & Darling-Hammond (2008), Krajcik & Shin (2014). Note: PBL effects are strongest when projects include explicit instruction, not instead of it.*

---

### Domain 8: Wellbeing, Motivation & Student Agency
*Core evidence base: Deci & Ryan SDT, Hattie & Donoghue, Zimmerman, Bandura, Fredrickson. This domain matters enormously to Gareth's D2R programme and should be built with care.*

44. **Motivation Diagnostic & Task Redesign** — analyses a learning task through SDT lens (autonomy, competence, relatedness) and suggests specific modifications that enhance intrinsic motivation without reducing rigour. *Evidence: Deci & Ryan (1985, 2000) Self-Determination Theory — the most robust motivational framework in education research. Note: extrinsic rewards can undermine intrinsic motivation when used for tasks already intrinsically interesting.*

45. **Self-Efficacy Builder Sequence** — designs a task sequence that systematically builds self-efficacy through mastery experiences, appropriate challenge, and attribution training. *Evidence: Bandura (1977, 1997) — self-efficacy is the strongest individual-level predictor of learning outcomes in Hattie's meta-analysis.*

46. **Wellbeing-Learning Connection Mapper** — maps the connections between a wellbeing intervention and specific learning outcomes, generating evidence-based rationale for school leadership. *Evidence: Hattie (2009) on student background factors, Fredrickson (2001) broaden-and-build theory, Roffey (2012) on school wellbeing.*

47. **Agency Scaffold Generator** — generates scaffolds that progressively release decision-making to students: choice of topic, process, audience, product, criteria. *Evidence: Zimmerman SRL, Deci & Ryan autonomy support research. Agency is the throughline of D2R — this skill directly supports the programme.*

48. **Belonging & Classroom Culture Designer** — generates specific classroom practices that build belonging for marginalised students. *Evidence: Walton & Cohen (2011) belonging uncertainty research, Yeager & Walton (2011) social-psychological interventions.*

---

### Domain 9: Professional Learning & Teacher Development
*Core evidence base: Timperley, Darling-Hammond, Hattie & Timperley. Often overlooked in skill libraries — this is the domain where the skill library can support teacher PD, not just lesson planning.*

49. **Lesson Observation Protocol Designer** — generates a structured observation protocol focused on a specific teaching practice, with evidence-based look-fors and feedback prompts. *Evidence: Darling-Hammond (2010), Timperley et al. (2007) Teacher Professional Learning and Development.*

50. **Reflective Practice Prompt Generator** — generates structured post-lesson reflection prompts calibrated to a specific teaching challenge or professional learning goal. *Evidence: Timperley (2011) on teacher inquiry as professional learning, Schön (1983) reflective practitioner.*

51. **Professional Development Session Designer** — designs a PD session using adult learning principles: problem-based, collaborative, connected to practice, with follow-through planning. *Evidence: Timperley et al. (2007) BES on professional learning — most effective PD is sustained, content-specific, and involves active practice.*

52. **Student Data Interpretation Guide** — guides a teacher through interpreting a specific dataset (test results, survey responses, assessment portfolio) to identify patterns and generate next steps. *Evidence: Wiliam (2011) on data use, Hattie (2009) on visible learning.*

---

## Build Sequence

Phase 1 (now): Build the brief and architecture (this document).
Phase 2 (Claude Code): Build all 52 skills as markdown files with YAML headers and full template.
Phase 3 (testing): Test against D2R programme and wellbeing class — real students, real curriculum, real assessment system. These are the first context layer prototypes.
Phase 4 (orchestrator): After skills are stable and tested, build the orchestrator agent that chains them.
Phase 5 (Kaku): Context engine integration — student data, curriculum data, assessment data injected into skills at runtime.

---

## Build Instructions for Claude Code

**For each skill, in this order:**

1. Research the evidence base. Write 3-5 specific citations with dates. If you can't name specific authors and studies, you don't know the evidence well enough to build the skill.
2. Write the YAML schema header. Define input/output types precisely.
3. Write the input schema. What does a teacher actually know and can provide in under 2 minutes?
4. Write the prompt. The evidence-based criteria must be *inside* the prompt — Claude should be evaluating its output against research standards, not just generating plausible educational content. Include a self-check instruction.
5. Write a realistic example output. This is your quality gate. Would a learning scientist be satisfied? Would a senior teacher find it immediately useful?
6. Write Known Limitations. Every skill has them. Be honest and specific.

**Hard rules:**
- Never use "research shows" without naming who and what.
- Never produce outputs that are lists of suggestions without structure.
- If the evidence base is contested, say so in Known Limitations. Don't hide it.
- If a skill overlaps with something in the exclusion list, flag it and get human review.
- Build Domain 1 completely, then review the batch for quality before continuing.

---

## Quality Checklist (per skill)

- [ ] YAML schema header complete and machine-parseable?
- [ ] Evidence claims name specific authors and studies?
- [ ] Input schema realistic for a teacher with 2 minutes?
- [ ] Prompt encodes research criteria explicitly?
- [ ] Example output impressive to a senior teacher AND a learning scientist?
- [ ] Known Limitations honest and specific?
- [ ] Chains_well_with populated with relevant skill IDs?
- [ ] No reference to excluded pseudoscientific practices?

---

## Repository Structure

```
education-skills/
  README.md               (public-facing: what this is, inclusion criteria, how to contribute)
  EVIDENCE.md             (the research canon this library draws on)
  EXCLUSIONS.md           (explicitly debunked practices and why they're excluded)
  ARCHITECTURE.md         (three-layer system design for contributors building on top)
  LICENSE                 (CC BY-SA 4.0)
  schemas/
    skill-schema.yaml     (JSON Schema for validating skill YAML headers)
  memory-learning-science/
    01-retrieval-practice-generator.md
    02-spaced-practice-scheduler.md
    03-interleaving-unit-planner.md
    04-cognitive-load-analyser.md
    05-worked-example-fading-designer.md
    06-elaborative-interrogation-generator.md
    07-feedback-quality-analyser.md
    08-dual-coding-designer.md
  self-regulated-learning/
    09-self-regulation-scaffold-generator.md
    ...
  explicit-instruction/
    ...
  questioning-discussion/
    ...
  literacy-critical-thinking/
    ...
  eal-language-development/
    ...
  curriculum-assessment/
    ...
  wellbeing-motivation-agency/
    ...
  professional-learning/
    ...
```

---

## What Distinguishes This from Everything Else

There are hundreds of "education prompt libraries" and "AI for teachers" tools. Most are garbage: generic, weakly evidenced, or built by people who don't know what good teaching looks like.

This library is different because:
1. **Evidence is the filter, not an afterthought.** Skills are built from research, not from "this seems useful."
2. **Bullshit is explicitly excluded** — with documented reasons. This is a feature for schools trying to avoid snake oil.
3. **Expertise is encoded in the prompt.** A teacher using Skill 1 gets the benefit of deep knowledge of retrieval practice research, even if they've never heard of Roediger.
4. **Designed for the future.** Orchestration-ready schemas mean this library can become the intelligence layer of a full curriculum AI system — which is what Kaku will be.
5. **Built by someone who knows education.** 20 years, 27 countries, actual classroom implementation.

---

*Built by Gareth Manning. CC BY-SA 4.0. Contributions welcome — all submissions reviewed against inclusion criteria.*
