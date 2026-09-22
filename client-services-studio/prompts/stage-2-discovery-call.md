# Stage 2 — Discovery Call

**Gate: none.** This stage produces the discovery record that Stage 3 scopes from.

**Input:** a lead that passed Gate 0 · **Output:** a discovery record

---

## Purpose

Discovery has one job: gather enough to write a scope that Gate A will pass. Every
question below maps to a field Gate A will check. A discovery call that does not
produce acceptance criteria, assumptions, exclusions and dated client inputs has not
finished, however pleasant it was.

## Orchestrated resource

**Run `domain-business-strategy/go-to-market/workflow_sales_discovery_call_preparation.md`
for the call itself.** It owns preparation, structure and conduct. This stage adds
only what the pipeline needs on top: the capture format, and the mapping from
questions to Gate A fields.

Supporting:

| For | Use |
|---|---|
| Planning what to learn | `domain-negotiation/preparation/negotiation_information_plan.md` |
| Mapping what they actually want | `domain-negotiation/preparation/negotiation_interest_mapping.md` |
| How much preparation this deserves | `domain-negotiation/preparation/negotiation_prep_depth_triage.md` |
| Question sequencing, live | `domain-negotiation/at-the-table/negotiation_question_sequencing_live.md` |
| Rehearsal | `domain-conversation-practice/conversation_practice_simulator.md` |

## What the pipeline needs from the call

Each question exists because a later gate needs its answer.

| Ask | Feeds |
|---|---|
| "Describe the problem in your words." | The proposal's opening paragraph |
| "What have you tried? What happened?" | Assumptions, and the value case |
| "What does done look like? How would you know?" | **Acceptance criteria — Gate A** |
| "What's explicitly not part of this?" | **Exclusions — Gate A** |
| "What would I need from you, and who owns it?" | **Client inputs — Gate A** |
| "What happens if that's late?" | **`if_late` — Gate A blocks without it** |
| "What does this cost you per month today?" | The value case, Stage 4 |
| "Who signs? What's the process after you say yes?" | Payment machinery, Stage 8 |
| "When does this need to be done, and why then?" | Timeline, and the urgency signal |

The `if_late` question is the one people skip. Asking "what happens if access slips
two weeks?" in the discovery call is comfortable; asking it in week three, when
access has slipped, is not.

## Capture format

```json
{
  "client": "",
  "problem_statement": "their words, their metrics",
  "trigger": "what made this urgent now",
  "tried_already": [],
  "success_looks_like": "",
  "how_they_would_know": "",
  "explicitly_out": [],
  "inputs_needed": [
    { "input": "", "owner": "", "due": "", "if_late": "" }
  ],
  "cost_of_current_state": "",
  "metric_they_track": "",
  "decision_process": "",
  "signer": "",
  "payment_machinery": {
    "terms_days": null, "approval_window_days": null,
    "payment_run_day_of_month": null, "cutoff_days_before_run": null,
    "po_required": null
  },
  "timeline_driver": "",
  "unresolved": []
}
```

`unresolved` is load-bearing. Anything you did not get an answer to goes here, and
Stage 3 either resolves it or converts it into a written assumption. Nothing
silently disappears.

## Asking about the payment machinery

Ask in the discovery call, not after the first invoice: "once we agree, what's the
process — is there a PO, who approves invoices, and when are payment runs?" It
sounds administrative and it is the difference between a 30-day and a 55-day
collection. People answer it readily before there is money at stake.

## Verification

- [ ] `success_looks_like` describes a changed state, not an activity
- [ ] `how_they_would_know` is observable — it will become an acceptance criterion
- [ ] `explicitly_out` is non-empty. If the client named nothing, you name two and
      confirm
- [ ] Every input in `inputs_needed` has an owner, a date and an `if_late`
- [ ] `signer` is a named person
- [ ] `unresolved` is written down rather than remembered

## If the call disqualifies the lead

Discovery surfaces things first contact did not. If a `decline`-tier signal appears,
return to Stage 1 and decline. Sunk discovery time is not a reason to proceed — it
is the smallest cost this engagement will ever present you with.
