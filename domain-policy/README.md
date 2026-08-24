# Domain: Policy

Public-policy analysis and communication. Policy work has constraints that general business analysis doesn't: options must be evaluated on equity and distributional effects, political viability, and reversibility alongside cost and effectiveness; the evidence is usually contested; and recommendations rest on values tradeoffs that honest analysis names rather than hides. The prompts in this domain enforce that discipline.

The current prompt is a documentation instrument — it communicates analysis already done, in a form a principal who wasn't in the working sessions can decide from. Users are policy analysts, executives, consultants, advocates, government-affairs teams, and civic-minded individuals organizing their own thinking on a policy debate.

## When to use this domain

- A principal (government body, foundation, NGO leadership, board, coalition partner) must choose among policy responses to a defined problem.
- An internal recommendation on which public-policy posture to advocate.
- Think-tank or academic comparison of policy options for an external audience.
- Organizing your own position on a live policy debate with auditable rigor.

## When NOT to use this domain (use a different one)

- **The "policy" is internal operations, not public policy** → `domain-decision-making/documentation/decisiondoc_options_memo.md`.
- **The recommendation is binary (do / don't)** → a simpler decision memo from `domain-decision-making/documentation/`.
- **Persuasion is the goal rather than auditable analysis** → `domain-professional-communication/` or `domain-professional-writing/`.
- **Regulatory risk monitoring for a business** → `domain-decision-making/decisioning_regulatory_risk_radar.md`.

## Prompts in this domain

| File | Purpose |
|------|---------|
| `policy_options_memo.md` | Compare 3–5 policy options on effectiveness, feasibility, fiscal cost, equity, political viability, reversibility, and unintended consequences; recommend with the values tradeoffs named |

## How prompts in this domain compose

The options memo sits at the end of an analysis chain, not the start: deliberation happens upstream (research, modeling, stakeholder input — e.g., `domain-reasoning-craft/systems/systems_unintended_consequence_scan.md` for second-order effects, `domain-reasoning-craft/epistemic/epistemic_disagreement_diagnosis.md` for contested evidence), and the memo communicates it. Its internal-operations sibling is `decisiondoc_options_memo.md` in `domain-decision-making/documentation/`.

## Frontmatter conventions specific to this domain

Prompts carry the machine-readable `reasoning:` block. The current prompt's profile is characteristic of the domain: `stakes: high`, `horizon: years`, `uncertainty: deep`, `domain_complexity: regulated`, with `normative` in the styles list — policy analysis is explicitly values-laden, and the prompts require the values tradeoffs to be stated rather than smuggled.

## Planned expansion

This domain currently holds one prompt; further policy prompts are planned (additional analysis and communication formats in the same auditable-rigor convention).

## Companion domains

- `domain-decision-making/documentation/` — the general-purpose decision-record formats this domain's memo specializes.
- `domain-reasoning-craft/` — systems and epistemic prompts for the deliberation upstream of the memo.
- `domain-legal/` — when the question is legal analysis of a policy instrument rather than choice among policy options.
- `domain-business-strategy/` — corporate strategy analysis where public policy is one input rather than the subject.
