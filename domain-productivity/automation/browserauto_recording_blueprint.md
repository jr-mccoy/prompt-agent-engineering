---
title: "Design a Recording Blueprint for a Scheduled Browser Workflow"
category: productivity/automation
description: "Design the blueprint before recording: inputs, flow, branches, error modes, dry-run plan, and success criteria — so the recorded automation is robust enough to schedule, not just fragile enough to demo."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - RT-02
  - QA-01
  - ST-03
difficulty: intermediate
tags:
  - browser-automation
  - recording
  - blueprint
  - scheduled-workflow
  - robustness
updated: "2026-04-20"
related_prompts:
  - domain-productivity/automation/browserauto_weekly_audit.md
  - domain-productivity/automation/browserauto_safety_check.md
  - domain-productivity/automation/browserauto_multi_tab_intel.md
---

# Design a Recording Blueprint for a Scheduled Browser Workflow

**Objective:** Produce the design document before opening a recorder. The blueprint specifies the workflow's inputs, step sequence, branches, error modes, dry-run plan, schedule, and success criteria — so when recording happens, it captures a robust automation ready to schedule, rather than a brittle happy-path demo that breaks on the third run.

**When to use:** After the weekly audit (`browserauto_weekly_audit.md`) has picked an automation candidate worth building. Before opening a browser-recording tool (Playwright codegen, Selenium IDE, vendor RPA recorders, UI.Vision, Claude browser tool). Any time an automation will run scheduled (daily, weekly, event-triggered) rather than ad-hoc.

**Audience:** Individual contributor or automation engineer building scheduled browser workflows. The blueprint is the artifact that goes into the recorder session; the recording itself is derivative.

---

## Inputs Required

1. **The task being automated.** Verb-first description + outcome (e.g., "Pull yesterday's report from X and email the summary to [team]").
2. **How often it will run and under what trigger.** Daily at 7am / weekly Monday / event-triggered / manual-on-demand with scheduling.
3. **The site(s) involved.** URLs, authentication method, any known rate limits.
4. **Inputs the automation will take.** Fixed parameters vs dynamic inputs (date, filter, account, etc.).
5. **What "success" looks like per run.** Observable, not "it worked."
6. **Consequences if it runs wrong.** Low (produces an ignorable artifact) / Medium (misdirects work) / High (customer-facing / financial / compliance). This drives how rigorous the blueprint must be.
7. **Rollback / manual fallback.** How the user will continue if the automation fails for a week.

Refuse to produce a blueprint for a High-consequence automation without a specified rollback. The blueprint is also a go/no-go check.

---

## Instructions

### Step 1 — State the contract

One paragraph at the top:
- What goes in (inputs).
- What comes out (outputs — the artifact, message, or state change the automation produces).
- Under what trigger.
- What must never happen (the automation must not, e.g., send external email, write to production DB, delete).

This is the contract the recording must honor. If the recording drifts from this, the recording is wrong.

### Step 2 — Map the happy-path flow

Numbered steps, pre-recording:
1. Open URL.
2. Authenticate (how — SSO, API token, cookie, stored credentials).
3. Navigate to the function.
4. Apply filters / enter inputs.
5. Extract or act.
6. Persist result (save, download, post, message).
7. Clean up (close tabs, log run metadata).

For each step, note:
- **Selector strategy.** What the automation will key on — ID, stable class, data-attribute, text, ARIA. Avoid xpath based on DOM position; it breaks.
- **Wait condition.** What tells the automation the page is ready — a specific element, a network-idle, a timeout (last resort).
- **Idempotency.** What happens if this step is retried. Most steps should be safe to retry; action steps (click Submit) must not.

### Step 3 — Enumerate branches

Real workflows branch. List the branches the recording must handle:
- **Login required / already authenticated.**
- **Result present / result empty.**
- **Popup / modal intercepts the flow.**
- **Rate-limit page or error banner.**
- **Multi-page pagination.**
- **Timeouts.**

For each branch, specify the detection (how the automation notices which branch) and the handling (continue / retry / stop-and-alert / skip).

A recording that only handles the happy path will fail on any deviation. Most scheduled-automation failures are here.

### Step 4 — Specify error handling

Three categories:
- **Retryable errors.** Network blips, transient 5xx, timeouts on a load. Bounded retry (e.g., 3 attempts, exponential backoff).
- **Non-retryable errors.** Auth failure, page structure changed, required field missing, rate-limit hit. Stop, alert, preserve state for debugging.
- **Poisoned-run errors.** The automation has taken part of an action and cannot safely continue (e.g., clicked Submit but the next page didn't load). Stop, alert, do not retry — manual review.

Name the alert destination (email, Slack webhook, nothing) and what information the alert carries.

### Step 5 — Dry-run and validation plan

Before scheduling:
- **Dry-run mode.** The recording runs to completion but short of the final write/send action. Output: the artifact the automation would have produced.
- **Validation criteria.** The dry-run is compared to a human-run baseline: same output? If not, investigate before scheduling.
- **Dry-run cadence.** For High-consequence automations: at least 5 successful dry-runs before first live run. Medium: 2–3. Low: 1.

### Step 6 — Schedule and observability

Once validated:
- **Schedule.** Precise: day, time, timezone. Default to quiet hours unless the workflow must be live.
- **Monitoring.** Where runs are logged. What fields are captured per run: timestamp, input parameters, outcome, duration, artifact produced.
- **Failure notification path.** Who, how fast, what information.
- **Review cadence.** Weekly check on whether the automation still runs cleanly — sites change, and scheduled automations rot silently.

### Step 7 — Success criteria

Observable, per run:
- Output artifact present and matches format expectation.
- Duration within expected range (variance is often the first sign of drift).
- No error alerts fired.
- If the automation produces a downstream action, the action was received by the downstream consumer.

### Step 8 — Retirement signal

What would make the automation retirable?
- The underlying task changes shape (adjust or retire).
- Site change that costs more to re-record than the monthly savings.
- The downstream consumer stops needing the output.

Pre-committing to retirement criteria prevents the zombie-automation problem.

---

## Constraints

### Must
- State the contract first. Recording follows contract.
- Use stable selectors (data-attributes, ARIA, text) over DOM-position.
- Specify wait conditions per step, not global timeouts.
- Enumerate at least 4 branches.
- Separate retryable, non-retryable, and poisoned-run errors.
- Define a dry-run plan before scheduling.
- Set retirement criteria.

### Must Not
- Open the recorder before the blueprint is drafted.
- Use xpath based on DOM position for any critical step.
- Record credentials in plain text inside the recording. Use vaulted credentials or SSO.
- Schedule a High-consequence automation without 5+ successful dry-runs.
- Omit observability. A scheduled automation with no logs is a bug in waiting.
- Skip retirement criteria.

---

## False-Positive Prevention

1. **Don't trust the first successful recording.** A recording that works once on the happy path will fail on the second run when data looks different. Branches are the test.
2. **Don't use DOM-position selectors.** They are the single largest cause of recorded-automation rot. Prefer text, ARIA, data-attributes.
3. **Don't treat dry-run as optional.** For any automation that writes, sends, or triggers, dry-run is the only way to verify the contract without risking a production action.
4. **Don't alert on every flake.** Transient retries are fine; alert on non-retryable failures and on degrading-success-rate trends.
5. **Don't schedule without retirement criteria.** The automation will outlive the need it was built for.
6. **If the contract forbids an action,** bake that into an assertion in the recording (e.g., "if URL contains /checkout, stop"). Defense in depth.

---

## Output Format

```
# Recording blueprint — [task name]

## Contract
- In: [inputs]
- Out: [outputs]
- Trigger: [schedule / event]
- Must never: [explicit prohibitions]

## Happy-path flow
| # | Step | Selector strategy | Wait condition | Idempotent? |
|---|------|-------------------|----------------|-------------|

## Branches
| Branch | Detection | Handling (continue/retry/stop-alert/skip) |
|--------|-----------|--------------------------------------------|

## Error handling
- Retryable: [which, retry budget, backoff]
- Non-retryable: [which, alert destination, state preserved]
- Poisoned-run: [which, stop-do-not-retry, manual review path]

## Dry-run plan
- Mode: [what is short-circuited]
- Baseline comparison: [how validated]
- Cadence before live: [N successful dry-runs]

## Schedule and observability
- Schedule: [day, time, timezone]
- Run log: [where, fields]
- Failure notify: [who, how, what info]
- Review cadence: [interval]

## Success criteria (per run)
- [Observable check]
- [Observable check]

## Retirement criteria
- [Condition that means retire or rebuild]
```

---

## Verification

- [ ] Contract is stated at the top with explicit "must never."
- [ ] Every step has a selector strategy, wait condition, and idempotency note.
- [ ] At least 4 branches are enumerated with handling.
- [ ] Error handling distinguishes retryable, non-retryable, and poisoned-run.
- [ ] Dry-run cadence matches consequence level.
- [ ] Schedule, logs, and failure path are specified.
- [ ] Retirement criteria are set.
