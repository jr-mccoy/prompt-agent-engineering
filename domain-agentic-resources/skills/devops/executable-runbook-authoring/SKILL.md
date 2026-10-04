---
name: executable-runbook-authoring
description: Writes and maintains runbooks that an unfamiliar on-call engineer can execute under stress. Each step is a contract (precondition, exact command, expected output, verification, stop condition, rollback), linked from the alert that needs it, tested by a dry run or drill, and kept fresh with an owner and review date. Use when asked to "write a runbook for this alert", "make our runbooks usable", "test our runbooks", or "turn tribal knowledge into a runbook".
metadata:
  tags:
    - devops
    - runbook
    - on-call
    - sre
    - operations
    - automation
  updated: "2026-10-04"
---
# Executable Runbook Authoring

A method for writing runbooks that work at 3 a.m. for someone who has never touched the
service. The difference between a runbook and a wiki page is that each step says exactly
what to run, what you should see, and what to do when you do not see it.

## Purpose

Most runbooks fail in the same ways: "check the logs" with no query, commands for
infrastructure that no longer exists, a destructive step with no precondition, and no
indication of when to stop and escalate. This skill gives a step format that makes those
failures visible during writing, and a test-and-refresh loop that keeps them from
returning.

## When to Use This Skill

- Writing a runbook for a specific alert or a recurring operational task (rotate a
  certificate, fail over a database, drain a node, replay a dead-letter queue)
- An existing runbook failed during an incident, or the postmortem names it as a gap
- Converting knowledge that lives in one person's head or shell history into a procedure
- Planning which runbook steps to automate, and in what order
- Running a runbook drill or a quarterly runbook review

## When NOT to Use This Skill

- **Starting from ready-made incident runbook content** (service outage, database
  incident, severity matrix, communication templates). Use `incident-runbook-templates`,
  then apply this skill's step contract and test loop to the result.
- **Coordinating a live incident** (roles, comms cadence, severity). See the
  `/incident_response` command and `on-call-handoff-patterns`.
- **Writing the post-incident review.** Use `postmortem-writing`.
- **Security-alert triage for a small team.** See the prompt
  `domain-risk/risk_security_alert_triage_runbook.md`.
- **Fully automated remediation design.** This skill covers the ladder up to automation;
  building the automation itself belongs to the relevant platform skill.

## Prerequisites

- The alert definition or task description the runbook serves
- Read access to the systems the runbook touches, and a non-production environment where
  read-only commands can be tried
- Someone who has done the task before (for Step 2), and someone who has not (for Step 6)

## Workflow

### Step 1: Scope one runbook to one trigger

Write the header first. If it needs two triggers, it is two runbooks.

```markdown
# Runbook: <alert name or task>
- Trigger: <alert name / ticket type / schedule>
- Goal: <the observable end state, e.g. "p99 latency < 300 ms and error rate < 0.5% for 10 min">
- Audience: on-call engineer with production read access; no prior knowledge of this service
- Owner: <team or person>   Last verified: <YYYY-MM-DD> by <name>   Review by: <date>
- Access needed: <roles, VPN, break-glass procedure>
- Time to execute (last drill): <minutes>
```

### Step 2: Harvest the real procedure

Sources, in order of trustworthiness: shell history and console audit logs from the last
time it was done; the incident channel transcript; the postmortem; the expert's
recollection. Ask the expert three questions: "What do you check first?", "What would make
you stop and call someone?", and "What have you seen go wrong doing this?"

### Step 3: Write every step as a contract

```markdown
### Step 3: Drain the unhealthy node
- Precondition: Step 2 showed exactly one node NotReady. If more than one, STOP and go to Escalation.
- Action:
    kubectl drain "$NODE" --ignore-daemonsets --delete-emptydir-data
- Expected: output ends with `node/<name> drained`
- Verify:
    kubectl get node "$NODE"     # STATUS includes SchedulingDisabled
- If not as expected: do not retry more than once. Go to Escalation with the output.
- Risk: evicts pods on the node; safe when PodDisruptionBudgets exist for affected workloads
- Rollback:
    kubectl uncordon "$NODE"
```

Contract rules:

- **Precondition** names the observation from an earlier step that makes this step safe.
- **Action** is copy-pasteable: one command per block, no prompts, no smart quotes,
  variables set once at the top of the runbook (`export NODE=...`) rather than edited in place.
- **Expected** and **Verify** are concrete enough that two people would agree whether they
  were met.
- **If not as expected** always says what to do next: a branch, a retry limit, or escalation.
- Mark destructive or irreversible actions with a leading `DESTRUCTIVE:` label and require
  the precondition to be met first.
- Diagnostic steps come before changes. Order read-only checks from cheapest to most expensive.

### Step 4: Make decisions explicit branches

Replace prose such as "depending on the cause, you may want to…" with a table:

| Observation from Step 2 | Go to |
|---|---|
| Error rate rose within 15 min of a deploy | Step 4a: roll back the deploy |
| Errors only from one availability zone | Step 4b: shift traffic away from the zone |
| Database connection errors | `runbooks/db-connection-exhaustion.md` |
| None of the above | Escalation |

Keep branching at most two levels deep; deeper trees become separate runbooks.

### Step 5: Link it where it is needed

- Add the runbook URL to the alert itself. Prometheus alerting rules accept free-form
  annotations, and `runbook_url` is a widely used convention; most paging tools render
  links from alert annotations (verify against your tool's docs).
- Link the dashboards the steps read from, with the exact panel and time range.
- From the runbook, link back to the alert definition, so the threshold and the procedure
  are reviewed together.

### Step 6: Test the runbook

Run at least one of these before calling the runbook done, and again after any material
change:

1. **Read-through by a newcomer:** someone unfamiliar with the service reads it aloud and
   says what they would type at each step. Every hesitation is a defect.
2. **Dry run in non-production:** execute every read-only command for real and every
   change command against a non-production target. Fix commands that fail or produce
   output that differs from **Expected**.
3. **Drill (game day):** inject the failure in a controlled environment and have the
   on-call engineer follow the runbook unaided. Record time to execute and each point of
   confusion.

Record the result in the header (`Last verified`, `Time to execute`).

### Step 7: Climb the automation ladder deliberately

| Level | Form | Promote when |
|---|---|---|
| 0 | Written steps | — |
| 1 | Copy-paste commands with variables | Default target for every runbook |
| 2 | A script per step, printing what it will do and asking for confirmation | Step run unchanged in three or more incidents |
| 3 | One command for the whole runbook, with a confirmation before each change | Steps stable and well tested |
| 4 | Automatic remediation triggered by the alert | Low risk, reversible, and well understood |

Keep the written runbook at every level: it documents what the automation does and how to
do it by hand when the automation itself fails.

### Step 8: Keep it fresh

- Every runbook has an owner and a `Review by` date (90 days is a common default).
- Review triggers: the service's architecture changes, a postmortem mentions the runbook,
  or a drill finds a defect.
- A simple staleness report: list runbooks whose `Last verified` date is older than the
  review interval, and send it to owners on a schedule.

## Verification

A runbook is ready when:

- [ ] Header complete: trigger, goal, owner, last verified, access needed
- [ ] Every step has precondition, action, expected, verify, and what to do if not as expected
- [ ] Every destructive step is labelled and has a rollback or states that none exists
- [ ] Every branch ends in a step, another runbook, or Escalation
- [ ] The alert links to the runbook, and the runbook links to the alert
- [ ] At least one test from Step 6 completed and recorded
- [ ] No secrets, tokens or passwords in the text

## Common Failure Modes

| Symptom | Cause | Fix |
|---|---|---|
| "Check the logs" with no detail | Step written from memory | Give the exact query, the time range, and what a bad result looks like |
| Commands fail during an incident | Infrastructure changed; runbook never re-run | Dry run after each relevant change; review triggers in Step 8 |
| On-call engineer lacks access mid-incident | Access assumed, never checked | List access in the header; verify it in the pre-shift checklist |
| Pasted command fails mysteriously | Smart quotes or line wraps from a wiki editor | Keep commands in code blocks; test by pasting from the rendered page |
| Runbook grows into a design document | Background mixed into steps | Move background to a linked "How this service works" page |
| Escalation is always the last step | Stop conditions missing | Add explicit stop conditions to every risky step |

## Safety & Constraints

**NEVER:**
- Put credentials, tokens or connection strings with passwords in a runbook; reference
  the secret manager path instead
- Include a destructive command without a precondition and a stated rollback (or an
  explicit "irreversible" warning)
- Run change commands during a drill against production unless the drill plan says so and
  is approved

**ALWAYS:**
- Prefer the reversible action (scale, drain, shift traffic) over the irreversible one
  (delete, restore over data)
- Record who ran a runbook and the outcome in the incident timeline

## Related Skills

- `incident-runbook-templates`: ready-made incident runbook content to start from
- `on-call-handoff-patterns`: shift handoff and escalation practices that runbooks plug into
- `postmortem-writing`: postmortem action items often create or fix runbooks
- `slo-burn-rate-alerting` (observability): page-worthy alerts that each need a runbook link
- `infrastructure-drift-detection`: reconcile changes made by hand during a runbook
