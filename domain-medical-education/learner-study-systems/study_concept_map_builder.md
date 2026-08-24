---
title: "Concept Map Builder (Hierarchical + Cross-Link, Text-Format)"
category: medical-education/learner-study-systems
description: "Build a text-format concept map of a topic with hierarchical structure plus cross-links. Output is a numbered node list, edge list with labeled relationships, and a free-text outline format that can be transcribed into any mapping tool. Includes an integrity audit (every edge has a labeled relationship; no orphan nodes; no untested cross-links)."
techniques:
  - ST-02
  - ST-03
  - DT-01
  - RT-04
  - NE-04
  - QA-01
difficulty: intermediate
intended_use: model-testing
target_users:
  - medical-student-pre-clinical
  - medical-student-clinical
  - intern
  - nursing-student
  - pa-student
  - pharmacy-student
  - allied-health-student
tags:
  - concept-map
  - visual-learning
  - integration
  - synthesis
  - study-system
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-study-systems/study_lecture_slide_to_study_guide.md
  - domain-medical-education/learner-study-systems/study_retrieval_practice_drill_designer.md
  - domain-medical-education/learner-foundational-sciences/study_pathophysiology_disease_mechanism_drill.md
  - domain-medical-education/learner-clinical-reasoning/reason_diagnostic_schema_designer.md
---

## Objective

Build a **text-format concept map** of a stated topic that a learner can transcribe into any mapping tool (XMind, Obsidian Canvas, Excalidraw, paper). Output: numbered nodes, labeled edges (`A —relation→ B`), hierarchical outline view, and a cross-link section. Every edge must have a named relationship; no edges of form "A relates to B." End with an integrity audit and 3 "test-the-map" recall questions.

## Your Role

Synthesis cartographer. You're not building a list — you're building a structure that surfaces how concepts *connect*. You hunt for cross-links between hierarchical branches because that's where most concept-mapping value lives: not in the tree but in the unexpected diagonal connection.

## Inputs

- `topic`: e.g., "Renal physiology," "Heart failure," "Hyponatremia," "Antibiotic resistance mechanisms"
- `learner_level`: `pre-clinical | clinical | intern | resident | nursing-student | pa-student | pharmacy-student`
- `target_depth`: `shallow (3 levels, ~15 nodes) | medium (4 levels, ~25 nodes) | deep (5 levels, ~40 nodes)` (default medium)
- `relationship_vocab`: optional override of the default 8 relationship verbs
- `cross_link_target_count`: minimum cross-links between hierarchical branches (default 3)
- `include_pathophys_chain`: bool — if true, force at least one chain of `cause → effect → effect → effect` ≥ 4 steps
- `output_dot_graph`: bool — emit a Graphviz DOT block in addition to outline

## Method

1. **Lock the root node.** The topic is node 0. State its scope in one sentence.

2. **Build the hierarchy (DT-01).** Decompose into 3–5 first-order branches. Each branch decomposes into sub-nodes. Reach `target_depth` level. Stop early if depth would force fabrication of low-yield nodes.

3. **Number every node.** Use Dewey-style numbering (0, 1, 1.1, 1.1.1, 2, 2.1, ...) so transcription is unambiguous.

4. **Use a fixed relationship vocab** (override with `relationship_vocab`). Default 8 verbs:
   - `causes` (mechanism)
   - `is a type of` (taxonomy)
   - `is treated with` (intervention)
   - `is diagnosed by` (test)
   - `discriminates from` (DDx)
   - `correlates with` (epi/lab)
   - `precedes / follows` (temporal)
   - `inhibits / activates` (regulatory)

   Every edge must use one. Edges without a verb are rejected.

5. **Find cross-links (RT-04 analogical).** Cross-links are edges between two non-sibling branches. Generate at least `cross_link_target_count`. Cross-links are where the integration value is — they reveal that two seemingly separate concepts share mechanism, treatment, or risk.

6. **Force pathophys chain (if `include_pathophys_chain`).** Identify the longest plausible cause → effect chain in the map. ≥ 4 hops. Number the chain explicitly.

7. **Render in three formats:**
   - **Outline** (Markdown nested list).
   - **Edge list** (`A —relation→ B` per row).
   - **DOT** (Graphviz block, optional).

8. **Integrity audit (QA-01 self-verify):**
   - Every node ≥ depth 2 has at least one inbound edge.
   - No orphan nodes.
   - No edge uses "relates to" / "is associated with" / "involves" (vague verbs banned).
   - At least `cross_link_target_count` cross-links present.
   - No invented sub-node not supported by the topic at `learner_level`.

9. **3 test-the-map questions (NE-04 good-vs-bad calibration).** Three retrieval questions that the map should answer if it's well-built:
   - One pathophys-chain question.
   - One discriminator question between two hierarchy branches.
   - One cross-link question requiring traversing a non-sibling edge.

## Output Format

```
CONCEPT MAP — [topic]
Level: [...]   Target depth: [...]   Cross-links target: [N]

>>> ROOT
Node 0: [topic] — [one-sentence scope]

>>> OUTLINE
- 0 [topic]
  - 1 [branch 1]
    - 1.1 [sub-node]
      - 1.1.1 [...]
    - 1.2 [...]
  - 2 [branch 2]
    - 2.1 [...]
  - 3 [branch 3]
    - 3.1 [...]
  ...

>>> EDGE LIST (hierarchical)
1.1 —is a type of→ 1
1.1.1 —causes→ 1.1
2.1 —is treated with→ 2.2
...

>>> CROSS-LINKS (non-sibling, ≥ [N])
1.1.2 —shares mechanism with→ 3.2.1   (why: both involve [shared concept])
2.3 —discriminates from→ 1.1   (why: [discriminator])
3.1 —precedes→ 2.1   (why: [temporal])
...

>>> PATHOPHYS CHAIN (if requested, ≥ 4 hops)
1.1 → causes → 1.1.2 → activates → 2.3 → causes → 2.3.1 → presents as → 2.3.1.a

>>> DOT GRAPH (optional)
digraph topic {
  rankdir=LR;
  "0" -> "1" [label="contains"];
  "1.1" -> "1" [label="is a type of"];
  ...
}

>>> INTEGRITY AUDIT
- Nodes total: [N]
- Edges total: [N]
- Cross-links: [N] (target: [N]) — [met / not met]
- Orphan nodes: [list or "none"]
- Vague-verb edges: [list or "none"]
- Pathophys chain length: [N] hops

>>> TEST-THE-MAP QUESTIONS (3)
Q1 (pathophys chain): [question that requires traversing the chain] — Answer: [path]
Q2 (discriminator): How do [branch X] and [branch Y] differ? — Answer: [edge invoked]
Q3 (cross-link): Why does treating [X] also affect [Y]? — Answer: [cross-link edge invoked]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `target_depth` | Shallow = overview; deep = study-for-shelf |
| `relationship_vocab` | Override default 8 verbs (e.g., add `regulates` for endocrine maps) |
| `cross_link_target_count` | Higher = harder synthesis; 3 is floor for genuine integration |
| `include_pathophys_chain` | Forces a long causal chain explicit in the map |
| `output_dot_graph` | Adds Graphviz block for tool rendering |
| `compare_to_existing_map` | If learner pastes their own map, render a diff (missing nodes, weak verbs, missed cross-links) |
| `embed_in_anki` | Generate Anki cards keyed to cross-link edges (one card per cross-link) |

## Verification Checklist

- [ ] Root node has a one-sentence scope.
- [ ] Every node has a Dewey-style ID; IDs are unique.
- [ ] Every edge uses one of the locked relationship verbs (or `relationship_vocab`); no "relates to."
- [ ] At least `cross_link_target_count` cross-links between non-sibling branches.
- [ ] No orphan nodes at depth ≥ 2.
- [ ] If `include_pathophys_chain`, the chain is ≥ 4 hops and is rendered as a single line.
- [ ] Test-the-map Q3 specifically requires a cross-link edge; if the map can't answer Q3, the map is rebuilt.
- [ ] No fabricated nodes (e.g., invented enzyme names or drug classes); content matches `learner_level`.
- [ ] Outline + edge list + (optional) DOT are all consistent — same node IDs throughout.
- [ ] If the topic is too narrow to require cross-links (e.g., "definition of glucagon"), the prompt says so and recommends a different topic.

## Worked Example (compact)

**Input:** `topic = "Hyponatremia"`, `learner_level = intern`, `target_depth = medium`, `cross_link_target_count = 3`, `include_pathophys_chain = true`.

**Output:**

```
CONCEPT MAP — Hyponatremia
Level: intern   Depth: medium   Cross-links: 3

>>> ROOT
Node 0: Hyponatremia — serum Na < 135 mEq/L; workup driven by volume status + osmolality + urine indices.

>>> OUTLINE
- 0 Hyponatremia
  - 1 By osmolality
    - 1.1 Hypotonic (true)
    - 1.2 Isotonic (pseudo — lipids/proteins)
    - 1.3 Hypertonic (hyperglycemia)
  - 2 Hypotonic — by volume
    - 2.1 Hypovolemic
      - 2.1.1 Renal loss (diuretics, salt-wasting)
      - 2.1.2 Extra-renal loss (GI, skin)
    - 2.2 Euvolemic
      - 2.2.1 SIADH
      - 2.2.2 Hypothyroidism
      - 2.2.3 Adrenal insufficiency
    - 2.3 Hypervolemic
      - 2.3.1 CHF
      - 2.3.2 Cirrhosis
      - 2.3.3 Nephrotic
  - 3 Treatment
    - 3.1 By chronicity (acute < 48 h vs chronic)
    - 3.2 By severity (asymptomatic, mild sx, severe sx)
    - 3.3 Correction rate (≤ 8 mEq/24 h chronic)
    - 3.4 ODS risk
  - 4 Diagnostics
    - 4.1 Serum osm
    - 4.2 Urine osm
    - 4.3 Urine Na
    - 4.4 TSH, cortisol

>>> EDGE LIST
1.1 —is a type of→ 1
2.1 —is treated with→ "isotonic saline"
2.2.1 —is a type of→ 2.2
2.3.1 —is treated with→ "fluid + Na restriction + diuresis"
3.3 —prevents→ 3.4
...

>>> CROSS-LINKS (3+)
2.1.1 —shares mechanism with→ 2.2.1 (both can present with low urine Na; diuretics complicate)
2.3.1 —discriminates from→ 2.2.1 (CHF: high BNP, edema; SIADH: euvolemic, normal BNP)
4.3 —discriminates between→ 2.1 vs 2.2 (UNa < 20 → extra-renal vs UNa > 40 → SIADH/renal)
3.3 —cross-links to→ 3.4 (rapid correction → ODS)

>>> PATHOPHYS CHAIN (≥ 4 hops)
2.2.1 (SIADH) → causes → 2.2.1.a (free water retention) → causes → 0 (dilutional ↓Na) → corrected too fast → 3.4 (ODS)

>>> INTEGRITY AUDIT
- Nodes: 23   Edges: 28   Cross-links: 4 (target 3 — met)
- Orphan nodes: none
- Vague-verb edges: none
- Pathophys chain: 4 hops ✓

>>> TEST-THE-MAP QUESTIONS
Q1 (pathophys chain): How does SIADH cause ODS? → SIADH → free H2O retention → dilutional ↓Na → over-rapid correction → ODS.
Q2 (discriminator): How distinguish CHF-hyponatremia from SIADH? → Volume status (hypervolemic vs euvolemic), BNP, UNa pattern; cross-link 2.3.1 ↔ 2.2.1.
Q3 (cross-link): Why does urine Na pattern matter for discriminating 2.1 vs 2.2? → Cross-link 4.3 → 2.1 vs 2.2: low UNa = extra-renal hypovolemic; high UNa = SIADH or renal loss.
```
