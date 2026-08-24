---
title: "Severity Scoring & Business Impact"
category: bug-bounty/reporting
description: "Score a validated finding with CVSS (v3.1/v4) and articulate concrete business impact so the report lands in the right payout tier without over- or under-claiming"
techniques:
  - ST-01
  - DS-01
  - RT-05
  - DS-06
  - DD-07
difficulty: intermediate
tags:
  - bug-bounty
  - cvss
  - severity
  - impact
  - payout
updated: "2026-06-18"
related_prompts:
  - domain-software-engineering/bug-bounty/bugbounty_finding_triage_validation.md
  - domain-software-engineering/bug-bounty/bugbounty_disclosure_report_writer.md
  - domain-software-engineering/bug-bounty/bugbounty_poc_builder.md
---

# Severity Scoring & Business Impact

**Objective:** Assign a defensible CVSS score and a clear business-impact narrative to a validated finding, so triage tiers it correctly — the difference between a Low and a High payout is usually impact articulation, not the bug itself.

## When to Use
- A finding has passed triage and you're preparing the report.
- The program scores by CVSS (or you want a defensible baseline) and you want to get the vector right.
- You suspect a finding is worth more than it looks and want to articulate the realistic impact.

## Inputs / Context
- **The validated finding** (type, affected asset, what you proved).
- **The program's severity basis** (CVSS v3.1, v4, or program-specific tiers) and reward table.
- **Context** that affects impact: data sensitivity, user base, privilege required, scope of effect.

## Instructions

1. **Restate what was actually proven** (not what's theoretically possible) — this is the floor of your score. Then separately note demonstrable escalation potential.

2. **Build the CVSS vector metric-by-metric**, justifying each from evidence:
   - Attack Vector, Attack Complexity, Privileges Required, User Interaction.
   - Scope (changed?), Confidentiality / Integrity / Availability impact.
   - Use the program's version (v3.1 or v4); if unspecified, give v3.1 and note v4 if materially different.

3. **Compute the base score and severity band**, and show the vector string so triage can verify it.

4. **Write the business-impact narrative:** translate the vector into what it means for the company — whose data, how many users, what an attacker gains, why it matters beyond the technical mechanics. This is what moves tiers.

5. **State realistic escalation** (with evidence or clear reasoning): chaining potential, blast radius, and whether the proven minimal PoC under-represents true impact. Be honest — overclaiming gets findings down-tiered and hurts your reputation.

6. **Calibrate against the program's reward table** to set an expectation (not a demand), and note where the program's tiering might differ from raw CVSS.

7. **CRITICAL — verify the score is defensible:**
   - Confirm each CVSS metric is justified by what you actually demonstrated, not the worst-case fantasy.
   - Confirm the impact narrative doesn't claim effects you didn't prove (mark proven vs. potential).
   - Check the score against the proven PoC: if you only proved reachability, don't score full compromise.
   - Note assumptions (e.g., "if metadata creds are extractable") explicitly rather than baking them silently into the score.

## False-Positive Prevention (MUST follow)
- ❌ Do NOT inflate CVSS metrics beyond what the PoC demonstrates (e.g., scoring full Confidentiality:High from a single-record read without showing broader reach).
- ❌ Do NOT claim Scope:Changed or Availability impact without evidence.
- ❌ Do NOT present escalation potential as if it were proven — separate "demonstrated" from "potential."
- ❌ Do NOT anchor on the program's max payout; anchor on the evidence.
- ✅ DO justify every metric from the demonstrated PoC.
- ✅ DO separate proven impact from realistic-but-unproven escalation.
- ✅ DO calibrate expectations to the program's actual tiers.

## Output Format
```
## What Was Proven (floor)
[Concise statement of the demonstrated effect]

## CVSS Vector (program version)
| Metric | Value | Justification (from evidence) |
- Vector string: CVSS:3.1/AV:.../...
- Base score: X.X (Severity band)

## Business Impact Narrative
[2-4 sentences: whose data/money/trust, scale, why it matters]

## Escalation: Proven vs. Potential
- Proven: ...
- Potential (reasoning): ...

## Expected Tier (calibrated, not demanded)
[Likely band per program table + caveats]

## Self-Audit
[Every metric tied to evidence; potential separated from proven]
```

## Example Output
```
## What Was Proven (floor)
Any authenticated user can read any other user's order (PII: name, address, items) via IDOR on
GET /v1/orders/{id}. Demonstrated cross-account read between my two test accounts.

## CVSS Vector (v3.1)
| Metric | Value | Justification |
|--------|-------|---------------|
| AV | Network | exploitable over the internet via the API |
| AC | Low | trivial: change an ID |
| PR | Low | requires an authenticated (any) account |
| UI | None | no victim interaction |
| Scope | Unchanged | stays within the app's authz context |
| C | High | full read of other users' order PII across the base |
| I | None | read-only on this endpoint |
| A | None | no availability effect |
- Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- Base score: 6.5 (Medium)

## Business Impact Narrative
An attacker with any free account can enumerate order IDs and harvest the personal and shipping data of
the entire customer base — a mass-PII exposure with privacy/regulatory consequences and clear reputational
harm. The barrier is a single incrementable identifier.

## Escalation: Proven vs. Potential
- Proven: cross-account read of one other account's full order (my account B).
- Potential: bulk enumeration across all users (IDs appear iterable) — not performed; would raise the
  practical severity even though CVSS C is already High.

## Expected Tier (calibrated)
Likely High by program tiering despite the 6.5 base, because programs weight mass-PII IDOR heavily.
Caveat: if IDs were unguessable, practical severity would drop — here they are sequential.

## Self-Audit
Each metric maps to the demonstrated read; C:High justified by the data class and iterable IDs (noting
bulk read was not performed); escalation kept in the "potential" column.
```

## Techniques Used
- **ST-01 (Clear Objective Statement)** — a defensible score plus impact narrative, not a guess.
- **DS-01 (Framework Application)** — applies the CVSS metric framework rigorously.
- **RT-05 (Evidence-Based Reasoning)** — every metric is justified from the demonstrated PoC.
- **DS-06 (Prioritization Guidance)** — calibrates expected tier against the program's reward table.
- **DD-07 (Self-Audit Table)** — verification separates proven impact from potential escalation.
