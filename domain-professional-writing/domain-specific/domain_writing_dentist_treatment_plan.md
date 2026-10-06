---
title: "Dentist Treatment Recommendation Letter — Phased Sequence, Real Alternatives, Estimates Pending Predetermination"
category: professional-writing/domain-specific
description: "Draft a dentist's letter explaining a recommended course of treatment to a patient: findings in plain words with tooth names, care sequenced disease-control first with elective items kept separate, a reasonable alternative for each item (including monitoring, extraction, or specialist referral), what may happen if care is delayed stated factually, and a cost-and-insurance estimate labelled as pending predetermination with annual-maximum effects shown. For licensed dentists writing to real patients — distinct from treatment-planning practice for dental learners (dental_treatment_planning_practice) and from the consent conversation itself (medicine_informed_consent_communicator)."
techniques:
  - DS-06
  - NE-16
  - NE-27
  - QA-04
  - QA-20
difficulty: intermediate
tags:
  - dentist
  - dental-treatment-plan-letter
  - patient-letter
  - treatment-options
  - dental-insurance-estimate
  - explain-dental-work-to-patient
updated: "2026-10-06"
related_prompts:
  - domain-medical-education/profession-specific/dental/dental_treatment_planning_practice.md
  - domain-healthcare-clinical/prompts/communication/medicine_informed_consent_communicator.md
  - domain-healthcare-clinical/templates/patient_education_template.md
  - domain-professional-writing/domain-specific/domain_writing_veterinarian_surgery.md
---

# Dentist Treatment Recommendation Letter

**Objective:** Give a patient a written account of what the dentist found, what they recommend and in what order, the reasonable alternatives, what may happen if care is delayed, and what it is likely to cost — clear enough to decide on and honest about what is still an estimate.

**When to Use:**
- After a comprehensive exam with more than one item of treatment to sequence.
- The patient asked for the plan in writing to think about, share with family, or compare.
- Insurance limits or cost make timing a real choice the patient should understand.
- The patient has deferred care before and needs reasons, not pressure.
- **Not this prompt if** you are a dental student practising treatment planning — use `domain-medical-education/profession-specific/dental/dental_treatment_planning_practice.md`. Structuring the consent discussion for a specific procedure is `domain-healthcare-clinical/prompts/communication/medicine_informed_consent_communicator.md`; this letter prepares for that conversation and does not replace it.

**Audience:** An adult patient (or parent/guardian) without dental training, who will weigh cost and inconvenience against advice and may feel embarrassed about their oral health. The dentist signs and owns the letter and all clinical content; the model drafts from the dentist's findings and adds none of its own.

## Inputs / Context

Paste source material inside the named tags and refer to it by tag name.

1. **Patient** — name, age, relevant medical history affecting care, concerns and goals in their words — in `<patient>`.
2. **Exam findings** — by tooth or area, with severity and the evidence (radiograph, probing depths, symptoms) — in `<exam_findings>`.
3. **Recommended sequence** — what, in what order, why that order, which items can safely wait and how long — in `<treatment_sequence>`.
4. **Alternatives and prognosis** — the dentist's own alternatives per item and any likelihood figures, in the dentist's words — in `<clinical_notes>`. The model adds no percentages.
5. **Fees and insurance** — fee per procedure; benefit breakdown (coverage %, annual maximum, amount used, reset date, frequency limits); predetermination status — in `<fees_insurance>`.
6. **Payment options** offered by the practice — in `<payment_options>`.

## Method

1. **Translate findings (DS-06).** Each finding: tooth name in words ("lower right first molar, #30"), what is wrong, how the dentist knows, and severity. Group into: needs treatment now, can be scheduled, optional/elective.
2. **Sequence and say why.** Disease control (infection, decay, active gum disease) before definitive restorations; restorations before replacements or cosmetic work. State any "can wait until" from `<treatment_sequence>` with its condition.
3. **Give a real alternative for each item (NE-16).** Include monitoring, a less extensive restoration, extraction (with or without replacement), and specialist referral where `<clinical_notes>` lists them; say plainly why the dentist prefers the recommendation.
4. **State delay consequences factually (NE-27).** What may change, roughly over what time if the dentist gave one, and what the treatment then becomes — in "may" language, without worst-case imagery.
5. **Build the estimate.**
   - `Insurance estimate = min(Σ fee × coverage %, remaining annual maximum)`; `Patient estimate = total fees − insurance estimate`.
   - If items can safely span the benefit-year reset, show both timings and the difference.
   - Label every figure "estimate" and state predetermination status.
6. **Verify before drafting (QA-04).** Every finding, alternative, and likelihood traces to `<exam_findings>` or `<clinical_notes>`; any prognosis figure without a dentist source is removed or marked `[VERIFY: dentist's figure]`; every fee and coverage % traces to `<fees_insurance>`; frequency limits or classifications not in the breakdown are `[VERIFY: plan / predetermination]`. Produce an internal check list that is not sent.

## Output Format

```
[Practice letterhead]   [Date]
Dear [Patient],

## What we found
[Item — tooth/area in words — what it is — how we know]

## What I recommend, in order
[Phase / visit — treatment — why this comes now]

## Your choices for each item
[Item — recommended — alternatives (incl. monitoring / referral) — why I prefer]

## If you wait
[Per item: what may happen, plainly]

## Timeline
[Visits, approximate dates, healing intervals]

## Estimated cost and insurance
| Treatment | Fee | Insurance est. | Your est. |
[Annual maximum effect · timing options · predetermination status · payment options]

## Next steps
[Book · questions · who to call]

[Dentist signature]

--- INTERNAL CHECK (not sent) ---
[Sources for each figure · VERIFY items · consent to be obtained at visit]
```

## Verification

- [ ] Every tooth number is paired with its plain name.
- [ ] Disease-control items precede restorative and elective items; elective items are labelled optional.
- [ ] Each item has at least one alternative, and monitoring or referral appears where clinically reasonable.
- [ ] Every likelihood figure is the dentist's own, labelled as such.
- [ ] Insurance estimates respect the remaining annual maximum and recompute from fees × coverage %.
- [ ] Predetermination status is stated; nothing is called final while it is pending.
- [ ] "If you wait" uses factual, non-alarming language.

## False-Positive Prevention

1. **A success rate the dentist never gave.** "Crowns last 10–15 years" or "95% success" reads authoritative and has no source in this patient's chart. Only the dentist's own figures, attributed to the dentist.
2. **"If untreated" as a scare.** "You will lose this tooth" or graphic worst cases push some patients to agree and others to avoid the office entirely. State what may happen and what treatment would then be needed.
3. **An insurance estimate presented as the bill.** Before the predetermination returns, coverage %, frequency limits, and how the plan classifies a procedure are assumptions. Call it an estimate and say what is pending.
4. **The annual maximum ignored.** Summing fee × coverage % across a large plan overstates insurance when the remaining maximum is lower — the patient finds out at checkout.
5. **No alternative offered.** A letter with only one option is a sales letter and leaves the patient unprepared for the consent conversation. Monitoring, extraction, and specialist referral are real options even when not preferred.
6. **Elective work folded into disease control.** Whitening or replacing sound fillings for appearance, listed in the same phase as decay and gum treatment, makes the whole plan look padded.
7. **Blame in the wording.** "Neglected", "you haven't been coming in", or "poor hygiene" makes a patient defer the very care the letter recommends. Describe the condition, not the patient.

## Dual-Failure Prevention (QA-20)

- **Harmful:** overstating urgency or certainty — invented prognosis figures, a final-sounding price, or fear-led delay consequences — so the patient agrees without understanding the options.
- **Unhelpful:** a letter of codes and disclaimers, or so soft that the patient cannot tell which item matters most and puts it all off.
- **Bar:** the patient can say which item matters most and why, what their alternatives are, roughly what they will pay and what could change that number — and nothing in the letter would embarrass the dentist if read aloud to a colleague.

## Example Output

```
Brookside Family Dentistry   6 October 2026
Dear Ms. Kowalski,

## What we found
1. Lower right first molar (#30): the large old silver filling has a cracked
   corner and decay underneath. It is sensitive to cold, and the X-ray shows the
   decay is close to the nerve.
2. Gums, upper right and lower left: pockets of 5–6 mm that bleed, with some bone
   loss on X-ray — moderate gum disease in those two areas.
3. Upper left first molar (#14): a small cavity between teeth.
4. Lower left first molar (#19), removed in 2019: the space can be filled later.
You also asked about whitening — that is optional and comes last.

## What I recommend, in order
Phase 1 — gum and decay control: deep cleaning of the two gum areas (scaling and
root planing, two visits); filling #14; a build-up and crown on #30.
Phase 2 — after the gums are rechecked: decide how, or whether, to replace #19.
Ongoing: gum maintenance cleanings every 3 months.

## Your choices for each item
#30: Crown (recommended) — holds the cracked tooth together. Alternatives: a
partial crown (onlay) if the crack proves small once the old filling is out;
removal of the tooth, with or without a replacement. Watching it is not one I
recommend, because it is cracked and already sensitive. If the nerve proves
involved, it would need a root canal first — I estimate about 1 in 5 from your
symptoms and X-ray. I would tell you before going further.
Gums: deep cleaning (recommended), or referral to a gum specialist (periodontist)
— a good choice too, and the next step if the pockets do not improve. A regular
cleaning cannot reach pockets this deep.
#14: tooth-coloured filling, or watching it for six months. I recommend filling
it while it is small.

## If you wait
#30: the crack may spread; if it reaches below the gum, the tooth may not be
saveable. Decay may reach the nerve, which would mean a root canal or removal.
Gums: lost bone does not grow back; treatment stops further loss.

## Timeline
Deep cleaning: 20 Oct and 27 Oct. #14 filling: 27 Oct. Gum recheck: early Dec.
#30 crown: now, or early January (safe to wait until then — call sooner if it
aches on its own or wakes you).

## Estimated cost and insurance
| Treatment                 | Fee    | Insurance est.* | Your est.* |
| Deep cleaning, 2 areas    | $520   | $416 (80%)      | $104 |
| #14 filling               | $210   | $168 (80%)      | $42  |
| #30 build-up + crown      | $1,645 | $822.50 (50%)   | $822.50 |
*Before your plan's yearly maximum. Your plan has $1,180 left for 2026
($1,500 − $320 used) and renews 1 January.
- All in 2026: insurance capped at $1,180 → you pay about $1,195 ($2,375 − $1,180).
- Crown in January: 2026 you pay $146; 2027 you pay $822.50 → $968.50 total,
  about $226.50 less.
We sent a predetermination for #30 on 22 Sept and have not heard back, so these
are estimates. Root canal, if needed: $1,150 fee, coverage to be confirmed.
Payment: up to 3 monthly payments, no interest.

## Next steps
Call Maria at the front desk to book 20 Oct, and tell her whether you prefer the
crown now or in January. Bring any questions to the first visit.

Dr. Anita Shah, DDS

--- INTERNAL CHECK (not sent) ---
"1 in 5" — Dr. Shah, <clinical_notes>. "Safe until January" — <treatment_sequence>.
Fees and 80/50%, $1,500 max, $320 used → <fees_insurance>.
VERIFY: plan classification of deep cleaning (basic vs major); root canal coverage
%; perio-maintenance frequency limit. Consent for each procedure at the visit.
```

## Techniques Used

- **DS-06 Prioritization and Severity Guidance** — findings sorted into treat-now, schedule, and optional, driving the phase order.
- **NE-16 Non-Judgmental Comparison** — each item's alternatives, including monitoring and referral, set out fairly.
- **NE-27 Cost of Inaction Framing** — delay consequences stated factually, in "may" language.
- **QA-04 Uncertainty Acknowledgment** — estimates labelled pending predetermination; likelihoods attributed to the dentist.
- **QA-20 Dual-Failure Quality Test** — neither pressure nor a letter too soft to act on.

## Related Prompts

- `domain-medical-education/profession-specific/dental/dental_treatment_planning_practice.md` — phased planning practice for learners, not letters to real patients.
- `domain-healthcare-clinical/prompts/communication/medicine_informed_consent_communicator.md` — the consent conversation this letter prepares for.
- `domain-healthcare-clinical/templates/patient_education_template.md` — general patient-education handouts on a condition.
- `domain-professional-writing/domain-specific/domain_writing_veterinarian_surgery.md` — the same honest-options letter for a pet owner.
