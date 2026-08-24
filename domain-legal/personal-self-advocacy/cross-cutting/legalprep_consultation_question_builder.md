---
title: "Consultation Question Builder — Get the Most from an Attorney Meeting"
category: legalprep
description: "Help a layperson build a prioritized list of questions to get the most from a (often paid) attorney consultation about a personal legal matter — the legal questions only a lawyer can answer, the practical logistics, and the fee/scope questions. Matter-agnostic. Organizes the user's own questions only. Does NOT answer the legal questions, assess the matter, predict outcomes, cite law, or draft a filing — those are for the attorney. Not legal advice."
techniques:
  - DS-01
  - ST-02
  - CM-01
  - QA-01
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - self-represented
  - consultation
  - questions
  - attorney
  - preparation
updated: "2026-07-23"
related_prompts:
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_handoff_brief.md
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_personal_legal_chronology_builder.md
  - domain-legal/personal-self-advocacy/cross-cutting/legalprep_incident_documentation_organizer.md
  - domain-legal/litigation/legal_complaint_drafter.md
---

**Purpose:** Help you build a prioritized, well-organized list of questions so a — often paid, often short — attorney consultation gives you the most value. A good question list covers three things: the **legal questions only a lawyer can answer** (is this actionable, what are my options, what would I file, what is it worth), the **practical logistics** (timeline, process, deadlines, what happens next), and the **fee and scope questions** (what this costs, how you are billed, what is and is not included). This organizes **your own questions** — it does **not** answer the legal questions, assess your matter, predict what the attorney will say, tell you whether you "have a case," or cite law. Those are exactly what you are paying the attorney to do.

**When to use:** You have a consultation scheduled (free or paid) and want to walk in prepared; you are choosing between attorneys and want the same questions for each; you have a lot to cover in limited time and need it prioritized so the most important questions come first.

**When NOT to use:** You want this tool to answer the legal questions instead of the attorney → it cannot and will not; that is the attorney's job. You are not sure you even need an attorney or which kind → start with `legalprep_professional_authority_router.md`. You want your facts organized to bring to the meeting → use `legalprep_professional_handoff_brief.md`. There is an active safety emergency → Safety Block first.

---

## Safety Block

Stop and use a different pathway if:
- You are in immediate danger, or a crime is in progress → **911** (US emergency).
- There is stalking, threats, harassment, or domestic violence → **National Domestic Violence Hotline 1-800-799-7233** (US). Do not confront anyone; preserve records securely; involve police and counsel.
- A child is unsafe or being abused → **Childhelp National Child Abuse Hotline 1-800-422-4453** (US); emergencies **911**.
- You or someone else is in crisis → **988 Suicide & Crisis Lifeline** (US).
- The matter is identity theft, fraud, or a scam → **IdentityTheft.gov** / **ReportFraud.ftc.gov** / **ic3.gov** (official reporting channels).

This prompt is educational support for preparing your own questions. It is not a substitute for legal, safety, or law-enforcement services, and it does not answer the questions for you.

---

## Scope Boundary — Read First

This **organizes your own questions for an attorney**. It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney or your jurisdiction's law.** It will **not** answer the legal questions it helps you ask, assess your matter, predict what the attorney will say, tell you whether you "have a case," state a legal conclusion, cite or invent statutes or standards, or draft anything. The answers **vary by state and country and change over time** and are for the attorney — that is the point of the consultation. If a draft question smuggles in an assumed answer ("since this is clearly harassment, ..."), it is rewritten as a neutral open question. Everything here routes *confirm with counsel for your jurisdiction.*

---

## Core Principles

1. **Build the questions; do not answer them.** This tool turns your uncertainty into sharp questions. The attorney supplies the answers.
2. **Prioritize ruthlessly — time is limited (and metered).** Put the questions that most affect your decisions first, so if the clock runs out you got the essentials.
3. **Three buckets: legal, logistical, fee/scope.** Keep the substantive legal questions, the how-does-this-work questions, and the what-does-it-cost questions distinct so none gets skipped.
4. **Open, neutral phrasing.** Ask "Do I have any viable options here, and what are they?" not "How do I win my obviously strong case?" Assumed conclusions produce weaker answers.
5. **Ask about cost and scope explicitly.** Fees, billing structure, retainer, what is included, and likely total range are fair, important questions — build them in.
6. **Capture the answers, don't argue them.** The list includes space to note the attorney's answers and next steps, not to debate them in the room.
7. **You prepare the questions; the attorney answers them.** This never fills in the legal answer itself — even when the user pushes for one.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Type of matter (your best guess):** [workplace / harassment or stalking / defamation / IP / consumer / housing / other]
- **What you most want to walk away knowing:** [in your own words]
- **The decisions this consultation should help you make:** [whether to pursue it / whom to hire / what it will cost / what to do next]
- **What you are unsure or worried about:** [the legal questions, the process, the money]
- **Consultation details:** [free or paid; how long; in person / phone / video]
- **Whether you are comparing attorneys:** [yes/no — if yes, the list doubles as a comparison sheet]
- **Any safety dimension?:** [if yes → Safety Block before anything else]

---

## Constraints

**Must:**
- Require the jurisdiction; build questions only from the user's own concerns.
- Organize questions into three buckets: legal, logistical, and fee/scope.
- Prioritize the list so decision-critical questions come first.
- Phrase every question as open and neutral; rewrite any that assume an answer.
- Include explicit fee, billing, retainer, and scope questions.
- Include space to capture the attorney's answers and next steps.
- Route every substantive legal question to the attorney — never answer it here.

**Must Not:**
- Answer any legal question, or hint at the "right" answer.
- Assess the matter, predict what the attorney will say, or say whether the user "has a case."
- State a legal conclusion or cite/invent statutes, standards, or fee amounts.
- Characterize the other party, attribute motive, or apply a label.
- Draft a pleading, letter, or the substance of the matter.
- Fill in facts the user did not provide, or coach the user to argue with the attorney.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Task
Screen for any safety dimension (route to Safety Block if present). Restate the matter type and jurisdiction. State the boundary: this builds the questions; the attorney answers them — this tool will not.

### Stage 2 — Surface What the User Needs to Decide
Reflect back the decisions the consultation should support (whether to pursue, whom to hire, cost, next steps). Questions that drive these decisions become the top priorities.

### Stage 3 — Build the Legal-Questions Bucket
Turn the user's uncertainties into open legal questions for the attorney: viability and options, what a process would look like, what could be recovered or achieved, risks and downsides. Phrase neutrally; do not answer any of them.

### Stage 4 — Build the Logistics Bucket
Draft practical questions: how the process works and how long it takes, any deadlines or time-sensitive steps, what the attorney needs from the user, what happens after the meeting, how the user should preserve or gather more.

### Stage 5 — Build the Fee & Scope Bucket
Draft explicit money and scope questions: consultation cost, fee structure (hourly, flat, contingency), retainer, estimated total range, what is included and excluded, who does the work, and how billing is communicated.

### Stage 6 — Prioritize, Add Capture Space, and Route Out
Order all questions with decision-critical ones first. Add a place to note answers and next steps. Point the user to `legalprep_professional_handoff_brief.md` to bring their organized facts to the meeting. Reaffirm that the answers come from the attorney.

---

## Output Format

```markdown
# Consultation Questions — [Your name] · [matter] · [jurisdiction]
Prepared by [you], [date]. FOR MY OWN PREP — NOT LEGAL ADVICE.
Organizes my questions. Does NOT answer them, assess the matter, or say whether I "have a case" —
that is what I am asking the attorney.
Consultation: [free/paid] · [length] · [in person/phone/video]

## Top Priorities (ask these first — they drive my decisions)
1. [The single most decision-critical question.]
2. [...]

## A. Legal Questions (for the attorney to answer)
- Do I appear to have any viable options here, and what are they?
- What would the process look like, at a high level?
- What could realistically be achieved or recovered — and what are the risks/downsides?
- Is anything time-sensitive I should know about?
- What are the strongest and weakest parts of my situation, in your view?

## B. Logistics & Process
- How long does a matter like this typically take?
- What do you need from me, and by when?
- What happens right after this meeting if I move forward?
- How should I preserve or gather more evidence in the meantime?
- How and how often will we communicate?

## C. Fees & Scope
- What does this consultation cost, and how am I billed after?
- Is this hourly, flat fee, or contingency — and what is the estimated total range?
- Is a retainer required, and how much?
- What is included in your fee, and what is extra?
- Who actually does the work (you, an associate, a paralegal)?

## Answers & Next Steps (fill in during/after)
| Question | Attorney's answer | Next step / who owns it |
|---|---|---|
| [Q] | [note it — don't argue it] | [action + date] |

---
The answers to Section A are for the attorney. *Confirm with counsel for your jurisdiction.*
```

---

## Verification

- [ ] Jurisdiction captured and everything flagged *confirm with counsel*?
- [ ] Questions organized into legal, logistical, and fee/scope buckets?
- [ ] List prioritized so decision-critical questions come first?
- [ ] Every question open and neutral — none assuming an answer?
- [ ] Explicit fee, billing, retainer, and scope questions included?
- [ ] Space included to capture the attorney's answers and next steps?
- [ ] No legal question answered and no "right answer" hinted?
- [ ] No matter assessment, outcome prediction, or "you have a case"?
- [ ] No legal conclusion, cited/invented statute, standard, or fee amount?
- [ ] No characterization of the other party?
- [ ] Substantive legal questions routed to the attorney?
- [ ] Any safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "You have a strong case — ask how much you'll get" | "Do I appear to have viable options, and what are they?" — open, unanswered |
| Answer "yes, that's illegal" inside a question | Leave it as a question for the attorney |
| "Since this is clearly harassment, ..." | Rewrite neutrally: "How would you assess what happened here?" |
| Skip the money questions to be polite | Build explicit fee, retainer, and scope questions in |
| Estimate what the attorney will charge | Ask the attorney; do not invent a fee amount |
| "He obviously did this on purpose — ask about damages" | Strip motive; ask "What could realistically be recovered, and what are the risks?" |
| Coach arguing with the attorney's answer | Capture the answer; decide afterward |
| Treat a safety emergency as meeting prep | Stop, follow the Safety Block, call 911 / report first |

---

## Adaptations

**By matter type:**
- **Workplace:** Add questions about internal reporting vs. an agency vs. a lawsuit and about any deadlines; the attorney-side counterparts include `../../employment-labor/legal_eeoc_position_statement_drafter.md`.
- **Defamation / something posted:** Add questions about takedown vs. legal action and about cost realism; the attorney-side counterpart is `../../ip/legal_defamation_publicity_risk_screen.md`.
- **IP / copyright:** Add DMCA-vs-litigation questions; attorney-side `../../ip/legal_copyright_fair_use_analysis.md` and `../../ip/legal_trademark_clearance_analysis.md`.
- **Consumer / housing:** Add small-claims-vs-attorney and cost-vs-recovery questions.

**By situation/profile:**
- **Comparing attorneys:** Use the same list for each and note answers side by side; fee/scope answers become the comparison.
- **Cost-constrained:** Foreground Section C and ask about legal aid, sliding scale, or limited-scope ("unbundled") representation.
- **Time-limited consult:** Trim to Top Priorities plus a few from each bucket so the essentials are covered first.

---

## Related Prompts

- `legalprep_professional_handoff_brief.md` — bring your organized facts to the meeting alongside these questions.
- `legalprep_professional_authority_router.md` — use first if you are unsure you need an attorney or which kind.
- `legalprep_personal_legal_chronology_builder.md` — the timeline you bring so the attorney can answer efficiently.
- `legalprep_incident_documentation_organizer.md` — the incident records that ground your legal questions.
- `../../litigation/legal_complaint_drafter.md` — the attorney-side counterpart if a matter proceeds to court.
