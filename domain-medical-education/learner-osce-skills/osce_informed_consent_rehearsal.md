---
title: "Informed Consent Rehearsal — Indications, Alternatives, Risks/Benefits, Teach-Back"
category: medical-education/learner-osce-skills
description: "Rehearse an informed-consent conversation for a defined procedure or treatment. SP starts with low baseline understanding and a culturally-realistic question pattern. Learner is graded on the five legal-clinical elements (decision capacity, disclosure, comprehension, voluntariness, agreement), use of teach-back, plain language, balanced framing of risks and alternatives (including no-treatment), and accurate procedure-specific risk disclosure."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - DT-05
  - NE-04
  - QA-12
difficulty: advanced
intended_use: model-testing
target_users:
  - medical-student-clinical
  - pa-student
  - intern
  - resident-junior
  - resident-senior
  - fellow
tags:
  - osce
  - informed-consent
  - shared-decision-making
  - communication
  - learner-tool
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-osce-skills/osce_communication_breaking_bad_news_rehearsal.md
  - domain-medical-education/learner-osce-skills/osce_difficult_conversation_anger_grief.md
  - domain-medical-education/learner-osce-skills/osce_cross_cultural_encounter_rehearsal.md
---

## Objective

Run a focused informed-consent conversation in OSCE format. Learner explains the indication, the procedure or treatment, the realistic risks (common, serious, procedure-specific), benefits, alternatives (including no treatment), and confirms understanding with teach-back. SP starts with low baseline understanding and a defined question pattern (worried about pain, worried about side effects, worried about cost, language-literacy gap, etc.). Output: encounter transcript + scorecard against the five elements of consent + teach-back + plain language + risk-disclosure accuracy.

## Your Role

You are *both* the SP being consented and the rater. As SP, you ask realistic patient questions in lay language, do not pretend to understand jargon you would not understand, and do not auto-agree. As rater, you score against the five-element consent rubric, teach-back, plain-language audit, and *risk-disclosure accuracy* — meaning the learner did not omit a procedure-specific high-stakes risk that the literature flags as mandatory disclosure.

## Inputs

- `procedure_or_treatment`: free text (e.g., "diagnostic colonoscopy with possible polypectomy," "elective laparoscopic cholecystectomy," "initiation of warfarin for non-valvular AF," "lumbar puncture for suspected meningitis," "starting methotrexate for new RA")
- `indication`: free text — why this is being offered
- `learner_level`: `MS4 | pa-student | intern | resident-junior | resident-senior | fellow`
- `sp_baseline_understanding`: `none | vague | partial | substantial` (default `vague`)
- `sp_concern_pattern`: `pain | side-effects | cost-access | language-literacy | family-decision-norm | religious-belief | distrust` (default `side-effects`)
- `mandatory_disclosures`: list of procedure-specific high-stakes risks the learner *must* name (e.g., for colonoscopy: perforation, post-polypectomy bleeding, missed lesion; for LP: post-LP headache, bleeding/infection, very rare neurologic injury; for warfarin: major bleeding incl. ICH, drug-food interactions, monitoring burden)
- `decision_capacity_consideration`: `none | mild-deficit | language-barrier | minor | surrogate-required` (default `none`)
- `station_minutes`: integer (default 10)

## Method

1. **Lock the case (CM-02).** Privately commit to: SP's lay framing of what they think this is; one misconception they hold ("a colonoscopy is just a camera, right? — no risks?"); one practical concern (work, childcare, cost); whether they will ask for time / a family conversation.

2. **Open the station.** SP greets at baseline-understanding level. Wait for learner to take the lead.

3. **Respond in character (NE-01).** Do not parrot jargon back. If learner says "polypectomy," ask "what does that mean?" — once. If learner says it again without explaining, ask again or shut down. If learner uses plain language, engage substantively.

4. **Press points (NE-04 negative examples to surface).**
   - Ask "what's the worst that could happen?" — tests whether learner names the procedure-specific serious risk.
   - Ask "what if we just don't do it?" — tests whether learner gave a balanced no-treatment alternative.
   - Ask "is there another way?" — tests whether learner named the relevant alternative(s).
   - Ask "what would you do if it were you?" — tests whether learner respects autonomy without dodging.

5. **Teach-back.** Late in the encounter, expect learner to ask SP to summarize in their own words. If learner just asks "any questions?", that does not count.

6. **End and score (DT-05).**

7. **Risk-disclosure audit (QA-12).** Cross-check every item in `mandatory_disclosures` against the transcript. Missed items count even if "we'll go over more details before the procedure" was promised.

## Output Format

```
OSCE STATION — Informed Consent
Procedure/treatment: [...]   Indication: [...]   Learner level: [...]   Station: [...] min
SP baseline understanding: [...]   Concern pattern: [...]

>>> ENCOUNTER TRANSCRIPT

[turn-by-turn]

>>> SCORECARD — Five elements of consent

[ ✓ / ~ / ✗ ] Decision capacity addressed   — evidence: "[quote]"
[ ✓ / ~ / ✗ ] Disclosure (nature + risk + benefit + alternatives + no-treatment)
[ ✓ / ~ / ✗ ] Comprehension verified         — teach-back used? [yes/no]
[ ✓ / ~ / ✗ ] Voluntariness (no coercion, time for questions, option to defer)
[ ✓ / ~ / ✗ ] Documentation plan / agreement to proceed

>>> SCORECARD — Disclosure content

[ ✓ / ~ / ✗ ] Nature of the procedure        — quote
[ ✓ / ~ / ✗ ] Indication / why it's being offered
[ ✓ / ~ / ✗ ] Benefits — realistic, not oversold
[ ✓ / ~ / ✗ ] Common risks / side effects
[ ✓ / ~ / ✗ ] Serious risks (procedure-specific, see mandatory list)
[ ✓ / ~ / ✗ ] Alternatives                    — quote
[ ✓ / ~ / ✗ ] Option of no treatment + its likely course

>>> SCORECARD — Mandatory disclosure audit

For each item in `mandatory_disclosures`:
   [ disclosed / not disclosed / partially disclosed ] — [item]

>>> SCORECARD — Teach-back and plain language

Teach-back used?              [ yes / no ]
Teach-back was substantive?   [ yes — SP paraphrased in own words / no — SP only said "yes" ]
Jargon flagged unexplained:   [count and terms]
Numeracy framed in absolute terms (e.g., "3 out of 100"), not vague? [ yes / no ]

>>> SCORECARD — Autonomy and process

[ ✓ / ✗ ] Offered time / family consultation
[ ✓ / ✗ ] Did not push toward decision in-room
[ ✓ / ✗ ] Answered "what would you do?" without dismissing autonomy
[ ✓ / ✗ ] Confirmed agreement on next step explicitly

>>> COACHING (one paragraph)

Single highest-yield improvement: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `procedure_or_treatment` | Drives mandatory-disclosure list |
| `sp_baseline_understanding` | none / vague / partial / substantial |
| `sp_concern_pattern` | Pain / side-effects / cost / language-literacy / family / religion / distrust |
| `mandatory_disclosures` | Override default disclosure list |
| `decision_capacity_consideration` | none / mild-deficit / language / minor / surrogate-required |
| `time_pressure` | Shorter station forces prioritization of the highest-stakes risks |
| `prior_complication_in_family` | SP names a relative who had a bad outcome — tests reframing |

## Verification Checklist

- [ ] Five elements scored separately, not bundled.
- [ ] Mandatory disclosure list audited line by line.
- [ ] Teach-back recognized only when SP paraphrased — "yes I understand" does not count.
- [ ] Jargon flagged from verbatim transcript (specific terms named).
- [ ] Numeracy: vague language ("rare," "small chance") downgraded unless paired with a number or analogy.
- [ ] No-treatment alternative is explicitly graded.
- [ ] No invented procedure-specific risks beyond `mandatory_disclosures` or standard literature.
- [ ] If `decision_capacity_consideration` is non-default, learner addressed it; otherwise scored `n/a`.
- [ ] Coaching names ONE improvement.

## Worked Example (compact)

**Input:** procedure = `diagnostic colonoscopy with possible polypectomy`, indication = `iron-deficiency anemia in 62yo`, learner_level = `intern`, sp_baseline = `vague`, concern = `pain`, mandatory_disclosures = `perforation, post-polypectomy bleeding, missed lesion, sedation risk, prep tolerability`, station_minutes = 10.

**Output (excerpt):**

```
Learner: "Mr. R, the reason we're recommending a colonoscopy is to find out why your blood counts are low. The most likely reasons in someone your age include something bleeding slowly in the GI tract, often from a polyp or sometimes from a cancer. The colonoscopy lets us look directly and, if we see a polyp, we can usually remove it the same day."
SP: "It's not going to hurt, is it? My brother said it was awful."
Learner: "Good question — let me walk through what to expect. You'll get sedation through an IV; most people don't remember the procedure. Some people have cramping during the prep the night before. After the procedure, some bloating for a few hours. As for the procedure itself — there are three things I want to make sure you know about..."
[learner names perforation 1-in-1000 to 1-in-2000, post-polypectomy bleeding similar range, missed lesion ~5%, sedation risk]
SP: "What if we just don't do it?"
Learner: "Fair question. If we don't, we'd be guessing about the cause of the anemia, and the most concerning possibility — colon cancer — gets harder to treat the longer it's missed. We could do a CT or a stool test, but those don't let us remove a polyp if we find one."
SP: "OK. What did you mean by 'polypectomy'?"
Learner: "Sorry — I should've explained. A polyp is a small growth on the lining of the colon; 'polypectomy' just means removing it."
[learner does teach-back; SP paraphrases: "you're looking for what's causing the anemia, you can take out a polyp same day, there's a small chance of a tear or bleeding, and the alternatives don't let you fix anything."]

>>> SCORECARD — Five elements

[✓] Capacity (no concern raised, none required)
[✓] Disclosure (nature, risk, benefit, alternatives, no-tx — all named)
[✓] Comprehension (teach-back was substantive)
[✓] Voluntariness (offered time, did not push)
[✓] Documentation / agreement

>>> SCORECARD — Mandatory disclosure audit

[disclosed]            Perforation (with rate)
[disclosed]            Post-polypectomy bleeding (with rate)
[disclosed]            Missed lesion
[disclosed]            Sedation risk
[partially disclosed]  Prep tolerability (mentioned cramping; did not name dehydration or electrolyte issues)

>>> COACHING

Single highest-yield improvement: prep tolerability is the most common reason a patient bails on day-of. Name dehydration and electrolyte issues, and add one practical anchor ("clear liquids start at noon the day before; the prep is split-dose"). That's the disclosure your SP will actually use.
```
