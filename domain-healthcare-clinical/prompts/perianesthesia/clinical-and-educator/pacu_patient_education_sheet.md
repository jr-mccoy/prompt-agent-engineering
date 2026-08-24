---
title: Post-Op Patient Education Sheet
category: pacu/patient-education
task_type: COMMUNICATE
audience: Post-op patient and family (adjustable literacy level)
updated: "2026-04-16"
tags:
  - pacu
  - patient-education
  - discharge
techniques:
  - ST-01
  - ST-03
  - RT-02
  - ED-02
  - DS-06
difficulty: beginner
related_prompts:
  - prompts/pacu_topic_primer.md
  - prompts/pacu_handoff_script.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.) — discharge teaching
  - ASPAN Standards of Perianesthesia Nursing Practice — patient education
  - AHRQ plain-language and health literacy guidance
---

# Post-Op Patient Education Sheet

> Safety reminder: Education supplement only — does not replace provider discharge instructions.

## Objective

Produce a **plain-language patient education sheet** for a specific surgery / procedure, adjustable to reading level. Covers: what to expect, activity, pain, diet, incision care, warning signs, and when to call.

## Inputs

- **Surgery / procedure:** {{…}}
- **Reading level target:** {{6th grade / 8th grade / plain language adult}}
- **Language / translation notes:** {{English; flag if other languages needed}}
- **Caregiver present?** {{yes / no}}
- **Source chapter or discharge protocol:** {{…}}

## Audience

- Patient and family reading after discharge from Phase 2 PACU.
- May be under residual sedation when they first read it; caregiver is often the primary reader.

## Output requirements

```markdown
# Going Home After {Surgery name}

> Safety reminder: These are general recovery tips. Follow the instructions your surgeon and nurse gave you. If anything differs, your team's instructions win.

## What to expect in the first 24 hours
- ...
- ...
- ...

## Pain
- How much pain is normal: ...
- How to take your pain medicine: follow the label and provider order; do not add medicines on your own.
- Things besides medicine that help: ice (if allowed), position changes, slow walking (if allowed).
- Call your surgeon if: pain gets worse after getting better; pain is not controlled by the medicine you were given.

## Moving around
- Today: ...
- Tomorrow: ...
- When to stop activity: ...

## Eating and drinking
- Start with: clear liquids, then light foods as tolerated.
- Call your surgeon if: you cannot keep liquids down for more than {per discharge order} hours.

## Your incision / dressing
- Keep it: ...
- When to change the dressing: follow the discharge instructions.
- Do NOT: ...

## Warning signs — call your surgeon
- Fever above {per discharge order}.
- Bleeding that soaks through a dressing.
- New or worsening pain.
- Redness, warmth, or pus around the incision.
- Trouble breathing.
- {surgery-specific warning}
- {surgery-specific warning}

## Warning signs — call 911
- Chest pain.
- Severe trouble breathing.
- Sudden confusion or you can't wake the person up.
- Uncontrolled bleeding.

## When to call your surgeon's office vs. the emergency department
- Office hours: {per provider instruction}.
- After hours: {per provider instruction}.

## Your follow-up appointment
- Date/time: {per provider instruction}.
- What to bring: ...

## Questions you might want to ask
- ...
- ...
```

## Must / Must not

**Must:**
- Reading level ≤ target (use short sentences, common words).
- Warning-sign section split into *call your surgeon* and *call 911*.
- Encourage patient to defer to their provider's instructions whenever in doubt.
- "Things you can do without medicine" section for pain.

**Must not:**
- No specific drug doses or timing beyond "follow the label and order".
- No temperature thresholds, fluid minimums, or drainage amounts unless cited from a facility discharge protocol.
- No medical jargon without plain-language definition.

## Quality signals

- A caregiver can read and act on it without googling terms.
- Warning signs are observable without equipment.
- Distinction between office call and 911 is unambiguous.

## Verification

Before returning, verify:

- [ ] Reading level is at or below target (short sentences, common words, no medical jargon without plain-language definition).
- [ ] Warning signs are split into two clearly labeled lists: "call your surgeon" and "call 911."
- [ ] Every warning sign is observable without equipment (no "BP > 160," no "temp > 101.4"; use "new bleeding that soaks through," "hard time breathing").
- [ ] Every reference to "your provider's instructions" is phrased so their instructions override anything on the sheet.
- [ ] At least two non-medication pain strategies listed.
- [ ] Follow-up block does not invent a calendar time, phone number, or address.

## False-Positive Prevention

Do **not** fabricate:

- **No invented medication doses, timings, or schedules.** Always say "follow the label and provider order."
- **No invented temperature thresholds, fluid minimums, urine output minimums, or wound drainage amounts** unless cited from a specific facility discharge protocol the user supplied.
- **No invented phone numbers, office hours, after-hours pathways, or clinic addresses.** Use `{per provider instruction}` placeholders.
- **No invented red-flag statistics** ("this happens in 3% of patients"). Use qualitative language.
- **No invented timelines** ("you will feel better in 3 days"). Use "most people feel better gradually; call if you are worse instead of better."
- **No medical advice beyond the sheet's scope.** Always defer to provider.
- **No prescription-strength lifting, activity, or driving limits** unless user supplied them from the order set.

## Worked Example

<details>
<summary>Example: Surgery = outpatient tonsillectomy, adult, 6th-grade reading level (click to expand, abbreviated)</summary>

```markdown
# Going Home After Your Tonsillectomy

> Safety reminder: These are general recovery tips. Follow the instructions your surgeon and nurse gave you. If anything differs, your team's instructions win.

## What to expect in the first 24 hours
- Your throat will be sore. This is normal.
- Your voice may sound different.
- You may have bad breath for a few days.
- You may feel tired — rest is part of healing.

## Pain
- How much pain is normal: sore throat, ear pain (the nerves are connected), worst around days 3–5.
- How to take your pain medicine: follow the label and provider order; do not add medicines on your own.
- Things besides medicine that help: cold drinks, popsicles, a cool-mist humidifier, small sips often, rest.
- Call your surgeon if: pain gets worse after getting better; pain is not controlled by the medicine you were given.

## Moving around
- Today: rest. Short walks around the house are fine.
- Tomorrow: gentle activity. No strenuous exercise.
- When to stop activity: if you feel dizzy, short of breath, or start bleeding.

## Eating and drinking
- Start with: cold, soft foods and clear liquids.
- Avoid: hot, sharp, or crunchy foods for the first week.
- Call your surgeon if: you cannot keep liquids down for more than {per discharge order} hours.

## Your incision / dressing
- There is no outside dressing.
- Do NOT gargle vigorously or spit forcefully.

## Warning signs — call your surgeon
- Any bright red blood in your spit or vomit.
- Fever {per discharge order}.
- Pain getting much worse instead of slowly better.
- Cannot keep fluids down.
- Dark-colored urine or you are peeing very little.

## Warning signs — call 911
- Heavy bleeding from your mouth that will not stop.
- Severe trouble breathing.
- Chest pain.
- Sudden confusion or you can't wake the person up.

## When to call your surgeon's office vs. the emergency department
- Office hours: {per provider instruction}.
- After hours: {per provider instruction}.
- Bleeding from mouth that won't stop: 911 or ED, not the office.

## Your follow-up appointment
- Date/time: {per provider instruction}.
- What to bring: list of medicines, questions.

## Questions you might want to ask
- When can I go back to work/school?
- When can I exercise?
- When can I travel?
```

Notes: no specific temperature cutoff (deferred to "per discharge order"), no specific "call within 4 hours" — uses qualitative trigger; every warning sign is observable; 911 triggers clearly separated.
</details>

## Self-check

- [ ] Plain-language throughout; target reading level met.
- [ ] Warning signs split into surgeon-call vs. 911.
- [ ] No unsourced doses or thresholds.
- [ ] Non-medication pain tips included.
- [ ] Follow-up and questions sections included.
- [ ] Safety reminder at top.
- [ ] Verification section passed.
- [ ] False-Positive Prevention section passed — no invented doses, thresholds, phone numbers, or timelines.
