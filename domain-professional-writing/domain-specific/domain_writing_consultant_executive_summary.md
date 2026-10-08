---
title: "Consultant Executive Summary — Recommendation First, Every Finding Traced to the Analysis"
category: professional-writing/domain-specific
description: "Write a management consultant's executive summary of a completed analysis for the C-suite: a committed recommendation with its number, range and confidence in the first paragraph, three or four findings each traced to a section of the analysis, the condition that would reverse the advice, and implementation considerations that respect what the engagement scoped. Distinct from the engagement proposal (this is the summary artifact, a component of the deliverable) and from an internal one-page decision brief."
techniques:
  - ST-46
  - QA-26
  - QA-20
  - QA-04
difficulty: intermediate
tags:
  - management-consultant
  - executive-summary
  - consulting-deliverable
  - c-suite-recommendation
  - findings-and-recommendation
  - strategy-consulting
updated: "2026-10-06"
related_prompts:
  - domain-professional-writing/business-writing/business_writing_client_engagement_proposal.md
  - domain-professional-writing/business-writing/business_writing_executive_brief.md
  - domain-decision-making/documentation/decisiondoc_one_pager.md
---

# Consultant Executive Summary

**Objective:** Produce a five-minute executive summary that leads with a committed
recommendation, supports it only with findings the underlying analysis contains, states
how confident the client should be and what would change the answer, and ends with the
decision the client must make.

**When to Use:**
- An engagement's analysis is complete (a report, model or deck exists) and the C-suite
  will read the summary, not the analysis.
- The summary is the part of the deliverable most likely to decide whether the
  recommendation is acted on.
- The recommendation is a go/no-go or a specific action with economics attached.
- Some of the evidence rests on client data you could not verify.
- **Not this prompt if** you are winning or scoping the engagement — use
  `domain-professional-writing/business-writing/business_writing_client_engagement_proposal.md`;
  this summary is a component of the deliverable, not the proposal. An internal
  one-page brief asking your own leadership for a decision is
  `domain-professional-writing/business-writing/business_writing_executive_brief.md`; a
  standalone one-pager with no analysis behind it is
  `domain-decision-making/documentation/decisiondoc_one_pager.md`.

**Audience:** The client's CEO and executive team, and the sponsor who will present the
recommendation internally. They need the answer, the economics, the confidence, and
what they must decide, readable in five minutes; the analysis is there for their staff.

The engagement lead signs the summary and is accountable that it claims no more than
the analysis supports; legal, tax and employment questions go to the client's own
advisers.

## Inputs / Context

Paste source material inside named tags and refer to it by name:
`<analysis>…</analysis>` (the report, model outputs or deck, with section numbers),
`<sow>…</sow>` (scope and exclusions), `<client_data_status>…</client_data_status>`.

1. **Analysis scope** — the question the engagement answered, and what it did not.
2. **Key findings** — the three or four most important, each with the section of
   `<analysis>` it comes from.
3. **Recommendation** — go/no-go or specific action, with the rationale.
4. **Supporting evidence** — the figures behind the recommendation: base case, range,
   sensitivity.
5. **Implementation considerations** — the factors for success if they proceed, and
   whether implementation is in the engagement's scope per `<sow>`.
6. **Data status** `<client_data_status>` — which client data was received, verified,
   or taken as given.
7. **Decision and deadline** — what the client must decide, by when, and why that date.

## Method

1. **Inventory the analysis before writing (QA-26).**
   - List every finding and figure in `<analysis>` with its section reference.
   - Each candidate sentence for the summary must map to a line in that list. A
     finding that does not — an interview remark, a hypothesis the analysis did not
     test, a number from memory — is dropped or moved to a "raised but not tested" line.
2. **State the recommendation as a committed choice.** One action, the economic result
   with its range, and the deadline. If the analysis cannot support a recommendation,
   say so and name the single missing datum; that is still a committed answer.
3. **Rate confidence per finding (QA-04).**
   - High: multiple sources or a full year of system data. Medium: one model or
     method, not tested in practice. Low: rests on client-supplied data not verified.
   - Mark any figure resting on unverified client data `[unverified — client data]`,
     consistent with `<client_data_status>`.
4. **Find the reversal condition.** Using the sensitivity in `<analysis>`, state the one
   condition under which the recommendation would change (a cost threshold, a demand
   level), computed from the model's own figures.
5. **Structure assertion-evidence (ST-46).** Each finding: a sentence that states the
   conclusion, followed by the evidence and its section reference. Order findings by
   how much they bear on the decision, not by the order the work was done.
6. **Write implementation considerations within scope.** If `<sow>` excluded
   implementation, say so and list what the client must own; do not promise delivery
   work. Legal, employment and tax steps are flagged for the client's advisers with
   `[VERIFY: …]`.
7. **Verify.** Every number recomputes from `<analysis>` (net = gross − costs; payback =
   one-time ÷ annual); the headline figure is the base case, with range beside it; no
   finding lacks a section reference; the first paragraph alone gives recommendation,
   number, confidence, and decision.

## Output Format

```
# Executive Summary: [question answered]
Prepared for: [client executives]   By: [engagement lead]   Date: [..]

## Recommendation
[action] — [base-case result, range] — confidence [H/M/L] — decision needed by [date]
Reverses if: [condition, computed]

## Why (key findings)
1. [assertion] — [evidence] ([analysis §]) — confidence [..]
2. ...

## Economics
| Item | Base | Range | Source (§) |

## What we did not establish
[raised but not tested; unverified client data]

## Implementation considerations
[in or out of engagement scope; what the client must own; adviser flags]

## Decision requested
[who decides what, by when, and why that date]
```

## Verification

- [ ] The first paragraph alone states the action, the base-case number with range,
      the confidence, and the decision date.
- [ ] Every finding carries an `<analysis>` section reference.
- [ ] No sentence states a finding the analysis does not contain.
- [ ] Figures resting on unverified client data are marked as such.
- [ ] The reversal condition is computed from the analysis's own figures.
- [ ] Implementation considerations match the engagement's scope in `<sow>`.
- [ ] Net figures and payback recompute from their components.

## False-Positive Prevention

1. **Findings the analysis does not contain.** A vivid interview remark ("South's
   productivity is 20% worse") slides into the summary as a finding, though no section
   tests it. The C-suite will act on it and the client's analyst will not find it.
   Every finding has a section number or it moves to "raised but not tested".
2. **A recommendation hedged until it is not one.** "Consolidation merits serious
   consideration, subject to further analysis of several factors" gives the executive
   nothing to approve. State the action; put the uncertainty in the confidence rating
   and the reversal condition.
3. **The high case as the headline.** Leading with the top of the savings range
   because it sounds decisive sets the number the client will hold you to. Lead with
   the base case and print the range beside it.
4. **Unverified client data presented as found.** A lease break fee from the client's
   own summary, never checked against the lease, reads as a consulting finding once it
   is in the economics table. Mark it and say what would verify it.
5. **Implementation promised outside the scope.** "We will manage the transition" in a
   summary for an engagement whose SOW excluded implementation creates the most
   disputed boundary in the trade. Say what the client must own.
6. **Softening a finding that implicates the sponsor.** When the underperforming unit
   reports to the person presenting the summary, the finding drifts into the passive
   voice or the appendix. It stays in the findings at its actual weight.
7. **Chronological findings.** Findings listed in the order the work was done (market,
   then operations, then finance) put the decisive one third. Order by bearing on the
   decision.

## Dual-Failure Prevention (QA-20)

- **Harmful:** overclaiming — the high case as the headline, unverified client data as
  a finding, a confident "close the site" when the reversal condition is close to
  current estimates. The client acts on economics the analysis does not support.
- **Unhelpful:** hedging and caveat soup — options "for consideration" with no
  recommendation, every sentence qualified, a page of methodology before the answer.
  The client pays for a decision and gets a literature review.
- **Bar:** a CEO who reads only the first paragraph knows what to do, the base-case
  number and its range, how confident to be, the one condition that would change the
  advice, and what they must decide by when.

## Example Output

```
# Executive Summary: Should Harlow Foods consolidate from three distribution centres to two?
Prepared for: CEO, COO, CFO, Harlow Foods   By: Engagement lead   Date: 6 Oct 2026

## Recommendation
Close DC South and serve its routes from DC Central. Base case: $6.1M a year net
savings (range $4.8M–$6.9M), $9.4M one-time cost, payback 18.5 months. Confidence:
high on the savings, medium on service impact, low on the lease exit cost. Decision
needed by 13 Nov to open lease negotiations within the notice window.
Reverses if: one-time cost exceeds $12.2M (payback beyond the 24-month hurdle in
§1) — i.e. if the lease break fee exceeds $5.0M rather than the $2.2M assumed.

## Why (key findings)
1. DC South is under-used: 54% of throughput capacity against 78% at Central, over
   12 months of warehouse-system data (§3, Table 3.2) — confidence high.
2. Central can absorb South's volume with a second shift; peak utilisation would be
   91% (§4.1 capacity model) — confidence high.
3. Longer routes raise transport cost by $1.3M a year, already netted from the savings
   (§4.3 route model) — confidence high.
4. Next-day coverage falls from 97% to 94% of customers: 41 southern accounts move to
   two-day delivery (§5) — confidence medium; modelled, not piloted.

## Economics
| Item                          | Base     | Range          | Source (§) |
| Facility savings (lease, labour, utilities) | $7.4M/yr | — | §4.2 |
| Added transport               | −$1.3M/yr | fuel ±15%     | §4.3 |
| Net run-rate savings          | $6.1M/yr | $4.8M–$6.9M    | §6 sensitivity |
| One-time cost                 | $9.4M    | —              | §4.4 |
|   of which lease break fee    | $2.2M [unverified — client data; lease not reviewed] | | <client_data_status> |
| Payback                       | 18.5 mo  | 16.3–23.5 mo   | computed |
Check: 7.4 − 1.3 = 6.1; 9.4 ÷ 6.1 = 1.54 yr = 18.5 mo; 9.4 ÷ 4.8 = 23.5 mo;
9.4 ÷ 6.9 = 16.3 mo. Reversal: 6.1 × 2 yr = 12.2; 12.2 − (9.4 − 2.2) = 5.0 fee ceiling.

## What we did not establish
- Labour productivity at South versus Central was raised in interviews and not tested;
  it is not part of the case above.
- The lease break fee is the client real-estate team's figure; verify against the
  lease's break clause before 13 Nov.

## Implementation considerations
Implementation is outside this engagement (SOW §2, exclusions). Harlow will need to own:
- Lease negotiation — the fee is the variable that can reverse the recommendation.
- Employee consultation and severance at South [VERIFY: obligations with employment
  counsel].
- A second shift at Central: 38 FTE (§4.1), hiring to start 12 weeks before cutover.
- Contact with the 41 accounts moving to two-day delivery before any announcement;
  §5 lists them by revenue.

## Decision requested
CEO and COO: approve opening lease negotiations for DC South and the customer contact
plan for the 41 accounts, by 13 Nov [VERIFY: notice date in the lease]. CFO: confirm the
24-month payback hurdle applies to this decision.
```

## Techniques Used

- **ST-46 Assertion-Evidence Content Structure** — each finding as a conclusion followed by
  its evidence and section reference.
- **QA-26 First-Invented-Fact Test** — every summary sentence mapped to the analysis
  inventory; untested claims moved out of the findings.
- **QA-20 Dual-Failure Quality Test** — overclaiming and over-hedging both named, with a
  first-paragraph bar.
- **QA-04 Uncertainty Acknowledgment** — confidence per finding and unverified client data
  marked, without diluting the recommendation.

## Related Prompts

- `domain-professional-writing/business-writing/business_writing_client_engagement_proposal.md`
  — the proposal that scoped this engagement; this summary is a component of what it
  delivers.
- `domain-professional-writing/business-writing/business_writing_executive_brief.md` — an
  internal one-page decision brief.
- `domain-decision-making/documentation/decisiondoc_one_pager.md` — a standalone one-pager
  with no analysis behind it.
- `client-services-studio/verticals/management-consultant/README.md` — the consulting
  practice pipeline that uses this prompt as its deliverable-writing step.
