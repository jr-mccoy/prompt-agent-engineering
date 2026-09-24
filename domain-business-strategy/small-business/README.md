# Small Business

Prompts for the **owner of a local shop, trades business or freelance practice** —
the person who does the work, keeps the books, answers the reviews and decides
whether to hire, usually in the same week.

The reader is load-bearing. The rest of `domain-business-strategy/` addresses a
startup founder or a company's leadership; `domain-finance/` addresses a controller
or analyst. These prompts assume one owner, a few hours a week for the business side,
an accountant seen a few times a year, and no finance team.

**Prefix:** `smallbiz_`

## Contents

| Prompt | Job |
|---|---|
| `smallbiz_weekly_owner_numbers_review.md` | Bank, tax set-asides, owed in and out, owner draw, 8-week cash look-ahead |
| `smallbiz_first_employee_readiness.md` | Loaded cost, break-even work, slow-season test, runway gate, classification flag |
| `smallbiz_local_marketing_plan.md` | Profile, listings, reviews, existing customers, neighbours, then paid — with kill signals |
| `smallbiz_bookkeeping_routine.md` | Weekly, monthly, quarterly cadence and the year-end accountant handoff |
| `smallbiz_customer_review_response.md` | Public reply, private follow-up, and the fix behind the complaint |
| `smallbiz_price_increase_plan.md` | Stand-still price, break-even customer loss, segment rollout, notice wording |

## Where the rest of the workflow lives

These jobs already have owners; this directory points to them rather than
duplicating them:

| Need | Owned by |
|---|---|
| Choosing how to charge for services (hourly, day rate, fixed, retainer) | `../client-services/services_pricing_model_selector.md` |
| The minimum rate a services business can charge | `../../domain-finance/corporate-finance-fpa/finance_services_rate_floor_model.md` |
| Choosing suppliers | `../../domain-operations/supply-chain-procurement/ops_supplier_selection_scorecard.md` |
| Inventory reorder points | `../../domain-operations/supply-chain-procurement/ops_inventory_reorder_policy.md` |
| A full 13-week or driver-based cash forecast | `../../domain-finance/treasury-capital-markets/finance_cash_flow_forecasting_model.md` |
| Invoicing schedules and collections | `../../domain-finance/accounting-controllership/finance_services_invoice_schedule_builder.md`, `../../domain-finance/accounting-controllership/finance_collections_escalation_ladder.md` |
| Employee vs contractor classification | `../../domain-legal/employment-labor/legal_wage_hour_classification_analysis.md` |
| The job posting | `../../domain-hr-management/hiring/hr_job_description_writer.md` |
| Local ad imagery | `../../domain-advertising/advertising_local_small_business.md` |

## Boundaries

- **Not a startup.** Fundraising, product-market fit and SaaS metrics live in
  `../startup/`.
- **Not a controller.** Close calendars, accruals and multi-entity consolidation live
  in `../../domain-finance/accounting-controllership/`.
- **No tax, payroll or employment-law determinations.** Set-aside percentages come
  from the owner's accountant; classification, registration and notice rules are
  flagged for an adviser.
- **Money objects stay in finance.** These prompts are the owner's routine and
  decisions; the underlying financial models are linked, not rebuilt.
