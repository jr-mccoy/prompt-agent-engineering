---
title: "Design a Personal Decision Journal That Calibrates Your Own Judgment"
category: personal-development/thinking
description: "Build a lightweight decision-journal format the user will actually keep — capturing the decision, the predicted outcome, and a confidence number — and a review cadence that later scores those predictions so the user learns where their judgment is reliable and where it isn't."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - DS-01
  - QA-12
difficulty: intermediate
tags:
  - decision-journal
  - calibration
  - judgment
  - confidence
  - self-knowledge
updated: "2026-07-23"
related_prompts:
  - domain-personal-development/prompts/thinking/thinking_regret_minimization.md
  - domain-personal-development/prompts/thinking/thinking_blind_spot_mirror_see_what_im_missing.md
  - domain-reasoning-craft/forecasting/forecasting_calibration_self_audit.md
  - domain-reasoning-craft/forecasting/forecasting_brier_tracker_design.md
  - domain-decision-making/documentation/decisiondoc_log_entry.md
---

# Design a Personal Decision Journal That Calibrates Your Own Judgment

**Objective:** Produce a decision-journal format tailored to the user's actual decision flow, plus a review ritual that scores past predictions against outcomes — so over time the user learns which kinds of calls they get right and which they systematically miss.

**When to use:** The user makes recurring consequential decisions (hires, bets, launches, purchases, relationship calls) and wants to know whether their gut is actually reliable; they've noticed they remember being right more than they were; or they're starting a role/project where judgment is the job. Not for one-off trivial choices, and not a replacement for a rigorous forecasting practice — for that, route to `domain-reasoning-craft/forecasting/`.

**Audience:** An individual building this for their own decisions. Not a tool for grading someone else's judgment, and not clinical. If reviewing past decisions triggers persistent rumination or self-punishment, that is a signal to stop and seek support — see `domain-psychology/` and a licensed professional.

---

## Inputs Required

1. **Decision types.** The 2–4 recurring kinds of decision the user actually faces (e.g., "which candidate to hire," "whether to take a client," "when to ship"). Not abstract categories — the concrete calls they repeat.
2. **Frequency.** Roughly how often each type comes up (daily, weekly, monthly, a few times a year). This sets the review cadence.
3. **Current capture habit.** What, if anything, the user records today (nothing, a notes app, a spreadsheet, memory). Required so the format fits their existing friction budget.
4. **Time budget per entry.** How many minutes the user will realistically spend logging a decision. If they say more than 5, push back — journals die from being too heavy.
5. **One real recent decision.** A specific decision the user made in the last month, with what they chose and what they expected to happen. Used to draft a worked example.

If the user cannot name at least 2 recurring decision types, refuse and ask for them. A journal of one-off decisions produces no calibration signal because nothing repeats to compare.

---

## Instructions

### Step 1 — Fix the minimal entry schema

Design the entry around exactly these five fields and no more. Extra fields are the main reason decision journals get abandoned.

| Field | What it captures | Rule |
|---|---|---|
| Decision | One line: what was decided, and the date | Present tense, written *before* the outcome is known |
| Options considered | The alternatives actually on the table | At least 2, or note "no real alternative" |
| Prediction | The specific outcome the user expects | Must be observable and dated — a thing that will visibly be true or false |
| Confidence | A number, 50–99% | Never 100; 50% means a coin flip |
| Reason (one line) | The core "because" | One sentence, so the review can see the actual logic |

The prediction must be falsifiable and time-stamped ("by end of Q3, this hire is still here and rated meets-or-above"), never vague ("this will probably work out").

### Step 2 — Match the format to friction

Using inputs 3 and 4, pick the lightest medium the user will actually use: a phone note template, a five-column spreadsheet, a physical index card, or a repeatable text snippet. If their time budget is under 3 minutes, cut "Options considered" to optional. Fit the tool to the habit, not the reverse.

### Step 3 — Draft the worked example

Convert input 5 (their real recent decision) into a filled-in entry using the schema. This proves the format works on a real case and gives the user a copy-paste template. Make them write the confidence number even though the outcome is partly known — note where hindsight is contaminating it.

### Step 4 — Set the review cadence and scoring rule

Set a review interval from input 2: predictions can only be scored once their outcome date has passed. Define a single scoring rule the user runs each review:

- Mark each due prediction **Right / Wrong / Unresolvable**.
- Group by confidence band (50–60%, 70–80%, 90–99%).
- Compare hit-rate to stated confidence: if the 90% calls come true 60% of the time, the user is overconfident in that decision type.

This is the calibration payload. Point to `forecasting_calibration_self_audit.md` and `forecasting_brier_tracker_design.md` for the rigorous scoring math if the user wants to go deeper than hit-rate-by-band.

### Step 5 — Name the one trap this user will hit

From inputs 3 and 5, predict the single most likely failure mode for *this* user (skipping the confidence number, only logging decisions they feel good about, never doing reviews, rewriting predictions after the fact) and specify one concrete guard against it.

### Step 6 — Produce one setup action

Output one action to start today: create the actual template in their chosen tool and log the one real decision from Step 3. Not "start journaling" — the specific file/note/card created, and the first entry already in it.

---

## Constraints

### Must
- Keep the entry schema to five fields; every field earns its place against the time budget.
- Require a numeric confidence (50–99%) and a falsifiable, dated prediction on every entry.
- Tie review cadence to the decision frequency, and score only predictions whose outcome date has passed.
- Deliver a filled worked example from the user's real decision (input 5).
- Name one user-specific abandonment trap with a concrete guard.

### Must Not
- Add mood logs, gratitude fields, or open-ended reflection prompts — this is a calibration instrument, not a diary.
- Allow 100% confidence, or predictions that can't be scored.
- Recommend an elaborate app, tagging system, or multi-page template.
- Moralize about past decisions or frame the review as self-improvement homework.
- Clone the rigorous forecasting machinery — reference `domain-reasoning-craft/forecasting/` instead.

---

## False-Positive Prevention

1. **Don't let hindsight write the prediction.** A prediction only counts if it was recorded *before* the outcome was known. Retro-filled entries feel calibrating but teach nothing; flag any entry built after the fact.
2. **Don't confuse a good outcome with a good decision.** The review scores whether the *prediction* was accurate at the stated confidence, not whether life turned out well. A right call that got unlucky is still a right call.
3. **Don't over-collect.** More fields is not more insight. If the format takes longer than the time budget, it will be abandoned and produce zero calibration data — worse than a lighter journal.
4. **Don't score unresolvable predictions as wins.** Vague predictions that can't be marked Right/Wrong are the failure of the format, not a neutral result; rewrite them as observable.
5. **Don't treat one review as calibration.** Calibration needs a run of scored predictions in a confidence band. A single decision reviewed proves nothing about the user's judgment.
6. **Don't pathologize a low hit-rate.** Discovering overconfidence is the point, not a defect. The output observes the gap; it does not lecture about it.

---

## Output Format

```
## Your decision journal — entry schema
| Field | Rule for this user |
|---|---|
| Decision | ... |
| Options considered | ... (optional if <3 min budget) |
| Prediction | observable + dated |
| Confidence | 50–99% |
| Reason | one line |

Medium: [phone note / spreadsheet / index card / text snippet — matched to friction]
Time per entry: [X minutes]

## Worked example (your real decision)
Decision: ...
Options: ...
Prediction: ... (by [date])
Confidence: ...%
Reason: ...
[Note on any hindsight contamination in the confidence number]

## Review ritual
Cadence: [every X], scoring only predictions past their outcome date.
Each review:
1. Mark due predictions Right / Wrong / Unresolvable
2. Group by confidence band (50–60 / 70–80 / 90–99)
3. Compare hit-rate to stated confidence → note over/under-confidence by decision type
[For rigorous scoring: domain-reasoning-craft/forecasting/forecasting_calibration_self_audit.md]

## Your most likely abandonment trap
[Named trap] → guard: [one concrete countermeasure]

## Setup action (today)
[Create the template in the chosen tool + log the Step 3 entry now.]

Predicted check: at the first review date, you have ≥ [N] scored entries and one confidence band you can read.
```

---

## Verification

- [ ] Entry schema is five fields, matched to the user's stated time budget.
- [ ] Every entry requires a numeric confidence (never 100%) and a falsifiable, dated prediction.
- [ ] Review cadence is tied to decision frequency and scores only past-due predictions.
- [ ] A worked example was produced from the user's real recent decision (input 5).
- [ ] One user-specific abandonment trap is named with a concrete guard.
- [ ] Rigorous calibration math is cross-linked, not rebuilt.
- [ ] Output ends in one setup action with an observable check, no diary fields, no moralizing.
