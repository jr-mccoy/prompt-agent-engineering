---
title: "Science Policy Brief Drafter"
category: science/public-engagement
description: "Draft a two-page, options-not-advocacy policy brief for a non-scientist policymaker, separating empirical evidence and its limits from value judgments, with an advocacy-creep check."
techniques:
  - ST-01
  - ST-03
  - RT-03
  - QA-01
  - QA-02
  - CM-02
difficulty: advanced
tags:
  - policy-brief
  - honest-broker
  - options-not-advocacy
  - science-communication
  - evidence-limits
  - uncertainty-disclosure
  - values-vs-evidence
  - plain-language
updated: "2026-06-26"
related_prompts:
  - domain-science/public-engagement/science_op_ed_drafter.md
  - domain-science/writing-communication/science_lay_summary_translator.md
  - domain-science/statistics/science_statistical_results_interpreter.md
---

# Science Policy Brief Drafter

**Objective:** Draft a two-page brief that gives a non-scientist policymaker what the evidence does and does not show, then presents policy options with tradeoffs rather than a recommendation. The brief takes an honest-broker stance: it expands the policymaker's choice set, separates empirical claims from value judgments, and runs an "advocacy creep" check to confirm it informs rather than advocates.

**When to use:** When a decision-maker needs an accessible synthesis of the evidence on an issue and would be better served by clearly laid-out options and uncertainties than by being told what to do.

**Required inputs:**
- **Discipline.** The scientific field(s) underpinning the issue.
- **Study type.** Observational / experimental / RCT / meta-analysis / modeling / synthesis, etc., for the evidence cited.
- **The finding(s)** (user-supplied; never invented) and the audience (e.g., legislator, agency official, staffer) and their decision context.
- **The policy problem or question** the brief must inform.

**Optional inputs:**
- The realistic option space (including status quo / do-nothing).
- Known limitations, effect sizes, and the strength/quality of the evidence base.
- Stakeholders, budget/feasibility constraints, and time horizon.
- Areas of genuine scientific disagreement.

**Constraints — Must:**
- Present options, not advocacy: lay out viable choices (including the status quo) with tradeoffs, not a single recommendation.
- State what the evidence shows AND its certainty/limits for each relevant claim.
- Separate empirical claims from value judgments explicitly throughout.
- Name what is still unknown or contested.
- Keep it to roughly two pages and in plain language without false confidence.
- Calibrate to the evidence: correlation is not causation; a single study is not settled; report effect size with a limitation.

**Constraints — Must Not:**
- Do not invent findings, statistics, quotes, citations, or certainty. Draft only from user-supplied results; mark gaps `[user-supplied]`.
- Do not advocate for a particular option or rank them as "best"; the policymaker's values decide.
- Do not use hype: "novel," "groundbreaking," "first-ever," "gold standard," "cure," "breakthrough," "proves." Substitute calibrated claims.
- Do not present contested or modeled results as established fact, or hide uncertainty to make the brief tidier.

**Instructions:**

1. **Intake and classify.** Capture discipline, study type(s), the finding, audience/decision context, and the policy problem. Note evidence quality and causal warrant.
2. **Frame the problem.** State the policy problem in one short, neutral paragraph a non-scientist can act on, without prejudging the answer.
3. **Summarize the evidence with its limits.** For each relevant claim, give the plain-language finding, the study type, the certainty level, and the principal limitation. Distinguish settled from contested.
4. **Separate evidence from values.** Mark which statements are empirical and which require a value judgment the policymaker must make.
5. **Lay out the options.** Present the realistic options including the status quo, each with tradeoffs (benefits, costs, risks, feasibility, who is affected), without ranking.
6. **State what is unknown.** Name the open questions, contested points, and what new evidence would resolve them.
7. **Run the advocacy-creep check.** Scan for language that nudges toward one option, smuggles a value judgment as a finding, or asserts more certainty than the evidence supports.
8. **Deliver.** Output the two-page brief structure followed by the advocacy-creep check.

**Output format (locked):**

```
## Policy Brief (≈2 pages)

### Title
[neutral, issue-focused]

### Bottom line for the policymaker
[2–3 sentences: the problem and what the evidence can and cannot settle — no recommendation.]

### The problem
[short, neutral framing.]

### What the evidence shows — and its limits
| Claim (plain language) | Study type | Certainty | Key limitation |
|---|---|---|---|
| [...] | [...] | [strong / moderate / preliminary / contested] | [...] |

### Empirical vs value judgment
- Empirical (what the science says): [...]
- Value judgment (what the policymaker must decide): [...]

### Policy options (not ranked)
| Option | Benefits | Costs / risks | Feasibility | Who is affected |
|---|---|---|---|---|
| Status quo / do nothing | [...] | [...] | [...] | [...] |
| Option A | [...] | [...] | [...] | [...] |
| Option B | [...] | [...] | [...] | [...] |

### What is still unknown
- [open question; what evidence would resolve it]

### Sources
- [user-supplied links to primary evidence]

## Advocacy-Creep Check
| Passage | Risk flagged | Neutral rewrite |
|---|---|---|
| [...] | [nudge toward one option / value-as-fact / overstated certainty] | [...] |

Check verdict: [PASS / REVISE — reasons]
```

**Reporting-standard alignment:** No formal reporting standard; aligns to science-communication best practice and the honest-broker model (Pielke) — options-not-advocacy framing, separating empirical claims from value judgments, "what this does and does NOT show" disclosure, plain language without false confidence, and overclaim avoidance.

**Verification checklist (before delivering):**
- [ ] The brief presents options (including status quo) without recommending or ranking one.
- [ ] Each evidence claim states study type, certainty, and a key limitation.
- [ ] Empirical statements are explicitly separated from value judgments.
- [ ] Open questions and contested points are named.
- [ ] Length is roughly two pages and language is plain without false confidence.
- [ ] No banned hype words appear in the drafted brief.
- [ ] No invented findings, statistics, or citations; gaps marked `[user-supplied]`.
- [ ] The advocacy-creep check table is completed with a PASS/REVISE verdict.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Advocacy creep | A "balanced" brief whose framing favors one option | Advocacy-creep check scans for directional language |
| Value-as-fact | A policy preference stated as an evidence finding | Mandatory empirical-vs-value separation section |
| False tidiness | Uncertainty omitted to make options look clean | Require certainty + limitation per claim and an "unknown" section |
| Missing baseline | Options listed without the status quo for comparison | Status quo / do-nothing row required in the options table |
| Modeled-as-real | Projections presented as observed outcomes | Tag study type per claim; flag modeled results explicitly |
