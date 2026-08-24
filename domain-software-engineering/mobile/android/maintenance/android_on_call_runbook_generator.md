---
title: "Android On-Call Runbook Generator"
category: mobile-development
description: "Generates per-failure-mode on-call runbooks for an Android app — detection signals, first-response steps, decision trees, and escalation paths — so any responder can act consistently during an incident."
techniques:
  - ST-01
  - ST-02
  - DS-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - android
  - maintenance
  - on-call
  - incident-response
  - runbook
updated: "2026-06-06"
related_prompts:
  - domain-software-engineering/mobile/android/maintenance/android_incident_triage_and_severity_classification.md
  - domain-software-engineering/mobile/android/maintenance/android_postmortem_and_corrective_action_planning.md
  - domain-software-engineering/mobile/android/maintenance/android_observability_logging_quality_review.md
  - domain-software-engineering/mobile/android/maintenance/android_reliability_slo_error_budget_review.md
---

# Android On-Call Runbook Generator

**Objective:** Produce ready-to-use on-call runbooks for an Android app's most likely failure modes — each with detection signals, an immediate-response checklist, a diagnose-and-mitigate decision tree, rollback/forward-fix criteria, and an escalation path — so that any responder (not just the original author) can act consistently under pressure.

**When to Use:** Use when standing up an on-call rotation, after a postmortem identifies missing runbooks, before a high-risk release, or to convert tribal knowledge into written response procedures. This closes the incident loop: triage → respond (runbook) → postmortem → corrective actions.

**Prompt Type:** Comprehensive (300-400 lines)

---

## Context Gathering

1. **App & stack:**
   - "What does the app do, and what are its critical user journeys (login, purchase, sync, core feature)?"
   - "What backend/services does it depend on (Firebase, custom API, payment, push)?"
   - "What architecture is in play (offline-first, WorkManager sync, Compose, etc.)?"

2. **Incident history & signals:**
   - "What have the last 3–5 incidents been? What failure modes recur?"
   - "What detection exists today — Crashlytics, Android Vitals, dashboards, alerts, support tickets?"
   - "What are the existing SLOs/thresholds (crash-free, ANR-free, sync success)?"

3. **Response context:**
   - "Who is on the rotation, and what authority do they have (can they roll back a release, toggle a flag)?"
   - "What release/rollback levers exist — staged rollout halt, Play release rollback, Remote Config kill switch?"
   - "What are the communication channels (status page, in-app, support, stakeholders)?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before publishing any runbook, you MUST:**

1. **Anchor each runbook to a real, detectable signal** — if there is no way to detect the failure mode, flag the detection gap instead of writing a runbook that can't be triggered.
2. **Make every step executable by a non-author** — no "ask Priya"; every step names a tool, query, dashboard, or command.
3. **Give explicit decision criteria** — rollback vs. forward-fix must have testable thresholds, not judgment calls.
4. **Define escalation by condition, not by panic** — name the trigger condition, who is paged, and the time bound.
5. **Tie each runbook to a kill-switch or mitigation if one exists** — and flag where none exists as a resilience gap.

### False-Positive Prevention

- ❌ Do NOT write runbooks for failure modes with no detection signal — list them as gaps for `android_observability_logging_quality_review.md`
- ❌ Do NOT include steps a responder lacks the access/authority to perform
- ❌ Do NOT leave "mitigate the issue" as a step — specify the lever (flag, rollback, config)
- ❌ Do NOT invent thresholds — derive them from the app's SLOs or ask
- ✅ DO separate immediate mitigation from root-cause diagnosis
- ✅ DO include a "first 5 minutes" checklist for every runbook
- ✅ DO mark any runbook that depends on a not-yet-built capability

---

### Phase 1: Failure-Mode Inventory

Enumerate the failure modes worth a runbook, ranked by likelihood × impact.

| Failure Mode | Likelihood | Impact | Detection Signal Exists? | Runbook Priority |
|--------------|-----------|--------|--------------------------|------------------|
| Crash spike (new release) | [H/M/L] | [H/M/L] | [Vitals / Crashlytics] | [P0–P3] |
| ANR spike | [H/M/L] | [H/M/L] | [Vitals ANR rate] | [P0–P3] |
| Auth/login outage | [H/M/L] | [H/M/L] | [error rate / tickets] | [P0–P3] |
| Sync failure / data loss | [H/M/L] | [H/M/L] | [sync success metric] | [P0–P3] |
| Backend/API degradation | [H/M/L] | [H/M/L] | [latency/error dashboards] | [P0–P3] |
| Payment/billing failure | [H/M/L] | [H/M/L] | [purchase success rate] | [P0–P3] |
| Push delivery failure | [H/M/L] | [H/M/L] | [FCM delivery metrics] | [P0–P3] |
| Bad config / flag rollout | [H/M/L] | [H/M/L] | [Remote Config + Vitals] | [P0–P3] |

**Output:** ranked list + an explicit "no detection signal" gap list.

---

### Phase 2: Runbook Template (generate one per high-priority mode)

Generate each runbook in this exact structure:

```markdown
## Runbook: [Failure Mode]

**Owner team:** [team] · **Last reviewed:** [date] · **Related SLO:** [metric + target]

### Detection
- **Primary signal:** [metric/alert + where to view it]
- **Threshold that means "incident":** [explicit value]
- **Confirming signals:** [secondary metrics, support volume]

### First 5 Minutes (Stabilize)
1. [ ] Acknowledge alert; open [dashboard link]
2. [ ] Confirm blast radius: [query/metric → % users, versions, regions]
3. [ ] Check recent changes: [last release, flag flips, server config] in last [N]h
4. [ ] Apply fastest safe mitigation if criteria met (see decision tree)

### Diagnose
| Observation | Likely Cause | Next Check |
|-------------|--------------|------------|
| [signal pattern] | [cause] | [specific check] |

### Mitigate — Decision Tree
- IF [condition: e.g. spike isolated to latest release ≥ X% crash-free drop]
  → **Halt staged rollout / roll back release** via [exact lever]
- ELSE IF [condition: e.g. traced to a flag/config change]
  → **Disable flag / revert Remote Config** key `[name]` via [console path]
- ELSE IF [condition: backend dependency]
  → **Engage [backend team]**; enable [degraded-mode flag] if present
- ELSE → continue diagnosis; escalate at time bound below

### Escalation
| Condition | Escalate To | Within |
|-----------|-------------|--------|
| [blast radius doubles / data loss confirmed / mitigation fails ×N] | [role/team] | [minutes] |

### Communication
- Internal: [channel] — template: "[short status template]"
- External: [status page / in-app] — when: [criteria]

### Exit / All-Clear
- [ ] Signal back under threshold for [duration]
- [ ] Mitigation documented; follow-up ticket filed
- [ ] Handoff note for postmortem (link triage + this runbook)
```

---

### Phase 3: Cross-Cutting Assets

Generate alongside the per-mode runbooks:

**A. Lever inventory** — every mitigation lever and who can pull it:

| Lever | What It Does | Who Can Use | Time to Effect |
|-------|--------------|-------------|----------------|
| Halt staged rollout | Stops promotion to more users | [role] | minutes |
| Play release rollback | Reverts to prior version (note: install caveats) | [role] | hours |
| Remote Config kill switch | Disables feature without release | [role] | minutes |
| Server feature flag | Backend-side disable | [role] | minutes |

**B. On-call quick reference** (one screen): top dashboards, alert routes, severity rubric pointer, escalation contacts.

**C. Detection-gap list:** failure modes without a runbook because no signal exists → route to observability review.

---

### Phase 4: Validation

**CHECKPOINT 1:** Before finalizing, validate each runbook.

- [ ] Every step is executable by someone other than the author
- [ ] Every mitigation names a concrete lever the responder can access
- [ ] Every decision branch has a testable condition
- [ ] Every escalation has a trigger condition + contact + time bound
- [ ] Runbooks with no detection signal are flagged, not faked
- [ ] (Recommended) Dry-run one runbook as a game-day exercise

---

## Expected Output

1. **Ranked failure-mode inventory** (likelihood × impact, with detection-gap flags)
2. **One runbook per high-priority failure mode** (using the Phase 2 template)
3. **Lever inventory** (mitigations + authority + time-to-effect)
4. **On-call quick-reference card**
5. **Detection-gap list** routed to observability work
6. **Validation checklist results** (and game-day recommendation)

---

## Techniques Used

- **ST-01** (Clear Objective): Generate actionable per-mode runbooks
- **ST-02** (Sequential Instructions): Inventory → template → cross-cutting → validate
- **DS-02** (Structured Decision Support): Mitigation decision trees with explicit conditions
- **CM-02** (Constraint Specification): Steps bounded by responder access/authority
- **QA-01** (Verification/Self-Check): Non-author executability + game-day validation

---

## Related Prompts

- [android_incident_triage_and_severity_classification.md](android_incident_triage_and_severity_classification.md) - Triage that precedes runbook execution
- [android_postmortem_and_corrective_action_planning.md](android_postmortem_and_corrective_action_planning.md) - Postmortem that often creates new runbooks
- [android_observability_logging_quality_review.md](android_observability_logging_quality_review.md) - Closes detection gaps surfaced here
- [android_reliability_slo_error_budget_review.md](android_reliability_slo_error_budget_review.md) - Source of the thresholds runbooks reference
- [../publishing/android_release_governance_runbook.md](../publishing/android_release_governance_runbook.md) - Release-level rollback/rollout levers
