---
title: "RAI EU AI Act Compliance Assessment"
category: AI-ML/responsible-ai-governance
description: "Assess an AI system against the EU AI Act's risk-based structure and obligations, with the user confirming the classification and without inventing article text or specific legal thresholds."
techniques:
  - DS-01
  - ST-02
  - CM-02
  - QA-12
  - DS-06
difficulty: advanced
tags:
  - eu-ai-act
  - regulatory-compliance
  - risk-classification
  - high-risk-obligations
  - responsible-ai
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/responsible-ai-governance/rai_governance_framework_design.md
  - domain-AI-ML/responsible-ai-governance/rai_model_risk_assessment.md
  - domain-AI-ML/responsible-ai-governance/rai_model_card_authoring.md
---

# RAI EU AI Act Compliance Assessment

**Objective:** Assess an AI system against the EU AI Act's risk-based structure — determining a *candidate* risk classification, mapping the obligation areas that follow, and identifying gaps — while requiring the user (and qualified legal counsel) to confirm the classification and without inventing article numbers, statutory text, or specific legal thresholds.

**When to Use:**
- When a system may be placed on the EU market or affect people in the EU and you need a structured first-pass assessment.
- To prepare materials for legal review of EU AI Act exposure.
- To map existing documentation onto the Act's obligation areas.

**When NOT to Use:**
- As a substitute for qualified legal advice — this is a structured pre-assessment, not a legal opinion.
- For non-EU regulatory regimes — ask the user which regulation applies and use the appropriate analysis.

## Inputs / Context

- **System description** — purpose, who it affects, the domain (e.g., employment, credit, biometrics, safety component).
- **Deployment context** — provider vs deployer role; whether placed on the EU market or used by EU-based people.
- **Autonomy & human oversight** — degree of automation in consequential decisions.
- **Existing documentation** — model cards, risk assessments, data governance, logging.
- **User-confirmed classification** — the candidate risk category the user/legal believes applies (ask; do not assert).

## Constraints

**Must:**
- Treat the risk classification as a *candidate to confirm*, not a determination — explicitly ask the user/legal to confirm it.
- Describe obligation *areas* (e.g., risk management, data governance, transparency, human oversight, record-keeping, accuracy/robustness) in general terms tied to the Act's structure.
- Distinguish what is documented/evidenced from what is missing.

**Must Not:**
- Invent or quote specific article numbers, annex contents, exact dates, or numeric thresholds; if a specific provision is needed, say it must be verified against the official text.
- Declare the system "compliant" or "non-compliant" — produce a gap assessment and route conclusions to legal.
- Assume the Act applies; confirm EU nexus with the user first.

**Instructions:**

1. **Confirm applicability and role.** Establish whether the system has an EU nexus and whether the organization is acting as provider or deployer. If unclear, mark as an open legal question.

2. **Derive a candidate risk classification.** Based on purpose and domain, propose the likely category (prohibited / high-risk / limited-risk transparency / minimal) as a *candidate*, and explicitly ask the user/legal to confirm. Do not cite specific annex listings from memory.

3. **Map obligation areas to the candidate class.** For the candidate class, list the general obligation areas that typically attach (risk management system, data governance, technical documentation, record-keeping/logging, transparency to users, human oversight, accuracy/robustness/cybersecurity, post-market monitoring) — described generically, not quoted.

4. **Assess current evidence per obligation area.** For each area, state what documentation/controls exist (cite the user's inputs) and what is missing.

5. **Identify gaps and rank them.** Rank gaps by likely significance and effort, marking which require legal interpretation.

6. **Flag transparency and oversight specifics.** Note where user-facing AI disclosure and meaningful human oversight obligations likely apply, as areas to verify.

7. **Produce a legal-handoff package.** Summarize the candidate classification, evidence, and gaps in a form a lawyer can verify against the official text.

**Output Format:**

A markdown pre-assessment:
- **Applicability & Role** — EU nexus, provider/deployer, open questions.
- **Candidate Risk Classification** — proposed category + explicit "confirm with legal" note.
- **Obligation-Area Gap Table** — Area | Typically requires (general) | Evidence present | Gap | Needs legal interpretation?
- **Ranked Gaps** — significance × effort.
- **Transparency & Oversight Notes**.
- **Legal Handoff Summary** — what to verify against the official text.
- **INSUFFICIENT EVIDENCE** — the correct state of the candidate risk classification whenever the deployment facts that determine it are unsettled. Every downstream obligation depends on the category, so a provisional classification silently propagates into the whole gap table. Name the unblocking datum: the specific deployment facts, and confirmation against the official text by counsel.

## Verification

- [ ] EU applicability and provider/deployer role are addressed (or flagged open).
- [ ] The risk classification is presented as a candidate to confirm, not a determination.
- [ ] No specific article numbers, annex text, dates, or numeric thresholds are invented.
- [ ] Each obligation area separates evidence-present from gap.
- [ ] No "compliant/non-compliant" verdict is issued.
- [ ] A legal-handoff summary routes conclusions to qualified counsel.
- [ ] The risk classification is marked INSUFFICIENT EVIDENCE where the determining deployment facts are unsettled, and the gap table states that its obligations are conditional on that classification.

## False-Positive Prevention

❌ **DON'T:**
- Quote "Article X requires Y" from memory — article text and numbering must be verified against the official source.
- Declare a system "high-risk" or "compliant" without legal confirmation.
- Assume the Act applies because the system uses AI — confirm the EU nexus.
- Invent a numeric accuracy or logging-retention threshold.

✅ **DO:**
- Present the classification as a candidate and route it to legal.
- Describe obligation areas generically and tie specifics to verification against the official text.
- Confirm applicability before assessing obligations.
- Mark every point needing legal interpretation.

## Example Output

```markdown
## EU AI Act Pre-Assessment: Automated CV-Screening Tool

### Applicability & Role
EU nexus: yes (used by EU employers). Role: provider (we build and place it on the market). Open: whether a specific deployer obligation also attaches.

### Candidate Risk Classification
Candidate: **high-risk** (employment/recruitment context tends to fall in scope). CONFIRM WITH LEGAL against the official text — classification is not asserted here.

### Obligation-Area Gap Table
| Area (general) | Typically requires | Evidence present | Gap | Needs legal? |
|---|---|---|---|---|
| Risk management system | Ongoing risk process | Partial (model risk assessment exists) | Lifecycle process not formalized | No |
| Data governance | Data quality/representativeness controls | Model card documents gaps | APAC-equivalent underrepresentation unaddressed | Some |
| Technical documentation | Comprehensive system docs | Model card v1.3 | Full tech file incomplete | Yes |
| Record-keeping/logging | Event logging | Inference logs exist | Retention policy unconfirmed | Yes |
| Transparency to users | Inform affected people | None | Candidate disclosure missing | Yes |
| Human oversight | Meaningful oversight | Human override exists | Oversight design not documented | Yes |
| Accuracy/robustness/security | Validated performance | Eval + per-group metrics | Robustness/adversarial testing missing | No |

### Ranked Gaps
1. Transparency/disclosure (high significance, moderate effort) — likely required.
2. Full technical documentation file (high, high) — needs legal scoping.

### Transparency & Oversight Notes
Affected candidates likely must be informed; oversight must be meaningful, not nominal — verify.

### Legal Handoff Summary
Candidate high-risk; gaps above; counsel to confirm classification and exact obligations against the official text.
```

**Techniques Used:**
- **DS-01 (Framework Application):** structures against the Act's risk-based obligation areas.
- **ST-02 (Structured Sequential Instructions):** applicability → classify → obligations → gaps → handoff.
- **CM-02 (Constraint Specification):** the no-invented-legal-text constraint governs the analysis.
- **QA-12 (False Positives Identification):** prevents fabricated articles and premature compliant/non-compliant verdicts.
- **DS-06 (Prioritization & Severity Guidance):** ranks gaps by significance and effort.

**Related Prompts:**
- `rai_governance_framework_design.md` — embed classification into internal risk tiers.
- `rai_model_risk_assessment.md` — the risk assessment feeding the risk-management obligation.
- `rai_model_card_authoring.md` — supplies technical documentation evidence.
