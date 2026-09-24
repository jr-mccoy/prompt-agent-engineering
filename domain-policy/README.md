# Domain: Policy

Public-policy analysis and communication. Policy work has constraints that general business analysis doesn't: options must be evaluated on equity and distributional effects, political viability, and reversibility alongside cost and effectiveness; the evidence is usually contested; and recommendations rest on values tradeoffs that honest analysis names rather than hides. The prompts in this domain enforce that discipline.

The four prompts follow the analysis in order: frame the problem, map the stakeholders, test feasibility, then communicate the options in a form a principal who wasn't in the working sessions can decide from. Users are policy analysts, executives, consultants, advocates, government-affairs teams, and civic-minded individuals organizing their own thinking on a policy debate.

## When to use this domain

- A principal (government body, foundation, NGO leadership, board, coalition partner) must choose among policy responses to a defined problem.
- An internal recommendation on which public-policy posture to advocate.
- Think-tank or academic comparison of policy options for an external audience.
- Organizing your own position on a live policy debate with auditable rigor.

## When NOT to use this domain (use a different one)

- **The "policy" is internal operations, not public policy** → `domain-decision-making/documentation/decisiondoc_options_memo.md`.
- **The recommendation is binary (do / don't)** → a simpler decision memo from `domain-decision-making/documentation/`.
- **Persuasion is the goal rather than auditable analysis** → `domain-product-management/` or `domain-professional-writing/`.
- **Regulatory risk monitoring for a business** → `domain-decision-making/decisioning_regulatory_risk_radar.md`.

## Prompts in this domain

| File | Purpose |
|------|---------|
| `policy_problem_framing.md` | Frame the problem before anyone proposes solutions: who is affected and by how much, the measured current state, the no-action trajectory, and the contested framings |
| `policy_stakeholder_coalition_map.md` | Map stakeholders on position, intensity, influence, interests, coalition and movability, then derive the coalition structures that decide outcomes |
| `policy_implementation_feasibility.md` | Test a proposal's implementation feasibility in depth: legal authority, administrative capacity, funding, a realistic timeline benchmarked against comparable efforts, and dependencies |
| `policy_options_memo.md` | Compare 3–5 policy options on effectiveness, feasibility, fiscal cost, equity, political viability, reversibility, and unintended consequences; recommend with the values tradeoffs named |

## How prompts in this domain compose

Run them in order: problem framing → stakeholder/coalition map → implementation feasibility → options memo. The options memo sits at the end of the chain, not the start. Deliberation happens upstream (research, modeling, stakeholder input — e.g., `domain-reasoning-craft/systems/systems_unintended_consequence_scan.md` for second-order effects, `domain-reasoning-craft/epistemic/epistemic_disagreement_diagnosis.md` for contested evidence), and the memo communicates it. Its internal-operations sibling is `decisiondoc_options_memo.md` in `domain-decision-making/documentation/`.

## Frontmatter conventions specific to this domain

Prompts carry the machine-readable `reasoning:` block. The options memo's profile is characteristic of the domain: `stakes: high`, `horizon: years`, `uncertainty: deep`, `domain_complexity: regulated`, with `normative` in the styles list — policy analysis is explicitly values-laden, and the prompts require the values tradeoffs to be stated rather than smuggled.

## Planned expansion

This domain holds four prompts. Known gaps, tracked for coverage Wave 4 in [`meta/COVERAGE_ROADMAP.md`](../meta/COVERAGE_ROADMAP.md): cost-benefit / regulatory impact analysis, program evaluation design, public comment letters on proposed rules, legislative bill analysis, and cross-jurisdiction comparison. Related work exists elsewhere: logic models (`domain-education-teaching/program/evaluation-analytics/`), testimony prep and op-eds (`domain-science/public-engagement/`).

## Companion domains

- `domain-decision-making/documentation/` — the general-purpose decision-record formats this domain's memo specializes.
- `domain-reasoning-craft/` — systems and epistemic prompts for the deliberation upstream of the memo.
- `domain-legal/` — when the question is legal analysis of a policy instrument rather than choice among policy options.
- `domain-business-strategy/` — corporate strategy analysis where public policy is one input rather than the subject.
