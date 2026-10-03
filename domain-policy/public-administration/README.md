# Policy — Public Administration

Six prompts for the people who **run government** rather than argue about it:
budget and finance staff, grants managers, rulemaking teams, caseworkers and
district staff, performance analysts, and the staff who write agenda reports for
councils and boards. The object is the agency's own work — its budget, its awards,
its rules, its correspondence, its measures, its meetings.

The flat prompts in [`../`](../README.md) analyse a policy choice (frame, map,
test, compare, recommend) or respond to someone else's bill or rule. These prompts
operate the machinery that turns a choice into delivered public service.

**Prefix:** `policy_` (one prefix across the domain) · **Category:** `policy/public-administration`

## Prompts

| File | Purpose |
|---|---|
| `policy_local_budget_shortfall_options.md` | Close a municipal, county or district budget gap: structural vs one-time split, legal screen, options scored on dollars by year, service units, equity and reversibility, balanced packages with the reserve policy tested |
| `policy_grant_post_award_compliance.md` | Recipient-side post-award review of a government grant: allowable / allocable / reasonable / documented cost testing, payroll charging, subrecipient vs contractor and risk-based monitoring, reporting calendar, audit-readiness traffic lights (US 2 CFR 200 as worked example) |
| `policy_agency_rulemaking_plan.md` | The agency's plan from mandate to effective final rule: authority, procedure choice, required analyses and reviews, comment taxonomy and significance test, re-proposal (logical-outgrowth) risk, backward timeline with gates |
| `policy_constituent_casework_system.md` | How an elected office or agency answers the public: views vs casework vs service requests, urgency triage, privacy release before action, templates calibrated against over-promising, escalation ladder, tracking and staffing |
| `policy_agency_performance_measures.md` | Logic model, Results-Based Accountability sort, operational definitions with unknown-handling, targets from baseline + trend + capacity, gaming risks with paired measures, attribution limits |
| `policy_public_meeting_staff_brief.md` | Staff report and one-page official's brief for a council, board or commission item: motion, authority, three-year fiscal impact, options with alternative motions, public input, likely questions, procedural traps |

## How they compose

The budget-shortfall prompt sets what the agency can afford; its packages reach the
body through `policy_public_meeting_staff_brief`. `policy_agency_performance_measures`
defines what the funded programs must show, and recurring issues logged by
`policy_constituent_casework_system` feed both the measures and the policy chain in
`../`. A mandate from the legislature runs through `policy_agency_rulemaking_plan`,
which schedules `../policy_regulatory_impact_analysis.md` into the docket; outsiders
respond with `../policy_public_comment_letter.md`. Federal or state money arriving
for a program is managed through `policy_grant_post_award_compliance`.

## Guards

- **Legal availability and procedure are verified, not asserted.** Levy limits,
  procedure acts, cost rules, open-meetings and ethics rules vary by jurisdiction;
  the prompts mark them `[verify — counsel / finance director / clerk]` unless the
  user supplies the text.
- **US examples are examples.** The Uniform Guidance, US administrative procedure
  and US-style council procedure appear as worked cases; each prompt states how to
  map other jurisdictions.
- **Staff analysis, not political advice.** Recommendations are labelled as staff
  views and kept separate from facts; values choices are left to elected officials.

## Lives elsewhere

| If you need… | Go to |
|---|---|
| A nonprofit's own budget with donor restrictions | `../../domain-business-strategy/nonprofit/nonprofit_operating_budget_restrictions.md` |
| Writing a grant proposal (pre-award) | `../../domain-business-strategy/nonprofit/nonprofit_foundation_grant_proposal.md`; research grants in `../../domain-science/grants-funding/` |
| Commenting on another agency's proposed rule | `../policy_public_comment_letter.md` |
| Challenging a final agency action in court | `../../domain-legal/litigation/legal_admin_law_apa_review.md` |
| A resident writing their own complaint to an agency or regulator | `../../domain-written-advocacy/institutions-and-records/advocacy_regulator_complaint_drafter.md` |
| Whether a program caused its outcomes | `../policy_program_evaluation_design.md` |
| Commercial customer-support queues | `../../domain-sales-customer/support/` |
| Public procurement tenders (buyer-side RFP) | `../../domain-operations/supply-chain-procurement/ops_rfp_procurement_package.md` |
