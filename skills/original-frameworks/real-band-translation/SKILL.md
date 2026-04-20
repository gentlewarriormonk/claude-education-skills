---
name: REAL Band Translation
description: Tag a harness-decomposed external curriculum (KUDs, LTs, progression structure) with REAL developmental-band metadata (A–F) while preserving source voice and source-band labels unchanged. Use when a framework produced by the curriculum harness needs to enter REAL School's internal planning system or be crosswalked against REAL's own framework.
disable-model-invocation: false
user-invocable: true
effort: medium
skill_id: original-frameworks/real-band-translation
skill_name: REAL Band Translation
domain: original-frameworks
version: "1.0"
evidence_strength: moderate
evidence_sources:
  - "Wiggins, G. & McTighe, J. (2005) — Understanding by Design (2nd ed.), ASCD: backward design establishes the principle that curriculum alignment begins from stated outcomes and works backward through learning targets; band-tagging is an alignment operation on that model."
  - "Wiggins, G. & McTighe, J. (2011) — The Understanding by Design Guide to Creating High-Quality Units, ASCD: KUD as the canonical unit of translation between frameworks."
  - "Vygotsky, L. S. (1978) — Mind in Society: The Development of Higher Psychological Processes, Harvard University Press: the Zone of Proximal Development provides the theoretical basis for developmental banding as an age-and-readiness construct rather than a pure age construct."
  - "Heritage, M. (2008) — Learning Progressions: Supporting Instruction and Formative Assessment, CCSSO: progressions are developmental rather than age-deterministic; band mappings must preserve this."
  - "Webb, N. L. (1997) — Criteria for Alignment of Expectations and Assessments in Mathematics and Science Education, CCSSO Research Monograph No. 6: alignment is multi-dimensional (categorical concurrence, depth-of-knowledge, range, balance) — band translation addresses only the age-range dimension and must not be mistaken for full alignment."
input_schema:
  required:
    - field: kud_json
      type: string
      description: The harness-produced KUD file (kud.json). Each item must include at minimum item_id, content_statement, knowledge_type, and source_block_id.
    - field: lts_json
      type: string
      description: The harness-produced LT file (lts.json). Each LT must include lt_id, lt_name, lt_definition, kud_item_ids, and knowledge_type.
    - field: progression_structure_json
      type: string
      description: The harness-produced progression_structure.json for the source. Must include band_labels, source_type, and age_range_hint (or per-band approximate_age_range).
  optional:
    - field: criterion_bank_json
      type: string
      description: The harness-produced criterion_bank.json if criterion-level band tagging is also required. Optional — if omitted the skill tags only KUD items and LTs.
    - field: source_name
      type: string
      description: Human-readable source name (e.g. "UK DfE Statutory RSHE, July 2025") for output provenance. Defaults to progression_structure.source_slug if omitted.
    - field: user_age_range_override
      type: string
      description: Explicit age-range mapping supplied by the user when a source has no native band structure (flat list). Required only when the skill emits a request_age_range_context error.
output_schema:
  type: object
  fields:
    - field: source_metadata
      type: object
      description: Source name, source_type, source_band_labels (unchanged), and skill run provenance (version, timestamp, invoker).
    - field: band_tagged_kud
      type: array
      description: Every KUD item with real_band (string or array), band_confidence, source_band_preserved, source_voice_preserved (always true), ambiguity_flag, teacher_review_flag, and band_rationale.
    - field: band_tagged_lts
      type: array
      description: Every LT with real_band (string or array), band_confidence, source_band_preserved, source_voice_preserved (always true), ambiguity_flag, teacher_review_flag, and band_rationale. Band is assigned from the LT's constituent KUD items using the aggregation rule described in the prompt.
    - field: band_tagged_criteria
      type: array
      description: Present only if criterion_bank_json was supplied. Same field set as LTs. Inherit band from parent LT unless a criterion explicitly narrows the age range.
    - field: summary_counts
      type: object
      description: Counts of items per REAL band, ambiguity flags, teacher review flags, and low-confidence tags. For rapid quality scanning.
    - field: skill_flags
      type: array
      description: Any skill-level warnings (missing age range, CASEL-style frameworks requiring full teacher review, source-voice preservation warnings if any rewriting was detected).
chains_well_with:
  - real-crosswalk
  - kud-knowledge-type-mapper
  - learning-progression-builder
  - competency-framework-translator
  - scope-and-sequence-designer
teacher_time: 10 minutes
tags:
  - REAL-bands
  - developmental-bands
  - curriculum-alignment
  - band-mapping
  - source-voice-preservation
  - Wiggins-McTighe
  - Vygotsky
  - ZPD
  - framework-translation
---

# What This Skill Does

This skill tags an external curriculum — already decomposed by the curriculum harness into KUD items, learning targets, and (optionally) criteria — with REAL School Budapest's six developmental bands: A (ages 5–8), B (8–10), C (10–12), D (12–14), E (14–16), F (16–18). Every item receives a `real_band` value, a confidence level, and diagnostic flags. The source's own band labels are preserved verbatim alongside the new REAL band tags, so the output can always be traced back to, and interpreted against, the original framework.

The skill is a metadata operation, not a content operation. It does not rewrite KUDs, LTs, or criteria into REAL prose, and it does not reinterpret the source's intent. Its only job is to answer the question: "If a REAL teacher planning for Band C opened this framework, which of its content is relevant to them?" The skill is deliberately conservative where a source band spans two REAL bands (common for UK Key Stages): it assigns both candidate bands, sets an ambiguity flag, and records a rationale. Downstream skills — especially the REAL Crosswalk skill and the human planning process — resolve these ambiguities with teacher judgement.

The skill handles three common source-structure scenarios. Most sources have an explicit band structure (Welsh CfW Progression Steps, NZ Curriculum Levels, IB PYP/MYP/DP phases) which maps cleanly with occasional boundary ambiguity. Some have a formal-but-compressed structure (UK RSHE has four Key Stage labels but only two actual age bands in the statutory document), where the skill applies the source's real 2-band structure first and then informs via `source_band_preserved` what the formal label was. A minority have no band structure at all (CASEL, some competency frameworks), where the skill maps by developmental descriptor rather than age and flags every item for teacher review.

# Evidence Foundation

**Wiggins & McTighe (2005, 2011)** — Understanding by Design establishes KUD (Know / Understand / Do) as the unit-level architecture through which framework content becomes teachable, and positions curriculum alignment as a backward-design operation from stated outcomes. The REAL Band Translation skill operates on exactly the KUD layer that UbD specifies, and treats REAL-band assignment as one step in a backward-design pipeline whose final consumer is the REAL School teacher.

**Vygotsky (1978)** — The Zone of Proximal Development grounds the concept that developmental banding is not a pure age-partition. A Band C learner is defined by what they can do with support, not only by their chronological age. This justifies the skill's use of both age-range and developmental-descriptor evidence when tagging, and its willingness to assign a REAL band from descriptor-based reasoning alone when age evidence is absent (the CASEL case).

**Heritage (2008)** — Learning progressions literature reinforces that progressions are developmental trajectories, not calendars. The skill treats REAL bands as trajectory-waypoints. Where a source's native progression is coarser than REAL's (RSHE's 2-band structure vs REAL's 6-band), the skill preserves the coarseness honestly via ambiguity flags rather than forcing false precision.

**Webb (1997)** — The canonical alignment framework defines four alignment dimensions: categorical concurrence, depth-of-knowledge consistency, range-of-knowledge correspondence, balance of representation. Band translation addresses primarily the *range* dimension (do the age spans match?) with partial touch on *categorical concurrence*. The skill does not claim to assess depth or balance alignment; this limit is reported in `skill_flags` and in Known Limitations.

# Input Schema

**Required inputs.** The skill needs three harness artefacts:

- **`kud_json`** — The KUD file. Required fields per item: `item_id`, `content_statement`, `knowledge_type`, `source_block_id`. The skill uses `source_block_id` to look up the block's native band label in the progression structure.
- **`lts_json`** — The LT file. Required fields per LT: `lt_id`, `lt_name`, `lt_definition`, `kud_item_ids`, `knowledge_type`. LTs inherit their band from their constituent KUD items using a max-span rule (see Prompt).
- **`progression_structure_json`** — The progression structure. Required: `band_labels`, `source_type`, and either a top-level `age_range_hint` or per-band `approximate_age_range`. If both age-range fields are absent, the skill returns `request_age_range_context` in `skill_flags` and halts.

**Optional inputs.**

- **`criterion_bank_json`** — If supplied, criteria are also tagged. Criteria inherit their parent LT's band unless their content narrows to a more specific age-range signal.
- **`source_name`** — A friendly name for output metadata.
- **`user_age_range_override`** — A user-supplied age-range mapping, used when the source has no native band structure and the first invocation halted with `request_age_range_context`.

**Worked example of required inputs.** For `uk-statutory-rshe`: `kud_json` = the 279-item KUD file from `docs/reference-corpus/uk-statutory-rshe/kud.json`; `lts_json` = the 44-LT file from the same folder; `progression_structure_json` = a structure declaring `band_labels: ["End of Primary (Year 6)", "End of Secondary (Year 11)"]`, `source_type: "national_statutory_curriculum"`, and age ranges 5–11 and 11–16 respectively. The skill would then produce band tags using the 2-band reality (primary → Band A/B/C ambiguous for early-primary items, Band C for late-primary items; secondary → Band D/E).

# Prompt

You are a curriculum band-translation assistant for REAL School Budapest. Your task is to tag an external framework — already decomposed by the curriculum harness — with REAL's six developmental bands, while preserving the source's own voice and labels completely unchanged.

## REAL bands

- Band A: ages 5–8
- Band B: ages 8–10
- Band C: ages 10–12
- Band D: ages 12–14
- Band E: ages 14–16
- Band F: ages 16–18

## Canonical band-mapping rules

Apply these first before any content inspection:

| Source band | REAL band(s) | Ambiguity? |
|---|---|---|
| UK KS1 (ages 5–7) | Band A | Low — if the source's own age lower bound is ≥5, tag Band A; if content clearly targets 5-year-olds only, note narrow-fit. |
| UK KS2 (ages 7–11) | Band A or B or C | High — KS2 spans three REAL bands; always set ambiguity_flag, tag all three, and explain. |
| UK KS3 (ages 11–14) | Band C and D | Medium — tag both, ambiguity_flag true. |
| UK KS4 (ages 14–16) | Band D and E | Medium — tag both, ambiguity_flag true. |
| UK RSHE "End of Primary" (ages 5–11) | Band A, B, C | High — 2-band source, 3 REAL bands; tag all three, set teacher_review_flag true for any item that plausibly narrows to one sub-band. |
| UK RSHE "End of Secondary" (ages 11–16) | Band C, D, E | High — same pattern; tag all three; teacher_review_flag true. |
| Welsh CfW PS1 (up to age 5, extends to 8) | Band A | Low — though PS1's lower bound predates REAL's lowest band (5), the overlap is Band A. |
| Welsh CfW PS2 (ages 8–11 approx) | Band B and C | Medium. |
| Welsh CfW PS3 (ages 11–14 approx) | Band C and D | Medium. |
| Welsh CfW PS4 (ages 14–16 approx) | Band D and E | Medium. |
| Welsh CfW PS5 (ages 16+) | Band E and F | Medium. |

## Procedure

1. **Read the progression structure.** Note `source_type`, `band_labels`, and age ranges. If both `age_range_hint` and per-band `approximate_age_range` are absent, emit `request_age_range_context` in `skill_flags`, do not tag anything, and stop.
2. **Build a band-mapping table** for *this* source. Start from the canonical table above. If the source's native bands match (RSHE, Welsh CfW), use the canonical row directly. If they don't match (e.g. NZ Levels), derive the mapping from the per-band age ranges.
3. **Tag every KUD item.**
   - Look up its `source_block_id` to find the source band.
   - Apply the band-mapping table to get candidate REAL bands.
   - `real_band`: single band as a string if unambiguous; array of bands if ambiguous.
   - `band_confidence`: `high` if single REAL band and source age range ≤2 years; `medium` if two REAL bands; `low` if three or more, or if derived by developmental-descriptor inference only.
   - `source_band_preserved`: the exact native label from the source (e.g. "Key Stage 2", "End of Primary", "Progression Step 3").
   - `source_voice_preserved`: always `true`. If you would need to rewrite the content to make it fit a REAL band, do NOT rewrite — instead set this to `false` and add a skill flag. This field exists to prove no rewriting occurred.
   - `ambiguity_flag`: `true` if `real_band` is an array.
   - `teacher_review_flag`: `true` when (a) `real_band` spans three or more bands, (b) confidence is `low`, (c) `source_type` is a dispositional/competency framework with no age-banding (e.g. CASEL), or (d) the content statement contains developmental language that would narrow the band beyond what the source label allows.
   - `band_rationale`: one sentence explaining the assignment.
4. **Tag every LT.** An LT's REAL band is the union of its constituent KUD items' bands (max-span rule). If any constituent is ambiguous, the LT is ambiguous. `teacher_review_flag` fires if any constituent has it or if the LT aggregates across three or more REAL bands.
5. **Tag criteria** (if `criterion_bank_json` supplied). Each criterion inherits its parent LT's band unless its content narrows it. Same field set as LTs.
6. **Emit summary counts and skill flags.** Count items per band, ambiguity flags, teacher-review flags, and low-confidence tags. Emit a skill flag for any source where >50% of items are ambiguous (signals a structural mismatch worth reviewing).

## Source-voice preservation rule (hard constraint)

You are **tagging** content, not rewriting it. Do not paraphrase, shorten, or "translate" content statements, LT definitions, or criterion descriptions into REAL's preferred prose style. If a content statement uses the source's idiom (e.g. "learners" vs "students", British vs American spelling, Welsh-curriculum phrasing), keep it exactly. The only new text you generate is `band_rationale`.

## CASEL / flat-framework handling

If `source_type` indicates a competency or dispositional framework with no age structure (e.g. CASEL), and no `user_age_range_override` was supplied:
- Set `teacher_review_flag: true` on every item.
- Set `band_confidence: low` on every item.
- Base `real_band` on the developmental sophistication of the descriptor: emotion-labeling → Band A/B; perspective-taking → Band C/D; systems-level social awareness → Band E/F.
- Emit `skill_flag: casel_style_framework_full_teacher_review_required`.

## Inputs

- `source_name`: {{source_name}}
- `progression_structure_json`: {{progression_structure_json}}
- `kud_json`: {{kud_json}}
- `lts_json`: {{lts_json}}
- `criterion_bank_json`: {{criterion_bank_json}}
- `user_age_range_override`: {{user_age_range_override}}

Produce the band-tagged output as a single JSON object conforming to the output schema. Do not rewrite source content. Do not invent bands the source cannot support.

# Example Output

**Source**: UK DfE Statutory RSHE (July 2025), `progression_structure.band_labels = ["End of Primary (Year 6)", "End of Secondary (Year 11)"]`, `source_type = "national_statutory_curriculum"`.

```json
{
  "source_metadata": {
    "source_name": "UK DfE Statutory RSHE, July 2025",
    "source_type": "national_statutory_curriculum",
    "source_band_labels": ["End of Primary (Year 6)", "End of Secondary (Year 11)"],
    "skill_version": "1.0",
    "run_timestamp": "2026-04-20T14:05:00Z"
  },
  "band_tagged_kud": [
    {
      "item_id": "blk_0002_item_01",
      "content_statement": "Young people understand the correct terms for different parts of the body",
      "knowledge_type": "Type 1",
      "real_band": ["A", "B", "C"],
      "band_confidence": "medium",
      "source_band_preserved": "End of Primary (Year 6)",
      "source_voice_preserved": true,
      "ambiguity_flag": true,
      "teacher_review_flag": true,
      "band_rationale": "Source groups all primary-age content into one band; anatomical terminology is taught across Bands A–C in REAL practice."
    },
    {
      "item_id": "blk_0346_item_03",
      "content_statement": "Pupils can communicate their boundaries about physical contact and privacy needs",
      "knowledge_type": "Type 2",
      "real_band": ["A", "B", "C"],
      "band_confidence": "medium",
      "source_band_preserved": "End of Primary (Year 6)",
      "source_voice_preserved": true,
      "ambiguity_flag": true,
      "teacher_review_flag": true,
      "band_rationale": "Statutory End-of-Primary expectation; boundary-communication progresses across all three primary-overlapping REAL bands."
    },
    {
      "item_id": "blk_0210_item_02",
      "content_statement": "Students understand the concepts of, and laws relating to, sexual consent",
      "knowledge_type": "Type 1",
      "real_band": ["D", "E"],
      "band_confidence": "medium",
      "source_band_preserved": "End of Secondary (Year 11)",
      "source_voice_preserved": true,
      "ambiguity_flag": true,
      "teacher_review_flag": false,
      "band_rationale": "Secondary-only content; REAL typically introduces consent law in Band D with deepening in Band E."
    }
  ],
  "band_tagged_lts": [
    {
      "lt_id": "cluster_01_lt_01",
      "lt_name": "Identifying Body Parts and Privacy",
      "real_band": ["A", "B", "C"],
      "band_confidence": "medium",
      "source_band_preserved": "End of Primary (Year 6)",
      "source_voice_preserved": true,
      "ambiguity_flag": true,
      "teacher_review_flag": true,
      "band_rationale": "Aggregated from 4 KUD items all tagged End of Primary; max-span = Bands A–C."
    }
  ],
  "summary_counts": {
    "total_kud_items": 279,
    "total_lts": 44,
    "kud_by_band": {"A_only": 0, "B_only": 0, "C_only": 0, "D_only": 0, "E_only": 0, "F_only": 0, "A-B-C_ambiguous": 176, "C-D-E_ambiguous": 103},
    "lts_by_band": {"A-B-C_ambiguous": 28, "C-D-E_ambiguous": 16},
    "teacher_review_flagged": 279,
    "low_confidence": 0
  },
  "skill_flags": [
    "high_ambiguity_rate_structural: 100% of items are ambiguous because source has 2 bands spanning 3 REAL bands each. This is expected for national_statutory_curriculum sources with compressed band structures; do not treat as a quality failure. Downstream planning must resolve via REAL teacher judgement (e.g. via REAL Crosswalk skill or human PLC)."
  ]
}
```

# Known Limitations

**The skill does not do construct alignment.** Two items tagged Band C are not, by that fact alone, teaching the same thing. Webb's (1997) categorical-concurrence and depth-of-knowledge dimensions are out of scope. The skill answers "is this age-relevant?" not "does this match REAL's learning intentions?" The Crosswalk skill addresses relationship-to-REAL but still requires human judgement for construct alignment.

**Ambiguity is not resolvable by this skill.** When a source's band structure is coarser than REAL's — particularly UK RSHE's 2-band structure and UK Key Stages — the skill deliberately preserves the ambiguity rather than guessing. High ambiguity rates (up to 100% for RSHE) are an honest report of the source's granularity, not a quality failure of the skill. They are resolved downstream by REAL teacher judgement, which is why `teacher_review_flag` exists. A skill run on RSHE that reported clean unambiguous band assignments would be *wrong*.

**Developmental-descriptor inference (CASEL case) is approximate.** When a framework has no age-banding, the skill maps by descriptor — labeling emotions → Band A/B, perspective-taking → Band C/D, systems-level social awareness → Band E/F. These are defensible starting points drawn from developmental-psychology consensus, but they are not framework-specific determinations. CASEL content tagged by this skill should be treated as a scaffold for teacher review, not as a validated mapping.

**The skill assumes harness-validated input.** It does not re-validate the source decomposition. If the upstream harness produced a broken KUD or LT file (cycles in prerequisite graph, content_statement missing, etc.), the skill will pass those errors through as band-tagged nonsense. Run the harness's own validation gates before invoking this skill.
