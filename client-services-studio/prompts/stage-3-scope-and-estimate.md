# Stage 3 — Scope and Estimate

**Gate: none here.** This stage builds the record Gate A will test in Stage 4.

**Input:** a discovery record · **Output:** the `scope` block of the engagement record

---

## Purpose

Turn a discovery record into a scope that can be priced. Gate A's requirements are
the specification: deliverables with formats and acceptance criteria, assumptions,
exclusions, and client inputs with owners, dates and consequences.

The discipline is that the scope is written **before** the number. Scoping backwards
from a price the client mentioned is how fixed fees become open commitments.

## Procedure

### 1. Write the deliverables

Each deliverable needs an id, a name, a format, an acceptance criterion and an effort
estimate.

The acceptance criterion is the hard part and the valuable one. Apply the stranger
test: **could someone holding only this sentence tell whether it had been
delivered?**

| Fails | Passes |
|---|---|
| "Strategic review of the data platform" | "A written assessment of the seven named pipelines against the six criteria in Appendix A" |
| "Recommendations" | "A ranked list in which every finding from D1 appears exactly once, with an effort estimate" |
| "Support during rollout" | "Attendance at the four scheduled rollout calls, with written notes within two working days of each" |

**Use `domain-engineering-workflows/workflows/workflow_definition_of_done_builder.md`
to convert fuzzy deliverables into testable conditions.** It exists for exactly this
and is vendored under `referenced-prompts/`.

### 2. Estimate effort per deliverable

Estimate each deliverable separately; do not estimate the engagement. Then apply your
own measured overrun from
`domain-finance/corporate-finance-fpa/finance_engagement_profitability_postcalc.md`.
If you have no measured overrun, that fact decides the pricing structure in Stage 4 —
you cannot quote a fixed price without it.

### 3. Write the assumptions

Every estimate rests on assumptions. Surface them. Start from the discovery record's
`unresolved` list: each entry becomes either a resolved fact or a written assumption.
Nothing stays unresolved and unwritten.

An assumption is well written when its falsity is observable and its consequence is
stated: "the seven pipelines in scope are those listed in Appendix A and do not
change" is testable; "the environment is reasonably well documented" is not.

### 4. Write the exclusions

Work through each deliverable and ask what a reasonable client will assume is
included. At minimum, decide explicitly on:

| Axis | The assumption to pre-empt |
|---|---|
| Implementation | Do you do the fix, or specify it? |
| Rounds | How many revision cycles before it is new work? |
| Access and systems | Whose, and who grants it? |
| Stakeholders | How many interviews, how many review meetings? |
| The obvious next question | The work will raise one — is answering it in? |
| Support after handover | For how long, at what rate? |

An exclusion list that excludes only absurdities is decorative. At least one entry
should be something you have actually been asked for and regretted saying yes to.

### 5. Write the client inputs

Each needs `input`, `owner` (a named person), `due` (a date) and `if_late` (a real
consequence). Gate A blocks without all four.

Real consequences, not hopes:

- "the clock continues; the end date moves day for day"
- "findings depending on it are marked unverified"
- "the engagement pauses and restarts at the next available slot"

"Client will provide access promptly" is not a consequence.

### 6. Assemble the record

```json
"scope": {
  "deliverables": [
    { "id": "D1", "name": "", "format": "", "acceptance": "", "estimated_days": 0 }
  ],
  "assumptions": [],
  "exclusions": [],
  "client_inputs": [
    { "input": "", "owner": "", "due": "", "if_late": "" }
  ]
}
```

## Orchestrated resources

| For | Use |
|---|---|
| Testable acceptance criteria | `domain-engineering-workflows/workflows/workflow_definition_of_done_builder.md` |
| The offer's standing exclusions | `domain-business-strategy/client-services/services_offer_definition_and_boundary.md` |
| Engagement risk register | `domain-risk/risk_register_builder.md` |
| Trading scope against constraints | `domain-decision-making/decisioning_multi_constraint_optimizer.md` |

## Verification

- [ ] Every acceptance criterion passes the stranger test
- [ ] Every deliverable has its own effort estimate
- [ ] Every entry on the discovery record's `unresolved` list is now resolved or a
      written assumption
- [ ] Every assumption's falsity is observable
- [ ] The exclusion list contains at least one item drawn from real past friction
- [ ] Every client input has an owner, a date and a real consequence
- [ ] No price appears anywhere in this record

The last item is not pedantry. Scope and price are separated so that Gate A can
refuse to price an under-specified scope. If the number is already in the document,
the gate has nothing to protect.
