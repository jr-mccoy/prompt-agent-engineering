---
title: "Medicare and Insurance Enrollment Prep — Documents, Questions, and a Verification Checklist Before You Choose"
category: productivity/home-life
description: "Prepare for a Medicare or health-insurance enrollment decision — your own or a parent's — by gathering the documents and facts the choice depends on (current coverage, prescriptions, doctors, expected care, income), writing the questions to take to the official program, a counselling service or a licensed agent, and building a checklist in which every premium, penalty, deadline and eligibility rule is marked [VERIFY with official source] rather than stated; distinct from `home_appointment_prep.md` (any single appointment) and `domain-psychology/client-self-use/pre-therapy/clientself_insurance_eap_sliding_scale_navigation.md` (paying for therapy)."
techniques:
  - SV-02
  - QA-04
  - QA-05
  - CM-02
  - DS-40
difficulty: intermediate
tags:
  - medicare
  - health-insurance
  - enrollment
  - aging-parents
  - household
  - preparation
updated: "2026-09-24"
related_prompts:
  - domain-productivity/home-life/home_appointment_prep.md
  - domain-psychology/client-self-use/pre-therapy/clientself_insurance_eap_sliding_scale_navigation.md
  - domain-finance/personal-finance-planning/finance_insurance_needs_analysis.md
---

# Medicare and Insurance Enrollment Prep

**Objective:** Arrive at an enrollment decision — or a counselling appointment about one —
with every relevant document gathered, your real usage written down, the right questions
ready, and a verification checklist that keeps figures and dates coming from official
sources rather than memory, advertising or this prompt.

**When to Use:**
- You or a parent are approaching Medicare eligibility, retiring, losing employer coverage,
  or moving, and a coverage choice is coming.
- An annual enrollment window is approaching and you want to check whether current coverage
  still fits.
- You are helping a parent who is overwhelmed by mailers and sales calls.
- The same structure applies to other health-insurance enrollment (marketplace, employer
  open enrollment); adjust the program names.

**Not this prompt if:**
- You want someone to tell you which plan to choose — this prompt prepares; the choice is made
  with official tools, a free counselling service or a licensed advisor.
- You need to pay for therapy specifically — `domain-psychology/client-self-use/pre-therapy/clientself_insurance_eap_sliding_scale_navigation.md`.
- You want to size life, disability or other insurance cover — `domain-finance/personal-finance-planning/finance_insurance_needs_analysis.md`.
- It is one appointment with one professional — `home_appointment_prep.md`.

**Hard rule:** This prompt never states a premium, deductible, penalty, income threshold,
enrollment date or eligibility rule. Each such item appears as a question or as
"[VERIFY with official source]". Programs, figures and dates change yearly.

## Inputs Required (SV-02)

**Group 1 — Person and timing**
1. Whose coverage (you or a parent) and their date of birth.
2. The event driving it: turning eligible age, retiring, losing employer coverage, moving, annual review.
3. Whether they (or a spouse) are still working, and whether employer coverage continues.

**Group 2 — Current coverage**
4. Every current plan: insurer, type, member ID location, what it costs now.
5. Any letters recently received from the program, insurer or employer.

**Group 3 — Real usage**
6. Every prescription: name, dose, frequency, pharmacy.
7. Every doctor, specialist and hospital they want to keep.
8. Expected care in the next year: surgeries, therapy, equipment, travel abroad.

**Group 4 — Money and help**
9. Rough household income (some help programs depend on it — the thresholds are to be verified).
10. Who helps: family member, free local counselling service, licensed agent — and whether the
    person wants someone authorised to speak for them.

## Instructions

### Step 1 — Build the document checklist
From the inputs, list what to gather with a status for each (have / find / request):
identity and program cards, current insurance cards, employer coverage letters, the full
medication list, doctor list with contact details, recent notices, income documents if help
programs may apply, and any authorisation form needed for a helper to speak on their behalf
("[VERIFY which form with official source]").

### Step 2 — Write the usage profile
One page: prescriptions, providers to keep, expected care, travel. This is what plan comparison
tools and counsellors need; having it written saves most of the appointment.

### Step 3 — Write the questions (CM-02)
Specific, answerable questions for the official program, a counselling service or an agent.
Examples of the *kind* of question:
- "Given [start date of eligibility], what is my enrollment window, and what happens if I miss it?" [VERIFY]
- "My spouse's employer coverage continues — does that change when I must enroll?" [VERIFY]
- "Are all of these prescriptions covered on this plan, at which tier, at this pharmacy?"
- "Are these doctors and this hospital in network?"
- "Do I qualify for any help with costs at this income?" [VERIFY]
For any agent: "How are you paid, and which insurers do you represent?"

### Step 4 — Build the verification checklist (QA-04, QA-05)
Every figure or date the decision depends on, with the source it must come from (official
program website or letter, the plan's own documents, the counselling service) and a column for
the verified value and date checked. Nothing is filled in from memory or from an advertisement.

### Step 5 — Plan the follow-through (DS-40)
Who books the counselling or official appointment; the decision-by date ("[VERIFY]"); how the
choice will be recorded; confirmation letter to watch for; a note to re-check at the next annual window.

## Constraints

### Must
- Mark every premium, penalty, threshold, date and eligibility rule "[VERIFY with official source]".
- Include a free, non-sales counselling option as a source of help where one exists ("[check availability locally]").
- Ask how any agent is compensated.
- Keep the person whose coverage it is at the centre of the decision.

### Must Not
- Recommend a plan or plan type.
- State any cost, penalty, date or rule as fact.
- Treat marketing mailers or TV adverts as sources.

## Output Format

```
## Enrollment prep — [whose coverage], [event], [date]
Decision needed by: [VERIFY] · Helper: [name, authorised? VERIFY form]

### Documents
- [ ] [item] — have / find / request

### Usage profile
| Prescriptions | Providers to keep | Expected care | Travel |

### Questions (priority order) — for: official program / counselling service / agent

### Verification checklist
| Item the decision depends on | Source it must come from | Verified value | Date checked |

### Follow-through
- [ ] Book [appointment] — [who] — [by when]
- [ ] Record choice + confirmation letter
- [ ] Re-check at next annual window: [VERIFY month]
```

## Verification

- [ ] No number, date or eligibility rule appears without "[VERIFY]".
- [ ] Every prescription and provider the person wants is listed.
- [ ] Documents have a status, not just a name.
- [ ] Questions are specific enough to get a yes/no or a figure.
- [ ] A non-sales help source is included; agent compensation is asked.
- [ ] Follow-through names who books what.

## False-Positive Prevention

1. **Figures from memory.** Premiums, penalties and windows change annually; a remembered
   number can cost real money. Verify every one.
2. **Adverts as information.** Mailers and TV ads sell specific plans; they are not neutral sources.
3. **Choosing on premium alone.** A cheap plan that drops a key prescription or doctor is not cheap.
   The usage profile exists to prevent this.
4. **"Someone else handles it."** A helper without the right authorisation cannot speak to the
   program or insurer on the person's behalf. Check the form.
5. **Missing the employer interaction.** Continued employer coverage, one's own or a spouse's,
   can change timing. Ask; do not assume.
6. **Deciding for a parent.** Where the parent can take part, their priorities (a specific doctor,
   a pharmacy they can walk to) lead.

## Example Output

```
## Enrollment prep — Dad (turns eligible age in March), retiring in June, 2026-09-24
Decision needed by: [VERIFY — ask official program] · Helper: Leah (daughter), authorised? [VERIFY form]

### Documents
- [ ] Program card — Dad has it (kitchen drawer)
- [ ] Employer coverage letter (ends June) — request from HR
- [ ] Medication list — Leah compiling from pharmacy printout
- [ ] Income documents — find last tax return

### Usage profile
| Metformin 500mg 2×/day; Lisinopril 10mg; eye drops (brand) | Dr Alvarez (GP); Dr Kim (cardiology); St Luke's | Cataract surgery likely 2027 | Winters with sister in another state |

### Questions
1. Given retirement in June, when must Dad enroll to avoid any penalty? [VERIFY] — official program
2. Are all four medications covered at CVS on Main St, and at what tier? — each plan / counsellor
3. Are Dr Kim and St Luke's in network, and does coverage work in his sister's state? — each plan
4. Does his income qualify for help with costs? [VERIFY] — counselling service
5. (Agent) How are you paid, which insurers do you represent?

### Verification checklist
| Enrollment window for his dates | Official program letter/site | | |
| Premium for each shortlisted plan | Plan documents | | |
| Out-of-network rule when travelling | Plan documents | | |

### Follow-through
- [ ] Book free counselling session — Leah — by 10-15
- [ ] Record choice + confirmation letter in /Home Docs/08 Health
- [ ] Re-check at next annual window: [VERIFY month]
```

## Techniques Used

- **SV-02 Grouped Input Gathering** — four input groups gathered before any output.
- **QA-04 Uncertainty Acknowledgment** — every figure and date marked for verification.
- **QA-05 Citation Requirements** — each decision-critical fact tied to the source it must come from.
- **CM-02 Constraint Specification** — no recommendations, no stated figures.
- **DS-40 Follow-Up Action Extraction** — the follow-through list with owners.

## Related Prompts

- `home_appointment_prep.md` — for the counselling or agent appointment itself.
- `home_family_caregiving_coordination.md` — when enrollment is one task in ongoing care of a parent.
- `../../domain-psychology/client-self-use/pre-therapy/clientself_insurance_eap_sliding_scale_navigation.md` — insurance navigation for therapy costs.
- `../../domain-finance/personal-finance-planning/finance_insurance_needs_analysis.md` — sizing other insurance cover.
