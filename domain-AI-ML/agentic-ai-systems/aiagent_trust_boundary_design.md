---
title: "AI Agent Trust Boundary Design"
category: AI-ML/agentic-ai-systems
description: "Treat the trust and compliance boundary as the first design constraint for an AI product or agent — classify data, map allowed flows, decide what executes in-perimeter, and apply a per-capability ship/no-ship gate before anything is built."
techniques:
  - ST-02
  - CM-02
  - RT-02
  - DS-06
  - QA-01
difficulty: advanced
tags:
  - trust-boundary
  - compliance
  - data-residency
  - agent-architecture
  - design-constraint
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_architecture_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_privacy_data_governance.md
  - domain-AI-ML/agentic-ai-systems/aiagent_safety_sandboxing.md
---

# AI Agent Trust Boundary Design

**Objective:** Make the trust/compliance boundary the *first* design constraint for an AI-powered product or agent — classifying data by sensitivity, mapping where each class may and may not flow, deciding what executes in-perimeter vs. externally, and applying a per-capability ship/no-ship gate — so the architecture that ships is the one that can clear compliance.

**When to Use:**
- You are designing an AI product or agent for a regulated industry or for clients with strict data-handling requirements.
- Sensitive or client data is involved and you need to know, up front, what can ever ship.
- Before architecture is locked, while the cost of moving the boundary is still low.

**When NOT to Use:**
- The system handles only public, non-sensitive data with no compliance exposure — note that and proceed to general architecture.
- You need runtime containment (use `aiagent_safety_sandboxing.md`) or detailed data governance mechanics (use `aiagent_privacy_data_governance.md`).

**Source:** Framework adapted from Anthropic "Building AI Agents for the Enterprise" (2026), a vendor report — facts attributed inline; no source text reproduced.

## Inputs / Context

Provide what you can; the design degrades gracefully if some are missing:
- **Data classes** — every category of data the system will touch and its sensitivity.
- **Trust perimeter** — where the security boundary actually sits (user's machine, org network, a tenant boundary).
- **Capability list** — each thing the product/agent will do that may move or process data.
- **Regulatory regime** — the compliance frameworks and contractual obligations in scope.
- **Deployment options** — what can run locally or in-perimeter vs. what must call external services.

## Constraints

**Must:**
- Solve the trust architecture first; anything that operates outside your trust boundary cannot ship.
- Classify every data class and map, per class, where it may and may not flow.
- Apply a ship/no-ship gate to each capability based on whether it keeps data inside the perimeter or moves it out.

**Must Not:**
- Treat data security and compliance as features to add later — in regulated industries they are prerequisites.
- Design a capability that requires sensitive or client data to leave the perimeter even temporarily without flagging the months-long compliance review it triggers (and the real chance of rejection).
- Ship a capability whose data flow crosses the boundary without an explicit gate decision and evidence.

**Instructions:**

1. **State the operating principle.** Solve the trust architecture first and you move quickly; treat it as an afterthought and products stall in compliance review indefinitely. Record the trust perimeter and the frameworks in scope.

2. **Classify data by sensitivity.** Enumerate every data class and rank it (e.g., public, internal, confidential, regulated/PII). The most sensitive class governs the boundary.

3. **Map allowed and forbidden flows per class.** For each data class, state where it may flow and where it may never go — especially across the trust perimeter to external services.

4. **Enumerate boundary-crossing actions.** List which agent actions cross the perimeter and which stay inside. Treat any crossing of sensitive/regulated data as a default no-ship pending a gate decision.

5. **Decide what executes in-perimeter.** Identify capabilities that can run locally or inside the org boundary so data never leaves — in-perimeter execution is a deployment accelerant that can bypass lengthy security reviews. Prefer it wherever feasible.

6. **Design auditability.** Specify observability (an OpenTelemetry-compatible trace) capturing who did what, when, and on whose behalf, so every boundary-relevant action is attributable.

7. **Design continuity.** Ensure context travels with the work across steps and sessions without forcing data across the boundary to do so.

8. **Apply the per-capability ship/no-ship gate.** For each capability, decide ship (stays in-perimeter or moves only permitted classes) or no-ship (requires sensitive data to leave the perimeter), and attach the compliance evidence chain that supports the decision.

**Output Format:**

A markdown trust-boundary design:
- **Operating Principle & Perimeter** — where the boundary sits, frameworks in scope
- **Data Classification** — table: Data class | Sensitivity | Where it may flow | Where it may never go
- **Trust-Boundary Map** — which actions stay inside vs. cross the perimeter
- **In-Perimeter Execution Plan** — capabilities run locally/in-perimeter to avoid crossings
- **Auditability & Continuity** — trace design + how context travels with the work
- **Ship / No-Ship Gate** — table: Capability | Crosses boundary? | Decision | Compliance evidence

## Verification

- [ ] The trust architecture is decided before the rest of the design.
- [ ] Every data class is classified and its allowed/forbidden flows are mapped.
- [ ] Every boundary-crossing action is identified; sensitive crossings default to no-ship pending a gate.
- [ ] In-perimeter execution is used wherever feasible to avoid crossings.
- [ ] Auditability (who/what/when/on-whose-behalf) and context continuity are designed.
- [ ] Each capability has an explicit ship/no-ship decision with a compliance evidence chain.

## False-Positive Prevention

❌ **DON'T:**
- Design the features first and "add security later" — in regulated contexts that order produces unshippable products.
- Wave through a capability that moves sensitive data out "only temporarily" — temporary crossings still trigger review and rejection.
- Claim a capability is compliant without an evidence chain tying it to the in-scope frameworks.
- Force data across the boundary just to carry context between steps when in-perimeter continuity is possible.

✅ **DO:**
- Solve the trust boundary first and let it determine what can ever ship.
- Default sensitive-data crossings to no-ship until a gate decision says otherwise.
- Prefer local/in-perimeter execution to bypass lengthy reviews.
- Attach a concrete compliance evidence chain to every ship decision.

## Example Output

```markdown
## Trust Boundary Design: Clinical Notes Assistant
Operating principle: solve trust first or stall in review. Perimeter = hospital network.
Frameworks in scope: HIPAA + the health system's BAA terms.

### Data Classification
| Data class | Sensitivity | May flow | Never goes |
|---|---|---|---|
| PHI (notes) | Regulated | within hospital network | external services |
| De-identified stats | Internal | network + approved analytics | unapproved third parties |
| App config | Public | anywhere | — |

### Trust-Boundary Map
- Stays inside: note summarization, entity extraction, draft generation.
- Would cross: sending raw notes to an external model API → flagged.

### In-Perimeter Execution Plan
Summarization and extraction run on in-network inference so PHI never leaves the
perimeter — this avoids the multi-month external-vendor security review.

### Auditability & Continuity
OpenTelemetry trace per action: clinician id, patient ref (tokenized), action, time.
Context (current encounter) travels with the work in-network; no external persistence.

### Ship / No-Ship Gate
| Capability | Crosses boundary? | Decision | Compliance evidence |
|---|---|---|---|
| In-network summarize | No | SHIP | PHI stays in perimeter; trace logged |
| External-API drafting | Yes (PHI out) | NO-SHIP | violates BAA; would trigger review/rejection |
| De-id trend export | Only de-id data | SHIP w/ gate | de-id verified before export |
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** principle → classify → map flows → in-perimeter → audit → gate.
- **CM-02 (Constraint Specification):** the trust boundary and "cannot ship outside it" rule are the governing constraints.
- **RT-02 (Adversarial / Red-Team Reasoning):** stress-tests each capability for unintended boundary crossings.
- **DS-06 (Prioritization & Severity Guidance):** the most sensitive data class governs the whole boundary.
- **QA-01 (Acceptance / Gate Criteria):** the per-capability ship/no-ship gate is the decision artifact.

**Related Prompts:**
- `aiagent_architecture_design.md` — the broader architecture this boundary constrains first.
- `aiagent_privacy_data_governance.md` — the data-handling mechanics behind the flow map.
- `aiagent_safety_sandboxing.md` — the runtime containment that enforces in-perimeter execution.
