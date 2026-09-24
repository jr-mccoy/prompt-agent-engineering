# Domain: Decision Making

**Purpose:** Prompts for structured decision analysis, tradeoff evaluation, blind spot identification, and decision frameworks.

---

## What This Domain Covers

Decision support for complex choices. The files are organised by **filename
prefix**, not by subfolder. `documentation/` is the only subfolder.

> **Correction (2026-09-24).** Earlier versions described `tradeoffs/`,
> `blind-spots/` and `frameworks/` subfolders with "TBD" counts. Those folders
> never existed. The prefix families below are the real structure.

| Family | Count | What it covers |
|---|---|---|
| `decisioning_*.md` | 25 | Tradeoff analysis, blind-spot mirror, first-principles decomposition, prioritization framework selector, regret minimization, sunk-cost audit, time-boxed decision protocol, stakeholder alignment, multi-constraint and resource-constrained solvers, escalation decision tree, and crisis severity triage, playbook and drills |
| `scenario_*.md` | 7 | Backcasting, 2×2 scenario matrix, multi-horizon roadmap, robustness test, signposts and triggers, wild-card injection, strategic pre-mortem |
| `tradeoff_*.md` | 4 | Multi-criteria decision analysis, Pugh matrix, real-options framing, reversibility × stakes grid |
| `judgement_assessment_prompt.md` | 1 | Assess the quality of a judgement call |
| [`documentation/`](documentation/) | 6 | `decisiondoc_*`: after-action report, decision log entry, Bezos-style narrative memo, one-pager, options memo, post-decision review |

Several files sit here for historical reasons and are candidates to move to their
subject homes:
- the three crisis-communication files → `domain-risk/`;
- `decisioning_competitive_intelligence_scanner.md` →
  `domain-business-strategy/`;
- `decisioning_pricing_experiment_matrix.md` → product and pricing.

These moves are tracked for coverage Wave 4 in
[`meta/COVERAGE_ROADMAP.md`](../meta/COVERAGE_ROADMAP.md).

---

## Directory Structure

```
domain-decision-making/
├── decisioning_*.md          # 25 decision-support prompts
├── scenario_*.md             # 7 scenario-planning prompts
├── tradeoff_*.md             # 4 structured tradeoff methods
├── judgement_assessment_prompt.md
├── documentation/            # 6 decision-record prompts (decisiondoc_*)
└── README.md
```

---

## Key Patterns

### Tradeoff Analysis
- **Rapid Tradeoff Analyzer** - Quick multi-factor analysis
- **Weighted Decision Matrix** - Scored comparison
- **Reversibility Assessment** - One-way vs two-way doors

### Blind Spot Detection
- **Devil's Advocate** - Challenge your assumptions
- **Pre-mortem** - Imagine failure and work backwards
- **Stakeholder Perspective** - See from other viewpoints

### Decision Frameworks
- **MECE Breakdown** - Mutually exclusive, collectively exhaustive
- **Second-Order Effects** - Downstream consequences
- **Regret Minimization** - Long-term perspective

---

## When to Use This Domain

Use these prompts when you need to:
- Make a complex decision with multiple factors
- Identify blind spots in your thinking
- Evaluate tradeoffs systematically
- Apply structured decision frameworks

**Do NOT use for:**
- Validation of already-made decisions (use domain-productivity/validation)
- Business analysis (use domain-business-strategy)
- Engineering decisions (use domain-engineering-workflows)

---

*Migrated from: `prompts/non-engineering/decisioning_*.md`*
