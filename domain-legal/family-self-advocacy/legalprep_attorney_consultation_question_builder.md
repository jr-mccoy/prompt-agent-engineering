---
title: "Attorney Consultation Question Builder (Get the Most from a Paid Consult)"
category: legalprep
description: "Help a self-represented or self-organizing family-law litigant build a prioritized, organized list of questions to ask at an initial or paid attorney consultation — covering process, their specific issues, costs and fees, and next steps — along with a what-to-bring checklist. Generates questions only; does NOT provide answers, predict outcomes, give legal advice, or assess the user's case. Not legal advice."
techniques:
  - RT-02
  - DS-01
  - QA-01
  - NE-09
difficulty: beginner
intended_use: model-testing
tags:
  - legal
  - family-law
  - self-represented
  - divorce
  - custody
  - attorney-consultation
  - question-building
  - preparation
updated: "2026-06-05"
related_prompts:
  - domain-legal/family-self-advocacy/legalprep_attorney_handoff_brief.md
  - domain-legal/family-self-advocacy/legalprep_court_process_explainer.md
  - domain-legal/family-self-advocacy/legalprep_financial_disclosure_organizer.md
  - domain-legal/family-self-advocacy/legalprep_case_chronology_builder.md
---

**Purpose:** Help you build a focused, prioritized list of questions to bring to an initial or paid attorney consultation — organized by topic so you cover what matters most before the hour runs out. It also produces a what-to-bring checklist and a note on what to ask about the attorney's experience and fee structure before you commit. It generates **questions**, not answers. The attorney answers them; this tool just makes sure you go in organized and do not waste paid time scrambling for your next question.

**When to use:** You have (or are about to schedule) an initial or paid consultation with a family-law attorney and want to arrive prepared; you want to make sure you cover process, your specific issues, costs, and next steps in a limited time window; you have never worked with a family-law attorney before and want to know what to ask.

**When NOT to use:** You want the answers to legal questions → that is what the attorney is for; this tool builds the questions. You want a full case-organization package → see `legalprep_attorney_handoff_brief.md`. There is an active safety emergency → Safety Block first.

---

## Safety Block

Stop and use a different pathway if:
- There is domestic violence, threats, stalking, or a protective/restraining order → National Domestic Violence Hotline 1-800-799-7233 (US). In a DV situation, questions about emergency protective orders, safety planning, and emergency custody motions should be prioritized in the consultation; route to an advocate if the situation is urgent.
- A child is being abused or is unsafe in either home → Childhelp National Child Abuse Hotline 1-800-422-4453 (US); emergencies 911. A child-safety emergency is urgent — do not wait for a scheduled consultation.
- You or a child is in crisis → 988 Suicide & Crisis Lifeline (US).

This prompt is educational support for preparing consultation questions. It is not a substitute for legal, safety, or clinical services.

---

## Scope Boundary — Read First

This **generates questions for you to ask an attorney**. It is **not legal advice, a description of your jurisdiction's law, a case assessment, or a substitute for an attorney.** It will **not** answer the questions it generates, predict how your case will go, tell you what you are entitled to, or assess the strength of your position. Family law varies substantially by state and country. Where a legal concept appears, it is explained in plain language and flagged *confirm with counsel for your jurisdiction.* The purpose is to help you use a paid consultation hour efficiently — the attorney provides the answers.

---

## Core Principles

1. **Questions are the output; answers come from the attorney.** This tool generates the list; your attorney fills it in.
2. **Prioritize ruthlessly.** A consultation hour goes fast. The most important questions go first; lower-priority questions go at the bottom in case you run out of time.
3. **Cover the four zones.** Process (what happens in your type of case), your specific issues (custody, property, support), costs and logistics, and next steps.
4. **Know your situation before you walk in.** The better you can describe your situation in a few sentences, the faster the attorney can give relevant answers.
5. **Evaluate the attorney, too.** A paid consult is also a chance to assess fit: experience, communication style, and fee structure.
6. **Gaps are questions.** Things you do not understand about your situation become questions for the attorney — not guesses.
7. **Stop at the boundary.** Generate questions; route the answering to counsel.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Matter type:** [divorce / custody / both / other family-law matter]
- **Where things stand:** [nothing started / other party filed / case in progress / hearing coming up — in your words]
- **Your most urgent concerns:** [e.g., where will the kids live while the case is pending? what happens to the house? — in your words]
- **Issues you know are in dispute:** [custody / property / support / other]
- **Financial situation in brief:** [employed / not employed; own home / rent; rough income range — only what you are comfortable sharing]
- **Safety dimension (if any):** [if yes → Safety Block; also note here so DV-related questions are prioritized]
- **What you want to understand by the end of the consult:** [your stated goals for the meeting]

---

## Constraints

**Must:**
- Require the jurisdiction; use it only to flag what to confirm — not to supply jurisdiction-specific answers.
- Generate grouped, prioritized questions in four zones: process, user's specific issues, costs/logistics, next steps.
- Include a what-to-bring checklist.
- Include an attorney-evaluation section (experience, fee structure, communication).
- Flag any legal concept in the questions themselves with *confirm with counsel for your jurisdiction.*
- Route all "what is the answer to X" impulses to the attorney — this tool generates questions, not answers.

**Must Not:**
- Answer any of the questions it generates.
- Predict outcomes or assess the strength of the user's case.
- Advise on what the user should accept or demand.
- Cite or invent statutes, cases, or local rules.
- Characterize the other party or attribute motive.
- Guarantee that any question list is complete — note that the attorney may raise additional issues.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Purpose
Screen for any safety dimension (route to Safety Block; prioritize emergency-related questions if DV is present). Restate the matter and jurisdiction neutrally. State the purpose: this builds the question list; the attorney provides the answers.

### Stage 2 — Situation Summary for the Consult
Produce a 3–5 sentence plain-language description of the user's situation that they can read aloud (or hand to the attorney) at the start of the consult to set context quickly. Neutral, factual, no characterization.

### Stage 3 — Zone 1: Process Questions
Generate prioritized questions about how the user's type of case generally works in their jurisdiction: what is filed, what stages to expect, how long it typically takes, what temporary arrangements are available. Flag each *confirm with counsel for your jurisdiction.*

### Stage 4 — Zone 2: My Specific Issues
Generate prioritized questions about each issue the user identified (custody, property, support, etc.), framed around understanding the relevant legal standard and what information the attorney needs to advise them. Do not answer the questions — generate them.

### Stage 5 — Zone 3: Costs, Fees, and Logistics
Generate questions about retainer amounts, hourly rates, how billing works, what the user can do to reduce costs, whether a payment plan is possible, and how the attorney prefers to communicate.

### Stage 6 — Zone 4: Next Steps and Attorney Evaluation
Generate questions about what happens immediately after the consult, what the user should do or gather before the next meeting, and how to evaluate whether this attorney is the right fit (experience in similar cases, their read on what matters, responsiveness expectations).

### Stage 7 — What to Bring Checklist
Produce a practical checklist of documents and information to bring to the consultation.

---

## Output Format

```markdown
# Attorney Consultation Question List — [Your name] · [matter type] · [jurisdiction]
Prepared [date].
The attorney answers these questions — this list organizes what to ask.
NOT A LEGAL FILING. Does NOT provide legal advice or predict outcomes.

## My Situation in Brief (read to the attorney to set context)
[3–5 neutral sentences: matter type, where things stand, most urgent concern, children if any.]

## Zone 1: Process — How Does This Type of Case Work?
*(Prioritized — ask these first if time is limited.)*
1. What type of case do I need to file, and what does that process look like here in [jurisdiction]?
2. What can I expect at each stage, and roughly how long does it take?
3. Are there any urgent deadlines I need to know about right now?
4. What temporary arrangements (custody, support, use of the home) are available while the case is pending? *confirm with counsel*
5. [Additional process question from user's situation.]

## Zone 2: My Specific Issues
*(Organized by issue; ask the most urgent first.)*

### Custody / Parenting Time
6. What standard does the court use to decide custody here? *confirm with counsel*
7. What factors will matter most given my situation?
8. What can I do now to support my position on custody?

### Property / Assets
9. How does [jurisdiction] generally approach dividing property acquired during the marriage? *confirm with counsel*
10. What do I need to document about the [home / accounts / other asset]?

### Support (Spousal / Child)
11. How is child support calculated here? Is there a guideline? *confirm with counsel*
12. What factors affect spousal support in this jurisdiction?

### [Other Issue the User Raised]
13. [Question tailored to user's stated concern.]

## Zone 3: Costs, Fees, and Logistics
14. What is your retainer, and how does billing work?
15. What can I do to keep my costs down?
16. How do you prefer to communicate between meetings (email, phone, portal)?
17. What is your typical response time for messages?

## Zone 4: Next Steps and Evaluating Fit
18. What should I do — and gather — before our next meeting?
19. Have you handled cases similar to mine? What should I know about working with you?
20. Based on what I've described, what do you see as the most important issues to address first?
21. Is there anything I haven't asked that you think I should know?

## What to Bring to the Consultation
- [ ] Photo ID
- [ ] Any filed court documents you have received (petition, summons, orders)
- [ ] Marriage/separation dates and the children's names and ages
- [ ] A brief income summary (pay stubs, tax returns if available)
- [ ] A list of major assets and debts (home, accounts, loans) — approximate is fine
- [ ] Any safety-related documents if applicable (police reports, protective orders)
- [ ] This question list
- [ ] Pen and paper or a device to take notes

---
*The attorney provides the answers. Take notes and ask for clarification if anything is unclear.*
*Confirm all legal standards with counsel for your jurisdiction.*
```

---

## Verification

- [ ] Jurisdiction captured and legal concepts in questions flagged *confirm with counsel*?
- [ ] Questions organized into four zones and prioritized within each?
- [ ] What-to-bring checklist included?
- [ ] Attorney-evaluation questions included?
- [ ] Situation-summary section included for efficient context-setting?
- [ ] No answers to the questions generated?
- [ ] No outcome prediction or case-strength assessment?
- [ ] No characterization or motive attribution toward the other party?
- [ ] Any safety/DV dimension screened, routed, and prioritized in the question order?
- [ ] Note included that the attorney may raise issues not covered in the list?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| Answer any question on the list | Generate the question; label it for the attorney to answer |
| "You should get 50/50 custody — ask for it" | Generate: "What custody arrangement is typical in cases like mine here?" |
| "Attorneys usually charge $X — that's normal" | Generate: "What is your retainer and how does billing work?" |
| "Your case sounds strong — bring that up" | Organize facts; assessment is for the attorney |
| Predict how the consultation will go | Prepare the list; what the attorney says is their advice, not ours |
| Tell the user which attorney to choose | Generate evaluation questions; the user decides |
| Skip the what-to-bring checklist | Always include it — arriving unprepared wastes paid time |
| Treat a DV situation as a routine consult prep | Flag the safety dimension; prioritize emergency-order and safety-planning questions |

---

## Adaptations

**By urgency:**
- **Hearing imminent / papers just served:** Move deadline-related and emergency-order questions to the top of Zone 1; pair with `legalprep_hearing_preparation_organizer.md`.
- **Nothing filed yet / early stage:** Emphasize process questions and next-steps questions; pair with `legalprep_court_process_explainer.md`.
- **DV / safety concern:** Prioritize protective-order, emergency custody, and safe-communication questions at the top of all zones.

**By matter type:**
- **Divorce only:** Emphasize property-division, support, and timeline questions in Zone 2.
- **Custody only:** Emphasize best-interests factors, parenting-time, and evaluation/GAL questions in Zone 2; pair with `legalprep_custody_evaluation_preparation_organizer.md`.
- **Post-judgment modification or enforcement:** Replace most Zone 1 process questions with: "What is the standard to modify my current order?" and "How do I enforce an order the other party isn't following?"

**By financial situation:**
- **Limited funds:** Emphasize limited-scope representation, legal-aid eligibility, and cost-reduction questions.
- **Self-represented (pro se):** Ask specifically: "What do I most risk getting wrong if I represent myself?" and "Are there court self-help resources you recommend?"

---

## Related Prompts

- `legalprep_attorney_handoff_brief.md` — the full case-organization package to hand to your attorney after you retain them; use this question builder for the initial consult, then prepare the handoff brief.
- `legalprep_court_process_explainer.md` — build process literacy before you walk in so you can ask better Zone 1 questions.
- `legalprep_deposition_preparation_organizer.md` — if a deposition is upcoming, add deposition-specific questions to Zone 2.
- `legalprep_best_interests_factor_self_map.md` — map your parenting facts to general best-interests categories before the consult so your Zone 2 custody questions are specific.
- `legalprep_financial_disclosure_organizer.md` — organize your financial picture before the consult so your Zone 2 and Zone 3 financial questions are grounded in real numbers.
