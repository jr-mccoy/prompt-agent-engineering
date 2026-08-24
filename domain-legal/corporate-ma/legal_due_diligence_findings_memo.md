---
title: "Due Diligence Findings Memo"
category: legal/corporate-ma
description: "Convert raw diligence findings into a buyer-ready memo: issues organized by severity tier, translated into deal impact (kill / reprice / indemnity / disclosure-only), with specific indemnity, escrow, special-indemnity, and R&W insurance recommendations keyed to each finding."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - m-and-a
  - corporate
  - due-diligence
  - findings-memo
  - indemnity
updated: "2026-05-11"
related_prompts:
  - domain-legal/corporate-ma/legal_due_diligence_request_list.md
  - domain-legal/corporate-ma/legal_disclosure_schedule_drafter.md
  - domain-legal/corporate-ma/legal_409a_or_qsbs_issue_spotter.md
  - domain-legal/research/legal_research_memo_irac.md
---

**Purpose:** Translate raw diligence findings into a decision document for the deal team: which findings kill the deal, which justify reprice, which need a special indemnity, and which are disclosure-only. Each finding ties to a specific reps-and-warranties section, a remedy, and an escrow/insurance recommendation.

**When to use:** End of buy-side diligence before final agreement markup; pre-signing risk meeting; R&W underwriter call prep; post-signing supplemental finding.

---

## Your Input

- **Deal structure:** [Asset / stock / forward merger / reverse triangular merger / 338(h)(10) / F-reorg]
- **Governing law:** [Default: Delaware]
- **Target state of formation/incorporation:** [State]
- **Industry:** [Industry — drives applicable regulatory frameworks]
- **Posture:** Buyer
- **Deal value and consideration mix:** [Cash / stock / rollover / earnout]
- **R&W insurance status:** [Bound / quoting / not pursuing — drives recommended escrow size and special indemnity structure]
- **Indemnity framework currently in draft:** [Cap %, basket type (deductible vs. tipping vs. first-dollar), basket amount, survival periods for general / fundamental / tax / IP / fraud, escrow %]
- **Findings to memorialize:** [List each finding with: source document, factual summary, applicable rep/covenant if known, estimated exposure, mitigation status]
- **Closing risk-allocation goals:** [E.g., walk away from cyber breach exposure; cap tax exposure via special indemnity; require pre-close consent procurement for top 5 customers]

---

## Constraints

**Must:**
- Tier every finding: **Critical** (deal-gating / walk-or-restructure), **High** (material reprice / special indemnity / escrow holdback), **Medium** (general indemnity / disclosure schedule), **Low** (disclosure-only / informational).
- Translate each finding into deal impact in one of four categories: **(1) Kill / restructure**, **(2) Reprice**, **(3) Indemnity** (general or special), **(4) Disclosure-only**.
- For every Critical and High finding, recommend specific risk-allocation mechanics: special indemnity, separate escrow tranche, R&W exclusion, pre-close covenant, walk-right, condition precedent, MAC trigger.
- Cite the specific rep, covenant, or schedule that the finding implicates.
- Specify dollar exposure (estimated range with methodology) or note "indeterminate" with the unknowns that would resolve it.
- Address survival period implications: fundamental rep survival (typically 6 years or statute of limitations), general rep survival (12–24 months typical), tax rep survival (statute of limitations + 60 days typical), IP rep survival (commonly extended).
- Note knowledge-qualifier and materiality-scrape implications (a knowledge qualifier shifts the risk; a materiality scrape reads materiality qualifiers out of the reps for damages calculation).
- Address sandbagging / anti-sandbagging treatment in the governing law (Delaware permits pro-sandbagging by default; some jurisdictions imply anti-sandbagging).
- For R&W insurance deals, identify expected underwriter exclusions and recommend special indemnities or seller carve-outs.

**Must Not:**
- Invent facts, exposure amounts, regulatory provisions, or case law. Use `[NEED: ...]` and `[CITE: ...]` placeholders.
- Bury Critical findings in the body — the executive summary leads with them.
- Recommend a generic "increase escrow" without sizing.
- Insert "consult counsel" disclaimers — this is the work product going to the deal team.
- Collapse multiple distinct findings into a single line item (each gets its own row).
- Conflate basket types (deductible baskets reduce dollar-one recovery; tipping baskets restore dollar-one recovery once exceeded).

---

## Instructions

1. **Executive summary.** Top 3–5 findings ranked by severity; recommended deal-team actions; total estimated exposure range; recommended escrow size delta vs. current draft.
2. **Methodology.** Documents reviewed (VDR index ranges), management interviews, third-party reports relied on, scope limitations.
3. **Findings by category** (Corporate, Cap Table, Material Contracts, IP, Employment & Benefits, Litigation, Regulatory & Compliance, Tax, Real Estate, Environmental, IT / Privacy / Cybersecurity, Insurance). Each finding contains:
   - Finding number and one-line title
   - Severity tier
   - Factual description with source citations to VDR
   - Implicated rep / covenant / schedule
   - Estimated exposure (range and methodology) or "indeterminate"
   - Deal impact category
   - Recommended risk allocation mechanic
   - Whether it is or should be R&W-insurance-covered or excluded
4. **Cross-cutting risk allocation summary table.** Pulls every special-indemnity recommendation, escrow holdback recommendation, walk-right, and pre-close covenant into one consolidated view.
5. **R&W insurance interaction.** Items likely to be underwriter-excluded; recommended seller carve-outs; recommended buyer-side specific indemnities.
6. **Open items.** Findings that remain indeterminate; what is needed to resolve.
7. **Recommended markup deltas.** Specific deltas to the draft Definitive Agreement: rep modifications, new covenants, new conditions, escrow size change, special-indemnity additions, materiality-scrape inclusion/exclusion, knowledge-qualifier scoping.

---

## Output Format

```markdown
# Due Diligence Findings Memo
**Project:** [CODE NAME]
**Target:** [TARGET]
**Buyer:** [BUYER]
**Deal Structure:** [Structure]   **Governing Law:** [State]
**Date:** [Date]   **Version:** [N]
**Privileged & Confidential — Attorney Work Product**

## Executive Summary
**Critical findings ([N]):**
1. [One-line summary] — recommendation: [kill / restructure / special indemnity / escrow holdback of $X / pre-close covenant]
2. [...]

**Total estimated indemnifiable exposure (point estimate / range):** $[Low] – $[High]
**Recommended escrow size delta vs. current draft:** [increase from X% to Y% / add separate tranche of $Z for tax / IP / cyber]
**Deal-team actions required before signing:** [list]

## Methodology and Scope
- VDR sections reviewed: [ranges]
- Management interviews: [list]
- Third-party reports relied on: [Phase I ESA, IP search, wage-and-hour audit, pen test]
- Scope limitations: [items not produced, redactions, clean-team restrictions]

## Findings

### 1. Corporate
| # | Finding | Tier | Implicated Rep | Exposure | Deal Impact | Recommendation |
|---|---|---|---|---|---|---|
| 1.1 | [Title] | Critical / High / Medium / Low | §3.X | $[range] | Kill / Reprice / Indemnity / Disclosure | [specific] |
{...}

### 2. Capitalization
{table}

### 3. Material Contracts
{table — flag change-of-control and anti-assignment triggers as Critical or High depending on revenue impact; consent procurement recommendations}

### 4. Intellectual Property
{table — chain-of-title gaps are typically High to Critical; recommend special indemnity uncapped or capped at purchase price for fundamental IP ownership}

### 5. Employment & Benefits
{table — §280G parachute exposure with gross-up risk; §409A operational and documentary failures; misclassification; restrictive-covenant enforceability by state}

### 6. Litigation
{table — pending matters scoped by exposure; threatened/demand letters; investigations}

### 7. Regulatory & Compliance
{table — FCPA, OFAC, ITAR/EAR, industry-specific; CFIUS interaction with closing condition if applicable}

### 8. Tax
{table — nexus exposure (post-Wayfair), §382 NOL limitation, transfer pricing, sales-and-use, R&D credit substantiation; if §338(h)(10) is on the table, S-corp validity is gating}

### 9. Real Estate
{table}

### 10. Environmental
{table — CERCLA successor / asset-deal liability framework}

### 11. IT / Privacy / Cybersecurity
{table — historical breach disclosure; pen-test findings; consent / DPA gaps; expected R&W exclusion}

### 12. Insurance
{table — coverage adequacy; D&O tail recommendation and sizing}

## Risk Allocation Summary (Consolidated)
| Finding | Tier | Special Indemnity? | Cap | Escrow Tranche | Survival | R&W Treatment |
|---|---|---|---|---|---|---|
| {short title} | Critical | Yes — uncapped or capped at PP | n/a or $X | Separate $Y tranche | Statute of limitations | Excluded — seller covers |
{...}

## R&W Insurance Interaction
**Expected underwriter exclusions:** [list with rationale — common: cyber breach pre-bind, wage-and-hour, NOL utilization, COVID-era exposures, pending litigation, specifically identified matters]
**Recommended seller-side special indemnities for excluded items:** [list with caps and survival]
**Buyer self-insurance gaps:** [areas where neither R&W nor seller indemnity covers]

## Open Items
| # | Item | Needed to Resolve | Owner | Target Date |
|---|---|---|---|---|

## Recommended Markup Deltas (Definitive Agreement)
1. [Rep §X.Y] — modify to remove knowledge qualifier on IP ownership (currently "Seller's knowledge"; recommend flat rep) — rationale: chain-of-title gaps identified.
2. [Indemnity §X.Y] — add special indemnity for [identified matter], uncapped, survival = statute of limitations, no basket.
3. [Escrow §X.Y] — increase from [X]% to [Y]%; add separate $[Z] tax tranche releasing on [date].
4. [Closing condition §X.Y] — add receipt of consents from [top N customers / top N suppliers] as condition to closing.
5. [Pre-close covenant §X.Y] — require seller to cure [identified item] before closing.
6. [Materiality scrape §X.Y] — confirm inclusion for damages calculation purposes; exclude for breach determination.
7. [Sandbagging §X.Y] — confirm pro-sandbagging language given Delaware governing law and identified findings.
```

---

## Verification

- [ ] Every finding is tiered (Critical / High / Medium / Low).
- [ ] Every finding ties to a specific rep, covenant, or schedule.
- [ ] Every Critical and High finding has a specific risk-allocation recommendation (not generic).
- [ ] Exposure estimates include methodology or are flagged "indeterminate" with resolution path.
- [ ] Executive summary leads with Critical findings and a total exposure range.
- [ ] Consolidated risk-allocation table reconciles to per-finding recommendations.
- [ ] R&W insurance exclusions identified with seller-side carve-out recommendations.
- [ ] Survival period and basket / cap interactions addressed.
- [ ] Sandbagging treatment under governing law addressed.
- [ ] No invented facts, exposure numbers, or citations; placeholders used.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| "Recommend increased escrow" without sizing | State the dollar amount or percentage delta and tie it to specific exposure |
| Treating all IP gaps as Medium | Chain-of-title gaps in fundamental IP are Critical for IP-heavy targets; recommend uncapped special indemnity |
| Recommending a special indemnity without survival | Specify survival period (statute of limitations is typical for tax and fundamental issues; 3–6 years common for IP) |
| Conflating fundamental and general reps for cap purposes | Fundamental reps (organization, authorization, capitalization, brokers, sometimes tax and IP) carry separate (usually 100% of purchase price) cap; general reps carry the negotiated cap (commonly 10–15% in non-R&W deals; lower with R&W) |
| Ignoring materiality scrape | If the agreement has a materiality scrape, "material" qualifiers in the reps are read out for damages calc — this materially changes loss calculation; address explicitly |
| Ignoring knowledge qualifier scope | A knowledge qualifier limits the rep to "knowledge of X officers after due inquiry" — identify whose knowledge is imputed; recommend removal where finding warrants |
| Treating cyber as R&W-covered | Cyber is almost always excluded or carved out by underwriters; recommend seller special indemnity for pre-close incidents and known vulnerabilities |
| Missing §280G gross-up exposure | If equity acceleration triggers parachute payments, §280G can create a 20% excise tax + lost deduction; quantify and recommend §280G cleansing vote or modification |
| Missing successor liability in asset deals | Successor liability still attaches in asset deals for environmental (CERCLA), product liability (de facto merger / continuity-of-enterprise), wage-and-hour (some states), tax (bulk sales) — address explicitly |
| Treating §1202 QSBS issues as seller's problem only | If buyer is paying with stock and seller intends to preserve QSBS, the QSBS holding period is tolled by the exchange unless §1202(h) tacking applies — buyer's structuring affects seller's after-tax economics and may affect price |
| Conflating basket types | Deductible basket = seller pays only above threshold; tipping basket = once threshold hit, dollar-one recovery; first-dollar / no basket = recovery from $1 |
| Recommending pro-sandbagging without checking governing law | Delaware default favors pro-sandbagging; if governing law is silent or contrary, draft express pro-sandbagging clause |
