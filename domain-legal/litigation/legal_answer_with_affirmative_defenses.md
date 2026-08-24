---
title: "Answer with Affirmative Defenses"
category: legal/litigation
description: "Draft a defendant's answer to a civil complaint — paragraph-by-paragraph admissions/denials, affirmative defenses pleaded with factual content, counterclaims/cross-claims if applicable, and prayer."
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
  - litigation
  - answer
  - affirmative-defenses
  - pleading
updated: "2026-05-08"
related_prompts:
  - domain-legal/litigation/legal_complaint_drafter.md
  - domain-legal/litigation/legal_motion_to_dismiss_12b6.md
  - domain-legal/research/legal_issue_spotter_from_facts.md
---

**Purpose:** Generate a defendant's answer that responds to each numbered paragraph of the complaint, pleads affirmative defenses with factual support sufficient to survive a motion to strike under the controlling pleading standard, and preserves all available counterclaims, cross-claims, or third-party claims.

**When to use:** After a complaint is served, after a motion to dismiss is denied or partially denied, or after an amended complaint. Also for training/evaluation tasks.

---

## Your Input

- **Court / venue:** [Federal / state, with district or county]
- **Pleading standard for affirmative defenses in this jurisdiction:** [Notice / plausibility — many courts require Twombly/Iqbal-level factual support for affirmative defenses; specify the local rule or default]
- **Complaint text (paragraph-by-paragraph):** [Paste numbered paragraphs]
- **Defendant's position on each paragraph:** [Admit / deny / lack knowledge — at the user's level of granularity, by paragraph or by paragraph segment]
- **Operative facts within defendant's knowledge:** [What defendant knows]
- **Available affirmative defenses:** [User-supplied list, or "identify candidates from the complaint and the facts"]
- **Counterclaims / cross-claims / third-party claims:** [If any]
- **Jury demand:** [Yes / no — defendant may demand even if plaintiff did not]

---

## Constraints

**Must:**
- Respond to **every numbered paragraph** of the complaint. Do not skip.
- Use a permitted response for each: admit / deny / admit in part and deny in part / deny for lack of knowledge sufficient to form a belief (where good-faith basis exists).
- Where a paragraph contains both factual and legal-conclusion content, separately address each segment.
- Plead affirmative defenses **with factual content** sufficient under the controlling standard. List each defense in its own numbered section.
- Reserve the right to assert additional affirmative defenses as discovery proceeds, where local rules permit such reservation.
- Include any **counterclaims, cross-claims, or third-party claims** as separate sections, each pleaded as a complaint would be.
- Include the prayer for relief and signature block.

**Must Not:**
- Use a "general denial" unless the rules of the jurisdiction permit it for verified complaints (rare in federal court; varies by state).
- Plead a stack of conclusory affirmative defenses ("estoppel; laches; waiver; unclean hands…") without facts; many courts strike these.
- Deny matters within the defendant's own knowledge by claiming lack of knowledge.
- Admit legal conclusions; respond that the paragraph "states a legal conclusion to which no response is required, and to the extent a response is required, denied."
- Plead affirmative defenses inconsistent with the answer's denials without acknowledging alternative pleading.
- Waive defenses by failing to plead them — Rule 8(c) and analogs require pleading or they are forfeited.

---

## Instructions

1. **Caption** matching the court's local rules. Title: "Answer, Affirmative Defenses, and Counterclaims" (or subset).
2. **Preamble:** "Defendant {Name}, by and through undersigned counsel, hereby answers the Complaint as follows:"
3. **Paragraph-by-paragraph response.** For each numbered paragraph in the complaint, produce one numbered paragraph in the answer with the response. Where the paragraph mixes factual and legal-conclusion content, segment.
4. **Affirmative Defenses.** Each defense:
   - Numbered.
   - Caption with the defense name (e.g., "First Affirmative Defense — Statute of Limitations").
   - Factual basis sufficient to give the plaintiff notice and to satisfy the local pleading standard.
5. **Counterclaims / Cross-claims / Third-party claims** (if any). Plead as a complaint would be — jurisdiction, parties (if new), facts, claims with elements tied to facts, prayer.
6. **Jury demand** for any new claims if not already preserved.
7. **Prayer for relief**: dismissal, costs, fees, jury trial preservation, any affirmative relief on counterclaims.
8. **Signature block** with bar number and certification placeholders.

---

## Output Format

```markdown
{COURT CAPTION}

ANSWER, AFFIRMATIVE DEFENSES, AND COUNTERCLAIMS

Defendant {Name}, by and through undersigned counsel, hereby answers the Complaint as follows. Each numbered paragraph below corresponds to the same-numbered paragraph of the Complaint.

I. RESPONSE TO ALLEGATIONS

1. {Admit / Deny / ...}
2. Defendant admits {portion}; denies {portion}; lacks knowledge sufficient to form a belief as to the truth of {portion}.
3. The allegations of paragraph 3 state a legal conclusion to which no response is required. To the extent a response is required, denied.
{Continue for every numbered paragraph}

II. AFFIRMATIVE DEFENSES

Defendant asserts the following affirmative defenses, without conceding that the burden of proof on any such defense rests with Defendant where it does not.

FIRST AFFIRMATIVE DEFENSE — Statute of Limitations
{Numbered factual content showing the claim accrued more than the limitations period before filing.}

SECOND AFFIRMATIVE DEFENSE — Failure to State a Claim
{Factual content; preservation of Rule 12(h)(2) defense.}

THIRD AFFIRMATIVE DEFENSE — {...}
{...}

Defendant reserves the right to assert additional affirmative defenses as they become known through discovery, to the extent permitted by the rules of this Court.

III. COUNTERCLAIMS (if applicable)

{Plead as a complaint: jurisdiction, parties, facts, counts with elements, prayer.}

IV. JURY DEMAND

Defendant demands trial by jury on all issues so triable.

V. PRAYER FOR RELIEF

WHEREFORE, Defendant respectfully requests that this Court:
A. Enter judgment in favor of Defendant on all counts of the Complaint;
B. Dismiss the Complaint with prejudice;
C. Award Defendant costs and attorneys' fees as permitted by law or contract;
D. {Affirmative relief on counterclaims, if any};
E. Grant such further relief as the Court deems just and proper.

Dated: {date}                       Respectfully submitted,

                                    /s/ {attorney name}
                                    {Bar No.}, {Firm, contact}
                                    Counsel for Defendant
```

---

## Verification

- [ ] Every numbered paragraph of the complaint has a response.
- [ ] Mixed paragraphs are segmented in the response.
- [ ] No "lack of knowledge" responses on matters within defendant's own knowledge.
- [ ] Affirmative defenses include factual content; no naked-label stacking.
- [ ] Each affirmative defense captioned with its name.
- [ ] All known affirmative defenses preserved (Rule 8(c) and analogs).
- [ ] Counterclaims pleaded as a complaint would be, with jurisdiction and elements.
- [ ] Jury demand preserved if applicable.
- [ ] No admissions of legal conclusions.
- [ ] Signature block and certification placeholders present.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Stacking conclusory affirmative defenses ("laches; estoppel; unclean hands") | Plead each with factual content; courts increasingly strike naked labels |
| Using "lack of knowledge" for matters in the defendant's own files | Improper; either admit or deny based on a reasonable inquiry |
| Admitting a paragraph that mixes a fact with a legal conclusion | Segment — admit the factual portion, deny the legal-conclusion portion |
| Forgetting to plead Rule 8(c) defenses | Failure to plead an affirmative defense generally waives it |
| Treating Rule 12(b)(6) failure-to-state-a-claim as un-pleadable post-answer | Preserve via Rule 12(h)(2) — judgment on the pleadings still available |
| Admitting jurisdictional allegations to "be cooperative" | Jurisdictional admissions are usually fine but verify before conceding personal jurisdiction or venue if you intended to challenge |
| Failing to demand a jury for new counterclaims | Counterclaims can require a separate jury demand |
| Filing without checking statute-of-limitations clock and tolling facts | Limitations is the most commonly overlooked dispositive defense |
