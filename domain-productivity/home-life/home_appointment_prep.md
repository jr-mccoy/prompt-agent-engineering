---
title: "Appointment Prep Generator"
category: productivity/home-life
description: "Prepare for any upcoming appointment — medical, school meeting, financial, home repair, or legal consultation — with a documents-to-bring list, targeted questions, and a post-appointment action plan."
techniques:
  - ST-01
  - DS-02
  - CM-02
  - CM-08
  - QA-01
  - RT-09
difficulty: beginner
tags:
  - appointments
  - preparation
  - medical
  - school
  - financial
  - household
updated: "2026-05-12"
related_prompts:
  - domain-parenting/parenting_school_accommodation_conversation_prep.md
  - domain-productivity/bottlenecks/bottleneck_capture_triage_system_design.md
  - domain-personal-development/prompts/agency/agency_next_action_spec.md
---

# Appointment Prep Generator

**Objective:** Produce a practical pre-appointment checklist for any scheduled professional meeting — what to gather, what to ask, and what to do afterward. Tailored to the appointment type so the output is specific, not generic.

**When to use:** Any time you have a professional appointment in the next few days and you want to walk in prepared rather than remembering questions in the parking lot on the way home. Especially valuable for medical visits, school meetings (IEP, 504, parent-teacher), financial consultations, home repair estimates, and legal consultations.

**Audience:** Adults attending any professional appointment on behalf of themselves or a family member. Works for one-time appointments and recurring visits where something specific needs to be addressed. Not designed for job interviews or sales meetings — this is for consumer and patient-side preparation.

---

## Inputs Required

1. **Appointment type.** What kind of appointment: medical/dental, school meeting (specify: IEP, 504 review, parent-teacher conference, disciplinary), financial (tax prep, financial advisor, mortgage), home repair or estimate, legal consultation, or other (describe). Type determines the prep template applied.

2. **Specific purpose of this appointment.** What is this particular visit for — not the category, but the specific issue. "Annual physical" is different from "follow-up on a new chest pain complaint." "Parent-teacher conference" is different from "meeting to discuss my child being recommended for retention." Be specific.

3. **Who is attending.** Who from your household is going to this appointment. If it's for a child or a dependent, note that.

4. **What information you think they'll need from you.** What the professional will likely ask for — recent test results, prior records, a list of medications, the model number of the broken HVAC unit, last year's tax documents. List what you have and what you'd need to find.

5. **Your existing questions or concerns.** Anything you already want to ask or know. Even vague: "I want to understand whether this is serious" or "I want to know if we have any legal options." These get sharpened in the output.

6. **What outcome you're hoping for from this appointment.** What a successful appointment looks like: a diagnosis, a treatment plan, a cost estimate, a signed agreement, a specific accommodation agreed to. This shapes which questions to prioritize.

---

## Instructions

### Step 1 — Classify the appointment type and apply the appropriate template

Match the appointment to one of these categories and activate the corresponding prep logic:

**Medical / Dental:**
- Documents: insurance card, photo ID, list of current medications (name, dose, frequency), prior test results if relevant to this visit, referral if required
- Information to prepare: symptom timeline (when did it start, how has it changed, what makes it better or worse), prior treatments tried, family history if relevant to the condition
- Questions focus: diagnosis, treatment options, alternatives to the recommended treatment, what to watch for, when to follow up, referral if needed

**School Meeting (IEP / 504 / Parent-Teacher):**
- Documents: any prior evaluation reports, current IEP or 504 if updating, grade reports or work samples if relevant, notes on behaviors or incidents you've observed at home
- Know your rights: if this is an IEP or 504 meeting, you have the right to bring a support person, request an independent evaluation, and disagree with proposed placements in writing
- Questions focus: what the school is observing, what accommodations are proposed and why, what the evaluation timeline is, what the parent's role is in the plan, what triggers a plan review

**Financial (Tax, Advisor, Mortgage):**
- Documents: last year's returns if tax appointment, account statements, recent pay stubs, list of major financial events this year (job change, home purchase, inheritance, large medical expenses)
- Questions focus: specific concern you came with (is this deductible? should I refinance? am I on track for retirement?), fees and how the professional is compensated, what to do before the next appointment

**Home Repair / Estimate:**
- Information to prepare: describe the problem accurately (when it started, what you've already tried, any related issues), know what you want from this visit (diagnosis only? diagnosis plus estimate? authorized repair?), note any warranty or prior work done on this system
- Questions to ask: what is the problem, what are the repair options and costs, how long will it take, are there parts required and lead times, payment terms, warranty on the work

**Legal Consultation:**
- Documents: any contracts, correspondence, notices, or evidence relevant to the matter
- Information to prepare: timeline of events in chronological order, what you want to achieve, what you're willing to accept
- Questions focus: do you have a viable claim or defense, what are the options, what does the process look like, what are the costs, what is the attorney's assessment of likely outcomes

### Step 2 — Sharpen existing questions

Take the user's existing questions or concerns from the inputs and improve them:

- Remove vague questions that won't get useful answers ("Is this serious?" → "What does this result mean for my prognosis, and what's the range of treatment approaches?")
- Add specificity about what decision the answer will inform ("I want to know if I need a specialist — what would make you refer me vs. manage this here?")
- Sequence questions from most important to least, so if time runs short, the critical ones are asked first

### Step 3 — Build the documents checklist

From Step 1's template plus the user's specific inputs, produce a complete list of what to bring or have available. For each item, note: "have it," "need to find it," or "need to request it in advance" where that's clear from the inputs.

### Step 4 — Build the post-appointment action plan

For the expected outcome the user described, list what they'll likely need to do after:
- Decisions to make within the next week (approve the treatment plan, sign the estimate, file the paperwork)
- Follow-up to schedule (next appointment, prescription to fill, specialist referral to call)
- Things to track or monitor (symptom changes, whether the repair holds, next steps in a legal process)

---

## Constraints

### Must
- Apply the type-appropriate template from Step 1 — do not use a generic checklist for all appointment types
- Sharpen every question the user provides — do not reproduce vague questions verbatim
- Sequence questions by priority (most important first)
- Include a post-appointment action section
- Note which documents need to be found or requested in advance, not just what to bring

### Must Not
- Add generic disclaimers ("consult your doctor before making any medical decisions") — the user is going to a doctor; this prompt prepares them
- Add legal disclaimers to legal prep — the user is going to an attorney; this prompt prepares them for that conversation
- Include questions irrelevant to the specific appointment type
- List documents as "bring everything" — be specific to this appointment's purpose
- Assume the user knows their rights in a school meeting without stating them explicitly

---

## False-Positive Prevention

1. **Generic prep list:** Produces the same checklist regardless of appointment type — "bring ID, write down your questions, arrive 10 minutes early." The value of this prompt is type-specific prep. If the output could apply to any appointment, it has failed.

2. **Untouched vague questions:** Returns the user's original questions without sharpening them. "I want to understand what's going on" must become a specific question the professional can actually answer.

3. **Missing decision focus:** Prepares questions but never clarifies what decision or outcome this appointment should produce. The user should leave knowing what they're supposed to do next.

4. **Documents without status:** Lists documents to bring without distinguishing "you have this" from "you need to call ahead and request this" — causing the user to show up missing critical items.

5. **School meeting rights omitted:** For IEP or 504 meetings, fails to note that parents have specific procedural rights. These are not optional to mention — they change how the user should approach the meeting.

---

## Output Format

```
## Appointment Prep: [Appointment Type] — [Date]

### Purpose of This Appointment
[One-sentence restatement of what this specific appointment is for]

---

### Documents to Bring

- [ ] [Item] — [Status: Have it / Need to find / Call ahead to request]
- [ ] [Item] — [Status]
- [ ] ...

---

### Questions to Ask (Priority Order)

1. **[Question]** — [Why this matters / what decision it informs]
2. **[Question]** — [Why this matters]
3. **[Question]** — [Why this matters]
[3–6 questions, ordered most important first]

---

### What to Tell Them (Information They'll Need From You)

- [Specific piece of information to have ready, e.g., "Symptom started approximately [date] and has been [describe change]"]
- ...

[For school meetings — know your rights:]
- [Applicable rights if IEP/504]

---

### Post-Appointment Action Plan

**Decide within this week:**
- [ ] [Decision to make]

**Schedule or follow up:**
- [ ] [Call/schedule/request]

**Monitor or track:**
- [ ] [What to watch for]

---

### Notes
[Any other context-specific flags — e.g., "If they recommend X without discussing Y, ask why" or "You have a right to a second opinion before agreeing to this"]
```

---

## Verification

- [ ] Prep checklist is specific to the appointment type, not generic
- [ ] All questions from the user's inputs are sharpened and sequenced by priority
- [ ] Documents list distinguishes what to bring vs. what needs to be requested in advance
- [ ] Post-appointment action plan specifies at least one concrete next step
- [ ] For school meetings (IEP/504), parental rights are noted
- [ ] Outcome the user wants is reflected in the question prioritization
- [ ] No generic disclaimers or boilerplate added
