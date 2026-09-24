---
title: "Appellate Issue Selection Memo — Preservation, Standard of Review, Strength, and Narrative Fit"
category: legal/appellate
description: "Screen every candidate appellate issue from a trial record for preservation, standard of review, harmless-error exposure, merits strength, and fit with a single appellate narrative — then recommend which issues to raise, lead with, or drop, citing the record and only user-supplied authority."
techniques:
  - ST-01
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - appellate
  - issue-selection
  - preservation
  - standard-of-review
  - harmless-error
updated: "2026-09-24"
related_prompts:
  - domain-legal/appellate/legal_statement_of_facts_builder.md
  - domain-legal/appellate/legal_petition_for_review_drafter.md
  - domain-legal/research/legal_issue_spotter_from_facts.md
  - domain-legal/research/legal_research_memo_irac.md
---

**Objective:** Produce a decision memo that takes every candidate error from the record, tests each against the gates an appellate court will apply — appealability, preservation, standard of review, prejudice/harmlessness — and against merits strength and narrative fit, then recommends a final issue list and order with the reasons for each inclusion and each cut.

**When to Use:** After the notice of appeal and before briefing; after the record (transcripts, clerk's record/appendix) is complete; when trial counsel hands off to appellate counsel with a long list of complaints; when deciding whether a cross-appeal or conditional issue is worth raising.

**Distinct from:**
- `domain-legal/research/legal_issue_spotter_from_facts.md` — spots claims from raw facts before litigation; this memo screens rulings already made on a closed record.
- `domain-legal/research/legal_research_memo_irac.md` — deep research on one issue; this memo triages many issues, and its survivors may then get IRAC memos.
- `domain-legal/litigation/` prompts — trial-level civil work; this memo applies appellate gates (civil or criminal appeals).

---

## Your Input

- **Appellate court and jurisdiction:** [Court, circuit/district — required]
- **Case type and posture:** [Civil / criminal; appellant / appellee / cross-appellant; final judgment / interlocutory]
- **Judgment or order appealed and date of entry:** [As entered]
- **Candidate issues:** [One row per issue: ruling, where in the record (transcript page, docket entry), objection or motion made, ruling text]
- **Post-trial motions:** [Filed, grounds, rulings — often determine preservation]
- **Authority supplied:** [Standard-of-review and preservation authority the user has verified for this court]
- **Client objectives:** [New trial, reversal and rendition, sentence reduction, narrowing, precedent]
- **Brief constraints:** [Word limit, deadline — as supplied]

---

## Constraints

**Must:**
- Screen each issue through the gates **in order**: (1) appealability/jurisdiction of this ruling, (2) preservation (objection made, specific ground, ruling obtained, renewed if required), (3) standard of review, (4) prejudice / harmless-error or plain-error posture, (5) merits strength, (6) narrative fit, (7) remedy obtained if won.
- Cite the record for every preservation finding (`R. 412:8–15`, `ECF 87`).
- State each standard of review with user-supplied authority or `[VERIFY SoR: {issue type} in {court}]` — never assign a standard from memory.
- Identify issues that are **mixed questions** or have components reviewed under different standards.
- Score strength qualitatively (Strong / Arguable / Weak) with the reason in one sentence.
- Recommend a final list (typically a small number of issues), lead issue, and order; explain every cut.
- Flag issues that must still be raised to avoid waiver for later proceedings (e.g., further review or collateral review) `[VERIFY: preservation-for-further-review rule]`.

**Must Not:**
- Invent standards of review, preservation rules, jurisdictional deadlines, or case law.
- Treat an unpreserved issue as reviewable under the ordinary standard; route it to plain-error or equivalent analysis only if the user supplies that framework.
- Recommend raising every colorable issue; weak issues dilute strong ones.
- Characterize a ruling not in the record supplied.
- Add "consult an attorney" boilerplate.

---

## Method

1. **Issue inventory.** One row per candidate ruling with record cite.
2. **Gate screen.** Run gates 1–4; issues failing gate 1 or clearly failing gate 2 go to a "not viable" list with reasons.
3. **Merits and prejudice.** For survivors, state the error theory in one sentence, the strongest record facts, and the harm theory.
4. **Narrative fit.** Draft a one-sentence theme for the appeal; mark each issue as Core / Supporting / Off-theme.
5. **Remedy check.** What relief does winning each issue produce? Prefer issues whose remedy matches client objectives.
6. **Recommendation.** Final list, order, lead issue, word budget allocation, and cut list.
7. **Research queue.** For each surviving issue, the authority still needed (`[CITE]`, `[NEED HOLDING]`).

---

## Output Format

```markdown
# APPELLATE ISSUE SELECTION MEMO — {Case} — {Court}

## 1. Theme
{One sentence the brief will prove.}

## 2. Screening Matrix
| # | Issue | Record cite | Appealable? | Preserved? (cite) | SoR [VERIFY] | Harm posture | Strength | Narrative fit | Remedy |

## 3. Issue Notes (survivors)
### Issue {n}: {one-line error theory}
- Preservation: {...}
- Standard of review: {...} [authority or VERIFY]
- Best record facts: {...}
- Harm theory: {...}
- Strongest counterargument: {...}

## 4. Not Viable / Cut
| Issue | Reason (gate failed or dilution) | Preserve anyway? |

## 5. Recommendation
- Lead: {...}
- Order: {...}
- Word budget: {...}

## 6. Research Queue
- {Issue} — {authority needed}
```

---

## Worked Example (abbreviated)

**Input:** Civil appeal by defendant after a jury verdict for plaintiff. Candidate issues: (1) denial of a motion to exclude plaintiff's damages expert; (2) a jury instruction on causation — trial counsel objected at the charge conference on one ground and argues a different ground now; (3) denial of JMOL on causation, renewed post-verdict; (4) admission of a photograph; (5) remark in closing, no objection.

**Output excerpt:**
- Theme: "Plaintiff never proved causation with admissible evidence."
- Issue 3 (JMOL) — preserved by pre-verdict motion and renewed post-verdict (ECF 142, ECF 160); SoR `[VERIFY SoR: JMOL denial in {circuit}]`; Strong; Core; remedy: rendition. **Lead.**
- Issue 1 (expert) — preserved (ECF 98, ruling ECF 110); SoR `[VERIFY: abuse-of-discretion framing for expert rulings in {circuit}]`; Arguable; Core (without the expert, causation fails).
- Issue 2 (instruction) — ground argued now differs from the charge-conference objection (Tr. 988:4–20) → preservation problem; route to plain-error only if authority supplied; Weak; Supporting → **cut**, but note it in case of further review `[VERIFY]`.
- Issues 4 and 5 — Off-theme; issue 5 unpreserved → cut.

---

## Verification

- [ ] Court and jurisdiction locked; posture stated.
- [ ] Every issue screened through all gates in order.
- [ ] Every preservation finding has a record cite.
- [ ] No standard of review or preservation rule stated without supplied authority or `[VERIFY]`.
- [ ] Recommendation limited to issues that serve the theme and client objectives; every cut explained.
- [ ] Remedy for each surviving issue matches the relief sought.
- [ ] Research queue lists every open placeholder.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Raising every colorable error | Cut issues that are weak, off-theme, or yield no useful remedy; explain cuts |
| Assuming an objection preserved a different ground | Compare the ground argued at trial (cite) with the ground on appeal |
| Stating "de novo" or "abuse of discretion" from memory | Use supplied authority or `[VERIFY SoR]` per issue |
| Ignoring harmless error | Every survivor gets a harm theory and the strongest harmlessness counter |
| Treating a post-trial motion as optional for preservation | Check whether renewal or a post-trial motion is required `[VERIFY]` and cite the record |
| Leading with the most emotionally compelling but weakest issue | Lead with the strongest issue that yields the best remedy |
| Overlooking appellate jurisdiction for an interlocutory ruling | Gate 1 is screened first for every issue |
