---
title: "Biblical Ethics — Framing a Moral Question Across Scripture and Traditions"
category: biblical-studies/theology-research
description: "Frame a moral or ethical question against the biblical material and the major ethical traditions: gather the relevant texts (by address, in context), separate what the text describes from what it commands, account for cultural distance and genuine diversity in Scripture, and present the competing ethical frameworks descriptively without issuing a verdict or fabricating sources."
techniques:
  - RT-02
  - RT-03
  - RP-03
  - QA-04
  - QA-05
difficulty: advanced
tags:
  - biblical-ethics
  - moral-question
  - descriptive-prescriptive
  - multi-tradition
  - neutrality
updated: "2026-06-06"
related_prompts:
  - domain-biblical-studies/theology-research/biblical_difficult_passage_analysis.md
  - domain-biblical-studies/theology-research/biblical_doctrine_study_neutral.md
  - domain-biblical-studies/sermon-devotional/biblical_application_bridge_builder.md
---

# Biblical Ethics — Framing a Moral Question

**Objective:** Work through a moral question with the biblical material and the major ethical traditions in view — gathering the relevant texts in context, separating description from command, naming where Scripture is diverse or silent, and presenting how different ethical frameworks reason about it — without handing the user a verdict or inventing sources.

> **STRONG-GUARD prompt.** Ethics tempts the model toward proof-texting a position and quoting ethicists from memory. This prompt gathers texts by address, distinguishes descriptive from prescriptive material, attributes ethical reasoning to identifiable frameworks/streams, and flags every named source as verify-required.

**When to use:**
- Thinking through a moral/practical question (e.g., wealth, violence, speech, divorce, justice, truth-telling) with Scripture and the ethical traditions in view.
- Preparing teaching, writing, or counsel that must represent the range fairly.

**When NOT to use:**
- The difficulty is a single hard text (apparent contradiction or hard saying) — use `biblical_difficult_passage_analysis.md`.
- You want a doctrine (not a moral question) across traditions — use `biblical_doctrine_study_neutral.md`.
- You already have the ethic and want contemporary application — use `biblical_application_bridge_builder.md`.

**Audience:** Pastors (P), seminary/academic (A), equipped leaders (G).

---

## Inputs / Context

1. **The moral question.** Stated precisely (what action/issue, in what situation).
2. **Texts in hand (optional).** To organize, not invent.
3. **Frameworks of interest (optional).** E.g., divine-command, virtue, natural-law, consequentialist-adjacent, kingdom/redemptive-movement readings.
4. **Declared tradition (optional).** May foreground that stream's ethic; alternatives still presented, no verdict.

---

## Constraints

### Must
- Gather the relevant texts **by address**, read in context (verify-required); include texts that pull in different directions, not only the convenient ones.
- For each text, distinguish **what it describes** (narrates as happening) from **what it commands/commends** (prescribes), and note the original audience/situation.
- Name **cultural distance** issues (where the situation behind the text differs from the contemporary one) without using distance to dissolve the text.
- Present how **different ethical frameworks** reason about the question, attributed to identifiable streams; surface the cruxes where they diverge.
- Flag where Scripture is **genuinely diverse** or **silent** on the specific question.

### Must Not
- Proof-text a single position; ignore counter-testimony; or invent texts, quotations, ethicists, or sources.
- Collapse descriptive narrative into a command (or treat a command as merely descriptive to avoid it).
- Issue a verdict on what the user ought to do, or present one framework's conclusion as the biblical one.

### Tradition-neutral stance (Must / Must Not)
- **Must:** represent each framework charitably and attribute it; preserve genuine moral disagreement.
- **Must Not:** endorse one ethic as correct or manufacture a consensus the traditions don't share.

---

## Instructions

### Step 1 — State the question
One precise sentence: the action/issue and the situation in view.

### Step 2 — Gather the biblical material
Collect texts by address (verify-required, in context), including texts that cut different ways. For each, mark describes vs. commands and the original audience.

### Step 3 — Account for distance and diversity
Note cultural-distance issues and where Scripture is diverse or silent on the precise question — without dissolving the texts.

### Step 4 — Frameworks' reasoning
For each ethical framework, summarize how it reasons from the material to a stance, attributed to its stream; name the cruxes where frameworks diverge.

### Step 5 — Honest close
Summarize where the biblical material is clear, where it is diverse/silent, where the frameworks genuinely differ, and what a responsible decision would have to weigh — no verdict.

---

## Output Format

```
# Biblical Ethics — [moral question]

## The question
> [precise: action/issue + situation]

## Biblical material (by address, verify-required, in context)
| Text | Describes / Commands | Original audience/situation | Note |
|------|----------------------|-----------------------------|------|
| [addr] | describes/commands | [..] | [..] |

## Distance & diversity
- Cultural-distance issues: [..] | Diverse within Scripture: [..] | Silent on: [..]

## Frameworks' reasoning (attributed; named sources verify-required)
- [Framework/stream A]: [reasoning → stance]
- [Framework/stream B]: [reasoning → stance]
- Cruxes where they diverge: [..]

## Honest close
- Clear in the material: [..] | Diverse/silent: [..] | Genuine divergence: [..]
- What a responsible decision must weigh (no verdict): [..]
```

---

## Verification

- [ ] Texts by address, in context, verify-required; counter-testimony included, not just convenient texts.
- [ ] Describes vs. commands marked for each text; original audience noted.
- [ ] Cultural-distance and Scripture-internal diversity/silence flagged honestly.
- [ ] Frameworks attributed to streams; cruxes named; no fabricated ethicists/sources.
- [ ] No verdict issued; no single framework's conclusion presented as the biblical one.

---

## False-Positive Prevention

❌ **DON'T:**
- Assemble the texts that support one stance and skip the ones that complicate it.
- Turn a narrative ("X happened") into a command ("therefore do X"), or explain away a command as "just descriptive."
- Quote an ethicist or tradition from memory and end by telling the user what to do.

✅ **DO:**
- Gather texts by address including counter-testimony; mark describes vs. commands.
- Name cultural distance and Scripture's own diversity/silence without dissolving the text.
- Attribute each framework's reasoning, flag sources verify-required, and leave the decision with the user.
