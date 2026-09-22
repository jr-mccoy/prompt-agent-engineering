# Stage 1 — Qualify the Lead

**Gate 0 — qualify-out.** Code-enforced. Blocked leads do not proceed to discovery.

**Input:** a lead record · **Output:** a Gate 0 result, and either a discovery
booking or a decline

---

## Purpose

The most expensive hour in a services practice is the one spent on an opportunity
that was visible as bad from the first email. This stage spends ten minutes instead.

Gate 0 tests four structural conditions and the practice's own disqualifier list. It
blocks; it does not advise.

## Procedure

### 1. Capture the lead record

From the first contact — email, call, referral — record:

```json
{
  "client": "",
  "decision_maker": null,
  "budget_authority": false,
  "outcome_defined": false,
  "indicative_budget": null,
  "indicative_days": null,
  "client_current_revenue_pct": 0,
  "client_added_revenue_pct": 0,
  "disqualifiers_observed": []
}
```

Do not infer these. `decision_maker` is a name they gave you, not the person who
emailed. `budget_authority` is true only if they said so or it is structurally
obvious. `outcome_defined` is true only if they described a changed state, not an
activity.

Leave `indicative_budget` null if unknown. Unknown budget is a discovery question,
not a Gate 0 failure — only a *stated* budget implying a sub-floor rate blocks.

### 2. Run the ten-minute question sequence

From your disqualifier work in Stage 0. At minimum:

1. "Who else needs to agree before this goes ahead?" → `decision_maker`,
   `budget_authority`
2. "What's different for you when this is done?" → `outcome_defined`
3. "What made this urgent now?" → trigger, and the urgency-disproportionate signal
4. "Has anyone worked on this before?" → the prior-vendor signal
5. "What range were you expecting to spend?" → `indicative_budget`

Record every disqualifier signal you observe by its config id.

### 3. Run the gate

```bash
python3 skills/scope-ledger/scripts/scope_ledger.py \
    --gate0 <lead.json> --config config/practice.json
```

Exit 0 proceeds. Exit 1 blocks.

### 4. Act on the result

**PASS with no warnings** → book discovery (Stage 2).

**PASS with warnings** → the gate found `probe` or `proceed_with_protection` tier
signals. Each names a specific question or a specific structural protection. Resolve
each before booking:

| Tier | Action |
|---|---|
| `probe` | Ask the one question that resolves it. An unsatisfying answer makes it a decline |
| `proceed_with_protection` | Book discovery, but only with the named protection — a paid discovery phase, a smaller first engagement, milestone payment, written decision-maker sign-off |

**BLOCKED** → decline, now, in the first conversation. Use the standard decline
message from your Stage 0 work. Decline honestly and briefly: a fabricated
scheduling excuse costs the referral that an honest "this isn't what I do, try X"
preserves.

### 5. Record the outcome

Every blocked lead is data. Record which check fired. If the same check blocks
repeatedly, either your positioning is attracting the wrong inquiries or the rule is
mis-calibrated — both are findings.

## Orchestrated resources

| For | Use |
|---|---|
| The disqualifier framework | `domain-business-strategy/client-services/services_ideal_client_and_disqualifiers.md` |
| Concentration check | `domain-business-strategy/client-services/services_client_concentration_risk_check.md` |
| Whether a thin pipeline is pressuring the rules | `domain-business-strategy/client-services/services_capacity_and_utilization_planner.md` |
| Background research before the call | `domain-business-strategy/go-to-market/research_person_background.md` |

## Verification

- [ ] Every field in the lead record came from something said, not inferred
- [ ] The gate was run, not eyeballed
- [ ] Warnings were each resolved before booking, not noted and ignored
- [ ] A blocked lead was actually declined
- [ ] The outcome was recorded

## The override

You will sometimes take a blocked lead. Do it **on the record**: note which check
fired, why you overrode it, and a review date. A deliberate, dated override is a
commercial decision. An undocumented one is the rule quietly ceasing to exist, and
the capacity planner's bench date is usually the reason. Check it before you
override.
