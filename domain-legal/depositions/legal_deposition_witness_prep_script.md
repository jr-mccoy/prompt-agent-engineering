---
title: "Deposition Witness Preparation Script (Your Own Witness)"
category: legal/depositions
description: "Prepare your own client or aligned witness for deposition — orientation, ground rules, document and topic walk-through, common traps, and a calibrated practice-Q&A set."
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
  - client-prep
  - 30b6-prep
updated: "2026-05-08"
related_prompts:
  - domain-legal/depositions/legal_deposition_outline_witness.md
  - domain-legal/depositions/legal_deposition_outline_30b6.md
  - domain-legal/depositions/legal_expert_deposition_prep.md
---

**Purpose:** Run a structured, multi-session preparation for your own witness — fact witness, party, or 30(b)(6) representative — covering psychology, ground rules, document review, topic walk-throughs, and practice Q&A under realistic conditions.

**When to use:** Before any deposition of a client or aligned witness. For 30(b)(6), use alongside `legal_deposition_outline_30b6.md`. For experts, see `legal_expert_deposition_prep.md`.

---

## Your Input

- **Witness:** [Name, role, capacity (fact / party / 30(b)(6) / hybrid)]
- **Matter and theory:** [Caption, the side's theory of the case in plain English]
- **Topics opposing counsel will probe:** [Best estimate based on notice and prior discovery]
- **Documents the witness authored, received, or is on:** [Bates list]
- **Prior statements:** [The witness's interrogatory verifications, prior depositions, declarations, public statements]
- **Witness-specific risks:** [Tendency to ramble, defensiveness, eagerness to help, prior inconsistent statements, sensitive topics]
- **Time available for prep:** [Hours; days remaining]
- **Format:** [In-person / video — note camera, lighting, and platform considerations]
- **Privilege framing:** [Yes — sessions are at direction of counsel for purpose of providing legal advice; mark accordingly]

---

## Constraints

**Must:**
- Frame prep as **privileged work product** at the open of every session.
- Run **multiple sessions** where time allows: orientation → document walk-through → practice Q&A → final tune-up. Single-session prep is the exception.
- Cover the **psychology** before the technique: most witnesses lose more on attitude (helping too much, arguing) than on substance.
- Teach the **ground rules** as habits, not as a memorized list — listen, pause, answer the question asked, do not guess, do not volunteer, ask for the question to be repeated, take a break before fatigue.
- Walk every **key document** the witness authored or received — the worst surprise in a deposition is being shown a document the witness has not seen since.
- Walk every **prior statement** the witness made — interrogatory verifications, declarations, public statements — and identify any apparent or actual inconsistency.
- Run **practice Q&A** with realistic adversarial pressure, including the lawyer techniques the witness will face: looping, summary mischaracterization, pace acceleration, silence-pressure, document ambush.
- Identify **must-not-rambles**: subjects on which the witness has pulled toward over-explaining; train short answers.
- Calibrate the **30(b)(6)** witness specifically: the corporation's binding answer comes from preparation, not from personal knowledge — train the witness to answer with what the corporation knows.

**Must Not:**
- Tell the witness what to say. Coaching to substantive answers is unethical and discoverable.
- Memorize phrases. Memorized witnesses sound memorized.
- Skip the document walk-through to save time.
- Treat the witness's own interrogatory verification as having been read by the witness — most have not, and seeing it cold during deposition is a frequent inconsistency source.
- Run prep without the witness reviewing the deposition notice and the noticed topics (for 30(b)(6)).
- Spend the prep on adversarial cross when the witness has not first solidified affirmative answers on the case theory.

---

## Instructions

1. **Session 1 — Orientation (60–90 min).**
   - Privilege framing.
   - What a deposition is and is not (no judge; transcript and video; can be used at trial).
   - The case in plain English.
   - The opposing side's theory in plain English.
   - The witness's role in the case theory.
   - Ground rules as habits.
   - Witness questions.
2. **Session 2 — Document Walk-Through (90–180 min).**
   - Walk every relevant document the witness authored or received.
   - For each: orient (date, sender, recipient, subject); refresh substance; identify any phrasing in the document that opposing counsel will pin on; identify any privilege framing.
   - Walk prior statements (interrogatory verifications, declarations, public statements).
3. **Session 3 — Practice Q&A (90–180 min).**
   - Friendly opening Q&A: identification, background, role.
   - Topic-by-topic adversarial Q&A using the most likely opponent moves.
   - Document-with-ambush Q&A: hand the witness a document cold, lay foundation, ask substance.
   - Loop and trap drills: identify the witness's tendency to ramble or argue; cut short.
   - Break and break-rules drill.
   - Debrief: what went well, what did not, what to do differently.
4. **Session 4 — Final Tune-Up (60 min, day before).**
   - Refresh on the three things to remember.
   - Refresh on ground rules.
   - Calm preparation, not new content.
   - Logistics: location, time, dress, breaks, eating, water.
5. **Day-of-Deposition Brief (15 min before).**
   - Settle. Hydrate. Reaffirm three things to remember.
   - Confirm privilege framing for any conversation during breaks.

---

## Output Format

```markdown
# WITNESS PREPARATION PLAN — {Witness} — {Matter}
**Privileged & Confidential — Attorney Work Product**

## Witness Profile
- Capacity: {fact / 30(b)(6) / party / hybrid}
- Role / strengths / risks: {...}
- Format: {in-person / video, platform}

## Theory of the Case (Our Side, in Plain English)
{Two short paragraphs.}

## Theory of the Case (Their Side, in Plain English)
{One short paragraph.}

## The Witness's Role in the Theory
{Two sentences.}

## Three Things to Remember
1. {Behavior — e.g., "Listen to the question asked. Answer the question asked."}
2. {Substance — e.g., "On {topic}, your honest answer is {summary in your own words}."}
3. {Tone — e.g., "You are not the case's lawyer. You don't have to win the deposition."}

## Ground Rules (as habits, not as a script)
- Listen.
- Pause.
- Answer the question asked, not the question you wish were asked.
- Do not guess. "I don't know" and "I don't recall" are honest answers when true.
- Do not volunteer.
- If you don't understand the question, ask for it to be rephrased.
- Take a break when you need one — request it before, not after, fatigue.
- If you realize you misspoke, correct on the record.
- If a question seeks your conversation with counsel, alert counsel. Do not disclose.

## Document Walk-Through Plan
| Bates | Description | Why opposing counsel will use it | Foundation cues | Substance refresh |
|-------|-------------|-------------------------------------|--------------------|---------------------|

## Prior Statements Walk-Through
| Source | Date | Substance | Apparent or actual inconsistency to address |
|--------|------|-----------|----------------------------------------------|

## Topic Walk-Through
| Topic | Honest summary in witness's own words | Likely opposing-counsel angle | Practiced short answer |
|-------|-----------------------------------------|---------------------------------|------------------------|

## Practice Q&A — Calibration Set

### Friendly opening (identification, background)
Q: ... / A: ...
{8–12 exchanges}

### Topic 1 — adversarial
Q (looping): ... / A: ...
Q (mischaracterization): ... / A: ...
Q (silence-pressure): ... / A: ...
Q (document ambush): ... / A: ...
{8–15 exchanges per topic}

### Topic 2 — adversarial
{...}

### Inconsistency-with-prior-statement drill
Q: Earlier today / in your interrogatory response, you said {X}. Now you're saying {Y}. Which is true?
A: {practiced response — usually orient the difference, not collapse}

### "Yes or no" trap
Q: Yes or no — did you ever consider {framed harshly}?
A: I can answer that, but it requires more than yes or no. {clean answer}

### Argument trap
Q: Wouldn't you agree that {opposing characterization}?
A: I wouldn't characterize it that way. {clean factual statement}

## 30(b)(6) Add-On (if applicable)
- Designation: which topics you are designated for.
- Preparation expectations: who you spoke to, what you reviewed.
- Binding effect: your answers bind the corporation on these topics.
- Practiced "we don't know" lines for topics where the corporation truly does not know.

## Logistics
- Date / time / location: {...}
- Wardrobe: {professional, neutral, video-friendly if remote}
- Camera / lighting (remote): {...}
- Breaks: {...}
- Eating / water: {...}

## Day-Of Brief (15 minutes before)
- Three things to remember.
- Hydrate, breathe.
- Confirm privilege framing for break conversations.
```

---

## Verification

- [ ] Privilege framing delivered at every session and noted in the plan.
- [ ] Ground rules taught as habits, not memorized lines.
- [ ] Every key document walked.
- [ ] Every prior statement walked, with inconsistency points identified.
- [ ] Practice Q&A simulates the specific adversarial techniques the witness will face.
- [ ] Witness's tendency-to-ramble subjects identified and trained for short answers.
- [ ] 30(b)(6) preparation expectation made explicit if applicable.
- [ ] Day-of plan minimal and focused on settling, not new content.
- [ ] No coaching to substantive answers; the substance is the witness's honest understanding.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Coaching the witness to specific words | Unethical and discoverable; coach process, not substance |
| Memorized phrases | Sound memorized in transcript; teach habits |
| Skipping the document walk-through | The single most common source of inconsistency at deposition |
| Skipping prior statements | Witnesses rarely remember their own interrogatory verifications |
| Practice Q&A only on friendly direction | Train under the techniques the witness will actually face |
| Not training the witness to take breaks | Fatigue is the largest cause of bad answers |
| Ignoring 30(b)(6) preparation expectations | Personal-knowledge answers from a corporate witness are unprepared answers |
| New content the day of | Day-of is for settling, not learning |
| Not warning about break-conversation privilege | Off-the-record coaching during breaks can be discoverable; advise on the rule in the controlling jurisdiction |
