---
title: "Jury Instruction Drafter"
category: legal/litigation
description: "Draft a complete set of proposed jury instructions for a civil case — preliminary, substantive (claims and defenses with elements), evidentiary, and verdict-form ready — anchored to pattern instructions where supplied."
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
  - litigation
  - jury-instructions
  - trial-prep
  - verdict-form
updated: "2026-05-08"
related_prompts:
  - domain-legal/litigation/legal_case_strategy_assessment.md
  - domain-legal/litigation/legal_complaint_drafter.md
---

**Purpose:** Draft a complete proposed jury-instruction package keyed to the user's claims, defenses, and pattern instructions. Output is filable as plaintiff's or defendant's proposed instructions or as a joint-submission draft.

**When to use:** Trial prep, charge conference preparation, training/evaluation tasks where the parties' theories and elements are bounded.

---

## Your Input

- **Court:** [Federal district / state court]
- **Pattern instruction source:** [e.g., Ninth Circuit Manual of Model Civil Jury Instructions; CACI; New York PJI; Illinois IPI — supply text or page references for relevant instructions]
- **Claims and defenses with elements:** [Per controlling law]
- **Theory of the case for proposing party:** [Plaintiff / defendant theory]
- **Anticipated evidentiary issues:** [Limiting instructions for prior bad acts, settlements, demonstratives, expert testimony, etc.]
- **Verdict form preference:** [General / general with interrogatories / special verdict]
- **Deviation from pattern:** [Where pattern instruction is inadequate or wrong; supply your modifications]
- **Burden allocation:** [Preponderance default; clear-and-convincing for specific claims (e.g., fraud, punitives); shifts on affirmative defenses]

---

## Constraints

**Must:**
- Open with **preliminary** instructions: jury role, evidence vs. argument, credibility, burden of proof.
- Include **substantive** instructions for each claim and each affirmative defense, with elements numbered and the burden assigned.
- Include **damages** instructions appropriate to each claim (compensatory, statutory, punitive — only if available and pleaded), with allocation and avoidance-of-double-recovery instruction if multiple claims overlap.
- Include **limiting** instructions for evidence with restricted use.
- Include **deliberation** instructions: deliberation process, unanimity requirement (or not), Allen-charge availability (note that an Allen charge is given only if needed).
- Include a **verdict form** (general / special) consistent with the instructions.
- For each instruction, cite the **pattern source** with a pinpoint (e.g., "Adapted from CACI 1900").
- Where the user is deviating from a pattern, include a **footnote** explaining the deviation and the supporting authority.

**Must Not:**
- Invent pattern instruction numbers or text. Use only the patterns supplied or note `[NEED PATTERN: {topic}]`.
- Mix burdens within an instruction.
- Combine multiple legal theories in a single instruction without internal demarcation.
- Insert argumentative language ("Defendant's reckless conduct"). Instructions are neutral.
- Use punitive-damages instructions where punitives are not substantively available or not pleaded.
- Skip a limiting instruction the rules of evidence require for evidence that came in for a restricted purpose.

---

## Instructions

1. **Caption** the document: "{Plaintiff/Defendant}'s Proposed Jury Instructions" or "Joint Proposed Instructions (with Disputed Items)."
2. **Numbering.** Number each instruction. Where parties dispute, mark "(Disputed)" and provide both versions.
3. **Sections.**
   - I. Preliminary Instructions
   - II. General Substantive Instructions (credibility, direct/circumstantial, burden of proof)
   - III. Substantive Instructions on Claims and Defenses
   - IV. Damages Instructions
   - V. Evidentiary / Limiting Instructions
   - VI. Deliberation and Verdict
   - VII. Verdict Form
4. **For each substantive claim:** state the elements; identify the party with the burden; identify the standard (preponderance / clear-and-convincing); cite the pattern source with pinpoint.
5. **For each affirmative defense:** state the elements; identify the burden (defendant for most affirmatives); cite pattern.
6. **Damages:** itemize categories; instruct on duty to mitigate; instruct against double recovery; punitive only if applicable, with the controlling-jurisdiction punitive standard and any cap.
7. **Limiting instructions:** for prior bad acts, settlements, insurance, prior consistent statements, expert reports, demonstratives, etc.
8. **Verdict form** matching the instructions; for special verdicts, list the questions in element order with branching.

---

## Output Format

```markdown
{COURT CAPTION}

{PARTY}'S PROPOSED JURY INSTRUCTIONS

I. PRELIMINARY INSTRUCTIONS

Instruction No. 1 — Role of the Jury
{Text — pattern source: ___; pinpoint: ___}

Instruction No. 2 — Evidence vs. Argument
{...}

Instruction No. 3 — Burden of Proof — Preponderance of the Evidence
{...}

II. GENERAL SUBSTANTIVE INSTRUCTIONS

Instruction No. 4 — Credibility of Witnesses
{...}

Instruction No. 5 — Direct and Circumstantial Evidence
{...}

III. SUBSTANTIVE INSTRUCTIONS ON CLAIMS AND DEFENSES

Instruction No. 10 — Plaintiff's Claim for {Claim Name}
To establish this claim, Plaintiff must prove the following elements by {a preponderance of the evidence / clear and convincing evidence}:
1. {element};
2. {element};
3. {element};
4. {element}.

If you find that Plaintiff has proven each of these elements, you must find for Plaintiff on this claim. If you find that Plaintiff has failed to prove any element, you must find for Defendant on this claim.

[Source: {pattern} {pinpoint} — adapted to {jurisdiction's} formulation in {case}.]

Instruction No. 11 — Defendant's Affirmative Defense of {Defense}
To establish this defense, Defendant must prove the following elements by {standard}:
1. ...
2. ...

[Source: ...]

IV. DAMAGES INSTRUCTIONS

Instruction No. 20 — Compensatory Damages
{Categories; mitigation; certainty; non-speculation.}

Instruction No. 21 — No Double Recovery
{...}

Instruction No. 22 — Punitive Damages (if applicable)
{Standard, cap, procedure.}

V. EVIDENTIARY / LIMITING INSTRUCTIONS

Instruction No. 30 — Limiting Instruction on {evidence}
{...}

VI. DELIBERATION AND VERDICT

Instruction No. 40 — Deliberation Process
{...}

Instruction No. 41 — Unanimity / Verdict Form
{...}

VII. VERDICT FORM

{General or special verdict form, structured to mirror the instructions; for special verdicts, branch logic by element.}

---

CERTIFICATE OF SERVICE
{...}
```

---

## Verification

- [ ] Pattern source cited with pinpoint for every instruction (or `[NEED PATTERN: ...]` placeholder).
- [ ] Burden of proof and standard identified for each claim and defense.
- [ ] No argumentative or characterizing language in the instructions.
- [ ] Damages instructions match the claims and the controlling law (punitives only if applicable, with cap and standard).
- [ ] Limiting instructions present for any restricted-use evidence.
- [ ] Verdict form mirrors the substantive instructions and supports the legal-sufficiency review.
- [ ] Disputed items marked and both versions provided.
- [ ] No invented pattern numbers or fabricated case citations.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Mixing preponderance and clear-and-convincing within an instruction | Separate; assign the standard to each element or each issue clearly |
| Drafting punitive-damages instructions without confirming availability | Verify the substantive law and the cap; otherwise omit |
| Combining multiple claims into one instruction | Each claim gets its own instruction with its own elements |
| Using argumentative language | Instructions are neutral; characterization belongs in argument |
| Forgetting limiting instructions for evidence admitted for a restricted purpose | Required by the rules of evidence; absence can produce reversible error |
| Generating a special verdict form that contradicts the general instructions | Verdict form must mirror the instructions' element structure |
| Citing a pattern instruction number you cannot verify | Use only supplied pattern materials or `[NEED PATTERN: ...]` |
| Skipping the no-double-recovery instruction in multi-claim cases | Required to avoid double-counting damages on overlapping theories |
| Failing to allocate the affirmative-defense burden | Defendant typically bears affirmative-defense burden; assign explicitly |
