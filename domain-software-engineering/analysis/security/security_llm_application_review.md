---
title: "LLM Application Security Review"
category: analysis/security
description: "Systematic security review of LLM-backed applications covering prompt injection, jailbreak resistance, output handling, tool-use authorization, data exfiltration, and RAG poisoning."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - RT-05
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - security
  - llm
  - ai-security
  - prompt-injection
  - jailbreak
  - rag
  - owasp-llm-top-10
  - agentic-systems
updated: "2026-04-17"
related_prompts:
  - security_vulnerability_analysis.md
  - security_authentication_authorization_review.md
  - ../../devops/llm_ops_evaluation_framework.md
---

# LLM Application Security Review

**Objective:** Perform a systematic security review of an LLM-backed application (chatbot, agent, RAG system, or LLM-augmented feature) to identify exploitable weaknesses specific to generative AI — prompt injection, jailbreak, insecure output handling, tool-use privilege escalation, training/RAG poisoning, and sensitive-data exfiltration — mapped to the OWASP LLM Top 10 (2025).

## When to Use

- Before shipping any user-facing LLM feature to production.
- When adding tool use / function calling to an existing LLM application.
- When introducing RAG over untrusted or user-controllable sources.
- During architecture review of agentic systems with multi-step autonomy.
- Post-incident, to widen the search for related exposures.

**Do NOT use this prompt for:**
- Non-LLM security review (use `security_vulnerability_analysis.md`).
- Model training security (different discipline).
- Pure jailbreak "red-teaming" of foundation models (this is an *application* review).

## Inputs / Context

Collect before starting:
- **Application shape**: chatbot / agent / RAG / classifier / code generator.
- **Trust boundaries**: who provides input, who sees output, what tools/APIs the model can invoke.
- **Data surface**: what user data the model sees, what it stores, what it logs.
- **Model provider and version**: Anthropic / OpenAI / open-source, model family, deployment (hosted / on-prem / edge).
- **Tool use**: exact list of callable tools with their scopes.
- **RAG sources**: origin, freshness, trust level, update mechanism.

If any of these are unknown, STOP and ask before proceeding.

## Must / Must Not

**Must:**
- Map every finding to a **OWASP LLM Top 10 (2025)** identifier (LLM01–LLM10) or state "Out-of-scope of OWASP LLM Top 10" and justify.
- Classify findings by severity: **Critical** (data exfil, tool-use RCE, full jailbreak of safety layer), **High** (bypass of business logic), **Medium** (hardening gap), **Low** / **Info**.
- Identify the **attacker persona** (external user, authenticated user, tenant neighbor, insider) for every finding.
- For every Critical/High finding, provide a **concrete exploit sketch** (how an attacker would weaponize it) and a **mitigation** (system prompt hardening, input/output filter, tool-scope narrowing, sandbox).
- Include **confidence level** per finding: High / Medium / Low.

**Must Not:**
- Claim "prompt injection is unfixable" and stop — there are partial mitigations (input isolation, output parsers, tool-scope narrowing, human-in-the-loop, sandbox).
- Invent CVEs or model-specific jailbreak strings; reference published categories, not unpublished exploits.
- Flag "the model might hallucinate" as a security finding unless the hallucination has a **privilege, integrity, or privacy** consequence.
- Treat all LLM output as untrusted without also recommending the specific parsing/sanitization step for the use case.
- Assume safety training is a security control — it is a **mitigation**, not a boundary.

## Instructions

Work through these six lenses in order. For each lens, produce findings per the Output Format.

1. **Prompt injection surface (LLM01)** — Where can an attacker inject instructions? Direct (user input), indirect (retrieved docs, emails, file contents, tool output)? Is user input mixed with system instructions without delimiters? Are retrieved documents treated as trusted?
2. **Insecure output handling (LLM02)** — Is the model's output executed (shell, SQL, HTML, eval)? Rendered as HTML (XSS)? Used to construct downstream API calls? What's the parsing / validation layer between model → execution?
3. **Training / RAG poisoning (LLM03/04)** — Can an attacker influence what goes into the RAG index? Retrain/fine-tune set? Is there provenance tracking for RAG sources?
4. **Tool use / excessive agency (LLM06/08)** — What tools can the model call? With what credentials? Over what data scope? Is there human-in-the-loop for destructive actions? Can one user cause actions on another user's data?
5. **Sensitive info disclosure (LLM07)** — Can the model exfiltrate system prompt? Other tenants' data? PII? Can prompt-injection instructions extract these?
6. **Supply chain / model integrity (LLM05/09)** — How is the model pinned (version, hash)? Is the API key scoped? Is inference logged / observable? Is there a rollback plan?

## Output Format

```
# LLM Application Security Review — <App Name>

## Summary
- Application shape: <chatbot/agent/RAG>
- Trust boundary map: <one paragraph>
- Overall risk: <Critical / High / Medium / Low>
- Critical findings: <N>
- High findings: <N>

## Findings

### [LLM01 — Prompt Injection] <Title>
- **Severity**: Critical
- **Confidence**: High
- **Attacker**: external unauthenticated user
- **Evidence**: <code path, prompt template, config line>
- **Exploit sketch**: <2–4 lines describing weaponization>
- **Mitigation**: <specific, actionable>
- **Effort to fix**: S / M / L

### [LLM02 — Insecure Output Handling] <Title>
...

## Out-of-Scope Observations
<things noticed but outside LLM security: general auth, infra, etc.>

## Verification Log
<1-paragraph summary of how the review was performed, what was inspected, what was not>
```

## Verification (Self-Check)

Before emitting findings, confirm:

1. Every Critical/High finding references a specific code path, prompt, or configuration.
2. Every finding is mapped to OWASP LLM Top 10 or explicitly marked out-of-scope.
3. The "attacker persona" is stated per finding — no generic "an attacker could".
4. Each mitigation is implementable within the application's architecture; no hand-waving.
5. Confidence is downgraded to **Medium** if the code / prompt was not directly inspected.
6. The Verification Log honestly states what was and was not inspected.

## False-Positive Prevention

Rule out before reporting:

- **"Prompt injection possible"** — Only Critical/High if it leads to **data exfil, privilege escalation, or tool misuse**. A model saying something embarrassing is Medium at best.
- **"Model might hallucinate"** — Only a security finding if the hallucination crosses a privilege/integrity/privacy boundary.
- **"System prompt leak"** — High only if the system prompt contains **secrets, proprietary logic, or authorization rules**. Leaking a generic "you are a helpful assistant" is Info.
- **"RAG source poisoning"** — Only if an attacker can **write** to the RAG source. Read-only RAG of curated sources is Low.
- **"Tool use is dangerous"** — Only flag Critical/High if the tool has **real-world side effects** (payments, deletes, emails) AND user input can steer it without human review.
- **"Output contains user input"** — That's the product. Only a finding if the output is **executed or rendered** without sanitization.

If you did not inspect the system prompt, tool schemas, AND the output-handling layer, cap confidence at **Medium**.

## Techniques Applied

ST-01 (Objective), ST-02 (Sequential), ST-03 (Output format), RT-02 (Multi-dim analysis: 6 lenses), RT-05 (Evidence-based), CM-02 (Constraints), QA-01 (Self-check).
