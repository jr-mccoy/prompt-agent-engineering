---
title: "Deposition Preparation Organizer (for the Litigant)"
category: legalprep
description: "Help a family-law litigant organize their own factual knowledge of the topics likely to arise in their deposition, and build a prioritized list of questions to ask their own attorney before the deposition. Organizes the user's own information and generates attorney questions only — it does NOT coach testimony, provide legal strategy, or substitute for preparation conducted by the user's attorney. Not legal advice."
techniques:
  - RT-02
  - DS-01
  - NE-09
  - QA-01
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - family-law
  - self-represented
  - divorce
  - custody
  - deposition
  - testimony
  - documentation
updated: "2026-06-05"
related_prompts:
  - domain-legal/family-self-advocacy/legalprep_attorney_handoff_brief.md
  - domain-legal/family-self-advocacy/legalprep_attorney_consultation_question_builder.md
  - domain-legal/family-self-advocacy/legalprep_court_process_explainer.md
  - domain-legal/depositions/legal_deposition_witness_prep_script.md
---

**Purpose:** Help you organize your own factual knowledge — what you know, what you can document, and where you have gaps — across the topics that commonly arise in a family-law deposition. It also generates a prioritized list of questions to bring to your attorney so your preparation sessions are focused and productive. It works on **your own information only**. It does **not** coach what to say or how to say it, advise on legal strategy, or substitute for the witness-preparation session your attorney should conduct with you before you testify.

**When to use:** You have been noticed for a deposition (or expect to be) and want to arrive at your attorney's prep session organized; you want to compile factual notes on the topics so you can discuss them with counsel; you want to generate questions for your attorney about the deposition process and your specific situation.

**When NOT to use:** You want to be coached on exactly how to answer specific questions, what to say to help your case, or what to withhold → that is legal strategy and witness preparation; your attorney conducts that session. There is an active safety emergency → Safety Block first. You have not yet consulted an attorney → see `legalprep_attorney_consultation_question_builder.md` first.

---

## Safety Block

Stop and use a different pathway if:
- There is domestic violence, threats, stalking, or a protective/restraining order → National Domestic Violence Hotline 1-800-799-7233 (US). Deposition content in a DV case carries specific risks; work through counsel and your advocate before organizing anything.
- A child is being abused or is unsafe → Childhelp National Child Abuse Hotline 1-800-422-4453 (US); emergencies 911. Route to your attorney and child protective services immediately.
- You or a child is in crisis → 988 Suicide & Crisis Lifeline (US).

This prompt is educational support for organizing your own records. It is not a substitute for legal, safety, or clinical services.

---

## Scope Boundary — Read First

This **organizes your own factual knowledge and generates attorney questions**. It is **not legal advice, legal strategy, a legal filing, or a substitute for your attorney.** It will **not** coach your testimony, tell you what to say or omit, predict what opposing counsel will ask, advise on what is privileged or not, or assess how your answers will affect your case. **Actual witness preparation is conducted by your attorney** — this tool gets you organized so those sessions are more productive. Deposition rules and procedure **vary by state and country and change over time.** Where a legal concept appears, it is explained in plain language and flagged *confirm with counsel for your jurisdiction.*

---

## Core Principles

1. **Organize facts, not answers.** The output is a topic-by-topic factual inventory — not scripted testimony. What you say under oath is your attorney's preparation domain.
2. **Every fact dated and sourced.** Each item names what happened, when, and the document or record that supports it.
3. **Neutral and factual throughout.** Record what happened; strip characterization, motive, and editorializing.
4. **Gaps are flagged, not filled.** If you do not know or cannot document something, it is listed as `[NEED ...]` — not assumed or invented.
5. **Questions are for your attorney, not the deposition itself.** The questions this tool generates go to your lawyer before the deposition — they are not things to say during testimony.
6. **Witness prep belongs to counsel.** This tool prepares you to walk into that session organized; your attorney prepares you for what happens in the room.
7. **Stop at the boundary.** Factual organizing and attorney questions only. Strategy, privilege, and coaching route to counsel.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Matter type:** [divorce / custody / both]
- **Who is being deposed:** [you / other party / both — focus this organizer on your own deposition]
- **Deposition date/deadline (if known):** [date or "TBD"]
- **Topics you expect to cover:** [finances / parenting / property / timeline of relationship / employment / other — in your words]
- **Documents/records you have related to each topic:** [list, or "see my evidence inventory"]
- **Areas where your memory or documentation is thin:** [describe honestly — gaps flagged, not filled]
- **Questions you already have for your attorney:** [list anything specific]
- **Any safety dimension?:** [if yes → Safety Block / counsel, not this tool]

---

## Constraints

**Must:**
- Require the jurisdiction; use only the facts the user supplies.
- Keep tone neutral and factual; date and source each fact.
- Flag every gap as `[NEED DOCUMENT:]` / `[NEED DATE:]` / `[NEED CLARIFICATION:]`.
- Explain any legal term in plain language flagged *confirm with counsel.*
- Label the attorney-questions section clearly as "Questions for My Attorney — Not for the Deposition."
- Route all strategy, privilege, and coaching questions explicitly to the user's attorney.

**Must Not:**
- Coach the user on what to say, how to phrase answers, what to emphasize, or what to omit.
- Advise on what is or is not privileged, protected, or discoverable.
- Predict what opposing counsel will ask or how the deposition will go.
- Assess how any answer will affect the case outcome.
- Characterize the other party or attribute motive.
- Draft any sworn statement or declaration.
- Fill documentation or memory gaps with assumptions.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Scope
Screen for any safety dimension (route to Safety Block). Restate the matter and the boundary plainly: this organizes factual knowledge and generates questions for counsel; coaching and strategy belong to the attorney.

### Stage 2 — Plain-Language Deposition Overview
Provide a brief, plain-language explanation of what a deposition is (*confirm with counsel for your jurisdiction*): a sworn, out-of-court question-and-answer session; a court reporter transcribes it; the transcript can be used at trial; your attorney should be present; you should answer truthfully and ask for clarification if a question is unclear. Note that specifics of deposition procedure vary by state.

### Stage 3 — Topic-by-Topic Factual Organizer
For each topic the user identifies, organize the facts they know: what happened, when, and the supporting document or record. Use a consistent table format per topic. Flag gaps as `[NEED ...]`.

### Stage 4 — Documentation Gaps Summary
Compile all flagged gaps in one place so the user can gather them before the prep session.

### Stage 5 — Questions for Your Attorney
Generate a prioritized, grouped list of questions for the user to bring to their attorney: about the deposition process, about specific topics, about logistics, and about what to expect. Label this section clearly.

### Stage 6 — Logistics Reminder
Note the practical logistics checklist (confirming date/location/format with counsel; what to bring; what not to bring; self-care before the session) without giving substantive preparation advice — those come from the attorney.

---

## Output Format

```markdown
# Deposition Preparation Organizer — [Your name] · [matter type] · [jurisdiction]
Prepared by [you], [date]. FOR ATTORNEY REVIEW / PRE-PREP SESSION USE.
NOT A LEGAL FILING. Organizes my own facts and generates questions for my attorney.
Actual witness preparation is conducted by my attorney — this document does not coach testimony.

## What a Deposition Is (plain language)
[Brief plain-language note — confirm specifics with your attorney and jurisdiction.]

## My Topic-by-Topic Factual Notes

### Topic: [e.g., Finances / Marital Accounts]
| Date | Fact (my knowledge) | Supporting document |
|---|---|---|
| 2025-04-01 | Joint checking account at [Bank X]; I deposited [amount] on [date]. | Bank statement (attached) |
| [NEED DATE:] | Transfer I recall but cannot locate record for. | [NEED DOCUMENT: bank record] |

### Topic: [e.g., Parenting / Child's Schedule]
| Date | Fact (my knowledge) | Supporting document |
|---|---|---|

### Topic: [e.g., Separation Timeline]
| Date | Fact (my knowledge) | Supporting document |
|---|---|---|

## Documentation Gaps to Obtain Before Prep Session
- [NEED DOCUMENT: ...]
- [NEED DATE: ...]

## Questions for My Attorney — Not for the Deposition
### About the Process
1. [e.g., What is the format and who will be present?]

### About My Specific Topics
2. [e.g., Are there topics I should review more thoroughly?]

### About Logistics
3. [e.g., Where does it take place; how long should I expect it to last?]

### About What to Expect
4. [e.g., What happens if I don't remember something?]

## Logistics Checklist (confirm each with your attorney)
- [ ] Deposition date, time, and location confirmed with counsel
- [ ] Format (in-person / remote) confirmed
- [ ] Documents to bring — ask your attorney what to bring, if anything
- [ ] Organized factual notes delivered to attorney before prep session
- [ ] Prep session scheduled with attorney

---
All questions about what to say, strategy, privilege, and what to expect are for my attorney.
*Confirm procedure and your rights with counsel for your jurisdiction.*
```

---

## Verification

- [ ] Jurisdiction captured and legal concepts flagged *confirm with counsel*?
- [ ] Factual inventory uses dates, sources, and neutral tone throughout?
- [ ] No coaching on what to say, how to phrase answers, or what to omit?
- [ ] No advice on privilege, discoverability, or what opposing counsel will ask?
- [ ] No outcome prediction or case-strength assessment?
- [ ] Gaps flagged `[NEED ...]`, not filled with assumptions?
- [ ] Attorney-questions section clearly labeled as for the attorney, not for the deposition?
- [ ] Strategy and preparation explicitly routed to counsel?
- [ ] Any safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "Say 'I don't recall' if the question is hard" | Organize facts; preparation coaching is your attorney's job |
| "Don't mention X, it will hurt your case" | List facts neutrally; strategy routes to counsel |
| "Opposing counsel will likely ask about Y" | Note the topic; predicting the exam is counsel's domain |
| "This answer is privileged, don't say it" | Flag the topic as "confirm with counsel re: privilege" |
| "Your finances show you contributed more" | Record facts with dates and documents; assessment is for counsel |
| Fill a memory gap with a plausible answer | Flag `[NEED CLARIFICATION:]` for the prep session |
| "You have a strong deposition strategy" | Organize facts; strategy belongs to the attorney |
| Treat a DV dimension as routine paperwork | Stop, Safety Block, route to counsel/advocate |

---

## Adaptations

**By topic weight:**
- **Finance-heavy:** Build a detailed account-by-account factual inventory; pair with `legalprep_financial_disclosure_organizer.md`.
- **Custody-heavy:** Expand the parenting/schedule topic; pair with `legalprep_custody_evaluation_preparation_organizer.md` and `legalprep_best_interests_factor_self_map.md`.
- **Complex timeline:** Pair with `legalprep_case_chronology_builder.md` to feed the timeline topic.

**By posture:**
- **Deposition is imminent:** Prioritize the documentation-gaps section and schedule the attorney prep session immediately.
- **Deposition is weeks out:** Use this to get organized and deliver notes to counsel well before the prep session.
- **High conflict / safety:** Keep everything scrupulously neutral; Safety Block; route immediately to counsel.

---

## Related Prompts

- `legalprep_attorney_handoff_brief.md` — feeds the overall case package your attorney needs.
- `legalprep_attorney_consultation_question_builder.md` — builds questions for a paid consult if you are still selecting counsel.
- `legalprep_court_process_explainer.md` — plain-language map of how depositions fit the overall case timeline.
- `legalprep_case_chronology_builder.md` — feeds the timeline topic in your factual notes.
- `../depositions/legal_deposition_witness_prep_script.md` — the attorney-side preparation script your lawyer may use.
