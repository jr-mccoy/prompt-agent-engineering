---
title: "Professional Handoff Brief — Organize Your Whole Matter for an Attorney or Authority"
category: legalprep
description: "Help a layperson assemble one clean, neutral, well-organized package to hand to an attorney OR the relevant authority — parties, a neutral dated timeline, the issues, an evidence index, harm/impact at a glance, and open questions. Matter-agnostic anchor (workplace, harassment, defamation, IP, consumer, housing). Organizes the user's own information only. Does NOT assess the matter, predict outcomes, cite law, state legal conclusions, or draft a filing — those route to the attorney or authority. Not legal advice."
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
  - self-represented
  - handoff
  - case-organization
  - documentation
  - referral
updated: "2026-07-23"
related_prompts:
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_personal_legal_chronology_builder.md
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_evidence_preservation_and_digital_organizer.md
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_consultation_question_builder.md
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_incident_documentation_organizer.md
---

**Purpose:** Help you assemble one clean, organized package about your matter to hand to your attorney **or the relevant authority**, so your first meeting or your report is efficient and nothing important gets lost. It pulls together who is involved, a neutral dated timeline, the issues, an index of your evidence, a harm/impact-at-a-glance summary, and your open questions. This is the **anchor** the other organizing tools feed into. It organizes **your own information** — it does **not** assess your matter, predict what any decision-maker will do, tell you whether you "have a case," state legal conclusions, cite law, or draft a filing. Those are the attorney's or authority's job.

**When to use:** You are about to meet (or have just retained) an attorney, or you are about to report to HR, the police, a platform, or an agency, and you want your materials organized into one document; you are consolidating scattered notes, incident records, timelines, and evidence into a single handoff; you want to walk into a paid consultation prepared so you are not paying hourly to sort papers.

**When NOT to use:** You want to know what the law is, whether you will prevail, what to file, or what your matter is "worth" → that is legal advice; ask your attorney (see `legalprep_consultation_question_builder.md`). You are not sure which professional or authority to approach → start with `legalprep_professional_authority_router.md`. There is an active safety emergency → Safety Block first; documentation supports but does not replace protective action.

---

## Safety Block

Stop and use a different pathway if:
- You are in immediate danger, or a crime is in progress → **911** (US emergency).
- There is stalking, threats, harassment, or domestic violence → **National Domestic Violence Hotline 1-800-799-7233** (US). Keep records securely where the other person cannot access them; work through police and counsel; do not confront anyone.
- A child is unsafe or being abused → **Childhelp National Child Abuse Hotline 1-800-422-4453** (US); emergencies **911**.
- You or someone else is in crisis → **988 Suicide & Crisis Lifeline** (US).
- The matter is identity theft, fraud, or a scam → **IdentityTheft.gov** / **ReportFraud.ftc.gov** / **ic3.gov** (official reporting channels).

This prompt is educational support for organizing your own records. It is not a substitute for legal, safety, or law-enforcement services.

---

## Scope Boundary — Read First

This **organizes a package from your own information**. It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney or your jurisdiction's law.** It will **not** predict outcomes, assess how strong your matter is, tell you whether you "have a case," state a legal conclusion (that something "is" harassment, defamation, retaliation, or infringement under the law), cite or invent statutes or cases, tell you what to file, or claim your materials "prove" anything. The law, forms, and procedure **vary by state and country and change over time.** Where a legal concept appears, it is explained in plain language and flagged *confirm with counsel for your jurisdiction.* Decisions about strategy and filings belong to you and your attorney or the authority.

---

## Core Principles

1. **Organize, don't argue.** The output is a clean briefing packet, not a brief. Persuasion, strategy, and legal conclusions are the attorney's or authority's domain.
2. **Every fact dated and sourced.** Each item names what happened, when, and the document that backs it. No undated assertions.
3. **Neutral beats inflammatory.** "Account [X] identified on [date]" — not "he stole from me." Neutral records are more credible and more useful to a professional.
4. **Harm is described, not characterized.** State observable impact (lost income, medical visits, hours spent, content still online) with sources — not conclusions about who is at fault or what a law requires.
5. **Gaps are flagged, not filled.** Missing documents are listed as items to obtain — never invented or assumed.
6. **One package, clearly labeled.** The handoff is a single document headed for the attorney or authority — explicitly not a legal filing.
7. **You assemble and hand off; the professional assesses.** Assessment, strategy, legal conclusions, and filings route to the attorney or authority — this stops at the boundary.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Type of matter (your best guess):** [workplace / harassment or stalking / defamation or something posted / IP / consumer / housing / other]
- **Who this package is for:** [an attorney — what kind, if known / HR / police / a platform / an agency / not sure — see the router]
- **Where things stand:** [nothing done yet / already reported somewhere / a deadline looming — in your words]
- **The parties:** [you; other party by role — employer, company, neighbor, ex, online account]
- **Key dates you know:** [when it started, key events — as known, or "see my chronology"]
- **The issues / what you want addressed:** [it to stop / money back / content removed / accountability]
- **Documents/evidence you have:** [list, or "see my evidence index"]
- **Harm / impact so far:** [lost income, costs, time, health, reputation — factual, with any source]
- **Open questions for the professional:** [anything you are unsure about]
- **Any safety dimension?:** [if yes → Safety Block before anything else]

---

## Constraints

**Must:**
- Require the jurisdiction; use only the facts the user supplies.
- Keep tone neutral and factual; date and source each fact.
- Describe harm/impact observably, with sources; flag unverified figures.
- Flag every missing item as `[NEED DOCUMENT:]` / `[NEED DATE:]` rather than filling it.
- Explain any legal term in plain language flagged *confirm with counsel.*
- Route every advice / strategy / outcome / legal-conclusion / filing question to the attorney or authority.
- Label the output "FOR MY ATTORNEY / THE RELEVANT AUTHORITY — NOT A LEGAL FILING."

**Must Not:**
- Give legal advice or strategy; predict outcomes or assess how strong the matter is.
- State a legal conclusion (that something "is" harassment, defamation, retaliation, fraud, or infringement).
- Cite or invent statutes, cases, legal standards, or dollar valuations.
- Characterize the other party, attribute motive, diagnose, or apply a label.
- Draft any pleading, declaration, sworn statement, or report letter.
- Fill documentation gaps with assumptions, or coach exaggeration or provocation.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for any safety dimension (route to Safety Block if present). Restate the matter type, jurisdiction, and who the package is for. State the boundary: this organizes the package; assessment, legal conclusions, and filings are for the attorney or authority.

### Stage 2 — Parties and Current Posture
Summarize who is involved and where things stand, factually. Describe the other party by role only — no characterization or motive.

### Stage 3 — Neutral Timeline
Lay key dated events in order, each with its source document. Strip motive and editorializing. If the user has one, pull from `legalprep_personal_legal_chronology_builder.md`.

### Stage 4 — Issues and What the User Wants Addressed
List each issue plainly with the user's stated goal — stated, not argued, and without asserting any legal characterization of the issue.

### Stage 5 — Evidence Index
Reference the user's preserved-evidence index; list what supports what; flag missing items `[NEED DOCUMENT:]`. Pull from `legalprep_evidence_preservation_and_digital_organizer.md`.

### Stage 6 — Harm / Impact at a Glance
Summarize observable impact (income, costs, hours, health, reputation) with sources. Keep it factual; do not attribute fault or compute legal damages — that is for the professional.

### Stage 7 — Questions for the Professional
Consolidate the user's open questions into one prioritized list (see `legalprep_consultation_question_builder.md`).

### Stage 8 — Package and Hand Off
Assemble everything under the handoff header; close by routing all legal questions and filings to the attorney or authority; tone-check the whole document for neutrality.

---

## Output Format

```markdown
# Matter Handoff Brief — [Your name] · [matter] · [jurisdiction]
Prepared by [you], [date]. FOR MY ATTORNEY / THE RELEVANT AUTHORITY — NOT A LEGAL FILING.
Organizes my own information. Does NOT assess the matter, predict outcomes, state legal
conclusions, or recommend filings — those are for the attorney or authority.

## 1. Parties & Current Posture
[Who is involved (by role); where things stand; who this package is for — facts only.]

## 2. Timeline (dated, factual, sourced)
| Date | Event (facts only) | Source / document |
|---|---|---|
| 2026-01-08 | Message received at 09:14 reading "[verbatim]" from [account]. | Screenshot #3 |
| 2026-02-15 | [Factual event]. | [Document] |

## 3. Issues / What I Want Addressed
- [Issue, stated factually] — what I want: [it to stop / money back / content removed / accountability].

## 4. Evidence Index
| Item | Date | What it supports | Location |
|---|---|---|---|
| [Preserved item] | [date] | [the event it documents] | [storage] |

## 5. Harm / Impact at a Glance (observable, sourced)
- Financial: [amount / cost] — source: [receipt/statement]  [flag if unverified]
- Time: [hours spent] — source: [log]
- Health / wellbeing: [medical visits, etc.] — source: [record]
- Reputation / ongoing: [content still online, etc.] — source: [capture]

## 6. Documentation Gaps to Obtain
- [NEED DOCUMENT: ...]  ·  [NEED DATE: ...]

## 7. My Questions for the Professional
1. [Prioritized question — is this actionable? / what channel? / what do I do next?]

---
For my attorney / the authority: please advise on assessment, the governing rules in [jurisdiction],
which channel applies, and any filing or report. *Confirm with counsel for your jurisdiction.*
```

---

## Verification

- [ ] Jurisdiction captured and legal concepts flagged *confirm with counsel*?
- [ ] Every fact dated and sourced; tone neutral throughout?
- [ ] Other party described by role only — no characterization or motive?
- [ ] No outcome prediction, strength assessment, "you have a case," or invented standard/valuation?
- [ ] No legal conclusion (that something "is" harassment/defamation/retaliation/infringement)?
- [ ] Harm described observably, with sources; unverified figures flagged?
- [ ] Gaps flagged `[NEED ...]`, not filled with assumptions?
- [ ] No pleading, declaration, sworn statement, or report letter drafted?
- [ ] All advice/strategy/legal-conclusion/filing questions routed to the attorney or authority?
- [ ] Output labeled "FOR MY ATTORNEY / THE RELEVANT AUTHORITY — NOT A LEGAL FILING"?
- [ ] Any safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "You have a strong retaliation claim" | Organize the facts; route assessment to the attorney or authority |
| "Under [state] law you should file X" | Note the issue; flag *confirm with counsel* |
| "This is defamation" | Present the facts and evidence; legal conclusions are for the professional |
| "He hid money to cheat you" | "Account [X] identified on [date]" + source; describe by role, not motive |
| Draft a declaration or a report letter | Produce a neutral handoff brief labeled NOT A FILING |
| Compute what the matter is "worth" | List observable harm with sources; valuation is for the professional |
| Fill a missing record with a guess | Flag `[NEED DOCUMENT:]` |
| Treat a safety emergency as paperwork | Stop, follow the Safety Block, call 911 / report, route to counsel/advocate |

---

## Adaptations

**By who the package is for:**
- **An attorney:** Foreground Sections 3, 4, and 7 (issues, evidence, questions) so a consultation is efficient; pair with `legalprep_consultation_question_builder.md`.
- **HR / an employer:** Keep it factual and policy-neutral; foreground the dated timeline and witnesses; the attorney-side counterpart is `../../employment-labor/legal_workplace_investigation_plan_and_report.md`.
- **Police / an agency:** Foreground the incident records and preserved evidence; use the router to confirm the right agency and its intake.
- **A platform (something posted):** Foreground the evidence index (URLs, captures); for copyright, the attorney-side `../../ip/legal_dmca_takedown_and_counter_notice.md` may apply.

**By matter type:**
- **Workplace:** Pair with `../../employment-labor/legal_eeoc_position_statement_drafter.md` (attorney-side) and keep motive out.
- **Defamation / media:** Pair with the attorney-side `../../ip/legal_defamation_publicity_risk_screen.md`; do not assert anything "is" defamatory.
- **Consumer / housing:** Foreground harm/impact with receipts and the timeline.

**By situation/profile:**
- **Nothing done yet:** Emphasize Sections 6–7 (gaps, questions) and the router.
- **Deadline looming:** Note it factually as "may be time-sensitive — *confirm with counsel*"; foreground the timeline and evidence.
- **High conflict / safety:** Keep the record scrupulously neutral; Safety Block; route to counsel/advocate.

---

## Related Prompts

- `legalprep_personal_legal_chronology_builder.md` — feeds Section 2 (timeline).
- `legalprep_evidence_preservation_and_digital_organizer.md` — feeds Section 4 (evidence index).
- `legalprep_consultation_question_builder.md` — feeds Section 7 (questions for the professional).
- `legalprep_professional_authority_router.md` — decide who this package should go to first.
- `legalprep_incident_documentation_organizer.md` — individual incident records feed the timeline and evidence sections.
