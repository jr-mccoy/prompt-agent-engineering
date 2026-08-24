---
title: "Internal AI Use Policy Authoring"
category: AI-ML/ai-product-leadership
description: "Author an internal AI use policy covering acceptable use, data handling, human review, and accountability — specific and enforceable rather than aspirational boilerplate."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - CM-02
  - RP-02
difficulty: intermediate
tags:
  - ai-policy
  - governance
  - acceptable-use
  - data-handling
  - accountability
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/ai-product-leadership/aipm_model_risk_brief_for_execs.md
  - domain-AI-ML/ai-product-leadership/aipm_vendor_model_selection.md
  - domain-AI-ML/ai-product-leadership/aipm_jargon_translator_for_stakeholders.md
---

# Internal AI Use Policy Authoring

**Objective:** Draft an internal AI use policy that is specific, enforceable, and usable — defining acceptable use, data-handling rules, required human review, and clear accountability — so employees know what they can and cannot do with AI tools, and the organization can demonstrate governance.

**When to Use:**
- Employees are using AI tools (LLMs, copilots) with no rules, creating data and compliance risk.
- A board, customer, or regulator asks "what's your AI policy?"
- Rolling out an approved AI tool and needing usage guardrails.

**When NOT to Use:**
- You need a per-model risk brief (use `aipm_model_risk_brief_for_execs.md`).
- You're selecting which tool to approve (use `aipm_vendor_model_selection.md`).

## Inputs / Context

- **Organization context** — industry, size, regulatory regimes (GDPR, HIPAA, sector rules), data sensitivity.
- **Current AI use** — what tools people use today, sanctioned or shadow.
- **Risk appetite** — conservative vs permissive posture from leadership.
- **Approved tools** — any vetted tools/vendors and their data terms.
- **Existing policies** — security, data classification, code-of-conduct the AI policy must align with.

## Constraints

**Must:**
- Make rules concrete and testable ("do not paste customer PII into non-approved tools"), not aspirational ("use AI responsibly").
- Tie data-handling rules to the org's data classification scheme and the approved tools' actual data terms.
- Assign accountability: who approves tools, who reviews high-risk uses, who employees ask when unsure.

**Must Not:**
- Produce generic boilerplate that could apply to any company; ground it in the stated industry, data, and tools.
- Cite specific laws or obligations the user did not confirm apply; flag legal-review-required items rather than inventing requirements.
- Write rules with no enforcement or escalation path.

**Instructions:**

1. **State scope and purpose.** Who the policy covers, what AI tools it governs (gen-AI assistants, embedded features, custom models), and the principles behind it. Anchor to a recognized governance frame (e.g., NIST AI RMF, EU AI Act) where the org's exposure warrants it.

2. **Define acceptable and prohibited use.** Concrete allowed uses and a clear prohibited list (e.g., no AI-generated decisions on protected-class matters without review; no shadow tools). Use examples.

3. **Set data-handling rules by classification.** Map each data class (public/internal/confidential/regulated) to what may be sent to which tools. Be explicit about PII, customer data, source code, and secrets.

4. **Require human review where stakes demand it.** Define which AI outputs require human verification before use (customer-facing content, code to prod, decisions affecting people) and to what standard.

5. **Address attribution, accuracy, and IP.** Rules on disclosing AI assistance, verifying AI claims before relying on them, and respecting IP/licensing of generated content.

6. **Establish governance and accountability.** Tool-approval process, roles (owner, reviewers, point of contact), incident reporting, and how the policy is updated.

7. **Add enforcement and escalation.** Consequences for violations, how to report concerns, and the "when in doubt, ask X" path. Flag every item that needs legal/compliance sign-off.

**Output Format:**

A markdown policy document:
- **Scope & Principles** — who/what it covers and why.
- **Acceptable Use / Prohibited Use** — concrete lists with examples.
- **Data Handling by Classification** — table: Data class | Approved tools | Rules.
- **Human Review Requirements** — which outputs require review, to what standard.
- **Accuracy, Attribution & IP** — verification and disclosure rules.
- **Governance & Accountability** — roles, approval, incident reporting, update cadence.
- **Enforcement & Escalation** — consequences and the "ask first" path.
- **⚠ Legal Review Required** — list of items needing counsel sign-off.

## Verification

- [ ] Rules are concrete and testable, not aspirational.
- [ ] Data-handling rules map to the org's classification scheme and tools' real terms.
- [ ] Accountability roles and an escalation path are named.
- [ ] No invented legal obligations; uncertain ones flagged for legal review.
- [ ] Human-review requirements specify which outputs and to what standard.

## False-Positive Prevention

❌ **DON'T:**
- Write "employees must use AI ethically and responsibly" and call it a policy.
- State that GDPR/HIPAA/etc. "requires X" without confirming the regime applies — flag for counsel instead.
- Permit confidential data in tools whose terms allow training on submitted data.
- Create rules with no owner, no escalation, and no consequence.

✅ **DO:**
- Give concrete, checkable rules with examples a manager could enforce.
- Map data classes to specific tools and cite the tools' actual data terms.
- Name the accountable roles and the "when unsure, ask X" contact.
- Mark every legal/compliance assertion as legal-review-required unless the user confirmed it.

## Example Output

```markdown
## Internal AI Use Policy — [Company], v1 (DRAFT — legal review pending)

### Scope & Principles
Covers all employees and contractors using any AI tool (assistants, copilots, embedded
features). Principles: protect customer/company data, keep humans accountable for
decisions, be transparent about AI use. Aligned to NIST AI RMF.

### Acceptable Use
- Drafting, brainstorming, summarizing INTERNAL/PUBLIC content in approved tools.
- Code assistance in [approved copilot] for non-secret repos.

### Prohibited Use
- Pasting confidential/regulated data or secrets into any non-approved tool.
- Using AI to make final decisions on hiring, credit, or other protected-class matters
  without documented human review.
- Installing unsanctioned AI tools ("shadow AI").

### Data Handling by Classification
| Data class | Approved tools | Rules |
|---|---|---|
| Public | Any approved | OK |
| Internal | [Tool A] (no-training tier) | OK, no external sharing |
| Confidential | [Tool A] enterprise only | Allowed only in vetted tier |
| Regulated (PII/PHI) | None until vetted | Prohibited pending DPA review ⚠ |

### Human Review Requirements
Customer-facing content, code to production, and any people-affecting decision require
human review and sign-off before use.

### Governance & Accountability
Tool approval: AI Governance lead. High-risk use review: [role]. Questions: #ai-help.
Incidents: report to security within 24h. Policy reviewed quarterly.

### ⚠ Legal Review Required
- Applicability of GDPR/CCPA to AI-tool data flows. - Regulated-data tooling DPAs.
- IP ownership of AI-generated marketing content.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** scope → use → data → review → governance → enforcement.
- **ST-03 (Output Format Specification):** a fixed, sectioned policy document.
- **DS-01 (Framework Application):** anchored to NIST RMF / EU AI Act where warranted.
- **CM-02 (Constraint Specification):** data classification maps to hard usage constraints.
- **RP-02 (Audience-Specific Framing):** written for employees and reviewers to act on.

**Related Prompts:**
- `aipm_model_risk_brief_for_execs.md` — per-model risk within this policy's frame.
- `aipm_vendor_model_selection.md` — vetting the tools the policy approves.
- `aipm_jargon_translator_for_stakeholders.md` — communicate the policy to non-technical staff.
