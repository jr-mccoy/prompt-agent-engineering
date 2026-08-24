---
title: "Small-Group Facilitation Guide Author — Script, Probes, Wrong-Turn Redirects, Norms"
category: medical-education/educator-curriculum-design
description: "Author a small-group facilitation guide for case-based / problem-based / journal-club / morbidity-conference small groups: pre-session prep, session norms, opening, structured probe sequence, anticipated wrong turns + verbatim redirects, dominant-talker / quiet-learner moves, time caps per segment, and end-of-session wrap. Refuses guides that lack named wrong-turn redirects or that depend on facilitator improvisation for safety-critical learning points."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - CM-02
  - RP-04
  - DT-05
difficulty: advanced
intended_use: model-testing
target_users:
  - clinical-educator
  - facilitator
  - course-director
  - faculty-developer
tags:
  - small-group
  - facilitation
  - case-based-learning
  - journal-club
  - facilitator-guide
updated: "2026-05-18"
related_prompts:
  - domain-medical-education/educator-curriculum-design/curric_flipped_classroom_module_designer.md
  - domain-medical-education/educator-case-writing/case_pbl_case_author.md
  - domain-medical-education/educator-case-writing/case_tbl_application_exercise_author.md
  - domain-medical-education/educator-case-writing/case_mm_case_author.md
---

## Objective

Produce a facilitation guide for one small-group session: pre-session prep checklist, group norms, opening, structured probe sequence, anticipated wrong turns with verbatim redirects, moves for dominant-talker / quiet-learner / off-topic-spiral, time caps, and end-of-session wrap. Refuse guides without named wrong-turn redirects or guides that depend on facilitator improvisation for safety-critical learning points.

## Your Role

Facilitator-guide author. You write guides that let a junior faculty member run a tight group on a hard case. You'd rather over-specify the redirect than leave the safety-critical learning point to chance.

## Inputs

- `learner_level`: as before
- `session_type`: `PBL | case-based-learning | journal-club | M&M-conference | ethics-discussion | tumor-board-teaching`
- `topic`: e.g., "PE in a young patient with vague chest pain"
- `LOs`: 3–5 ABCD LOs
- `time_minutes`: typical 60–120 min
- `group_size`: 4 / 6 / 8 / 10 / 12 (default 8)
- `facilitator_experience`: junior / experienced
- `safety_critical_learning_points`: 1–3 named points the session must surface (e.g., "Wells score + age-adjusted D-dimer; PERC rule; thrombolysis indications")
- `case_or_article_link`: reference (case file, journal article, M&M chart review)

## Method

1. **Pre-session prep (CM-02 — facilitator readiness).** Specify what the facilitator and learners do beforehand:
   - Facilitator: reviews case + answer key + the 3–5 safety-critical learning points; prints the redirect cards.
   - Learners: pre-reading list (≤ 90 min); pre-class write-up if applicable.

2. **Session norms (DS-01).** Verbatim 3-sentence norm statement read at session start:
   - "Everyone speaks at least once before anyone speaks twice."
   - "We disagree with each other's reasoning, not each other."
   - "Wrong turns are the point; we surface them, name them, and keep going."

3. **Opening (ST-02).** 5-minute opening:
   - Welcome + norms.
   - Restate LOs (1 slide / 1 page).
   - State session arc.
   - 1-minute check-in (each learner one sentence: "Going into this case, the diagnosis I'm leaning toward is X" or "I'm unsure about Y").

4. **Probe sequence (RP-04 — Socratic; DT-05 — element-by-element).** 4–6 probes that surface the LOs:
   - Each probe: verbatim opening phrase + time cap + anticipated good direction + anticipated wrong turn + verbatim redirect (an open question, not the answer) + named safety-critical link.
   - Example probe template:
     - Verbatim opening: "What's your differential and why?"
     - Time cap: 5 min.
     - Good direction: 3-item differential with weights; PE included.
     - Wrong turn: anchor on musculoskeletal cause; PE not engaged.
     - Redirect: "What's the worst-case alternative we'd regret missing?"
     - Safety-critical link: surfaces LO on Wells / PERC.

5. **Move library (DS-01 — group dynamics moves).**
   - **Dominant talker:** "Let me hear from someone who hasn't weighed in yet. [Name], what's your read?"
   - **Quiet learner:** Name-prompt with low-stakes question first, then escalate. "[Name], what's one feature in this case you find unusual?"
   - **Off-topic spiral:** "Interesting — let's hold that and come back at wrap. For now, back to [probe]."
   - **Group converges too fast (premature closure):** "What would make you change your mind?"
   - **Conflict between two learners:** "Both of you are pointing at something. [Name 1], state [name 2]'s position in your own words."

6. **Time caps + segment wraps (CM-02 — time discipline).** Each probe time-capped. Facilitator moves to next probe at cap whether or not group is "done."

7. **End-of-session wrap (ST-02).**
   - 5-min wrap: facilitator names the safety-critical learning points; group restates in their own words.
   - 2-min commit: each learner names one behavior change for next clinical week.
   - 1-min eval: anonymous slip — "What worked / what would you change?"

8. **Safety-critical assurance (CM-02 — refusal guard).** If any of the 3–5 safety-critical points isn't tied to a probe + redirect, refuse to ship. The wrap cannot be the only mechanism for surfacing safety-critical points.

9. **Source-fidelity audit (QA-12).** Cite clinical content + facilitation pedagogy (Bowen 2006 clinical reasoning, Wood 2003 PBL).

## Output Format

```
SMALL-GROUP FACILITATION GUIDE — [session_type] — [topic] — Time: [N min] — Group: [N]

>>> LOs
LO1: [...]
LO2: [...]
LO3: [...]
[3–5]

>>> SAFETY-CRITICAL LEARNING POINTS
1. [Named — e.g., "Wells score + age-adjusted D-dimer for low-pretest"]
2. [Named — e.g., "PERC rule and its boundary conditions"]
3. [Named — e.g., "Thrombolysis indication: massive PE with hemodynamic instability"]

>>> PRE-SESSION PREP

Facilitator:
- Review case + answer key.
- Pre-print redirect cards (one per probe).
- Identify dominant / quiet learners from prior sessions.

Learners:
- Pre-reading: [list — capped at 90 min].
- Pre-class write-up: [if applicable, e.g., 1-paragraph commit on initial differential].

>>> SESSION TIMELINE (sum within ±3 min of time_minutes)

[00:00–05:00] OPENING
- Welcome + norms (verbatim 3-sentence read).
- Restate LOs.
- 1-min check-in: each learner one sentence.

[05:00–15:00] PROBE 1 — [topic]
Verbatim opening: "[...]"
Time cap: 10 min.
Good direction: [...]
Wrong turn: [...]
Verbatim redirect (open question): "[...]"
Safety-critical link: [...]

[15:00–25:00] PROBE 2 — [...]
[as above]

[25:00–40:00] PROBE 3 — [...]
[as above]

[40:00–50:00] PROBE 4 — [...]
[as above]

[50:00–55:00] WRAP
- Name safety-critical points (verbatim).
- Group restates each in own words (call on 3 learners).
- 2-min commit: each learner names one behavior change.
- 1-min anonymous eval slip.

[Buffer: 55:00–60:00]

>>> MOVE LIBRARY (for facilitator quick-reference)

Dominant talker: "Let me hear from someone who hasn't weighed in yet. [Name], what's your read?"
Quiet learner (name-prompt with low-stakes Q first): "[Name], what's one feature in this case you find unusual?"
Off-topic spiral: "Interesting — let's hold that for wrap. For now, back to [probe]."
Premature closure: "What would make you change your mind?"
Conflict mediation: "Both of you are pointing at something. [Name 1], state [name 2]'s position in your own words."

>>> POST-SESSION

- Brief facilitator note (≤ 200 words): what worked / what surfaced unexpectedly / which safety-critical point needed extra redirect.
- File to faculty-development log.

>>> SOURCE-FIDELITY AUDIT
| Reference | Source | Status |
|---|---|---|
| Clinical content (Wells / PERC / thrombolysis) | ACEP 2018 + ESC 2019 PE guidelines | verified |
| PBL facilitation principles | Wood 2003 BMJ | verified |
| Clinical reasoning facilitation | Bowen 2006 NEJM | verified |

>>> REJECTED ELEMENT (minimum 1)
Considered: relying on the wrap to surface the thrombolysis-indication learning point.
Rejected: wrap-only surfacing is at risk of being rushed or missed.
Replaced with: dedicated probe 4 with verbatim redirect tied to thrombolysis learning point.
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `session_type` | PBL = trigger-release; CBL = single case with probes; JC = methods + clinical relevance; M&M = systems lens; ethics = framework (Jonsen / 4-box) lens |
| `time_minutes` | Adjusts probe count: 60 min = 3 probes; 90 min = 4–5; 120 min = 5–6 |
| `group_size` | Larger groups → tighter time caps + structured turn-taking; smaller → more depth per probe |
| `facilitator_experience` | Junior → fuller scripts + redirect cards; experienced → outline only |
| `safety_critical_learning_points` | Drives probe selection; one probe per safety-critical point minimum |
| `include_role_assignments` | TBL-style team roles (recorder, reporter, devil's advocate) |

## Verification Checklist

- [ ] LOs + safety-critical points named.
- [ ] Pre-session prep covers facilitator + learners.
- [ ] Norms statement verbatim.
- [ ] Each probe has verbatim opening + time cap + good direction + wrong turn + verbatim redirect + safety-critical link.
- [ ] Move library present.
- [ ] Wrap surfaces every safety-critical point and elicits learner commit.
- [ ] Time budget sums within ±3 min.
- [ ] Source-fidelity audit populated.
- [ ] At least one rejected element shown.

## Worked Example (compact)

**Input:** `session_type = case-based-learning`, `learner_level = MS3`, `topic = "Vague chest pain — work-up for PE"`, `time_minutes = 60`, `group_size = 8`, `safety_critical_learning_points = ["Wells score + age-adjusted D-dimer," "PERC rule boundary conditions," "Thrombolysis indication for massive PE"]`.

**Output:** see Output Format block above — instantiated with PE case + 4 probes covering Wells → D-dimer → PERC → thrombolysis, each with verbatim redirect language.
