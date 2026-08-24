---
title: "Negotiation Position Paper"
category: legal/contracts-transactional
description: "Internal posture memo with primary, fallback, and walkaway positions for each open issue, plus BATNA, leverage assessment, sequencing strategy, and trade-space analysis for cross-issue concessions."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - legal
  - contracts
  - negotiation
  - position-paper
  - batna
  - trade-space
updated: "2026-05-11"
related_prompts:
  - domain-legal/contracts-transactional/legal_contract_review_full_redline.md
  - domain-legal/contracts-transactional/legal_contract_clause_redline_targeted.md
  - domain-legal/contracts-transactional/legal_contract_risk_heatmap.md
  - domain-legal/research/legal_research_memo_irac.md
---

**Purpose:** Produce an **internal** position paper (not for sharing with the counterparty) that prepares the deal team for negotiation. For each open issue: primary position, defensible fallback, walkaway threshold, rationale, and trade value. Includes BATNA, leverage assessment, sequencing strategy, and a trade-space matrix showing which concessions in one area unlock movement in another. Sets internal authority boundaries so negotiators know what they can concede without re-approval.

**When to use:** Pre-negotiation kickoff; before each major round when positions need refresh; after a counterparty counterproposal that changes the trade space; escalation requests requiring CFO/CEO sign-off on a concession.

---

## Your Input

- **Deal context:** [Brief — parties, deal type, value, strategic importance]
- **Posture:** [Buyer / Supplier / etc.]
- **Governing law / state of formation:** [State]
- **Current contract draft or term sheet:** [Paste or reference]
- **Open issues identified:** [List, ideally from the heatmap or redline output]
- **Counterparty profile:** [Size, sophistication, prior dealings, in-house counsel quality, leverage]
- **Our BATNA:** [What we do if this deal does not close]
- **Their BATNA (estimated):** [What they do if this deal does not close]
- **Strategic value of deal:** [Revenue, market position, reference customer, distribution, regulatory]
- **Timeline pressure:** [Days to target close; consequences of delay]
- **Internal authority matrix:** [Who can approve LoL exceptions, indemnity exceptions, price concessions, etc.]
- **Known counterparty pressures:** [Their fiscal close, board approval, regulatory clock, competitive pressure]
- **Prior negotiation history on similar deals:** [Recent precedents on key issues]
- **Issues already pre-conceded by business:** [Things legal cannot reopen]

---

## Constraints

**Must:**
- For each open issue, define **three positions**: Primary (opener), Fallback (defensible mid-position), Walkaway (do-not-sign threshold).
- Tag each position with **rationale** (legal, commercial, strategic) and **trade value** (how much this issue is worth in concession terms).
- Identify **issues we will trade away** (low value to us, high value to them) and **issues we must hold** (high value to us regardless of trade).
- Build a **trade-space matrix**: which concessions unlock which counter-concessions.
- Identify **sequencing strategy**: which issues to raise first, which to hold for later rounds, which to bundle.
- Assess **leverage**: ours, theirs, and how it shifts over time (e.g., our leverage decreases as their fiscal close approaches; their leverage decreases as we get deeper into the partnership).
- Identify **authority boundaries**: what positions can the lead negotiator accept without re-approval; what requires escalation to whom.
- Identify **walkaway scenarios** with explicit triggers — not vague "if it gets bad enough" but specific issues × positions that would trigger a no-deal decision.
- Surface **counterparty's likely positions** and rationale based on profile.
- Identify **information asymmetries**: what we know they don't, and vice versa, and how to exploit / protect.

**Must Not:**
- Confuse the position paper with the redline. The position paper is internal strategy; the redline is what we send.
- Set walkaway thresholds that are not actually walkaways — the test is "would we genuinely not sign at this position?"
- Invent counterparty motivations without basis. Use `[INFER: ...]` for assumptions about their side.
- Provide generic disclaimers.
- Lock in positions that the business has already conceded or that contradict internal direction.
- Set fallback positions that are barely distinguishable from primary — fallbacks must be genuinely defensible mid-positions.
- Treat the BATNA assessment as throwaway. Position strength flows from BATNA.

---

## Position Ladder Schema

For each open issue:

| Field | Description |
|---|---|
| Issue ID | Cross-reference to heatmap / redline / TS-translator |
| Issue title | Plain-language name |
| Category | Indemnity / LoL / IP / termination / price / etc. |
| Current state | What the contract / counterparty currently says |
| Our value | Why this matters to us (legal, commercial, strategic) — High / Medium / Low |
| Their value (inferred) | Why this likely matters to them — High / Medium / Low |
| **Primary** | Opening position with specific language target |
| **Fallback** | Defensible mid-position with specific language target |
| **Walkaway** | Position at or below which we do not sign |
| Trade value | What this concession is worth (scale or relative) |
| Sequencing | Round 1 / 2 / 3 — bundle with which issues |
| Authority | Who can concede beyond Primary |
| Counterparty likely position | Inferred opener and fallback |

---

## Instructions

1. **Frame the deal.** Strategic context, timeline, BATNA both sides.
2. **List open issues.** Pull from heatmap / redline / TS translator. Deduplicate.
3. **Score our value and their value** per issue (High / Medium / Low).
4. **Build the position ladder** for each issue (Primary / Fallback / Walkaway).
5. **Identify trade pairs.** Where we have Low value × they have High value (give-away candidates); where we have High value × they have Low value (must-hold candidates); where both are High (real negotiation).
6. **Build the trade-space matrix.** Columns: things we want; rows: things they want; cells: trade possibilities.
7. **Sequence the issues.** Round 1 (anchor issues, easy give-aways); Round 2 (real negotiation); Round 3 (escalation/final).
8. **Set authority boundaries.** For each issue and position level, who can approve.
9. **Walkaway scenarios.** Specific issue × position combinations that trigger no-deal.
10. **Surface counterparty likely positions** and asymmetries.
11. **Risk register.** What could go wrong with this strategy and how to mitigate.

---

## Output Format

```markdown
# INTERNAL — Negotiation Position Paper — {Deal Name}
**Posture:** {posture}  |  **Lead Negotiator:** {name}  |  **Date:** {YYYY-MM-DD}

> CONFIDENTIAL — INTERNAL USE ONLY. Do not share with counterparty.

## 1. Deal Frame
- **Parties:** {names + posture}
- **Deal type and value:** {type, $$$}
- **Strategic importance:** {High / Medium / Low — rationale}
- **Target close:** {date}
- **Our BATNA:** {what happens if no deal}
- **Their BATNA (inferred):** {what likely happens if no deal — `[INFER: ...]`}
- **Our leverage:** {High / Medium / Low — sources: BATNA strength, alternatives, timing}
- **Their leverage:** {High / Medium / Low — same factors}
- **Leverage trajectory:** {how leverage shifts over the next __ days}

## 2. Pre-Conceded Items (Do Not Reopen)
- {Item} — conceded by {role} on {date} because {rationale}
- {Item} — outside scope of legal authority; commercial team owns

## 3. Position Ladder by Issue

### OI-001 — {Issue Title}
- **Category:** {Indemnity / LoL / IP / etc.}
- **Section reference:** {§}
- **Current state:** "{quote or summary}"
- **Our value:** High — {2–3 sentence rationale}
- **Their value (inferred):** Medium — {2–3 sentence rationale, with `[INFER: ...]`}
- **Primary:** {specific language target + rationale}
- **Fallback:** {specific language target + rationale}
- **Walkaway:** {position at or below which we do not sign + rationale}
- **Trade value:** {High / Medium / Low — what we'd give to get vs what we'd give up}
- **Sequencing:** {Round 1 / 2 / 3; bundle with OI-XXX}
- **Authority to concede beyond Primary:** {role}
- **Counterparty likely position:** Opener = {...}; Fallback = {...}

### OI-002 — {Issue Title}
{...}

{Continue through all open issues}

## 4. Trade-Space Matrix

|  | We want: LoL cap up | We want: IP indemnity broad | We want: Audit rights | We want: 30-day TFC |
|---|---|---|---|---|
| They want: Auto-renewal yes | Trade unlocked | — | — | — |
| They want: Residuals clause | — | Trade unlocked | — | — |
| They want: Caps on warranties | — | — | Trade unlocked | — |
| They want: Wind-down fees | — | — | — | Trade unlocked |

Cells marked "Trade unlocked" indicate a viable bilateral concession pair.

## 5. Sequencing Strategy

### Round 1 — Anchors and Easy Give-Aways
- Open hard on: {OI-001, OI-003, OI-007}
- Concede early (build goodwill): {OI-012, OI-015}
- Why: {rationale}

### Round 2 — Real Negotiation
- Trade {OI-002 fallback} for {their concession on OI-X}
- Hold firm on {OI-005} — walkaway issue
- Why: {rationale}

### Round 3 — Final and Escalation
- Reserve for: pricing, indemnity cap, termination assistance
- Escalation: anything below fallback requires {role} approval

## 6. Authority Matrix
| Issue | Lead negotiator authority | Escalation owner |
|---|---|---|
| LoL cap | Primary or Fallback | CFO for below Fallback |
| Indemnity scope | Primary only | GC for any change |
| Price concession | Within 3% | CFO above 3%, CEO above 10% |
| Term length | Per primary | GM for variance |
| Data protection / DPA | Primary only | CISO + Privacy |
| ... | | |

## 7. Walkaway Scenarios
1. **Walkaway 1:** Counterparty refuses to cap data-breach exposure below uninsurable threshold AND refuses adequate carve-out. Trigger: review by {role} within 24 hours.
2. **Walkaway 2:** Counterparty demands perpetual license to customer data. Trigger: hard stop.
3. **Walkaway 3:** Counterparty insists on assignment to competitors without consent. Trigger: hard stop.

## 8. Counterparty Profile Notes
- **Sophistication:** {senior in-house counsel; uses outside counsel for complex deals; etc.}
- **Prior dealings:** {brief history if any}
- **Inferred pressures:** {fiscal close in __; board approval needed; competitive deal in flight}
- **Known pet issues:** {clauses they always insist on}
- **Soft spots:** {clauses they typically concede}

## 9. Information Asymmetries
| What we know they don't | Use case |
|---|---|
| {Our walk-away is firm because BATNA is __} | Do not signal; preserve credibility of walk-away |
| {Their fiscal close is in __ days} | Pace negotiation to compress decision pressure on them |

| What they know we don't | Risk |
|---|---|
| {Their internal price authority} | Could refuse to escalate when they have authority to concede |

## 10. Risk Register
- **Risk:** Counterparty hardens after initial concession → counter: position concession as conditional on package
- **Risk:** Their lead leaves mid-negotiation → counter: document handoff items
- **Risk:** Our champion departs → counter: brief next-up so deal not dependent on individual
- **Risk:** Regulatory change before close → counter: include change-of-law clause and define materiality
```

---

## Verification

- [ ] Every open issue has Primary / Fallback / Walkaway with specific language targets.
- [ ] Our value × Their value scored for each issue (High / Medium / Low).
- [ ] Trade pairs identified (Low × High = give-away; High × Low = hold).
- [ ] Trade-space matrix shows bilateral concession options.
- [ ] Sequencing strategy assigns issues to rounds.
- [ ] Authority matrix specifies who approves what.
- [ ] Walkaway scenarios are specific, not vague.
- [ ] BATNA assessed for both sides; leverage scored.
- [ ] Counterparty profile and inferred pressures documented.
- [ ] No invented counterparty motivations beyond `[INFER: ...]` flags.
- [ ] Pre-conceded items listed and not reopened.
- [ ] Document marked CONFIDENTIAL — INTERNAL USE ONLY at top.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Walkaway thresholds that are not actually walkaways | Test each: would we genuinely refuse to sign? If "we'd push back hard but sign," it's a Fallback, not Walkaway |
| Fallback positions indistinguishable from Primary | Fallback must be genuinely defensible mid-position with meaningful concession; otherwise it is window dressing |
| Trade-space matrix with no trade pairs | If everything is High × High, return to value scoring; some issues must be tradeable for negotiation to function |
| Skipping the BATNA assessment | Position strength flows from BATNA; without honest BATNA assessment, the position paper rests on wishful thinking |
| Treating counterparty as monolithic | Different counterparty stakeholders (in-house counsel, business sponsor, CFO) have different positions; surface |
| Authority matrix that requires escalation for everything | If lead negotiator has no authority, they cannot negotiate; calibrate to balance speed and control |
| Sequencing that opens on walkaway issues | Round 1 should anchor and trade easy items; opening on walkaway burns leverage |
| Sharing the position paper with counterparty | This is an internal document; if shared, it surrenders all positional information |
| Counterparty profile based on stereotype rather than evidence | Use `[INFER: ...]` flags and update as actual behavior is observed |
| Risk register treated as compliance exercise | Each risk should have an actual mitigation, not "monitor" |
| Pre-conceded items reopened by legal in the draft | Once business has conceded, legal documents the concession and does not reopen unless authorized |
| Failing to document leverage trajectory | Leverage shifts over time (fiscal closes, competitive deals, regulatory clocks); plan for shifts, do not assume static |
