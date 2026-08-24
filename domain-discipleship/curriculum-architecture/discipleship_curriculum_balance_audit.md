---
title: "Curriculum Balance Audit — Gaps, Imbalance, and Smuggled Distinctives"
category: discipleship/curriculum-architecture
description: "Audit an existing discipleship curriculum against the five formation domains to surface coverage gaps, over-weighting, missing practice, and tradition-specific distinctives that have entered as unmarked assumptions — reporting findings with evidence from the supplied material rather than impressions."
techniques:
  - ST-02
  - RT-02
  - OC-03
  - QA-01
  - QA-04
difficulty: intermediate
tags:
  - discipleship
  - curriculum-architecture
  - audit
  - gap-analysis
  - formation
updated: "2026-08-04"
related_prompts:
  - domain-discipleship/curriculum-architecture/discipleship_formation_outcomes_framework.md
  - domain-discipleship/curriculum-architecture/discipleship_curriculum_architecture.md
  - domain-discipleship/curriculum-architecture/discipleship_material_evaluation.md
  - domain-discipleship/program-operations/discipleship_program_health_review.md
  - domain-biblical-studies/theology-research/biblical_exegetical_fallacy_detector.md
---

# Curriculum Balance Audit

**Objective:** Audit a supplied discipleship curriculum across the five formation domains — Scripture,
character, practice, community, mission — and report coverage gaps, over-weighting, content that forms
no practice, and tradition-specific distinctives that have entered the curriculum as unmarked
assumptions, with every finding tied to evidence in the supplied material.

> **Boundary guardrail.** This audits *material*, not the people who wrote it or teach it. Findings
> describe what the curriculum does and does not cover; they are not judgments of anyone's faithfulness,
> competence, or theology.

**When to use:** You have an existing discipleship curriculum — inherited, purchased, accumulated, or
your own — and need an honest read on what it is actually forming and what it silently omits.

**When NOT to use:**
- You are evaluating whether to *adopt* a third-party product — use `discipleship_material_evaluation.md`.
- You are designing a curriculum from scratch — use `discipleship_curriculum_architecture.md`.
- You are reviewing the health of a *program* rather than its content — use
  `../program-operations/discipleship_program_health_review.md`.
- You are checking an interpretation for exegetical error — use
  `domain-biblical-studies/theology-research/biblical_exegetical_fallacy_detector.md`.

**Audience:** Discipleship pastors, program leads, and curriculum designers reviewing material already
in use.

---

## Inputs / Context

**Required:**

1. **The curriculum.** Module list, session outlines, topics, and Scripture references, supplied in a
   `<curriculum>` block. Outlines are sufficient; full text is better. The audit reports only on what
   is supplied.
2. **What it is for.** Intended participant, duration, and delivery context.
3. **Stated intent.** What the curriculum's authors or owners say it is meant to produce, if known.
   Findings are strongest when measured against the curriculum's own claims.

**Optional:**

4. **Declared tradition (optional).** If the curriculum belongs to a declared tradition, distinctives
   of that stream are reported as **intentional commitments** rather than smuggled assumptions — but
   they are still surfaced, because a participant should know what is confessional and what is shared.
5. **Formation outcomes framework.** If one exists (see
   `discipleship_formation_outcomes_framework.md`), the audit measures coverage against it rather than
   the generic five domains.

**If any required input is missing:** Ask clarifying questions before proceeding. Do not audit a
curriculum you have only been told about — an audit of a description produces findings about the
description.

---

## Constraints

### Must

- Tie **every finding to specific evidence** in the supplied material: the module, session, or line
  that supports it. A finding without a locator is an impression and must be dropped or marked as such.
- Report coverage across all five domains, distinguishing **absent** from **thin** from **present**.
- Distinguish **content coverage** (a topic is taught) from **practice formation** (the participant
  does something) and report where the curriculum has the first without the second.
- Surface tradition-specific distinctives that appear **unmarked**, and say which stream holds them and
  what the alternatives are.
- Separate findings by confidence: **Confirmed** (directly evidenced in the material), **Probable**
  (strongly implied), **Cannot assess** (the supplied material is insufficient).
- Report what the supplied material was **not sufficient to assess**, explicitly.
- Where a gap is found, describe the *kind* of module that would fill it — not a named product.

### Must Not

- Report a gap or imbalance that cannot be located in the supplied material.
- Infer the curriculum's theology from its omissions. A curriculum that does not cover a topic in the
  supplied excerpt may cover it elsewhere; that is a "cannot assess," not a finding.
- Quote Scripture text from memory when checking a reference; confirm the address is present and note
  that wording is verify-required.
- Invent statistics, research, benchmarks, or "typical" coverage percentages against which to compare.
- Recommend a named published resource to fill a gap.
- Treat a declared tradition's intentional distinctive as an error. It is reported as a commitment, and
  the finding is whether it is *marked* as one.
- Score the curriculum numerically or assign it a grade.

### Tradition-neutral stance (Must / Must Not)

- **Must:** distinguish shared-core content from stream-specific content throughout; where the
  curriculum takes a position on a contested practice, report the position, the streams, and whether
  the curriculum acknowledges the disagreement.
- **Must Not:** treat any one tradition's coverage pattern as the balanced baseline against which
  others are deficient, or flag a tradition's distinctive as a defect merely for being distinctive.

---

## Instructions

### Step 1 — Inventory what was supplied

List every module and session in `<curriculum>` with its topic and Scripture addresses. State plainly
what form the material took (full text, outlines, titles only) — this bounds every finding that follows.

### Step 2 — Map coverage to the five domains

For each module, mark which of the five formation domains it addresses. Build the coverage matrix.
Mark each domain overall as absent, thin, or present, with the evidence.

### Step 3 — Test content against practice

For each module, ask whether a participant *does* anything as a result, and what. Flag every module
that teaches a topic without forming a practice. This is the most common finding in real discipleship
curricula and it is worth reporting even when it is pervasive.

### Step 4 — Detect unmarked distinctives

Scan for positions on contested practices — baptism, sacraments, spiritual gifts, church governance,
gender roles, eschatology, sanctification, confession, alcohol, political engagement — that the
curriculum asserts without flagging as contested. For each, name the position, the streams, and the
alternatives.

### Step 5 — Check the Scripture handling

Confirm that Scripture references are present and relevant to their module's claim. Flag references
used as proof-texts against context, and flag modules whose claims carry no Scripture at all. Do not
attempt exegesis here — route detailed concerns to
`domain-biblical-studies/theology-research/biblical_exegetical_fallacy_detector.md`.

### Step 6 — Assess against stated intent

Compare findings to what the curriculum claims to produce. Where the material cannot deliver the stated
intent, say so with evidence.

### Step 7 — Grade confidence and report limits

Assign every finding a confidence level. Then write what the supplied material was insufficient to
assess, and what would need to be supplied to close each of those.

---

## Output Format

Produce exactly this structure. Use `[..]` where a value depends on user input.

```
# Curriculum Balance Audit — [curriculum name]

## What Was Audited
- Material supplied: [full text | session outlines | module titles only]
- Modules reviewed: [n]
- Stated intent: [..]
- Declared tradition: [declared tradition | none stated]
- **Bound on these findings:** [what the supplied form of the material does and does not allow]

## Coverage Matrix
| Module | Scripture | Character | Practice | Community | Mission |
|---|---|---|---|---|---|
| [..] | ● | ○ | ● | — | — |

Legend: ● addressed · ○ touched lightly · — not addressed

## Domain Findings
| Domain | Status | Evidence | Confidence |
|---|---|---|---|
| Scripture | present / thin / absent | [module, session] | Confirmed / Probable / Cannot assess |

## Content Without Practice
| Module | Topic taught | Practice formed | Finding |
|---|---|---|---|

## Unmarked Distinctives
| Module | Position asserted | Streams holding it | Alternatives | Marked as contested? |
|---|---|---|---|---|

## Scripture Handling
| Module | Reference | Concern | Confidence |
|---|---|---|---|

## Against Stated Intent
| Claim | Can the material deliver it? | Evidence |
|---|---|---|

## Gaps and What Would Fill Them
| Gap | Kind of module needed | Where it would sit |
|---|---|---|

## Could Not Assess
| Question | Why | What would need to be supplied |
|---|---|---|
```

---

## Verification

- [ ] Every finding names the module or session it came from.
- [ ] Every finding carries a confidence level.
- [ ] "Cannot assess" is used where the supplied material is genuinely insufficient, rather than
      inferring from silence.
- [ ] No numeric score or grade is assigned to the curriculum.
- [ ] No named published resource is recommended to fill a gap.
- [ ] The bound on findings, set by the form of material supplied, is stated at the top and respected
      throughout.

---

## False-Positive Prevention

❌ **DON'T:**
- Treat an omission in an excerpt as an omission in the curriculum. You audited what you were given.
- Report "no mission content" for a curriculum whose stated scope is the first six weeks after
  conversion. Measure against stated intent, not an ideal.
- Flag a tradition's deliberate distinctive as an error. The finding is whether it is *marked*, not
  whether it is held.
- Invent a benchmark — "most discipleship curricula devote 30% to..." — to make imbalance look
  quantified.
- Diagnose the authors' theology from their coverage choices. A gap has many causes, most of them
  mundane.
- Let "content without practice" findings become a blanket condemnation. Report the pattern, count it,
  and name the modules where it matters most.

✅ **DO:**
- State the bound on your findings before the findings, so a reader with only titles knows how much
  weight the audit carries.
- Separate absent from thin. A thin domain is a different problem with a different fix.
- Name the specific line or session that evidences each finding, so the owner can go look.
- Report unmarked distinctives even when you agree with them — a participant is owed the knowledge of
  what is confessional.
- Use "cannot assess" freely. It is a first-class result here, and it is far more useful than a
  confident guess.
- Describe the *kind* of module a gap needs and where it would sit in the existing sequence.

---

## Techniques Used

- **ST-02 (Structured Sequential Instructions):** inventory → coverage → practice → distinctives →
  Scripture → intent → confidence, so that every later judgement rests on the bound established in
  Step 1 rather than on general impression.
- **RT-02 (Multi-Dimensional Analysis Framework):** the five formation domains crossed against the
  module list produce a coverage matrix in which a lopsided curriculum becomes visible structurally
  instead of arguable.
- **OC-03 (Markdown Table Specification):** the coverage matrix and finding tables force a locator and
  a confidence level onto every claim, which is what stops the audit degrading into impressions.
- **QA-01 (Self-Verification):** the verification block checks each finding for evidence and confidence
  before the report is issued, and enforces the stated bound on the material.
- **QA-04 (Uncertainty Acknowledgment):** "Cannot assess" is a first-class output with its own table,
  so silence in the supplied material is never converted into a confident finding about the curriculum.

---

## Related Prompts

- [`discipleship_formation_outcomes_framework.md`](discipleship_formation_outcomes_framework.md) —
  supplies the outcomes this audit can measure coverage against
- [`discipleship_curriculum_architecture.md`](discipleship_curriculum_architecture.md) — rebuild once
  the audit shows the gaps
- [`discipleship_material_evaluation.md`](discipleship_material_evaluation.md) — evaluating third-party
  material before adopting it
- [`../program-operations/discipleship_program_health_review.md`](../program-operations/discipleship_program_health_review.md) —
  the program-level counterpart to this content-level audit
- [`domain-biblical-studies/theology-research/biblical_exegetical_fallacy_detector.md`](../../domain-biblical-studies/theology-research/biblical_exegetical_fallacy_detector.md) —
  where detailed Scripture-handling concerns route
