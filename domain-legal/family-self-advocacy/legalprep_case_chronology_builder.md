---
title: "Case Chronology Builder — A Neutral, Dated Timeline of Your Marriage and the Disputed Events"
category: legalprep
description: "Help a self-represented or self-organizing family-law litigant build a master dated chronology of their marriage, separation, and disputed events — each row a date, factual event, and source document. Strips motive and editorializing; flags gaps; produces a clean timeline the attorney or court can use. Organizes the user's own information only. Not legal advice."
techniques:
  - DS-01
  - ST-03
  - ST-02
  - CM-01
  - NE-25
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - family-law
  - self-represented
  - divorce
  - custody
  - chronology
  - timeline
  - documentation
updated: "2026-06-05"
related_prompts:
  - domain-legal/family-self-advocacy/legalprep_attorney_handoff_brief.md
  - domain-legal/family-self-advocacy/legalprep_evidence_inventory_organizer.md
  - domain-legal/family-self-advocacy/legalprep_incident_documentation_organizer.md
  - domain-legal/family-self-advocacy/legalprep_witness_and_source_map.md
  - domain-legal/divorce/legal_divorce_intake_and_case_assessment.md
  - domain-parenting/caregiver-facing/custody/parenting_custody_changed_circumstances_documentation_organizer.md
---

**Purpose:** Help you build one clean, neutrally worded, dated chronology of your case — a master timeline of your relationship, separation, and the events that are in dispute. Each row names what happened, when it happened, and the document that backs it. It strips motive language and editorializing so what remains is a factual record that is useful to your attorney and credible to a court. It organizes **your own information** — it does **not** assess your case, predict outcomes, tell you which events "matter" legally, or claim your timeline "proves" anything. Those are your attorney's job.

**When to use:** You are preparing to meet your attorney and want a single, organized timeline to give them; you have dates, records, and recollections scattered across texts, emails, and notes and need them in one place; you are assembling an evidence package and need the chronology layer; you need to flag where your timeline has gaps before paying counsel to chase them.

**When NOT to use:** You want to know which events are legally significant, what the statute of limitations is, or how the timeline affects your rights → that is legal advice; ask your attorney (see `legalprep_attorney_consultation_question_builder.md`). You want to draft a declaration or sworn statement → route to your attorney. There is an active safety emergency → Safety Block first; the timeline supports but does not replace protective action.

---

## Safety Block

Stop and use a different pathway if:
- There is domestic violence, threats, stalking, or a protective/restraining order → National Domestic Violence Hotline 1-800-799-7233 (US). Keep records securely; work through counsel/advocate; do not confront anyone.
- A child is being abused or is unsafe in either home → Childhelp National Child Abuse Hotline 1-800-422-4453 (US); emergencies 911. Report and route to your attorney immediately.
- You or a child is in crisis → 988 Suicide & Crisis Lifeline (US).

This prompt is educational support for organizing your own records. It is not a substitute for legal, safety, or clinical services.

---

## Scope Boundary — Read First

This **builds a chronology from your own information**. It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney or your jurisdiction's family law.** It will **not** predict outcomes, assess which events are legally significant, cite or invent statutes or cases, tell you what to file, or claim your timeline "proves" anything. Family-law standards and procedure **vary by state and country and change over time.** Where a legal concept appears, it is explained in plain language and flagged *confirm with counsel for your jurisdiction.* Decisions about which events matter and how to use the chronology belong to you and your attorney.

---

## Core Principles

1. **One fact per row, one row per date.** A timeline is a sequence of events, not a narrative argument. Keep each entry tight: what happened, when, and what document backs it.
2. **Every fact dated and sourced.** An undated assertion is not a timeline entry. If you do not have a date, flag it `[NEED DATE:]`; if you do not have a source, flag it `[NEED DOCUMENT:]`.
3. **Neutral language only.** "Other party moved out of marital residence on [date]" — not "he abandoned us." Courts read both versions; only one looks credible.
4. **Strip motive and characterization.** What someone did belongs in the record. Why you believe they did it does not. Save that conversation for your attorney.
5. **Gaps are evidence of what to find, not invitation to fill.** A visible gap in the timeline is a task list for you and your attorney, not a blank to fill with assumption.
6. **Sub-timelines by category.** One master sequence plus sub-timelines by category (relationship milestones, custody/parenting events, financial events, legal filings) makes the record easier to use.
7. **Courts credit contemporaneous documentation over memory.** The closer in time a record was made to the event, the more weight it carries. Note which entries are backed by contemporaneous documents versus reconstructed from memory.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Matter type:** [divorce / custody / both]
- **Marriage / relationship start date:** [as known]
- **Separation date (if applicable):** [as known, or "approximately — see notes"]
- **Children's initials + ages (if applicable):** [optional — use initials only]
- **Key events in your own words:** [paste a list, a narrative, or a set of notes — include dates where known]
- **Source documents you can attach or reference:** [list — e.g., marriage certificate, lease, bank statement, emails, school records]
- **Key gaps you are already aware of:** [e.g., "I don't know the exact date we opened the joint account"]
- **Any safety dimension?:** [if yes → Safety Block]

---

## Constraints

**Must:**
- Require the jurisdiction; use only the facts the user supplies.
- Keep every entry neutral, factual, and dated; source each entry.
- Flag every missing date as `[NEED DATE:]` and every missing document as `[NEED DOCUMENT:]`.
- Distinguish contemporaneous documents from reconstructed memory.
- Explain any legal term in plain language and flag *confirm with counsel.*
- Route every "which events matter" / strategy / outcome question to the attorney.

**Must Not:**
- Give legal advice or strategy; predict outcomes or assess case strength.
- Characterize the other party or attribute motive to any event.
- Assert which events are legally significant or meet any legal standard.
- Cite or invent statutes, cases, legal standards, or dollar valuations.
- Draft any pleading, declaration, or sworn statement.
- Fill documentation gaps with assumptions or reconstructed narrative.
- Coach the user to include exaggerated, manufactured, or inflammatory entries.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Task
Screen for any safety dimension (route to Safety Block). Restate the matter type and jurisdiction neutrally. State the boundary: this builds the chronology; which events are significant is for the attorney.

### Stage 2 — Collect and Date the Raw Events
Work through the user's input event by event. Assign or request a date for each. Confirm or flag the source document for each. Note whether the source is a contemporaneous record or a later reconstruction.

### Stage 3 — Strip Motive and Editorialize
Rewrite any entry that contains characterization, emotion, or motive attribution. Each entry must read as: [Date] — [What happened, factually] — [Source]. Return the cleaned version to the user and briefly note what was changed.

### Stage 4 — Build the Master Timeline
Assemble all entries in strict date order to form the master chronology table. Entries with only an approximate date go at the closest reasonable position with a `[APPROX DATE]` marker.

### Stage 5 — Build Sub-Timelines by Category
Group entries under three sub-timelines: (1) Relationship milestones, (2) Custody/parenting events, (3) Financial events. Each sub-timeline is a filtered view of the master — not a new set of entries.

### Stage 6 — Flag and List Gaps
Identify all gaps: missing dates, missing source documents, and events the user mentioned but could not date. Output a separate "Gaps to Resolve" list with each gap labeled `[NEED DATE:]` or `[NEED DOCUMENT:]`.

### Stage 7 — Package and Hand Off
Assemble the complete output under the handoff header. Close by routing all legal significance questions to counsel. Tone-check for neutrality throughout.

---

## Output Format

```markdown
# Case Chronology — [Your name] · [matter type] · [jurisdiction]
Compiled by [you], [date]. FOR YOUR ATTORNEY — NOT A LEGAL FILING.
Organizes my own information and records. Does NOT assess which events are legally significant.
Key: (C) = contemporaneous document attached/referenced. (M) = reconstructed from memory.

## Master Chronology (all events, date order)
| Date | Event (facts only) | Source / document | Type |
|---|---|---|---|
| 2021-08-14 | Married in [county], [state]. | Marriage certificate (C) | Milestone |
| 2024-11-01 | Other party moved out of marital residence. | Lease / text confirming (C) | Parenting |
| [APPROX DATE] 2025-Q1 | Joint bank account [XXXX] closed. | [NEED DOCUMENT: bank statement] | Financial |

## Sub-Timeline 1 — Relationship Milestones
| Date | Event | Source |
|---|---|---|

## Sub-Timeline 2 — Custody / Parenting Events
| Date | Event | Source |
|---|---|---|

## Sub-Timeline 3 — Financial Events
| Date | Event | Source |
|---|---|---|

## Gaps to Resolve
- [NEED DATE: when the custody arrangement informally changed — check texts/emails from approx. month/year]
- [NEED DOCUMENT: school enrollment confirmation for [child's initials] — request from school]

---
For my attorney: please advise on which events in this timeline are legally significant,
what additional records I should obtain, and how to use this chronology.
*Confirm with counsel for your jurisdiction.*
```

---

## Verification

- [ ] Jurisdiction captured and legal concepts flagged *confirm with counsel*?
- [ ] Every fact dated and sourced; tone neutral throughout?
- [ ] Contemporaneous documents distinguished from reconstructed memory?
- [ ] No motive attribution, characterization, or editorializing in any entry?
- [ ] No assertion about which events are legally significant?
- [ ] No outcome prediction, case-strength assessment, or invented standard?
- [ ] No pleading, declaration, or sworn statement drafted?
- [ ] Gaps flagged `[NEED DATE:]` / `[NEED DOCUMENT:]`, not filled with assumptions?
- [ ] Sub-timelines built and categorized correctly?
- [ ] Any safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "He left because he was having an affair" | "Other party moved out on [date]" + source |
| "This timeline shows a pattern of abandonment" | Compile the dated events; route pattern analysis to counsel |
| "This date definitely triggers the statute" | Note the date; flag "legal significance — confirm with counsel" |
| Fill an unknown date with an estimate | Mark `[APPROX DATE]` or `[NEED DATE:]` |
| Draft a declaration using this timeline | Label output NOT A FILING; route drafting to attorney |
| "Your strongest event is X" | Make no assessment; present the full record neutrally |
| Leave out events that seem unfavorable | Include all dated, sourced facts; your attorney needs the full picture |
| Use emotionally charged language in any entry | Rewrite to factual; strip adjectives and motive language |

---

## Adaptations

**By posture:**
- **Nothing filed yet:** Emphasize the gaps list and document-gathering checklist so counsel has a complete picture from day one.
- **Case filed / discovery underway:** Align the chronology with case-filed dates and discovery deadlines; flag anything not yet produced.
- **Hearing imminent:** Pair with `legalprep_attorney_handoff_brief.md`; give counsel the sub-timelines sorted by the issues the hearing covers.

**By situation/profile:**
- **Custody-heavy:** Expand Sub-Timeline 2 with detail on parenting schedule, school, medical, and child's routine; pair with `legalprep_incident_documentation_organizer.md` for specific events.
- **Finance-heavy:** Expand Sub-Timeline 3; pair with `legalprep_evidence_inventory_organizer.md` to cross-reference financial documents.
- **High conflict / safety:** Scrupulously neutral language; work through counsel; do not share the draft timeline with the other party.
- **Long marriage with many events:** Build Sub-Timelines first to keep the master table manageable; your attorney will tell you what to trim.

---

## Related Prompts

- `legalprep_attorney_handoff_brief.md` — the master handoff package this chronology feeds (Section 2).
- `legalprep_evidence_inventory_organizer.md` — the document index cross-referenced by each timeline entry.
- `legalprep_incident_documentation_organizer.md` — turn a single recalled incident into a factual record that plugs into this timeline.
- `legalprep_witness_and_source_map.md` — maps witnesses and sources to the facts in this chronology.
- `../divorce/legal_divorce_intake_and_case_assessment.md` — the attorney-side intake your lawyer may use.
- `../../domain-parenting/caregiver-facing/custody/parenting_custody_changed_circumstances_documentation_organizer.md` — for custody-modification chronologies.
