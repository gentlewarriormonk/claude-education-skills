---
name: REAL Crosswalk
description: Compare two or more band-tagged frameworks (produced by REAL Band Translation) against REAL's own band-tagged framework to produce a PLC-ready document showing convergence, divergence, unique content, sequencing differences, and open questions. Use when preparing a cross-framework review for a PLC or when integrating an external framework into REAL planning.
disable-model-invocation: false
user-invocable: true
effort: high
skill_id: original-frameworks/real-crosswalk
skill_name: REAL Crosswalk
domain: original-frameworks
version: "1.0"
evidence_strength: moderate
evidence_sources:
  - "Webb, N. L. (1997) — Criteria for Alignment of Expectations and Assessments in Mathematics and Science Education, CCSSO Research Monograph No. 6: the canonical four-dimension alignment framework (categorical concurrence, depth-of-knowledge consistency, range-of-knowledge correspondence, balance of representation); this skill operationalises categorical concurrence and range at the REAL-band level."
  - "Porter, A. C. (2002) — Measuring the content of instruction: Uses in research and practice, Educational Researcher 31(7), 3–14: the Surveys of Enacted Curriculum methodology for comparing intended vs enacted curricula across frameworks via common content taxonomies."
  - "Porter, A. C., Smithson, J., Blank, R. & Zeidner, T. (2007) — Alignment as a teacher variable, Applied Measurement in Education 20(1), 27–51: alignment indices and content-matrix methodology applied across standards documents."
  - "Case, B. J., Jorgensen, M. A. & Zucker, S. (2004) — Alignment in Educational Assessment, Pearson Assessment Report: practical alignment procedures that surface rather than hide framework differences — the rationale for the divergence and unique-content tables in this skill's output."
  - "Martone, A. & Sireci, S. G. (2009) — Evaluating alignment between curriculum, assessment, and instruction, Review of Educational Research 79(4), 1332–1361: literature review establishing that alignment studies should preserve framework distinctiveness rather than collapse to a lowest-common-denominator schema — the design principle behind this skill's refusal to produce a merged mega-framework."
input_schema:
  required:
    - field: real_framework_band_tagged
      type: string
      description: REAL School Budapest's own framework, already band-tagged. Must have the same structure as a Band Translation skill output — per-item real_band, source_band_preserved, content statements, etc.
    - field: external_frameworks_band_tagged
      type: string
      description: Array of one or more external frameworks, each produced by the REAL Band Translation skill. Each entry must include source_metadata, band_tagged_kud (or equivalent content-bearing items), and band_tagged_lts.
  optional:
    - field: focus_bands
      type: string
      description: Restrict the crosswalk to a subset of REAL bands (e.g. "D,E" for secondary-focused PLC). If omitted, all six bands are covered.
    - field: focus_themes
      type: string
      description: Restrict to specific thematic areas (e.g. "consent, relationships" for an RSHE-focused PLC). If omitted, all content is compared.
    - field: plc_context
      type: string
      description: A short description of the PLC context (e.g. "Band D/E wellbeing team preparing for September 2026 planning"). The skill uses this to tune the Questions for PLC section.
output_schema:
  type: object
  fields:
    - field: crosswalk_document
      type: string
      description: A Markdown document intended for direct use by a teacher or PLC facilitator. Contains the five required sections (Convergence, Divergence, Unique Content, Sequencing Differences, Questions for PLC) plus a short preamble identifying the frameworks compared and the scope of the comparison.
    - field: skill_flags
      type: array
      description: Skill-level warnings (insufficient overlap to produce meaningful convergence, framework with >50% ambiguity upstream, focus_bands exclude all content in one framework, etc.).
    - field: internal_trace
      type: object
      description: Non-prose metadata retained for debugging and for skill chaining — framework ids compared, item counts per section, band-coverage matrix. Not included in the crosswalk_document itself.
chains_well_with:
  - real-band-translation
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
  - REAL-bands
  - source-voice-preservation
---

# What This Skill Does

This skill produces a readable crosswalk document comparing two or more band-tagged frameworks against REAL School Budapest's own framework. Its input is the output of the REAL Band Translation skill (one output per external framework, plus REAL's own pre-tagged framework). Its output is a Markdown document that a teacher or PLC facilitator can open and use directly for a professional discussion — no JSON, no technical metadata, no field names — just prose and tables organised under the five required sections: Convergence, Divergence, Unique Content, Sequencing Differences, and Questions for PLC.

The skill is deliberately additive, not reductive. It does not merge the frameworks into a single synthesised schema. It does not rewrite statements into a common voice. Each framework's content appears in the crosswalk in the original words the framework used, attributed by name. The crosswalk shows *relationships* — "REAL Band D includes consent-law content; UK RSHE covers the same at End of Secondary; Welsh CfW covers it in PS4" — without collapsing three distinct curricular traditions into one. This is a design decision grounded in Martone & Sireci (2009): alignment work that hides framework distinctiveness loses the very information a PLC needs to make a planning decision.

The skill is opinionated about the distinction between "cross-framework agreement" and "cross-framework coincidence". Two frameworks addressing the same topic at the same band is convergence only if they also treat the topic at comparable depth and intent. Where that is unclear — because the harness-produced items are at different grain sizes, or because one framework is propositional and the other dispositional — the skill flags the pairing as *apparent convergence, teacher confirmation needed* rather than silently counting it as agreement. This is the Webb-alignment categorical-concurrence distinction operationalised at the crosswalk level.

# Evidence Foundation

**Webb (1997)** — The four-dimension alignment framework (categorical concurrence, depth-of-knowledge consistency, range-of-knowledge correspondence, balance of representation) is the canonical reference point for alignment work in curriculum and assessment. This skill operationalises categorical concurrence (do the frameworks address the same topics?) and range (do the ages match?) at the REAL-band level. Depth-of-knowledge and balance are deliberately not assessed automatically; the Questions for PLC section surfaces them for human discussion.

**Porter (2002) and Porter et al. (2007)** — The Surveys of Enacted Curriculum methodology established that framework comparison requires a common content taxonomy. Here, REAL's own framework serves as the taxonomy, and external frameworks are cross-referenced against it. The skill inherits the Porter methodology's commitment to making the comparison visible and defensible — every cell in the convergence and divergence tables traces back to specific items in specific frameworks.

**Case, Jorgensen & Zucker (2004)** — Practical alignment procedures in assessment explicitly recommend that alignment studies preserve framework differences rather than suppress them. The unique-content table (Section 3) exists for exactly this reason: a framework's distinctive content is often its most pedagogically valuable feature, and a crosswalk that only showed overlap would erase it. For REAL, what UK RSHE covers that REAL does not — and vice versa — is at least as informative as what they share.

**Martone & Sireci (2009)** — This review article establishes that alignment studies should preserve framework distinctiveness rather than collapse to a lowest-common-denominator schema. The skill's refusal to produce a merged mega-framework, and its commitment to showing each framework's content in its own voice, follow directly from this finding.

# Input Schema

**Required inputs.** The skill needs two inputs:

- **`real_framework_band_tagged`** — REAL School Budapest's own framework, already band-tagged in the same structure as Band Translation output. The skill assumes this is the authoritative comparison axis.
- **`external_frameworks_band_tagged`** — An array (one or more) of Band Translation outputs for external frameworks. Two is the minimum useful case (REAL + 1 external); three or more produces a multi-framework crosswalk. Beyond four frameworks the Convergence table becomes unwieldy and the skill emits a `too_many_frameworks_for_readable_output` flag.

**Optional inputs.**

- **`focus_bands`** — A comma-separated list of REAL bands to restrict the crosswalk to (e.g. `"D,E"` for a secondary PLC). Content outside these bands is excluded from the tables but acknowledged in the preamble.
- **`focus_themes`** — Free-text theme restriction (e.g. `"consent, relationships"`). The skill filters items using keyword and semantic-similarity matching against content statements; a match log is retained in `internal_trace`.
- **`plc_context`** — One or two sentences describing the PLC audience and purpose. Used to tune the Questions for PLC section (e.g. a merger-planning PLC gets different questions from a curriculum-renewal PLC).

**Worked example of required inputs.** A Band D/E wellbeing PLC preparing for September 2026 planning might pass: `real_framework_band_tagged` = the REAL School Wellbeing Framework from `docs/reference-corpus/real-wellbeing-2026-04/`, band-tagged; `external_frameworks_band_tagged` = [band-tagged UK DfE Statutory RSHE, band-tagged Welsh CfW Health & Wellbeing]; `focus_bands = "D,E"`; `plc_context = "Band D/E wellbeing team reviewing coverage gaps for 2026-27 planning"`.

# Prompt

You are a curriculum crosswalk assistant for REAL School Budapest. You produce a PLC-ready Markdown document that compares external frameworks against REAL School's own framework, using the REAL developmental bands (A–F) as the comparison axis.

## Five required sections — in this order

1. **Convergence table** — content that REAL and at least one external framework address at the same REAL band. Columns: REAL band; REAL content (verbatim); external framework; external content (verbatim); confidence (high / medium / apparent-only).
2. **Divergence table** — content that REAL and at least one external framework *both* address but at *different* REAL bands. Columns: Topic; REAL band; REAL content (verbatim); external framework; external band; external content (verbatim); band-gap (in REAL-band units).
3. **Unique-content table** — content present in only one framework. One subsection per framework. Columns: REAL band(s); content (verbatim); knowledge type if known.
4. **Sequencing-difference notes** — narrative description (prose, not tables) of meaningful differences in how the frameworks sequence related content. Where REAL introduces X before Y but an external framework does the reverse, surface that with the relevant band labels and a one-sentence interpretation. Focus on differences that have planning implications, not cosmetic re-orderings.
5. **Questions for PLC** — a numbered list of questions the crosswalk surfaces for professional discussion. Do NOT answer these questions. Good PLC questions are: (a) concrete, (b) grounded in specific cells from the tables above, (c) open (no obviously right answer), (d) relevant to planning decisions the PLC will actually make. Target 6–10 questions.

## Output format (hard constraints)

- Markdown only. No JSON, no YAML, no field names, no `{variable}` placeholders.
- All framework content quoted verbatim. Do not paraphrase, shorten, or "translate" content statements into REAL house style, even when they are awkward. Quote marks around exact source text.
- Attribute every content statement to its source framework by name. Use the `source_name` from Band Translation's `source_metadata`.
- Preserve source-band labels alongside REAL bands in every row. A reader should be able to see *both* "Band D" (REAL's band) and "End of Secondary" or "Progression Step 3" (the source's label) at every cell.
- If an item's band assignment was ambiguous upstream (multi-band), reflect that by listing every relevant REAL band, not by picking one.

## Matching procedure

1. **Build a content index.** For each framework (REAL + externals), list all band-tagged items with their REAL band(s), content statement, and source-band label.
2. **Pair by REAL band.** For each REAL band in `focus_bands` (or all six if omitted):
   - For each REAL item in that band, search external frameworks for items tagged to the same band with overlapping thematic content.
   - Matching is semantic, not lexical. "Understanding consent" in REAL Band D matches "the concepts of, and laws relating to, sexual consent" in RSHE End of Secondary → Band D/E.
3. **Classify each pair**:
   - **Convergent** — same REAL band, same topic, comparable grain size and intent → Convergence table.
   - **Apparent-only convergent** — same REAL band, same topic, but one is propositional and one is dispositional, or grain sizes differ by >2× → Convergence table with confidence=apparent-only, AND a Question for PLC.
   - **Divergent** — same topic but different REAL bands → Divergence table. Record the band-gap in REAL-band units (e.g. Band B vs Band D = 2 bands).
4. **Identify unique content.** For each framework, list items with no match in any other framework within the focus scope. These populate Section 3, one subsection per framework.
5. **Surface sequencing differences.** Look for cases where related-content chains run in different orders across frameworks. If REAL introduces X before Y but an external does Y before X, and both are in-scope, write one prose paragraph describing the difference and its likely planning implication.
6. **Compose questions for PLC.** Draw them from the tables. Anchor each question to at least one specific row ("Given that REAL places consent-law content in Band D but Welsh CfW places it at Progression Step 4 / Band D–E, should REAL consider a Band E revisit?").

## Scope rules

- Exclude any item outside `focus_bands` (if supplied) from all tables. Note the exclusion in the preamble.
- Filter by `focus_themes` (if supplied) using keyword + semantic matching. Retain the filter log in `internal_trace`.
- If any framework has <3 items remaining after filtering, emit `insufficient_items_after_filter` in `skill_flags` and do not produce a crosswalk for that framework.

## Source-voice preservation (hard constraint)

Every content statement you reproduce must appear exactly as it did in the band-tagged input. Quote it. Attribute it. Do not rewrite it to sound like REAL. Do not rewrite REAL's content to sound like the external framework either. This is not stylistic — it is the crosswalk's core integrity property. A facilitator must be able to see, side by side, what each framework actually says.

## Inputs

- `real_framework_band_tagged`: {{real_framework_band_tagged}}
- `external_frameworks_band_tagged`: {{external_frameworks_band_tagged}}
- `focus_bands`: {{focus_bands}}
- `focus_themes`: {{focus_themes}}
- `plc_context`: {{plc_context}}

Produce a `crosswalk_document` (Markdown string), a `skill_flags` list, and an `internal_trace` object. The crosswalk_document is the primary output and must be directly usable by a PLC facilitator.

# Example Output

**Context**: Band D/E wellbeing PLC, comparing REAL School Wellbeing Framework against UK DfE Statutory RSHE (July 2025) and Welsh CfW Health & Wellbeing. `focus_bands = "D,E"`. `focus_themes` omitted. The `crosswalk_document` field would contain:

---

## Crosswalk — REAL Wellbeing × UK RSHE × Welsh CfW H&W

**Scope**: REAL Bands D and E (ages 12–16). **Compared frameworks**: REAL School Budapest Wellbeing Framework (2026-04); UK DfE Statutory RSHE (July 2025); Welsh Curriculum for Wales Health & Wellbeing AoLE. **PLC context**: Band D/E wellbeing team reviewing coverage gaps for 2026-27 planning.

Note on ambiguity: RSHE content appears under the source label "End of Secondary" which spans REAL Bands C–E. Welsh CfW PS3 spans Bands C–D; PS4 spans Bands D–E. All RSHE "End of Secondary" and Welsh "PS3/PS4" rows in the tables below carry that ambiguity; band-gap calculations use the midpoint of each candidate range.

### 1. Convergence

| REAL band | REAL content | External framework | External content | Source label | Confidence |
|---|---|---|---|---|---|
| D | "Students can identify healthy and unhealthy relationship patterns and articulate why each is so." | UK DfE Statutory RSHE | "the characteristics of positive and healthy friendships… respect, honesty, trust, loyalty, kindness, generosity, boundaries, privacy, consent and the management of conflict" | End of Secondary | high |
| D | "Students understand consent as an ongoing, reversible, affirmative process." | UK DfE Statutory RSHE | "the concepts of, and laws relating to, sexual consent, sexual exploitation, abuse, grooming, coercion, harassment, rape, domestic abuse, forced marriage, honour-based violence and FGM" | End of Secondary | apparent-only (REAL frames consent developmentally; RSHE frames it propositionally and in law. Same topic, different epistemic stance.) |
| E | "Students can analyse how identity, values, and context shape their decisions about relationships." | Welsh CfW H&W | "I can analyse and evaluate how my identity, values and sense of self-worth affect the way I interact with others" | Progression Step 4 | high |

### 2. Divergence

| Topic | REAL band | REAL content | External framework | External band | External content | Source label | Band-gap |
|---|---|---|---|---|---|---|---|
| Financial wellbeing | E | "Students can assess personal financial decisions in terms of their wellbeing impact." | UK DfE Statutory RSHE | not covered at D/E (health-only framing in RSHE statutory) | — | — | n/a — framework gap |
| Mental-health help-seeking | D | "Students can identify when to seek help for themselves or a peer and know at least two trusted routes." | UK DfE Statutory RSHE | End of Primary covers "where to get advice e.g. family, school and/or other sources" | End of Primary | Content appears in RSHE's primary phase but REAL introduces it at Band D (secondary). | 2 bands |
| Digital wellbeing | E | "Students can evaluate the wellbeing effects of their own technology use and adjust it." | Welsh CfW H&W | "I can make informed decisions about how to use digital technologies… to enhance my physical health and well-being" | Progression Step 3 | PS3 maps to Bands C–D in REAL — earlier than REAL's own Band E placement. | 1–2 bands |

### 3. Unique content

**REAL only (at Bands D/E, not matched in RSHE or Welsh CfW)**:
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

REAL introduces mental-health help-seeking at Band D (ages 12–14); UK RSHE introduces the same content at End of Primary (ages 5–11). The 2-band gap is the largest in the crosswalk and reflects a substantive sequencing choice: REAL positions help-seeking as a secondary-aged regulatory competency, while RSHE treats it as a primary-aged safeguarding topic. A PLC will need to decide whether REAL's Band A–C should include an earlier version of this content.

REAL introduces identity-and-values analysis at Band E (ages 14–16); Welsh CfW introduces an equivalent at Progression Step 4 (ages 14–16). These sequence together. However, Welsh CfW also introduces a lighter-touch version at PS3 (ages 11–14 / Band C–D), which REAL does not. Whether to seed this earlier in REAL is an open question.

Digital-wellbeing content runs 1–2 bands earlier in Welsh CfW than in REAL. This is consistent with Welsh policy emphasising digital competency as foundational; REAL treats it as an applied topic on top of regulatory foundations. Neither ordering is obviously wrong; the PLC should decide whether REAL's placement is deliberate or legacy.

### 5. Questions for PLC

1. Should REAL introduce mental-health help-seeking earlier than Band D, given that UK RSHE treats it as an End-of-Primary competency? What would a Band A/B version look like in REAL voice?
2. The consent-content match between REAL and RSHE is "apparent-only" because REAL frames consent developmentally and RSHE propositionally/legally. Does the REAL Band D learner need both framings, and if so, which comes first?
3. REAL's restorative-practice content at Band D has no counterpart in either external framework. Is this a distinctive strength of REAL worth highlighting in the school story, or a gap that the external frameworks reveal in REAL (i.e. should we also teach the content RSHE and Welsh CfW place here)?
4. UK RSHE's End-of-Secondary STI and contraception content does not appear in REAL at Band D or E. Is that absence intentional, and if so, what is the REAL position on statutory-equivalent coverage?
5. Welsh CfW's PS3 "natural environment" wellbeing content is absent from REAL. Does REAL's biophilic-learning work cover this implicitly, and if so, is it worth making explicit?
6. The digital-wellbeing band placement differs by 1–2 bands from Welsh CfW. Is REAL's Band E placement a deliberate pedagogical choice or a legacy from when digital wellbeing was treated as elective content?
7. The UK RSHE "End of Secondary" label spans Bands C–E in REAL. Of the content ambiguous across these bands, which items does the Band D/E team own, and which should be referred to the Band C team for early-band sequencing?
8. Where the crosswalk shows convergence, does the convergence extend to assessment intent — or only to topic coverage? (Webb's depth-of-knowledge question, deliberately deferred from the skill to the PLC.)

---

# Known Limitations

**The skill does not assess depth-of-knowledge alignment.** Webb's depth-of-knowledge dimension is out of scope for automated comparison. The skill can see that two frameworks both address "consent" at Band D, but it cannot reliably judge whether they do so at the same cognitive depth. The Questions for PLC section is where depth-of-knowledge discussions belong, not the Convergence table. Convergence at apparent-only confidence is explicitly flagged for this reason.

**The skill inherits upstream ambiguity.** Where the Band Translation skill tagged items with multiple candidate REAL bands (common for UK RSHE's 2-band structure), the crosswalk carries that ambiguity into every table. A framework with high upstream ambiguity produces a crosswalk with many multi-band rows, which is honest but can be harder to read. The skill emits a skill flag when >50% of upstream items are multi-band and includes a preamble note explaining the effect.

**The skill does not merge frameworks.** This is intentional (Martone & Sireci, 2009) and some readers initially experience it as a limitation. The crosswalk will not produce a synthesised REAL-plus-RSHE-plus-Welsh framework, nor a single recommended order of topics for REAL to adopt. Those are planning decisions for the PLC, informed by this document but made by humans. A reader expecting a unified curriculum will find the crosswalk disappointingly plural; that is the design.

**Thematic matching is not perfect.** The skill pairs items by semantic similarity in content statements, anchored by REAL band. False negatives (genuine matches missed because the language is very different) and false positives (superficial lexical overlap with different pedagogical intent) are both possible. The `apparent-only` confidence tier exists to surface the false-positive risk; the `Questions for PLC` section is the backstop for the false-negative risk (a good PLC question asks "is anything missing from this crosswalk?"). The skill does not claim to replace the teacher's reading of the source documents; it is a scaffold for that reading.
