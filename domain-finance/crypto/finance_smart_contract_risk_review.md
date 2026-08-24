---
title: "Smart-Contract & Protocol Risk Review — Audit, Admin Keys, Upgradeability, Dependencies"
category: finance/crypto
description: "Assess the non-market risk of holding or interacting with a token/protocol: audit status and history, admin-key and upgradeability powers, oracle and bridge dependencies, custody model, and concentration/governance attack surface — as an investment risk review, not a security exploitation guide. Produces a ranked risk profile with severity, evidence, and a go/size-down/avoid read."
techniques:
  - QA-02
  - DS-02
  - RT-06
  - NE-10
  - QA-04
difficulty: advanced
tags:
  - smart-contract-risk
  - protocol-risk
  - admin-keys
  - upgradeability
  - oracle-bridge-risk
  - crypto
updated: "2026-06-18"
related_prompts:
  - domain-finance/crypto/finance_token_valuation_framework.md
  - domain-finance/crypto/finance_onchain_metrics_analysis.md
  - domain-finance/risk-management/finance_counterparty_risk_assessment.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice and not a security audit. This is an investment risk review, not an exploitation guide; a clean review does not mean a protocol is safe. All outputs require independent verification, including a professional smart-contract audit, before any capital is committed.**

## Objective

Characterize the technical and governance risk of holding a token or depositing into a protocol,
from an investor's standpoint. The deliverable is a ranked risk profile across the surfaces that
most often cause total or severe loss in crypto — admin-key control, upgradeable code, oracle and
bridge dependencies, custody assumptions, and holder/governance concentration — each with a
severity, the supporting evidence (or a queued gap), and a clear go / size-down / avoid read.
This is a *risk* review: it identifies and ranks exposure; it does not probe for or weaponize
exploits.

## When to Use

- Building the protocol-risk section of a Stage 2 crypto dossier
- Deciding whether a token's technical/governance risk warrants a smaller position or avoidance
- Comparing two protocols on non-market risk
- Re-reviewing after a contract upgrade, governance change, or dependency change

## Inputs / Context Required

**Code & audit posture**
- Audit history (who, when, scope, findings resolved); bug-bounty presence; time-in-production
- Open-source vs. closed; verified contracts on-chain

**Control & upgradeability**
- Admin/owner keys and their powers (pause, mint, upgrade, drain, parameter changes)
- Multisig threshold and signer set; timelock presence/length; proxy/upgradeability pattern

**Dependencies**
- Oracle design (source, manipulation resistance); bridge exposure; external protocol/composability
  dependencies; stablecoin/collateral assumptions

**Custody & concentration**
- Custody model (self-custody vs. exchange vs. protocol-held); holder/governance concentration
  (link to `finance_onchain_metrics_analysis.md`)
- Any unavailable input → mark `UNAVAILABLE` and queue (DS-02)

## Constraints

### Must
- Treat this as an investment risk review; identify and rank exposure without providing exploit
  steps or attack tooling (QA-02).
- Assess admin-key/upgradeability powers explicitly — what can a privileged actor do to holders,
  and what controls (timelock, multisig) constrain it (DS-02).
- Map external dependencies (oracle, bridge, composability) since these are common loss vectors
  (RT-06).
- Rank risks by severity and translate the profile into a position-level read (go / size-down /
  avoid), reflecting that tail risk can be total loss (NE-10).
- Mark `UNAVAILABLE` evidence and treat an unverifiable control as a risk, not a pass (QA-04).

### Must Not
- Provide exploitation instructions, proof-of-concept attacks, or vulnerability-weaponization.
- Treat the existence of an audit as proof of safety (note scope, date, and unresolved findings).
- Assume a multisig/timelock exists or functions without evidence.
- Ignore dependency risk because the core contract "looks fine."
- Invent audit findings, key powers, or signer sets — queue unknowns (DS-02).

## Instructions

1. **Audit & maturity posture (DS-02).** Summarize audits (scope, date, resolution), bounty, time
   in production, and open-source/verification status. An audit is evidence, not a guarantee —
   note what it did *not* cover.

2. **Privilege & upgradeability (QA-02).** Enumerate admin/owner powers (pause, mint, upgrade,
   drain, parameter changes) and the controls on them (multisig threshold, timelock length, proxy
   pattern). Assess worst-case privileged action against holders — descriptively, not as a recipe.

3. **Dependency map (RT-06).** Identify oracle, bridge, collateral, and composability dependencies;
   for each, state the failure mode and how it would hit holders. Cross-read concentration data
   from the on-chain analysis for governance-capture/dump risk.

4. **Custody & concentration.** State the custody model and its trust assumptions; quantify holder
   and governance concentration and the resulting attack/dump surface.

5. **Rank and translate (NE-10, QA-04).** Produce a severity-ranked risk list; for each, give
   severity, likelihood qualifier, and evidence (or queued gap). Convert the profile into a
   position-level read, noting where tail risk is total loss. Flag unverifiable controls as risks.

## Output Format

```
## PROTOCOL RISK REVIEW: <PROTOCOL/TOKEN> | as_of [date] | Read: [GO / SIZE-DOWN / AVOID]
```

### Posture summary
| Surface | Finding | Evidence / status |
|---|---|---|
| Audit history & scope | … | … |
| Open-source / verified | … | … |
| Time in production | … | … |

### Privilege & upgradeability
| Power | Who holds it | Control (multisig/timelock) | Worst-case to holders |
|---|---|---|---|

### Dependency & custody risk
| Dependency | Failure mode | Impact on holders |
|---|---|---|
| Oracle | … | … |
| Bridge | … | … |
| Custody model | … | … |

### Ranked risk profile
| Rank | Risk | Severity | Likelihood | Evidence (or queued) |
|---|---|---|---|---|

### Position read & open items
- Read: [GO / SIZE-DOWN / AVOID] + rationale (note total-loss tail risks)
- `UNAVAILABLE` evidence treated as risk: [list / queued]

## Verification

- [ ] Framed as an investment risk review; no exploit steps or attack tooling provided.
- [ ] Admin-key/upgradeability powers and their controls are enumerated.
- [ ] Oracle/bridge/composability/custody dependencies are mapped with failure modes.
- [ ] Risks ranked by severity and translated into a position-level read.
- [ ] Audit treated as scoped evidence, not a safety guarantee.
- [ ] Unverifiable controls flagged as risk; missing evidence queued, not invented.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| "Audited, therefore safe" | Note audit scope/date/unresolved findings; audit ≠ guarantee |
| Assuming a timelock/multisig constrains admin power | Require evidence of threshold + timelock; absence = risk (QA-02) |
| Core contract "fine" so protocol deemed safe | Mandatory dependency map (oracle/bridge/composability) (RT-06) |
| Concentration ignored | Quantify holder/governance concentration; dump/capture risk surfaced |
| Severe-but-rare risk understated | Severity ranking notes total-loss tails (NE-10) |
| Missing control assumed present | `UNAVAILABLE` → treated as risk, queued (DS-02, QA-04) |
| Review drifts into exploitation | Risk-only framing; no PoC/attack instructions |
