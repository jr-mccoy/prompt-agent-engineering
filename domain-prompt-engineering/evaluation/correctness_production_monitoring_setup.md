---
title: "Production Monitoring for Output Correctness Drift"
category: prompt-engineering/evaluation
description: "Design monitoring that catches correctness drift in a live AI system — signals grounded in the user's actual telemetry, alert thresholds that separate drift from noise, sampling strategies that keep costs tractable, and a response playbook that names who acts on what. Distinct from a pre-ship eval: monitoring runs continuously against production traffic that the eval never saw."
techniques:
  - ST-01
  - ST-02
  - RT-09
  - CM-02
  - DS-01
  - OC-06
  - QA-01
difficulty: advanced
tags:
  - correctness
  - monitoring
  - drift
  - production
  - observability
  - prompt-engineering
updated: "2026-04-21"
related_prompts:
  - domain-prompt-engineering/evaluation/correctness_discovery_prompt.md
  - domain-prompt-engineering/evaluation/correctness_eval_design_prompt.md
  - domain-prompt-engineering/evaluation/correctness_pre_mortem.md
  - domain-prompt-engineering/evaluation/correctness_prompt_specification_audit.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_auto_improving_trace_infrastructure_audit.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_auto_improving_triplet_diagnostic.md
---

# Production Monitoring for Output Correctness Drift

**Objective:** Design a monitoring setup for a deployed AI system that catches correctness drift before the business catches it. The artifact names the signals to log, the sampling strategy, the alert thresholds that separate drift from noise, the response playbook, and the review cadence. Every signal is grounded in telemetry the user already has or can realistically add. Drift metrics the user cannot actually measure in their stack are excluded.

**When to use:**
- An AI feature is shipped and running against live traffic.
- The pre-ship eval confirmed current correctness, but the user knows the eval doesn't see tomorrow's inputs, next week's model version, or next month's consumer shift.
- A prior incident demonstrated that the team learned about a failure from a stakeholder rather than from their own monitoring.

**Audience:** Prompt engineers, ML engineers, and developers shipping AI-powered features who operate a live AI system and need monitoring distinct from their pre-ship eval. Not for pre-production; use `correctness_eval_design_prompt.md` and `correctness_pre_mortem.md` before this.

---

## Inputs Required

1. **The deployed system.** The prompt, model version, tool / context configuration, and deployment shape (synchronous / batch / streaming).
2. **The correctness spec.** Live version used by the pre-ship eval.
3. **The pre-ship eval's recent results.** Baseline primary metric, guardrail, and category breakdowns. The monitoring is tuned against these.
4. **The actual telemetry available.** What the user logs today — inputs, outputs, user feedback, downstream actions, latency, cost, model / prompt version. What can be added within a reasonable effort budget.
5. **Traffic shape.** Volume per day, rough distribution across the eval's case categories if known.
6. **Who is on call.** Who receives alerts, at what hours, with what authority to pause, roll back, or route to human.
7. **Known drift patterns from adjacent or prior tasks.** Silent consumer-behavior shifts, model-provider behavior changes, upstream data shifts. One paragraph.

**Refuse the design if:**
- No pre-ship eval results exist. Monitoring without a baseline reports noise as drift.
- No telemetry exists and the user cannot add any. Monitoring is not a substitute for observability. Route to an observability design step first.
- The user wants monitoring purely for optics. Monitoring is a cost center unless it is wired to action. If there is no responder, refuse.

---

## Instructions

### Step 1 — Separate drift from noise conceptually

Name what "drift" means for this system, specifically:

- **Input drift.** The distribution of inputs is changing (new case types, shifting ratios, vocabulary change).
- **Model drift.** The model's behavior changed (new provider version, retrieval-store change, context change).
- **Output drift.** The output distribution is changing (length, format, refusal rate, confidence markers) independent of inputs or model.
- **Consumer drift.** The downstream consumer's tolerance or use has shifted — outputs that used to satisfy no longer do.
- **Spec drift.** The definition of correct has quietly changed but the spec document hasn't.

These are different problems with different signals. Monitoring must distinguish them or it will misattribute incidents.

### Step 2 — Select signals per drift type, scoped to actual telemetry

For each drift type, name 1–3 signals the user can actually measure. Each signal:

- Is derivable from existing telemetry or an addition the user has committed to making.
- Is computable at the cadence monitoring needs (hourly / daily / weekly).
- Has a reference value from the pre-ship eval or early production.

Typical signals:

- **Input drift:** input-length distribution, vocabulary novelty rate, case-category classifier output (if one exists), incoming request-type mix.
- **Model drift:** model / prompt version log, provider-announced version changes, retrieval-store freshness / diff.
- **Output drift:** output-length distribution, refusal rate, structured-output schema-compliance rate, confidence-marker rate, latency distribution.
- **Consumer drift:** user-feedback rate (thumbs-up / escalate / override), downstream action rate, reformulation rate (same user retries with a different prompt within N minutes).
- **Spec drift:** rate of graders marking cases "rubric unclear," spec-revision log, open tickets naming correctness ambiguity.

Drop any signal the user cannot measure. Wishes are not controls.

### Step 3 — Set sampling strategy

Grading every output is unaffordable at production scale. Sampling options:

- **Stratified random sample.** A fixed share of outputs per category per period, human-scored against the rubric.
- **Triggered sample.** Outputs matching high-risk input patterns are always sampled; low-risk inputs are sampled at lower rate.
- **Feedback-triggered sample.** Every user-flagged output is reviewed; adjacent outputs (same session, same input type) are also pulled for context.
- **Auto-graded sample.** A programmatic check applied to the full population (schema compliance, length bounds, refusal rate). Cheap; only catches what's mechanically testable.

Most monitoring combines all four. Name the target sample size per cadence, the cost, and who does the grading.

### Step 4 — Set alert thresholds

For each signal, define:

- **Reference value.** From pre-ship eval or early production.
- **Noise band.** Normal day-to-day variation. Measured, not assumed. Typical: the standard deviation of the signal over a rolling 2-week window.
- **Investigate threshold.** Signal moves outside the noise band for ≥ N consecutive periods. Opens a ticket, does not page.
- **Act threshold.** Signal moves > M × noise band, or investigate-threshold has been open for ≥ T periods without resolution. Pages on-call.
- **Circuit-breaker threshold.** If it exists — signal level at which the system auto-pauses or auto-downgrades (e.g., refuses new traffic until a human clears it).

Thresholds set below the measured noise band produce alert fatigue. Thresholds set well above it produce silent incidents. Measure, don't guess.

### Step 5 — Write the response playbook

For each alert-capable signal, one paragraph specifying:

- **First check.** The ≤5-minute action the on-call takes to classify drift vs. noise (is the model version the same? is the input mix the same? is it a specific consumer complaining?).
- **Triage routes.** Where to hand off once drift type is identified (input-drift → data team, model-drift → model owner, output-drift → prompt owner, consumer-drift → product owner, spec-drift → spec owner).
- **Stabilization options.** Pause traffic / roll back prompt version / roll back model / narrow inputs / route to human — matched to drift types.
- **Incident log location.** Where the event is recorded for the post-drift review.

A response playbook without named hand-off owners stalls at 2 AM. Name roles.

### Step 6 — Define the review cadence

- **Real-time.** Alerts.
- **Weekly.** Scan dashboards for signals that are moving but haven't crossed thresholds; surface slow drift.
- **Monthly.** Rerun a subset of the pre-ship eval against recent production inputs to detect silent regression not captured by signals.
- **Quarterly.** Full eval rerun + spec review + monitoring review. Retire stale signals, add new ones for newly-observed drift types.

Monitoring without a review cadence decays; signals tuned for last quarter's traffic fire on noise in next quarter's.

### Step 7 — Build the drift-vs-noise adjudication rule

For each investigate-threshold trip, the on-call needs a rule to avoid chasing noise:

- Is the trip sustained across ≥ N consecutive periods? If no → noise.
- Is it localized to a specific input category, consumer, or time window? If yes → scoped incident, not system-wide drift.
- Does a rerun of a small eval slice on recent production inputs reproduce the trip? If no → signal artifact.
- Does the trip correlate with a known upstream change (provider version, context change, traffic composition)? If yes → that's the cause, not emergent drift.

Adjudication rules protect against two failure modes: chasing every noise trip and missing real drift by dismissing the first alert.

### Step 8 — Write the monitoring dossier

Final artifact: a dossier the on-call team can use at 2 AM. Signals table, thresholds, sampling plan, playbook, review cadence, adjudication rule, ownership. Short enough to read, specific enough to act.

---

## Constraints

### Must
- Ground every signal in telemetry the user actually has or has committed to adding.
- Measure noise bands from data; do not assume.
- Name a responder and triage route for every alert-capable signal.
- Include a spec-drift signal, not just input/output/model signals.
- Review and revise thresholds at the monthly or quarterly cadence.

### Must Not
- Invent metrics the user's stack cannot compute.
- Alert on signals with no responder.
- Treat aggregate output metrics as a substitute for category-level monitoring — the same failures that hid in the eval hide here.
- Confuse a dashboard with monitoring. Dashboards display; monitoring alerts and routes.
- Conflate drift types. An input-drift alert that triggers a prompt rewrite is misdiagnosis.
- Set thresholds below the measured noise band.

---

## False-Positive Prevention

1. **Imagined telemetry.** Signals the user cannot measure in their actual stack are decorative. Every signal must pass a "can the user compute this today or in the next two weeks" test.
2. **Noise-band guessing.** Thresholds set without measuring actual variance produce either alert fatigue or silence. Measure variance first, set thresholds second.
3. **Drift-type confusion.** Investigating output drift when the real cause is input drift leads to prompt edits that don't help and sometimes regress the system. The drift-type taxonomy exists to prevent this; enforce it in the playbook.
4. **Alerts without responders.** Alerts routed to "the team" go unanswered. Name roles. If no role exists, don't alert on that signal.
5. **Aggregate-only monitoring.** Per-category monitoring is mandatory; aggregates hide category regressions the same way they did in the eval.
6. **Stale thresholds.** Thresholds set once and never revisited drift out of alignment with production. Quarterly threshold review is non-negotiable.
7. **Over-instrumentation.** Tens of signals all firing intermittently produces monitoring that nobody reads. Prefer 5–10 well-tuned signals over 30 half-tuned ones.
8. **Chasing every trip.** An investigate-threshold trip is an invitation to look, not a confirmed incident. Adjudication rules protect on-call from chasing noise.
9. **Dashboard theater.** A dashboard nobody watches is not monitoring. If the user's review cadence doesn't include looking at the dashboard, remove it or wire it to alerts.
10. **Monitoring without spec drift.** Input / model / output drift all assume the spec is stable. It often isn't. A spec-drift signal (rubric-unclear flags, open ambiguity tickets) is easy to skip and the most damaging to miss.

---

## Output Format

```markdown
## System under monitoring
[Deployed prompt / model / configuration / shape.]

## Spec version
[Reference + date.]

## Baseline (from pre-ship eval + early production)
- Primary metric: [...]
- Category breakdowns: [...]
- Guardrail: [...]
- Measured noise bands by signal: [...]

## Telemetry inventory
- Available today: [...]
- Committed additions: [...]
- Refused additions (out of scope): [...]

## Signals table
| Signal | Drift type | Source telemetry | Reference value | Noise band | Investigate | Act | Circuit-breaker (if any) |
|---|---|---|---|---|---|---|---|
| 1 | [...] | input / model / output / consumer / spec | [...] | [value] | [rule] | [rule] | [rule] | [rule] |
| ... |

## Sampling strategy
- Stratified random: [share per category per period]
- Triggered: [input patterns that force sample]
- Feedback-triggered: [rule]
- Auto-graded: [programmatic checks applied to full population]
- Total human-grading budget: [per week / per month]

## Response playbook
| Signal | First check (≤5 min) | Triage route | Stabilization options | Incident log location |
|---|---|---|---|---|
| 1 | [...] | [role] | [...] | [...] |
| ... |

## Review cadence
- Real-time: alerts
- Weekly: [...]
- Monthly: [eval slice rerun, signal review]
- Quarterly: [full review, threshold reset, signal retirement / addition]

## Adjudication rule
- Sustained across ≥ [N] periods
- Localized vs. system-wide
- Reproduces on small-eval rerun
- Correlates with known upstream change

## Ownership
- Monitoring owner: [role]
- On-call schedule: [reference]
- Authority: [pause / rollback / route-to-human]

## Dossier date
[Timestamp + version.]
```

---

## Verification

- [ ] Every signal is computable from available or committed telemetry.
- [ ] Noise bands were measured, not assumed.
- [ ] Investigate and act thresholds are set above the measured noise band.
- [ ] Every alert-capable signal has a named responder and triage route.
- [ ] Spec-drift signal is included, not just input/output/model.
- [ ] Sampling strategy combines random + triggered + feedback + auto-graded.
- [ ] Adjudication rule is documented.
- [ ] Review cadence is set and includes threshold reset.
- [ ] Monitoring is wired to action, not just display.
- [ ] The dossier is short enough for on-call to read at 2 AM.
