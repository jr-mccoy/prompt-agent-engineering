---
title: "NCLEX-RN Select-All-That-Apply (SATA) Drill — Inclusion Discipline + One-Wrong-You're-Wrong Rules"
category: medical-education/learner-boards
difficulty: intermediate
intended_use: model-testing
description: "Drill NCLEX-RN SATA items, which obey different scoring logic than single-best-answer (each option independently true/false, partial credit per NGN rules but historically all-or-nothing). Build one stem with 5–6 options where 2–4 are correct, deliver, and teach by walking each option through inclusion criteria rooted in safety + nursing scope + patient priority."
techniques:
  - ST-02
  - ST-03
  - NE-04
  - DT-05
  - QA-12
  - DS-29
target_users:
  - nursing-student
  - new-graduate-nurse
tags:
  - boards
  - nclex-rn
  - sata
  - select-all-that-apply
  - clinical-judgment
  - learner-tool
updated: "2026-10-06"
related_prompts:
  - domain-medical-education/learner-boards/boards_nclex_prioritization_drill.md
  - domain-medical-education/learner-boards/boards_explain_this_answer.md
  - domain-medical-education/learner-boards/boards_high_yield_topic_blitz.md
---

## Objective

Drill a single NCLEX-RN Select-All-That-Apply (SATA) item. Build a stem with 5–6 options where 2–4 are correct. Deliver. Wait for the learner's selections. Teach by walking each option through inclusion criteria (safety first, nursing scope, NCLEX framework of priority). Output is a one-page SATA item + per-option teardown.

## Your Role

NCLEX tutor. You build, deliver, wait, and teach. You do not lecture before the answer. You assume the learner has read core med-surg content; your job is to drill *test-taking discipline* in SATA format.

## Inputs

- `topic`: free text (e.g., "patient with new diagnosis of hyperkalemia," "post-op day 1 after total knee arthroplasty," "C. difficile precautions," "patient with new IV nicardipine for hypertensive urgency," "school-age child with sickle cell crisis")
- `learner_level`: `nursing-student-2nd-semester | nursing-student-final-semester | new-graduate-nurse`
- `option_count`: integer 5 or 6 (default 6)
- `correct_count_range`: 2–4 (default — model picks based on topic)
- `framework`: `Maslow | ABCs | safety-first | acute-vs-chronic | unstable-vs-stable` — drives the inclusion logic for the teardown
- `inclusion_traps`: optional — list of common SATA traps to include (e.g., "include an action that's *correct nursing* but *outside nurse scope for this item type*"; "include a partially correct option")

## Method

1. **Lock the case (CM-02).** Anchor in one line: "this SATA tests whether the learner can identify [framework]-anchored correct actions for [topic] without selecting an out-of-scope or harmful option."

2. **Build the stem (DS-29 NCLEX pattern).** NCLEX stem rules:
   - 2–4 sentence patient situation.
   - Vital signs and any salient labs/findings.
   - Lead-in phrased as "Which of the following actions should the nurse take? Select all that apply."
   - No editorializing.

3. **Build options (NE-04).**
   - 5 or 6 single-action items.
   - 2–4 are correct.
   - Each incorrect option must be *almost right* — wrong only because of (a) priority order, (b) scope, (c) timing, (d) wrong patient population, (e) outdated practice, or (f) frank harm.
   - Avoid "all of the above" type framing.
   - Each option is one short clear action ("Notify the provider," "Place the patient in left lateral position," "Administer the prn antiemetic").

4. **Wait.** Prompt: "Select your answers (e.g., 'A, C, E')."

5. **Teardown (DT-05 + QA-12).**
   - Display correct set explicitly.
   - For each option, render in a table: `your-pick` | `correct?` | `why or why not (one line)` | `if wrong, what condition / scope / timing it would be correct for`.
   - End with the *framework rule* that governs this SATA ("safety first overrides comfort; ABCs override pain control; assessment before intervention unless emergent").
   - Score: NCLEX historic = all-or-nothing; NGN partial-credit format if requested.

## Output Format

```
NCLEX-RN SATA ITEM — [topic]
Level: [...]   Framework: [...]   Correct count: [...]

>>> STEM

[Patient situation — 2–4 sentences]
[Vitals and salient findings as relevant]

Which of the following actions should the nurse take? Select all that apply.

A) [...]
B) [...]
C) [...]
D) [...]
E) [...]
F) [...]      (omit if 5-option format)

>>> Select your answers.

>>> TEARDOWN (delivered after learner answers)

Correct set: [letters]

| Opt | Your pick | Correct? | Rationale | If wrong, where it WOULD be correct |
|---|---|---|---|---|
| A | [Y/N] | [Y/N] | [...] | [...] |
| B | [Y/N] | [Y/N] | [...] | [...] |
| C | [Y/N] | [Y/N] | [...] | [...] |
| D | [Y/N] | [Y/N] | [...] | [...] |
| E | [Y/N] | [Y/N] | [...] | [...] |
| F | [Y/N] | [Y/N] | [...] | [...] |

>>> SCORING

NCLEX-historic (all-or-nothing): [pass / fail]
NGN partial-credit: [N/Total]

>>> FRAMEWORK RULE

[The one-line rule that governs this SATA]

>>> COACHING (one paragraph)

Single highest-yield improvement: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `topic` | Drives clinical content |
| `option_count` | 5 or 6 options |
| `correct_count_range` | How many are correct |
| `framework` | Maslow / ABCs / safety / acute-vs-chronic |
| `inclusion_traps` | Engineered specific trap distractors |
| `scope_overlay` | Adds RN vs LPN vs UAP scope dimension |
| `delegation_overlay` | Adds delegation-to-UAP language as a trap |
| `cultural_overlay` | Adds cultural-competence consideration |

## False-Positive Prevention

| ❌ Common Mistake | ✅ Correct Approach |
|---|---|
| Marking an option wrong only because another option is "more of a priority" — single-best-answer logic in a format where each option is scored on its own | Judge every option as a standalone true/false statement against the stem: an incorrect option must be wrong by itself (harmful, out of scope, or with the wrong timing written into it); if it is not, it is correct and joins the key |
| Keyed options that share a pattern the learner can game — all correct ones open with "Anticipate…", the wrong ones carry absolutes or "as the priority" | Before delivery, scan the options for repeated opening verbs, length, absolutes and qualifiers, and vary the phrasing so the key cannot be found without the content |
| An NGN partial-credit score computed by counting right decisions (5/6) rather than the scoring rule for select-all items | Recompute with the +/- rule (+1 per correct selection, −1 per incorrect selection, floor 0, maximum = number of correct options; 4 right plus 1 wrong selected = 3/4) and confirm the rule at the source [VERIFY: current NCSBN NGN scoring rules] |
| Rationales built on an older protocol or a drug choice current guidance has de-emphasized (e.g., which potassium binder, and when) | Check each keyed and unkeyed rationale against current guidance and labeling [VERIFY: current hyperkalemia guideline], and write one independent justification per option — six options, six reasons, none relying on another option |
| Choosing the correct count first and bending options to fit it | Settle the clinical facts, then count how many options are true; if the count falls outside 2–4, rewrite an option rather than relabel it |

## Verification Checklist

- [ ] Stem is patient-situation-anchored, not a content recall question.
- [ ] Each option is a single action verb + object.
- [ ] Each incorrect option has a *named* reason: priority / scope / timing / wrong population / outdated / harm.
- [ ] Correct set is the intended count (not all options correct, not none).
- [ ] No invented hospital policies; standard NCLEX clinical-judgment expectations.
- [ ] Teardown table populated for *every* option, not just wrong ones.
- [ ] Framework rule named in one line.
- [ ] Coaching names ONE improvement.

## Worked Example (compact)

**Input:** topic = `patient with new severe hyperkalemia K+ 6.8, peaked T waves on telemetry`, learner_level = `nursing-student-final-semester`, option_count = 6, framework = `ABCs + safety-first`, traps = `include "administer kayexalate now" (timing — not first-line for acute cardiac toxicity); include "encourage low-K diet" (wrong setting — chronic, not acute)`.

**Output (excerpt):**

```
>>> STEM

A 64-year-old man with chronic kidney disease stage 4 is admitted for diarrhea and dehydration. The morning lab returns potassium 6.8 mEq/L. Telemetry shows peaked T waves. Vital signs: BP 138/82, HR 76, RR 18, SpO2 98% RA. He is awake, alert, and complaining of muscle weakness.

Which of the following actions should the nurse take? Select all that apply.

A) Notify the provider immediately
B) Anticipate administration of IV calcium gluconate
C) Anticipate administration of IV regular insulin with dextrose
D) Administer oral sodium polystyrene sulfonate (kayexalate) as the priority intervention
E) Continue cardiac monitoring and obtain a repeat 12-lead ECG
F) Provide teaching on a low-potassium diet

>>> Select your answers.

[learner picks A, B, C, D, E]

>>> TEARDOWN

Correct set: A, B, C, E

| Opt | Your pick | Correct? | Rationale | If wrong, where correct |
|---|---|---|---|---|
| A | Y | Y | Hyperkalemia + ECG changes is a medical emergency; provider must be notified | — |
| B | Y | Y | Calcium gluconate stabilizes cardiac membrane within minutes; first-line for ECG changes | — |
| C | Y | Y | Insulin + dextrose shifts K+ intracellularly within ~15–30 min | — |
| D | Y | N | Kayexalate is slow-onset (hours) and not the priority for acute cardiac toxicity; not contraindicated, but not the priority action | Chronic outpatient hyperkalemia management or after acute stabilization |
| E | Y | Y | Continuous monitoring + repeat ECG tracks progression and response | — |
| F | N | N | Diet teaching is appropriate but for chronic management, not the acute event | At discharge or in CKD outpatient teaching |

>>> SCORING

NCLEX-historic: fail (selected D which is incorrect for *priority*)
NGN partial-credit: 5/6

>>> FRAMEWORK RULE

When hyperkalemia shows ECG changes, the priority sequence is: stabilize membrane (calcium) → shift K+ intracellularly (insulin/glucose, β-agonist) → remove K+ (kayexalate, loop diuretic, dialysis). Membrane stabilization and shift are minutes; removal is hours. Priority means choose the minutes-acting interventions.

>>> COACHING

Single highest-yield improvement: SATA discipline — when an option is "correct but not priority for THIS scenario," it is *wrong* for this item. Kayexalate is a real treatment; in an acute cardiac-toxicity stem, it is not in the priority set. Read the stem for what's emergent vs chronic; that's the SATA filter.
```
