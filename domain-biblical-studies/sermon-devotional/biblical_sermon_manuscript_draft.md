---
title: "Sermon Manuscript Draft — Convert Outline to Oral-Delivery Manuscript"
category: biblical-studies/sermon-devotional
description: "Convert a sermon outline into a full manuscript formatted for oral delivery — with spoken-language phrasing, transition markers, pace/pause cues, and illustration placement — without fabricating illustrations, statistics, quotes, or story details."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - NE-14
difficulty: intermediate
tags:
  - sermon
  - manuscript
  - preaching
  - oral-delivery
  - writing
updated: "2026-06-25"
related_prompts:
  - domain-biblical-studies/sermon-devotional/biblical_expository_sermon_prep.md
  - domain-biblical-studies/sermon-devotional/biblical_sermon_series_planner.md
  - domain-biblical-studies/sermon-devotional/biblical_sermon_delivery_coaching.md
  - domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_sermon_feedback_debrief.md
---

# Sermon Manuscript Draft

**Objective:** Convert a sermon outline (points, passages, notes) into a full manuscript formatted for oral delivery — using spoken-language phrasing, paragraph breaks for pacing, transition markers, and cues for pauses, emphasis, and illustration placement — so the preacher has a speakable draft they can internalize or bring to the pulpit.

**When to use:**
- You have a complete sermon outline and want a full manuscript.
- You preach from a manuscript (or near-manuscript) and want a speakable draft.
- You want to see your outline in full prose to check flow before delivery.

**When NOT to use:**
- You are building the outline from a passage — use `biblical_expository_sermon_prep.md`.
- You want delivery coaching (pacing, nerves, notes vs. manuscript) — use `biblical_sermon_delivery_coaching.md`.

**Audience:** Pastors (P).

---

## Inputs / Context

1. **The outline.** The user provides their sermon outline: big idea, main points, sub-points, Scripture references, and any illustration or application notes.
2. **Delivery style.** Manuscript (read verbatim), semi-manuscript (internalized, glanced at), or detailed notes (key phrases only).
3. **Time target.** How long the sermon should be when spoken.
4. **Voice notes (optional).** Any stylistic preferences (conversational, formal, storytelling-heavy, direct, etc.).

---

## Constraints

### Must
- Write in spoken English, not written English — short sentences, contractions, direct address ("you"), rhetorical questions, and natural rhythm.
- Include delivery cues: [PAUSE], [SLOW], [EMPHASIS], [LOOK UP], and [ILLUSTRATION: topic] markers the preacher can use or remove.
- Place transition sentences between major sections — the audience can't see the outline's structure.
- Respect the user's outline — the manuscript follows their structure, not a reorganized version.
- Flag where the time target may not fit the content (too much material for the time, or too thin).

### Must Not
- Fabricate illustrations, stories, quotes, statistics, or personal anecdotes — use [ILLUSTRATION: suggested topic] placeholders.
- Add theological content the user didn't include in their outline.
- Write in academic or literary prose — this is meant to be spoken.
- Produce a manuscript so polished the preacher can't make it their own.

### Tradition-neutral stance (Must / Must Not)
- **Must:** match the user's theological tone as expressed in their outline.
- **Must Not:** add theological claims or applications not present in the outline.

---

## Instructions

### Step 1 — Confirm the outline and style
Restate the big idea, main points, delivery style, time target, and any voice notes. Flag if the outline has too much content for the time target.

### Step 2 — Draft the opening
Write a spoken opening that hooks the audience and introduces the big idea. Include a transition to the passage reading.

### Step 3 — Draft the body
For each main point, convert outline bullets into spoken prose:
- Transition sentence from the previous point.
- The point stated clearly (then explained, not the reverse).
- Scripture engagement — how the text is read or referenced.
- Application or illustration placement (use placeholders for fabrication-risk content).
- Delivery cues as appropriate.

### Step 4 — Draft the closing
Write a closing that restates the big idea, lands the final application, and (if applicable) invites a response. Avoid introducing new content in the close.

### Step 5 — Time and pace check
Estimate spoken time (roughly 120–150 words per minute for deliberate preaching). Flag sections that are too dense or too thin for the target.

---

## Output Format

```
# Sermon Manuscript — [title]
Big idea: [one sentence]
Estimated time: [minutes] | Word count: [N] | Style: [manuscript/semi/notes]

---

## Opening
[spoken prose with delivery cues]

## Point 1: [title]
[TRANSITION]
[spoken prose]
[ILLUSTRATION: suggested topic]
[spoken prose]

## Point 2: [title]
[..]

## Closing
[spoken prose]
[PAUSE]
[response invitation if applicable]

---

## Time check
- Target: [..] | Estimated: [..] | Adjust: [sections to cut or expand]
```

---

## Verification

- [ ] The manuscript is written in spoken English (short sentences, contractions, direct address).
- [ ] Delivery cues (PAUSE, SLOW, EMPHASIS) are included.
- [ ] Transitions between sections are explicit.
- [ ] No fabricated illustrations, quotes, or statistics — placeholders used.
- [ ] Time estimate is provided and flagged if it doesn't fit the target.

---

## False-Positive Prevention

DON'T:
- Write in academic or literary prose — this is for speaking.
- Fabricate illustrations, stories, or quotes.
- Reorganize the user's outline without permission.

DO:
- Write in spoken rhythm (short sentences, rhetorical questions, direct address).
- Use delivery cues the preacher can keep or remove.
- Flag time mismatches between content and target length.
