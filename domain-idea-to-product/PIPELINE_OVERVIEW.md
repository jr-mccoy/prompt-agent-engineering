# Pipeline Overview

Visual flow, stage-by-stage inputs/outputs, branching logic, and terminal artifacts for the idea-to-product pipeline.

---

## Flow

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ STAGE 1: IDEATION                                                            │
│   In: raw hunch                                                              │
│   Out: stress-tested idea (GO/KILL/RESHAPE)                                  │
└──────────┬───────────────────────────────────────────────────────────────────┘
           │ GO
           ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ STAGE 2: PROBLEM VALIDATION                                                  │
│   In: hypothesis + segment                                                   │
│   Out: 5-10 rubric-scored interviews → STRONG/RESHAPE/KILL                   │
└──────────┬───────────────────────────────────────────────────────────────────┘
           │ STRONG (≥6/N high-scoring, clustered)
           ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ STAGE 3: MARKET RESEARCH                  ◄── often parallel with stage 5    │
│   In: validated problem + segment                                            │
│   Out: TAM/SAM/SOM + unit economics (GREEN/YELLOW/RED)                       │
└──────────┬───────────────────────────────────────────────────────────────────┘
           │ GREEN or YELLOW (with plan)
           ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ STAGE 4: BUSINESS MODEL                                                      │
│   In: market signals + unit economics                                        │
│   Out: business model canvas + pricing/monetization                          │
└──────────┬───────────────────────────────────────────────────────────────────┘
           ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ STAGE 5: STRATEGY & POSITIONING                                              │
│   In: model + market + segment                                               │
│   Out: SWOT + positioning + 90-day GTM plan                                  │
└──────────┬───────────────────────────────────────────────────────────────────┘
           ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ STAGE 6: DECISION VALIDATION ◄─── HARD GATE before stage 7                   │
│   In: everything above                                                       │
│   Out: pre-mortem + blind-spot scan + am-i-being-nuts pass                   │
└──────────┬───────────────────────────────────────────────────────────────────┘
           │ pass
           ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ STAGE 7: PRD AUTHORING                                                       │
│   In: validated everything                                                   │
│   Out: PRD (passes quality gate) + epic/feature tree with MVP/V1/V2 cuts     │
└──────────┬───────────────────────────────────────────────────────────────────┘
           ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ STAGE 8: ARCHITECTURE DESIGN                                                 │
│   In: PRD + epic/feature tree                                                │
│   Out: deep-design doc + stack decisions (ADR per component) + canon decl    │
└──────────┬───────────────────────────────────────────────────────────────────┘
           ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ STAGE 9: PHASED BUILD PLAN                                                   │
│   In: PRD + features + stack                                                 │
│   Out: phased plan with checkpoints + sprint-level breakdown                 │
└──────────┬───────────────────────────────────────────────────────────────────┘
           ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ STAGE 11: BUILD-RISK PRE-MORTEM ◄─── HARD GATE before stage 10               │
│   In: full plan                                                              │
│   Out: failure-mode pre-mortem with verification attached to each            │
└──────────┬───────────────────────────────────────────────────────────────────┘
           │ pass
           ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ STAGE 10: AI-AGENT HANDOFF                                                   │
│   In: everything                                                             │
│   Out: day-1 agent bundle (CLAUDE.md + tasks + acceptance specs + memory)    │
└──────────────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
                       BUILD WITH AI CODING AGENT
```

---

## Stage-by-stage inputs / outputs

| # | Stage | Required inputs | Primary outputs | Verdict gates |
|---|-------|-----------------|-----------------|---------------|
| 1 | Ideation | Idea one-liner, founder context | Stress-tested idea | GO / KILL / RESHAPE |
| 2 | Problem Validation | Hypothesis + segment | 5-10 interviews + cohort synthesis | STRONG / RESHAPE / KILL |
| 3 | Market Research | Validated problem | TAM/SAM/SOM + unit econ | GREEN / YELLOW / RED |
| 4 | Business Model | Market signals + econ | Canvas + pricing model | (informational) |
| 5 | Strategy & Positioning | Model + market | SWOT, positioning, GTM 90-day plan | (informational) |
| 6 | Decision Validation | Everything above | Pre-mortem + blind-spot + am-i-nuts | pass / fail (must pass) |
| 7 | PRD Authoring | Stages 1-6 passed | PRD + epic/feature tree | PRD quality score ≥ threshold |
| 8 | Architecture Design | PRD + feature tree | Deep design + stack ADRs + canon decl | (informational) |
| 9 | Phased Build Plan | PRD + features + stack | Phased plan + sprint breakdown | (informational) |
| 11 | Build-Risk Pre-Mortem | Full plan | Failure modes + verification | pass / fail (must pass) |
| 10 | AI-Agent Handoff | All above + stack canon | Day-1 bundle | bundle complete = ready |

---

## Branching logic

- **Stage 1 KILL** → either abandon the idea, or return after fundamental founder/market changes.
- **Stage 1 RESHAPE** → re-run stage 1 with reshaped idea statement.
- **Stage 2 KILL** → return to stage 1 with reshaped hypothesis OR different segment.
- **Stage 2 RESHAPE** → re-run stage 2 with refined hypothesis.
- **Stage 3 RED** → either return to stage 4 with different monetization, or return to stage 1.
- **Stage 3 YELLOW** → continue but flag binding constraint; must show plan to improve at stage 5 GTM design.
- **Stage 6 fail** → fix specific blind spots / pre-mortem failures, then re-run stage 6.
- **Stage 7 PRD quality fail** → re-author with the rubric items that failed.
- **Stage 11 fail** → return to whichever upstream stage owns the failure mode (e.g., risk is unbuildable → stage 8; risk is unsellable → stage 5).

---

## Recommended cadence

Solo founder, part-time:
- Stage 1: 1-3 days
- Stage 2: 2-4 weeks (interview scheduling is the rate-limit)
- Stage 3: 1 week (parallel with stage 4 OK after week 1)
- Stage 4: 1 week
- Stage 5: 1-2 weeks
- Stage 6: 2-3 days
- Stage 7: 1-2 weeks
- Stage 8: 1 week
- Stage 9: 2-3 days
- Stage 11: 1-2 days
- Stage 10: 2-3 days

**Total to agent kickoff: 8-14 weeks part-time, 4-8 weeks full-time.**

Funded team:
- Stages 1-6 in parallel tracks: 2-4 weeks
- Stages 7-11: 1-2 weeks
- Stage 10: 1 week

**Total to agent kickoff: 4-7 weeks.**

---

## Terminal artifacts (the deliverable bundle)

After the full pipeline, you have these artifacts to hand to the AI coding agent:

```
/project-root
├── CLAUDE.md                          # canonical rules (from stage 8 + stage 10)
├── README.md                          # user-facing overview
├── docs/
│   ├── prd.md                         # stage 7
│   ├── architecture/
│   │   ├── deep-design.md             # stage 8 deepthink_design output
│   │   ├── stack-decisions.md         # stage 8 tech-stack selector output
│   │   └── adr/                       # one file per ADR
│   ├── feature-tree.md                # stage 7 decomposer output
│   └── build-plan/
│       ├── 00-overview.md             # stage 9 phased plan
│       ├── 01-task-order.md           # stage 10 bridge output
│       └── tasks/
│           ├── T-001.md               # stage 10 acceptance-test-writer output
│           ├── T-002.md
│           └── ...
├── .project-memory/
│   ├── 00-state.md                    # initialized by stage 10
│   ├── decisions-log.md
│   └── open-questions.md
└── docs/business/
    ├── prd-business-context.md        # stages 1-3 summary
    ├── gtm-plan.md                    # stage 5 GTM output
    ├── unit-economics.md              # stage 3 econ designer output
    └── decision-log.md                # stage 6 pre-mortem + blind-spot scan
```

---

## When to return to earlier stages mid-build

The pipeline is not strictly one-way. Return to earlier stages when:

- **Mid-build customer signal contradicts the MVP hypothesis** → return to stage 2 or 1.
- **Mid-build scope creep** → return to stage 7 decomposer to re-cut MVP/V1/V2.
- **Mid-build technical wall** → return to stage 8 (stack reconsideration) or stage 11 (revise failure modes).
- **Mid-build burn rate alarm** → return to stage 3 (unit economics) or stage 5 (GTM channel mix).
- **Agent walls / drift** → use `domain-software-engineering/vibe-coding-rescue/` (general) or its `android/` subpath for Android-specific rescue.

The orchestrator can route you back to earlier stages — just paste the new signal and ask it to re-classify.
