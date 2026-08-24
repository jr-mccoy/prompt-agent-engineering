---
title: "Exegetical Fallacy Detector — Scan an Interpretation for Word-Study, Grammatical, Logical, Historical, and Systemic Errors"
category: biblical-studies/theology-research
description: "Scan an interpretation or argument the user supplies for common exegetical fallacies — word-study fallacies, grammatical misuse, logical errors, historical/background overreach, and theological-system imposition — naming each fallacy descriptively, showing where it occurs, and suggesting the disciplined alternative, without itself fabricating lexical or historical data."
techniques:
  - ST-02
  - RT-02
  - RT-05
  - QA-04
  - QA-05
difficulty: advanced
tags:
  - exegesis
  - fallacies
  - word-study
  - interpretation
  - critique
  - attribution
updated: "2026-06-19"
related_prompts:
  - domain-biblical-studies/exegesis-interpretation/biblical_passage_exegesis_workflow.md
  - domain-biblical-studies/exegesis-interpretation/biblical_word_study_original_language.md
  - domain-biblical-studies/theology-research/biblical_commentary_evaluation.md
  - domain-biblical-studies/exegesis-interpretation/biblical_multiview_interpretation_map.md
---

# Exegetical Fallacy Detector

**Objective:** Take an interpretation or argument the user supplies and scan it for common exegetical fallacies — naming each fallacy type descriptively, pinpointing where it occurs, explaining why it weakens the argument, and offering the disciplined alternative — without manufacturing the very lexical, grammatical, or historical data needed to "prove" or "disprove" a reading.

> **STRONG-GUARD prompt.** Detecting a word-study or background fallacy can tempt the model to assert the "correct" lexical range, etymology, grammatical parsing, or historical fact as if it knew them. It must not. Name the fallacy and the disciplined method that would resolve it; route the actual data to a lexicon, grammar, or the word-study prompt, and flag every specific linguistic/historical claim as verify-required.

**When to use:**
- You have written (or are reviewing) an interpretation, paper, sermon point, or argument and want it stress-tested for method errors.
- A teaching or commentary claim feels overreaching and you want to name *why*.
- You are training yourself to spot the recurring traps before they reach an audience.

**When NOT to use:**
- You want to build a sound reading from the text rather than critique one — use `biblical_passage_exegesis_workflow.md`.
- The core question is one term's meaning — use `biblical_word_study_original_language.md`.
- You want the legitimate range of interpretations mapped, not a fallacy scan — use `biblical_multiview_interpretation_map.md`.
- You are choosing or weighing commentaries — use `biblical_commentary_evaluation.md`.

**Audience:** Pastors (P), seminary/academic (A), and equipped group leaders (G). Advanced — assumes familiarity with exegetical method.

---

## Inputs / Context

1. **The interpretation/argument under review.** The claim, paragraph, sermon point, or paper section the user wants scanned (pasted by the user).
2. **The passage(s) it concerns.** Reference(s) plus the text in a named translation, supplied by the user. The model references by address and uses supplied text rather than quoting from memory.
3. **The supporting data the argument cites (optional).** Any lexical, grammatical, or historical claims the argument leans on — so the model can flag which ones require verification rather than assert its own.
4. **Declared tradition (optional).** If supplied, the model may note where the argument is internally consistent with that stream, but still flags fallacies on their own terms. No declaration → neutral default.
5. **Depth / output length.** Quick scan vs. full annotated audit.

---

## Constraints

### Must
- Classify each suspected fallacy **descriptively** by category: word-study (root fallacy, etymologizing, illegitimate totality transfer, anachronism, semantic-domain misuse), grammatical, logical (false either/or, appeal to selective evidence, word=concept equation), historical/background, and presuppositional/theological-system overreach.
- Quote or point to the **exact location** in the supplied argument where the fallacy occurs.
- Explain **why** it is a fallacy and state the **disciplined alternative** (the method or resource that would settle it).
- Distinguish a genuine fallacy from a merely *contested but legitimate* interpretive choice; flag the latter as a difference of view, not an error.
- State confidence on each flag and what evidence would confirm or clear it.

### Must Not
- Assert lexical ranges, etymologies, grammatical parsings, semantic domains, or historical facts from memory in order to adjudicate a flag. Name the method/resource instead.
- Invent citations, cross-references, original-language data, scholar/lexicon attributions, or council/commentary references.
- Treat a reading you disfavor as a fallacy merely because a different stream holds it.
- Manufacture a fallacy where the argument is simply uncertain or appropriately tentative.

### Tradition-neutral stance (Must / Must Not)
- **Must:** assess method, not conclusions; describe competing positions fairly, attributed to identifiable streams; treat doctrinal/interpretive claims as positions, not fact; label confidence on contested flags.
- **Must Not:** privilege/endorse any single tradition as correct; brand a stream's legitimate reading a "fallacy"; smooth genuine disagreement into false consensus.

---

## Instructions

### Step 1 — Orient
Restate what is being reviewed: the argument's main claim, the passage(s) it concerns, and the supporting data it cites. Name the genre of the source (sermon point, paper, commentary excerpt) in a line.

### Step 2 — Map the argument's moves
Break the argument into its discrete inferential steps: what it observes, what it claims a word/grammar/background means, and what conclusion it draws from each. This exposes where a leap occurs.

### Step 3 — Scan by fallacy category
Work each category in turn (RT-02 multi-dimensional):
- **Word-study:** root fallacy, etymologizing, illegitimate totality transfer, anachronistic sense, semantic-domain misuse, word=concept.
- **Grammatical:** misused tense/voice/mood claims, overloaded particles/prepositions, parsing asserted without support.
- **Logical:** false either/or, selective evidence, question-begging, non sequitur from data to conclusion.
- **Historical/background:** parallels or customs asserted to control meaning without warrant.
- **Presuppositional/systemic:** a theological system read *into* the text as though the text states it.
For each, mark present / not evident / cannot assess from supplied data.

### Step 4 — Locate and explain each flag
For every flag, point to the exact phrase, name the fallacy descriptively, explain why it does not follow, and name the disciplined alternative (e.g., "establish sense from usage in context via a lexicon, not from the root").

### Step 5 — Separate fallacy from legitimate disagreement
For each flag, decide: is this a method error, or a contested-but-defensible choice attributable to a stream? Reclassify the latter as a difference of view, attributed, not adjudicated.

### Step 6 — Confidence & verification routing
For each flag, give confidence (low/moderate/high) and the specific data/resource that would confirm or clear it (lexicon, grammar, the word-study prompt, primary background source). Mark all such data verify-required; assert none from memory.

### Step 7 — Repair summary (optional)
If the user wants it, summarize how the argument could be restated to keep its legitimate insight while dropping the fallacious moves — without supplying invented data to do so.

---

## Output Format

```
# Exegetical Fallacy Scan — [argument / reference]

## Orientation
- Claim under review: [..] | Passage(s): [..] | Cited support: [..]

## Argument moves
1. [observation/claim] → [inference] → [conclusion]
2. ...

## Flags by category
- Word-study: [present/not evident/cannot assess] — [location] — [why] — [disciplined alternative] (confidence: ..; verify: ..)
- Grammatical: [..]
- Logical: [..]
- Historical/background: [..]
- Presuppositional/systemic: [..]

## Fallacy vs. legitimate disagreement
- [flag] → method error / contested choice ([stream])

## Verification routing
- [data needed] → [lexicon / grammar / word-study prompt / source] (verify-required)

## Repair summary (optional)
- [restatement preserving the insight, dropping the fallacy]
```

---

## Verification

- [ ] Each flag classified descriptively by category and located in the exact text.
- [ ] Each flag explains *why* and names the disciplined alternative.
- [ ] No lexical, grammatical, or historical data asserted from memory to adjudicate any flag.
- [ ] No invented citations, cross-references, original-language data, or scholar/lexicon attributions.
- [ ] Genuine fallacies distinguished from contested-but-legitimate readings (latter attributed to streams).
- [ ] Each flag carries confidence + a verification route.

---

## False-Positive Prevention

❌ **DON'T:**
- "Prove" a fallacy by asserting the word's "real" meaning, etymology, or grammatical force from memory.
- Brand a different stream's defensible reading a "fallacy" because you disagree with its conclusion.
- Invent a parallel custom or cross-reference to show the argument's background claim is wrong.
- Manufacture an error where the argument is simply tentative or appropriately hedged.

✅ **DO:**
- Name the fallacy and the method/resource that would actually resolve it.
- Separate method errors from legitimate contested choices, and attribute the latter to streams.
- Flag every lexical/grammatical/historical data point as verify-required and route it.
- State confidence and a change condition on each flag.

---

## Techniques Used

- **ST-02 (Structured Sequential Instructions):** The 7-step sequence (Orient → Map moves → Scan by category → Locate/explain → Separate from legitimate disagreement → Verify → Repair) prevents drive-by accusations by forcing the argument to be decomposed before any flag is raised.
- **RT-02 (Multi-Dimensional Analysis Framework):** The category-by-category scan (word-study, grammatical, logical, historical, systemic) ensures the audit covers every common failure surface rather than fixating on one.
- **RT-05 (Evidence-Based Reasoning):** Each flag must point to an exact location, explain why the inference fails, and name the disciplined alternative — vague "this seems wrong" verdicts are prohibited.
- **QA-04 (Uncertainty Acknowledgment):** Every flag carries a confidence level and a "cannot assess from supplied data" option, and contested-but-legitimate readings are explicitly distinguished from genuine errors.
- **QA-05 (Citation Requirements):** All lexical, grammatical, and historical data needed to adjudicate a flag is marked verify-required and routed to a lexicon, grammar, or the word-study prompt; nothing is asserted from memory as authoritative.
