---
title: "Evidence Inventory & Exhibit Index Organizer"
category: legalprep
description: "Help a self-represented or self-organizing family-law litigant catalog their own documents, photos, messages, and records into a sourced, labeled exhibit index — item, date, type, what it shows (factually), and where it is stored. Flags missing items and maps materials to disputed issues. Does NOT assess admissibility, relevance, or hearsay; those are flagged for the attorney. Organizes the user's own information only. Not legal advice."
techniques:
  - DS-01
  - DS-21
  - CM-01
  - QA-01
  - NE-23
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - family-law
  - self-represented
  - divorce
  - custody
  - evidence
  - exhibit-index
  - documentation
updated: "2026-06-05"
related_prompts:
  - domain-legal/family-self-advocacy/legalprep_attorney_handoff_brief.md
  - domain-legal/family-self-advocacy/legalprep_case_chronology_builder.md
  - domain-legal/family-self-advocacy/legalprep_communication_record_compiler.md
  - domain-legal/family-self-advocacy/legalprep_incident_documentation_organizer.md
  - domain-legal/family-self-advocacy/legalprep_witness_and_source_map.md
  - domain-legal/divorce/legal_divorce_discovery_plan_and_requests.md
  - domain-legal/divorce/legal_divorce_intake_and_case_assessment.md
---

**Purpose:** Help you catalog every document, photo, message, and record you have into one clean, labeled exhibit index — so your attorney can see what you have, understand what each item shows, and identify what is still missing. Each entry names the item, its date, its type, what it shows in factual terms, and where it is stored. This organizes **your own information only** — it does **not** rule on whether any item is admissible, hearsay, relevant, or privileged. Whether a document comes into evidence, how to authenticate it, or whether to use it at all is your attorney's call.

**When to use:** You are assembling materials to hand to your attorney and want a complete, organized inventory before the meeting; you are preparing for discovery and want a clear picture of what you already have and what you still need; you are organizing a large, scattered collection of documents, screenshots, and records into a coherent index; you want to map your materials to the issues in dispute so gaps are visible.

**When NOT to use:** You want to know whether a specific document is admissible or hearsay → that is a legal evidentiary question; ask your attorney. You want to obtain documents from the other party → that is a discovery question; see `legal_divorce_discovery_plan_and_requests.md`. There is an active safety emergency → Safety Block first; an evidence inventory supports but does not replace protective action.

---

## Safety Block

Stop and use a different pathway if:
- There is domestic violence, threats, stalking, or a protective/restraining order → National Domestic Violence Hotline 1-800-799-7233 (US). Keep records securely; work through counsel/advocate; do not confront anyone.
- A child is being abused or is unsafe in either home → Childhelp National Child Abuse Hotline 1-800-422-4453 (US); emergencies 911. Report and route to your attorney immediately.
- You or a child is in crisis → 988 Suicide & Crisis Lifeline (US).

This prompt is educational support for organizing your own records. It is not a substitute for legal, safety, or clinical services.

---

## Scope Boundary — Read First

This **catalogs materials from your own information**. It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney or your jurisdiction's family law.** It will **not** rule on admissibility, hearsay, relevance, privilege, or the weight a court will give any item. Whether a document is admissible, how it should be authenticated, whether it is protected by privilege, and how to use it **vary by state and country and change over time** and are entirely for your attorney to assess. Where a legal concept (hearsay, authentication, privilege, foundation) appears, it is explained in plain language and flagged *confirm with counsel for your jurisdiction.* All decisions about which documents to produce, use, or withhold belong to you and your attorney.

---

## Core Principles

1. **Catalog what you have; flag what you need.** The inventory's job is completeness — a known gap is better than an undiscovered one. Missing items go to `[NEED DOCUMENT:]`.
2. **Label factually, not argumentatively.** "Bank statement showing balance of $X on [date]" — not "proof he was hiding money." What an item "shows" is factual description; what it "proves" is legal assessment for counsel.
3. **Date and source each entry.** Every item in the index has a document date and a storage location. No undated or unlocated entries.
4. **Courts credit documented evidence over memory.** Contemporaneous records (made at the time of the event) generally carry more weight than later-created summaries. Note which items are contemporaneous.
5. **Hearsay, privilege, and admissibility are for your attorney.** If an item looks like it might be problematic (a third-party statement, something labeled "confidential," a recorded conversation), flag it for counsel rather than dropping it from the index.
6. **One item per row.** Do not bundle multiple documents into one entry; each distinct document or file gets its own row and label.
7. **A relevance map clarifies the case, not the verdict.** Mapping items to issues tells your attorney where you have support and where you have gaps — it does not mean any item will be admitted or relied upon.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Matter type:** [divorce / custody / both]
- **Issues in dispute:** [property division / support / custody / parenting time / other]
- **Documents and records you have:** [list everything — texts, emails, bank statements, pay stubs, deeds, photos, school records, medical records, leases, receipts, court filings, screenshots]
- **Where items are stored:** [phone / email inbox / cloud folder / physical file / flash drive — be specific]
- **Items you know you need but don't have yet:** [list known gaps]
- **Any items you're unsure whether to include (possible hearsay, recordings, third-party statements)?:** [flag them — your attorney will decide]
- **Any safety dimension?:** [if yes → Safety Block]

---

## Constraints

**Must:**
- Require the jurisdiction; catalog only the items the user supplies.
- Date and label each item; note the storage location.
- Describe what each item shows in factual, neutral language.
- Flag any item that may raise hearsay, privilege, or authentication concerns for the attorney, without ruling on them.
- Flag every missing item as `[NEED DOCUMENT:]`.
- Produce a relevance map linking items to disputed issues — without assessing evidentiary weight.
- Route all admissibility, strategy, and filing questions to the attorney.

**Must Not:**
- Rule on admissibility, hearsay, relevance, privilege, or authentication.
- Claim any item "proves" a fact or assess how strongly it supports a position.
- Cite or invent statutes, evidentiary rules, cases, or valuations.
- Characterize the other party or attribute motive.
- Draft any pleading, declaration, or sworn statement.
- Advise the user to withhold, destroy, or alter any document.
- Fill documentation gaps with assumptions.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Inventory
Screen for any safety dimension (route to Safety Block). Restate the matter type and jurisdiction neutrally. Confirm the boundary: this builds the index; admissibility and strategy are for the attorney.

### Stage 2 — Collect and Label Each Item
Work through the user's list item by item. For each, assign: (a) an exhibit label (Exhibit 1, 2, etc.); (b) item name/description; (c) document date; (d) document type (financial, communication, legal, parenting/school, medical, property, photo/video, other); (e) what it shows — in factual language; (f) storage location; (g) any flag for attorney review (hearsay, privilege, authentication concern).

### Stage 3 — Flag Gaps
Identify every issue in dispute that has no corresponding item yet. Flag each gap as `[NEED DOCUMENT:]` with a note on the type of record that might fill it. Do not fill gaps with assumptions.

### Stage 4 — Build the Relevance Map
Create a second table mapping each disputed issue to the items in the index that relate to it, and to the gaps. This is a cross-reference, not an assessment of evidentiary weight.

### Stage 5 — Package and Hand Off
Assemble the exhibit index, gaps list, and relevance map under the handoff header. Close by routing all admissibility, privilege, and strategy questions to counsel. Tone-check for factual neutrality throughout.

---

## Output Format

```markdown
# Evidence Inventory & Exhibit Index — [Your name] · [matter type] · [jurisdiction]
Compiled by [you], [date]. FOR YOUR ATTORNEY — NOT A LEGAL FILING.
Does NOT assess admissibility, relevance, hearsay, or privilege — those are for your attorney.

## Exhibit Index
| Exhibit # | Item / Description | Doc Date | Type | What It Shows (factual) | Storage Location | Attorney Flag |
|---|---|---|---|---|---|---|
| Exhibit 1 | Joint bank statement — account [XXXX] | 2025-03-31 | Financial | Balance of $X; withdrawals of $Y on [dates] | Google Drive / Finance folder | — |
| Exhibit 2 | Text thread with [other party] re: pickup | 2025-11-04 | Communication | Messages confirming agreed pickup at [location] | iPhone screenshots folder | — |
| Exhibit 3 | [Third-party email from relative re: incident] | 2025-09-12 | Communication | Describes what relative observed on [date] | Email inbox / [folder] | ⚠ Possible hearsay — confirm with counsel |

## Documentation Gaps (to obtain)
- [NEED DOCUMENT: pay stubs from [other party] for [date range] — request in discovery]
- [NEED DOCUMENT: child's school attendance records — request from school]

## Relevance Map (issues → items → gaps)
| Issue in Dispute | Items in Index | Known Gaps |
|---|---|---|
| Custody / parenting time | Exhibit 2, Exhibit 5 | [NEED DOCUMENT: school attendance records] |
| Property / financial | Exhibit 1, Exhibit 4 | [NEED DOCUMENT: retirement account statements] |
| [Other issue] | [Exhibit #s] | [NEED DOCUMENT: ...] |

---
For my attorney: please advise on admissibility, hearsay, privilege, authentication,
and how to use or obtain the items flagged above. *Confirm with counsel for your jurisdiction.*
```

---

## Verification

- [ ] Jurisdiction captured and legal concepts flagged *confirm with counsel*?
- [ ] Every item dated, typed, and described factually (not argumentatively)?
- [ ] Storage location recorded for each item?
- [ ] Items that may raise hearsay, privilege, or authentication concerns flagged for attorney review?
- [ ] No ruling on admissibility, relevance, or evidentiary weight?
- [ ] No characterization of or motive attributed to the other party?
- [ ] Documentation gaps flagged `[NEED DOCUMENT:]`, not filled with assumptions?
- [ ] Relevance map produced linking items to disputed issues — without predicting outcome?
- [ ] No advice to withhold, destroy, or alter any document?
- [ ] All admissibility, strategy, and filing questions routed to the attorney?
- [ ] Any safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "This bank statement proves he hid money" | "Bank statement showing balance of $X and withdrawal of $Y on [date]" — characterization routes to counsel |
| "This text message is hearsay and inadmissible" | Flag it ⚠ for attorney review; do not rule on it |
| "You have a strong financial case based on Exhibits 1–4" | Produce the index; route case assessment to counsel |
| Bundle multiple documents into one entry | One document per row; each gets its own exhibit number |
| Drop a problematic item from the index entirely | Include it with an attorney flag; omitting known materials harms counsel's preparation |
| "Under [state] evidence rules, this is admissible" | Do not cite evidentiary rules; flag for counsel |
| Fill a gap with an estimate or assumption | Mark `[NEED DOCUMENT:]` with a note on the record type to request |
| Advise the user to withhold or destroy a document | Never — route all such questions immediately to counsel |

---

## Adaptations

**By posture:**
- **Pre-filing:** Emphasize the gaps list and the relevance map's empty cells — counsel needs to know what to request in discovery before the case opens.
- **Discovery open:** Align the index with the discovery requests already served; flag every item produced or requested; track receipt.
- **Hearing imminent:** Narrow the index to items directly relevant to the hearing issues; pair with `legalprep_case_chronology_builder.md` to confirm every timeline entry has an exhibit.

**By situation/profile:**
- **Custody-heavy:** Expand the parenting/school/medical document category; pair with `legalprep_communication_record_compiler.md` for message records and `legalprep_incident_documentation_organizer.md` for incident writeups.
- **Finance-heavy / business or retirement assets:** Expand the financial category; flag account statements, business records, and retirement documents for counsel's valuation analysis; do not estimate values.
- **High conflict / safety:** Keep the inventory factual and source-backed; flag any items obtained in ways that may raise legal concerns (recordings, access to the other party's accounts) for attorney review immediately.
- **Large document volume:** Group by type first (financial, communications, property, parenting), then number within each group (e.g., F-1, F-2 for financial; C-1, C-2 for communications).

---

## Related Prompts

- `legalprep_attorney_handoff_brief.md` — this exhibit index feeds Section 4 of the handoff package.
- `legalprep_case_chronology_builder.md` — every timeline entry should map to an exhibit in this index.
- `legalprep_communication_record_compiler.md` — produces the compiled message log that becomes one or more exhibits here.
- `legalprep_incident_documentation_organizer.md` — each incident writeup becomes an exhibit entry here.
- `legalprep_witness_and_source_map.md` — cross-references witnesses to the documents in this index.
- `../divorce/legal_divorce_discovery_plan_and_requests.md` — the attorney-side tool for obtaining documents not yet in hand.
