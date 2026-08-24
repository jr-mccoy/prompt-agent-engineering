# Domain: Risk

Risk management as a working discipline: identify risks, structure them, prioritize them, harden against them, and learn when one materializes anyway. The seven prompts here adapt the standard instruments — register, heat map, FMEA, threat model, dependency audit, tail-risk scan, after-action review — for general operators, not just safety engineers, and each enforces the discipline that makes its instrument worth more than a spreadsheet: registers get named owners and review cadences, heat maps force the "are we actually doing the top-3 mitigations?" question, AARs run a blameless root-cause ladder instead of finding a culprit.

The domain spans the full lifecycle. Before the fact: build the catalogue (`risk_register_builder`), hunt what the catalogue systematically misses (`risk_tail_risk_scan`), model intelligent adversaries (`risk_threat_model_non_technical`), decompose a process's failure modes (`risk_fmea_analysis`), and find the single points of failure (`risk_dependency_chain_audit`). During: visualize and re-rank (`risk_heat_map`). After: learn without scapegoating (`risk_after_action_review`).

Users are PMs, operators, founders, executives, engineers, and analysts who own delivery or continuity — anyone for whom "we knew about that risk but nobody owned it" is an unacceptable post-mortem line.

## When to use this domain

- Standing up risk governance for a project, launch, or operation — or reviving a stale risk list with no owners and no review rhythm.
- You need to know which dependency, vendor, person, or contract would hurt most if it vanished tomorrow.
- A multi-step process needs systematic failure analysis (with severity, occurrence, and detectability rated) before it goes live or scales.
- A high-visibility move is being planned as if no one will push back, and intelligent opposition is realistic.
- Before a hard-to-reverse commitment, you want to pressure-test for the low-probability, high-impact risks the register doesn't capture.
- A risk event, incident, or near-miss has happened and the instinct to assign blame needs redirecting into systemic learning.

## When NOT to use this domain (use a different one)

- **Software/system security review** → `domain-software-engineering/analysis/security/` (real STRIDE-style threat modeling); `risk_threat_model_non_technical.md` is explicitly the non-software adaptation.
- **Stress-testing one specific plan's failure path forward** → `domain-decision-making/scenario_strategic_pre_mortem.md` or `domain-prompt-engineering/evaluation/correctness_pre_mortem.md`.
- **Scenario planning under strategic uncertainty** → `domain-decision-making/` scenario prompts (`scenario_two_by_two_matrix.md`, `scenario_wild_card_injection.md`, `scenario_signposts_and_triggers.md`).
- **Drawing the structural dependency wiring (topology, cycles, fan-in/out) rather than ranking what to harden** → `domain-reasoning-craft/systems/systems_dependency_map.md`.
- **Reviewing a completed decision (not a risk event) for decision-vs-outcome quality** → `domain-decision-making/documentation/decisiondoc_after_action_report.md`.

## Prompts in this domain

| File | Purpose |
|------|---------|
| `risk_register_builder.md` | Build a maintainable register: per-risk scores, named owner, mitigation, monitoring, escalation trigger, residual risk, review cadence |
| `risk_heat_map.md` | Plot scored risks on a 5×5 likelihood × impact map, force-rank, and force the "are we doing the top-3 mitigations?" question |
| `risk_tail_risk_scan.md` | Provocation-driven hunt for 5–8 low-probability, high-impact risks the register misses, with a "would we even know?" detection check |
| `risk_fmea_analysis.md` | Per-step failure modes with severity × occurrence × detectability (RPN), adapted for software, org processes, supply chains, events |
| `risk_dependency_chain_audit.md` | Trace dependency chains, find single points of failure, prioritize by blast radius × replacement difficulty, prescribe resilience moves |
| `risk_threat_model_non_technical.md` | Security threat-modeling discipline (assets, actors, attack paths, mitigations) for launches, statements, partnerships, reveals |
| `risk_after_action_review.md` | US Army AAR frame on a materialized risk event: supposed/actual/gap/why, blameless root-cause ladder, keep/start/stop by level |

## Quick routing

| You're saying | Use |
|---------------|-----|
| "We have no risk catalogue / our risk list is stale and ownerless" | `risk_register_builder.md` |
| "Which risks should get attention this cycle?" / "show the board our risk posture" | `risk_heat_map.md` |
| "What are we not seeing?" / "what would be catastrophic even if unlikely?" | `risk_tail_risk_scan.md` |
| "Where can this process fail, and would we catch it?" | `risk_fmea_analysis.md` |
| "What happens if this vendor / person / contract disappears?" | `risk_dependency_chain_audit.md` |
| "Who would push back on this launch / statement / deal, and how?" | `risk_threat_model_non_technical.md` |
| "It happened — what do we learn without a blame hunt?" | `risk_after_action_review.md` |

## How prompts in this domain compose

The backbone chain is **register → heat map → review cadence**: `risk_register_builder` produces the scored catalogue, `risk_heat_map` visualizes and re-ranks it each cycle, and when a register risk triggers anyway, `risk_after_action_review` closes the loop and feeds revisions back into the register. `risk_tail_risk_scan` is the register's adversary — run it after the register exists to find what the register's frame excluded, then log the survivors. The two decomposition tools slot in by subject shape: `risk_fmea_analysis` when the subject has discrete steps or components, `risk_dependency_chain_audit` when the question is concentration and single points of failure (often downstream of `systems_dependency_map.md`, which draws the wiring this prompt ranks). `risk_threat_model_non_technical` is the special case for moves with an intelligent adversary; its outputs also feed the register as adversarial risk entries.

## Frontmatter conventions specific to this domain

All prompts carry a machine-readable `reasoning:` block (styles, stakes, horizon, uncertainty, output_format, user_role, mode). The `uncertainty` field is diagnostic for routing within the domain: `risk` for the quantifiable instruments (register, heat map, FMEA), `ambiguity` for the AAR and threat model, and `radical` for the tail-risk scan — which is also the only prompt here with `stakes: high`, `horizon: years`, and `evidence_quality: sparse` baked in, reflecting its black-swan territory. Output formats cluster on `matrix_ranked_list` and `structured`; `mode` distinguishes the forward-looking prompts (`audit`, `forecast`, `plan`) from the backward-looking AAR (`diagnose`, `document`).

## Companion domains

- `domain-decision-making/` — scenario prompts (`scenario_strategic_pre_mortem.md`, `scenario_wild_card_injection.md`, `scenario_two_by_two_matrix.md`) for plan-shaped and strategy-shaped uncertainty, plus `tradeoff_reversibility_stakes_grid.md` for deciding whether a decision warrants this domain's overhead at all.
- `domain-reasoning-craft/systems/` — `systems_dependency_map.md` (structural companion to the dependency audit) and `systems_unintended_consequence_scan.md` (second-order effects that become register entries).
- `domain-prompt-engineering/evaluation/` — `correctness_pre_mortem.md`, the forward-looking counterpart to the after-action review.
- `domain-reasoning-craft/forecasting/` — base rates and calibration for the likelihood scores the register and heat map depend on.
- `domain-software-engineering/analysis/security/` — actual technical security review when the threat surface is software.
