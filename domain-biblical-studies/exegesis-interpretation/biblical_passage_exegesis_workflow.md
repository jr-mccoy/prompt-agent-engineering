---
title: "Staged Passage Exegesis Workflow — Observation → Context → Structure → Meaning"
category: biblical-studies/exegesis-interpretation
description: "Work a single passage through a disciplined exegetical sequence — observation, historical-literary context, structure/flow, key terms, and meaning — attributing every interpretive claim, distinguishing what the text says from what traditions infer, and flagging where readings legitimately diverge. The flagship exegesis prompt of the domain."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - QA-05
difficulty: intermediate
tags:
  - exegesis
  - interpretation
  - passage-study
  - context
  - attribution
updated: "2026-06-11"
related_prompts:
  - domain-biblical-studies/exegesis-interpretation/biblical_word_study_original_language.md
  - domain-biblical-studies/exegesis-interpretation/biblical_literary_context_structure.md
  - domain-biblical-studies/exegesis-interpretation/biblical_historical_cultural_context.md
  - domain-biblical-studies/exegesis-interpretation/biblical_multiview_interpretation_map.md
  - domain-biblical-studies/sermon-devotional/biblical_application_bridge_builder.md
---

# Staged Passage Exegesis Workflow

**Objective:** Take one passage and move it through a repeatable exegetical sequence that draws meaning *out of* the text, separates observation from interpretation, attributes interpretive claims, and is honest about where the text is clear versus where credible readings diverge.

**When to use:**
- Preparing a careful study, paper, lesson, or sermon on a specific passage.
- You want a structured method rather than jumping straight to "what it means to me."
- Checking your own reading against the text's context and structure.

**When NOT to use:**
- You only need a quick first-look — use `biblical_passage_observation_beginner.md`.
- You're surveying a whole book — use `biblical_book_overview_synthesis.md`.
- The core question is a contested interpretation you want mapped — use `biblical_multiview_interpretation_map.md`.
- The passage is a story and your question is *how it's told* (character, plot, narrator) — use `biblical_narrative_analysis.md`.

**Audience:** Pastors (P), seminary/academic (A), and equipped group leaders (G). Difficulty scales with the passage.

---

## Inputs / Context

1. **The passage.** Reference plus the text in a named translation (pasted by the user). The model references by address and uses the supplied text rather than quoting from memory.
2. **The exegetical question (optional).** A specific question to focus the study (e.g., "What is Paul arguing here and why?").
3. **Declared tradition (optional).** If supplied, the model may foreground that reading and its resources but must still note where it is contested and name main alternatives. No declaration → neutral, multi-view default.
4. **Depth / output length.** Quick study vs. full exegetical brief.

---

## Constraints

### Must
- Separate **observation** (what the text states) from **interpretation** (what it means) from **application** (what to do) — and keep them in that order.
- Attribute interpretive claims: distinguish "the text says" from "this is a [stream] inference."
- Read the passage in its **immediate, book-level, and canonical** context and its **genre**.
- Where credible readings diverge, name the divergence and attribute each reading to an identifiable stream; do not present one contested reading as the plain meaning.
- State confidence on the central interpretive conclusion and what would change it.

### Must Not
- Import meaning the text does not support (eisegesis).
- Invent citations, cross-references, original-language data, or scholar attributions. Reference by address; route language questions to the word-study prompt.
- Collapse genuine interpretive disagreement into false consensus.
- Privilege or endorse a single tradition as correct (unless the user declared one — and even then, note alternatives).

### Tradition-neutral stance (Must / Must Not)
- **Must:** present text + consensus; describe differing positions fairly, attributed to identifiable streams; treat doctrinal/interpretive claims as positions, not fact; label confidence on contested points.
- **Must Not:** privilege/endorse any single tradition as correct; present a contested reading as the plain meaning; smooth genuine disagreement into false consensus.

---

## Instructions

### Step 1 — Orient
Restate the passage reference, genre, and (if given) the exegetical question. Note the book and the passage's place in it in one or two lines.

### Step 2 — Observation
List what the text actually says: who, what, when, where, repeated words, connectors (therefore, but, because), commands, contrasts, cause/effect. Observation only — no interpretation yet.

### Step 3 — Context
- **Immediate:** what precedes and follows, and how this passage fits the flow.
- **Book-level:** how it serves the book's purpose/argument.
- **Historical-cultural:** background that bears on meaning — labeled by confidence; route deep background to `biblical_historical_cultural_context.md` and do not invent.
- **Canonical:** relevant connections elsewhere (by address; mark verify-required).

### Step 4 — Structure & key terms
- Trace the argument/discourse flow (or narrative movement); note structuring devices.
- Flag 1–3 key terms whose sense materially affects meaning; route to `biblical_word_study_original_language.md` rather than inventing lexical data.

### Step 5 — Interpretation
State the passage's meaning in context, claim by claim, each tagged as **text-supported** or **inference (stream)**. Where readings diverge, lay out the main options with their strongest textual basis and attribute each to a stream — without ruling, unless a tradition was declared.

### Step 6 — Confidence & open questions
- Central conclusion + confidence (low/moderate/high) + what would change it.
- Remaining open questions and where to take them (commentary, lexicon, the multi-view prompt).

### Step 7 — Bridge to use (optional)
If the user wants application, hand off to `biblical_application_bridge_builder.md` rather than improvising application here.

---

## Output Format

```
# Exegesis — [reference]

## Orientation
- Genre: [..] | Book context: [..] | Question: [..]

## Observation (what the text says)
- [observation] / [observation] / ...

## Context
- Immediate: [..]
- Book-level: [..]
- Historical-cultural (confidence-labeled): [..]
- Canonical links (by address, verify): [..]

## Structure & key terms
- Flow: [..]
- Key terms (→ word study): [term], [term]

## Interpretation
- [claim] — text-supported
- [claim] — inference ([stream])
- Divergent readings: [Option A — stream + basis] | [Option B — stream + basis]

## Confidence & open questions
- Central conclusion: [..] (confidence: ..; would change if ..)
- Open questions: [..]
```

---

## Verification

- [ ] Observation, interpretation, and application kept distinct and ordered.
- [ ] Each interpretive claim tagged text-supported vs. inference (stream).
- [ ] Immediate, book-level, and canonical context addressed; genre named.
- [ ] No invented citations, cross-references, lexical data, or scholar attributions.
- [ ] Divergent readings attributed to streams, not adjudicated (unless tradition declared).
- [ ] Central conclusion carries confidence + a change condition.

---

## False-Positive Prevention

❌ **DON'T:**
- Jump to "what it means to me" before observing what the text says.
- Read a later doctrine back into the passage as if the text states it (eisegesis).
- Present one contested reading as "the obvious meaning."
- Fill context gaps with invented historical detail or recalled cross-references.

✅ **DO:**
- Move observation → context → structure → interpretation → (handoff to) application.
- Tag every claim as text-supported or stream-inference.
- Name divergent readings with their textual basis and attribute them to streams.
- Mark background and cross-references as confidence-labeled / verify-required.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Opens with a single-sentence objective — a disciplined exegetical sequence that draws meaning out of the text — so the scope is clear before the workflow begins.
- **ST-02 (Structured Sequential Instructions):** The 7-step numbered workflow (Orient → Observe → Context → Structure → Interpret → Confidence → Bridge) prevents jumping to meaning before establishing observation and context.
- **RT-02 (Multi-Dimensional Analysis Framework):** Requires analysis across multiple dimensions — immediate, book-level, historical-cultural, and canonical context — so interpretation addresses the text's full setting.
- **RT-05 (Evidence-Based Reasoning):** Every interpretive claim must be tagged text-supported or stream-inference; contextual data must be confidence-labeled; vague generalities are explicitly prohibited.
- **QA-05 (Citation Requirements):** Cross-references and canonical links are given by address and marked verify-required; nothing recalled from memory is presented as authoritative.
