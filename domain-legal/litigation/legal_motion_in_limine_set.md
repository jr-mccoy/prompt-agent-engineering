---
title: "Motion in Limine Set Drafter"
category: legal/litigation
description: "Draft a coordinated set of pretrial motions in limine — prior bad acts, settlement evidence, expert exclusions, demonstratives, undisclosed witnesses — calibrated to the controlling evidentiary regime and trial posture."
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
  - evidence
  - motion-in-limine
  - trial
updated: "2026-05-11"
related_prompts:
  - domain-legal/litigation/legal_trial_theme_and_narrative_designer.md
  - domain-legal/litigation/legal_jury_instruction_drafter.md
  - domain-legal/litigation/legal_motion_for_summary_judgment.md
---

**Purpose:** Produce a coordinated motion-in-limine (MIL) set with separately captioned motions, each tied to specific evidence the user expects opposing counsel to offer, grounded in the controlling evidentiary code (FRE or state equivalent) and circuit/state authority supplied by the user.

**When to use:** 30–90 days before trial in civil or criminal cases; after the pretrial order has identified exhibits and witnesses; when the user has specific evidentiary problems to neutralize before opening statements.

---

## Your Input

- **Court / venue:** [Federal district + division, or state court + county]
- **Evidentiary code:** [Federal Rules of Evidence / state equivalent — name the version]
- **Posture:** [Plaintiff / defendant / prosecution / defense]
- **Trial date:** [Date]
- **Identified problem evidence (one row per item):**
  - Source (witness, exhibit number, deposition designation)
  - Substance (what opposing side will try to introduce)
  - Rule(s) implicated (e.g., FRE 404(b), 408, 702, 403)
  - Authority on point (cases, statutes — supplied or `[CITE: ...]`)
- **Local rules / standing orders:** [Page limits, meet-and-confer requirements, deadline for MILs]
- **Demonstratives at issue:** [Charts, animations, summaries — describe]
- **Witness disclosures:** [Status of Rule 26 disclosures or state equivalent]

---

## Constraints

**Must:**
- Draft each motion as a **separately captioned, separately numbered MIL** with its own statement of relief, ready to file as a packet or individually.
- For each motion, identify: (a) the specific evidence sought to exclude, (b) the controlling rule, (c) the relief requested (exclude / limit / require advance notice / order sidebar before mention).
- Track the user's posture — do not draft prosecution-side MILs if user is defense, unless explicitly requested.
- Use placeholders for unsupplied authority: `[CITE: case for FRE 404(b) limiting instruction]`.
- For each motion, propose an alternative narrower relief if the broad exclusion is denied.

**Must Not:**
- Invent case citations, holdings, or rule pinpoints. Use `[CITE: ...]` / `[NEED HOLDING: ...]` when authority not supplied.
- Combine unrelated evidentiary issues into a single motion.
- Treat MILs as substitutes for objections at trial — preserve the objection chain regardless.
- Move to exclude evidence the user has not specifically identified opposing counsel will offer.
- Insert generic "consult counsel" or refusal boilerplate.

---

## Instructions

1. **Inventory the problem evidence.** Build a table: item → rule(s) → desired relief → strength of position.
2. **Cluster by rule.** Group items implicating the same rule, but **do not** combine into one motion unless they share an identical legal theory.
3. **Draft each MIL** with this structure:
   - Caption
   - Introduction (1–2 sentences identifying the evidence and relief sought)
   - Factual background (what the evidence is, how it was disclosed, when)
   - Legal standard (the rule + governing case law placeholders)
   - Argument (apply rule to facts)
   - Proposed alternative relief
   - Conclusion / prayer
4. **Add a master MIL index** listing each motion, the evidence covered, the rule, and the relief sought.
5. **Coordinate across motions.** Flag any conflicts (e.g., asking to exclude a document under 403 while seeking to admit a related document) and resolve them in a coordination note.
6. **Identify reciprocal exposure.** Note any MILs opposing counsel is likely to file against the user's own evidence.

---

## Output Format

```markdown
# MOTION IN LIMINE PACKET — INDEX

| MIL # | Title | Evidence | Rule | Relief Sought |
|---|---|---|---|---|
| 1 | Exclude Evidence of Prior Conviction | Witness X's 2018 misdemeanor | FRE 609(a)(1)(A), 403 | Exclude |
| 2 | Exclude Settlement Negotiations | Email re: 2024 settlement talks | FRE 408 | Exclude |
| ... | ... | ... | ... | ... |

---

## MIL #1 — {Title}

[CAPTION]

### Introduction
{One sentence: evidence + relief}

### Background
{Disclosure history; how evidence emerged}

### Legal Standard
Under {FRE/state rule}, ... [CITE: controlling authority]

### Argument
{Apply rule to specific item}

### Alternative Relief
If the Court declines to exclude entirely, Movant requests {narrower relief — e.g., limiting instruction; advance ruling before mention in opening; sidebar requirement}.

### Conclusion
For the foregoing reasons, Movant respectfully requests {relief}.

---

## Coordination Notes
- {Conflict: MIL #3 asks to exclude X; MIL #7 seeks to admit Y, which references X. Resolution: ...}

## Reciprocal Exposure
- Opposing counsel likely to MIL: {item; user's mitigation plan}
```

---

## Verification

- [ ] Each MIL is independently captioned and could be filed separately.
- [ ] Each motion identifies a specific item of evidence, not categories.
- [ ] Controlling rule cited with subsection-level precision.
- [ ] No invented case citations — placeholders where authority not supplied.
- [ ] Alternative relief proposed for every motion.
- [ ] Coordination conflicts flagged and resolved.
- [ ] Reciprocal exposure section completed.
- [ ] Local-rule constraints (page limits, meet-and-confer) addressed.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Treating MILs as a free-form objection list | Each motion targets a specific item with a specific rule basis |
| Citing FRE 404(b) for character evidence generally | Distinguish 404(a) (character), 404(b) (other acts), and 405 (methods of proof) |
| Asking to exclude all "prejudicial" evidence under 403 | 403 requires unfair prejudice substantially outweighing probative value, not mere harm to one side |
| Confusing FRE 408 (settlement) with FRE 409 (medical payments) | These rules have different scopes and exceptions |
| Moving to exclude expert testimony without specifying Daubert/Frye prong | Identify whether the challenge is qualifications, methodology, reliability, or fit |
| Forgetting that some MIL rulings are advisory and require renewal at trial | Note in each motion which rulings need to be renewed; preserve objections |
| Drafting a single MIL covering ten unrelated items | Split into separate motions; judges grant partial relief more readily when issues are isolated |
| Omitting reciprocal exposure analysis | The user's evidence is equally vulnerable — anticipate opposing MILs |
