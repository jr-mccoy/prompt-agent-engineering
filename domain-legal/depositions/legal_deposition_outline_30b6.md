---
title: "Rule 30(b)(6) Deposition Outline (Corporate Representative)"
category: legal/depositions
description: "Build a 30(b)(6) examination outline that pins each enumerated topic to specific questions, exhibits, and lock-ins, captures the corporation's binding answer, and surfaces preparation deficiencies that justify follow-up relief."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - depositions
  - 30b6
  - corporate-representative
  - examination-outline
updated: "2026-05-08"
related_prompts:
  - domain-legal/depositions/legal_deposition_outline_witness.md
  - domain-legal/discovery/legal_meet_and_confer_letter.md
  - domain-legal/litigation/legal_case_strategy_assessment.md
---

**Purpose:** Build an outline for a Federal Rule 30(b)(6) deposition (or state analog) that walks the corporate designee through each noticed topic, captures the corporation's **binding** answer, and creates a record sufficient to (a) support summary judgment or impeachment and (b) compel re-designation if the corporation prepares the wrong witness or fails to prepare at all.

**When to use:** Examining a corporate party where the responses to written discovery are insufficient or where corporate-knowledge admissions are needed for an element or affirmative defense.

---

## Your Input

- **Notice topics (verbatim):** [The topics noticed under Rule 30(b)(6)]
- **Designee(s):** [Names, roles, and the topics each is designated for]
- **Matter:** [Caption, claims, posture]
- **Examiner's role:** [Plaintiff or defendant]
- **Theories the deposition serves:** [Specific elements / affirmative-defense facts]
- **Documents and prior responses tied to each topic:** [Bates ranges, interrogatory responses, prior testimony]
- **Time budget:** [Per the controlling rule and any agreement; default is 7 hours per Rule 30(d), but 30(b)(6) practice may allocate 7 hours per topic in some courts]
- **Prep questions to ask:** [Whether the witness is prepared adequately for each topic]

---

## Constraints

**Must:**
- Open with a **30(b)(6) framing** colloquy: confirm the witness is appearing on behalf of the entity, has been designated for specified topics, has prepared, and understands that their answers bind the entity on those topics.
- Cover **each noticed topic** in order, with a topic-block that captures the corporation's position fully.
- Within each topic, lay foundation, ask the topic substantively, and **ask preparation questions**: who the witness spoke to, what documents the witness reviewed, what the witness asked but could not learn.
- Where the witness lacks knowledge, **make a clean record of unpreparedness**: the corporation's binding answer is "we don't know" and the predicate facts (no documents, no people consulted) support relief or estoppel.
- Capture **inconsistencies** between the 30(b)(6) testimony and the corporation's prior written discovery responses.
- Address **scope objections** the corporation has lodged (e.g., topic objected to as overbroad) by tightening the question to the in-scope core and asking it.
- Time the outline so that the most consequential topics are not at the end where attention flags.

**Must Not:**
- Drift from the noticed topics. Off-topic questions to a 30(b)(6) witness are personal, not corporate, and may not bind.
- Accept "I don't know personally" as the corporation's answer. The witness speaks for the corporation; the corporation must have prepared.
- Skip the preparation colloquy on each topic. Without it, an unprepared answer is just an unprepared answer; with it, you have grounds for relief.
- Ask the witness for legal conclusions ("Did the corporation breach the contract?"). Ask facts.
- Treat the witness as a fact witness on personal events outside the noticed topics — those are personal capacity and may need a separate deposition.

---

## Instructions

1. **Pre-deposition prep brief**: theory, must-gets, risks, time plan.
2. **Identification and 30(b)(6) framing colloquy.**
3. **Topic-by-topic blocks**, each containing:
   - Notice topic (quoted).
   - Witness designation for this topic (quoted).
   - Preparation colloquy (people consulted, documents reviewed, gaps).
   - Core substantive line.
   - Lock-in.
   - Inconsistency check (against written discovery, prior testimony, public statements).
   - Exhibits with foundation.
4. **Preparation deficiency capture**: at each topic where the witness lacks knowledge, make a clean record:
   - "Did you speak to anyone in preparation for testifying on Topic {N}?"
   - "Whom?"
   - "What did you ask them?"
   - "What documents did you review?"
   - "Did you ask whether anyone in the company has the answer to {specific question}?"
   - "Did you locate that person?"
   - "So as you sit here today, the corporation's answer to that question is 'we do not know'?"
5. **Cross-topic synthesis questions** at the end: themes across topics; consistency.
6. **Catch-all** for related personal-capacity testimony (only if the noticed topics permit, or proceed by separate notice).
7. **Close**: confirm the corporation's positions are the binding answers; reservation of rights.

---

## Output Format

```markdown
# 30(b)(6) DEPOSITION OUTLINE — {Corporation} — {Designee} — {Date}
**Privileged & Confidential — Attorney Work Product**

## Pre-Deposition Brief
- Theory: {...}
- Must-gets: {1, 2, 3}
- Top risks: {...}
- Time plan: {topic minutes summing under cap}

## I. Identification and 30(b)(6) Framing

- Q: You are appearing today on behalf of {Corporation}? A.
- Q: You have been designated by {Corporation} as its representative under Rule 30(b)(6) on the topics in the deposition notice? A.
- Q: For which topics in the notice are you designated? A.
- Q: Do you understand that your answers today will bind {Corporation} on those topics? A.
- Q: Have you prepared to testify on each of those topics? A.
- Q: Do you understand that "I don't know" — if no one at the corporation has prepared you on a topic — is the corporation's binding answer? A.

## II. Topic 1 — {Verbatim notice topic}

### Designation
- Q: Are you the designated representative on Topic 1? A.

### Preparation Colloquy
- Q: To prepare for Topic 1, whom did you speak to? A.
- Q: What did you ask them? A.
- Q: What documents did you review? A.
- Q: Were there any questions about Topic 1 that you tried to answer but could not? A.
- Q: For each, what did you do to find the answer? A.

### Substantive Examination
- Q: {core question 1}
- Q: {core question 2}
- Q: {lock-in}

### Inconsistency Check
- Compare to {written discovery response, prior testimony, public statement}.
- Q: {targeted question that draws out the inconsistency}.

### Exhibits
- Ex. {N} — {description} — foundation script: {...}

### Preparation Deficiency Capture (if needed)
- Q: As {Corporation}'s designated representative on Topic 1, what is the corporation's answer to {specific factual question}?
- A: {witness response}.
- Q: If your answer is "I don't know," is anyone at the corporation able to answer that question?
- Q: Did you ask?
- Q: So the corporation, after reasonable preparation, has no answer to that question?

## III. Topic 2 — {...}
{repeat structure}

## IV. ...

## V. Cross-Topic Synthesis
- {Themes across topics; corporate consistency}

## VI. Close
- Q: For each topic on which you have testified today, is your testimony the corporation's binding answer on that topic? A.
- Q: Are there any topics on which the corporation wishes to supplement? A.
- Reservation of rights for re-designation if preparation is shown to be inadequate.
```

---

## Verification

- [ ] 30(b)(6) framing colloquy delivered up front and revisited at close.
- [ ] Every noticed topic has its own block with preparation colloquy, substantive examination, lock-in, inconsistency check, and exhibits.
- [ ] Preparation deficiency capture script ready for each topic; used where preparation is lacking.
- [ ] Inconsistency check tied to specific prior responses, testimony, or statements.
- [ ] Time plan keeps consequential topics out of the fatigue zone.
- [ ] No drift to non-noticed topics (or acknowledged as personal-capacity).
- [ ] No legal-conclusion questions.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Accepting "I don't know personally" as the corporation's answer | The corporation must prepare; build the record of unpreparedness |
| Skipping the preparation colloquy | Without it, an unprepared answer is just an unprepared answer; with it, it grounds re-designation relief |
| Drifting to off-notice topics | Off-notice questions may yield personal-capacity testimony only |
| Asking legal conclusions of a corporate witness | Ask facts; legal conclusions are not corporate testimony |
| Treating scope objections as ending the inquiry | Tighten to the in-scope core and ask |
| Ending without confirming binding effect | Close with a confirmation question for each topic |
| Failing to compare to prior corporate statements | The inconsistency check is the highest-value move in 30(b)(6) practice |
