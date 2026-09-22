# Stage 9 — Close Out

**Gate C — close-out complete.** Code-enforced. An engagement is not closed until it
is closed.

**Input:** a delivered engagement · **Output:** a close-out record, an updated
estimate-error series, and the two asks

---

## Purpose

Close the financial loop and harvest what the engagement is worth beyond its fee. The
estimate-error series that decides every future fixed-price question only exists if
this stage runs **every time** — including on the engagements that went well, which
establish the lower bound of the range.

## Procedure

### 1. Assemble the close-out record

```json
{
  "engagement": "", "client": "",
  "revenue": { "invoiced": 0, "write_offs": 0, "outstanding": 0 },
  "direct_costs": {},
  "effort": { "estimated_days": 0, "billed_days": 0, "unbilled_days": 0 },
  "case_study_consent": "",
  "client_verdict": ""
}
```

`unbilled_days` is the number most consistently under-reported and exactly the one
that turns an apparently profitable engagement into a marginal one. Rework, absorbed
scope, extra meetings, client-specific admin. Be honest; nobody else sees this.

### 2. Run Gate C

```bash
python3 skills/engagement-economics/scripts/economics.py --gateC <closeout.json>
```

It blocks while an invoice is outstanding and not written off, while unbilled effort
or the original estimate is unrecorded, or while case-study consent and the
repeat/decline verdict are missing. An engagement with money outstanding is not
closed; it is in collections — go back to Stage 8.

### 3. Compute the realised economics

```bash
python3 skills/engagement-economics/scripts/economics.py \
    --postcalc <closeout.json> --config config/practice.json
```

Revenue is **collected**, effort is **total**. The result places the realised rate
against walk-away, floor and standard.

Full method:
`domain-finance/corporate-finance-fpa/finance_engagement_profitability_postcalc.md`.
It also covers the variance decomposition and the divergence point — the specific
moment and the specific decision at which plan and reality parted. There is almost
always a decision, and it was almost always made in a single message without
deliberation.

### 4. Update the estimate-error series

Append `total_effort / estimated_days`. Once five points exist, the coefficient of
variation rules on fixed-price eligibility for this engagement type. Feed it forward
to Stage 4 and to
`domain-business-strategy/client-services/services_productized_offer_designer.md`.

### 5. Run the qualitative retrospective

The financial loop is closed; the human one is not. Use an existing retrospective
rather than a fifth generic one:

| For | Use |
|---|---|
| What happened and why | `domain-risk/risk_after_action_review.md` |
| Negotiation-specific | `domain-negotiation/after-the-deal/negotiation_post_negotiation_debrief.md` |
| Written for the client | `domain-professional-writing/business-writing/business_writing_post_mortem.md` |

### 6. Update the disqualifier list

State plainly whether you would take this client again, and on what terms. Feed the
answer to
`domain-business-strategy/client-services/services_ideal_client_and_disqualifiers.md`
and into `config/practice.json`. A disqualifier list never updated from close-outs is
theory.

### 7. Ask — at the right moment, separately

Close-out is usually the **wrong** moment for a testimonial. The client has a
deliverable; they do not yet have a result. Wait for visible value — typically four
to twelve weeks — or for unprompted praise, which is a testimonial they have already
written.

When the moment comes, the two asks go in **separate messages**, testimonial first:

```
domain-professional-writing/business-writing/business_writing_testimonial_and_referral_request.md
```

Gate on outstanding items first. Never ask while an invoice is unpaid — it reads as
leverage.

### 8. Write the case study

```
domain-professional-writing/business-writing/business_writing_engagement_case_study.md
```

Check the confidentiality position **before** drafting. Every claimed number carries
a baseline, a source, a period and a measurer. State what else could account for the
result — a sophisticated buyer discounts unqualified claims automatically. Fact-check
with the sponsor before publication, then score with
`domain-professional-writing/content-quality/quality_slop_case_study.md`.

## Verification

- [ ] Gate C passed
- [ ] Unbilled effort recorded honestly
- [ ] Revenue is collected, not invoiced
- [ ] The estimate-error series is updated — including on engagements that went well
- [ ] The divergence point names an actual moment and an actual decision
- [ ] The client verdict fed back into `config/practice.json`
- [ ] The asks were timed to visible value, sent separately, and gated on outstanding
      items
- [ ] Case-study consent is recorded, whichever way it went

## The loop closes here

Stage 9 feeds Stage 0. The rate floor consumes the overrun figure; the disqualifier
list consumes the client verdict; fixed-price eligibility consumes the variance. A
practice that runs Stage 9 every time gets better at quoting. One that runs it only
after bad engagements learns only about bad engagements.
