---
title: "Incident Documentation Organizer (Turn a Recalled Event into a Factual Record)"
category: legalprep
description: "Help a self-represented or self-organizing family-law litigant turn a recalled incident into a clean, structured factual write-up — date/time, location, who was present, first-hand observations separated from hearsay and opinion, supporting documents, and witnesses. Teaches the critical distinction between first-hand observation and heard-from-others accounts. Organizes the user's own recollection only. Not legal advice."
techniques:
  - ST-03
  - DS-01
  - NE-25
  - CM-01
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - family-law
  - self-represented
  - divorce
  - custody
  - incident
  - documentation
  - witness
updated: "2026-06-05"
related_prompts:
  - domain-legal/family-self-advocacy/legalprep_case_chronology_builder.md
  - domain-legal/family-self-advocacy/legalprep_evidence_inventory_organizer.md
  - domain-legal/family-self-advocacy/legalprep_witness_and_source_map.md
  - domain-legal/family-self-advocacy/legalprep_attorney_handoff_brief.md
  - domain-parenting/caregiver-facing/custody/parenting_custody_changed_circumstances_organizer.md
---

**Purpose:** Help you turn a recalled incident into a structured, factual write-up that your attorney can use and a court can credit. The write-up captures the date and time, location, who was present, what you observed directly (first-hand), what you heard from others (hearsay — clearly labeled), supporting documents, and potential witnesses. The single most important skill this prompt teaches is **separating what you saw and heard yourself from what someone else told you** — courts treat those two categories very differently, and mixing them damages credibility. This organizes **your own recollection** — it does **not** assess the legal significance of the incident, predict how a court will view it, or tell you whether it "proves" anything.

**When to use:** You recall a specific incident — a missed pick-up, a witnessed event, an altercation, a medical emergency, a child's disclosure — and want to write it down while it is fresh, or organize an older recollection before meeting with your attorney. Use one copy of this template per incident.

**When NOT to use:** You want to know whether the incident is legally significant, meets a legal threshold, or how it affects your case → that is legal analysis; take the write-up to your attorney. You want to compile an entire message thread → use `legalprep_communication_record_compiler.md`. You want to build a full timeline → use `legalprep_case_chronology_builder.md`. There is an active safety emergency → Safety Block first.

---

## Safety Block

Stop and use a different pathway if:
- There is domestic violence, threats, stalking, or a protective/restraining order → National Domestic Violence Hotline 1-800-799-7233 (US). Keep records securely; work through counsel/advocate; do not confront anyone.
- A child is being abused or is unsafe in either home → Childhelp National Child Abuse Hotline 1-800-422-4453 (US); emergencies 911. Report and route to your attorney immediately — document after safety is addressed.
- You or a child is in crisis → 988 Suicide & Crisis Lifeline (US).

This prompt is educational support for organizing your own records. It is not a substitute for legal, safety, or clinical services.

---

## Scope Boundary — Read First

This **structures a factual incident record from your own recollection and documents**. It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney or your jurisdiction's family law.** It will **not** assess the legal significance of the incident, predict whether a court will find it credible or relevant, cite or invent standards or cases, characterize the other party, or draft any filing. Whether an incident rises to a legally relevant threshold — and what to do with the write-up — **vary by state and country and change over time** and are entirely for your attorney. Where a legal concept (hearsay, foundation, corroboration) appears, it is explained in plain language and flagged *confirm with counsel for your jurisdiction.*

---

## Core Principles

1. **First-hand and hearsay are two different categories — always label them.** "I saw [X]" and "My neighbor told me she saw [X]" are not the same. The incident record must separate them clearly so your attorney and the court know which is which.
2. **One incident per document.** Do not combine multiple events into one write-up. Your attorney needs to assess each incident separately.
3. **Describe what you observed; do not interpret it.** "Child arrived with a bruise on his left forearm, approximately 2 inches, photographed at 5:07 PM" — not "he was clearly abusing the child." Courts credit observed fact; characterization undermines credibility.
4. **Date and time as precisely as possible.** Contemporaneous records (photos, texts sent at the time) anchor the incident to a specific moment and carry far more weight than "sometime in the fall."
5. **Strip opinion, emotion, and motive attribution.** What the other party "intended," "was trying to do," or "always does" is not first-hand fact. Strip it; save it for the attorney conversation.
6. **Witnesses are named, not quoted extensively.** The write-up notes who was present and what they could have observed — not a full transcript of what they said. A witness's statement is their own document.
7. **Supporting documents anchor the record.** Photos, texts sent around the time of the incident, medical records, school records, police or report numbers — each is listed and stored. An unsupported recollection is weaker than one tied to a contemporaneous document.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Date and time of incident:** [as precisely as possible; "approximately [date]" if uncertain]
- **Location:** [address or description]
- **What you observed (first-hand only):** [describe in your own words — what you saw, heard directly, physically witnessed]
- **What others told you (hearsay — label clearly):** [who said what, to you, after the fact]
- **Who was present:** [names/initials — you, other party, children, third parties]
- **Documents you have from around this time:** [photos with timestamps, texts sent that day, medical/school records, police report number, 911 call record]
- **Potential witnesses:** [name/initials + what they could have observed]
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
- Route all questions about legal significance, admissibility, and strategy to the attorney.

**Must Not:**
- Assess the legal significance of the incident or predict how a court will weigh it.
- Characterize the other party, attribute motive, or make inferences about intent.
- Present hearsay as first-hand observation or merge the two categories.
- Claim the record "proves" abuse, neglect, or any other legal conclusion.
- Draft any declaration, affidavit, sworn statement, or pleading.
- Fill factual gaps with assumption, reconstruction, or inference.
- Coach the user to exaggerate, embellish, or add details that were not observed.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Task
Screen for any safety dimension (route to Safety Block if present). Restate the matter type and jurisdiction. Confirm the boundary: this structures the incident record; what it means legally is for the attorney.

### Stage 2 — Establish the Anchor Facts
Confirm the incident date, time (as precise as available), and location. Confirm who was present. Flag any uncertainty: `[APPROX DATE:]`, `[NEED TIME:]`, `[NEED LOCATION DETAIL:]`.

### Stage 3 — Separate First-Hand from Hearsay
Work through the user's account. Tag each piece of information:
- **(F)** = First-hand: you were present and directly observed or heard this.
- **(H)** = Hearsay: someone else told you this; they were present but you were not.

If the user conflates the two (very common), gently separate them and return both labeled versions.

### Stage 4 — Strip Opinion and Characterization
Rewrite any sentence that contains motive attribution ("he did this to scare me"), opinion ("she was obviously lying"), or characterization ("his parenting is dangerous"). Each such sentence is returned in factual form: what was observed, not what it meant.

### Stage 5 — List Supporting Documents and Witnesses
List every document that was created around the time of the incident (photos with timestamps, texts sent that day, medical records, police reports). Flag items that should exist but are not yet obtained. List each potential witness with what they could have directly observed.

### Stage 6 — Package and Close
Assemble the full incident record under the handoff header. Note that this is one incident and it belongs in the master chronology (`legalprep_case_chronology_builder.md`) and evidence index (`legalprep_evidence_inventory_organizer.md`). Route legal significance questions to counsel.

---

## Output Format

```markdown
# Incident Record — [Your name] · [matter type] · [jurisdiction]
Incident date: [date/time]. Location: [description].
Compiled by [you], [date of compilation]. FOR YOUR ATTORNEY — NOT A LEGAL FILING.
Does NOT assess legal significance, admissibility, or outcome.
Key: (F) = First-hand observation. (H) = Heard from others / hearsay — labeled as such.

## Anchor Facts
- Date: [YYYY-MM-DD] [or APPROX: month/year if uncertain]
- Time: [HH:MM] [or NEED TIME:]
- Location: [address or description]
- Who was present: [you; other party; children — initials; third parties — initials or role]

## What I Observed Directly (First-Hand)
1. (F) [Factual, specific, stripped of opinion. What you saw, heard, or physically witnessed yourself.]
2. (F) [...]

## What Others Told Me (Hearsay — labeled)
1. (H) [Person's initials/role] told me: "[What they said, as close to verbatim as possible]." Date told: [date].
2. (H) [...]

## Supporting Documents (from around this time)
| Item | Date / Timestamp | What It Captures | Storage Location | Status |
|---|---|---|---|---|
| Photo of [description] | [date/time from EXIF or filename] | [Factual description of what is visible] | [folder/device] | Have it |
| Text sent to [person] | [date/time] | [Briefly — topic of message at the time] | [screenshots folder] | Have it |
| [Medical/police/school record] | [date] | [Factual description] | [location] | [NEED DOCUMENT: to request from provider] |

## Potential Witnesses
| Person (initials/role) | What they could have observed directly | Contact status |
|---|---|---|
| [Neighbor — initials] | Was present at [location] during [time]; could describe [what they observed] | [Known to me / unknown if willing] |

## Gaps to Address
- [NEED DATE: approximate incident time — check texts/photos from that day]
- [NEED DOCUMENT: medical record from [provider] visit on or near [date]]

---
For my attorney: please advise on how to use this record, whether any entries
raise hearsay or foundation concerns, and next steps.
*Confirm with counsel for your jurisdiction.*
```

---

## Verification

- [ ] Jurisdiction captured and legal concepts flagged *confirm with counsel*?
- [ ] Incident anchored to a specific date, time, and location (or flagged)?
- [ ] Every item of information labeled (F) first-hand or (H) hearsay?
- [ ] First-hand and hearsay sections kept separate throughout?
- [ ] No opinion, motive attribution, or characterization in any entry?
- [ ] No claim that the record "proves" a legal conclusion?
- [ ] Supporting documents listed with dates and storage locations; gaps flagged?
- [ ] Potential witnesses listed with what they could have directly observed (not quoted statements)?
- [ ] No declaration, affidavit, or sworn statement drafted?
- [ ] All legal-significance, admissibility, and strategy questions routed to the attorney?
- [ ] Any safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "She was clearly trying to alienate the child" | (F) "Child stated [verbatim quote] at [time]" — motive is for counsel |
| Mix first-hand and hearsay in one paragraph | Label every item (F) or (H); keep sections separate |
| "My sister saw the whole thing — he was abusive" | (H) "Sister [initials] told me she observed [description]" — her account is her own document |
| "This incident proves a pattern of neglect" | Compile the incident; pattern analysis routes to counsel |
| Reconstruct a detail you are not sure about | Flag `[UNCERTAIN:]` or `[NEED TO CONFIRM:]`; do not fill with inference |
| Draft the incident write-up as a declaration | Label it FOR YOUR ATTORNEY — NOT A FILING; sworn statements route to counsel |
| Include your emotional state as a fact | Strip emotional language; describe observable facts only |
| Treat a safety incident as mere documentation | Stop, follow Safety Block, report as required, then document with counsel |

---

## Adaptations

**By incident type:**
- **Missed or disrupted pick-up:** Anchor to the scheduled time from the parenting plan/order; list texts or app messages sent at the time; note who else observed the missed exchange.
- **Child's disclosure:** Quote the child's words as precisely as possible, with the setting and time; note that a child's out-of-court statement is hearsay and flag it accordingly for counsel.
- **Medical or injury:** Attach photos with EXIF timestamps; reference the medical provider visit date; let the medical record speak; do not diagnose cause.
- **Property or financial event:** Note what was present/absent, when discovered, with any financial record that anchors the observation.
- **Third-party witness event:** The third party's account is entirely in the (H) column; note them as a potential witness; do not compose their statement.

**By situation/profile:**
- **High conflict:** Keep every entry tightly sourced; strip adjectives; work through counsel on any response.
- **Child with special needs:** Document observable behavioral changes factually (e.g., "Child arrived from other parent's home with three unanswered school emails on [date]") — not characterizations of cause.
- **Safety incident:** Safety Block first; after safety is addressed, use this template to document factually and route to counsel.

---

## Related Prompts

- `legalprep_case_chronology_builder.md` — each incident record adds one or more rows to the master timeline.
- `legalprep_evidence_inventory_organizer.md` — each incident record and its supporting documents become entries in the exhibit index.
- `legalprep_witness_and_source_map.md` — the witnesses listed here are mapped to corroborating facts in the witness/source map.
- `legalprep_attorney_handoff_brief.md` — incident records feed the evidence section of the handoff package.
- `domain-parenting/caregiver-facing/custody/parenting_custody_changed_circumstances_organizer.md` — for organizing a series of incidents into a changed-circumstances record for post-order modification work.
