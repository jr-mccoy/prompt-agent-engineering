---
title: "Extract Handwritten Notes Into Digital Structure"
category: productivity/deep-work
description: "Convert a pile of handwritten pages the user took during a meeting, workshop, or thinking session into one of three structured digital outputs (decision log, action list, idea cluster) — not an OCR dump, and not a retroactive essay — so the notes feed downstream work instead of staying unsearchable."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - OC-01
  - QA-01
difficulty: beginner
tags:
  - deep-work
  - notes
  - handwritten
  - capture
  - synthesis
updated: "2026-04-20"
related_prompts:
  - domain-productivity/deep-work/deepwork_block_end_context_capture.md
  - domain-productivity/deep-work/deepwork_project_state_synthesis.md
---

# Extract Handwritten Notes Into Digital Structure

**Objective:** Take a set of handwritten pages (transcribed, photographed, or described) and produce exactly one of three structured outputs — decision log, action list, or idea cluster — chosen by the nature of the notes. Not a verbatim transcription, not an essay. Output must be searchable and usable.

**When to use:** After a meeting, workshop, whiteboard session, or paper thinking session where the user wrote by hand. Before the notes go stale (within 48 hours is dramatically better than after).

**Audience:** The individual who took the notes, digitizing for their own downstream use. Not producing meeting minutes for others.

---

## Inputs Required

1. **The notes themselves.** Transcribed text, photos with legible writing, or a description of what's on the pages.
2. **The occasion.** Meeting / workshop / solo thinking / reading. One sentence.
3. **Participants (if any) and their roles.**
4. **The user's intent when taking the notes.** Decide something, capture ideas, track actions, or "I wasn't sure, I just wrote things down." The last answer is allowed and changes the recommendation.
5. **Whether any mark on the page was meaningful** — stars, arrows, boxes. If yes, describe the mark system; if no, say no.

If the notes are illegible or missing, stop and ask rather than guess.

---

## Instructions

1. **Classify the notes into exactly one output type.** Base on input 4 and the content:
   - **Decision log** — if the notes contain resolved questions, chosen options, or commitments with named owners
   - **Action list** — if the notes contain to-dos, next steps, or follow-ups
   - **Idea cluster** — if the notes are generative: concepts, sketches, fragments, unresolved threads

   If the notes contain two types, split output into two. Do not merge.

2. **For each item extracted, preserve the mark if meaningful.** A starred item is flagged; a boxed item is tagged as a key concept. Do not discard structure the user deliberately added.

3. **Apply the correct output shape:**

   **Decision log:**
   ```
   | Decision | Rationale on page | Owner | Status |
   |---|---|---|---|
   ```
   If owner or rationale is missing, write "not captured" — do not invent.

   **Action list:**
   ```
   - [ ] [action] — owner: [name] — by: [date or "undated"] — source page: [ref]
   ```

   **Idea cluster:**
   Group items by visible affinity (topic, sketch region, thread). Each cluster gets a name you extract from the notes — do not invent a category.

4. **Flag fragile items.** Anything the user may forget the meaning of in 30 days — cryptic phrase, arrow to nowhere, a name without context. Mark with "fragile:" and a specific clarifying question.

5. **Produce one "follow-up to do first."** The single item that, if not acted on this week, makes the rest of the notes worthless.

---

## Output Format

```
## Source
Occasion: [input 2]
Date: [if supplied]
Pages/items covered: [count]

## Output Type
[Decision log / Action list / Idea cluster] — chosen because [one-sentence reason]

## [Selected output, in shape above]

## Fragile Items
- fragile: "[phrase]" — clarifying question: [...]
- ...

## Follow-Up to Do First
[The single highest-decay item.]

## What Was Not Extracted
- [items deliberately skipped, with reason — doodles, unrelated notes, illegible lines]
```

---

## Constraints

**Must:**
- Choose exactly one output type (or split cleanly if two).
- Preserve user-added marks when they have stated meaning.
- Use "not captured" literally rather than invent.
- Flag fragile items with the word "fragile:".

**Must not:**
- Produce a verbatim transcription. The point is structure, not reproduction.
- Expand phrases into full sentences the user didn't write.
- Add analytic commentary ("this suggests...", "notably..."). The user wrote what they wrote.
- Assign owners that weren't in the notes.

---

## False-Positive Prevention

- **Interpretive drift:** A three-word phrase ("maybe ping Sarah") will tempt embellishment ("follow up with Sarah to get her input on the API design"). Do not. "maybe ping Sarah" goes in as-is, with a fragile-item clarifying question.
- **False owner assignment:** If no name is next to an action, owner is "not captured." Do not default to the user.
- **Merged types:** Forcing decisions, actions, and ideas into one document destroys the usefulness of each. Split into two outputs if needed.
- **Illegibility laundering:** If you cannot read a line, say so. Do not guess and present as fact.

---

## Self-Verification (before finalizing)

- [ ] Exactly one output type chosen (or cleanly split into two).
- [ ] Every extracted item has a source reference (page/area).
- [ ] "Not captured" used where owner/rationale/date is missing.
- [ ] Fragile items labeled and each has a clarifying question.
- [ ] Exactly one "follow-up to do first" named.
- [ ] No invented owners, dates, or expansions.
