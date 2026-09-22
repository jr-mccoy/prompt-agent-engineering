# Stage 5 — Proposal and SOW

**Gate: none here.** Gate A has passed; Gate B follows in Stage 6.

**Input:** the complete engagement record · **Output:** a proposal, and SOW input

---

## Purpose

Produce the document the client says yes to — and make it the same document that
governs delivery. A proposal whose scope language is persuasive rather than precise
creates the dispute it was meant to prevent.

## Procedure

### 1. Render from the record

```bash
python3 skills/proposal-assembler/scripts/assemble.py --render <engagement.json>
```

This produces the skeleton with every section populated from the record, plus the
proposal → SOW correspondence table. Rendering rather than writing freehand is what
guarantees the correspondence: the accepted document and the governing document come
from one source.

### 2. Write the prose the renderer cannot

The renderer places facts. Three sections need you:

- **The problem as we understand it** — in the client's words from the discovery
  record, with their metric names and their terminology. Do not translate into your
  framework. A proposal opening with your credentials is skimmed.
- **What success looks like** — the changed state, measurable where possible.
- **Objection pre-emption** — the two or three objections discovery told you will
  actually be raised. Two real ones beat six generic ones.

**Run `domain-professional-writing/business-writing/business_writing_client_engagement_proposal.md`**
for the full method. It owns the writing; this stage owns the mechanics.

### 3. Keep the exclusions in the body

Exclusions belong in the proposal, not only in attached terms. The conversation about
what is out happens either now, cheaply, or in week six, expensively. Write them
without defensiveness — "implementation is not included; we can quote separately" is
a sentence that sells a second engagement.

### 4. Draft the SOW from the same record

The correspondence table maps each proposal section to its SOW section. Deliverable
and acceptance language should transfer **verbatim** — if it has to be rewritten to
be contractual, it was not precise enough for the proposal either.

Hand off to `domain-legal/contracts-transactional/legal_sow_drafter.md` for the
contractual form, and `legal_msa_drafter.md` where no master agreement exists.

### 5. Gate the draft

```
domain-professional-writing/content-quality/quality_slop_client_deliverable.md
```

Run it before sending. It returns ACCEPT / REVISE / REJECT.

### 6. Keep it short

Two to four pages of body. Methodology, credentials and case studies go in an
appendix the decision-maker need not read. Length correlates negatively with
acceptance.

## Orchestrated resources

| For | Use |
|---|---|
| The proposal method | `domain-professional-writing/business-writing/business_writing_client_engagement_proposal.md` |
| Executive-audience structure | `domain-professional-writing/field_guide.md` |
| Supporting collateral | `domain-agentic-resources/skills/marketing/sales-enablement/` |
| The SOW | `domain-legal/contracts-transactional/legal_sow_drafter.md` |
| Quality gate | `domain-professional-writing/content-quality/quality_slop_client_deliverable.md` |
| Where the numbers came from | `domain-negotiation/preparation/negotiation_opening_offer_design.md` |

## Verification

- [ ] Rendered from the record, not written freehand
- [ ] The opening uses the client's words
- [ ] Exclusions appear in the body
- [ ] Every acceptance criterion transfers to the SOW verbatim
- [ ] Two or three real objections are addressed
- [ ] The next step names an action, a person and a date
- [ ] Body under four pages
- [ ] Passed the client-deliverable quality gate

## Boundaries

Not legal advice. The rendered output is a proposal and SOW input, not a contract.
Have a lawyer review before signature — Gate B in Stage 6 treats the absence of that
review as a finding.
