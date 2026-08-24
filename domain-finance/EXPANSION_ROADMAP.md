# Finance & Economics — Expansion Roadmap

**Status as of 2026-06-08:** **Library complete — Phases 1–5 built (135 prompts).** Phase 1 (23): `financial-statement-analysis/` (11) and `valuation/` (12). Phase 2 (30): `investing-research/` (11), `credit-lending/` (9), and `risk-management/` (10). Phase 3 (29): `corporate-finance-fpa/` (11), `accounting-controllership/` (10), and `treasury-capital-markets/` (8). Phase 4 (46): `mergers-acquisitions/` (9), `markets-macro/` (9), `tax-planning/` (8), `regulatory-compliance/` (8), and `personal-finance-planning/` (12). Phase 5 (7): `quant-fintech-data/` (7). Promoted from `domain-specialized-fields/finance/`; [`field_guide.md`](./field_guide.md) anchors conventions.

**Target size:** ~135 prompts across 14 subdirectories, authored in 5 phases.

This document enumerates every planned prompt with:
- target subdirectory
- proposed filename (`finance_` prefix, per repo naming convention)
- 1-line objective
- difficulty tag

Prompts can be added in any order; the phase grouping is for batch-authoring efficiency and reuse-value sequencing, not hard dependency.

---

## Positioning & Boundaries

This domain is the **quantitative, model-grade, practitioner finance library**. It deliberately does **not** duplicate adjacent domains:

| Adjacent domain | Owns | This domain owns instead |
|---|---|---|
| `domain-business-strategy/analysis/` | High-level / qualitative strategy framing | The quantitative modeling and analysis behind it |
| `domain-professional-writing/domain-specific/` (CPA, financial advisor) | *Client-facing communication* of finance | The *analysis* that the communication reports |
| `domain-legal/corporate-ma/` | The *legal* side of deals (DD lists, disclosure schedules, §409A/QSBS) | The *financial* side (accretion/dilution, synergy, deal model) |
| `domain-idea-to-product/stage-3-market-research/` | Startup unit economics (LTV/CAC) | Institution-grade corporate & investment finance |

**Audience:** financial analysts, equity/credit research, FP&A, controllers, treasury, risk managers, underwriters, economists, financial planners/advisors, and finance leaders.

---

## Authoring Conventions (load-bearing — apply to every prompt)

1. **No fabrication.** Never invent figures, ratios, peer benchmarks, regulatory citations, or accounting-standard thresholds. Every number traces to a stated input or a named, real source.
2. **Calculation auditability.** Show formula → inputs → result. Use **NE-11 (Embedded Calculation Formulas)** so output can be checked.
3. **Scenario range, not point estimates.** Base / bull / bear (or stress) with explicit, internally consistent assumptions (**NE-10**).
4. **Currency & jurisdiction flag.** State accounting framework (US GAAP vs IFRS), tax jurisdiction, and a "verify against current regulations as of [date]" line where rules govern the output.
5. **Adversarial stress-test built in.** Thesis/valuation/credit prompts include **QA-02 (Adversarial Stress-Test)** and, where useful, **RP-03 (bull/bear debate)**.
6. **Assumption transparency.** All inputs, assumptions, and excluded factors stated explicitly.
7. **Bias guardrails.** Name the relevant pitfall (anchoring, confirmation, recency, survivorship, precision-illusion, tail-risk blindness) and require a disconfirming check.
8. **Standard structure + lock.** Frontmatter → Objective → When to Use → Inputs → Constraints (Must / Must Not) → Instructions → Output Format → Verification checklist + false-positive matrix.
9. **Disclaimer discipline.** One clean "informational only, not financial/tax/investment advice" line — not boilerplate smothering every section (mirror the legal domain's restraint).

Default technique stack (from `field_guide.md`): **NE-11, NE-10, QA-01, DS-02, RT-05** core; **QA-02, RT-03, DT-02, QA-04, RT-02** high-value.

---

## Phase Overview

| Phase | Theme | Subdirectories | Prompts |
|---|---|---|---|
| **1** ✅ | Core analyst toolkit (**built**) | financial-statement-analysis, valuation | 23 |
| **2** ✅ | Capital & risk (**built**) | investing-research, credit-lending, risk-management | 30 |
| **3** ✅ | Corporate & operating finance (**built**) | corporate-finance-fpa, accounting-controllership, treasury-capital-markets | 29 |
| **4** ✅ | Specialized & advisory (**built**) | mergers-acquisitions, markets-macro, tax-planning, regulatory-compliance, personal-finance-planning | 46 |
| **5** ✅ | Quant & fintech (**built**) | quant-fintech-data | 7 |
| | | **Total** | **~135** |

---

## Phase 1 — Core Analyst Toolkit (23) ✅ BUILT (2026-06-08)

### `financial-statement-analysis/` (11)

| File | Objective | Difficulty |
|------|-----------|------------|
| `finance_ratio_analysis_engine.md` | Compute and interpret the full ratio set (liquidity/profitability/leverage/efficiency/valuation) with formulas shown and peer/industry context | intermediate |
| `finance_common_size_trend_analyzer.md` | Common-size and multi-period trend analysis flagging directional shifts and inflection points | intermediate |
| `finance_quality_of_earnings_review.md` | Assess earnings quality: accruals, one-timers, revenue timing, capitalization choices, cash conversion | advanced |
| `finance_cash_flow_quality_analyzer.md` | Decompose CFO/CFI/CFF, reconcile to net income, test FCF durability | intermediate |
| `finance_working_capital_analysis.md` | Cash-conversion-cycle and working-capital efficiency analysis with driver attribution | intermediate |
| `finance_footnote_red_flag_scanner.md` | Scan footnotes/MD&A for accounting red flags (related parties, off-balance-sheet, revenue policy changes) | advanced |
| `finance_segment_analysis.md` | Segment-level revenue/margin/asset analysis to locate value and drag | intermediate |
| `finance_peer_benchmarking_builder.md` | Build a like-for-like peer comparison table with normalization adjustments | intermediate |
| `finance_dupont_decomposition.md` | 3- and 5-step DuPont ROE decomposition with driver narrative | beginner |
| `finance_liquidity_solvency_stress_check.md` | Stress liquidity/solvency against revenue/margin/rate shocks (Altman-Z aware) | intermediate |
| `finance_financial_statement_anomaly_detector.md` | Detect anomalies/inconsistencies across the three statements (Beneish-aware) | advanced |

### `valuation/` (12)

| File | Objective | Difficulty |
|------|-----------|------------|
| `finance_dcf_model_builder.md` | Build a defensible DCF: FCFF/FCFE projection, WACC, terminal value, with assumption register | advanced |
| `finance_dcf_model_auditor.md` | Audit an existing DCF for methodology, assumption reasonableness, and input sensitivity errors | advanced |
| `finance_trading_comps_builder.md` | Construct a trading-comparables set with multiple selection, normalization, and outlier handling | intermediate |
| `finance_precedent_transactions_analysis.md` | Precedent-transaction multiples with control-premium and timing adjustments | intermediate |
| `finance_lbo_model_builder.md` | Build an LBO: sources/uses, debt schedule, returns (IRR/MOIC), and covenant headroom | advanced |
| `finance_dividend_discount_model.md` | DDM (Gordon / multi-stage) with implied-growth and reinvestment checks | intermediate |
| `finance_sum_of_the_parts_valuation.md` | SOTP build with per-segment method selection and holding-company discount | advanced |
| `finance_wacc_builder.md` | Cost-of-capital build: CAPM, capital weights, size/country premia, with sensitivity | intermediate |
| `finance_terminal_value_sanity_check.md` | Reasonableness test on terminal value (implied multiple, perpetuity-growth bounds) | intermediate |
| `finance_valuation_sensitivity_scenario.md` | Sensitivity tables + scenario matrix across the value-driving assumptions | intermediate |
| `finance_football_field_synthesizer.md` | Synthesize multiple methods into a valuation range with weighting rationale | intermediate |
| `finance_reverse_dcf_expectations.md` | Reverse-DCF: back out the growth/margin the current price implies and test plausibility | advanced |

---

## Phase 2 — Capital & Risk (30) ✅ BUILT (2026-06-08)

### `investing-research/` (11)

| File | Objective | Difficulty |
|------|-----------|------------|
| `finance_investment_thesis_builder.md` | Build a thesis: catalysts, variant view, valuation, risks, exit criteria, disconfirming evidence | advanced |
| `finance_bull_bear_debate_memo.md` | Structured bull/bear memo via opposing-analyst debate with decision synthesis | intermediate |
| `finance_10k_10q_teardown.md` | Systematic 10-K/10-Q teardown extracting drivers, risks, and changes vs prior filings | intermediate |
| `finance_earnings_preview_builder.md` | Pre-earnings setup: expectations, key metrics, scenarios, what would move the stock | intermediate |
| `finance_earnings_review_analyzer.md` | Post-print analysis: beat/miss attribution, guidance read-through, thesis impact | intermediate |
| `finance_competitive_moat_analyzer.md` | Moat/durability analysis (network/scale/switching/IP/brand) with erosion tests | intermediate |
| `finance_short_thesis_constructor.md` | Construct a short thesis with catalyst, borrow/squeeze risk, and asymmetry assessment | advanced |
| `finance_catalyst_map_builder.md` | Map dated catalysts and their probability-weighted impact on the thesis | intermediate |
| `finance_position_sizing_framework.md` | Position-size via conviction/edge/odds (Kelly-aware) with risk limits | advanced |
| `finance_portfolio_construction_review.md` | Review portfolio for concentration, factor tilt, correlation, and sizing discipline | advanced |
| `finance_management_quality_assessment.md` | Assess management capital-allocation track record and incentive alignment | intermediate |

### `credit-lending/` (9)

| File | Objective | Difficulty |
|------|-----------|------------|
| `finance_five_cs_credit_analysis.md` | 5-Cs credit assessment (capacity/capital/conditions/character/collateral) with rating | intermediate |
| `finance_credit_memo_builder.md` | Full credit memo: facility, rationale, risk rating, structure, covenants, monitoring | advanced |
| `finance_covenant_design_aid.md` | Design financial covenants with headroom sizing and definitions | advanced |
| `finance_covenant_headroom_monitor.md` | Track covenant compliance and project headroom under downside cases | intermediate |
| `finance_debt_capacity_sizing.md` | Size debt capacity from cash flow / leverage / coverage with cushion | intermediate |
| `finance_pd_lgd_ead_framing.md` | Frame PD / LGD / EAD inputs and expected-loss logic (methodology, not invented data) | advanced |
| `finance_watchlist_early_warning.md` | Early-warning indicator set and watchlist trigger design | intermediate |
| `finance_workout_restructuring_options.md` | Distressed-credit workout/restructuring option analysis (amend-extend, DDE, recovery) | advanced |
| `finance_consumer_credit_decision_framework.md` | Consumer/SME underwriting decision framework with bias/fair-lending guardrails | intermediate |

### `risk-management/` (10)

| File | Objective | Difficulty |
|------|-----------|------------|
| `finance_enterprise_risk_register.md` | Build an enterprise risk register with likelihood/impact, owners, and treatment | intermediate |
| `finance_market_risk_var_stress.md` | Market-risk framing: VaR methods, limitations, and complementary stress tests | advanced |
| `finance_liquidity_risk_analysis.md` | Liquidity-risk analysis: runway, funding concentration, LCR-style buffers | advanced |
| `finance_operational_risk_rcsa.md` | Operational-risk control self-assessment (RCSA) with KRIs | intermediate |
| `finance_interest_rate_risk_analysis.md` | Interest-rate risk (duration/gap, banking-book IRRBB) with rate-shock impact | advanced |
| `finance_stress_test_scenario_design.md` | Design coherent, severe-but-plausible stress scenarios across drivers | advanced |
| `finance_model_risk_validation.md` | Validate a financial model (conceptual soundness, inputs, outcomes, governance) | advanced |
| `finance_hedging_strategy_designer.md` | Design a hedging program (instrument selection, ratio, cost, residual risk) | advanced |
| `finance_tail_risk_premortem.md` | Tail-risk / black-swan pre-mortem on a position, portfolio, or plan | intermediate |
| `finance_counterparty_risk_assessment.md` | Counterparty/credit-exposure assessment with concentration and netting | intermediate |

---

## Phase 3 — Corporate & Operating Finance (29) ✅ BUILT (2026-06-08)

### `corporate-finance-fpa/` (11)

| File | Objective | Difficulty |
|------|-----------|------------|
| `finance_three_statement_model_builder.md` | Build an integrated, balancing three-statement model with driver assumptions | advanced |
| `finance_budget_variance_investigator.md` | Budget-vs-actual variance analysis isolating one-time vs recurring root causes | intermediate |
| `finance_rolling_forecast_designer.md` | Design a rolling forecast process with drivers, cadence, and accuracy tracking | intermediate |
| `finance_driver_based_scenario_model.md` | Driver-based scenario/operating model with toggle assumptions | advanced |
| `finance_capital_allocation_framework.md` | Capital-allocation framework ranking reinvest / M&A / debt-paydown / return | advanced |
| `finance_capex_prioritization_analysis.md` | Capex prioritization via NPV/IRR/payback with strategic and risk overlays | intermediate |
| `finance_dividend_buyback_policy_analysis.md` | Dividend vs buyback policy analysis with payout sustainability and signaling | intermediate |
| `finance_board_finance_package_builder.md` | Assemble a board-grade finance package (results, forecast, KPIs, risks) | intermediate |
| `finance_unit_economics_model.md` | Build/critique unit economics (contribution margin, payback, cohort) | intermediate |
| `finance_breakeven_operating_leverage.md` | Break-even and operating-leverage analysis with sensitivity | beginner |
| `finance_cost_structure_optimization.md` | Analyze fixed/variable cost structure and identify optimization levers | intermediate |

### `accounting-controllership/` (10)

| File | Objective | Difficulty |
|------|-----------|------------|
| `finance_month_end_close_checklist.md` | Generate a month-end close checklist with owners, dependencies, and SLAs | beginner |
| `finance_account_reconciliation_protocol.md` | Structured account-reconciliation protocol with exception handling | beginner |
| `finance_revenue_recognition_asc606_memo.md` | ASC 606 / IFRS 15 five-step revenue-recognition analysis memo | advanced |
| `finance_lease_accounting_asc842_analysis.md` | ASC 842 / IFRS 16 lease classification and measurement analysis | advanced |
| `finance_accrual_deferral_logic_builder.md` | Build accrual/deferral entries with support and reversal logic | intermediate |
| `finance_sox_internal_controls_designer.md` | Design SOX internal controls / control matrix for a process | advanced |
| `finance_journal_entry_review_protocol.md` | JE review protocol for completeness, accuracy, and segregation of duties | intermediate |
| `finance_technical_accounting_memo_writer.md` | Structure a technical accounting position memo (issue/analysis/conclusion) | advanced |
| `finance_audit_pbc_preparation.md` | Prepare an audit PBC list and supporting-schedule package | intermediate |
| `finance_management_reporting_kpi_pack.md` | Build a management-reporting KPI pack with definitions and drill-downs | intermediate |

### `treasury-capital-markets/` (8)

| File | Objective | Difficulty |
|------|-----------|------------|
| `finance_cash_flow_forecasting_model.md` | Direct/indirect cash-flow forecast with liquidity buffer and variance loop | intermediate |
| `finance_capital_structure_optimization.md` | Optimize capital structure (target leverage, cost, flexibility, ratings impact) | advanced |
| `finance_debt_issuance_analysis.md` | Analyze a debt issuance (size, tenor, fixed/float, covenants, all-in cost) | advanced |
| `finance_liquidity_runway_covenant_analysis.md` | Project liquidity runway against covenant and maturity walls | intermediate |
| `finance_treasury_hedging_program_design.md` | Design a treasury hedging program (FX/rates/commodity) with policy limits | advanced |
| `finance_investment_policy_statement_builder.md` | Build a corporate/institutional investment policy statement | intermediate |
| `finance_capital_raise_readiness_assessment.md` | Assess readiness for a capital raise (debt or equity) with gap list | intermediate |
| `finance_bank_relationship_rfp_framework.md` | Structure a banking-services RFP and relationship-evaluation framework | beginner |

---

## Phase 4 — Specialized & Advisory (46) ✅ BUILT (2026-06-08)

### `mergers-acquisitions/` (9)

| File | Objective | Difficulty |
|------|-----------|------------|
| `finance_accretion_dilution_analysis.md` | Accretion/dilution analysis with financing mix and breakeven synergy | advanced |
| `finance_ma_deal_model_builder.md` | Build a merger model (combined financials, financing, pro-forma metrics) | advanced |
| `finance_synergy_estimation_framework.md` | Estimate and stage cost/revenue synergies with realization risk and timing | advanced |
| `finance_financial_due_diligence_workstream.md` | Run the financial DD workstream: QoE, net debt, working-capital target | advanced |
| `finance_purchase_price_allocation.md` | Purchase-price allocation logic (intangibles, goodwill) for modeling | advanced |
| `finance_earnout_structuring_analysis.md` | Structure and value an earn-out with metric, threshold, and payout design | advanced |
| `finance_deal_financing_structure_analysis.md` | Analyze deal financing structures (cash/stock/debt) and impact | intermediate |
| `finance_integration_finance_plan.md` | Post-close integration finance plan (Day-1 reporting, synergy tracking) | intermediate |
| `finance_deal_post_mortem_review.md` | Post-acquisition post-mortem vs deal thesis and synergy targets | intermediate |

### `markets-macro/` (9)

| File | Objective | Difficulty |
|------|-----------|------------|
| `finance_economic_scenario_modeler.md` | Build internally consistent base/optimistic/pessimistic/stress macro scenarios | advanced |
| `finance_macro_indicator_dashboard_interpreter.md` | Interpret a macro dashboard (growth/inflation/labor/credit) into a read | intermediate |
| `finance_rate_path_yield_curve_analysis.md` | Analyze rate path and yield-curve shape for signal and positioning | advanced |
| `finance_fx_exposure_analysis.md` | Map and analyze FX exposure (transaction/translation/economic) | intermediate |
| `finance_commodity_exposure_analysis.md` | Analyze commodity-price exposure and pass-through to financials | intermediate |
| `finance_sector_rotation_framework.md` | Cycle-based sector-rotation framework with regime indicators | intermediate |
| `finance_inflation_regime_analysis.md` | Inflation-regime analysis and asset/sector implications | advanced |
| `finance_central_bank_reaction_function.md` | Model a central-bank reaction function and policy-path scenarios | advanced |
| `finance_cross_asset_correlation_analysis.md` | Cross-asset correlation/regime analysis for diversification and risk | advanced |

### `tax-planning/` (8 — analysis, not legal/tax advice)

| File | Objective | Difficulty |
|------|-----------|------------|
| `finance_entity_structure_tax_comparison.md` | Compare entity structures (C/S/LLC/partnership) on tax outcomes | advanced |
| `finance_multi_year_tax_projection.md` | Build a multi-year tax projection across income/deduction scenarios | intermediate |
| `finance_capital_gains_harvesting_analysis.md` | Tax-loss/gain harvesting analysis with wash-sale and bracket awareness | intermediate |
| `finance_equity_compensation_tax_analysis.md` | ISO/NSO/RSU/ESPP tax-treatment and exercise/sale-timing scenarios | advanced |
| `finance_state_nexus_apportionment_mapper.md` | Map multistate nexus and apportionment exposure (analysis only) | advanced |
| `finance_rd_and_credits_mapping.md` | Map R&D and other credits/incentives to qualifying activities | intermediate |
| `finance_charitable_giving_tax_strategy.md` | Model charitable-giving strategies (DAF, appreciated stock, bunching) | intermediate |
| `finance_retirement_account_tax_optimization.md` | Optimize across pre-tax/Roth/taxable with conversion-ladder scenarios | advanced |

### `regulatory-compliance/` (8)

| File | Objective | Difficulty |
|------|-----------|------------|
| `finance_regulatory_requirement_mapper.md` | Map applicable regulations (SEC/Basel/Dodd-Frank/MiFID/etc.) to activities | advanced |
| `finance_compliance_gap_analysis.md` | Gap analysis of current state vs regulatory requirements with remediation | advanced |
| `finance_aml_kyc_program_designer.md` | Design an AML/KYC program (risk rating, CDD/EDD, monitoring) | advanced |
| `finance_mdna_disclosure_review.md` | Review MD&A / disclosure for completeness, consistency, and required items | intermediate |
| `finance_reg_bi_fiduciary_check.md` | Reg-BI / fiduciary-standard check on a recommendation process | intermediate |
| `finance_basel_capital_adequacy_analysis.md` | Basel III capital-adequacy and RWA analysis (methodology framing) | advanced |
| `finance_regulatory_filing_calendar.md` | Build a regulatory filing calendar with owners and deadlines | beginner |
| `finance_sanctions_screening_program.md` | Design a sanctions-screening program and escalation workflow | intermediate |

### `personal-finance-planning/` (12)

| File | Objective | Difficulty |
|------|-----------|------------|
| `finance_retirement_projection_model.md` | Retirement projection: required savings rate, funding gap, scenario bands | intermediate |
| `finance_monte_carlo_withdrawal_analysis.md` | Monte-Carlo retirement-withdrawal and sequence-of-returns risk analysis | advanced |
| `finance_education_funding_planner.md` | Education-funding plan (529/cost-inflation/required contributions) | intermediate |
| `finance_asset_allocation_glidepath.md` | Build an age/goal-based asset-allocation glidepath with rebalancing rules | intermediate |
| `finance_debt_payoff_strategy.md` | Debt-payoff strategy (avalanche vs snowball) with interest/time tradeoffs | beginner |
| `finance_tax_aware_withdrawal_sequencing.md` | Tax-efficient drawdown sequencing across account types in retirement | advanced |
| `finance_insurance_needs_analysis.md` | Life/disability/LTC insurance-needs analysis with coverage gap | intermediate |
| `finance_emergency_fund_sizing.md` | Size an emergency fund from income stability and fixed-cost analysis | beginner |
| `finance_buy_vs_rent_analysis.md` | Buy-vs-rent analysis with full cost of ownership and breakeven horizon | intermediate |
| `finance_fire_planning_model.md` | FIRE planning: target number, savings rate, withdrawal-rate sensitivity | intermediate |
| `finance_estate_beneficiary_review.md` | Estate/beneficiary review checklist (analysis; routes legal docs to attorney) | intermediate |
| `finance_net_worth_cashflow_diagnostic.md` | Personal net-worth and cash-flow diagnostic with savings-rate read | beginner |

---

## Phase 5 — Quant & Fintech (7) ✅ BUILT (2026-06-08)

### `quant-fintech-data/` (7)

| File | Objective | Difficulty |
|------|-----------|------------|
| `finance_backtest_design_critique.md` | Design or critique a backtest (look-ahead, survivorship, overfitting checks) | advanced |
| `finance_factor_model_builder.md` | Build/interpret a factor model (exposure, attribution, multicollinearity) | advanced |
| `finance_fraud_anomaly_detection_framework.md` | Transaction fraud/anomaly-detection feature and rule framework | advanced |
| `finance_alt_data_thesis_evaluator.md` | Evaluate an alternative-data signal for edge, decay, and capacity | advanced |
| `finance_time_series_forecast_critique.md` | Critique a time-series forecast (stationarity, validation, error bands) | intermediate |
| `finance_trading_strategy_premortem.md` | Pre-mortem a trading strategy (regime risk, costs, crowding, capacity) | intermediate |
| `finance_risk_model_validation.md` | Validate a quantitative risk model against benchmarks and stress | advanced |

---

## Authoring Order Recommendation

1. **Phase 1** — highest reuse; anchors every other prompt. Statement analysis + valuation are referenced by research, credit, and M&A.
2. **Phase 2** — investing/credit/risk; completes the buy-side and lending analyst corpus.
3. **Phase 3** — corporate/FP&A/accounting/treasury; completes the in-house finance corpus.
4. **Phase 4** — specialized & advisory; M&A, macro, tax, regulatory, and personal planning.
5. **Phase 5** — quant/fintech, only if demand warrants.

No hard dependencies between phases — they can be authored in any order, but Phase 1 first maximizes cross-referencing (`related_prompts`).

---

## Sizing Estimate

| Phase | Prompts | Avg. lines/prompt | Approx. total lines |
|------|---------|-------------------|---------------------|
| 1    | 23      | 210               | ~4,800              |
| 2    | 30      | 210               | ~6,300              |
| 3    | 29      | 200               | ~5,800              |
| 4    | 46      | 190               | ~8,700              |
| 5    | 7       | 210               | ~1,500              |
| **Total** | **135** | — | **~27,100 lines** |

---

*Last updated: 2026-06-08*
*Domain promoted from `domain-specialized-fields/finance/` to top-level `domain-finance/` on 2026-06-08.*
