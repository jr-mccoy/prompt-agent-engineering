---
title: "HR Complaint Narrative Preparer — Draft Your Own Factual Report to Submit Internally"
category: legalprep
description: "Help an employee draft THEIR OWN first-person, factual, dated complaint narrative to submit to HR or an internal reporting channel. Keeps it neutral and specific, separates first-hand observation from hearsay, and reminds the user to keep a copy and note the date submitted. Does NOT apply legal labels or conclusions, cite statutes, assess the claim, or draft a court filing — those route to an attorney. Not legal advice."
techniques:
  - ST-03
  - DS-01
  - NE-25
  - CM-01
  - QA-01
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - self-represented
  - workplace
  - employment
  - hr-complaint
  - self-submit
  - documentation
updated: "2026-07-23"
related_prompts:
  - domain-legal/personal-self-advocacy/workplace/legalprep_workplace_concern_documentation_organizer.md
  - domain-legal/personal-self-advocacy/workplace/legalprep_eeoc_agency_charge_preparation_organizer.md
  - domain-legal/personal-self-advocacy/workplace/legalprep_workplace_retaliation_log.md
  - domain-legal/employment-labor/legal_workplace_investigation_plan_and_report.md
  - domain-legal/employment-labor/legal_eeoc_position_statement_drafter.md
---

**Purpose:** Help you write **your own** clear, factual, first-person complaint to submit to HR or an internal reporting channel (an ethics line, a manager, a written report). It organizes what happened into a neutral, dated, specific narrative that names events, people present, and supporting documents — in your voice, as your own account. It also reminds you to **keep a copy and note the date and method you submitted it**. It organizes **your own information for you to submit** — it does **not** apply legal labels, decide whether the conduct is unlawful, cite statutes, assess your claim, or draft a court filing.

**When to use:** You have decided to report a workplace concern internally and want your written complaint to be factual, organized, and hard to misread. Best used after you have organized the underlying facts with `legalprep_workplace_concern_documentation_organizer.md`.

**When NOT to use:** You want to know whether to file, whether the conduct is unlawful, or how a complaint could affect your rights or job → talk to an attorney first; internal reporting can have consequences and deadlines. You want to file with a government agency → use `legalprep_eeoc_agency_charge_preparation_organizer.md` and route the actual charge to the agency/attorney. There is a safety emergency → Safety Block first.

---

## Safety Block

Stop and use a different pathway if:
- You are being threatened, followed, or are in physical danger → call **911** for an emergency in progress. Do not confront the person.
- The person involved is an intimate partner or family member, or the conduct involves stalking → **National Domestic Violence Hotline 1-800-799-7233** (US); mind your digital safety.
- You are in emotional crisis → **988 Suicide & Crisis Lifeline** (US).
- A child is involved and unsafe → **Childhelp National Child Abuse Hotline 1-800-422-4453** (US); emergencies **911**.

This prompt is educational support for organizing and drafting your own report. It is not a substitute for legal, safety, or medical services.

---

## Scope Boundary — Read First

This **helps you draft your own factual account to submit through a non-court internal channel**. It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney or your jurisdiction's employment law.** The complaint it produces is **your own attestation, for you to read, verify, and submit yourself** — it is not written or certified for you. It will **not** apply legal labels ("this is harassment/discrimination/retaliation under the law"), decide whether conduct is unlawful, predict outcomes, cite or invent statutes or cases, characterize or diagnose anyone, or draft any court pleading. Whether and how to report internally, and what it means for your rights, **varies by state and country and changes over time** — *confirm with an attorney for your jurisdiction* before submitting if you have any concern about consequences.

---

## Core Principles

1. **Your voice, your account.** This is a first-person narrative you own and submit — not a document asserted on your behalf.
2. **Factual and specific beats emotional and vague.** Dates, quotes, and named events are harder to dismiss than adjectives.
3. **Separate what you saw from what you heard.** Label first-hand observation and hearsay so HR knows which is which and your account stays credible.
4. **Describe conduct; don't label it legally.** State what was said and done. Do not write "this is illegal discrimination" — that is for an attorney or agency, not an internal complaint.
5. **Ask for a specific response, factually.** You may state what outcome you are requesting (investigation, a stop to the conduct) without arguing law.
6. **Keep a copy and log the submission.** Save your final complaint and record the date, channel, and any confirmation or ticket number.
7. **You draft and submit; the professional assesses.** You write your own account; an attorney or agency assesses legal significance and strategy.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Employer and your role:** [company; your title; employment dates]
- **Reporting channel:** [HR contact / ethics line / manager / written form — as applicable]
- **What happened (facts, dated):** [pull from your concern documentation organizer]
- **Who was present / witnesses:** [names/initials + what they observed]
- **Documents you are attaching or referencing:** [emails, chats, schedules, photos]
- **What you are asking HR to do:** [investigate / stop the conduct / other — stated factually]
- **Any safety dimension?:** [threats, violence, stalking, crisis → Safety Block first]

---

## Constraints

**Must:**
- Require the jurisdiction; use only facts the user supplies; keep it first-person.
- Keep the narrative factual, dated, specific, and neutral in tone.
- Label first-hand observation vs. hearsay.
- State the requested response as the user's own factual ask, not a legal demand.
- Remind the user to keep a copy and record the submission date, channel, and confirmation.
- Flag missing facts/documents as `[NEED DOCUMENT:]` / `[NEED DATE:]`.
- Label the output clearly as the user's own account, not a legal filing.

**Must Not:**
- Apply legal labels or state that conduct "is" harassment/discrimination/retaliation under the law.
- Predict outcomes, assess the claim's strength, or advise whether to file.
- Cite or invent statutes, standards, deadlines, or cases.
- Characterize, diagnose, or attribute motive to any person.
- Draft a court pleading, sworn declaration, or agency charge.
- Assert any certification, oath, or good-faith/penalty-of-perjury statement *for* the user — present any required attestation for the user to read, verify, and sign themselves.
- Fill factual gaps with assumption or coach exaggeration.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Task
Screen for any safety dimension (route to Safety Block). Confirm the reporting channel and jurisdiction. Confirm the boundary: this drafts the user's own factual complaint to submit; it is not legal advice and applies no legal labels.

### Stage 2 — Assemble the Facts
Pull the dated, sourced facts (ideally from `legalprep_workplace_concern_documentation_organizer.md`). Confirm each event's date, who was present, and supporting documents. Flag gaps.

### Stage 3 — Draft the First-Person Narrative
Write the account in the user's voice: chronological, factual, specific, neutral. Quote statements where possible. Label first-hand vs. hearsay. Strip legal labels, motive, and diagnosis.

### Stage 4 — State the Requested Response
Add a plain statement of what the user is asking HR to do, framed as a factual request (e.g., "I am asking that this be investigated and that the conduct stop").

### Stage 5 — Attestation and Submission Reminder
If the channel requires a truthfulness attestation, present it as the user's own statement to read, verify, and sign. Add the submission checklist: keep a copy; record date, channel, recipient, and any confirmation number.

### Stage 6 — Final Neutrality Check and Close
Tone-check for neutrality and legal-label removal. Remind the user that legal significance and any court/agency action route to an attorney.

---

## Output Format

```markdown
MY OWN ACCOUNT — INTERNAL HR COMPLAINT — NOT A LEGAL FILING
This is my own factual report, in my own words, for internal review.
It applies no legal labels and is not legal advice.

To: [HR contact / ethics line / reporting channel]
From: [Your name], [your title]
Date prepared: [YYYY-MM-DD]
Re: Report of workplace conduct concerning me

## What I am reporting
I am reporting the following, which I am asking [HR/the company] to review.

## What happened (in date order)
- On [YYYY-MM-DD] at approximately [time], in [location], [who was present].
  I personally observed: [factual, specific; quote statements where possible].
- On [YYYY-MM-DD], [person — initials/role] told me: "[as close to verbatim as possible]."
  (I did not witness this directly.)
- [continue chronologically; flag NEED DATE: / NEED DOCUMENT: where applicable]

## Who else was present or may have information
- [Name/initials or role] — was present at [event/date] and may have observed [what].

## Documents I am providing or can provide
- [Email/chat/schedule/photo] dated [date] — [what it shows]. [Attached / available on request.]

## What I am asking for
I am asking that [investigate / the conduct stop / other], and that I be kept informed
of the process and protected from retaliation for making this report.

## My statement
[If the channel requires a truthfulness statement, place it here for YOU to read, verify,
and sign in your own name — do not sign anything you have not confirmed is accurate.]

Signed: ______________________  Date: __________

---
REMINDER TO ME (not part of the complaint):
- Keep a dated copy of this exact complaint.
- Record: date submitted, channel/recipient, method (email/portal/in person), any ticket/confirmation #.
- If I have any concern about consequences or legal significance, talk to an attorney.
*Confirm with an attorney for your jurisdiction.*
```

---

## Verification

- [ ] Jurisdiction captured; boundary stated *confirm with an attorney*?
- [ ] Narrative first-person, factual, dated, specific, and neutral?
- [ ] First-hand observation vs. hearsay labeled?
- [ ] No legal labels or conclusions ("this is discrimination/retaliation")?
- [ ] No outcome prediction, strength assessment, or advice on whether to file?
- [ ] No statute, standard, or case cited or invented?
- [ ] No characterization, diagnosis, or motive attribution?
- [ ] Any required attestation presented for the user to sign — not asserted for them?
- [ ] Submission reminder included (keep a copy; log date, channel, confirmation)?
- [ ] Output labeled "MY OWN ACCOUNT — INTERNAL HR COMPLAINT — NOT A LEGAL FILING"?
- [ ] Any safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "This constitutes unlawful harassment" | Describe the conduct; no legal label in an internal complaint |
| "You should file — you'll win" | Draft the account; whether to file and outcome route to an attorney |
| "He targeted me because I'm disabled" | State the facts; leave motive/inference to counsel |
| Write "I swear under penalty of perjury…" for the user | Present any attestation for the user to read, verify, and sign |
| Cite Title VII / a state code in the complaint | Keep it factual; legal framing is for an attorney/agency |
| Blend what you saw with what a coworker told you | Label first-hand vs. hearsay; keep them distinct |
| Skip the copy/submission log | Remind: keep a copy; record date, channel, confirmation # |
| Treat a threat as an HR matter only | Stop, Safety Block, call 911 if in danger, then report |

---

## Adaptations

**By channel:**
- **HR / manager email:** Keep it concise; attach the documents; request written acknowledgment.
- **Ethics/compliance hotline or portal:** Have the same narrative ready to paste; capture the ticket number.
- **Formal written form:** Map your narrative into the form's fields; keep your own full-length copy too.

**By situation/profile:**
- **Fear of retaliation:** Include the factual request to be protected from retaliation; start a `legalprep_workplace_retaliation_log.md` on the day you submit.
- **Multiple incidents over time:** Present them in date order; do not characterize them collectively as a legal "pattern."
- **Considering an agency charge:** Talk to an attorney about timing before submitting internally; pair with `legalprep_eeoc_agency_charge_preparation_organizer.md`.

---

## Related Prompts

- `legalprep_workplace_concern_documentation_organizer.md` — build the dated factual record that feeds this complaint.
- `legalprep_eeoc_agency_charge_preparation_organizer.md` — organize facts for a government-agency intake or attorney.
- `legalprep_workplace_retaliation_log.md` — log adverse actions after you submit.
- `../../employment-labor/legal_workplace_investigation_plan_and_report.md` — the employer-side investigation counterpart.
- `../../employment-labor/legal_eeoc_position_statement_drafter.md` — the employer-side agency-response counterpart.
