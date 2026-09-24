---
title: "Process Map and Waste Scan — SIPOC, Value-Stream Timeline, Eight Wastes, and Lead Time vs. Touch Time"
category: operations/process-improvement
description: "Map an existing process as it actually runs — a SIPOC to fix the boundaries, then a value-stream timeline with touch time and queue time per step — scan it for the eight lean wastes with evidence, and separate lead time from touch time so the improvement targets the waiting rather than the work."
techniques:
  - DS-01
  - DS-02
  - RT-05
  - OC-03
  - QA-01
difficulty: intermediate
tags:
  - process-mapping
  - value-stream
  - sipoc
  - lean
  - eight-wastes
  - lead-time
updated: "2026-09-24"
related_prompts:
  - domain-operations/process-improvement/ops_root_cause_a3_report.md
  - domain-operations/process-improvement/ops_capacity_and_bottleneck_model.md
  - domain-professional-writing/business-writing/business_writing_sop.md
---

# Process Map and Waste Scan

**Objective:** Produce an as-is map of one process — boundaries, steps, owners,
touch time and queue time per step — and a waste scan that ties each of the eight
wastes to an observed step, so the team can see where the lead time actually goes
before anyone proposes a fix.

**When to Use:**
- A process "takes too long" and nobody can say which part.
- Hand-offs between teams are where things disappear, and each team believes its own
  step is fast.
- You are about to redesign or automate a process and want the as-is baseline first.
- You need the current-condition section of an A3 or the Measure phase of a DMAIC
  project.
- **Not this prompt if** you need to *write the procedure* people will follow — that is
  `domain-professional-writing/business-writing/business_writing_sop.md`. This prompt
  designs and diagnoses the process; the SOP documents the result. If the process is
  software delivery (build, deploy, review), use `domain-engineering-workflows/`.

## Inputs / Context

1. **The process in one line**, with a start trigger and an end state
   ("customer requests a return" → "refund posted").
2. **Steps as performed**, with the owner of each. Walked or observed beats recalled.
3. **Touch time per step** (hands-on work) and **queue time before each step**
   (waiting), with the source: timestamps, a time study, or estimate.
4. **Volume**: units per day/week, and the mix if it varies.
5. **Known pain**: rework loops, escalations, complaints, overtime.
6. **Time basis**: calendar hours or working hours. You must choose one.

If touch and queue times are unknown, the output is a map with `[measure]` markers
and a data-collection plan — not invented numbers.

## Method

1. **Fix the boundaries with a SIPOC (DS-01).** Suppliers, Inputs, Process (5–7
   high-level steps only), Outputs, Customers. The start trigger and end state must be
   observable events. A map without agreed boundaries will be argued about forever.
2. **Build the value-stream timeline (DS-02).** For each step: owner, touch time,
   queue time *before* it, first-pass yield (% that proceed without rework), and batch
   size if work is batched. Tag each number `measured`, `sampled (n=)`, or `estimated`.
3. **Compute the three time metrics, with definitions stated.**
   - **Lead time** = time from start trigger to end state for one unit (sum of queue +
     touch along the path).
   - **Touch time** = sum of hands-on work.
   - **Process cycle efficiency (PCE)** = touch time ÷ lead time, on the declared basis.
   - **Cycle time** is used inconsistently across organizations (per-step interval
     between completions vs. end-to-end). State which meaning you use, or avoid the term.
   Separate **internally controllable** waits from **external** ones (customer transit,
   regulator review) — only the first are yours to remove.
4. **Scan for the eight wastes, step by step (RT-05).** Defects, Overproduction,
   Waiting, Non-utilized talent, Transportation, Inventory, Motion, Extra-processing.
   Each finding names the step, the evidence, and the size (time, count, or cost). A
   waste with no evidence is a hypothesis and is labelled as one.
5. **Rank by lead-time share.** The largest controllable queue is usually the
   first target, not the slowest touch step.
6. **Propose countermeasures as experiments, not conclusions.** For each top waste:
   the change, the modeled effect on lead time (labelled *modeled*), and how it will
   be measured after.
7. **Verify (QA-01).** Re-sum the timeline; check that PCE uses the same time basis
   top and bottom; confirm every waste links to a step.

## Output Format

```
# Process map — [process name]
Start trigger: [...]   End state: [...]   Time basis: [calendar | working]

## SIPOC
| Suppliers | Inputs | Process (5–7 steps) | Outputs | Customers |

## Value-stream timeline
| # | Step | Owner | Queue before | Touch | FPY | Batch | Source |
Lead time: [..]  Touch time: [..]  PCE: [..%]
Controllable wait: [..]  External wait: [..]

## Waste scan
| Waste | Step | Evidence | Size | Confidence |

## Top countermeasures (experiments)
| Change | Targets | Modeled effect (modeled) | How we'll measure |

## Data gaps
- [what is estimated, and how to measure it]
```

## Verification

- [ ] Start trigger and end state are observable events.
- [ ] Every time value carries a source tag.
- [ ] Lead time equals the sum of queue + touch on the critical path.
- [ ] PCE numerator and denominator use the same basis.
- [ ] External waits are separated from controllable ones.
- [ ] Every waste finding names a step and evidence; unevidenced ones say "hypothesis".
- [ ] Modeled improvements are labelled modeled, not measured.

## False-Positive Prevention

1. **Mapping the process as designed.** The documented flow is not the flow. Map
   what happened to the last 20 units, including the workarounds.
2. **Blaming the slowest touch step.** Touch time is usually a small fraction of
   lead time; a 12-minute inspection is not the problem when the item waited two days
   before it.
3. **Mixing calendar and working time.** A PCE computed with working-hour touch over
   calendar-hour lead time is off by a factor of three or more.
4. **Counting external waits as waste you can remove.** Customer transit time is real
   but not yours; list it separately.
5. **Labelling every approval "extra-processing".** Some approvals are controls
   (segregation of duties, safety sign-off). Check what the approval prevents before
   proposing to remove it; regulated or safety-critical controls go to the qualified
   owner.
6. **Averages hiding batches.** A weekly batch produces a wait of up to five working
   days, averaging about half the batch interval; report the batch, not just the mean.
7. **Precision theatre.** Three estimated inputs do not produce a lead time to the
   minute. Round to the resolution of the worst input.

## Example Output

```
# Process map — Customer returns (RMA) to refund
Start: customer submits return request   End: refund posted   Basis: calendar days

## SIPOC
| Customer, carrier | Return form, item, original order | Log → Approve → Customer ships →
  Receive & match → Inspect → Refund | Refund, restocked item | Customer, finance |

## Value-stream timeline  (source: 60 RMAs sampled from Q3 timestamps)
| # | Step            | Owner      | Queue before       | Touch  | FPY  | Batch  |
| 1 | Log request     | CS         | 1.5 d (inbox)      | 6 min  | 98%  | —      |
| 2 | Approve RMA     | Supervisor | 1.0 d              | 3 min  | 100% | —      |
| 3 | Customer ships  | Customer   | 4.0 d (EXTERNAL)   | —      | —    | —      |
| 4 | Receive & match | Dock       | 2.0 d (pallet)     | 8 min  | 87%  | pallet |
| 5 | Inspect & grade | QC         | 0.5 d              | 12 min | 97%  | —      |
| 6 | Issue refund    | Finance    | 2.5 d (weekly run) | 4 min  | 99%  | weekly |
Lead time: 11.5 d   Touch: 33 min   PCE: 33 / 16,560 min = 0.2%
Controllable wait: 7.5 d   External wait: 4.0 d

## Waste scan
| Waste            | Step | Evidence                                          | Size        | Conf. |
| Waiting          | 6    | refunds run Fridays only                          | 2.5 d avg   | High  |
| Waiting          | 4    | returns pallet opened when full                   | 2.0 d       | High  |
| Defects          | 4    | 13% lack RMA # on label → manual lookup  | 8 of 60     | Med   |
| Extra-processing | 2    | supervisor approved 100% of 60 sampled            | 1.0 d queue | Med — check what the approval screens for |
| Inventory        | 4    | avg 40 unopened returns on dock                   | [measure $] | Low   |

## Top countermeasures (experiments)
| Change                               | Targets | Modeled effect        | Measure              |
| Daily refund run                     | 6       | −2.0 d (2.5 → 0.5)    | request→refund, 4 wk |
| Auto-approve returns under $75       | 2       | −1.0 d on ~80% of RMAs| same                 |
| Pre-printed RMA label in return email| 4       | FPY 87% → [measure]   | lookups per week     |
Modeled lead time if the first two land: ~8.7 d (modeled, not measured).

## Data gaps
- FPY at step 4 from 60 units only; extend to a full month.
- Dock inventory value not captured.
```

## Techniques Used

- **DS-01 Framework Application** — SIPOC and the eight-waste lens applied to one process.
- **DS-02 Metric Specification** — lead time, touch time, PCE, FPY with stated definitions.
- **RT-05 Evidence-Based Reasoning** — every waste tied to an observed step and source.
- **OC-03 Markdown Table Specification** — timeline and waste scan as comparable tables.
- **QA-01 Self-Verification** — re-summing the timeline and checking the time basis.

## Related Prompts

- `ops_root_cause_a3_report.md` — when one waste needs a proper root-cause A3.
- `ops_capacity_and_bottleneck_model.md` — when the queue is a capacity problem.
- `domain-professional-writing/business-writing/business_writing_sop.md` — writing up the redesigned process.
- `domain-risk/risk_fmea_analysis.md` — failure modes of the process, rather than its waste.
