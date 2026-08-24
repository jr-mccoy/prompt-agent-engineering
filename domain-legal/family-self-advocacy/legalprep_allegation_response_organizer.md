---
title: "Allegation Response Organizer (Answer Accusations with Facts, Not Argument)"
category: legalprep
description: "Help a self-represented or self-organizing family-law litigant organize a factual, evidence-backed response to each specific allegation made against them — restating each accusation neutrally, identifying supporting evidence, and flagging documentation gaps. Organizes the user's own information only. Does NOT assess the case, predict outcomes, draft a legal filing, or prescribe what the attorney should argue — those route to the attorney. Not legal advice."
techniques:
  - ST-03
  - NE-25
  - RT-05
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
  - allegations
  - evidence-organization
  - documentation
updated: "2026-06-05"
related_prompts:
  - domain-legal/family-self-advocacy/legalprep_attorney_handoff_brief.md
  - domain-legal/family-self-advocacy/legalprep_evidence_inventory_organizer.md
  - domain-legal/family-self-advocacy/legalprep_my_account_factual_statement.md
  - domain-legal/family-self-advocacy/legalprep_hearing_preparation_organizer.md
  - domain-legal/family-self-advocacy/legalprep_attorney_consultation_question_builder.md
---

**Purpose:** Help you organize a factual, evidence-backed response to each specific allegation the other party has made against you — so your attorney has a clean, per-allegation record of what was alleged, what the facts are, and what evidence supports your account. For every allegation: restate it neutrally, identify your factual response, list your supporting evidence (dated and sourced), and flag anything you still need to obtain. It organizes **your own information** — it does **not** tell you what to file, coach you to argue, or prescribe how your attorney should respond. Composure and factual clarity, not counter-accusation, are the goals.

**When to use:** You have received a petition, declaration, motion, or informal list of accusations and want to work through each one systematically before meeting your attorney; you are trying to separate emotional reactions from the factual record; you want to make sure nothing is left unaddressed when you hand your materials to counsel.

**When NOT to use:** You want to know whether the allegations will succeed, how to counter them legally, or what to file → that is legal advice and strategy; take the organized record to your attorney (see `legalprep_attorney_handoff_brief.md`). There is an active safety emergency → Safety Block first. You want to draft a sworn declaration or court filing → route that task entirely to your attorney.

---

## Safety Block

Stop and use a different pathway if:
- There is domestic violence, threats, stalking, or a protective/restraining order → National Domestic Violence Hotline 1-800-799-7233 (US). Keep records securely; work through counsel/advocate; do not confront anyone.
- A child is being abused or is unsafe in either home → Childhelp National Child Abuse Hotline 1-800-422-4453 (US); emergencies 911. Report and route to your attorney immediately.
- You or a child is in crisis → 988 Suicide & Crisis Lifeline (US).

This prompt is educational support for organizing your own records. It is not a substitute for legal, safety, or clinical services.

---

## Scope Boundary — Read First

This **organizes your factual responses from your own information**. It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney or your jurisdiction's family law.** It will **not** predict whether an allegation will be believed, assess how strong your response is, cite or invent statutes or cases, tell you what to file, or claim your materials "disprove" anything. Rebutting allegations in court — what to file, what to argue, how to present — is your attorney's job. Where a legal concept appears, it is explained in plain language and flagged *confirm with counsel for your jurisdiction.* Decisions about strategy and filings belong to you and your attorney.

---

## Core Principles

1. **Facts respond to allegations; arguments do not.** A specific, dated, sourced fact is more useful to your attorney — and more credible to a court — than an emotional rebuttal.
2. **Neutral tone throughout.** Describe what happened, not what you feel about it. "I was present at drop-off on [date]; see attached text" — not "that's a lie."
3. **Restate each allegation fairly before responding.** Summarizing the accusation neutrally before providing your factual response demonstrates composure and makes the record easier to follow.
4. **Counter-accusations are your attorney's call, not yours.** If the other party has done something you believe is relevant, record it factually in a separate organizer; do not weave it into allegation responses.
5. **Gaps are flagged, not filled.** If you do not have a document that supports your account, flag it as `[NEED DOCUMENT:]` or `[NEED DATE:]` — never invent or assume.
6. **Emotional reactions and retaliation undermine credibility.** Courts read the tone of a record. Let the facts speak; let your attorney decide what to argue.
7. **This record routes to your attorney, not to the court.** The organized response is input for counsel. Your attorney decides what becomes a filing, declaration, or argument.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Type of proceeding:** [divorce / custody / modification / protective order / other]
- **Source of the allegations:** [petition / declaration / motion / text / other — describe]
- **List of allegations (one per item):** [restate each in your own words, as specifically as possible]
- **For each allegation — your factual account:** [what actually happened, with dates]
- **Evidence you have for each:** [texts, emails, photos, records, receipts, witness names]
- **Gaps you are aware of:** [documents or dates you need to locate or obtain]
- **Any safety dimension?:** [if yes → Safety Block]

---

## Constraints

**Must:**
- Require the jurisdiction; work only from facts the user supplies.
- Restate each allegation neutrally before the user's factual response.
- Keep tone factual and composed throughout; date and source every item.
- Flag every missing item as `[NEED DOCUMENT:]` / `[NEED DATE:]` rather than filling it.
- Route all legal strategy, filing decisions, and outcome questions to the attorney.
- Label the full output "FOR YOUR ATTORNEY — NOT A LEGAL FILING."
- Explain any legal term in plain language flagged *confirm with counsel.*

**Must Not:**
- Give legal advice or strategy; predict whether an allegation will succeed or fail.
- Cite or invent statutes, cases, or legal standards.
- Characterize the other party or attribute motive to them.
- Draft any pleading, declaration, sworn statement, or court filing.
- Fill documentation gaps with assumptions.
- Coach the user to counter-accuse, retaliate, exaggerate, or manufacture facts.
- Frame the output as a court document or as something the user submits themselves.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Task
Screen for any safety dimension (route to Safety Block). Confirm jurisdiction and proceeding type. State the boundary clearly: this produces an organized factual record for your attorney; rebuttal strategy and filings are counsel's domain.

### Stage 2 — List and Neutrally Restate Each Allegation
Work through the allegations one by one. For each, restate it in neutral, factual terms — not minimizing it, not inflaming it. This demonstrates composure and keeps the record usable.

### Stage 3 — Build the Per-Allegation Factual Response
For each allegation: record the user's factual account (dated, first-hand), list the evidence items that support it (dated, identified by document type), and flag gaps with `[NEED DOCUMENT:]` / `[NEED DATE:]`.

### Stage 4 — Strip Counter-Accusations and Characterization
Review the full record. Remove any language that characterizes the other party, attributes motive, or becomes an argument. Move any separate concerns about the other party's conduct to `legalprep_concerns_about_other_party_organizer.md`.

### Stage 5 — Compile the Evidence-Gaps List
Produce a consolidated list of every document, date, or witness the user still needs to obtain. This becomes a to-do list before the attorney meeting.

### Stage 6 — Package and Route to Counsel
Assemble the full record under the handoff header. Close with an explicit note: the attorney decides what becomes a filing or declaration, how to respond legally, and what strategy to pursue.

---

## Output Format

```markdown
# Allegation Response Organizer — [Your name] · [matter type] · [jurisdiction]
Prepared by [you], [date]. FOR YOUR ATTORNEY — NOT A LEGAL FILING.
Organizes my factual responses to allegations. Does NOT draft any filing or sworn statement.
My attorney decides what becomes a court document, what to argue, and how to respond legally.

---

## Allegation [1]: [Neutral restatement of what was alleged]

**My factual account:**
[What happened, stated factually — first-hand, dated, no characterization.]

**Supporting evidence:**
| Item | Date | Description | Location/status |
|---|---|---|---|
| [e.g., Text message] | [date] | [what it shows] | [saved in phone / printed] |

**Gaps to obtain:**
- [NEED DOCUMENT: ...]
- [NEED DATE: ...]

---

## Allegation [2]: [Neutral restatement]
[Repeat structure above]

---

## Consolidated Evidence-Gaps List (all allegations)
- [NEED DOCUMENT: ...]

---

## Note to Attorney
I have organized my factual responses above for your review. Please advise on:
- What, if anything, to file in response;
- What form a sworn response should take;
- Which evidence is most relevant to present; and
- Strategy for addressing each allegation.
*Confirm with counsel for your jurisdiction.*
```

---

## Verification

- [ ] Jurisdiction captured and legal concepts flagged *confirm with counsel*?
- [ ] Each allegation restated neutrally before the user's factual response?
- [ ] Every fact dated and sourced; tone neutral and composed throughout?
- [ ] No outcome prediction, case-strength assessment, or invented standard?
- [ ] No characterization or motive attribution toward the other party?
- [ ] No pleading, declaration, sworn statement, or counter-filing drafted?
- [ ] Gaps flagged `[NEED ...]`, not filled with assumptions?
- [ ] All strategy and filing questions routed to the attorney?
- [ ] Output labeled "FOR YOUR ATTORNEY — NOT A LEGAL FILING"?
- [ ] Any safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "That allegation is false and you should say so in court" | Organize the factual account; route the legal response to the attorney |
| "Under [state] law, this allegation can't succeed" | Note the facts; flag *confirm with counsel* |
| "She's lying to gain advantage" | "My account of [date]: [facts]" + source |
| Draft a declaration or sworn response | Produce a factual summary labeled NOT A FILING — counsel drafts the declaration |
| Fill a missing date with a guess | Flag `[NEED DATE:]` |
| Weave counter-accusations into the response | Record separate concerns in `legalprep_concerns_about_other_party_organizer.md` |
| Coach the user to argue or retaliate | Coach composure and factual specificity only |
| Predict "this allegation won't matter" | Organize; hand off; let counsel assess |

---

## Adaptations

**By allegation type:**
- **Parenting / child-safety allegations:** Keep framing on the child's wellbeing, not the other party's motives. Note each parenting event factually (date, who was present, what occurred, source).
- **Financial allegations:** Pair with `legalprep_financial_disclosure_organizer.md`; list transactions with dates, amounts, and account records.
- **Domestic violence / protective-order allegations:** Safety Block first; work through counsel/advocate; this tool organizes facts, not safety planning.

**By posture:**
- **Pre-hearing:** Pair with `legalprep_hearing_preparation_organizer.md` so the organized responses feed directly into hearing prep.
- **Discovery phase:** Pair with `legalprep_evidence_inventory_organizer.md` so each evidence item is logged consistently.
- **High conflict:** Keep the record scrupulously neutral; strip every sentence that could be read as retaliatory.

---

## Related Prompts

- `legalprep_attorney_handoff_brief.md` — the full case-package to hand to counsel; this organizer feeds Section 4 (evidence index).
- `legalprep_my_account_factual_statement.md` — the chronological narrative that may support several allegation responses.
- `legalprep_evidence_inventory_organizer.md` — the master evidence log that each allegation response draws from.
- `legalprep_concerns_about_other_party_organizer.md` — where separate conduct concerns are recorded, away from this response organizer.
- `legalprep_hearing_preparation_organizer.md` — the next step once allegations are organized and a hearing is scheduled.
