---
title: "Bug Bounty Program Selection & ROI"
category: bug-bounty/strategy
description: "Rank candidate bug bounty programs by expected return on your limited time using payout ranges, triage responsiveness, scope size, competition, and skill fit"
techniques:
  - ST-01
  - RT-02
  - DS-06
  - QA-02
  - DD-07
difficulty: intermediate
tags:
  - bug-bounty
  - strategy
  - roi
  - program-selection
  - prioritization
updated: "2026-06-18"
related_prompts:
  - domain-software-engineering/bug-bounty/bugbounty_program_scope_analyzer.md
  - domain-software-engineering/bug-bounty/bugbounty_getting_started_orientation.md
  - domain-software-engineering/bug-bounty/bugbounty_report_postmortem.md
---

# Bug Bounty Program Selection & ROI

**Objective:** Decide where to spend your limited hunting hours by scoring candidate programs on the factors that actually drive expected value: payout, responsiveness, scope, competition, and fit.

## When to Use
- You have a few hours a week and too many programs to choose from.
- A program you've been on feels low-yield and you want to compare alternatives objectively.
- You want to avoid the beginner trap of grinding crowded, slow, or stingy programs.

## Inputs / Context
- **Candidate programs** (2–10): names, platform, and any public stats you can see (bounty ranges, average response/resolution time, number of resolved reports, scope breadth, launch date).
- **Your profile:** strongest vuln classes, time budget, and whether you need income soon vs. learning.
- **Constraints:** private-only access, regions, or asset types you can/can't test.

## Instructions

1. **Authorization note.** Only evaluate programs the user can legitimately join (public, or private invites they hold). Do not advise circumventing invite-only access.

2. **Score each program on weighted factors** (default weights; let the user adjust):
   - **Payout potential** (bounty ranges, especially for the user's strong classes).
   - **Responsiveness** (mean time to triage/bounty; slow programs cost you in held findings and duplicates).
   - **Scope size & freshness** (wide scope and recently expanded/launched scope = more unfound bugs).
   - **Competition** (resolved-report count, "thanks" volume, program age — crowded mature programs have fewer easy bugs).
   - **Skill fit** (does the program's tech/asset type match the user's strengths?).
   - **Signal quality** (does the program reward thoroughly, or down-tier and reject?).

3. **Compute a comparable score** per program (e.g., weighted 1–5 per factor) and rank them, but treat the score as a guide, not gospel — note where a single factor dominates.

4. **Sanity-check the ranking against reality:** a high theoretical payout with 18-month triage times or saturated scope may be worse than a modest, fast, fresh program. Surface these traps explicitly.

5. **Recommend a portfolio, not a single bet:** typically one "primary" program (best fit, run deeply) plus one "fresh/expansion" program to catch newly-added scope.

6. **CRITICAL — verify the recommendation is grounded:**
   - Confirm each score cites the input it's based on (don't invent stats you weren't given).
   - Mark any factor scored on assumption as **"ESTIMATE"** and say what data would confirm it.
   - Confirm the recommendation matches the user's stated goal (income-soon vs. learning) and time budget.

## False-Positive Prevention (MUST follow)
- ❌ Do NOT fabricate bounty figures, response times, or report counts — use only provided/known data.
- ❌ Do NOT rank purely on max bounty; a high ceiling with slow triage or saturated scope is often worse.
- ❌ Do NOT recommend a program whose tech stack is a poor fit for the user's skills just because it pays well.
- ❌ Do NOT advise gaming access to private programs.
- ✅ DO label assumed values as ESTIMATE and name the data that would confirm them.
- ✅ DO weight responsiveness and scope freshness, not just payout.
- ✅ DO tie the final pick to the user's stated goal and hours.

## Output Format
```
## Scoring Weights (adjust as needed)
[Factor: weight]

## Program Scorecard
| Program | Payout | Responsiveness | Scope/Freshness | Competition | Fit | Signal | Weighted score |

## Traps & Caveats
- [Program]: [why the raw score may mislead] (ESTIMATE where applicable)

## Recommended Portfolio
- Primary: [program] — why
- Secondary/fresh-scope: [program] — why
- Skip/deprioritize: [program] — why

## What data would sharpen this
- ...
```

## Example Output
```
## Scoring Weights
Payout 0.25 · Responsiveness 0.2 · Scope/Freshness 0.2 · Competition 0.15 · Fit 0.15 · Signal 0.05

## Program Scorecard
| Program | Payout | Resp. | Scope/Fresh | Comp. | Fit | Signal | Score |
|---------|--------|-------|-------------|-------|-----|--------|-------|
| Acme (web/API) | 4 | 4 | 5 (just added *.api) | 3 | 5 | 4 | 4.2 |
| MegaBank | 5 | 2 (ESTIMATE: slow) | 2 (mature) | 2 | 3 | 3 | 2.9 |
| FreshStartup | 3 | 5 | 5 (launched 3wk ago) | 5 | 4 | 3 | 4.1 |

## Traps & Caveats
- MegaBank: top bounty ceiling, but maturity + (estimated) slow triage means scarce easy bugs and long
  cash-conversion. Confirm triage time from the program's public metrics before committing.
- FreshStartup: low competition and fresh scope are great for a beginner, but lower ceilings.

## Recommended Portfolio
- Primary: Acme — best fit for your web/API + IDOR strength, fast triage, freshly expanded API scope.
- Secondary/fresh-scope: FreshStartup — low competition, ideal for building confidence and first bounties.
- Deprioritize: MegaBank until you have a track record and can absorb slow triage.

## What data would sharpen this
Pull each program's published mean-time-to-triage and resolved-report count; confirm MegaBank's response
time (currently an estimate).
```

## Techniques Used
- **ST-01 (Clear Objective Statement)** — frames the task as expected-value ranking under time scarcity.
- **RT-02 (Multi-Dimensional Analysis)** — scores programs across six weighted factors, not just payout.
- **DS-06 (Prioritization Guidance)** — produces a ranked portfolio with explicit primary/secondary picks.
- **QA-02 (Adversarial Thinking)** — the traps step attacks misleading raw scores.
- **DD-07 (Self-Audit Table)** — verification flags fabricated data and ties the pick to stated goals.
