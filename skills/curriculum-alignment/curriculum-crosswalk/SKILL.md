---
name: curriculum-crosswalk
description: Compares two or more band-tagged frameworks and produces a PLC-ready document showing convergence, divergence, unique content, sequencing differences, and questions for teacher discussion.
disable-model-invocation: false
user-invocable: true
effort: high
skill_id: curriculum-alignment/curriculum-crosswalk
skill_name: Curriculum Crosswalk
domain: curriculum-alignment
version: "1.0"
evidence_strength: moderate
evidence_sources:
  - "Webb, N. L. (1997) — Criteria for Alignment of Expectations and Assessments in Mathematics and Science Education, CCSSO Research Monograph No. 6: the canonical four-dimension alignment framework (categorical concurrence, depth-of-knowledge consistency, range-of-knowledge correspondence, balance of representation); this skill operationalises categorical concurrence and range at the school-band level."
  - "Porter, A. C. (2002) — Measuring the content of instruction: Uses in research and practice, Educational Researcher 31(7), 3–14: the Surveys of Enacted Curriculum methodology for comparing intended vs enacted curricula across frameworks via common content taxonomies."
  - "Porter, A. C., Smithson, J., Blank, R. & Zeidner, T. (2007) — Alignment as a teacher variable, Applied Measurement in Education 20(1), 27–51: alignment indices and content-matrix methodology applied across standards documents."
  - "Case, B. J., Jorgensen, M. A. & Zucker, S. (2004) — Alignment in Educational Assessment, Pearson Assessment Report: practical alignment procedures that surface rather than hide framework differences — the rationale for the divergence and unique-content tables in this skill's output."
  - "Martone, A. & Sireci, S. G. (2009) — Evaluating alignment between curriculum, assessment, and instruction, Review of Educational Research 79(4), 1332–1361: literature review establishing that alignment studies should preserve framework distinctiveness rather than collapse to a lowest-common-denominator schema — the design principle behind this skill's refusal to produce a merged mega-framework."
input_schema:
  required:
    - field: reference_framework_band_tagged
      type: string
      description: The reference framework, already band-tagged using the Developmental Band Translator. Its band labels define the comparison axis for all tables. Must include source_metadata, band_tagged_kud (or equivalent content-bearing items), and band_tagged_lts.
    - field: comparison_frameworks_band_tagged
      type: string
      description: Array of one or more comparison frameworks, each produced by the Developmental Band Translator. Each entry must include source_metadata, band_tagged_kud (or equivalent content-bearing items), and band_tagged_lts.
  optional:
    - field: reference_framework_name
      type: string
      description: Human-readable name of the reference framework for output labelling. Defaults to source_name from reference_framework_band_tagged metadata if omitted.
    - field: focus_bands
      type: string
      description: Restrict the crosswalk to a subset of school bands (e.g. "D,E" for secondary-focused PLC). If omitted, all bands are covered.
    - field: focus_themes
      type: string
      description: Restrict to specific thematic areas (e.g. "consent, relationships"). If omitted, all content is compared.
    - field: plc_context
      type: string
      description: A short description of the PLC context (e.g. "Band D/E wellbeing team preparing for September 2026 planning"). The skill uses this to tune the Questions for PLC section.
output_schema:
  type: object
  fields:
    - field: crosswalk_document
      type: string
      description: A Markdown document intended for direct use by a teacher or PLC facilitator. Contains the five required sections (Convergence, Divergence, Unique Content, Sequencing Differences, Questions for PLC) plus a short preamble identifying the frameworks compared and the scope of the comparison.
    - field: crosswalk_csv
      type: string
      description: Flat CSV with one row per LT × band × comparison framework pairing. Columns — lt_id, lt_name, band, reference_content, comparison_framework, comparison_content, comparison_source_label, confidence, issue_type, notes. Empty comparison_content means no equivalent found. issue_type is one of convergence, divergence, or unique. Suitable for Google Sheets filtering by band, LT, or issue type.
    - field: skill_flags
      type: array
      description: Skill-level warnings (insufficient overlap to produce meaningful convergence, framework with >50% ambiguity upstream, focus_bands exclude all content in one framework, etc.).
    - field: internal_trace
      type: object
      description: Non-prose metadata retained for debugging and for skill chaining — framework ids compared, item counts per section, band-coverage matrix. Not included in the crosswalk_document itself.
chains_well_with:
  - developmental-band-translator
  - learning-progression-builder
  - scope-and-sequence-designer
  - curriculum-knowledge-architecture-designer
  - gap-analysis-from-student-work
teacher_time: 30 minutes
tags:
  - curriculum-alignment
  - crosswalk
  - framework-comparison
  - Webb-alignment
  - Porter-content-analysis
  - PLC
  - source-voice-preservation
---

# What This Skill Does

This skill produces a readable crosswalk document comparing two or more band-tagged frameworks. Its input is the output of the Developmental Band Translator skill — one output per framework (a designated reference framework plus one or more comparison frameworks). Its output is a Markdown document that a teacher or PLC facilitator can open and use directly for a professional discussion — no JSON, no technical metadata, no field names — just prose and tables organised under five required sections: Convergence, Divergence, Unique Content, Sequencing Differences, and Questions for PLC. Alongside the Markdown document, the skill produces a flat CSV of the same comparison data for spreadsheet filtering and analysis.

The skill is deliberately additive, not reductive. It does not merge the frameworks into a single synthesised schema. It does not rewrite statements into a common voice. Each framework's content appears in the crosswalk in the original words the framework used, attributed by name. The crosswalk shows *relationships* — "the reference framework's Band D includes consent-law content; UK RSHE covers the same at End of Secondary; Welsh CfW covers it in PS4" — without collapsing distinct curricular traditions into one. This is a design decision grounded in Martone & Sireci (2009): alignment work that hides framework distinctiveness loses the very information a PLC needs to make a planning decision.

The skill is opinionated about the distinction between "cross-framework agreement" and "cross-framework coincidence". Two frameworks addressing the same topic at the same band is convergence only if they also treat the topic at comparable depth and intent. Where that is unclear — because the harness-produced items are at different grain sizes, or because one framework is propositional and the other dispositional — the skill flags the pairing as *apparent convergence, teacher confirmation needed* rather than silently counting it as agreement. This is the Webb-alignment categorical-concurrence distinction operationalised at the crosswalk level.

# Evidence Foundation

**Webb (1997)** — The four-dimension alignment framework (categorical concurrence, depth-of-knowledge consistency, range-of-knowledge correspondence, balance of representation) is the canonical reference point for alignment work in curriculum and assessment. This skill operationalises categorical concurrence (do the frameworks address the same topics?) and range (do the ages match?) at the school-band level. Depth-of-knowledge and balance are deliberately not assessed automatically; the Questions for PLC section surfaces them for human discussion.

**Porter (2002) and Porter et al. (2007)** — The Surveys of Enacted Curriculum methodology established that framework comparison requires a common content taxonomy. Here, the reference framework's band labels serve as the comparison axis, and other frameworks are cross-referenced against it. The skill inherits the Porter methodology's commitment to making the comparison visible and defensible — every cell in the convergence and divergence tables traces back to specific items in specific frameworks.

**Case, Jorgensen & Zucker (2004)** — Practical alignment procedures in assessment explicitly recommend that alignment studies preserve framework differences rather than suppress them. The unique-content table (Section 3) exists for exactly this reason: a framework's distinctive content is often its most pedagogically valuable feature, and a crosswalk that only showed overlap would erase it. What one framework covers that another does not — in either direction — is at least as informative as what they share.

**Martone & Sireci (2009)** — This review article establishes that alignment studies should preserve framework distinctiveness rather than collapse to a lowest-common-denominator schema. The skill's refusal to produce a merged mega-framework, and its commitment to showing each framework's content in its own voice, follow directly from this finding.

# Input Schema

**Required inputs.** The skill needs two inputs:

- **`reference_framework_band_tagged`** — The reference framework, already band-tagged by the Developmental Band Translator. Its band labels define the comparison axis. The skill does not assume the reference framework is any particular school's own curriculum; it can be any band-tagged framework the user designates as primary.
- **`comparison_frameworks_band_tagged`** — An array (one or more) of Developmental Band Translator outputs for comparison frameworks. Two is the minimum useful case (reference + 1 comparison); three or more produces a multi-framework crosswalk. Beyond four frameworks the Convergence table becomes unwieldy and the skill emits a `too_many_frameworks_for_readable_output` flag.

**Optional inputs.**

- **`reference_framework_name`** — A human-readable label for the reference framework used in output headings and table columns.
- **`focus_bands`** — A comma-separated list of school bands to restrict the crosswalk to (e.g. `"D,E"` for a secondary PLC). Content outside these bands is excluded from the tables but acknowledged in the preamble.
- **`focus_themes`** — Free-text theme restriction (e.g. `"consent, relationships"`). The skill filters items using keyword and semantic-similarity matching against content statements; a match log is retained in `internal_trace`.
- **`plc_context`** — One or two sentences describing the PLC audience and purpose. Used to tune the Questions for PLC section.

**Worked example of required inputs.** A REAL School Budapest Band D/E wellbeing PLC preparing for September 2026 planning might pass: `reference_framework_band_tagged` = the REAL School Wellbeing Framework band-tagged output; `comparison_frameworks_band_tagged` = [band-tagged UK DfE Statutory RSHE, band-tagged Welsh CfW Health & Wellbeing]; `reference_framework_name = "REAL School Budapest Wellbeing Framework"`; `focus_bands = "D,E"`; `plc_context = "Band D/E wellbeing team reviewing coverage gaps for 2026-27 planning"`.

# Prompt

You are a curriculum crosswalk assistant. You produce a PLC-ready Markdown document that compares multiple band-tagged frameworks, using the reference framework's school band labels as the comparison axis.

## Six required outputs — in this order

First, produce the `crosswalk_document` containing these five sections:

1. **Convergence table** — content that the reference framework and at least one comparison framework address at the same school band. Columns: Band; Reference content (verbatim); Comparison framework; Comparison content (verbatim); Confidence (high / medium / apparent-only).
2. **Divergence table** — content that the reference framework and at least one comparison framework *both* address but at *different* school bands. Columns: Topic; Reference band; Reference content (verbatim); Comparison framework; Comparison band; Comparison content (verbatim); Source label; Band-gap (in band units).
3. **Unique-content table** — content present in only one framework. One subsection per framework. Columns: Band(s); Content (verbatim); Knowledge type if known.
4. **Sequencing-difference notes** — narrative description (prose, not tables) of meaningful differences in how the frameworks sequence related content. Where the reference framework introduces X before Y but a comparison framework does the reverse, surface that with the relevant band labels and a one-sentence interpretation. Focus on differences that have planning implications.
5. **Questions for PLC** — a numbered list of questions the crosswalk surfaces for professional discussion. Do NOT answer these questions. Good PLC questions are: (a) concrete, (b) grounded in specific cells from the tables above, (c) open (no obviously right answer), (d) relevant to planning decisions the PLC will actually make. Target 6–10 questions.

Second, produce the `crosswalk_csv`: a flat CSV from the same comparison data. One row per LT × band × comparison framework pairing. Columns: lt_id, lt_name, band, reference_content, comparison_framework, comparison_content, comparison_source_label, confidence, issue_type, notes. Every convergence and divergence row appears in the CSV. Unique-content items appear with empty comparison_content. Do not omit rows where no match was found — an empty comparison_content cell is data.

## Output format (hard constraints)

- `crosswalk_document`: Markdown only. No JSON, no YAML, no field names, no `{variable}` placeholders.
- All framework content quoted verbatim in the document. Do not paraphrase, shorten, or translate content statements, even when they are awkward. Quote marks around exact source text.
- Attribute every content statement to its source framework by name.
- Preserve source-band labels alongside school bands in every table row. A reader should see both the school band and the framework's own label (e.g. "End of Secondary", "Progression Step 3") at every cell.
- If an item's band assignment was ambiguous upstream (multi-band), reflect that by listing every relevant band, not by picking one.

## Matching procedure

1. **Build a content index.** For each framework (reference + comparisons), list all band-tagged items with their school band(s), content statement, and source-band label.
2. **Pair by school band.** For each school band in `focus_bands` (or all bands if omitted):
   - For each reference-framework item in that band, search comparison frameworks for items tagged to the same band with overlapping thematic content.
   - Matching is semantic, not lexical.
3. **Classify each pair**:
   - **Convergent** — same school band, same topic, comparable grain size and intent → Convergence table.
   - **Apparent-only convergent** — same school band, same topic, but one is propositional and one dispositional, or grain sizes differ by >2× → Convergence table with confidence=apparent-only, AND a Question for PLC.
   - **Divergent** — same topic but different school bands → Divergence table. Record the band-gap in band units.
4. **Identify unique content.** For each framework, list items with no match in any other framework within the focus scope. These populate Section 3, one subsection per framework.
5. **Surface sequencing differences.** Look for cases where related-content chains run in different orders across frameworks. If the reference framework introduces X before Y but a comparison framework does the reverse, write one prose paragraph describing the difference and its likely planning implication.
6. **Compose questions for PLC.** Draw them from the tables. Anchor each question to at least one specific row.

## Scope rules

- Exclude any item outside `focus_bands` (if supplied) from all tables. Note the exclusion in the preamble.
- Filter by `focus_themes` (if supplied) using keyword + semantic matching. Retain the filter log in `internal_trace`.
- If any framework has <3 items remaining after filtering, emit `insufficient_items_after_filter` in `skill_flags` and do not produce a crosswalk for that framework.

## Source-voice preservation (hard constraint)

Every content statement you reproduce must appear exactly as it did in the band-tagged input. Quote it. Attribute it. Do not rewrite it to match another framework's style. This is not stylistic — it is the crosswalk's core integrity property.

## Inputs

- `reference_framework_band_tagged`: {{reference_framework_band_tagged}}
- `reference_framework_name`: {{reference_framework_name}}
- `comparison_frameworks_band_tagged`: {{comparison_frameworks_band_tagged}}
- `focus_bands`: {{focus_bands}}
- `focus_themes`: {{focus_themes}}
- `plc_context`: {{plc_context}}

Produce a `crosswalk_document` (Markdown string), a `crosswalk_csv` (CSV string), a `skill_flags` list, and an `internal_trace` object. The crosswalk_document is the primary output and must be directly usable by a PLC facilitator.

# Example Output

**Context**: Band D/E wellbeing PLC, comparing REAL School Budapest Wellbeing Framework (reference) against UK DfE Statutory RSHE (July 2025) and Welsh CfW Health & Wellbeing. `focus_bands = "D,E"`. The `crosswalk_document` field would contain:

---

## Crosswalk — REAL Wellbeing × UK RSHE × Welsh CfW H&W

**Scope**: School Bands D and E. **Reference framework**: REAL School Budapest Wellbeing Framework (2026-04). **Comparison frameworks**: UK DfE Statutory RSHE (July 2025); Welsh Curriculum for Wales Health & Wellbeing AoLE. **PLC context**: Band D/E wellbeing team reviewing coverage gaps for 2026-27 planning.

Note on ambiguity: RSHE content appears under the source label "End of Secondary" which spans school Bands C–E. Welsh CfW PS3 spans Bands C–D; PS4 spans Bands D–E. All rows carrying these source labels reflect that ambiguity.

### 1. Convergence

| Band | Reference content | Comparison framework | Comparison content | Source label | Confidence |
|---|---|---|---|---|---|
| D | "Students can identify healthy and unhealthy relationship patterns and articulate why each is so." | UK DfE Statutory RSHE | "the characteristics of positive and healthy friendships… respect, honesty, trust, loyalty, kindness, generosity, boundaries, privacy, consent and the management of conflict" | End of Secondary | high |
| D | "Students understand consent as an ongoing, reversible, affirmative process." | UK DfE Statutory RSHE | "the concepts of, and laws relating to, sexual consent, sexual exploitation, abuse, grooming, coercion, harassment, rape, domestic abuse, forced marriage, honour-based violence and FGM" | End of Secondary | apparent-only (reference frames consent developmentally; RSHE frames it propositionally and in law. Same topic, different epistemic stance.) |
| E | "Students can analyse how identity, values, and context shape their decisions about relationships." | Welsh CfW H&W | "I can analyse and evaluate how my identity, values and sense of self-worth affect the way I interact with others" | Progression Step 4 | high |

### 2. Divergence

| Topic | Reference band | Reference content | Comparison framework | Comparison band | Comparison content | Source label | Band-gap |
|---|---|---|---|---|---|---|---|
| Financial wellbeing | E | "Students can assess personal financial decisions in terms of their wellbeing impact." | UK DfE Statutory RSHE | — | not covered at D/E | — | n/a — framework gap |
| Mental-health help-seeking | D | "Students can identify when to seek help for themselves or a peer and know at least two trusted routes." | UK DfE Statutory RSHE | A–C | "where to get advice e.g. family, school and/or other sources" | End of Primary | 2 bands |
| Digital wellbeing | E | "Students can evaluate the wellbeing effects of their own technology use and adjust it." | Welsh CfW H&W | C–D | "I can make informed decisions about how to use digital technologies… to enhance my physical health and well-being" | Progression Step 3 | 1–2 bands |

### 3. Unique content

**Reference framework only (at Bands D/E, not matched in RSHE or Welsh CfW)**:
- "Students can use a restorative-practice protocol to address conflict with a peer" (Band D).
- "Students can identify their own regulation patterns across at least three settings" (Band E).

**UK DfE Statutory RSHE only (at End of Secondary)**:
- "the facts about the full range of contraceptive choices, efficacy and options available".
- "the impact of viewing harmful content" (specific to pornography).
- "how the different sexually transmitted infections (STIs), including HIV/AIDs, are transmitted".

**Welsh CfW H&W only (at PS3/PS4)**:
- "I can explain the benefits of spending time in the natural environment for my health and well-being" (PS3).
- "I understand the social, cultural, ethical and legal factors that influence my health and well-being decisions" (PS4).

### 4. Sequencing differences

The reference framework introduces mental-health help-seeking at Band D (ages 12–14); UK RSHE introduces the same content at End of Primary (ages 5–11). The 2-band gap reflects a substantive sequencing choice: the reference framework positions help-seeking as a secondary-aged regulatory competency, while RSHE treats it as a primary-aged safeguarding topic.

Digital-wellbeing content runs 1–2 bands earlier in Welsh CfW than in the reference framework. Welsh policy emphasises digital competency as foundational; the reference framework treats it as an applied topic built on regulatory foundations. Neither ordering is obviously wrong.

### 5. Questions for PLC

1. Should the reference framework introduce mental-health help-seeking earlier than Band D, given that UK RSHE treats it as an End-of-Primary competency?
2. The consent-content match is "apparent-only" because frameworks differ in epistemic stance. Does the Band D learner need both framings, and if so, which comes first?
3. The restorative-practice content at Band D has no counterpart in either comparison framework. Is this a distinctive strength worth highlighting, or does it reveal a gap?
4. UK RSHE's End-of-Secondary STI and contraception content does not appear in the reference framework at Band D or E. Is that absence intentional?
5. Welsh CfW's PS3 "natural environment" wellbeing content is absent from the reference framework. Is it covered implicitly elsewhere?
6. The digital-wellbeing band placement differs by 1–2 bands from Welsh CfW. Is the Band E placement a deliberate pedagogical choice or a legacy?
7. Where the crosswalk shows convergence, does the convergence extend to assessment intent, or only to topic coverage?

---

The `crosswalk_csv` field would contain:

```csv
lt_id,lt_name,band,reference_content,comparison_framework,comparison_content,comparison_source_label,confidence,issue_type,notes
cluster_01_lt_01,Healthy Relationship Patterns,D,"Students can identify healthy and unhealthy relationship patterns and articulate why each is so.",UK DfE Statutory RSHE,"the characteristics of positive and healthy friendships… respect, honesty, trust, loyalty",End of Secondary,high,convergence,
cluster_02_lt_01,Consent Understanding,D,"Students understand consent as an ongoing, reversible, affirmative process.",UK DfE Statutory RSHE,"the concepts of, and laws relating to, sexual consent, sexual exploitation, abuse",End of Secondary,apparent-only,convergence,Reference frames consent developmentally; RSHE propositionally
cluster_03_lt_01,Identity and Values in Relationships,E,"Students can analyse how identity, values, and context shape their decisions about relationships.",Welsh CfW H&W,"I can analyse and evaluate how my identity, values and sense of self-worth affect the way I interact with others",Progression Step 4,high,convergence,
cluster_04_lt_01,Financial Wellbeing,E,"Students can assess personal financial decisions in terms of their wellbeing impact.",UK DfE Statutory RSHE,,,high,divergence,No RSHE coverage at D/E
cluster_05_lt_01,Mental-health Help-seeking,D,"Students can identify when to seek help for themselves or a peer and know at least two trusted routes.",UK DfE Statutory RSHE,"where to get advice e.g. family, school and/or other sources",End of Primary,medium,divergence,RSHE places this 2 bands earlier
cluster_06_lt_01,Restorative Practice,D,"Students can use a restorative-practice protocol to address conflict with a peer.",UK DfE Statutory RSHE,,,high,unique,No counterpart in RSHE or Welsh CfW
cluster_07_lt_01,Digital Wellbeing,E,"Students can evaluate the wellbeing effects of their own technology use and adjust it.",Welsh CfW H&W,"I can make informed decisions about how to use digital technologies… to enhance my physical health and well-being",Progression Step 3,medium,divergence,Welsh CfW places this 1-2 bands earlier
```

# Known Limitations

**The skill does not assess depth-of-knowledge alignment.** Webb's depth-of-knowledge dimension is out of scope for automated comparison. The skill can see that two frameworks both address "consent" at the same band, but it cannot reliably judge whether they do so at the same cognitive depth. The Questions for PLC section is where depth-of-knowledge discussions belong. Convergence at apparent-only confidence is explicitly flagged for this reason.

**The skill inherits upstream ambiguity.** Where the Developmental Band Translator tagged items with multiple candidate school bands (common for UK RSHE's 2-band structure), the crosswalk carries that ambiguity into every table. A framework with high upstream ambiguity produces a crosswalk with many multi-band rows, which is honest but can be harder to read. The skill emits a skill flag when >50% of upstream items are multi-band and includes a preamble note explaining the effect.

**The skill does not merge frameworks.** This is intentional (Martone & Sireci, 2009). The crosswalk will not produce a synthesised unified framework, nor a single recommended topic order. Those are planning decisions for the PLC, informed by this document but made by humans.

**Thematic matching is not perfect.** The skill pairs items by semantic similarity in content statements. False negatives (genuine matches missed because the language is very different) and false positives (superficial lexical overlap with different pedagogical intent) are both possible. The `apparent-only` confidence tier surfaces false-positive risk; the Questions for PLC section backstops false-negative risk. The skill is a scaffold for the teacher's reading of the source documents, not a substitute for it.
