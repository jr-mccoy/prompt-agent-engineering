# Nonprofit

Prompts for **running a nonprofit organisation** — raising money from foundations,
governments and individuals, governing it, reporting what it achieved, running its
volunteers, and budgeting under restrictions.

The distinction is load-bearing. The rest of `domain-business-strategy/` assumes a
company selling something. A nonprofit's binding constraints are different: much of
its money arrives with conditions attached, its "customers" and its funders are
different people, and its credibility rests on reporting results it did not invent.

**Prefix:** `nonprofit_`

## Contents

| Prompt | Job |
|---|---|
| `nonprofit_foundation_grant_proposal.md` | Funder-fit gate first, then a proposal drafted from the organisation's own logic model and budget |
| `nonprofit_case_for_support.md` | The master, evidence-traced argument every appeal, proposal and ask is cut from |
| `nonprofit_donor_appeal_letter.md` | A segmented appeal with ask ladders from last gift and gift lines that reconcile to the budget |
| `nonprofit_major_gift_ask_plan.md` | Readiness, amount, purpose, asker, conversation and stewardship for one donor |
| `nonprofit_board_governance_health_check.md` | Evidence-rated board assessment with compliance questions routed to counsel |
| `nonprofit_impact_report_builder.md` | Results against an existing logic model, every figure provenance-tagged |
| `nonprofit_volunteer_program_design.md` | Roles in hours, recruitment arithmetic, risk-tiered screening, retention, hours valuation |
| `nonprofit_operating_budget_restrictions.md` | Restricted vs unrestricted, indirect recovery, functional allocation, the unrestricted gap |

## Where the rest of the workflow lives

| Need | Owned by |
|---|---|
| Logic model or theory of change | `../../domain-education-teaching/program/evaluation-analytics/program_logic_model_designer.md` |
| Evaluation design | `../../domain-education-teaching/program/evaluation-analytics/program_program_evaluation_framework.md` |
| Research grants (NSF, NIH, ERC) | `../../domain-science/grants-funding/` |
| Cause-marketing imagery | `../../domain-advertising/advertising_nonprofit_cause_marketing.md` |
| Safeguarding and conduct policy | `../../domain-discipleship/program-operations/discipleship_safeguarding_and_conduct_policy.md` |
| Church volunteer roles | `../../domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_volunteer_recruitment_role_design.md` |
| The donor's own giving and tax planning | `../../domain-finance/tax-planning/finance_charitable_giving_tax_strategy.md` |
| Budget variance against actuals | `../../domain-finance/corporate-finance-fpa/finance_budget_variance_investigator.md` |

## Boundaries

- **No logic-model prompt here.** `program_logic_model_designer.md` owns it; the grant
  and impact-report prompts consume a logic model as input and never re-derive one.
- **No tax or legal determinations.** Exempt status, unrelated business income,
  lobbying and political-activity limits, gift classification and filing
  requirements are flagged for the auditor, accountant or counsel — never decided.
- **No invented impact.** Every figure carries a source or a `[verify]` marker; no
  beneficiary story appears without recorded consent, and no composite is presented
  as one person.
- **Donor side goes to finance.** How a donor should give tax-efficiently is the
  donor's adviser's question, not the organisation's.
