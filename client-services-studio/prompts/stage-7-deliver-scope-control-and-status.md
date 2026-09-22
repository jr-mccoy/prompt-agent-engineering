# Stage 7 — Deliver, Control Scope, Report Status

**Gate: none.** Continuous drift detection rather than a single checkpoint.

**Input:** a signed engagement · **Output:** change orders, and status reports

---

## Purpose

Two jobs that run for the length of the engagement: keep delivered work aligned with
agreed scope, and keep the client informed in a way that makes bad news survivable.

The failure this stage prevents is the quiet one. Scope does not usually blow out; it
drifts, one small agreement at a time, each too minor to object to. The close-out
post-calculation will name the moment it started — this stage is where you catch it
instead.

## Scope control

### 1. Track delivered work against the record

Maintain a delivered record as work completes:

```json
{ "items": [ { "id": "D1", "name": "", "days": 0 } ] }
```

Items delivered against agreed deliverables carry their `id`. Anything else gets a
new id — and that is the signal.

### 2. Run drift detection at every checkpoint

```bash
python3 skills/scope-ledger/scripts/scope_ledger.py \
    --drift <engagement.json> --delivered <delivered.json>
```

| Finding | Meaning | Action |
|---|---|---|
| **high** | Delivered work is on the exclusion list | Stop. Change order before any further work |
| **medium** (item) | Delivered work is not an agreed deliverable | Change order |
| **medium** (effort) | Effort exceeds agreed by more than 15% | Review scope before continuing |

### 3. Raise the change order

A change order is a small, unembarrassed document: what is being added, what it
costs, what it does to the timeline, and a signature line. Price it at your standard
rate, not at a discount — a discounted change order teaches the client that the scope
boundary is negotiable.

The procedure is in `domain-legal/contracts-transactional/legal_sow_drafter.md`,
which owns the contractual mechanism.

### 4. Say no when the answer is no

Not every request becomes a change order. Some are outside the offer entirely. The
scripts for this conversation exist and are vendored:

| For | Use |
|---|---|
| Repricing without souring the relationship | `domain-negotiation/contexts/negotiation_freelance_rate_conversation.md` |
| Holding a line under pressure | `domain-negotiation/contexts/negotiation_customer_escalation_concession.md` |
| Declining upward | `domain-negotiation/difficult-conversations/difficultconvo_saying_no_upward.md` |
| Written, asynchronous | `domain-negotiation/channels/negotiation_written_async_message.md` |

### 5. Watch the obligations, not just the deliverables

**`domain-negotiation/after-the-deal/negotiation_implementation_and_relationship.md`**
converts signed terms into obligations with owners and dates, and names the terms
likely to lapse quietly and the early-warning signals of drift. It is the backbone of
this stage; do not rebuild it.

Client-side obligations matter as much as yours. A missed client input with a stated
`if_late` consequence must actually trigger that consequence, in writing, at the
time. An `if_late` clause invoked retrospectively is not a clause.

## Status reporting

### Cadence and content

Report on a fixed cadence agreed at kickoff. Each report carries:

- **Status** — on track / at risk / blocked, stated plainly in the first line
- **Since last time** — what was delivered
- **Next** — what happens before the next report
- **Budget posture** — days consumed against days agreed, and scope consumed
- **Blocked on** — including anything you are waiting on from them, with its date
- **Decisions needed** — with a by-when

The budget line is what distinguishes a services status report from a project
update. It is also the mechanism by which an overrun becomes a conversation in week
three rather than a surprise at invoice time.

### Orchestrated resources

| For | Use |
|---|---|
| The report itself | `domain-professional-writing/business-writing/business_writing_status_report.md` |
| Budget posture framing | `domain-legal/client-intake-communications/legal_client_status_update_memo.md` |
| Delivering bad news | `domain-negotiation/difficult-conversations/difficultconvo_delivering_bad_news.md` |
| Preparing for a hard conversation | `domain-negotiation/difficult-conversations/difficultconvo_pre_brief.md` |
| Quality gate on client-facing output | `domain-professional-writing/content-quality/quality_slop_client_deliverable.md` |

### Bad news travels immediately

A slipping date reported the day you know is a manageable problem. The same date
reported at the deadline is a credibility event. There is no version of this where
waiting helps.

## Verification

- [ ] Drift detection runs at every checkpoint, not at the end
- [ ] Every non-agreed item became a change order or an explicit written decision to
      absorb it
- [ ] Absorbed items are recorded — the close-out post-calculation needs them
- [ ] Change orders are priced at standard rate
- [ ] Every missed client input triggered its stated consequence, in writing, at the time
- [ ] Every status report carries a budget posture line
- [ ] Bad news was reported on the day it was known
