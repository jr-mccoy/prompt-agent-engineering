---
title: PACU Skill Drill Designer (5-Minute Rapid-Fire Bedside Drill)
category: pacu/simulation
task_type: SIMULATE
audience: PACU preceptor running a short bedside or huddle-area skill drill with an orientee
updated: "2026-04-16"
tags:
  - pacu
  - simulation
  - skill-drill
  - rapid-fire
  - huddle
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: intermediate
related_prompts:
  - prompts/pacu_simulation_scenario_builder.md
  - prompts/pacu_simulation_debrief_facilitator.md
  - prompts/pacu_emergency_drill_designer.md
  - prompts/pacu_red_flag_card.md
  - prompts/pacu_complication_deep_dive.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Drain's PeriAnesthesia Nursing Practice (7th ed.)
  - Rapid-cycle deliberate practice (RCDP) literature — brief repetitive drill framework
---

# PACU Skill Drill Designer

> Safety reminder: Bedside teaching aid — drill is between a preceptor and orientee on a real or simulated patient space, not on a real active patient. If the preceptor's real patient needs attention, the drill stops immediately. All doses, thresholds, and escalation specifics illustrative; facility protocol governs real events.

## Objective

Produce a **5-minute rapid-fire bedside skill drill** designed to be run between admissions or at shift-start huddle — one cue, a stopwatch, an expected sequence of actions, and a list of common misses. Output is a drill card the preceptor runs verbatim, plus a micro-debrief script for the 2-minute conversation after.

## When to use

- Between admissions / during low-activity windows in PACU.
- Start-of-shift huddle warm-up on a high-frequency skill (trend recognition, SBAR, emergence assessment).
- Repeat practice during remediation, between full sims.
- Targeted reinforcement after a near-miss or a debrief-identified gap.

## When not to use

- For a full scenario run — use `pacu_simulation_scenario_builder.md`.
- For a crisis / emergency team drill — use `pacu_emergency_drill_designer.md`.
- For a paper case — use `pacu_unfolding_case_study.md`.
- For a knowledge check — use `pacu_quick_quiz_generator.md`.

## Inputs

- **Skill focus (one only):** {{e.g., "SpO₂ drop to mid-80s after extubation — first 90 seconds," "post-spinal BP trend recognition," "SBAR call to CRNA for residual blockade," "PONV second-wave escalation"}}
- **Orientation phase:** {{Week 0–2, Week 2–6, Week 6–10}}
- **Runtime:** fixed at 5 minutes drill + 2 minutes micro-debrief.
- **Format:** {{verbal / tabletop | mock bedside with mannequin or empty bay}}
- **Stopwatch access:** required.

## Audience / Scope

- **Primary:** Preceptor running the drill.
- **Learner:** Orientee during a quiet moment on shift or in a sim space.
- **Scope:** One skill, one rep (or 2–3 reps of the same skill for rapid-cycle deliberate practice).

## Output requirements

```markdown
# {Skill focus} — 5-Minute Bedside Drill

> Safety reminder: Drill only. Stop immediately if your real patient needs attention. Escalation specifics illustrative; facility protocol governs real events.

## Skill Focus
{One specific observable behavior}

## Total Runtime
5 min drill + 2 min micro-debrief = 7 min.

## Setup (30 sec)
- Find a quiet space or empty bay.
- Preceptor states: "This is a 5-minute drill. Stopwatch starts when I say the cue. Stop anytime if a real patient needs you."
- Learner confirms readiness.

## The Cue (T+0, verbatim)
"{Cue delivered in one sentence — e.g., 'Your patient in bay 3, post-op general, just dropped SpO₂ to 86% from 97%. Go.'}"

Preceptor starts stopwatch.

## Expected Sequence of Actions (next ~90 sec)

| Time | Expected learner action | Verbalization expected | Common miss |
|---|---|---|---|
| 0–15 sec | Move toward bay / patient; visual assessment | "Airway open, work of breathing, color" | Starts talking before moving |
| 15–30 sec | Initial intervention (reposition, jaw thrust if indicated per scope, O2 increase per order) | "Repositioning, increasing O2 per order" | Waits for preceptor cue before moving |
| 30–45 sec | Bedside problem-solving | "Checking for airway obstruction, snoring, secretions" | Fixates on monitor without hands-on |
| 45–60 sec | Escalation decision | "Calling anesthesia by role — SBAR ready" | Delays call; tries more interventions first |
| 60–75 sec | SBAR verbalization | "S: bay 3, post-op general, SpO₂ dropped 97 → 86 in ~1 min; B: recent extubation, rocuronium, reversed; A: repositioned, O2 increased, still 88; R: bedside eval" | SBAR jumps to A/R without complete S/B |
| 75–90 sec | Continue intervention + anticipate | "Watching for further drop; prepared BVM; anticipating residual blockade differential" | Stops thinking after call; waits passively |

Preceptor stops stopwatch at 90 sec OR when learner verbalizes the full SBAR, whichever first.

## Micro-Debrief (2 min — preceptor runs)

Opening stem:
- "What did you see first? What did you do first?"

Three probes:
1. "At what second did you decide to call anesthesia? What tipped you?"
2. "Walk me through your SBAR R — what was the ask?"
3. "What would you do differently in the first 15 seconds next rep?"

Close:
- "One sentence — what's your takeaway?"

## Optional: Rapid-Cycle Deliberate Practice (RCDP)
If time permits, run 2–3 repetitions of the same cue with brief micro-corrections between:
- Rep 1: Run as above.
- Correction: One-sentence feedback from preceptor tied to the gap observed.
- Rep 2: Re-run with the correction in place.
- (If time) Rep 3: Re-run again.

Stop RCDP if the real patient needs attention OR if the learner is reaching a plateau.

## Common Misses (orientee patterns, preceptor-facing)
- **Talks before moving.** Learner verbalizes differential before laying eyes on patient. Redirect: "Hands and eyes first, voice second."
- **Fixates on monitor.** Learner stares at the SpO₂ number. Redirect: "Your patient is the primary display, not the monitor."
- **Delays escalation to try more interventions.** Learner wants to "fix it first." Redirect: "Escalation is not a last resort; it's parallel to your intervention."
- **Incomplete SBAR.** Learner jumps to R without a clear S and B. Redirect: "Who, where, what happened, what have I done, what do I need."
- **Stops thinking after call.** Learner passively waits after SBAR. Redirect: "Your anticipation continues while help is coming."

## Sources / reference
- ASPAN *Standards of Perianesthesia Nursing Practice*, {relevant sections}
- *Drain's PeriAnesthesia Nursing*, {chapter on the skill}
- RCDP literature — Hunt et al., brief repetitive practice framework.
```

## Must / Must not

**Must:**
- Target exactly **one** skill per drill.
- Total runtime = 5 min drill + 2 min micro-debrief. Do not bloat.
- Cue delivered in one sentence, verbatim.
- Expected-sequence table has time anchors and expected verbalizations per row.
- Common-miss list names the redirect verbatim.
- Drill stops immediately if the preceptor's real patient needs attention.
- Micro-debrief is 2 min and asks 3 probes max.

**Must not:**
- Fabricate doses, specific thresholds, or facility protocols. Use "per order" / qualitative cues.
- Invent ASPAN or Drain's citations.
- Include patient-identifying information (MRN, full name, full DOB, room).
- Reference age, race, sex, disability, religion, national origin, pregnancy, license pathway, or prior unit as variables unless clinically essential.
- Run a drill on a real active patient — drills happen in an empty bay, tabletop, or on a mannequin.
- Stretch the drill into a full scenario — that's a different prompt.
- Use the drill as a punishment for a prior miss; frame as repetition-practice.
- Turn the micro-debrief into a full sim debrief — if deeper reflection needed, schedule a full debrief via `pacu_simulation_debrief_facilitator.md`.

## Quality signals

- Drill runs in ≤ 5 min, micro-debrief in ≤ 2 min.
- Learner executes an observable sequence with verbalization.
- Preceptor delivers verbatim redirects when a common miss occurs.
- Learner leaves with a one-sentence takeaway.
- If RCDP is used, Rep 2 shows a measurable correction over Rep 1.

## Verification

Before running the drill, verify:

- [ ] Exactly one skill targeted.
- [ ] Cue is one sentence, verbatim.
- [ ] Expected-sequence table has time anchors (0–15 / 15–30 / 30–45 / ...).
- [ ] Common-miss list has verbatim redirects.
- [ ] Micro-debrief is 2 min, 3 probes, one-sentence close.
- [ ] Safety reminder at top.

During and after the drill:

- [ ] Drill stopped at 90 sec or on full SBAR completion.
- [ ] Real patient not compromised by drill attention.
- [ ] Learner left with one-sentence takeaway.
- [ ] If RCDP used, each rep had a specific correction tied to an observed gap.

## False-Positive Prevention

Do **not** fabricate:

- **No invented doses** in the cue or expected-action sequence. Use "per order."
- **No invented vital-sign thresholds as the single driver** — qualitative cues or ranges if not sourced.
- **No invented facility pager numbers, rapid-response codes, or escalation pathways.** "Call anesthesia by role" is enough.
- **No invented equipment brand names or supply specifics.** Generic.
- **No invented ASPAN / Drain's citations.** Mark `{{confirm}}` if unknown.
- **No personality labels in the common-miss list** ("learner was anxious"). Describe the observable behavior ("talked before moving").
- **No patient-identifying information.**
- **No protected-characteristic references.**
- **No drill that expects the learner to act outside scope** — no "intubate," no "push unordered vasopressor."

## Worked Example

<details>
<summary>Example: Skill = SBAR call for residual blockade, Week 6 orientee, RCDP 2 reps (click to expand)</summary>

```markdown
# SBAR Call for Residual Blockade — 5-Minute Drill

## The Cue (T+0, verbatim)
"Your patient in bay 2 is post-op general, extubated in OR 20 min ago. You just checked a sustained head-lift and it was less than 5 seconds. What do you do? Go."

Preceptor starts stopwatch.

## Expected Sequence

| Time | Expected action | Expected verbalization | Common miss |
|---|---|---|---|
| 0–15 sec | Move to patient; recheck head-lift; check tidal-volume pattern, mentation | "Rechecking — head-lift still <5 sec; shallow breathing; alert but can't sustain swallow" | Doesn't physically recheck |
| 15–30 sec | Reposition; coach deep breath; notify CRNA by role | "Calling CRNA" | Waits for monitor alarm |
| 30–60 sec | SBAR delivery | "S: bay 2, post-op general, residual blockade suspected; B: rocuronium, reversed at OR exit; A: sustained head-lift <5 sec, shallow breathing, alert, drooling; R: evaluate for additional reversal per order" | Jumps to R; skips head-lift finding in A |
| 60–90 sec | Anticipation while help is coming | "Prepared BVM, suction ready, monitoring RR + SpO₂, reassess head-lift in 1 min" | Stops thinking after call |

## Micro-Debrief Probes
1. "When did you decide this was residual blockade vs. over-sedation?"
2. "Your R — was the ask specific enough for the CRNA to act on without follow-up questions?"
3. "What would you do in the first 15 seconds next rep?"

## Rep 2 (after 30-sec correction)
Correction: "Good SBAR. One fix: in A, name head-lift time AND tidal-volume observation first — those are the cheap, early signs."

Rep 2 cue: "Same patient, same finding. Go."

Expected shift: SBAR A-section now leads with head-lift + tidal-volume observation before general description.
```

Notes: one skill, one cue, stopwatch, observable sequence, common misses named; correction between reps is specific and observable; no doses written (additional reversal "per order").
</details>

## Self-check

- [ ] One skill, 5-min drill + 2-min debrief.
- [ ] Verbatim cue.
- [ ] Time-anchored expected sequence.
- [ ] Verbatim redirects for common misses.
- [ ] No invented doses, thresholds, facility specifics.
- [ ] No patient-identifying information.
- [ ] No protected-characteristic references.
- [ ] Drill stops if real patient needs attention.
- [ ] Safety reminder at top.
- [ ] Verification section passed.
- [ ] False-Positive Prevention section passed.
