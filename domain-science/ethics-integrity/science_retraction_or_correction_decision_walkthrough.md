---
title: "Retraction or Correction Decision Walkthrough"
category: science/ethics-integrity
description: "Walk a post-publication problem through the COPE/ICMJE decision logic — severity and whether the core conclusions still hold — to distinguish an erratum, corrigendum, expression of concern, or retraction, then route to the right contacts and draft an honest, non-defensive notice skeleton."
techniques:
  - ST-01
  - RT-01
  - RT-03
  - CM-02
  - QA-01
  - ST-03
difficulty: advanced
tags:
  - retraction
  - correction
  - corrigendum
  - expression-of-concern
  - cope
  - post-publication
  - research-integrity
  - self-correction
updated: "2026-06-26"
related_prompts:
  - domain-science/ethics-integrity/science_image_integrity_self_check.md
  - domain-science/ethics-integrity/science_misconduct_self_audit.md
  - domain-science/ethics-integrity/science_authorship_and_credit_resolver.md
---

# Retraction or Correction Decision Walkthrough

**Objective:** When a problem is discovered in a published work, walk the author through the COPE/ICMJE decision logic — how severe the problem is and whether the paper's core conclusions still hold — to distinguish a correction (erratum vs. corrigendum), an expression of concern, or a retraction. It routes the decision to the people who own it and drafts an honest notice skeleton. It structures the choice and the communication; the journal editor and COPE process make the final determination.

**When to use:** As soon as an author, coauthor, or reader identifies a post-publication error, data problem, image issue, or integrity concern that may require a published notice.

**Required inputs:**
- **Discipline.** <field>
- **Study / manuscript context.** <publication title, venue, what was published, and how it is being used/cited; user-supplied, never invented>
- **Problem description.** <what is wrong, how it was found, and what part of the work it touches, in the user's own words; `[user-supplied]` for anything not stated>

**Optional inputs:**
- Whether the core conclusions still hold given the problem.
- Source of the error (honest mistake vs. publisher production error vs. suspected misconduct).
- Whether an institutional investigation is underway.
- Coauthor awareness and agreement.
- Venue's correction/retraction policy text (if known).

**Constraints — Must:**
- Apply COPE retraction guidelines and ICMJE corrections guidance to separate: **erratum** (publisher/production error), **corrigendum** (author error, minor, conclusions intact), **expression of concern** (serious concern under investigation, outcome pending), and **retraction** (core conclusions invalid, unreliable data, or confirmed misconduct).
- Anchor the decision on two axes: severity of the problem and whether the core conclusions survive it.
- Treat suspected misconduct, fabrication, or invalidating data errors as pointing toward expression of concern or retraction, not a quiet correction.
- Identify who must be contacted (corresponding author, all coauthors, journal editor, and the institution where an investigation may be warranted).
- Draft an honest, non-defensive notice that names precisely what is and is not affected, in calibrated language.

**Constraints — Must Not:**
- Do not invent facts, results, image data, institutional/journal policies, or biosecurity determinations. Work only from user-supplied content; mark gaps `[user-supplied]`.
- This prompt organizes/structures/flags only; it does not give a final biosecurity, legal, or editorial determination, and does not replace the IBC / institutional biosafety / DURC committee / journal editor / COPE process. Route formal decisions there.
- Do not decide guilt, label a person as having committed misconduct, or promise that a venue will accept a particular notice type.
- Do not draft a defensive, minimizing, or blame-shifting notice; honest self-correction is the standard.
- Do not use "novel," "groundbreaking," or "first-ever" in any drafted text.

**Instructions:**

1. **Confirm scope.** Restate the publication, the problem, and how the work is being cited. Mark missing detail `[user-supplied]`.
2. **Assess severity.** Characterize the problem (typographical/production, data/analysis error, image issue, methodological flaw, suspected misconduct) using only stated facts.
3. **Test the conclusions (Tree of Thoughts).** Reason through whether the core conclusions still hold under the corrected facts: hold fully / hold with caveats / do not hold / cannot tell pending investigation. Lay out the branches explicitly.
4. **Run the decision tree.** Map severity × conclusions-status to the notice type: erratum (publisher error) / corrigendum (author error, conclusions intact) / expression of concern (under investigation) / retraction (conclusions invalid or misconduct).
5. **Check for special triggers.** If misconduct is suspected or an investigation is open, route to expression of concern + institution, and note that the editor/COPE leads.
6. **Build the routing plan.** Order the contacts: align coauthors → notify the journal editor in writing → engage the institution where required; note that the editor issues the notice.
7. **Draft the notice skeleton.** Produce an honest notice that states what was published, what is wrong, what is corrected, what remains valid, and what is now uncertain — without defensiveness or blame-shifting.
8. **Emphasize self-correction.** Frame timely, transparent correction as the integrity-preserving action and confirm the editor/COPE owns the final call.
9. **Self-check.** Confirm no fact, policy, or determination was invented and that every gap is `[user-supplied]`.

**Output format (locked):**

```
## Scope Confirmation
[publication, venue, problem, citation/usage; gaps flagged]

## Severity Assessment
[problem type and reach, from stated facts]

## Do the Core Conclusions Hold? (branches)
- Hold fully → ...
- Hold with caveats → ...
- Do not hold → ...
- Cannot tell pending investigation → ...
[selected branch + why]

## Decision-Tree Result
Recommended notice type: [Erratum / Corrigendum / Expression of Concern / Retraction] — rationale (severity × conclusions)
[Special trigger note: misconduct suspected / investigation open → editor + institution lead]

## Routing Plan (who to contact, in order)
- Coauthors (align)
- Journal editor (written notice)
- Institution (if investigation warranted)
- Note: the editor issues the notice; COPE process governs.

## Draft Notice Skeleton (honest, non-defensive)
[What was published] / [What is wrong] / [What is corrected] / [What remains valid] / [What is now uncertain]

## Open Items
- [ ] [user-supplied gap]
```

**Standard alignment:** COPE retraction guidelines (when to retract vs. correct vs. issue an expression of concern) and ICMJE corrections guidance (erratum = publisher error; corrigendum = author error; retraction = invalid conclusions/misconduct); honest self-correction norms; venue-specific correction/retraction policies (verify against the target venue).

**Verification checklist (before delivering):**
- [ ] Discipline and study/manuscript context captured before any recommendation.
- [ ] Severity and conclusions-status assessed from stated facts only.
- [ ] Decision tree explicitly maps severity × conclusions to notice type.
- [ ] Erratum vs. corrigendum distinction tied to publisher- vs. author-error source.
- [ ] Suspected misconduct/open investigation routed to expression of concern + institution.
- [ ] Routing plan names coauthors, editor, and institution; editor owns issuance.
- [ ] Notice skeleton is honest and non-defensive, naming what is and isn't affected.
- [ ] Final call left to editor/COPE, not asserted here.
- [ ] No fact, policy, or determination invented; gaps marked `[user-supplied]`; drafted text free of "novel/groundbreaking/first-ever."

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Under-classifying | Calling an invalidating error a minor corrigendum | If conclusions don't hold, the path is retraction, not correction |
| Quiet fix | Correcting suspected misconduct without escalation | Route to expression of concern + institution; editor/COPE leads |
| Wrong notice label | Using "erratum" for an author's own error | Erratum = publisher error; corrigendum = author error |
| Defensive notice | A skeleton that minimizes or shifts blame | Require honest naming of what is and isn't affected |
| Self-issued verdict | Telling the user their paper "must" be retracted | Recommend and route; the editor/COPE makes the determination |
