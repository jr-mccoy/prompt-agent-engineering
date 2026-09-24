---
title: "Plea Offer Analysis — Exposure, Collateral Consequences, and Trial Comparison"
category: legal/criminal
description: "Compare a plea offer against trial for defense counsel: sentencing exposure under each path (guideline or state-grid inputs the user supplies), collateral consequences including immigration, strength-of-evidence assessment by element, and a client-communication summary — without inventing guideline values, statutory ranges, or conviction probabilities."
techniques:
  - ST-01
  - RT-02
  - DS-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - criminal
  - plea-bargaining
  - sentencing-exposure
  - collateral-consequences
  - immigration-consequences
updated: "2026-09-24"
related_prompts:
  - domain-legal/criminal/legal_sentencing_memorandum.md
  - domain-legal/criminal/legal_motion_to_suppress.md
  - domain-legal/litigation/legal_settlement_value_range_analysis.md
  - domain-legal/litigation/legal_case_strategy_assessment.md
---

**Objective:** Give defense counsel a structured, auditable comparison of a pending plea offer against trial — exposure under each path, collateral consequences, element-by-element evidence strength, and the decision factors the client must weigh — so counsel can advise the client and document that the offer was communicated and explained.

**When to Use:** A plea offer is on the table (or expected); before the offer deadline; when re-evaluating after a suppression ruling, new discovery, or a superseding charge; when the client is a non-citizen or holds a license, benefit, or status a conviction may affect.

**Distinct from:**
- `domain-legal/litigation/legal_settlement_value_range_analysis.md` — civil expected-value settlement ranges in dollars; criminal pleas trade liberty and status, and the decision belongs to the client.
- `domain-legal/litigation/legal_case_strategy_assessment.md` — civil case strategy at the matter level.
- `domain-legal/criminal/legal_sentencing_memorandum.md` — advocacy after a conviction or plea; this prompt is the pre-plea decision analysis.
- This prompt is for counsel advising a client; it is never advice to a defendant negotiating without counsel.

---

## Your Input

- **Jurisdiction and sentencing system:** [Federal (U.S. Sentencing Guidelines — state the Manual edition) / state guidelines grid / indeterminate — required]
- **Charges now pending:** [Counts, statutes, statutory minimum/maximum as the user has verified them]
- **Plea offer terms:** [Count(s) of conviction, stipulations, dismissed counts, sentencing recommendation, appeal/collateral waivers, cooperation terms, deadline]
- **Guideline or grid inputs (per path):** [Base offense level, specific offense characteristics, adjustments, acceptance credit, criminal history points/category — as counsel has calculated them]
- **Client profile:** [Citizenship/immigration status, professional licenses, public benefits, housing, firearms, family circumstances, prior record]
- **Evidence summary by element:** [Government's evidence and defense responses for each element of each charge]
- **Pending or winnable motions:** [Suppression, severance, dismissal — and their status]
- **Local practice notes:** [Judge's known practice only if counsel supplies it]

---

## Constraints

**Must:**
- Compute exposure for **each path** (plea as offered; trial conviction on all counts; plausible partial verdict) using **only** the inputs supplied, showing every step.
- Mark every statutory range, guideline value, and mandatory minimum not supplied with `[VERIFY: ...]` and exclude it from totals until verified.
- Assess evidence strength **per element** on a qualitative scale (Strong / Contested / Weak for the government) with the specific evidence cited; do not output a numeric conviction probability unless counsel supplies one, and then label it as counsel's estimate.
- List collateral consequences by category — immigration, licensing, employment, housing, benefits, firearms, registration, civil liability, future sentencing enhancement — marking each `[VERIFY with {specialist/authority}]` where the consequence depends on law not supplied.
- Flag immigration consequences as requiring a specific, verified analysis of the offense of conviction; identify any alternative plea structure that may change the consequence as a question for immigration counsel.
- Separate **what the lawyer advises** from **what the client decides**; the plea decision is the client's.
- Produce a plain-language client summary suitable for documenting that the offer was conveyed and explained.

**Must Not:**
- Invent offense levels, ranges, mandatory minimums, collateral-consequence rules, or case law.
- Present the plea-vs-trial choice as a single expected-value number.
- Assume a waiver's scope; quote the offer's waiver language or mark `[NEED TEXT: waiver clause]`.
- Recommend a plea on the basis that the client "is probably guilty" — the analysis concerns proof and consequences.
- Add "consult an attorney" boilerplate; the reader is the attorney.

---

## Method

1. **Lock the terms.** Restate the offer, deadline, and every waiver in a terms table. Missing terms → `[NEED TEXT]`.
2. **Exposure by path.** For each path, show the calculation line by line (offense level build, criminal history, resulting range, statutory floor/ceiling), plus custody, supervision, fines, restitution, and forfeiture where supplied.
3. **Element-by-element proof map.** For each count: element → government's evidence (cited) → defense response → rating.
4. **Motion leverage.** How each pending motion's likely outcome changes the proof map and exposure; state outcomes as scenarios, not predictions.
5. **Collateral consequence matrix.** Consequence → triggered by plea? by trial conviction? → severity to this client → verification needed.
6. **Counter-offer levers.** Terms counsel could seek (different count of conviction, stipulation changes, waiver carve-outs, sentencing recommendation) tied to the consequence or exposure each addresses.
7. **Client summary.** Plain language; both paths side by side; explicit statement that the decision is the client's; space for the client's questions.

---

## Output Format

```markdown
# PLEA OFFER ANALYSIS — {Matter} — Offer deadline {date}

## 1. Offer Terms
| Term | Offer language / summary | Source | Notes |

## 2. Exposure by Path
| | Plea as offered | Trial — all counts | Trial — partial ({counts}) |
|---|---|---|---|
| Offense level build | ... | ... | ... |
| Criminal history | ... | ... | ... |
| Range | ... | ... | ... |
| Statutory min / max | [VERIFY] | [VERIFY] | [VERIFY] |
| Supervision / fines / restitution / forfeiture | ... | ... | ... |
(Calculation steps shown beneath the table.)

## 3. Proof Map
| Count | Element | Govt evidence (cite) | Defense response | Rating |

## 4. Motion Scenarios
| Motion | If granted | If denied | Effect on exposure |

## 5. Collateral Consequences
| Category | Plea | Trial conviction | Severity for client | Verify with |

## 6. Counter-Offer Levers
- {Lever} → addresses {consequence / exposure}

## 7. Counsel's Assessment
{Reasoned view; clearly labeled as advice.}

## 8. Client Summary (plain language)
{Side-by-side; "This is your decision"; questions to discuss.}

## Open Items
- {Every [VERIFY]/[NEED TEXT]/[CITE]}
```

---

## Worked Example (abbreviated)

**Input:** Federal; two counts (distribution; possession of a firearm in furtherance). Offer: plead to distribution count, government dismisses the firearm count, recommends low end, appeal waiver. Client is a lawful permanent resident with a professional license. Counsel supplies offense-level inputs for the drug count and notes the firearm count carries a consecutive mandatory term, statute cited but not yet verified.

**Output excerpt:**
- Exposure: plea path range computed from counsel's inputs with acceptance credit shown; trial path adds the firearm count as "consecutive mandatory term `[VERIFY: 18 U.S.C. provision and length]`" — excluded from the total until verified, with a note that it dominates the comparison if confirmed.
- Proof map: firearm "in furtherance" element rated **Contested** — gun found in a bedroom closet, drugs in the kitchen (Bates 0112, 0118); no statement linking them.
- Collateral: removal consequences of a controlled-substance conviction for an LPR flagged **Severe — verify offense-specific consequence with immigration counsel before the deadline**; license reporting obligation `[VERIFY: licensing board rule]`.
- Counter-offer lever: explore an offense of conviction that immigration counsel confirms carries a lesser consequence — framed as a question, not an assertion that one exists.
- Client summary states both paths, the unverified mandatory term, and "the choice to accept or reject is yours."

---

## Verification

- [ ] Jurisdiction and sentencing-system lock (including Guidelines Manual edition or state grid version).
- [ ] Every exposure number traces to a supplied input; unverified values excluded from totals.
- [ ] Proof map covers every element of every count.
- [ ] No numeric conviction probability unless counsel supplied one, labeled as such.
- [ ] Immigration and other collateral consequences flagged with specific verification owners.
- [ ] Waiver language quoted or marked `[NEED TEXT]`.
- [ ] Advice and client decision clearly separated; client summary in plain language.
- [ ] No invented authority or deadlines.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Producing a guideline range from memory of offense levels | Compute only from counsel's inputs; mark missing values `[VERIFY]` |
| Reducing the decision to "65% chance of conviction" | Use per-element qualitative ratings; numbers only as counsel's labeled estimate |
| Treating immigration consequences as a generic warning line | Make it a severity-rated matrix row with a named verification owner and deadline relevance |
| Omitting the dismissed count's relevance at sentencing | Note that dismissed conduct may still be considered `[VERIFY: relevant-conduct rule in jurisdiction]` |
| Ignoring the appeal/collateral waiver's cost | Quote the waiver and list what it forecloses (e.g., challenge to a denied suppression motion) |
| Framing the recommendation as the client's obligation | State counsel's advice, then state the decision is the client's |
| Assuming federal concepts in a state case | Use the state's grid and terminology supplied by the user |
