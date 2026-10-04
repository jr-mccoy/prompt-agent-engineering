# Professional Services — Running the Firm

Four prompts for the **people who run multi-person professional firms** —
accounting and audit, consulting, engineering, architecture, agencies — covering
the firm-operations work that happens around client engagements: whether the firm
was paid for the hours it worked, why a fixed-fee job is over budget, who staffs
what over the next quarter, and whether the firm may accept a new engagement at all.
Each turns the firm's own time, billing, staffing and relationship data into a
checked work product with the arithmetic shown.

These sit on the **practitioner and firm-operations side**. The commercial cycle of
a single engagement — qualify, scope, price, propose, contract, deliver, invoice,
close out — already lives in
[`domain-business-strategy/client-services/`](../../domain-business-strategy/client-services/README.md)
and is sequenced by [`client-services-studio/`](../../client-services-studio/README.md);
nothing here duplicates it.

**Prefix:** `proserv_` · **Category:** `specialized-fields/professional-services`

## Contents

| File | Use |
|---|---|
| [`proserv_utilization_realization_review.md`](proserv_utilization_realization_review.md) | Quarter or year review: utilization by grade against grade targets, standard value → billed → collected, write-downs by cause, leverage, and the margin × productivity × leverage levers on profit per partner |
| [`proserv_fixed_fee_overrun_diagnosis.md`](proserv_fixed_fee_overrun_diagnosis.md) | A running fixed-fee or capped engagement over budget: evidence-based percent complete, earned hours, two EACs, overrun split by cause, staffing-mix effect, recovery options priced against the margin floor |
| [`proserv_engagement_staffing_plan.md`](proserv_engagement_staffing_plan.md) | Rolling 8–13 week plan: supply by grade after leave, hard and soft bookings, the binding grade, gap-closing moves in order with their cost, named-assignment checks |
| [`proserv_independence_conflict_check.md`](proserv_independence_conflict_check.md) | Accounting and consulting client acceptance: relationship map, independence vs conflict classification, threats and safeguards, prohibited services, consent feasibility, accept/decline record |

Order of use: independence check before acceptance → staffing plan once accepted →
overrun diagnosis while delivering → utilization and realization review at period
end, which names the engagements that need the overrun diagnosis next time.

## Guards (every prompt)

- **Firm data stays the firm's.** People appear by ID in anything circulated; time
  and billing figures are source-tagged `[data]` / `[estimate]` / `[assumption]`.
- **Professional determinations stay with the profession.** Independence and
  ethics decisions are made by the firm's designated independence or ethics partner
  under the governing code (AICPA, IESBA, regulator rules); code sections are cited
  only as supplied or marked `[verify]`.
- **Contract positions go to the partner and counsel.** Whether a SOW assumption was
  breached or a change is chargeable is flagged, not decided.
- **Not accounting, tax or legal advice.** Firm financial figures are management
  information for discussion with the firm's accountant.

## Boundaries — not here

| If you need… | Go to |
|---|---|
| Qualifying, scoping, pricing, proposing, contracting, invoicing one engagement | [`client-services-studio/`](../../client-services-studio/README.md) and [`domain-business-strategy/client-services/`](../../domain-business-strategy/client-services/README.md) |
| A solo practice's sellable days and bench date | [`services_capacity_and_utilization_planner.md`](../../domain-business-strategy/client-services/services_capacity_and_utilization_planner.md) |
| One finished engagement's estimate-versus-actual close-out | [`finance_engagement_profitability_postcalc.md`](../../domain-finance/corporate-finance-fpa/finance_engagement_profitability_postcalc.md) |
| Revenue and capacity dependence on one client | [`services_client_concentration_risk_check.md`](../../domain-business-strategy/client-services/services_client_concentration_risk_check.md) |
| A law firm's conflicts check | [`legal_conflicts_check_memo.md`](../../domain-legal/ethics-professional-conduct/legal_conflicts_check_memo.md) |
| Engagement letters and SOW clauses | [`domain-legal/`](../../domain-legal/) — e.g. `client-intake-communications/legal_engagement_letter_drafter.md` |
| Pricing a construction change order | [`trades_change_order_pricing_notice.md`](../trades/trades_change_order_pricing_notice.md) |
