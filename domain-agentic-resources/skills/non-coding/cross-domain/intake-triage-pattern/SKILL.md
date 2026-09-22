---
name: intake-triage-pattern
description: Design an intake and triage system for incoming requests of any kind. Use this skill to "set up an intake process", "triage incoming requests", "stop things arriving by DM", "we have no idea what's in the queue", "route requests to the right person", or when you need a single front door, required fields that make a request actionable, a small closed set of severity or priority levels with observable definitions, explicit routing rules, a stated service level per level, and a reject-or-return path. Domain-agnostic — serves support queues, internal service desks, legal and security review requests, editorial submissions and research intake.
tags:
  - intake
  - triage
  - routing
  - prioritization
  - service-levels
  - cross-domain
updated: "2026-09-22"
---

# Intake Triage Pattern

A domain-agnostic pattern for turning an unmanaged stream of requests into a queue that
can be worked. The failure it fixes is always the same shape: requests arrive by six
channels, nobody knows the backlog, everything is urgent, and the person who shouts
loudest is served first.

## When to Use This Skill

- Requests arrive by direct message, email, hallway and ticket, and none of it is visible
- Everything submitted is marked urgent
- Work starts before anyone knows whether it is actionable
- Nobody can say what the queue contains or how long things wait
- The same clarifying questions are asked on every request

## Not for

- **Incident response during an incident.** Live incident handling is a different
  discipline — see
  `../../../devops/incident-runbook-templates/` and
  `../../../devops/on-call-handoff-patterns/`.
- **Escalation pathways.** How something moves up rather than in is
  `../../../../../domain-decision-making/decisioning_escalation_decision_tree.md` and
  `decisioning_crisis_severity_triage.md`.
- **Scoring or ranking the substance** of a request once accepted — that is
  `../quality-rubric-template/`.
- **Sales lead qualification**, which has its own lifecycle model — see
  `../../../marketing/revops/`.

## The Pattern

### 1. One front door

Every additional channel multiplies the invisible work. Pick one intake surface, publish
it, and route the others into it — including the informal ones.

The informal channels are the hard part and the reason most intake systems fail. A
colleague asking in person is not going to file a form, so the rule is: **the person who
receives an out-of-channel request files it**, not the requester. That keeps the queue
honest without making people feel bureaucratic, and it makes the real volume visible.

### 2. Required fields that make a request actionable

The intake form's job is to prevent the first round trip. For each field ask: does the
request become *actionable* without it? If yes, do not require it.

Almost always required:

| Field | Why |
|---|---|
| What is being asked for | The actual ask, not the proposed solution |
| Why now / what happens if it waits | The only honest input to priority |
| Requester and decision-maker | Frequently different people |
| Deadline, and what drives it | A date with no driver is a preference |
| What they have already tried | Prevents repeating work |

Usually a mistake to require: an estimate, a priority chosen by the requester, a
suggested assignee, elaborate categorisation. Requester-chosen priority is universally
inflated and should be an input, never the answer.

### 3. A small closed set of levels, defined observably

Three or four. More cannot be applied consistently; five-level scales collapse into
"high" and "everything else".

Define each level by **observable conditions**, not adjectives — otherwise the level
records the requester's tone:

| Level | Observable condition | Response target | Who can assign it |
|---|---|---|---|
| 1 | Work is fully stopped for [n] people, or a legal/safety deadline is inside [x] | | Triager |
| 2 | A committed external date is at risk | | Triager |
| 3 | Work continues with a known workaround | | Triager |
| 4 | Improvement with no deadline | | Triager |

Two rules that make it hold: **only the triager assigns the level**, and **the level is
visible to the requester** with its definition, so disagreement is about the definition
rather than about feelings.

### 4. Route on the request, not on who asked

Write the routing rules down. Unwritten routing means the triager's memory is the system,
and it breaks when they are away.

| If the request is about | Route to | Fallback |
|---|---|---|

Then the two cases most systems omit:

- **Nobody obviously owns it.** Name a default owner who decides where it goes. Requests
  with no home are the ones that sit for weeks.
- **It needs several owners.** One accountable owner, named, who coordinates. Two owners
  is no owner.

### 5. State a service level per level, and make it a promise you keep

Two separate commitments, and conflating them is the commonest cause of frustration:

- **Time to first response** — someone has read it and said what happens next. Should be
  short for every level, including the lowest.
- **Time to resolution** — varies by level and may be "not scheduled".

A stated 24-hour response that routinely takes a week is worse than an honest "we triage
weekly on Mondays". Publish what you actually do.

### 6. Provide a reject-or-return path

A queue with no exit is a queue that grows until it is abandoned. Four legitimate
outcomes, all of them ending the request:

| Outcome | Meaning |
|---|---|
| **Accepted** | Levelled, routed, owned |
| **Returned** | Not yet actionable — the specific missing information is named |
| **Declined** | Out of scope. The reason is given and, where possible, an alternative |
| **Merged** | Duplicate of an existing request, which is linked |

"Declined" must be genuinely available. An intake process that can only accept
accumulates a backlog everybody stops believing in — and the honest decline is kinder
than the indefinite wait.

### 7. Review the queue on a cadence, and review the system too

- **Queue review** — at a fixed cadence: what is ageing, what is mis-levelled, what
  should be declined now.
- **System review** — periodically, on the intake itself:

| Signal | What it means |
|---|---|
| Most requests arrive at the top level | Level definitions are not being applied, or the definitions are wrong |
| Many returns for the same missing field | That field should be required, or the form asks it unclearly |
| A category recurs constantly | It should be self-service or automated, not triaged |
| Requests still arriving out of channel | The front door is harder to use than the informal route |
| Ageing items nobody will decline | The decline path is not actually available in practice |

The last two are the ones that quietly kill an intake system, and both are fixable.

## Output Template

```markdown
## Intake and triage — [queue name]

**Front door:** [the one channel] · **Out-of-channel rule:** the receiver files it
**Triager:** [role] · **Cadence:** [when triage happens]

### Required fields
| Field | Required? | Why |
|---|---|---|

### Levels
| Level | Observable condition | First response | Resolution target | Assigned by |
|---|---|---|---|---|

### Routing
| Request about | Route to | Fallback |
|---|---|---|
**No obvious owner →** [default decider]
**Multiple owners →** one accountable coordinator, named

### Outcomes
| Outcome | Criteria | Who communicates it |
|---|---|---|
| Accepted | | |
| Returned | | |
| Declined | | |
| Merged | | |

### Published to requesters
[where the levels, targets and the decline path are visible]

### Reviews
Queue: [cadence, owner] · System: [cadence, owner]
| System signal | Current | Action |
|---|---|---|
```

## Verification

- [ ] Exactly one front door, with the out-of-channel rule assigning filing to the receiver
- [ ] Every required field is genuinely needed for the request to be actionable
- [ ] Requester-chosen priority is an input, not the assigned level
- [ ] Three or four levels, each defined by observable conditions
- [ ] Only the triager assigns levels, and definitions are visible to requesters
- [ ] Routing rules are written, with a default owner for unowned requests
- [ ] Multi-owner requests have one accountable coordinator
- [ ] First-response and resolution targets are separate, and the response target is real
- [ ] Decline is genuinely available and has been used
- [ ] Both a queue review and a system review have owners and cadences

**False-positive prevention.** The dominant failure is level definitions written as
adjectives — "critical", "high", "normal". Everything arrives critical, because the
requester is describing their own urgency rather than an observable condition. Define
levels by what is true in the world: how many people are stopped, whether a committed
date is at risk, whether a workaround exists.

The second failure is an intake form that optimises for the triager's convenience. Every
non-essential required field raises the cost of filing and pushes requests back to the
informal channel, which is exactly the problem the system exists to solve. Require only
what makes a request actionable.

The third is a queue with no exit. If nothing is ever declined, the backlog grows past
credibility and requesters stop filing — then the work arrives by DM again. Use the
decline path, and give a reason.

The fourth is skipping the system review. Intake systems degrade predictably: levels
inflate, the front door erodes, one category dominates. The signals table catches all
three, and it takes minutes.

## Related

- `../quality-rubric-template/` — scoring a request's substance once accepted
- `../handoff-approval-workflow/` — what happens after triage routes it
- `../../../../../domain-decision-making/decisioning_escalation_decision_tree.md` — moving up rather than in
- `../../../../../domain-risk/risk_appetite_statement.md` — where severity thresholds should agree with the organisation's stated limits
- `../../../devops/incident-runbook-templates/` — live incident handling
