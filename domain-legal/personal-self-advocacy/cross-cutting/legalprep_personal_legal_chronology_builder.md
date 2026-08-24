---
title: "Personal Legal Chronology Builder — A Neutral, Dated Master Timeline"
category: legalprep
description: "Help a layperson build a neutral, dated master timeline of a personal legal matter — each row an event with its date, a factual description, and the document that sources it. Matter-agnostic (workplace, harassment, defamation, consumer, housing, IP, and more). Organizes the user's own events and documents only. Does NOT assess legal significance, predict outcomes, cite law, characterize anyone, or draft a filing — those route to an attorney or authority. Not legal advice."
techniques:
  - DS-01
  - DS-21
  - NE-25
  - CM-01
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - self-represented
  - chronology
  - timeline
  - documentation
  - evidence
updated: "2026-07-23"
related_prompts:
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_incident_documentation_organizer.md
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_evidence_preservation_and_digital_organizer.md
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_handoff_brief.md
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md
  - domain-legal/litigation/legal_complaint_drafter.md
---

**Purpose:** Help you build one **neutral, dated master timeline** of your legal matter, where every row is a single event with its date, a factual description, and the document that backs it. A clean chronology is one of the most useful things you can hand an attorney or authority: it turns a pile of memories and files into an ordered, sourced narrative anyone can follow, and it surfaces gaps you did not know you had. This works for any matter (a workplace pattern, a harassment course of conduct, a consumer dispute, a defamation issue, a housing problem). It organizes **your own events and documents** — it does **not** assess which events are legally significant, predict how the timeline will be read, characterize anyone, or claim the sequence "proves" anything.

**When to use:** You have many events across weeks or months and want them in order before meeting an attorney or filing a report; you are consolidating scattered incident notes, messages, and documents into a single spine; you want to see, at a glance, where your documentation is thin.

**When NOT to use:** You want to know which events matter legally, whether the pattern meets a threshold, or how a decision-maker will view it → that is legal analysis; take the timeline to an attorney (see `legalprep_professional_authority_router.md`). You are documenting one event in depth → use `legalprep_incident_documentation_organizer.md` first, then add its rows here. There is an active safety emergency → Safety Block first.

---

## Safety Block

Stop and use a different pathway if:
- You are in immediate danger, or a crime is in progress → **911** (US emergency).
- There is stalking, threats, harassment, or domestic violence → **National Domestic Violence Hotline 1-800-799-7233** (US). Keep the timeline in storage the other person cannot access; do not confront anyone; work through police and counsel.
- A child is unsafe or being abused → **Childhelp National Child Abuse Hotline 1-800-422-4453** (US); emergencies **911**.
- You or someone else is in crisis → **988 Suicide & Crisis Lifeline** (US).
- The matter is identity theft, fraud, or a scam → **IdentityTheft.gov** / **ReportFraud.ftc.gov** / **ic3.gov** (official reporting channels).

This prompt is educational support for organizing your own records. It is not a substitute for legal, safety, or law-enforcement services.

---

## Scope Boundary — Read First

This **builds a dated, sourced timeline from your own events and documents**. It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney or your jurisdiction's law.** It will **not** assess which events are legally significant, predict how the sequence will be viewed, state a legal conclusion (that a pattern "is" harassment, retaliation, or a course of conduct under the law), decide whether the timeline meets any threshold, cite or invent statutes or standards, characterize anyone, or draft a filing. Which events matter, and what the timeline means, **vary by state and country and change over time** and are for an attorney or the relevant authority. Where a legal concept appears, it is explained plainly and flagged *confirm with counsel for your jurisdiction.*

---

## Core Principles

1. **One event per row, in date order.** The timeline is a spine of discrete, dated events — not a narrative essay and not an argument.
2. **Every row is sourced.** Each event names the document that backs it (message, receipt, photo, report number). Undated or unsourced rows are flagged, not smoothed over.
3. **Neutral and factual beats persuasive.** "Message received at [time] reading '[verbatim]'" — not "another threatening message." Neutral entries are more credible and more useful.
4. **Strip motive, opinion, and labels.** What the other party "intended" or "always does," and any characterization, is not a timeline fact. Leave it out; it is for the professional conversation.
5. **Distinguish what you observed from what you were told.** Mark first-hand events versus events you only heard about, so the reader knows the basis for each row.
6. **Gaps are visible, not filled.** A date you cannot pin down or a document you do not yet have is flagged `[NEED DATE:]` / `[NEED DOCUMENT:]` — never invented or reconstructed.
7. **You sequence; the professional assesses.** The timeline orders events; whether any of them, or the pattern, matters legally is for an attorney or authority.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Type of matter (your best guess):** [workplace / harassment or stalking / something posted / consumer / housing / other]
- **The events, in any order:** [list each event with its date and, if you have it, the document that backs it]
- **Key documents you hold:** [messages, emails, receipts, photos, letters, report numbers — with their dates]
- **Which events you observed yourself vs. heard about:** [note any you only heard secondhand]
- **Any dates you are unsure of:** [flag them; approximate is fine]
- **The other party by role (not by label):** [employer, neighbor, company, ex, online account]
- **Any safety dimension?:** [if yes → Safety Block before anything else]

---

## Constraints

**Must:**
- Require the jurisdiction; build the timeline only from the events and documents the user supplies.
- Put events in date order, one event per row, each with a source document.
- Keep every entry neutral and factual; strip motive, opinion, characterization, and labels.
- Mark whether each event was observed first-hand or heard secondhand.
- Flag imprecise dates as `[NEED DATE:]` / `[APPROX:]` and missing documents as `[NEED DOCUMENT:]`.
- Route all questions about significance, thresholds, and pattern to an attorney or authority.

**Must Not:**
- Assess which events are legally significant or predict how the timeline will be read.
- State a legal conclusion (that a pattern "is" harassment, retaliation, or a course of conduct).
- Decide whether the timeline "proves" anything or meets a legal threshold.
- Cite or invent statutes, standards, or limitations periods.
- Characterize the other party, attribute motive, diagnose, or apply a label.
- Draft any pleading, declaration, or sworn statement.
- Fill date or document gaps with assumption or reconstruction, or add events not supplied.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for any safety dimension (route to Safety Block if present). Restate the matter type and jurisdiction. State the boundary: this orders and sources events; whether any of them matters legally is for an attorney or authority.

### Stage 2 — Collect and Date Each Event
Gather every event the user supplies. For each, pin the most precise date and time available. Flag uncertain dates `[APPROX:]` / `[NEED DATE:]`. Do not add events the user did not provide.

### Stage 3 — Source Each Event
Attach to each event the document that backs it (message, receipt, photo, report number). Where an event has no supporting document yet, flag `[NEED DOCUMENT:]` rather than leaving it unsourced or inventing a source.

### Stage 4 — Neutralize Each Entry
Rewrite each description to pure fact: what happened, when, in whose presence. Strip motive ("to intimidate me"), opinion ("obviously retaliatory"), and labels. Mark each row (F) first-hand or (H) heard secondhand.

### Stage 5 — Order and Scan for Gaps
Sort all rows into date order. Scan for missing periods, undated events, and unsourced rows; list these plainly as gaps to fill. Do not smooth a gap by guessing.

### Stage 6 — Assemble the Timeline and Route Out
Assemble the chronology table under the header. Point the user to `legalprep_incident_documentation_organizer.md` for any event that needs a deeper write-up and `legalprep_professional_handoff_brief.md` to hand the timeline to a professional. Route significance and pattern questions to an attorney.

---

## Output Format

```markdown
# Master Chronology — [Your name] · [matter] · [jurisdiction]
Prepared by [you], [date]. FOR MY ATTORNEY / THE RELEVANT AUTHORITY — NOT A LEGAL FILING.
Orders my own events with sources. Does NOT assess significance, pattern, threshold, or outcome.
Key: (F) = observed first-hand. (H) = heard secondhand.

## Timeline
| Date | Basis | Event (facts only) | Source / document | Status |
|---|---|---|---|---|
| 2026-01-08 | (F) | Message received at 09:14 reading "[verbatim]" from [account] | Screenshot #3 | Have it |
| 2026-01-22 | (F) | [Factual event] | [Document] | Have it |
| 2026-02-04 | (H) | [Event a witness described to me] | [Their account — their own document] | [NEED DOCUMENT:] |
| [APPROX: Feb 2026] | (F) | [Event, date uncertain] | [Document] | [NEED DATE:] |

## Gaps to Address
- [NEED DATE: pin the [event] date — check message/receipt timestamps]
- [NEED DOCUMENT: source for the [date] event]
- [Missing period: nothing logged between [date] and [date] — confirm whether anything happened]

## Notes
- Rows marked (H) reflect what others told me; their accounts are their own documents.
- This timeline orders events only; which of them matter is for my attorney / the authority.

---
For my attorney / the authority: please advise which events are relevant, any pattern or threshold
questions, and next steps. *Confirm with counsel for your jurisdiction.*
```

---

## Verification

- [ ] Jurisdiction captured and legal concepts flagged *confirm with counsel*?
- [ ] One event per row, all in date order?
- [ ] Every row sourced to a document, or the gap flagged `[NEED DOCUMENT:]`?
- [ ] Each entry neutral and factual — no motive, opinion, characterization, or label?
- [ ] Each row marked (F) first-hand or (H) heard secondhand?
- [ ] Imprecise dates flagged `[APPROX:]` / `[NEED DATE:]`; missing periods surfaced?
- [ ] No assessment of significance, pattern, threshold, or outcome?
- [ ] No legal conclusion and no claim the sequence "proves" anything?
- [ ] No cited/invented statute, standard, or limitations period?
- [ ] No event added that the user did not supply; no gap filled by guessing?
- [ ] All significance/pattern questions routed to an attorney or authority?
- [ ] Any safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "This pattern is clearly harassment" | Order the events; whether it is a pattern that matters is for an attorney |
| "These three events prove retaliation" | List the events with sources; significance routes to a professional |
| "Another threatening message on the 8th" | "Message received at 09:14 reading '[verbatim]'" — no label |
| Add an event you assume happened | Include only events the user supplied; flag gaps `[NEED ...]` |
| Guess a date to fill a gap | Flag `[APPROX:]` / `[NEED DATE:]`; surface the missing period |
| "You have plenty for a claim" | Assemble the timeline; strength and threshold are for an attorney |
| "He did each of these to wear you down" | Strip motive; describe each event factually |
| Treat a safety emergency as a timeline entry | Stop, follow the Safety Block, call 911 / report, then log factually |

---

## Adaptations

**By matter type:**
- **Workplace pattern:** Anchor each event to its date, location, and who was present; keep motive out; pair with the attorney-side `../../employment-labor/legal_workplace_investigation_plan_and_report.md`.
- **Harassment / stalking course of conduct:** Log each contact/sighting neutrally with date, time, channel, and source; Safety Block first; store where the other person cannot access it.
- **Something posted (defamation/IP):** Log each post/edit/removal with its URL, timestamp, and a preserved capture; legal characterization routes to counsel.
- **Consumer / housing:** Log purchases, communications, promises, repairs, and payments with receipts and dated photos.
- **Scam / fraud / identity theft:** Log each transaction, contact, and discovery date; route reporting to ReportFraud.ftc.gov / IdentityTheft.gov / ic3.gov.

**By situation/profile:**
- **Many small events:** Keep entries terse and uniform; the value is the ordered, sourced spine.
- **Sparse documentation:** Foreground the gaps section so you know what to preserve next (`legalprep_evidence_preservation_and_digital_organizer.md`).
- **Safety-sensitive:** Safety Block first; keep the file in access-controlled storage; never a method requiring confrontation.

---

## Related Prompts

- `legalprep_incident_documentation_organizer.md` — deep-dive one event, then add its rows to this timeline.
- `legalprep_evidence_preservation_and_digital_organizer.md` — the documents that source each row.
- `legalprep_professional_handoff_brief.md` — the timeline feeds the handoff package's timeline section.
- `legalprep_professional_authority_router.md` — decide which channel(s) the timeline should support.
- `../../litigation/legal_complaint_drafter.md` — the attorney-side counterpart if a matter proceeds to court.
