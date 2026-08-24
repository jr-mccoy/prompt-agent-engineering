---
title: "Fact Witness Deposition Outline"
category: legal/depositions
description: "Build a topic-organized deposition outline for a fact witness — chronological exhibits, foundation questions, looped impeachment paths, and locked-in admissions tied to elements of claims and defenses."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - legal
  - depositions
  - witness-prep
  - fact-witness
  - examination-outline
updated: "2026-05-08"
related_prompts:
  - domain-legal/depositions/legal_deposition_outline_30b6.md
  - domain-legal/depositions/legal_deposition_summary.md
  - domain-legal/depositions/legal_deposition_witness_prep_script.md
  - domain-legal/litigation/legal_case_strategy_assessment.md
---

**Purpose:** Build an examination outline that walks a fact witness through the topics relevant to the case, locks in admissions tied to specific elements, lays foundation for exhibits, and preserves impeachment material — usable by a single examiner with one reading-pass.

**When to use:** Pre-deposition prep for a witness whose role and relevant knowledge can be mapped from documents and pleadings.

---

## Your Input

- **Witness:** [Name, role, employer, relationship to events]
- **Matter:** [Case caption, claims at issue, posture]
- **Examiner's role:** [Plaintiff or defendant; offensive vs. defensive examination]
- **Key topics the witness can speak to:** [From document review and other discovery]
- **Documents the witness authored, received, or is on:** [Bates ranges; supply text or descriptions]
- **Prior statements:** [Sworn — interrogatory verifications, declarations, prior deps; unsworn — emails, internal communications, public statements]
- **Theories the deposition serves:** [Specific elements you want admissions on; specific affirmative-defense facts to develop]
- **Time budget:** [Hours allotted under controlling rule]
- **Style:** [Funnel-then-pin / chronological / exhibit-driven / hybrid]

---

## Constraints

**Must:**
- Open with **identification, qualifications, and ground rules** sufficient to support every other use of the testimony.
- Build the outline by **topic**, not by document. Documents are tools used inside topics.
- For each topic: state the **purpose** (admission, foundation, impeachment, lock-in), the **target answer**, the **walk-up questions** (foundation), the **closing question** (the lock-in), the **fallback** if the witness evades, the **exhibits** to use, and the **bridge** to the next topic.
- Build a **chronology** of events on the witness's role and use it as the organizing spine for events-based topics.
- Lay **foundation** for every exhibit before reading from it — recognition, authorship/receipt, business-record qualification if needed.
- **Lock in** admissions with closed questions: "So as of {date}, you knew that {fact}. Yes?"
- Preserve **prior-inconsistent-statement** paths: identify each prior statement, the question that surfaces the inconsistency, the impeachment exhibit.
- Build in **time discipline**: per-topic time targets summing within the rule's limit.
- End with a **clean-up section**: privilege instructions ignored, errata-eligible items, and "Are you aware of anyone else who has knowledge of {topic}?"

**Must Not:**
- Lead the witness on direct topics that go to the witness's affirmative knowledge — courts and the rules permit broad latitude in deposition, but leading on key facts on a friendly examination produces weak testimony.
- Read documents to the witness without first laying foundation.
- Ask the witness for legal conclusions ("Was the contract breached?") — ask for facts and let the lawyers argue conclusions.
- Telegraph impeachment so the witness can repair the prior statement before being pinned.
- Stack compound questions; deposition transcripts read worst when the question and the answer are both ambiguous.
- Skip the chronology; without it, the transcript reads in fragments.

---

## Instructions

1. **Pre-deposition prep brief** (top of outline):
   - Witness summary (role, dates, knowledge map)
   - Theory of the case for our side
   - Three things you must come away with
   - Top three risks
   - Time plan
2. **Identification and ground rules.**
3. **Background and qualifications** — sufficient to authenticate and contextualize testimony.
4. **Chronology of events** — walk the witness through the timeline using exhibits in date order.
5. **Topic blocks** — one block per substantive topic. Each block:
   - Purpose
   - Target admission(s)
   - Walk-up questions
   - Closing/lock-in question
   - Exhibits with foundation script
   - Fallback if witness evades
   - Bridge to next topic
6. **Document deep-dives** — for each key exhibit:
   - Authentication
   - Walk-through (date, sender, recipient, subject)
   - Substance — what the witness understood at the time
   - Lock-in
7. **Prior statements** — surface inconsistencies near the topic each statement bears on; do not stack them at the end.
8. **Affirmative defense facts** (if defending) or **damages facts** (if pursuing).
9. **Knowledge attribution** — what was known by whom at what time.
10. **Catch-all** — others with knowledge; documents not yet seen; instructions received from counsel (if not privileged).
11. **Close** — confirm completeness; reserve readback if applicable.

---

## Output Format

```markdown
# DEPOSITION OUTLINE — {Witness} — {Date Set} — Privileged & Confidential — Attorney Work Product

## Witness Summary
- Role / dates: {...}
- Knowledge map: {...}

## Theory of the Case (Our Side)
{One paragraph.}

## Must-Get-Out-of-This-Deposition
1. {Admission tied to element}
2. {Foundation for exhibit}
3. {Lock-in on a fact for MSJ}

## Top Risks
1. {...}
2. {...}

## Time Plan
| Section | Target time |
|---------|-------------|
| Identification + ground rules | 0:15 |
| Background | 0:30 |
| Chronology | 1:30 |
| Topic 1 | 1:00 |
| Topic 2 | 1:00 |
| Documents deep-dive | 1:30 |
| Catch-all | 0:30 |
| **Total** | **6:15 of 7:00** |

---

## I. Identification and Ground Rules
- Name; address; current employer.
- Ground rules (audible answers, not nodding; one question at a time; let me finish; signal a break by asking; you understand you're under oath).

## II. Background and Qualifications
- Education; relevant prior roles; tenure at {employer}; reporting line; team.

## III. Chronology of Events
| Date | Event | Exhibit | Walk-up | Lock-in |
|------|-------|---------|---------|---------|
| {date} | {event} | Ex. {N} | {questions} | "So on {date}, you {fact}. Correct?" |

## IV. Topic Blocks

### Topic 1: {Title — e.g., Knowledge of the Defect Report}
- Purpose: lock in awareness of the defect by {date}.
- Target admission: "By {date}, you had received and reviewed the defect report."
- Walk-up:
  1. Did you know {Engineer} during this period? In what capacity?
  2. Did you exchange emails with {Engineer} about {project}? How frequently?
  3. Were you on the email distribution list {DL}?
- Exhibit foundation:
  - Ex. {N} — Defect Report dated {date}.
    - Q: Do you recognize Ex. {N}? Yes / No.
    - Q: Have you seen it before? When? In what context?
    - Q: Did you receive it in the ordinary course?
- Lock-in: "So you received the defect report on or about {date}, and you read it within {timeframe}. Yes?"
- Fallback if evasive: "Let me direct you to page {X}, where your name appears in the recipient field. Does that refresh your recollection?"
- Bridge: "Let's now look at what you did after receiving that report."

### Topic 2: {Title}
{...}

## V. Document Deep-Dives
- Ex. {A} — {description} — authentication / walk-through / substance / lock-in.
- Ex. {B} — {...}.

## VI. Prior Statements (Impeachment Material)
| Topic | Prior statement | Source / Bates | Question that surfaces inconsistency |

## VII. Affirmative Defense Facts (or Damages Facts)
- {...}

## VIII. Knowledge Attribution
- "Who else knew {fact} by {date}?"
- "Who reported to you on {topic}?"
- "Who reported up to you on {topic}?"

## IX. Catch-All
- Anyone else with knowledge?
- Documents you have not been shown that bear on {topic}?
- Communications with counsel about today (only the existence of, not content).
- Errata practice — reservation.

## X. Close
- "Other than what we've covered, do you have any further information about {claims at issue}?"
- "Have you brought any documents with you to the deposition?"
```

---

## Verification

- [ ] Outline organized by topic, not by document.
- [ ] Every topic has purpose, target answer, walk-up, lock-in, fallback, exhibits, and bridge.
- [ ] Foundation laid for every exhibit before substantive use.
- [ ] Time plan totals within the rule's limit.
- [ ] Prior-statement impeachment paths surface near the topic, not stacked at the end.
- [ ] Catch-all section covers others-with-knowledge and unseen documents.
- [ ] No legal-conclusion questions; questions seek facts.
- [ ] No compound questions in lock-ins.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Outlining by document instead of topic | Documents are tools inside topics; the outline organizes around topics |
| Asking "did you breach the contract?" | Ask for facts; the legal conclusion is for argument |
| Reading from an exhibit before laying foundation | Authenticate first, then read |
| Compound questions | One fact per question; closed questions for lock-ins |
| Stacking impeachment at the end | Surface impeachment when the topic is fresh |
| Forgetting the chronology | Without a chronology, the transcript reads in fragments |
| No fallback for evasive answers | Build the next-question-after-evade into each block |
| Skipping ground rules | Ground rules support every later use of the transcript |
| No time plan | Time runs out before the lock-ins; plan the budget topic by topic |
