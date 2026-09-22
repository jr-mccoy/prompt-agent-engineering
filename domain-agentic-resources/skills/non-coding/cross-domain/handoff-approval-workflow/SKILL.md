---
name: handoff-approval-workflow
description: Design a handoff or approval workflow that does not stall. Use this skill to "design an approval process", "work keeps getting stuck in review", "who signs off on this", "reduce approval bottlenecks", "define the handoff between teams", or when you need entry criteria per stage, one accountable approver instead of a committee, a stated timeout with a default action, a rework path that does not restart the whole chain, and an audit trail. Domain-agnostic — serves editorial review, procurement sign-off, change approval, clinical or legal review and cross-team delivery handoffs.
tags:
  - approval-workflow
  - handoff
  - sign-off
  - bottlenecks
  - accountability
  - cross-domain
updated: "2026-09-22"
---

# Handoff / Approval Workflow

A domain-agnostic pattern for moving work between people without it stalling. Two
failures recur: approvals that wait indefinitely because no timeout exists, and
committees where everyone can block and nobody can decide.

## When to Use This Skill

- Work sits in review for days with no one accountable for moving it
- Nobody is sure who approves what
- A handoff between teams keeps dropping context
- Approvals have accumulated until three people sign what one used to
- Rework sends a change back to the start of a five-stage chain

## Not for

- **Routing work in.** That is `../intake-triage-pattern/`.
- **Scoring the work's quality.** That is `../quality-rubric-template/`, which supplies
  the approval criterion this workflow gates on.
- **Escalating a stuck decision.** That is
  `../../../../../domain-decision-making/decisioning_escalation_decision_tree.md`.
- **Technical deployment gates** — CI, staged rollout, release pipelines — see
  `../../../cicd-automation/deployment-pipeline-design/` and
  `../../../../../domain-engineering-workflows/done-definition/`.

## The Pattern

### 1. Name each stage by the decision it makes

A stage that makes no decision is a queue. Every stage answers one question, and the
answer changes what happens next.

| Stage | The question it answers | Who answers it |
|---|---|---|

If two adjacent stages answer the same question, merge them. If a stage's answer is
always yes, it is a notification rather than an approval — relabel it, because a rubber
stamp adds delay and diffuses accountability without adding control.

### 2. Write entry criteria, so a stage can refuse to start

**This is the highest-value element and the one most workflows omit.** Without entry
criteria, work enters review incomplete, the reviewer spends their slot discovering what
is missing, and the round trip costs a full cycle.

| Stage | Entry criteria — work is not accepted without these |
|---|---|

A stage that can say "not ready, here is what is missing" in five minutes protects the
whole chain. This is the same discipline as a gate that refuses to run on an
under-specified input.

### 3. One accountable approver per stage

Not a committee. A committee requiring consensus defaults to the most cautious voice; a
committee requiring a majority means nobody owns the outcome.

Where several people must be *consulted*, separate the roles explicitly:

| Stage | Approver (decides) | Consulted (input, cannot block) | Informed (told after) |
|---|---|---|---|

The distinction between **consulted** and **approver** is where most approval bloat
lives. People added to be respectful acquire a veto nobody intended, and the workflow
slows by a day per person. Consultation is a request for input with a deadline; it is not
a gate.

### 4. Every stage has a timeout with a default action

An approval with no timeout is an indefinite hold, and "waiting on approval" becomes the
permanent state of the work.

| Stage | Timeout | Default on timeout |
|---|---|---|

Pick a default deliberately:

- **Auto-approve** — for reversible, low-consequence decisions. It puts the cost of
  silence on the approver rather than on the work, which is usually correct.
- **Escalate to the approver's deputy or manager** — for consequential decisions that
  must still be decided.
- **Return to the submitter** — where proceeding without a real decision would be worse
  than a delay.

**Auto-approve is legitimate and under-used**, but not everywhere: for safety, legal,
regulatory or irreversible decisions the default must be escalate or return, never
approve by silence. State which category each stage is in.

### 5. A rework path that does not restart the chain

The default design sends any change back to stage one, which is why people batch
feedback, avoid raising issues late, and route around the process entirely.

| Change type | Re-enters at | Stages that must re-approve |
|---|---|---|
| Cosmetic / editorial | The stage that raised it | None |
| Substantive within the same scope | The stage that raised it | Any later stage already passed |
| Scope change | Stage one | All |

Name who classifies the change — usually the stage that raised it — and make the
classification visible, because an unclassified change defaults to the most expensive
path.

### 6. Carry the context with the work

A handoff drops context unless the workflow requires it to travel. Define the minimum
packet each stage passes on:

| Field | Why the next stage needs it |
|---|---|
| What changed since the last stage | Avoids re-reviewing unchanged work |
| Decisions already made, and by whom | Prevents relitigating |
| Known open questions | Stops each stage rediscovering them |
| What this stage explicitly did **not** check | The most valuable field, and the rarest |

The last one prevents the shared assumption that someone earlier looked at something
nobody looked at.

### 7. Keep an audit trail, and use it to tune the workflow

Record who decided what, when, and on what basis. Then measure:

| Metric | What it tells you |
|---|---|
| Time in each stage | Where the bottleneck actually is, as opposed to where people think it is |
| Rejection rate per stage | A stage that never rejects is a rubber stamp; one that always rejects means entry criteria are too loose upstream |
| Timeout frequency per approver | An approver who times out routinely is over-allocated, not negligent |
| Rework loops per item | More than one or two means entry criteria or the rubric are unclear |

These four numbers are what turn an approval process from folklore into something
improvable. A stage that never rejects should be removed; an approver who always times
out should be replaced or given fewer stages.

## Output Template

```markdown
## Workflow — [what moves through it]

### Stages
| # | Stage | Decision it makes | Approver | Consulted | Informed |
|---|---|---|---|---|---|

### Entry criteria
| Stage | Not accepted without |
|---|---|

### Timeouts
| Stage | Timeout | Default on timeout | Category |
|---|---|---|---|
*Category: reversible (auto-approve permitted) / consequential (escalate) / irreversible
or regulated (return; never auto-approve)*

### Rework
| Change type | Re-enters at | Must re-approve | Classified by |
|---|---|---|---|

### Context packet
| Field | Required |
|---|---|
| What changed | |
| Decisions already made, by whom | |
| Open questions | |
| **Not checked at this stage** | |

### Audit and tuning
| Metric | Current | Target | Owner |
|---|---|---|---|
| Time in stage | | | |
| Rejection rate per stage | | | |
| Timeout frequency per approver | | | |
| Rework loops per item | | | |

### Removed from the previous workflow
| Stage or approver removed | Why |
|---|---|
```

## Verification

- [ ] Every stage makes a decision; none is a queue or a rubber stamp
- [ ] Every stage has entry criteria it can refuse on
- [ ] Exactly one accountable approver per stage
- [ ] Consulted and informed roles are separated from approver, and cannot block
- [ ] Every stage has a timeout with a deliberately chosen default
- [ ] No irreversible, safety or regulated stage defaults to auto-approve
- [ ] The rework path does not restart the chain for cosmetic or in-scope changes
- [ ] Someone is named to classify change types
- [ ] The context packet includes what the stage did *not* check
- [ ] The four tuning metrics have owners
- [ ] Stages that never reject have been removed

**False-positive prevention.** The dominant failure is approval by committee. It is
adopted to be inclusive and produces the opposite of accountability: three people can
block, none can decide, and the work waits for whoever is on leave. Separate approver
from consulted, and accept that consultation has a deadline and no veto.

The second failure is no timeout. "Waiting on approval" becomes the permanent state, and
because no rule was broken nobody can escalate. A timeout with a default converts an
indefinite hold into a decision — including the decision that silence means yes, which
for reversible work is usually right.

The third is the full-restart rework path. It is the reason people batch feedback and
raise concerns late: raising an issue costs the whole chain. Let in-scope changes re-enter
where they were raised.

The fourth is measuring nothing. Without time-in-stage and rejection-rate data, the
bottleneck is identified by whoever complains loudest, and rubber-stamp stages survive
indefinitely because removing them feels risky. The four metrics make both visible.

## Related

- `../intake-triage-pattern/` — how work gets into the workflow
- `../quality-rubric-template/` — the criterion a stage approves against
- `../../../../../domain-decision-making/decisioning_escalation_decision_tree.md` — when a stage cannot decide
- `../../../../../domain-engineering-workflows/done-definition/` — engineering's own stage criteria
- `../../../cicd-automation/deployment-pipeline-design/` — the automated deployment counterpart
