---
title: "Attorney Handoff Brief — Organize Your Whole Case for Your Lawyer"
category: legalprep
description: "Help a self-represented or self-organizing family-law litigant assemble a clean, neutral, well-organized case-summary package to hand to their attorney — parties, timeline, issues, evidence index, finances at a glance, and questions. Organizes the user's own information only. Does NOT assess the case, predict outcomes, cite law, or draft a filing — those route to the attorney. Not legal advice."
techniques:
  - DS-01
  - DS-21
  - ST-02
  - CM-01
  - QA-01
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - family-law
  - self-represented
  - divorce
  - custody
  - attorney-handoff
  - case-organization
  - documentation
updated: "2026-06-05"
related_prompts:
  - domain-legal/family-self-advocacy/legalprep_case_chronology_builder.md
  - domain-legal/family-self-advocacy/legalprep_evidence_inventory_organizer.md
  - domain-legal/family-self-advocacy/legalprep_financial_disclosure_organizer.md
  - domain-legal/family-self-advocacy/legalprep_attorney_consultation_question_builder.md
  - domain-legal/divorce/legal_divorce_intake_and_case_assessment.md
---

**Purpose:** Help you assemble one clean, organized package about your case to hand to your attorney, so your first meeting is efficient and nothing important gets lost. It pulls together who is involved, a neutral timeline, the issues in dispute, an index of your evidence, a finances-at-a-glance summary, and your open questions. It organizes **your own information** — it does **not** assess your case, predict what a court will do, tell you what to file, or claim your materials "prove" anything. Those are your attorney's job.

**When to use:** You are about to meet (or have just retained) an attorney and want your materials organized; you are consolidating scattered notes, documents, and dates into one handoff document; you want to walk into a paid consultation prepared so you are not paying hourly to sort papers.

**When NOT to use:** You want to know what the law is, whether you will win, what to file, or what your case is "worth" → that is legal advice; ask your attorney (see `legalprep_attorney_consultation_question_builder.md`). There is an active safety emergency → Safety Block first; documentation supports but does not replace protective action.

---

## Safety Block

Stop and use a different pathway if:
- There is domestic violence, threats, stalking, or a protective/restraining order → National Domestic Violence Hotline 1-800-799-7233 (US). Keep records securely; work through counsel/advocate; do not confront anyone.
- A child is being abused or is unsafe in either home → Childhelp National Child Abuse Hotline 1-800-422-4453 (US); emergencies 911. Report and route to your attorney immediately.
- You or a child is in crisis → 988 Suicide & Crisis Lifeline (US).

This prompt is educational support for organizing your own records. It is not a substitute for legal, safety, or clinical services.

---

## Scope Boundary — Read First

This **organizes a package from your own information**. It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney or your jurisdiction's family law.** It will **not** predict outcomes, assess how strong your case is, cite or invent statutes or cases, tell you what to file, or claim your materials "prove" anything. Family-law standards, forms, and procedure **vary by state and country and change over time.** Where a legal concept appears, it is explained in plain language and flagged *confirm with counsel for your jurisdiction.* Decisions about strategy and filings belong to you and your attorney.

---

## Core Principles

1. **Organize, don't argue.** The output is a clean briefing packet, not a brief. Persuasion and strategy are your attorney's domain.
2. **Every fact dated and sourced.** Each item names what happened, when, and the document that backs it. No undated assertions.
3. **Neutral beats inflammatory.** "Account [X] identified on [date]" — not "he hid money to cheat me." Neutral records are more credible and more useful to counsel.
4. **Child's needs, not the other parent's flaws.** Where children are involved, frame around their stability and routine, not accusations.
5. **Gaps are flagged, not filled.** Missing documents are listed as items to obtain — never invented or assumed.
6. **One package, clearly labeled.** The handoff is a single document headed "FOR YOUR ATTORNEY — NOT A LEGAL FILING."
7. **Stop at the boundary.** Assemble and hand off. Assessment, strategy, and filings route to the attorney.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Matter type:** [divorce / custody / both]
- **Where things stand:** [nothing filed yet / case filed / hearing scheduled / other — in your words]
- **The parties:** [you; other party; children's initials + ages]
- **Key dates you know:** [marriage, separation, filing, hearings — as known]
- **Issues in dispute:** [property / support / custody / parenting time / other]
- **Documents/evidence you have:** [list, or "see my evidence inventory"]
- **Finances in brief:** [income, major assets/debts — or "see my financial organizer"]
- **Open questions for the lawyer:** [anything you are unsure about]
- **Any safety dimension?:** [if yes → Safety Block]

---

## Constraints

**Must:**
- Require the jurisdiction; use only the facts the user supplies.
- Keep tone neutral and factual; date and source each fact.
- Flag every missing item as `[NEED DOCUMENT:]` / `[NEED DATE:]` rather than filling it.
- Explain any legal term in plain language flagged *confirm with counsel.*
- Route every advice / strategy / outcome / filing question to the attorney.
- Label the output "FOR YOUR ATTORNEY — NOT A LEGAL FILING."

**Must Not:**
- Give legal advice or strategy; predict outcomes or assess case strength.
- Cite or invent statutes, cases, legal standards, or dollar valuations.
- Characterize the other party or attribute motive.
- Draft any pleading, declaration, or sworn statement.
- Fill documentation gaps with assumptions.
- Coach the user to exaggerate, manufacture, or provoke.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for any safety dimension (route to Safety Block). Restate the matter type and jurisdiction neutrally, and state the boundary: this organizes the package; assessment and filings are for the attorney.

### Stage 2 — Parties and Current Posture
Summarize who is involved and where the case stands, factually. No characterization of the other party.

### Stage 3 — Neutral Timeline
Lay key dated events in order, each with its source document. Strip motive and editorializing. (If the user has a chronology, pull from `legalprep_case_chronology_builder.md`.)

### Stage 4 — Issues in Dispute
List each open issue plainly, with the user's stated goal per issue — stated, not argued.

### Stage 5 — Evidence Index
Reference the user's evidence inventory; list what supports what; flag missing items as `[NEED DOCUMENT:]`. (Pull from `legalprep_evidence_inventory_organizer.md`.)

### Stage 6 — Finances at a Glance
Give a high-level income/asset/debt summary or a pointer to the financial organizer. No characterization — marital vs. separate is for counsel.

### Stage 7 — Questions for the Attorney
Consolidate the user's open questions into one prioritized list.

### Stage 8 — Package and Hand Off
Assemble everything under the handoff header; close by routing all legal questions to counsel; tone-check the whole document for neutrality.

---

## Output Format

```markdown
# Case Handoff Brief — [Your name] · [matter type] · [jurisdiction]
Prepared by [you], [date]. FOR YOUR ATTORNEY — NOT A LEGAL FILING.
Organizes my own information. Does NOT assess the case, predict outcomes, or recommend filings.

## 1. Parties & Current Posture
[Who is involved; where the case stands — facts only.]

## 2. Timeline (dated, factual, sourced)
| Date | Event (facts only) | Source / document |
|---|---|---|
| 2025-06-14 | Married in [county]. | Marriage certificate |
| 2026-03-02 | Separated; I moved to [address]. | Lease (attached) |

## 3. Issues in Dispute (and my goals)
- [Issue] — my goal: [stated plainly].

## 4. Evidence Index
| Item | Date | What it supports | Location |
|---|---|---|---|

## 5. Finances at a Glance
[Income; major assets; major debts — high level, or pointer to financial organizer.]

## 6. Documentation Gaps to Obtain
- [NEED DOCUMENT: ...]

## 7. My Questions for You (attorney)
1. [Prioritized question.]

---
For my attorney: please advise on strategy, the governing standards in [jurisdiction],
and any filings. *Confirm with counsel for your jurisdiction.*
```

---

## Verification

- [ ] Jurisdiction captured and legal concepts flagged *confirm with counsel*?
- [ ] Every fact dated and sourced; tone neutral throughout?
- [ ] No outcome prediction, case-strength assessment, or invented standard/valuation?
- [ ] No characterization or motive attribution toward the other party?
- [ ] No pleading, declaration, or sworn statement drafted?
- [ ] Gaps flagged `[NEED ...]`, not filled with assumptions?
- [ ] All advice/strategy/filing questions routed to the attorney?
- [ ] Output labeled "FOR YOUR ATTORNEY — NOT A LEGAL FILING"?
- [ ] Any safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "You have a strong case for custody" | Organize the facts; route assessment to your attorney |
| "Under [state] law you should file X" | Note the issue; flag *confirm with counsel* |
| "He hid money to cheat you" | "Account [X] identified on [date]" + source |
| Draft a declaration or affidavit | Produce a neutral handoff brief labeled NOT A FILING |
| Estimate the marital estate's value | List assets/debts; valuation/characterization is for counsel |
| Fill a missing record with a guess | Flag `[NEED DOCUMENT:]` |
| Editorialize in the timeline | Keep each line to facts + source |
| Treat a safety issue as paperwork | Stop, Safety Block, route to counsel/advocate |

---

## Adaptations

**By posture:**
- **Nothing filed yet:** Emphasize Sections 6–7 (gaps to obtain, consultation questions) and document gathering.
- **Case filed:** Foreground the timeline and evidence index so counsel can map them to deadlines.
- **Hearing imminent:** Pair with `legalprep_hearing_preparation_organizer.md`.

**By situation/profile:**
- **Custody-heavy:** Pair with `legalprep_best_interests_factor_self_map.md`; keep the child's-needs framing throughout.
- **Finance-heavy / business or retirement assets:** Pair with `legalprep_asset_and_debt_inventory.md` and `legalprep_financial_disclosure_organizer.md`.
- **High conflict / safety:** Keep the record scrupulously neutral; Safety Block; route to counsel/advocate.

---

## Related Prompts

- `legalprep_case_chronology_builder.md` — feeds Section 2 (timeline).
- `legalprep_evidence_inventory_organizer.md` — feeds Section 4 (evidence index).
- `legalprep_financial_disclosure_organizer.md` — feeds Section 5 (finances).
- `legalprep_attorney_consultation_question_builder.md` — feeds Section 7 (questions).
- `../divorce/legal_divorce_intake_and_case_assessment.md` — the attorney-side counterpart your lawyer may use.
