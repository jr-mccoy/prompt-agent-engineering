# Gate B red flags

Ten structural conditions over a contract summary. Critical and high block unless
accepted with a recorded rationale; medium warns.

| Flag | Severity | Condition | Why it matters |
|---|---|---|---|
| `unlimited_liability` | critical | `liability_cap` absent, zero, or `"unlimited"` | Exposure unbounded by the engagement's value |
| `uncapped_ip_indemnity` | critical | `ip_indemnity_capped` is `false` | The most common serious gap when subcontracting |
| `unilateral_scope_change` | critical | `unilateral_scope_change` is `true` | The client may vary what you owe without agreeing a price |
| `unbounded_ip_assignment` | high | `ip_assignment_scope` is `"all_work_product"` | Assignment reaches beyond deliverables to your tools and methods |
| `payment_terms_long` | high | `payment_terms_days` > 60 | Working-capital exposure, worse still when subcontracting |
| `no_termination_compensation` | high | convenience termination with no compensation | Bench cost and committed third-party costs fall on you |
| `unilateral_set_off` | high | `set_off` is `"unilateral"` | The client becomes judge of its own claim |
| `counsel_review` | high | `counsel_reviewed` is absent or false | Absence of review is itself a finding |
| `no_suspension_right` | medium | `suspension_right` is `false` | The payment clause has no enforcement behind it |
| `unpriced_transition_assistance` | medium | `transition_assistance` is `"unpriced"` | Commonly the largest unpriced liability in long engagements |
| `no_undisputed_portion_clause` | medium | `undisputed_portion_payable` is `false` | A small dispute holds an entire invoice |

## Accepting a flag

A blocking flag can be carried deliberately:

```json
"accepted_risks": [
  { "flag": "payment_terms_long", "rationale": "offset by a 40% deposit" }
]
```

The `rationale` is required. An entry without one does not unblock, because the
point of the mechanism is that carrying a known risk is a decision with a name on
it rather than an oversight.

## Where the drafting positions live

This scan names the problem. The clause language and the negotiating ladder are in
`domain-legal/contracts-transactional/`:

| Flag family | Prompt |
|---|---|
| Liability, IP, indemnity, warranties, termination language | `legal_contract_clause_redline_targeted.md` |
| Payment terms, late fees, suspension, set-off, retainage | `legal_payment_terms_and_late_fee_review.md` |
| Termination economics — kill fee, notice, WIP, transition | `legal_termination_economics_provider_side.md` |
| Flow-down where you subcontract | `legal_subcontractor_flow_down_check.md` |
| Scoring all findings together | `legal_contract_risk_heatmap.md` |

## Not legal advice

The scan reads a summary a human produced. It cannot tell you what a clause means,
whether it is enforceable, or what your jurisdiction does with it. Counsel review
before signature is a gate condition.
