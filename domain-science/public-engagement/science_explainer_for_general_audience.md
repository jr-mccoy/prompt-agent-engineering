---
title: "Explainer for General Audience"
category: science/public-engagement
description: "Drafts a plain-language explainer that builds correct intuition with concrete examples while flagging where each analogy breaks down and stating the boundaries of current knowledge."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - CM-02
  - NE-10
difficulty: advanced
tags:
  - explainer
  - science-communication
  - analogy-limits
  - intuition
  - jargon
  - calibrated-certainty
  - general-audience
  - public-engagement
updated: "2026-06-26"
related_prompts:
  - domain-science/public-engagement/science_social_media_thread_drafter.md
  - domain-science/writing-communication/science_lay_summary_translator.md
  - domain-science/statistics/science_statistical_results_interpreter.md
---

# Explainer for General Audience

**Objective:** Draft a plain-language explainer of a scientific concept or finding that builds *correct* intuition for a non-expert reader. The explainer uses concrete examples and analogies but states explicitly where each analogy breaks down, defines jargon, calibrates certainty, and names the boundaries of current knowledge. The deliverable includes an "analogy limits" table so the reader never mistakes a metaphor for the mechanism.

**When to use:** You need to explain a scientific topic to a lay audience (article, FAQ, museum panel, classroom handout, blog) and want it to be accurate and intuitive without the false confidence that vivid metaphors can create.

**Required inputs:**
- **Discipline.** <field, e.g., immunology, quantum optics, hydrology>
- **Study type.** <if explaining a specific result: observational / experimental / modeling / review; if explaining a concept, note "concept">
- **The finding(s) / claim or concept** (user-supplied; never invented) and the audience/forum — what you're explaining, and who will read it and where.
- **Audience level.** <e.g., general adult, high-school, curious-but-busy professional>

**Optional inputs:**
- Specific misconceptions you want to correct.
- Analogies you already use (to vet for where they mislead).
- Numbers, effect sizes, or uncertainty ranges (user-supplied).
- Length limit and tone/voice constraints.
- Open questions or active debates in the field.

**Constraints — Must:**
- Build intuition with at least one concrete example grounded in everyday experience.
- For every analogy or metaphor used, state where it breaks down — what it gets right and where it misleads.
- Define each jargon term in plain language at first use.
- Calibrate certainty: distinguish established consensus from active debate, and a single result from a body of evidence.
- State the boundaries of current knowledge — what is not yet known or is contested.
- Keep empirical claims separate from value or policy implications.

**Constraints — Must Not:**
- Do not invent findings, statistics, quotes, citations, opponents' positions, or certainty. Draft only from user-supplied facts; mark gaps `[user-supplied]`.
- Do not use hype language ("novel," "groundbreaking," "first-ever," "gold standard," "cure," "breakthrough," "proves") in the drafted explainer.
- Do not let an analogy stand without its limits, or imply the metaphor IS the mechanism.
- Do not flatten genuine uncertainty into false simplicity for readability.

**Instructions:**

1. **Confirm the target.** Restate discipline, study type or "concept," the user-supplied subject, the audience level, and the forum. Mark gaps `[user-supplied]`.
2. **State the takeaway plainly.** Open with one or two sentences capturing the core idea accurately and at the audience's level, calibrated (not oversimplified into wrongness).
3. **Build intuition with a concrete example.** Use an everyday situation that maps onto the mechanism. Prefer examples over abstraction.
4. **Introduce analogies deliberately.** Where an analogy helps, use it — then immediately note what it captures and where it fails. Log each one for the analogy-limits table.
5. **Define jargon inline.** Replace or gloss every technical term at first use; keep necessary terms but make them legible.
6. **Calibrate certainty.** Mark what is well established vs. emerging vs. debated. Attach any user-supplied numbers with their uncertainty.
7. **Draw the knowledge boundary.** Add a short "what we don't yet know" passage naming open questions or active disagreements.
8. **Assemble the analogy-limits table.** For each analogy, fill in what it gets right and where it misleads.
9. **Tone and fact/opinion check.** Keep the voice clear and non-condescending; isolate and label any opinion or implication; remove hype.

**Output format (locked):**

```
## Target (confirmed)
- Discipline / study type or concept:
- Subject (user-supplied):
- Audience level / forum:

## Explainer
### The short version
[1–2 calibrated sentences]
### How it works (with a concrete example)
[plain-language body; analogies used with their limits noted inline; jargon defined at first use]
### What's solid vs. still being worked out
[consensus vs. debate; user-supplied numbers with uncertainty]
### What we don't yet know
[open questions / active debates]

## Analogy Limits
| Analogy | What it gets right | Where it misleads |
|---|---|---|
| [analogy 1] |  |  |
| [analogy 2] |  |  |

## Jargon Glossary
| Term | Plain-language definition |
|---|---|
|  |  |

## Calibration Note
- Established / emerging / debated:
- Empirical vs. opinion separation:
```

**Reporting-standard alignment:** No formal reporting standard; aligns to science-communication best practice — build accurate intuition with concrete examples, define jargon, state analogy limits so metaphors don't create false confidence, calibrate certainty, and mark the boundaries of current knowledge.

**Verification checklist (before delivering):**
- [ ] At least one concrete, everyday example is used to build intuition.
- [ ] Every analogy has its limits stated (what it gets right, where it misleads).
- [ ] All jargon is defined in plain language at first use.
- [ ] Certainty is calibrated (consensus vs. debate; single study vs. body of evidence).
- [ ] A "what we don't yet know" section is present.
- [ ] No hype words appear in the drafted text.
- [ ] No invented findings, statistics, quotes, or citations; gaps marked `[user-supplied]`.
- [ ] Opinion/implication is separated from empirical claims; analogy-limits table is complete.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Metaphor-induced false confidence | A vivid analogy the reader takes as the literal mechanism | Mandatory analogy-limits table; state where each analogy breaks down inline |
| Oversimplification into wrongness | A clean, satisfying explanation that omits a load-bearing caveat | "What's solid vs. still being worked out" section; calibration note forbids flattening uncertainty |
| Smuggled certainty | "Scientists now know" phrasing applied to a single or contested result | Mark established vs. emerging vs. debated; ban "proves" |
| Jargon left undefined | A term that reads fluent to the author but opaque to the reader | First-use glossing requirement; jargon glossary table |
| Value claim as fact | "Therefore we must…" presented as part of the science | Separate and label opinion; keep the explainer body empirical |
```
