---
title: "Health Decision Research — Evidence Structure, Source Quality, Question Preparation, and Decision Documentation"
category: personal-development/major-decisions
description: "Support the research process for a non-emergency health decision: treatment options, surgical decisions, screening choices, lifestyle interventions, or second-opinion strategy. Clarifies the underlying question (often not what it first appears), structures the evidence available (study quality, comparable cases, base rates), identifies what to bring to appointments, frames the risk-benefit analysis per option, and documents the reasoning for auditability. This is research scaffolding — the user makes the decision with their clinician."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - personal-decisions
  - health
  - research
  - decision-quality
  - evidence
updated: "2026-05-11"
reasoning:
  styles: [analytic, bayesian, evidence-based]
  stakes: high
  horizon: years
  uncertainty: risk
  evidence_quality: variable
  domain_complexity: regulated
  collaboration: solo
  output_format: structured
  user_role: [individual, patient, caregiver]
  mode: [decide, audit, diagnose, document]
related_prompts:
  - domain-personal-development/major-decisions/personal_relocation_decision.md
  - domain-personal-development/major-decisions/personal_financial_decision_framework.md
  - domain-decision-making/tradeoff_reversibility_stakes_grid.md
  - domain-decision-making/decisioning_regret_minimization.md
  - domain-decision-making/documentation/decisiondoc_options_memo.md
---

# Health Decision Research

**Objective:** Scaffold the research process for a non-emergency health decision so you arrive at consultations better prepared, evaluate evidence more rigorously, and document your reasoning in a way that future-you (or a future clinician) can audit. The prompt clarifies the underlying question being decided (often not the surface question), structures the evidence landscape, identifies what doctors and sources to consult and what questions to bring, walks through risk-benefit per option, and captures the reasoning before the decision is made.

**When to use:**
- Evaluating treatment options where more than one viable path exists.
- Considering an elective surgical procedure.
- Deciding whether to pursue screening, testing, or watchful waiting.
- Evaluating a lifestyle intervention for a chronic condition.
- Preparing for a second-opinion consultation.
- Documenting a health decision for your own records.

**When NOT to use:**
- Emergency or urgent medical situation — act first, research later.
- The decision is straightforward and already made by the clinician you trust.
- You're seeking a diagnosis — that's for a clinician, not a research prompt.

**Audience:** Individuals or caregivers facing a non-emergency health decision where research quality and decision documentation would improve the outcome.

---

## Inputs / Context

1. **The decision being considered.** As specifically as you can state it: what are the options on the table?
2. **Current clinical picture.** Diagnosis or condition (if known), relevant test results, current treatments.
3. **What you've already learned.** Sources consulted, positions of clinicians involved, what's been recommended and why.
4. **Your goal.** What outcome matters most to you? (Avoid recurrence? Minimize recovery time? Preserve function? Avoid side effects?)
5. **Who's involved in the decision.** Solo, with a partner/family, with one clinician, with multiple specialists?

---

## Constraints

### Must
- Clarify the underlying question before evaluating options. The stated question ("should I have surgery?") is often a proxy for the real question ("what is the probability that surgery improves my functional outcome at 5 years compared to conservative management, and what are the major risks?").
- Assess evidence quality per option: RCT data, observational data, case series, expert opinion, or patient forums. These have different weights.
- Include base rates: how common is the condition, how common is each outcome, what's the natural history without intervention?
- Identify who to consult: the right specialist, and whether a second opinion from a different institution adds information or confirms what's known.
- Prepare a question list for appointments, including questions that are hard to ask but matter.
- Document the reasoning so it's auditable: what information was weighed, how, and what was chosen and why.

### Must Not
- Present the model's analysis as medical advice. The prompt produces research scaffolding; the clinician-patient relationship makes the decision.
- Allow the user to skip the "what is my goal" step. Decisions optimized for the wrong goal are common and avoidable.
- Treat patient forums or testimonials as equivalent to clinical evidence. Testimonials are selected on survivors and positive outcomes; they're useful for understanding patient experience, not for estimating probabilities.
- Let the question stay vague ("is this option safe?") when it can be made precise ("what is the rate of [specific complication] in patients with my profile, at what surgical volume threshold?").
- Omit the watchful-waiting option if it exists.

---

## Instructions

### Step 1 — Clarify the actual question
Restate the decision being made with precision:
- What are the candidate options, including no-treatment or watchful waiting?
- What outcome is being optimized? (If the user hasn't stated this, ask.)
- What time horizon matters? (5-year outcomes? Immediate quality of life? Long-term function?)
- What's the decision deadline? Is there a time pressure or does the decision window stay open?

### Step 2 — Understand the natural history
Before evaluating interventions, understand the baseline:
- What happens if no intervention is taken?
- What is the natural course of this condition in patients with this profile?
- Is the condition stable, progressing, or variable?

This establishes what interventions are being compared against.

### Step 3 — Evidence quality per option
For each candidate option, assess:
- Level of evidence: RCTs, meta-analyses, observational cohort, case series, expert consensus, or anecdote.
- Applicable population: does the evidence apply to patients with your specific profile (age, comorbidities, disease severity)?
- Effect size: how large is the benefit, and on what outcome measure (surrogate endpoint vs. patient-centered outcome)?
- Harms: what are the documented harms, at what frequency, and how severe?
- Source quality: peer-reviewed, institutional, patient advocacy (with incentive to overstate), manufacturer-sponsored.

### Step 4 — Base rates
- How common is the condition in the relevant population?
- What is the background rate of the outcomes each intervention is trying to prevent?
- What is the absolute risk reduction vs. relative risk reduction? (Relative risk numbers are typically larger and more persuasive; absolute risk reductions are more informative.)

### Step 5 — Identify who to consult
- What specialty or subspecialty has the most relevant expertise for this decision?
- Is a second opinion at a different institution likely to add information (e.g., different surgical approach, different evidence interpretation) or confirm what's already known?
- What specific question would you ask the second-opinion provider that you haven't yet gotten a clear answer to?
- Are there patient support networks for this condition with members who have faced the same decision? (Useful for patient-experience data, not probability data.)

### Step 6 — Question list for appointments
Prepare questions in three categories:
- **Probability questions:** "What is the probability of [outcome] with option A vs. option B, in patients with my profile?"
- **Process questions:** "What does the procedure/treatment involve, what's recovery, what's the monitoring plan?"
- **Values questions:** "If your family member were in my situation, what would you recommend and why?"

Also prepare the hard question: the one you've been avoiding because you're afraid of the answer. Write it down. Bring it.

### Step 7 — Risk-benefit per option
For each option:
- Expected benefit: what's the likely upside if the intervention works?
- Probability of benefit in patients like you.
- Major risks: what are the significant harms, at what probability?
- Minor risks / side effects: frequency, manageability.
- Reversibility: if this option doesn't work or causes harm, what are the recovery paths?
- Option value of waiting: if watchful waiting is available, does it preserve the option to intervene later at the same probability of benefit?

### Step 8 — Decision quality independent of outcome
Document the reasoning:
- What information was weighted and how.
- What the decision is and why, stated in terms of your stated goal.
- What would change the decision (new information, test result, second opinion finding).
- Calibration anchor: a sentence written today that captures what you're choosing and why, for your own records.

---

## False-Positive Prevention

1. **Vague question acceptance.** "Is this safe?" is not a question that produces useful answers. Precision is: "What is the 30-day complication rate for this procedure in patients with my risk profile at high-volume centers?"
2. **Relative risk inflation.** "Reduces risk by 40%" sounds dramatic. If background risk is 2%, the absolute reduction is 0.8%. Know which number you're working with.
3. **Testimonial weighting.** Positive patient testimonials are systematically selected for positive outcomes and by patients motivated to share. They're useful for understanding the experience; they're not probability data.
4. **Goal-omission.** Making a decision without having stated what outcome matters most. Surgery that eliminates recurrence risk at the cost of function is optimal for one goal and wrong for another.
5. **Second-opinion inflation.** A second opinion at the same institution, from the same specialty, trained at the same school, adds less than it appears. Seek second opinions that add genuine independence.
6. **Watchful-waiting skip.** Active surveillance is frequently the correct choice for a range of conditions. It deserves full evaluation, not default dismissal as "doing nothing."
7. **Option-value neglect.** Some interventions foreclose future options; others preserve them. The option to intervene later at equivalent probability of benefit is worth something — factor it in.
8. **Manufacturer-sponsored evidence weighting.** Clinical evidence sponsored by device or pharmaceutical manufacturers is not necessarily wrong, but it has a documented bias toward positive findings. Weight accordingly.
9. **Urgency manufacture.** "You need to decide this soon" is sometimes accurate and sometimes creates pressure that compresses research. Ask what the actual decision window is.

---

## Output Format

```
# Health decision research — [condition / decision]

## Decision restated
- Options on the table: [including watchful waiting if applicable]
- Outcome being optimized: [user's stated goal]
- Time horizon: [...]
- Decision deadline: [...]

## Natural history (no intervention)
- Expected course: [...]
- Rate of progression / stabilization: [...]

## Evidence quality per option
| Option           | Level of evidence | Applicable to my profile? | Effect size | Major harms (rate) | Source quality |
|------------------|-------------------|--------------------------|-------------|-------------------|----------------|
| [Option A]       |                   |                          |             |                   |                |
| [Option B]       |                   |                          |             |                   |                |
| Watchful waiting |                   |                          |             |                   |                |

## Base rates
- Condition prevalence in my profile: [...]
- Outcome rates (absolute, not relative): [per option]
- Absolute risk reduction per option: [...]

## Who to consult
- Primary specialist: [type, what question they answer]
- Second opinion: [needed? at what institution? what specific question?]
- Patient network: [useful for what — experience, not probability]

## Appointment question list
- Probability questions: [list]
- Process questions: [list]
- Values question: [the "what would you recommend for a family member" question]
- The hard question I've been avoiding: [write it down]

## Risk-benefit per option
| Option           | Expected benefit | Probability of benefit | Major risks (rate) | Reversible? |
|------------------|-----------------|----------------------|--------------------|-------------|
| [Option A]       |                 |                      |                    |             |
| [Option B]       |                 |                      |                    |             |
| Watchful waiting |                 |                      |                    |             |

## Decision reasoning (for your records)
- Information weighed: [list]
- Decision: [what and why, in terms of your stated goal]
- What would change this: [new information, test result, second-opinion finding]
- Calibration anchor (write down today): "I am choosing [option] because [evidence-based reason tied to my goal], understanding the primary risk is [named risk] at [stated probability]."
```

---

## Verification

- [ ] Underlying question clarified with precision (not vague).
- [ ] Natural history (no intervention) described.
- [ ] Watchful waiting included as an option if applicable.
- [ ] Evidence quality assessed per option (level, applicability, effect size).
- [ ] Absolute risk reduction used, not just relative.
- [ ] Base rates included.
- [ ] Appointment question list includes the hard question.
- [ ] Risk-benefit table completed per option including reversibility.
- [ ] Testimonials and patient forums weighted for what they're useful for (experience, not probability).
- [ ] Decision documented with calibration anchor.
