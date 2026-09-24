---
title: "Sentencing Memorandum — §3553(a) Factors, Guideline Objections, and Mitigation"
category: legal/criminal
description: "Draft a defense (or government) sentencing memorandum that addresses the guideline calculation and objections, walks each 18 U.S.C. §3553(a) factor (or the state's sentencing factors) with record-supported facts, integrates mitigation and character letters, and requests a specific, justified sentence — with no invented guideline values, variance statistics, or case law."
techniques:
  - ST-01
  - ST-02
  - DS-01
  - RT-05
  - QA-01
difficulty: advanced
tags:
  - legal
  - criminal
  - sentencing
  - mitigation
  - section-3553a
  - variance
  - client-convicted
updated: "2026-09-24"
related_prompts:
  - domain-legal/criminal/legal_plea_offer_analysis.md
  - domain-legal/litigation/legal_trial_theme_and_narrative_designer.md
  - domain-legal/research/legal_research_memo_irac.md
  - domain-legal/client-intake-communications/legal_client_status_update_memo.md
---

**Objective:** Produce a sentencing memorandum that (1) resolves the guideline calculation with specific objections to the presentence report (PSR), (2) applies each statutory sentencing factor to documented facts about the offense and the person, and (3) asks for a specific sentence the court can adopt, supported by a coherent mitigation narrative and exhibits.

> **Scope guard — attorney-facing only.** For licensed counsel on the matter (defense counsel, or the prosecutor where a government posture is offered). If the person running it appears to be an unrepresented defendant or a family member, stop and route them to the public defender's office or appointed counsel, or to `domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md`, rather than producing strategy. This guard is not a disclaimer; the ban on "consult an attorney" boilerplate below still applies.

**When to Use:** After a plea or verdict and receipt of the draft or final PSR; before the objection and memorandum deadlines set by local rule or the court's order; for government counsel responding to a defense variance request (posture switch).

**Distinct from:**
- `domain-legal/criminal/legal_plea_offer_analysis.md` — pre-plea exposure comparison; this prompt is post-conviction advocacy.
- `domain-legal/litigation/legal_trial_theme_and_narrative_designer.md` — jury-facing theme at trial; sentencing narrative is judge-facing and must account for the whole person and the offense.
- `domain-legal/research/legal_research_memo_irac.md` — research on a variance or departure issue can feed this memo; this prompt drafts the filing.

---

## Your Input

- **Jurisdiction and system:** [Federal (state Guidelines Manual edition used by PSR) / state guidelines / indeterminate — required]
- **Posture:** [Defense / government]
- **Offense(s) of conviction and plea/verdict terms:** [Including any stipulations or sentencing agreements]
- **PSR:** [Offense-level calculation, criminal history, paragraphs the user disputes, probation's recommendation]
- **Mitigation record:** [Personal history, health, mental health, substance use, employment, family obligations, military service, post-offense rehabilitation, conduct on release — each with its source document]
- **Character letters:** [Authors, relationship, key content]
- **Victim impact / restitution:** [As applicable]
- **Requested sentence:** [Custody, alternatives, supervision conditions, recommendations for BOP programming or facility placement]
- **Authority supplied:** [Cases, policy statements, statistics sources the user has verified]
- **Local rules:** [Deadlines, page limits, sealing procedure for sensitive exhibits]

---

## Constraints

**Must:**
- Separate **guideline objections** (legal/factual challenges to PSR paragraphs) from **departure** and **variance** arguments; label each correctly for the jurisdiction. Treat departures as conditional: include a departure ground only if the current Manual still provides for it `[VERIFY: current Manual's departure framework — most departures were removed effective Nov. 1, 2025]`; otherwise present the same facts as §3553(a) variance grounds.
- For each objection: PSR ¶ → what it says → why it is wrong (fact or law) → correct calculation → effect on range.
- Walk each statutory factor — for federal cases the §3553(a) factors: nature and circumstances of the offense and history and characteristics of the defendant; the purposes of sentencing (just punishment, deterrence, protection of the public, rehabilitation); kinds of sentences available; the guideline range and policy statements; unwarranted disparities; restitution — using facts from the record and exhibits.
- Tie every mitigation fact to an exhibit (letter, record, report) and propose sealing for medical, mental-health, or minor-related material.
- Request a specific sentence and explain why it is "sufficient but not greater than necessary" (federal) or the state analog.
- Use disparity data only if the user supplies the source and figures.

**Must Not:**
- Invent guideline values, offense-level adjustments, policy-statement text, disparity statistics, or case citations. Use `[CITE: ...]`, `[VERIFY: ...]`, `[NEED SOURCE: ...]`.
- Minimize the offense or contradict facts admitted at plea or found at trial.
- Quote a character letter beyond what the user supplies, or embellish its content.
- Disclose sealed or sensitive material in the public body of the memo.
- Add "consult an attorney" boilerplate.

---

## Method

1. **Calculation table.** Reproduce the PSR calculation and a parallel column with the user's position; show the range under each.
2. **Objections.** Draft each objection as its own numbered section with record support.
3. **Theory of the sentence.** One paragraph: who the client is, how the offense happened, why the requested sentence serves each purpose of sentencing. Every later section must support it.
4. **Factor-by-factor application.** Apply each statutory factor with cited facts; acknowledge aggravating facts and answer them.
5. **Alternatives and conditions.** Propose conditions tailored to identified risks (treatment, employment, restitution plan) to show the requested sentence protects the public.
6. **Exhibit list and sealing plan.**
7. **Government-posture switch (if selected).** Same structure; address the defense's likely variance grounds and why the range (or a higher sentence) is warranted.

---

## Output Format

```markdown
[CAPTION]
{DEFENDANT'S / GOVERNMENT'S} SENTENCING MEMORANDUM

## I. Introduction and Requested Sentence
{Specific request; theory of the sentence in one paragraph.}

## II. Guideline Calculation
| Component | PSR ¶ | PSR position | Our position | Basis |
**Resulting range:** PSR {...} / Ours {...}

### Objection 1 — PSR ¶{n}: {issue}
{Record support; law [CITE]; corrected calculation.}

## III. Departure Grounds (only if the current Manual still provides for them) [VERIFY: current Manual's departure framework — most departures were removed effective Nov. 1, 2025]

## IV. Statutory Sentencing Factors
### A. Nature and circumstances of the offense
### B. History and characteristics
### C. Purposes of sentencing
### D. Kinds of sentences available
### E. Guideline range and policy statements
### F. Unwarranted disparities [NEED SOURCE if data used]
### G. Restitution

## V. Proposed Conditions and Recommendations

## VI. Conclusion

---
## Exhibit List
| Ex. | Description | Sealed? | Supports section |

## Open Items
- {Every placeholder}
```

---

## Worked Example (abbreviated)

**Input:** Federal wire-fraud plea; defense posture. PSR applies a loss enhancement based on intended loss and a sophisticated-means enhancement. Client, 58, repaid part of the loss before indictment, cares for a disabled spouse, and has no prior record. Eleven character letters. User requests a below-range sentence of home confinement plus restitution.

**Output excerpt:**
- Objection 1 — PSR ¶24: loss figure counts invoices never submitted. Because the guideline's text now defines loss as the greater of actual or intended loss, the objection does not rest on excluding intended loss; it challenges proof — the record does not show the client intended to obtain the amounts on unsubmitted invoices, and the government bears the burden on the amount. Defense calculates actual loss from bank records (Ex. B) and argues intended loss is not proven above that figure `[CITE: user-supplied authority on burden and proof of intended loss]` `[VERIFY: current §2B1.1 loss definition]`. Corrected range shown in the calculation table.
- Objection 2 — PSR ¶26: "sophisticated means" rests on use of a personal email account; record shows no concealment layering (PSR ¶15) `[CITE]`.
- Factor B: caregiving role documented by physician letter (Ex. D, filed under seal) and two letters; pre-indictment repayment documented by wire confirmations (Ex. C).
- Factor C: acknowledges the breach of trust; answers deterrence with the collateral losses already incurred (license surrender, Ex. E) and a restitution schedule.
- Factor F: no disparity figures cited because none supplied — flagged `[NEED SOURCE: sentencing data for comparable offenses]`.

---

## Verification

- [ ] Jurisdiction and Manual/grid edition locked and matched to the PSR.
- [ ] Objections, departures (only those the current Manual still provides `[VERIFY]`), and variances labeled and argued separately.
- [ ] Every statutory factor addressed with record-cited facts.
- [ ] Aggravating facts acknowledged, not ignored.
- [ ] Specific sentence requested and justified against each purpose of sentencing.
- [ ] Sensitive exhibits identified for sealing; not quoted in the public body.
- [ ] No invented guideline values, statistics, or authority; placeholders listed.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Calling every argument a "departure" | Distinguish guideline objections, departures, and variances per the jurisdiction's framework; most federal departures were removed effective Nov. 1, 2025, so argue those facts as variances unless the current Manual retains the departure `[VERIFY]` |
| Reciting the §3553(a) factors without facts | Each factor section must cite record facts and exhibits |
| Generic mitigation ("he is a good person") | Specific, documented facts: dates, roles, outcomes, corroborating letters |
| Contradicting the factual basis of the plea | Mitigation explains context; it never disputes admitted conduct |
| Citing national disparity statistics from memory | Use only user-supplied data with source; otherwise `[NEED SOURCE]` |
| Asking for "leniency" without a number | Request a specific sentence and conditions the court can adopt |
| Putting medical or minor-related details in the public filing | Move to sealed exhibits and reference them by exhibit number |
| Ignoring the government's strongest aggravating point | Name it and answer it; judges notice omissions |
