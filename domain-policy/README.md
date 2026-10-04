# Domain: Policy

Public-policy analysis and communication. Policy work has constraints that general business analysis doesn't: options must be evaluated on equity and distributional effects, political viability, and reversibility alongside cost and effectiveness; the evidence is usually contested; and recommendations rest on values tradeoffs that honest analysis names rather than hides. The prompts in this domain enforce that discipline.

Fifteen prompts: nine flat analysis prompts at the domain root, plus six in [`public-administration/`](public-administration/README.md). Four root prompts follow the core analysis in order: frame the problem, map the stakeholders, test feasibility, then communicate the options in a form a principal who wasn't in the working sessions can decide from. Five more cover the instruments around that chain: regulatory impact analysis, program evaluation design, rulemaking/consultation comments, legislative bill analysis, and cross-jurisdiction comparison. The `public-administration/` subfolder covers running government itself: budget shortfalls, grant post-award compliance, the agency's rulemaking plan, constituent casework, performance measures, and staff briefs for public meetings. Users are policy analysts, executives, consultants, advocates, government-affairs teams, public-sector staff, and civic-minded individuals organizing their own thinking on a policy debate.

## When to use this domain

- A principal (government body, foundation, NGO leadership, board, coalition partner) must choose among policy responses to a defined problem.
- An internal recommendation on which public-policy posture to advocate.
- Think-tank or academic comparison of policy options for an external audience.
- Organizing your own position on a live policy debate with auditable rigor.
- Running the agency's own work: closing a budget gap, managing a grant after award, planning a rulemaking, answering constituents, setting performance measures, briefing a council or board (`public-administration/`).

## When NOT to use this domain (use a different one)

- **The "policy" is internal operations, not public policy** → `domain-decision-making/documentation/decisiondoc_options_memo.md`.
- **The recommendation is binary (do / don't)** → a simpler decision memo from `domain-decision-making/documentation/`.
- **Persuasion is the goal rather than auditable analysis** → `domain-product-management/` or `domain-professional-writing/`.
- **Regulatory risk monitoring for a business** → `domain-decision-making/decisioning_regulatory_risk_radar.md`.

## Prompts in this domain

```
domain-policy/
├── policy_*.md (9)            core analysis chain + instruments
└── public-administration/ (6) running government: budget, grants, rulemaking, casework, measures, meetings
```

### Root (9)

| File | Purpose |
|------|---------|
| `policy_problem_framing.md` | Frame the problem before anyone proposes solutions: who is affected and by how much, the measured current state, the no-action trajectory, and the contested framings |
| `policy_stakeholder_coalition_map.md` | Map stakeholders on position, intensity, influence, interests, coalition and movability, then derive the coalition structures that decide outcomes |
| `policy_implementation_feasibility.md` | Test a proposal's implementation feasibility in depth: legal authority, administrative capacity, funding, a realistic timeline benchmarked against comparable efforts, and dependencies |
| `policy_options_memo.md` | Compare 3–5 policy options on effectiveness, feasibility, fiscal cost, equity, political viability, reversibility, and unintended consequences; recommend with the values tradeoffs named |
| `policy_regulatory_impact_analysis.md` | Government-side cost-benefit / RIA of a proposed rule: failure addressed, baseline, 3+ options, monetised and non-monetised effects, discounting, distribution, break-even and sensitivity (A-4 / Green Book / OECD practice, jurisdiction-neutral) |
| `policy_program_evaluation_design.md` | Evaluation design for a public program: theory of change, impact/process/economic questions, counterfactual chosen from the rollout (RCT, RDD, DiD, ITS, process-only), MDE, gaming-aware indicators, ethics and governance |
| `policy_public_comment_letter.md` | A stakeholder's rulemaking or consultation comment: provision-anchored, evidence the agency can use, rebuttal of the impact analysis, ranked redline-style requested changes |
| `policy_legislative_bill_analysis.md` | Section-by-section bill analysis against quoted current law, technical sections cleared, fiscal and implementation implications, stakeholder effects, questions for counsel, amendments |
| `policy_cross_jurisdiction_comparison.md` | Compare how other jurisdictions handle the problem on a common grid, separate outcomes from evaluated effects, name the drivers, and test transferability before borrowing, adapting or avoiding |

### [`public-administration/`](public-administration/README.md) (6)

| File | Purpose |
|------|---------|
| `policy_local_budget_shortfall_options.md` | Municipal/county/district budget gap: structural vs one-time, legal screen, options by dollars, service units, equity and reversibility, balanced packages with the reserve tested |
| `policy_grant_post_award_compliance.md` | Recipient-side grant compliance after award: cost allowability testing, payroll charging, subrecipient monitoring, reporting calendar, audit readiness (US 2 CFR 200 as worked example) |
| `policy_agency_rulemaking_plan.md` | Agency side of rulemaking: authority, procedure, required analyses, comment taxonomy and significance test, re-proposal risk, backward timeline with gates |
| `policy_constituent_casework_system.md` | Elected-office or agency correspondence and casework: triage, privacy release, templates, escalation ladder, tracking, staffing |
| `policy_agency_performance_measures.md` | Output vs outcome measures, operational definitions, targets from baseline and capacity, gaming risks with paired measures |
| `policy_public_meeting_staff_brief.md` | Staff report and official's one-page brief before a council, board or commission vote: motion, fiscal impact, options, public input, likely questions, procedure |

### Quick routing

| You're saying | Use |
|---|---|
| "We're $8 M short next year — what are the options?" | `public-administration/policy_local_budget_shortfall_options.md` |
| "We got the federal grant — now how do we not get audited out of it?" | `public-administration/policy_grant_post_award_compliance.md` |
| "The legislature told us to write a rule by 2028" | `public-administration/policy_agency_rulemaking_plan.md` |
| "We're commenting on the agency's proposed rule" | `policy_public_comment_letter.md` |
| "Our office is drowning in constituent mail" | `public-administration/policy_constituent_casework_system.md` |
| "Our measures count activity, not results" | `public-administration/policy_agency_performance_measures.md` |
| "Did the program cause the improvement?" | `policy_program_evaluation_design.md` |
| "The item goes to council on the 20th — brief the members" | `public-administration/policy_public_meeting_staff_brief.md` |

## How prompts in this domain compose

Run the core chain in order: problem framing → stakeholder/coalition map → implementation feasibility → options memo. The other five root prompts plug into it: cross-jurisdiction comparison and regulatory impact analysis feed the options memo; program evaluation design follows a chosen option into delivery; bill analysis and the public comment letter respond to a specific bill or proposed rule someone else has tabled. The options memo sits at the end of the chain, not the start. Deliberation happens upstream (research, modeling, stakeholder input — e.g., `domain-reasoning-craft/systems/systems_unintended_consequence_scan.md` for second-order effects, `domain-reasoning-craft/epistemic/epistemic_disagreement_diagnosis.md` for contested evidence), and the memo communicates it. Its internal-operations sibling is `decisiondoc_options_memo.md` in `domain-decision-making/documentation/`. Once an option is chosen, `public-administration/` runs it: the rulemaking plan schedules the regulatory impact analysis into the docket, performance measures define what the program reports, and the staff brief carries budget and policy items to the deciding body.

## Frontmatter conventions specific to this domain

Prompts carry the machine-readable `reasoning:` block. The options memo's profile is characteristic of the domain: `stakes: high`, `horizon: years`, `uncertainty: deep`, `domain_complexity: regulated`, with `normative` in the styles list — policy analysis is explicitly values-laden, and the prompts require the values tradeoffs to be stated rather than smuggled.

Filenames use the `policy_` prefix everywhere, including `public-administration/`. Root prompts carry a per-prompt `category:` (`policy/options-analysis`, `policy/regulatory-impact`, …); every prompt in `public-administration/` uses `category: policy/public-administration`.

## Coverage

The five analyses tracked for coverage Wave 4 in [`meta/COVERAGE_ROADMAP.md`](../meta/COVERAGE_ROADMAP.md) — cost-benefit / regulatory impact analysis, program evaluation design, public comment letters on proposed rules, legislative bill analysis, and cross-jurisdiction comparison — shipped in Wave 6 (2026-10-02). Public administration (budget shortfalls, grant post-award compliance, agency rulemaking plans, constituent casework, performance measures, public-meeting staff briefs) shipped in coverage Wave 7 (2026-10-03) as `public-administration/`. Related work stays elsewhere: logic models and education-program evaluation frameworks (`domain-education-teaching/program/evaluation-analytics/`), estimator-level causal inference (`domain-science/statistics/science_causal_inference_design.md`), testimony prep and op-eds (`domain-science/public-engagement/`), grant proposals before award (`domain-business-strategy/nonprofit/`, `domain-science/grants-funding/`), nonprofit budgets with donor restrictions (`domain-business-strategy/nonprofit/nonprofit_operating_budget_restrictions.md`), a company's compliance view of a new rule (`domain-legal/regulatory-compliance/legal_regulatory_change_impact_assessment.md`), and case-law jurisdiction splits (`domain-legal/research/legal_jurisdiction_split_analysis.md`).

## Companion domains

- `domain-decision-making/documentation/` — the general-purpose decision-record formats this domain's memo specializes.
- `domain-reasoning-craft/` — systems and epistemic prompts for the deliberation upstream of the memo.
- `domain-legal/` — when the question is legal analysis of a policy instrument rather than choice among policy options.
- `domain-business-strategy/` — corporate strategy analysis where public policy is one input rather than the subject.
