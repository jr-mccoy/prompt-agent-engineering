---
title: "Agency Rulemaking Plan — From Mandate to Final Rule: Authority, Procedure, Required Analyses, Docket, Consultation, Comment Handling, and a Backward Timeline"
category: policy/public-administration
description: "Plan a rulemaking from the agency's side: confirm the legal authority and any statutory or court deadline, choose the procedure the jurisdiction allows, list the analyses and reviews the rule will trigger, design pre-proposal engagement and the docket, set up comment intake with an issue taxonomy and a significance test, decide in advance what changes would need re-proposal, and build a backward timeline with gates and float — distinct from a stakeholder's comment on someone else's proposal (policy_public_comment_letter) and from the cost-benefit annex itself (policy_regulatory_impact_analysis)."
techniques:
  - DT-01
  - DS-33
  - AG-11
  - QA-08
difficulty: advanced
tags:
  - rulemaking
  - administrative-procedure
  - notice-and-comment
  - regulatory-docket
  - comment-analysis
  - regulatory-agenda
  - write-new-regulation
  - plan-a-new-rule
  - respond-to-public-comments
updated: "2026-10-03"
reasoning:
  styles: [structural, analytic, rule_application, temporal]
  stakes: high
  horizon: years
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: regulated
  collaboration: team
  output_format: [structured, timeline]
  user_role: [agency_policy_staff, rulemaking_coordinator, regulatory_counsel_support, program_manager]
  mode: [plan, document]
related_prompts:
  - domain-policy/policy_public_comment_letter.md
  - domain-policy/policy_regulatory_impact_analysis.md
  - domain-legal/litigation/legal_admin_law_apa_review.md
---

# Agency Rulemaking Plan

**Objective:** Give an agency team a plan that gets a rule from mandate to an
effective final rule on time and on a record that survives review — authority
confirmed, procedure chosen, every required analysis scheduled, comments handled
systematically, and the re-proposal risk decided before it arrives.

**Audience:** Agency policy staff, rulemaking coordinators, program managers who
own a mandate, and the counsel and economists they work with, at national, state or
local level.

**When to Use:**
- A statute, court order or executive direction requires a new or amended rule.
- Leadership wants a date for the final rule and you need to show what drives it.
- A proposed rule is about to close for comment and the team has no plan for
  thousands of submissions.
- **Not this prompt if** you are **outside the agency commenting** on a proposal —
  use `domain-policy/policy_public_comment_letter.md`. The cost-benefit analysis that
  goes in the docket is `domain-policy/policy_regulatory_impact_analysis.md`; this
  prompt schedules it. Whether a final rule can be challenged in court is
  `domain-legal/litigation/legal_admin_law_apa_review.md`, for counsel.

## Inputs / Context

1. **The mandate**: statutory text (quoted), any deadline, court order or
   executive direction, and what the rule must and must not do.
2. **Jurisdiction and procedure law**: national or state administrative procedure
   act, publication outlet (federal register, state register, gazette), and any
   consultation code.
3. **Review and analysis triggers known to the team**: economic significance tests,
   small-business or regulatory-flexibility analysis, paperwork or information-
   collection approval, environmental review, tribal or local-government
   consultation, legislative rules-review committee, post-adoption legislative
   review.
4. **Affected parties and known positions.**
5. **Team and capacity**: drafters, economists, counsel, comment-analysis staff.
6. **Prior rules** on the subject and any litigation history.

Procedure requirements are listed only from the jurisdiction's own law as supplied
or as marked `[verify — agency counsel]`. Executive orders and review thresholds
change; their current status is always `[verify current]`.

## Method

1. **Confirm authority.** Quote the provision that authorises the rule, state what
   it requires versus permits, and flag any gap to counsel. A rule beyond its
   authority fails however good the analysis.
2. **Choose the procedure (DS-33).** Ordinary notice-and-comment; advance notice or
   call for evidence first; negotiated rulemaking; interim final or direct final
   rule where good cause or non-controversy allows. State why, and what the choice
   costs in time and legal risk.
3. **Break down the work (DT-01).** Workstreams: authority memo, rule text,
   preamble or explanatory statement, impact analysis, small-entity analysis,
   information-collection approval, consultations, docket and record, comment
   analysis, response-to-comments document, final package and filing, compliance
   guidance.
4. **Design pre-proposal engagement.** Who is consulted, in what format, and how
   contacts are logged so the record shows what the agency heard (ex parte rules).
5. **Set up comment handling (AG-11).** An issue taxonomy coded by provision ×
   issue × commenter type; a de-duplication rule for mass campaigns (counted, one
   representative response); a significance test (raises a new fact, a legal issue,
   a cost the analysis missed, or a workable alternative); and a response-to-
   comments structure that answers every significant comment by issue code.
6. **Pre-decide the re-proposal line.** Changes in the final rule must be a logical
   outgrowth of the proposal. List the likely changes now and which would need a
   further notice, with the time that adds.
7. **Build the backward timeline with gates (QA-08).** From the deadline back:
   effective-date period, filing, review periods, comment analysis, comment period,
   publication, internal and legal clearance, analysis completion. Each gate has a
   pass criterion and an owner. Show the float.
8. **Plan the record.** Everything relied on is in the docket by the time it is
   relied on; the record is what a court reviews.

## Output Format

```
# Rulemaking plan — [rule]   Agency: [..]   Jurisdiction: [..]
Mandate: [quoted provision]   Deadline: [..]   Procedure: [..]

## 1. Authority (requires / permits / gaps for counsel)
## 2. Procedure choice and why
## 3. Required analyses and reviews
| Trigger | Applies? | Basis | Owner | Duration | [verify] |
## 4. Workstreams
| Workstream | Output | Owner | Start | Done |
## 5. Engagement and ex parte log plan
## 6. Comment handling
Taxonomy · de-duplication rule · significance test · response structure · staffing
## 7. Re-proposal risk
| Likely change | Logical outgrowth? | If not: added time |
## 8. Backward timeline and gates
| Gate | Date | Pass criterion | Owner |
Float to deadline: [..]
```

## Verification

- [ ] Authority is quoted, not paraphrased; gaps are routed to counsel.
- [ ] Every analysis or review listed has a basis or a `[verify]` marker.
- [ ] Timeline runs backward from the deadline and shows float.
- [ ] Comment taxonomy, de-duplication rule and significance test exist before the comment period opens.
- [ ] Likely final-rule changes are tested for logical outgrowth in advance.
- [ ] Each gate has an objective pass criterion and an owner.

## False-Positive Prevention

1. **Counting comments as votes.** Volume is information about salience, not a
   tally; substantive points decide changes. Say so in the response document.
2. **Ignoring mass campaigns.** De-duplicate but still read and code; a campaign may
   carry one significant point.
3. **Analysis written after the decision.** An impact analysis finished after the
   rule text is fixed looks — and often is — post-hoc. Schedule it to inform the
   options.
4. **Optimistic review durations.** Use the agency's actual history for clearance
   and external review, not statutory minima.
5. **Interim final as a shortcut.** Good-cause claims that fail cost more time than
   the comment period saved.
6. **One jurisdiction's procedure everywhere.** State and national procedures,
   publication rules and review committees differ; plan from the governing law.

## Example Output

```
# Rulemaking plan — Indoor Heat Illness Prevention Standard
Agency: State Occupational Safety Board (illustrative)   Jurisdiction: state APA
Mandate: "The board shall adopt a standard … not later than 24 months after the
effective date of this act." Effective 1 Jul 2026 → deadline 30 Jun 2028.
Procedure: ordinary notice-and-comment with 45-day comment and 2 hearings; advisory
committee pre-proposal. Interim final rejected — no good cause; deadline is reachable.

## 3. Required analyses
| Economic impact statement | Yes | state APA [verify] | Economist | 4 mo |
| Small-business impact statement | Yes | state APA [verify] | Economist | with above |
| Legislative rules-review committee | Yes | statute [verify] | Counsel | 60 days |
| Attorney General form-and-legality review | Yes | [verify] | Counsel | 6 wk |

## 6. Comment handling
Taxonomy: provision (§1–§9) × issue (threshold temp, acclimatisation, cost, records,
small employers) × commenter (worker, employer, association, health, public).
Expected ~2,400 comments (prior heat rule: 2,100); ~1,900 identical campaign letters
→ counted and answered once. ~140 unique substantive → 2 analysts × 6 weeks.
Significant = new data, a missed cost, a legal issue, or a workable alternative.

## 7. Re-proposal risk
| Raise trigger temperature 80°F → 82°F | Yes — range was asked about in the notice | — |
| Exempt employers < 10 staff | No — not raised in notice | +5 months |
Action: ask about a small-employer phase-in in the proposal's questions, so it is in scope.

## 8. Backward timeline
| Effective (30 days after filing)            | 15 May 2028 | Filed by 15 Apr | Counsel |
| Rules-review committee complete             | 10 Apr 2028 | No objection or objection answered | Counsel |
| Final text adopted by board                 | 9 Feb 2028  | Response-to-comments complete | Director |
| Comment analysis complete                   | 15 Dec 2027 | All significant comments coded and answered | Analysts |
| Comment period closes (45 d) + hearings     | 15 Jul 2027 | Record closed | Coordinator |
| Proposed rule published                     | 1 Jun 2027  | AG review cleared; impact statements in docket | Coordinator |
| AG form-and-legality review                 | 15 Apr 2027 | Draft package complete | Counsel |
| Advisory committee (3 meetings) + call for data | Sep 2026 – Jan 2027 | Ex parte log current | Program |
Float to 30 Jun 2028: 6.5 weeks. A re-proposal (+5 months) breaks the deadline → the
small-employer question goes in the proposal.
```

## Techniques Used

- **DT-01 Hierarchical Task Breakdown** — the rulemaking split into workstreams with owners and outputs.
- **DS-33 Jurisdiction-Adaptive Output** — procedure, analyses and review steps taken from the governing law, marked for verification.
- **AG-11 Taxonomy-Based Classification Systems** — the provision × issue × commenter coding that makes comment response complete.
- **QA-08 Gate-Based Verification** — each milestone a gate with a pass criterion, run backward from the deadline.

## Related Prompts

- `domain-policy/policy_public_comment_letter.md` — the commenter's side of the same docket.
- `domain-policy/policy_regulatory_impact_analysis.md` — the impact analysis this plan schedules into the docket.
- `domain-legal/litigation/legal_admin_law_apa_review.md` — counsel's view of whether the final rule withstands challenge.
