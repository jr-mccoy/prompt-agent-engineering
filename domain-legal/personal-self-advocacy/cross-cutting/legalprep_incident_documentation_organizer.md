---
title: "Incident Documentation Organizer — Turn a Recalled Event into a Factual Record"
category: legalprep
description: "Help a layperson turn a single recalled incident — a harassing message, a workplace event, a scam call, a stalking sighting, a confrontation — into a clean, structured factual write-up: date/time/location, who was present, first-hand observations separated from hearsay and opinion, supporting documents, and witnesses. Matter-agnostic; one incident per document. Organizes the user's own recollection only. Does NOT assess legal significance, predict outcomes, cite law, characterize anyone, or draft a filing — those route to an attorney or authority. Not legal advice."
techniques:
  - ST-03
  - DS-01
  - NE-25
  - CM-01
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - self-represented
  - incident
  - documentation
  - witness
  - evidence
updated: "2026-07-23"
related_prompts:
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_personal_legal_chronology_builder.md
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_evidence_preservation_and_digital_organizer.md
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_handoff_brief.md
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md
  - domain-legal/litigation/legal_complaint_drafter.md
---

**Purpose:** Help you turn a recalled incident into a structured, factual write-up that an attorney can use, an authority can act on, and a decision-maker can credit. The write-up captures the date and time, the location, who was present, what you observed directly (first-hand), what you heard from others (hearsay — clearly labeled), supporting documents, and potential witnesses. The single most important skill this prompt teaches is **separating what you saw and heard yourself from what someone else told you** — those two categories are treated very differently, and mixing them damages credibility. This works for any kind of matter (a harassing message, a workplace event, a scam call, a stalking sighting, a consumer dispute). It organizes **your own recollection** — it does **not** assess the legal significance of the incident, predict how it will be viewed, or tell you whether it "proves" anything.

**When to use:** You recall a specific incident and want to write it down while it is fresh, or organize an older recollection before contacting an attorney, HR, the police, a platform, or an agency. Use one copy of this template per incident.

**When NOT to use:** You want to know whether the incident is legally significant, meets a legal threshold, or how it affects your options → that is legal analysis; take the write-up to an attorney or the relevant authority (see `legalprep_professional_authority_router.md`). You want to build a full timeline across many events → use `legalprep_personal_legal_chronology_builder.md`. You need to preserve and inventory the underlying evidence → use `legalprep_evidence_preservation_and_digital_organizer.md`. There is an active safety emergency → Safety Block first.

---

## Safety Block

Stop and use a different pathway if:
- You are in immediate danger, or a crime is in progress → **911** (US emergency).
- There is stalking, threats, harassment, or domestic violence → **National Domestic Violence Hotline 1-800-799-7233** (US). Keep records securely; work through police and counsel; do not confront anyone.
- A child is being abused or is unsafe → **Childhelp National Child Abuse Hotline 1-800-422-4453** (US); emergencies **911**.
- You or someone else is in crisis → **988 Suicide & Crisis Lifeline** (US).
- The incident is identity theft, fraud, or a scam → **IdentityTheft.gov** / **ReportFraud.ftc.gov** / **ic3.gov** (official reporting channels).

This prompt is educational support for organizing your own records. It is not a substitute for legal, safety, or law-enforcement services.

---

## Scope Boundary — Read First

This **structures a factual incident record from your own recollection and documents**. It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney or your jurisdiction's law.** It will **not** assess the legal significance of the incident, predict whether it will be found credible or relevant, state a legal conclusion (that something "is" harassment, a threat, fraud, or a crime), cite or invent standards or cases, characterize anyone, or draft any filing or report. Whether an incident rises to a legally relevant threshold — and what to do with the write-up — **vary by state and country and change over time** and are entirely for an attorney or the relevant authority. Where a legal concept (hearsay, corroboration) appears, it is explained in plain language and flagged *confirm with counsel for your jurisdiction.*

---

## Core Principles

1. **First-hand and hearsay are two different categories — always label them.** "I saw [X]" and "A coworker told me she saw [X]" are not the same. The record must separate them so an attorney or authority knows which is which.
2. **One incident per document.** Do not combine multiple events into one write-up; each incident needs to stand on its own.
3. **Describe what you observed; do not interpret it.** "A message reading '[verbatim]' arrived at 5:07 PM from [account]" — not "he was clearly threatening me." Observed fact is credited; characterization undermines credibility.
4. **Date and time as precisely as possible.** Contemporaneous records (a message timestamp, a photo's metadata) anchor the incident to a specific moment and carry far more weight than "sometime last month."
5. **Strip opinion, emotion, and motive attribution.** What the other party "intended," "was trying to do," or "always does" is not first-hand fact. Strip it; save it for the professional conversation.
6. **Witnesses are named, not scripted.** Note who was present and what they could have observed — not a full transcript of what they said. A witness's statement is their own document.
7. **You document; the professional or authority assesses.** Supporting documents anchor the record, but whether the incident matters legally is for an attorney or that authority — never for this write-up to decide.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Type of matter (your best guess):** [workplace / harassment or stalking / scam or fraud / something posted / consumer / other]
- **Date and time of incident:** [as precisely as possible; "approximately [date]" if uncertain]
- **Location or channel:** [physical address, or the platform/phone/email where it happened]
- **What you observed (first-hand only):** [what you saw, heard directly, or received yourself]
- **What others told you (hearsay — label clearly):** [who said what, to you, after the fact]
- **Who was present or involved:** [names/initials/roles — you, other party, witnesses]
- **Documents you have from around this time:** [screenshots, messages, call logs, receipts, photos with timestamps, report numbers]
- **Potential witnesses:** [name/initials/role + what they could have observed]
- **Any safety dimension?:** [if yes → Safety Block before anything else]

---

## Constraints

**Must:**
- Require the jurisdiction; build the record from only the facts the user supplies.
- Label every item of information as either (F) first-hand observation or (H) heard-from-others/hearsay.
- Date and time-stamp the incident as precisely as the user's information allows.
- Flag imprecise dates as `[NEED DATE:]` or `[APPROX: ...]`.
- Keep all description factual; strip motive, opinion, and characterization.
- List supporting documents and witnesses; flag missing items as `[NEED DOCUMENT:]`.
- Route all questions about legal significance and next steps to an attorney or the relevant authority.

**Must Not:**
- Assess the legal significance of the incident or predict how it will be weighed.
- State a legal conclusion (that something "is" harassment, a threat, fraud, defamation, or a crime).
- Characterize the other party, attribute motive, diagnose, or apply a label.
- Present hearsay as first-hand observation or merge the two categories.
- Claim the record "proves" any legal conclusion.
- Draft any declaration, affidavit, sworn statement, report, or pleading.
- Fill factual gaps with assumption, reconstruction, or inference, or coach exaggeration.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for any safety dimension (route to Safety Block if present). Restate the matter type and jurisdiction. Confirm the boundary: this structures the incident record; what it means legally is for an attorney or authority.

### Stage 2 — Establish the Anchor Facts
Confirm the incident date, time (as precise as available), and location or channel. Confirm who was present or involved. Flag any uncertainty: `[APPROX DATE:]`, `[NEED TIME:]`, `[NEED LOCATION DETAIL:]`.

### Stage 3 — Separate First-Hand from Hearsay
Work through the user's account. Tag each piece of information:
- **(F)** = First-hand: you were present and directly observed, heard, or received this.
- **(H)** = Hearsay: someone else told you this; they observed it but you did not.

If the user conflates the two (very common), gently separate them and return both labeled versions.

### Stage 4 — Strip Opinion and Characterization
Rewrite any sentence that contains motive attribution ("he did this to scare me"), opinion ("she was obviously lying"), or a label ("he is a predator"). Return each in factual form: what was observed, not what it meant.

### Stage 5 — List Supporting Documents and Witnesses
List every document created around the time of the incident (screenshots, message timestamps, call logs, receipts, photos with metadata, report numbers). Flag items that should exist but are not yet obtained. List each potential witness with what they could have directly observed.

### Stage 6 — Package and Route Out
Assemble the full incident record under the header. Note that this is one incident and belongs in the master chronology (`legalprep_personal_legal_chronology_builder.md`) and evidence index (`legalprep_evidence_preservation_and_digital_organizer.md`). Route legal-significance questions to an attorney and reporting to the right channel (`legalprep_professional_authority_router.md`).

---

## Output Format

```markdown
# Incident Record — [Your name] · [matter type] · [jurisdiction]
Incident date: [date/time]. Location/channel: [description].
Compiled by [you], [date of compilation]. FOR MY ATTORNEY / THE RELEVANT AUTHORITY — NOT A LEGAL FILING.
Does NOT assess legal significance or outcome.
Key: (F) = First-hand observation. (H) = Heard from others / hearsay — labeled as such.

## Anchor Facts
- Date: [YYYY-MM-DD] [or APPROX: month/year if uncertain]
- Time: [HH:MM] [or NEED TIME:]
- Location / channel: [address, platform, phone, or email]
- Who was present / involved: [you; other party — role/initials; witnesses — initials or role]

## What I Observed Directly (First-Hand)
1. (F) [Factual, specific, stripped of opinion. What you saw, heard, or received yourself.]
2. (F) [...]

## What Others Told Me (Hearsay — labeled)
1. (H) [Person's initials/role] told me: "[What they said, as close to verbatim as possible]." Date told: [date].
2. (H) [...]

## Supporting Documents (from around this time)
| Item | Date / Timestamp | What It Captures | Storage Location | Status |
|---|---|---|---|---|
| Screenshot of [message/post] | [date/time visible in capture] | [Factual description of what is visible] | [folder/device] | Have it |
| Call log / voicemail | [date/time] | [Number shown; length; that a message exists] | [phone/export] | Have it |
| [Receipt / letter / report] | [date] | [Factual description] | [location] | [NEED DOCUMENT: to obtain] |

## Potential Witnesses
| Person (initials/role) | What they could have observed directly | Contact status |
|---|---|---|
| [Coworker — initials] | Was present at [location/channel] during [time]; could describe [what they observed] | [Known to me / unknown if willing] |

## Gaps to Address
- [NEED DATE: approximate incident time — check message/call timestamps from that day]
- [NEED DOCUMENT: [record] from [source] on or near [date]]

---
For my attorney / the authority: please advise how to use this record and any next steps.
*Confirm with counsel for your jurisdiction.*
```

---

## Verification

- [ ] Jurisdiction captured and legal concepts flagged *confirm with counsel*?
- [ ] Incident anchored to a specific date, time, and location/channel (or flagged)?
- [ ] Every item of information labeled (F) first-hand or (H) hearsay?
- [ ] First-hand and hearsay sections kept separate throughout?
- [ ] No opinion, motive attribution, label, or characterization in any entry?
- [ ] No legal conclusion and no claim that the record "proves" anything?
- [ ] Supporting documents listed with dates and storage locations; gaps flagged?
- [ ] Potential witnesses listed with what they could have observed (not scripted statements)?
- [ ] No declaration, affidavit, report, or pleading drafted?
- [ ] All legal-significance and next-step questions routed to an attorney or authority?
- [ ] Any safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "He was clearly trying to intimidate you" | (F) "A message reading '[verbatim]' arrived at [time]" — motive is for a professional |
| Mix first-hand and hearsay in one paragraph | Label every item (F) or (H); keep sections separate |
| "My coworker saw it — he's harassing everyone" | (H) "Coworker [initials] told me she observed [description]" — her account is her own document |
| "This proves a pattern of harassment" | Compile the incident; pattern and legal significance route to a professional |
| Reconstruct a detail you are unsure about | Flag `[UNCERTAIN:]` or `[NEED TO CONFIRM:]`; do not fill with inference |
| Draft the write-up as a sworn declaration | Label it FOR MY ATTORNEY / AUTHORITY — NOT A FILING; sworn statements route out |
| Include your emotional reaction as a fact | Strip emotional language; describe observable facts only |
| Treat a safety emergency as mere documentation | Stop, follow the Safety Block, call 911 / report, then document |

---

## Adaptations

**By incident type:**
- **Harassing or threatening message:** Anchor to the message timestamp and sender/account; quote verbatim; preserve the original via `legalprep_evidence_preservation_and_digital_organizer.md`; do not label it a "threat" — that is for a professional.
- **Workplace event:** Note the policy context factually (time, location, who was present); keep motive out; witnesses are coworkers who observed, not who "agree with you."
- **Scam or fraud call:** Anchor to the call log/number and time; note what was said and any money/data requested; route reporting to ReportFraud.ftc.gov / ic3.gov.
- **Stalking sighting:** Safety Block first; anchor date/time/location and what was directly observed; do not confront; preserve any recording lawfully — *confirm what is lawful with counsel.*
- **Third-party account event:** The third party's account is entirely in the (H) column; note them as a potential witness; do not compose their statement.

**By situation/profile:**
- **High conflict:** Keep every entry tightly sourced; strip adjectives; route any response through a professional.
- **Digital-only incident:** Capture full context (URL, account handle, timestamp) at capture time; the screenshot is the anchor.
- **Safety incident:** Safety Block first; after safety is addressed, document factually and route out.

---

## Related Prompts

- `legalprep_personal_legal_chronology_builder.md` — each incident record adds one or more rows to the master timeline.
- `legalprep_evidence_preservation_and_digital_organizer.md` — each incident's supporting documents become entries in the preserved-evidence index.
- `legalprep_professional_handoff_brief.md` — incident records feed the evidence section of the handoff package.
- `legalprep_professional_authority_router.md` — decide which channel(s) the incident should be routed to.
- `../../litigation/legal_complaint_drafter.md` — the attorney-side counterpart if a matter proceeds to court.
