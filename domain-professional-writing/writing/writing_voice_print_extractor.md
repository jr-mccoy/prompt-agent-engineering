---
title: "Voice Print Extractor — Build a Reusable Voice Spec from a Writing Sample"
category: professional-writing/writing
description: "Analyze a 500+ word writing sample to extract a compact, reusable 'voice print': sentence-length distribution, cadence, signature rhetorical moves, diction tier, punctuation habits, and 3–5 do/don't steering rules to paste into future prompts."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - DS-01
difficulty: intermediate
tags:
  - voice
  - style-analysis
  - reusable-spec
  - tone
  - ghostwriting
updated: "2026-06-07"
related_prompts:
  - domain-professional-writing/writing/writing_precision_doc_edit.md
  - domain-professional-writing/writing/writing_voice_clone_profile_builder.md
  - domain-professional-writing/writing/writing_ux_copy_tone_swap.md
---

# Voice Print Extractor

**Objective:** Analyze a representative writing sample and produce a compact, reusable "voice print" — a structured spec the author can paste into any future prompt so generated or edited text sounds like them.

**When to Use:**
- The author wants AI-assisted drafts that match their established voice.
- A team needs to codify a person's or brand's voice so others (or a model) can write consistently in it.
- Before any ghostwriting, editing, or content-scaling task where voice fidelity matters.
- To diagnose *what specifically* makes a writer's prose recognizable.

**When NOT to use:**
- The sample is under ~500 words or is a mix of several authors — too thin or noisy to extract a stable signal.
- The author wants to *change* their voice rather than reproduce it.
- The sample is heavily edited boilerplate (legal templates, form letters) with no personal signal.

**Audience:** Writers, content teams, brand/marketing leads, ghostwriters, anyone building reusable prompt scaffolding.

---

## Inputs / Context

1. **The writing sample** (500+ words; paste it; wrap in `<sample>...</sample>`). More is better; 1,000–2,000 words gives a sturdier print.
2. **Sample provenance:** is this the author's own unedited writing, or polished/co-written? (Affects how much to trust each signal.)
3. **Intended reuse:** what will the voice print be used for — drafting, editing, social posts, long-form? (Shapes which steering rules matter most.)
4. **Known constraints (optional):** terms the author always/never uses, register that is off-limits.

If only one short sample is available, extract the print but mark confidence Low and note which features are tentative.

---

## Constraints

### Must
- Base every feature on **observable evidence in the sample**, with a short quoted example for each major claim.
- Quantify what can be quantified (approximate sentence-length range and distribution, average words/sentence, punctuation frequency) rather than vague adjectives alone.
- Capture **signature rhetorical moves** — the recurring devices that make the voice recognizable (not generic "uses metaphors").
- Produce a **pasteable spec block** that is self-contained and short enough to drop into a prompt without bloating it.
- Include **3–5 do/don't steering rules** that would most change output if followed.
- Assign a **confidence level** (High/Medium/Low) to the overall print based on sample size and consistency.

### Must Not
- Fabricate features not present in the sample, or generalize from a single occurrence as if it were a pattern.
- Mistake the *topic* of the sample for the *voice* (a piece about finance is not "a financial voice").
- Produce a print so long or abstract that it is useless as a reusable prompt input.
- Flatten distinctive habits into generic praise ("clear and engaging").
- Confuse polished-editor smoothing with the author's native voice when provenance says the text was heavily edited.

---

## Instructions

1. **Measure sentence architecture.**
   - Estimate average words/sentence, the range (shortest to longest), and the distribution shape (uniform? bursty — short punches between long sentences?). Note paragraph length tendency. Quote a representative short and long sentence.

2. **Characterize cadence and rhythm.**
   - How does the prose move? Staccato and clipped, flowing and subordinated, list-like, conversational with asides? Identify the dominant rhythm and any deliberate rhythm breaks the author uses for effect.

3. **Identify diction and vocabulary tier.**
   - Plain / conversational / formal / technical? Concrete vs. abstract leaning? Note characteristic word choices, recurring favorite words, contractions usage, and whether jargon appears (and if it is explained or assumed).

4. **Catalog signature rhetorical moves.**
   - The recurring devices: rhetorical questions, em-dash asides, parallel triads, understatement, direct address ("you"), opening with a claim vs. a scene, analogies, one-line paragraphs for emphasis. Quote one instance of each.

5. **Note punctuation and formatting habits.**
   - Em-dashes vs. parentheses vs. colons; semicolon usage; Oxford comma; sentence fragments for effect; emphasis style (italics, caps, none); list usage.

6. **Note stance and persona.**
   - Degree of certainty (confident / hedged), warmth vs. distance, humor, self-reference, how the author handles disagreement or nuance.

7. **Derive 3–5 steering rules.**
   - The do/don't rules that, if a writer or model followed them, would most reliably reproduce the voice. Each rule should be concrete enough to act on ("keep most sentences under 18 words, break with one long subordinated sentence per paragraph" — not "be punchy").

8. **Assemble the pasteable voice-print spec** and assign overall confidence.

---

## False-Positive Prevention

1. **One occurrence is not a pattern.** A single rhetorical question does not make "uses rhetorical questions" a signature move. Require recurrence (2+ instances) before calling it a habit, or label it tentative.
2. **Topic ≠ voice.** Strip away subject matter; describe *how* the author writes, not *what about*. The same voice should be reproducible on any topic.
3. **Adjective soup.** "Engaging, clear, authentic" is not a voice print. Every descriptor must be backed by a quoted example and, where possible, a number.
4. **Editor smoothing mistaken for native voice.** If provenance says the text was heavily edited, distinctive-but-smoothed features may be the editor's, not the author's — flag this.
5. **Spec bloat.** A voice print longer than ~250 words is too heavy to reuse as a prompt input. Keep it tight.
6. **Over-claiming on a small sample.** A 500-word sample supports a Medium-confidence print at best for some features; do not present tentative patterns as certain.
7. **Steering rules that aren't actionable.** "Be conversational" cannot steer output; "use contractions, address the reader as 'you,' and open with a question" can.

---

## Output Format

```
# Voice Print — [author / brand name]
**Source:** [word count, provenance] | **Overall confidence:** [High/Medium/Low]

## Quantified signal
- Avg sentence length: ~[N] words (range [min]–[max])
- Rhythm: [bursty / flowing / clipped / list-like] — [one line, with example]
- Paragraph tendency: [short / medium / long]

## Diction & vocabulary
- Tier: [plain / conversational / formal / technical]
- Concreteness: [concrete / abstract leaning]
- Notable habits: [contractions, favorite words, jargon handling] — example: "[quote]"

## Signature moves (recurring)
1. [move] — e.g., "[quoted instance]"
2. [move] — e.g., "[quoted instance]"
3. [move] — e.g., "[quoted instance]"

## Punctuation & formatting
- [em-dash / parens / semicolons / fragments / emphasis style / lists]

## Stance & persona
- [certainty, warmth, humor, self-reference]

## REUSABLE STEERING BLOCK (paste into future prompts)
> Write in this voice: [3–5 concrete do/don't rules, ~5–8 lines total]

## Tentative / low-confidence features
- [features needing more sample to confirm — or "none"]
```

---

## Verification

- [ ] Every major feature is backed by a quoted example from the sample.
- [ ] Quantifiable features (sentence length, range, punctuation) are given as numbers/ranges, not adjectives alone.
- [ ] Signature moves are recurring (2+ instances) or explicitly marked tentative.
- [ ] Topic/subject matter has been excluded; the print describes *how*, not *what about*.
- [ ] The steering block is pasteable, self-contained, and ≤ ~250 words.
- [ ] Steering rules are concrete and actionable, not vague adjectives.
- [ ] Overall confidence reflects sample size and consistency.
- [ ] Editor-smoothing vs. native-voice provenance is acknowledged where relevant.
