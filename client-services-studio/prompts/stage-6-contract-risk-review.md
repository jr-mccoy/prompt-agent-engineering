# Stage 6 — Contract Risk Review

**Gate B — signature risk cleared.** Code-enforced. No engagement is marked closeable
while unresolved red-flag clauses remain.

**Input:** the contract, and a summary you extract from it · **Output:** a Gate B
result and a negotiating position

---

## Purpose

Catch the clause structures that lose money quietly. Gate B is a structural scan over
a summary **you** produce by reading the contract; it is not a contract reader and
does not replace counsel. Its job is to stop known-bad structures reaching signature
unnoticed.

## Boundaries — read first

- **Not legal advice.** Nothing here tells you what a clause means, whether it is
  enforceable, or what your jurisdiction does with it.
- **Counsel review is a gate condition.** `counsel_reviewed: false` is itself a
  high-severity finding. The scan passing is not a substitute for a lawyer.
- The scan reads a structured summary. Garbage in, confident garbage out.

## Procedure

### 1. Extract the contract summary

Read the contract and fill in the `contract` block. The fields and what each means
are in `skills/proposal-assembler/references/red-flags.md`.

For the clause-level analysis that produces these answers, use the existing legal
prompts rather than reasoning from scratch — they are vendored under
`referenced-prompts/`:

| Area | Prompt |
|---|---|
| Liability, IP, indemnity, warranties, termination | `domain-legal/contracts-transactional/legal_contract_clause_redline_targeted.md` |
| Payment terms, late fees, suspension, set-off, retainage | `domain-legal/contracts-transactional/legal_payment_terms_and_late_fee_review.md` |
| Termination economics — kill fee, notice, WIP, transition | `domain-legal/contracts-transactional/legal_termination_economics_provider_side.md` |
| Flow-down, where you subcontract | `domain-legal/contracts-transactional/legal_subcontractor_flow_down_check.md` |
| Full redline | `domain-legal/contracts-transactional/legal_contract_review_full_redline.md` |
| Scoring everything together | `domain-legal/contracts-transactional/legal_contract_risk_heatmap.md` |

### 2. Run the gate

```bash
python3 skills/proposal-assembler/scripts/assemble.py --gateB <engagement.json>
```

Ten flags at three severities. Critical and high block; medium warns.

### 3. Work the findings

For each blocking finding, one of three outcomes:

| Outcome | Meaning |
|---|---|
| **Negotiate it out** | Default. Use the position ladders from the legal prompts |
| **Accept with a recorded rationale** | Carried deliberately, with a name on it |
| **Walk away** | The clause exceeds what the engagement earns |

Acceptance requires a written rationale:

```json
"accepted_risks": [
  { "flag": "payment_terms_long", "rationale": "offset by a 40% deposit" }
]
```

An entry without a rationale does not unblock. The mechanism exists so that carrying
a known risk is a decision rather than an oversight.

### 4. Rank the asks by resistance, not importance

Counterparties concede unevenly. In most services agreements:

| Ask | Value | Resistance |
|---|---|---|
| Payment for work performed to termination, pro-rated | high | low |
| Transition assistance at standard rates, capped | high | low |
| Undisputed portion payable during a dispute | medium | low |
| Set-off limited to admitted sums | high | low |
| Right to suspend for non-payment | medium | low |
| Recovery of committed third-party costs | medium | low |
| Liability cap at a defined multiple | high | moderate |
| Longer notice period | moderate | moderate |
| Kill fee | high | high |

Leading with the kill fee is the common error. Items at the top are frequently
conceded without argument and often recover more.

### 5. Take it to counsel

Gate B passing means no known-bad structure is present unexamined. It does not mean
the contract is safe. Send it, with your questions listed, and record the review.

## Verification

- [ ] The summary was extracted by reading the contract, not guessed
- [ ] The gate was run
- [ ] Every blocking finding was negotiated, accepted with a rationale, or caused a
      walk-away
- [ ] Medium findings were read, not skipped
- [ ] Asks were ranked by resistance
- [ ] A lawyer reviewed it and `counsel_reviewed` is true
- [ ] Where you subcontract, the flow-down check was run separately
