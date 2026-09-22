---
title: "Business Continuity Plan — Recovery Objectives, Tested Procedures, and an Honest Gap List"
category: risk
description: "Build a continuity plan around the functions that must keep running: business impact analysis producing a recovery time and data-loss objective per function, the dependencies each one needs, procedures written for someone working in degraded conditions, activation authority and succession, a communications plan, and a test schedule with the untested and unmet objectives listed openly. Refuses plans with untested procedures presented as capability."
techniques:
  - ST-02
  - CM-02
  - QA-08
  - RT-10
  - OC-03
difficulty: advanced
tags:
  - business-continuity
  - disaster-recovery
  - rto-rpo
  - resilience
  - succession
updated: "2026-09-22"
related_prompts:
  - domain-risk/risk_dependency_chain_audit.md
  - domain-risk/risk_appetite_statement.md
  - domain-risk/risk_after_action_review.md
---

# Business Continuity Plan

**Objective:** Produce a plan organised around **the functions that must keep running**,
not around the disasters that might happen: a business impact analysis giving each
critical function a recovery time objective and a data-loss objective, the dependencies
it needs, procedures written for a tired person working with degraded tools, stated
activation authority and succession, a communications plan, and a test schedule — with
every untested procedure and every unmet objective listed openly. A plan that presents
untested procedures as capability is refused.

**When to Use:**
- You have no continuity plan and a customer, insurer, auditor or investor has asked.
- Your plan is a document nobody has opened since it was written.
- A near-miss showed that the recovery path existed only in one person's head.
- `risk_dependency_chain_audit.md` has surfaced single points of failure and you need the
  response side.

**When NOT to use:**
- You need to *find* the single points of failure — that is
  `risk_dependency_chain_audit.md`, which traces dependency chains and prioritises by
  blast radius × replacement difficulty. Run it first; this plan responds to what it
  finds.
- You need the structural dependency topology — that is
  `../domain-reasoning-craft/systems/systems_dependency_map.md`.
- You need technical disaster recovery for one system — runbooks and failover — route to
  `../domain-agentic-resources/skills/devops/incident-runbook-templates/` and
  `../domain-agentic-resources/skills/observability/slo-implementation/`.
- You need incident response for a live incident — route to
  `../domain-agentic-resources/skills/devops/incident-runbook-templates/`; this is the
  plan you make beforehand.
- You need scenario planning under strategic uncertainty — this domain routes that out:
  `../domain-decision-making/scenario_two_by_two_matrix.md` and siblings.
- You are planning for **agent session memory** continuity — unrelated despite the
  shared word; that is
  `../domain-AI-ML/agentic-ai-systems/aiagent_project_continuity_memory_design.md` and
  the `continuity-kit/` toolkit.

---

## Context Gathering

1. **Functions, not systems**
   - "List what the organisation *does* that someone outside would notice stopping."
   - "For each: who does it, and what do they need to do it?"
   - "Which of these could stop for a week without permanent damage? Which for a day?"

2. **Obligations**
   - "Any contractual availability or recovery commitments? Regulatory ones?"
   - "Anything where stopping creates a safety or legal exposure rather than a
     commercial one?"

3. **Dependencies**
   - From `risk_dependency_chain_audit.md`: "which people, suppliers, systems,
     premises, licences and data stores are single points of failure?"

4. **What has actually happened**
   - "What has gone wrong in the last three years? What did you do?"
   - "Has any recovery procedure ever been executed for real, or tested?"

The last question determines the plan's honesty. Most continuity plans contain
procedures that have never been run once, and the organisation believes it has a
capability it has not verified.

---

## Method

### Step 1 — Business impact analysis: functions first, disasters never

Do not organise by scenario. A plan with chapters for fire, flood, pandemic and
cyber-attack triplicates the same procedures and still misses the disaster you get. Plan
for **loss of a capability**, and the causes become irrelevant to the response.

Four losses cover almost everything:

| Loss | Covers |
|---|---|
| Loss of **people** | Illness, resignation, accident, key-person absence, industrial action |
| Loss of **premises or access** | Fire, flood, utility failure, denial of access, travel disruption |
| Loss of **systems or data** | Outage, ransomware, corruption, supplier failure, expired certificate |
| Loss of a **supplier or third party** | Insolvency, breach, withdrawal, contract termination |

For each critical function:

| Function | Impact of stopping — 1h / 1d / 1w | RTO | RPO | Obligation driving it |
|---|---|---|---|---|

- **RTO** (recovery time objective): how quickly it must be working again.
- **RPO** (recovery point objective): how much data loss is acceptable — which for many
  functions is the harder number and the one nobody has asked.

Set these from impact and obligation, **not** from what current capability allows. A plan
whose objectives are back-derived from what you can already do records the status quo and
discovers nothing.

### Step 2 — Map each function's dependencies

| Function | People | Systems | Data | Premises | Suppliers | Licences / access |
|---|---|---|---|---|---|---|

Then flag every dependency that is a single point of failure, drawing on
`risk_dependency_chain_audit.md`. The intersection of *critical function* and *single
point of failure* is the entire priority list; everything else in this document is
paperwork around it.

### Step 3 — Write procedures for degraded conditions

Continuity procedures get executed by a tired person at an inconvenient hour, possibly
not the person who wrote them, possibly without the usual tools. Write accordingly:

- **Numbered steps**, no prose paragraphs.
- **Named roles, not names**, with a named current holder in an appendix — the plan
  outlives the person.
- **No dependency on the thing that failed.** A procedure stored only in the wiki that
  is down, or requiring the SSO that is unavailable, or naming a contact reachable only
  through the failed system, is not a procedure. Check every step against the loss it
  responds to.
- **Offline availability.** Printed, or in a location independent of the primary
  systems. State where.
- **Decision points marked**, with who decides and what to do if they are unreachable.

| Step | Action | Role | Needs | If unavailable |
|---|---|---|---|---|

### Step 4 — State activation authority and succession

The most common failure in real events: nobody was sure they were allowed to invoke the
plan, so everyone waited.

- **Who can activate**, by role, and what triggers it. Include a partial-activation
  option — most events are not total.
- **Succession**, at least two deep, for every activation role and every single-point
  person. A succession list one deep is not a succession list.
- **Authority while activated** — what can the acting person commit, spend, or decide
  that they normally could not? An acting lead with no spending authority cannot buy the
  replacement hardware.
- **Stand-down authority** and criteria, because a plan that never formally ends leaves
  the organisation in degraded mode for weeks.

### Step 5 — Plan communications, with the channel independence check

| Audience | Who tells them | Channel | Within | First message says |
|---|---|---|---|---|
| Staff | | | | |
| Customers | | | | |
| Suppliers | | | | |
| Regulator / insurer | | | | |
| Public / press | | | | |

Two checks that continuity plans routinely fail. **Channel independence**: if the
notification channel depends on the failed system — staff email during an email outage,
a status page on the failed infrastructure — it is not a channel. Name the out-of-band
alternative and hold the contact list somewhere reachable without the primary systems.

And write the **first message now**, as a template with blanks. Nobody drafts well in
hour one, and the first message sets the tone for the whole event.

### Step 6 — Schedule tests, and list what is untested

A procedure that has never been tested is a hypothesis. Three levels, escalating in cost
and confidence:

| Level | What it is | Confidence it gives |
|---|---|---|
| **Walkthrough** | Read the procedure aloud with the roles present | Finds missing steps and wrong contacts |
| **Tabletop** | Simulate an event and talk through decisions | Finds authority gaps and unclear triggers |
| **Live test** | Actually fail over, actually restore the backup | The only thing that tests capability |

Backup restoration in particular is only proven by restoring. An untested backup is a
belief, and the discovery that it does not restore reliably happens during the event.

### Step 7 — List the gaps openly

The section that makes the plan trustworthy, and the one most plans omit:

| Function | RTO required | RTO achievable today | Gap | What would close it | Cost | Accepted by |
|---|---|---|---|---|---|---|

An honest gap list is more valuable than a plan claiming full coverage, for three
reasons: it lets someone accept the residual risk deliberately (feeding
`risk_appetite_statement.md`), it gives the investment case a number, and it means the
plan does not lie to the person who opens it during an event.

---

## Output Format

```markdown
## Business continuity plan — [organisation], [date]

**Owner:** [role] · **Last tested:** [date, level] · **Next review:** [date]
**Held offline at:** [location] · **Activation contact list at:** [independent location]

### Business impact analysis
| Function | Impact 1h / 1d / 1w | RTO | RPO | Obligation |
|---|---|---|---|---|

### Dependencies and single points of failure
| Function | People | Systems | Data | Premises | Suppliers | SPOF flagged |
|---|---|---|---|---|---|---|

### Procedures by loss type
#### Loss of people
| Step | Action | Role | Needs | If unavailable |
|---|---|---|---|---|
#### Loss of premises / access
#### Loss of systems / data
#### Loss of supplier

**Independence check:** no step depends on the failed capability [confirmed per procedure]

### Activation
| | |
|---|---|
| Who can activate | [roles] |
| Triggers | |
| Partial activation available | |
| Authority while activated | [spend, commit, decide] |
| Stand-down authority and criteria | |

### Succession (two deep minimum)
| Role | Primary | Second | Third |
|---|---|---|---|

### Communications
| Audience | Who | Channel | Out-of-band alternative | Within | First message |
|---|---|---|---|---|---|

**First message templates:** [drafted, with blanks]

### Test schedule
| Procedure | Level | Last run | Result | Next due |
|---|---|---|---|---|

**Never tested:** [listed explicitly]

### Gaps
| Function | RTO required | Achievable | Gap | To close | Cost | Accepted by |
|---|---|---|---|---|---|---|
```

---

## Verification

- [ ] Organised by loss of capability, not by disaster scenario
- [ ] Every critical function has an RTO **and** an RPO
- [ ] Objectives are set from impact and obligation, not back-derived from current capability
- [ ] Dependencies are mapped and SPOFs flagged from the dependency audit
- [ ] Every procedure is numbered steps with roles, not prose with names
- [ ] No procedure step depends on the capability that failed — checked per procedure
- [ ] The plan and the contact list are available offline, and the location is stated
- [ ] Activation authority, partial activation, acting authority and stand-down are all specified
- [ ] Succession is at least two deep for every activation role and SPOF person
- [ ] Every communication channel has an out-of-band alternative
- [ ] First messages are drafted in advance
- [ ] A test schedule exists and untested procedures are listed as untested
- [ ] Backup restoration has been tested by restoring, not by checking the job succeeded
- [ ] The gap list is present, with an accepter for each residual gap

**False-positive prevention.** The dominant failure is the untested plan presented as a
capability. It satisfies the auditor, reassures the board, and does not work — and the
discovery happens at the worst moment. The test schedule and the explicit
"never tested" list are the corrective: a plan honest about what is unproven is more
useful than one that implies coverage it has not verified.

The second failure is organising by disaster. Fire, flood and pandemic chapters
triplicate the same three procedures and still miss the actual event, which is usually a
supplier failure or one person being unavailable. Four capability losses cover the field.

The third is the self-referential procedure — stored in the wiki that is down, requiring
the SSO that is out, listing a contact reachable only by the failed email. It is
extremely common because plans are written while everything works. Check every step
against the loss it responds to; that check alone justifies the exercise.

The fourth is back-derived objectives. An RTO of four hours because that is what the
current backup schedule allows is not an objective, it is a description. Set it from
impact, then let the gap list show the distance — that distance is the investment case.

The fifth is succession one deep. Naming a single deputy for a single-point-of-failure
person has moved the problem, not solved it: the event that removes one person
frequently removes both.

---

## Related

- `risk_dependency_chain_audit.md` — finds the single points of failure this responds to
- `risk_appetite_statement.md` — where residual gaps get formally accepted
- `risk_register_builder.md` — the register these functions and dependencies should appear in
- `risk_after_action_review.md` — after a real activation, blamelessly
- `../domain-agentic-resources/skills/devops/incident-runbook-templates/` — the technical runbook layer
- `../domain-business-strategy/client-services/services_client_concentration_risk_check.md` — client-side concentration, for a services practice
