---
title: "Speaker Notes and Rehearsal Coach — Cue-Based Notes and a Scored Run-Through Plan"
category: presentations/narrative-delivery
description: "Convert a finished deck or talk outline into cue-based speaker notes (purpose line, key phrases, transition, timing checkpoint, stage direction per slide — not a script), then run a staged rehearsal plan: talk-through, timed run, recorded self-review, and audience run, each scored on named delivery dimensions with a fix list and a stop rule. Distinct from domain-agentic-resources/skills/document-processing/ppt-creator/SKILL.md (generates decks with notes as a by-product) and domain-biblical-studies/sermon-devotional/biblical_sermon_delivery_coaching.md (preaching-specific delivery)."
techniques:
  - DT-03
  - DD-06
  - QA-17
  - CM-02
  - QA-01
difficulty: beginner
tags:
  - presentations
  - speaker-notes
  - rehearsal
  - delivery-coaching
  - public-speaking
  - timing
  - reading-off-slides
  - running-over-time
  - nervous-speaker
updated: "2026-09-24"
related_prompts:
  - domain-agentic-resources/skills/document-processing/ppt-creator/SKILL.md
  - domain-biblical-studies/sermon-devotional/biblical_sermon_delivery_coaching.md
  - domain-presentations/narrative-delivery/presentation_keynote_talk_arc.md
---

# Speaker Notes and Rehearsal Coach

**Objective:** Get a presenter from "the slides are done" to "I can give this talk on time without reading". The prompt produces speaker notes that cue rather than script — enough to recover a lost thread at a glance, not enough to read aloud — and then a rehearsal plan of four escalating runs, each scored on named delivery dimensions, with a fix list between runs and a rule for when to stop rehearsing. Feedback after each run is based on what the presenter reports or records, not on imagined performance.

---

## When to Use

- A deck exists and the presentation is days away.
- You tend to read slides aloud, overrun, or lose your place.
- You have a script and want to wean yourself off it.
- You want structured feedback on a recorded run-through.

**Distinct from:**
- `domain-agentic-resources/skills/document-processing/ppt-creator/SKILL.md` — generates decks, with speaker notes as a component. This prompt starts from an existing deck and focuses on delivery.
- `domain-biblical-studies/sermon-devotional/biblical_sermon_delivery_coaching.md` — delivery coaching for preaching, with its own conventions.
- `domain-medical-education/learner-clinical-rotation/study_oral_presentation_rehearsal.md` — clinical case presentations on rounds.
- `domain-presentations/narrative-delivery/presentation_keynote_talk_arc.md` — fixes the talk's structure; run it first if the arc is not settled.

**When NOT to use:**
- The talk's structure is still wrong — rehearsing a weak arc only makes it fluent.
- You need accessibility-specific accommodations or clinical support for speech anxiety; seek appropriate specialist help.

---

## Inputs / Context

1. **The deck or outline.** Slide titles and content, or section headings.
2. **Time slot.** Total minutes and Q&A allocation.
3. **Setting.** Stage, meeting room, or video; lectern or handheld notes; confidence monitor available?
4. **Known habits.** E.g., speaks fast when nervous, says "so" a lot, reads slides.
5. **Rehearsal time available.** Days and approximate hours.
6. **Run reports (later turns).** Timings, a transcript, or self-observations after each run.

---

## Method

### Step 1 — Write cue-based notes per slide
For each slide:
- **Purpose** — one line: why this slide exists.
- **Key phrases** — 2–4 fragments, not sentences; the exact wording only for the opening line, any statistic, and the close.
- **Transition** — the bridge phrase into the next slide.
- **Timing checkpoint** — cumulative minute mark when this slide should end.
- **Stage direction** — pause, click, look at the room, demo switch.
Cap notes at about 40 words per slide.

### Step 2 — Set the delivery dimensions
Score each run 1–5 on: **timing** (within ±5% of target), **clarity of the one point per slide**, **transitions**, **pace and pauses**, **filler words**, **eye contact / camera**, **energy**. Define what 3 and 5 mean for each before the first run.

### Step 3 — Run 1: talk-through
Speak the whole talk from notes, stopping as needed. Goal: find where notes fail. Output: note revisions only.

### Step 4 — Run 2: timed, no stopping
Record section times against checkpoints. Output: cuts or expansions per section, and a revised checkpoint table.

### Step 5 — Run 3: recorded self-review
Record audio or video. The presenter reports scores and observations (or supplies a transcript to count fillers and measure pace). Output: the three highest-impact fixes, not a list of everything.

### Step 6 — Run 4: with an audience
One or two listeners, ideally near the real audience. They report the one point they remember from each section. Mismatches with the intended point are the final fix list.

### Step 7 — Stop rule and day-of card
Stop when two consecutive runs land within timing tolerance and score 4+ on clarity and transitions; further runs risk sounding memorised. Produce a day-of card: opening line, three checkpoints, closing line.

---

## Output Format

```
# Speaker notes — [talk], [N] min

## Notes
### Slide [n]: [title]   ends at [mm:ss]
Purpose: ...
Key phrases: ... / ... / ...
Transition: "..."
Direction: [pause / click / demo]

## Delivery rubric
| Dimension | 3 means | 5 means |

## Rehearsal log
| Run | Type | Duration | Scores (T/C/Tr/P/F/E/En) | Top fixes |

## Stop rule status
## Day-of card
Opening line · Checkpoints (3) · Closing line
```

---

## Verification

- [ ] Notes are fragments, ≤ ~40 words per slide, with full wording only for opening, statistics, and close.
- [ ] Every slide has a transition and a cumulative timing checkpoint.
- [ ] Rubric anchors for 3 and 5 defined before Run 1.
- [ ] Feedback after each run is based only on reported timings, transcript, or observations.
- [ ] Each run produces at most three prioritised fixes.
- [ ] Stop rule evaluated; day-of card produced.

---

## False-Positive Prevention

1. **Notes as script.** Full sentences in notes get read aloud. If a slide's note can be read as a paragraph, cut it to fragments.
2. **Invented feedback.** Do not claim the presenter "sounded rushed" without a timing, transcript, or their own report. Coach from data supplied.
3. **Fixing everything at once.** A list of twelve fixes changes nothing; three prioritised fixes change the next run.
4. **Rehearsing into memorisation.** Past the stop rule, delivery becomes recited. Stop when the criteria are met.
5. **Timing only the whole.** A talk that finishes on time but rushes the close has a section problem. Check each checkpoint.
6. **Filler-word obsession.** Occasional fillers rarely hurt a talk; unclear points do. Weight clarity above fillers.
7. **Ignoring the setting.** Notes for a lectern differ from notes for a handheld card or a video call; format for where they will be read.

---

## Example

**Talk:** the 20-minute feature-flag talk from `presentation_keynote_talk_arc.md`, 12 slides, stage with a confidence monitor. **Habit:** speeds up in the middle section.

**Slide 5 notes (ends at 10:00):**
Purpose: prove that flags multiply states.
Key phrases: "ten flags" / "1,024 versions of your app" / "you test one".
Transition: "And that's assuming you remember they exist…"
Direction: pause after 1,024; click only after the pause.

**Rehearsal log:**
| Run | Type | Duration | Scores | Top fixes |
|-----|------|----------|--------|-----------|
| 1 | Talk-through | ~24 min | — | Slides 3 and 8 notes too long; add transition 6→7 |
| 2 | Timed | 22:40 | T2 | Myth 2 runs 7:30 against 5:00; cut second war story |
| 3 | Recorded | 20:50 | T4 C3 Tr3 P2 F3 E3 En4 | Pace spikes 170 wpm in myth 2 (from transcript); add pause cues; rewrite 6→7 transition |
| 4 | Audience | 20:10 | T5 C4 Tr4 P4 F3 E4 En4 | Listener remembered "flags are debt" for myth 3 but not myth 1's point — sharpen slide 3 headline |

**Stop rule:** Runs 3 and 4 both within ±5%? Run 3 is +4%, Run 4 +1%; clarity and transitions reached 4 only in Run 4 — one more timed run after the slide 3 fix, then stop.
**Day-of card:** opening line · 07:00 end of myth 1 · 12:00 end of myth 2 · 16:00 start close · closing line.

---

## Techniques Used

- **DT-03 Iterative Refinement** — four escalating runs with fixes between them.
- **DD-06 Iteration Control** — explicit stop rule to prevent over-rehearsal.
- **QA-17 Named Scores for Multi-Dimensional Metrics** — seven named delivery dimensions with anchors.
- **CM-02 Constraint Specification** — word cap per slide and three-fix limit.
- **QA-01 Self-Verification** — feedback grounded in reported data.

---

## Related Prompts

- `domain-agentic-resources/skills/document-processing/ppt-creator/SKILL.md` — build the deck itself.
- `domain-biblical-studies/sermon-devotional/biblical_sermon_delivery_coaching.md` — the preaching-specific counterpart.
- `domain-presentations/narrative-delivery/presentation_keynote_talk_arc.md` — settle the arc before rehearsing.
