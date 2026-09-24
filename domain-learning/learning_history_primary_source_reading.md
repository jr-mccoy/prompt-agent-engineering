---
title: "History Primary Source Reading — Sourcing, Contextualization, and Corroboration for the Self-Taught Reader"
category: learning/humanities
description: "Coach an adult reading a historical primary source on their own through the historian's four moves — sourcing, contextualization, close reading, corroboration — learner-attempts-first, with every background fact tagged by provenance and a closing verdict on what the source can and cannot be evidence of; distinct from the classroom lesson in teaching_primary_source_analysis.md and from building a historical argument in learn_history_evidence_claim_tutor.md."
techniques:
  - CM-01
  - RT-05
  - RT-06
  - ED-03
  - QA-04
difficulty: intermediate
tags:
  - history
  - primary-sources
  - historical-thinking
  - self-study
  - humanities
  - adult-learner
updated: "2026-09-24"
reasoning:
  styles: [analytic, evidential, contextual]
  stakes: low
  horizon: hours
  uncertainty: ambiguity
  evidence_quality: sparse
  domain_complexity: single_domain
  collaboration: solo
  output_format: [structured, narrative]
  user_role: [individual, learner]
  mode: [audit, synthesize]
related_prompts:
  - domain-education-teaching/instructor/subject-pedagogy/social-studies/teaching_primary_source_analysis.md
  - domain-education-teaching/learner/stuck-and-confused/learn_history_evidence_claim_tutor.md
  - domain-learning/learning_reading_list_curator.md
---

# History Primary Source Reading — Sourcing, Contextualization, and Corroboration

**Objective:** Help an adult reading history on their own read one primary source the way a historian does. They question who made it and why, place it in its moment, read what it actually says, and check it against other evidence. The reading ends with a clear statement of what the source can and cannot show.

**When to Use:**
- You are reading a history book, an archive, or an online source collection on your own, and you have reached a letter, speech, decree, diary, photograph or report that you want to read properly rather than skim.
- You have a habit of treating a primary source as a window onto "what happened" and want to replace that habit with a routine.
- You want someone to check your reading without handing you the answer first.

**Not this prompt if…**
- You are a teacher designing a lesson that takes students through a source. That is `domain-education-teaching/instructor/subject-pedagogy/social-studies/teaching_primary_source_analysis.md`, which produces a lesson plan, not a reading.
- You already have several sources and need to build and test a historical *claim* from them. That is `learn_history_evidence_claim_tutor.md`, which maps evidence to claims and tests causal reasoning. This prompt works on one source before any claim exists.
- You need to know *which* books or collections to read. Use `domain-learning/learning_reading_list_curator.md`.
- You are working on a biblical or ancient religious text. Use the biblical-studies domain, which has its own conventions for text and translation.

## Inputs / Context

1. **The source itself.** Paste the text or describe the image. Include any headnote, date or attribution that came with it, marked as supplied by the collection.
2. **Where you found it.** A book, an archive, a website, a sourcebook. Say whether it is a translation or an excerpt.
3. **Why you are reading it.** The question you are carrying. "Just curious" is a valid answer.
4. **What you already know** about the period, in a sentence or two.
5. **Other sources to hand**, if any, for corroboration.

## Method

1. **Learner attempts first (ED-03).** Before offering any analysis, ask the learner for their own answer to four questions, one line each: who made this, and for whom? When and where? What does it say? What would you want to check it against? Then work from what they wrote. Do not replace it.

2. **Sourcing.** Establish the source's origin from the text and its attribution, and only from those.
   - Author, their position, and their stake in the events.
   - Intended audience, and whether the text was public or private.
   - Genre and its conventions. A petition exaggerates grievance and a diplomatic report flatters its recipient.
   - Time between the event and the writing.
   - Transmission: is this an original, a translation, an excerpt, or a later copy? Who chose the excerpt?

3. **Contextualization (CM-01).** Place the source in its moment. Tag every background fact you supply:
   - `[in source]`: stated in the text or its attribution.
   - `[general context, verify]`: widely held background that the learner should confirm in a reference work.
   - `[unknown]`: something the reading needs that neither of you has.
   Never supply a specific date, name, number or quotation that the learner has not given and you cannot tag with confidence. Mark it `[unknown]` and say where it could be found.

4. **Close reading (RT-05).** Separate three layers of the text:
   - what it **asserts** (claims of fact),
   - what it **reveals without meaning to** (assumptions, vocabulary, what goes unsaid),
   - what it **wants** (the action or belief it is trying to produce).
   Quote the specific phrase behind every point.

5. **Corroboration (RT-06).** If other sources are supplied, compare them claim by claim: agrees, conflicts, or is silent. If none is supplied, name two *kinds* of source that would corroborate or undercut the key claim, such as a record from the other side, an administrative record, or a later memoir. Do not invent the contents of those sources.

6. **Verdict: evidence of what? (QA-04).** State what this source is good evidence for, what it is weak evidence for, and what it cannot show at all. Give a confidence level for each. A biased source is often excellent evidence of its author's outlook and poor evidence of the events it describes.

7. **Compare with the learner's first attempt.** Say which of their four answers held up, which changed, and why. Name the one move they skipped or rushed, as the thing to practise on the next source.

## Output Format

```
# Source reading — [short title of source]

## Your first read (as given)
Who/for whom: … | When/where: … | What it says: … | Check against: …

## Sourcing
| Question | Answer | Basis |
|---|---|---|
| Author and stake | | [in source] / [general context, verify] / [unknown] |
| Audience, public or private | | |
| Genre and its conventions | | |
| Distance from events | | |
| Transmission (original / translation / excerpt) | | |

## Context
- [fact] [tag]

## Close reading
- Asserts: "[quote]" → …
- Reveals: "[quote]" → …
- Wants: "[quote]" → …

## Corroboration
| Claim | Other source | Agrees / conflicts / silent |
(or: two kinds of source that would test the key claim)

## Evidence of what?
- Strong evidence for: … (Confidence: High/Medium/Low)
- Weak evidence for: …
- Cannot show: …

## Your read vs. this read
Held: … | Changed: … | Practise next time: [one move]
```

## Verification

- [ ] The learner's first read was collected before any analysis was offered.
- [ ] Every contextual fact carries a provenance tag, and none is an untagged invention.
- [ ] Transmission was checked: translation, excerpt and editor are named or marked unknown.
- [ ] Each close-reading point quotes the phrase it rests on.
- [ ] Corroboration either compares real supplied sources or names *kinds* of source without inventing their content.
- [ ] The verdict separates what the source is evidence *of* from what it *describes*, with confidence levels.
- [ ] The closing names exactly one move to practise.

## False-Positive Prevention

1. **The window fallacy.** Treating the source as a transparent account of events. Every reading must include the verdict step, and a vivid source is not a reliable one.
2. **Bias as dismissal.** Calling a source "biased" and stopping there. Bias tells you what the source is evidence *of*. Name that instead of discarding it.
3. **Invented context.** Filling a gap with a confident date, office holder or statistic. Tag it `[unknown]`. A self-taught reader has no teacher to catch the error later.
4. **Invented corroboration.** Saying "other accounts confirm…" without a source in hand. Name the kind of source and stop.
5. **Presentism.** Judging the author's vocabulary by today's meanings without flagging that the words may have shifted.
6. **Excerpt blindness.** Reading a sourcebook excerpt as though it were the whole document. Ask who cut it and what the cut might hide.
7. **Answer-first tutoring.** Delivering the full reading before the learner has tried. That turns a skill into something they only receive.

## Example Output

```
# Source reading — Letter of a Lancashire mill worker to a newspaper, 1842 (excerpt)

## Your first read (as given)
Who/for whom: a worker, to the public | When/where: 1842, Lancashire |
What it says: wages cut, families starving | Check against: wage records

## Sourcing
| Question | Answer | Basis |
|---|---|---|
| Author and stake | Signed "A Spinner"; writing during a wage dispute | [in source] |
| Audience | Newspaper readers, therefore public and persuasive | [in source] |
| Genre | Letter to the editor: selected, possibly edited by the paper | [general context, verify] |
| Distance from events | Written during the events it describes | [in source] |
| Transmission | Excerpt from a modern sourcebook; the omissions are unmarked | [in source] |

## Context
- 1842 saw widespread industrial unrest in northern England [general context, verify]
- The paper's political stance [unknown]: check a newspaper directory or the paper's masthead

## Close reading
- Asserts: "our wages lowered three times since Candlemas" → a claim of fact that can be checked
- Reveals: "we ask no charity" → honour and respectability are central to how the writer presents the case
- Wants: "let the public judge the masters" → aims to turn public opinion against the employers

## Corroboration
No other sources supplied. Would test the key claim: (1) the mill's own wage books or a
parliamentary inquiry into wages; (2) a mill owner's reply printed in the same or a rival paper.

## Evidence of what?
- Strong evidence for: how workers framed their grievance for a public audience (High)
- Weak evidence for: the exact size and timing of the wage cuts (Low, one interested party)
- Cannot show: conditions across the district, or the employers' reasons

## Your read vs. this read
Held: public audience; wage records as a check. Changed: "families starving" is the letter's
framing, not an established fact. Practise next time: transmission. Ask who excerpted the source.
```

## Techniques Used

- **CM-01 (Explicit Context Framing):** contextualization is a separate step with provenance tags, so context is established rather than assumed.
- **RT-05 (Evidence-Based Reasoning):** every close-reading point quotes its phrase, and every verdict rests on the sourcing table.
- **RT-06 (Correlation and Cross-Analysis):** corroboration compares claims across sources as agrees, conflicts or silent.
- **ED-03 (Guided Discovery):** the learner reads first and the reading is built from their attempt.
- **QA-04 (Uncertainty Acknowledgment):** `[unknown]` tags and confidence levels in the verdict.

## Related Prompts

- `domain-education-teaching/instructor/subject-pedagogy/social-studies/teaching_primary_source_analysis.md`: the same four moves as a classroom lesson.
- `domain-education-teaching/learner/stuck-and-confused/learn_history_evidence_claim_tutor.md`: the next step, building a claim from several sources.
- `domain-learning/learning_reading_list_curator.md`: choosing what to read in the first place.
