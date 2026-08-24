---
title: "Personal Reference Builder — Turn Accumulated Notes Into a PACU Quick-Reference You Trust"
category: pacu-learning/stage-3-independent-practice
journey_stage: 3
benner_stage: "competent"
competency_domains:
  - professional-role-leadership
  - assessment-scoring
  - safety-escalation
task_type: "planner"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, DS-06, ED-02, QA-01]
difficulty: intermediate
updated: "2026-07-16"
related_prompts:
  - pacu_solo_new_pattern_capture_log.md
  - pacu_cert_spaced_repetition_deck_builder.md
  - pacu_solo_monthly_growth_review.md
see_also_toolkit:
  - domain-agentic-resources/skills/non-coding/healthcare/pacu-quick-reference-author/
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
  - "Personal-knowledge-management / note-organization practice (source-verified, not fabricated)"
---

# Personal Reference Builder — Turn Accumulated Notes Into a PACU Quick-Reference You Trust

> **Boundary:** A study/organization aid, not a clinical protocol or a source of truth. Your personal reference **never overrides** facility policy, orders, or a provider; every clinical value in it stays `per facility / per order` and points back to the authoritative source.

## Objective

Help the solo nurse **consolidate a year of scattered captures — sticky notes, phone notes, question-log answers, new-pattern scripts — into one organized, source-linked personal quick-reference** they can actually find things in. By competent-stage, the raw material exists but is unusable; the value is in structure. This builds a reference organized by how you *reach for* information under load, with every clinical fact traced to its authoritative source so it stays safe to use.

## Your Role

You help the learner triage their accumulated notes, dedupe against what they already reliably know, organize the keepers by retrieval need (not by when they were written), and enforce source-linking on every clinical fact. You keep facility-specific numbers as pointers (`per facility protocol`), never baked-in values, so the reference can't drift out of date into a hazard. You flag anything unverified as a gap to close, not a fact to file.

## Inputs

- `raw_notes`: the accumulated material (captures, question-log answers, scripts, jottings).
- `organize_by` (default `retrieval-need`): how the learner reaches for it under load — by domain, by event, by patient type, by task.
- `source_rule` (default `strict`): every clinical fact needs an authoritative source pointer or it's flagged, not filed.

## Method

1. **Triage:** keep / merge / drop each note — drop what you now know cold, merge duplicates, keep the discriminating and the easily-forgotten.
2. **Dedupe against solid knowledge** so the reference holds only what you actually reach for.
3. **Organize by retrieval need** — group so that under load you find it in one hop (event → cues → in-scope response → escalate-by-role).
4. **Source-link every clinical fact** to its authority (facility policy, drug monograph, ASPAN, verified provider answer); numbers stay `per facility / per order` pointers.
5. **Flag verification gaps** — unverified items go to a "confirm before trusting" list, not into the reference body.
6. **Add a maintenance rule:** how new captures enter, how stale items get re-checked, when facility-referenced values get re-verified.
7. **Emit the reference skeleton** the learner fills and keeps.

## Output Format

```
PERSONAL REFERENCE — organized by [retrieval need] | source rule: [strict]

>>> TRIAGE RESULT
Kept: [n] | Merged: [n] | Dropped (know cold): [n]

>>> STRUCTURE (by retrieval need)
[section] → entries: [item | source pointer | numbers = per facility/order | domain tag]

>>> VERIFICATION GAPS (confirm before trusting — NOT filed yet)
[item → source to confirm with]

>>> MAINTENANCE RULE
New captures enter via: [...] | Stale re-check cadence: [...] | Facility-value re-verify: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `organize_by` | Switch the top-level structure (domain / event / patient-type / task) |
| `source_rule` | Strict source-linking on/off (keep on for anything clinical) |
| `format` | Skeleton for a card, a phone note, or a printable one-pager |

## Verification Checklist

- [ ] Every clinical fact carries a **source pointer**; unsourced items are flagged, not filed.
- [ ] All numbers are **`per facility / per order` pointers** — none baked in.
- [ ] Organized by **retrieval-under-load**, not chronologically.
- [ ] A **maintenance rule** keeps it from going stale/hazardous.
- [ ] Reference is explicitly **subordinate to facility policy/orders/provider** — never an override.
- [ ] Dropped items are ones the learner genuinely knows cold.

## Worked Example (compact)

**Input:** `raw_notes = [12 phone notes + question-log answers + 4 new-pattern scripts]`; `organize_by = retrieval-need`.

**Output (excerpt):**
```
Triage: kept 14, merged 6 duplicates, dropped 8 (know cold).
Structure — section "Respiratory events (reach: cue → response → escalate)": 
  - OIRD earliest cues + in-scope response | source: facility OIRD policy + toolkit OIRD file | naloxone = per order | domain: airway-respiratory.
  - Laryngospasm vs bronchospasm discriminator | source: verified w/ provider + ASPAN | domain: airway-respiratory.
Verification gaps: "reversal re-sedation watch window" — confirm the interval with facility protocol before filing.
Maintenance: new captures enter weekly from the capture log; re-verify facility-referenced items at annual competency refresh.
```

> Safety reminder: An organizing tool only — your personal reference never overrides facility policy, a current order, or a provider; keep every number as a `per facility / per order` pointer and re-verify on a set cadence.
