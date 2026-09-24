---
title: "Deal Qualification Scorecard — MEDDPICC Scored on Buyer Evidence, Not Rep Belief"
category: sales-customer/sales
description: "Score one open opportunity against the eight MEDDPICC elements using only evidence the buyer has given or done, grade each element Verified / Inferred / Unknown, and return a mechanical qualification verdict plus the two questions that would close the largest gap — distinct from discovery-call prep, which plans the conversation that produces this evidence."
techniques:
  - DS-01
  - RT-05
  - AG-02
  - QA-04
  - DP-13
difficulty: intermediate
tags:
  - sales
  - qualification
  - meddpicc
  - opportunity-management
  - deal-review
  - b2b
updated: "2026-09-24"
related_prompts:
  - domain-sales-customer/sales/sales_mutual_close_plan.md
  - domain-sales-customer/sales/sales_forecast_commit_review.md
  - domain-business-strategy/go-to-market/workflow_sales_discovery_call_preparation.md
---

# Deal Qualification Scorecard

**Objective:** Decide whether one opportunity is qualified enough to keep investing
in, by scoring each MEDDPICC element on what the buyer has actually said or done —
and naming the single gap that most changes the answer.

**When to Use:**
- An opportunity is about to move stages, enter a forecast category, or pull in
  a solutions engineer, and nobody has written down why it deserves to.
- A manager asks "is this real?" and the answer is a feeling.
- The deal has been open for longer than your median cycle and you suspect it is
  being carried rather than worked.
- You inherited an opportunity and need to know what is known versus assumed.
- **Not this prompt if** you are preparing the next discovery call — use
  `domain-business-strategy/go-to-market/workflow_sales_discovery_call_preparation.md`,
  which plans the questions; this prompt grades the answers. For a whole-pipeline
  sweep use `workflow_sales_pipeline_risk_assessment.md`; for lead scoring before an
  opportunity exists use `domain-agentic-resources/skills/marketing/revops/`.

## Inputs / Context

1. **Opportunity record:** stage, amount, close date, age, product, competitor(s).
2. **Evidence log:** call notes, emails, meeting attendees, documents the buyer
   sent. Paste raw; the prompt separates buyer statements from rep summaries.
3. **Your stage-exit criteria**, if your team has them. If not, the default below
   is used and labelled as such.
4. **Median sales cycle and average deal size** for this segment, if known.
5. **Anything the rep believes but has not been told** — list it separately. It
   is useful as a hypothesis and disqualifying as evidence.

Missing inputs are marked `[NOT PROVIDED]`, never filled with a plausible value.

## Method

1. **Separate evidence from belief (RT-05).** Tag every input line:
   - `[B-said]` the buyer stated it (quote or close paraphrase, with date and who).
   - `[B-did]` the buyer took an action: sent data, booked a meeting, introduced
     someone, shared a procurement form.
   - `[R-inferred]` the rep's interpretation, a third party's claim, or a
     website/LinkedIn deduction.

2. **Score the eight elements (DS-01), 0–3, evidence-first:**

   | Element | 3 = | Minimum for a 2 |
   |---|---|---|
   | **M**etrics | Buyer quantified the outcome and its baseline | Buyer named the metric, not the number |
   | **E**conomic buyer | Met, and stated the priority themselves | Named by the champion with a role, not met |
   | **D**ecision criteria | Written or agreed list, weighted | Stated verbally by more than one buyer |
   | **D**ecision process | Steps, owners and dates, confirmed by buyer | Steps known, dates missing |
   | **P**aper process | Legal, security, procurement path and lead times known | Buyer named who signs |
   | **I**dentify pain | Pain tied to a cost or an event with a date | Pain stated, not costed |
   | **C**hampion | Has *acted* for you: shared internal info, sold in a meeting you were not in | Has access and interest, untested |
   | **C**ompetition | Alternatives known, including do-nothing and build | One named competitor |

   An element supported only by `[R-inferred]` lines scores **at most 1**.

3. **Grade confidence separately from score (QA-04).** Each element gets
   Verified / Inferred / Unknown. A 2 that is Inferred is a different finding from
   a 2 that is Verified; do not average them together.

4. **Default to unqualified (AG-02).** The deal starts at "not qualified" and
   earns its way up. "They loved the demo" earns nothing; enthusiasm is not an
   element.

5. **Test the champion.** List what the champion has *done*. If the list is empty,
   the champion is a coach at best, and Champion scores ≤1 regardless of sentiment.

6. **Find the largest gap.** The gap that matters most is the lowest-scoring
   element whose absence would kill the deal at signature — usually Economic
   buyer, Paper process, or Decision process — not the lowest score overall.

7. **Write the kill signal (DP-13).** One observable event, with a date, that
   would move this deal to disqualify or nurture: e.g. "economic buyer meeting not
   booked by 14 Oct."

8. **Apply the verdict rule** (below) and stop. Do not soften it.

## Output Format

```
# Qualification — [Account] / [Opportunity] — [date]
Stage: [..]  Amount: [..]  Close date: [..]  Age: [n days] vs median [n | NOT PROVIDED]

## Scorecard
| Element | Score 0–3 | Confidence | Evidence (tag, who, date) | Gap |
|---|---|---|---|---|
(8 rows)
Total: [n]/24   Verified elements: [n]/8

## Champion test
Actions taken for us: [list | none]

## Largest gap
[element] — why it kills at signature — the two questions that close it, and who
must be asked

## Beliefs held without evidence
- [R-inferred claim] → how to verify

## Kill signal
[observable event] by [date] → [disqualify | nurture]

## Verdict
[QUALIFIED | CONDITIONAL | NOT QUALIFIED | INSUFFICIENT EVIDENCE] — rule line that fired
```

**Verdict rule (mechanical):**
- **QUALIFIED** iff total ≥16, no element is 0, and Economic buyer, Pain and
  Decision process are each ≥2 **Verified**.
- **CONDITIONAL** iff total ≥12 and at most two of those three are below the bar;
  name the date by which each must clear.
- **NOT QUALIFIED** iff total <12, or Pain is 0, or the kill signal has already
  fired.
- **INSUFFICIENT EVIDENCE** iff more than four elements are Unknown — plus the
  single cheapest datum (usually one direct question to the champion) that unblocks it.
No other verdict may be emitted; "it depends" is banned.

## Verification

- [ ] Every score ≥2 cites at least one `[B-said]` or `[B-did]` line with a date.
- [ ] No element supported only by `[R-inferred]` scores above 1.
- [ ] The champion section lists actions, not adjectives.
- [ ] Total recomputed from the eight rows and matches.
- [ ] The largest gap is chosen by kill-at-signature, not by lowest number.
- [ ] The verdict names the rule line that fired.

## False-Positive Prevention

1. **Attendance is not an economic buyer.** A VP who joined one call for ten
   minutes and said nothing about priority is a 1, not a 3.
2. **The rep's summary is not the buyer's words.** "Pain: slow onboarding" in a
   CRM field is `[R-inferred]` until a buyer is quoted saying it.
3. **A friendly contact is not a champion.** If they have not spent any of their
   own capital on you, they have not been tested.
4. **Written decision criteria can be the competitor's.** Criteria that map
   feature-for-feature to one vendor's datasheet were probably written with that
   vendor; score Competition down, not Decision criteria up.
5. **A close date the buyer never said is a rep's hope.** Decision process scores
   on the buyer's steps, not on the CRM field.
6. **Do-nothing is a competitor.** Competition at 3 with only named vendors
   listed is wrong; the status quo must be in the row.
7. **High totals can hide a zero.** 20/24 with Paper process at 0 is not
   qualified in an enterprise deal; the rule's "no zeros" clause exists for this.
8. **Do not hedge into "promising."** The output is a verdict and a gap, not a
   mood. If the evidence is thin, the verdict is INSUFFICIENT EVIDENCE, which is
   a committed answer.

## Example Output

```
# Qualification — Halvorsen Freight / Fleet analytics platform — 2026-09-24
Stage: Solution validation  Amount: $84,000 ARR  Close date: 2026-10-31
Age: 71 days vs median 58

## Scorecard
| Element | Score | Confidence | Evidence | Gap |
|---|---|---|---|---|
| Metrics | 2 | Verified | [B-said] Ops Dir. R. Okafor, 09-03: "fuel variance is the number the board asks about" | No baseline figure |
| Economic buyer | 1 | Inferred | [R-inferred] CFO assumed signer; never met | Not met, not confirmed |
| Decision criteria | 2 | Verified | [B-did] Okafor sent 6-item eval sheet, 09-10 | Unweighted |
| Decision process | 1 | Inferred | [R-inferred] "they decide in October" | No steps, no owners |
| Paper process | 0 | Unknown | none | Security review path unknown |
| Identify pain | 3 | Verified | [B-said] Okafor, 08-20: fuel overspend $310k last FY, audit finding due Q1 | — |
| Champion | 2 | Verified | [B-did] Okafor forwarded internal fuel report, 09-12 | Not yet sold internally without us |
| Competition | 2 | Verified | [B-said] incumbent telematics add-on; spreadsheet status quo | Build option not asked |
Total: 13/24   Verified elements: 5/8

## Champion test
Actions taken for us: forwarded the internal fuel report (09-12); sent eval sheet (09-10).

## Largest gap
Paper process (0) — with a 10-31 close and no security-review path known, the
deal cannot sign even if every other element is perfect.
Q1 (to Okafor): "Who runs vendor security review, and how long did the last one take?"
Q2 (to Okafor): "Will the CFO sign, or does it go to a committee above $75k?"

## Beliefs held without evidence
- CFO is the signer → verify with Q2.
- "They decide in October" → ask Okafor to walk the steps from eval sheet to signature.

## Kill signal
No named security-review owner by 2026-10-08 → move close date to Q1 and nurture.

## Verdict
CONDITIONAL — total 13 (≥12); Economic buyer and Decision process below 2 Verified.
Economic buyer must clear by 10-08; Decision process by 10-10. Paper process at 0
blocks QUALIFIED regardless of total.
```

## Techniques Used

- **DS-01 Framework Application** — MEDDPICC with an explicit 0–3 definition per element.
- **RT-05 Evidence-Based Reasoning** — every score cites a tagged, dated buyer line.
- **AG-02 Skeptical Default Stance** — the deal starts unqualified and earns each point.
- **QA-04 Uncertainty Acknowledgment** — confidence graded separately from score.
- **DP-13 Kill Signal Definition** — one dated, observable disqualifier.

## Related Prompts

- `domain-sales-customer/sales/sales_mutual_close_plan.md` — once CONDITIONAL or
  QUALIFIED, turn the gaps into dated buyer-owned steps.
- `domain-sales-customer/sales/sales_forecast_commit_review.md` — the forecast
  category this verdict feeds.
- `domain-business-strategy/go-to-market/workflow_sales_discovery_call_preparation.md`
  — plan the call that closes the largest gap.
