---
title: "Injection Hunting (SQLi / Command / SSTI / NoSQL)"
category: bug-bounty/hunting
description: "Black-box test plan for injection vulnerabilities on in-scope targets: SQL, NoSQL, OS command, and server-side template injection, using safe non-destructive confirmation"
techniques:
  - ST-01
  - ST-02
  - QA-02
  - RT-05
  - DD-07
difficulty: advanced
tags:
  - bug-bounty
  - sql-injection
  - command-injection
  - ssti
  - nosql-injection
updated: "2026-06-18"
related_prompts:
  - domain-software-engineering/bug-bounty/bugbounty_tech_stack_threat_profile.md
  - domain-software-engineering/bug-bounty/bugbounty_poc_builder.md
  - domain-software-engineering/bug-bounty/bugbounty_finding_triage_validation.md
---

# Injection Hunting (SQLi / Command / SSTI / NoSQL)

**Objective:** Find places where attacker input is interpreted as code or query syntax on an in-scope target, and confirm injection safely — proving the vulnerability without destroying data or exfiltrating beyond minimal proof.

## When to Use
- You have in-scope endpoints that take input feeding queries, shell commands, or templates.
- The tech-stack profile flagged an injection-prone component or sink.
- You have a candidate injection point and need safe confirmation.

## Inputs / Context
- **In-scope input vectors** (params in path/query/body/headers/cookies; file names; JSON fields).
- **Tech-stack hints** (DB type, template engine, OS) from recon/threat profile.
- **An OOB collaborator you control** (for blind/out-of-band confirmation).
- **RoE limits** — especially prohibitions on destructive payloads and high-volume fuzzing.

## Instructions

1. **Authorization gate.** Confirm endpoints are in scope. Use **only non-destructive** payloads: no `DROP`/`DELETE`/`UPDATE` that changes data, no command payloads that modify the system, no stress/fuzz volumes the RoE forbids. Confirmation must prove interpretation, not cause damage.

2. **Map input → sink hypotheses:** for each input, hypothesize the interpreter it might reach (SQL, NoSQL, shell, template) based on behavior and stack. Prioritize inputs that visibly affect query results, error messages, or rendered output.

3. **SQL injection:** test with benign syntax-breaking inputs (a single quote, comment, boolean pairs like `' AND 1=1--` vs `' AND 1=2--`) and observe differential responses. For blind cases, use time-based (`SLEEP`-style) sparingly and OOB techniques. Confirm via consistent boolean/time differential, not a one-off error.

4. **NoSQL injection:** test operator injection (`{"$ne": null}`, `[$gt]=`) in JSON/query params on Mongo-style backends; watch for auth bypass or query manipulation via differential responses.

5. **OS command injection:** test benign separators (`;`, `|`, `&&`, backticks, `$( )`) with a **non-destructive** payload that proves execution via OOB (e.g., a DNS lookup to your collaborator) or a benign, observable timing delay — never a system-modifying command.

6. **Server-side template injection (SSTI):** where input is rendered, test engine-detecting expressions (e.g., `{{7*7}}` → `49`) to confirm evaluation; identify the engine before any further step and stop at proof of evaluation.

7. **CRITICAL — verify exploitability without harm:**
   - Confirm the differential is *consistent and reproducible* (boolean true vs. false, or OOB hit), not a transient error or WAF artifact.
   - For OOB/time-based proofs, correlate to your collaborator/timing and rule out false signals.
   - Confirm you used no data-destructive or system-modifying payload.
   - State the interpreter and the minimal proof; do NOT dump full databases or run further commands.
   - Assign confidence (High/Med/Low) and note what would change it.

## False-Positive Prevention (MUST follow)
- ❌ Do NOT report SQLi from a single 500 error — many errors are input validation, not injection. Require a reproducible boolean/time/OOB differential.
- ❌ Do NOT use destructive payloads (DROP/DELETE/UPDATE, rm, write operations) to "prove" injection.
- ❌ Do NOT dump entire databases or run post-exploitation commands — minimal proof only.
- ❌ Do NOT mistake reflected input (potential XSS) for template injection without confirming server-side evaluation (`{{7*7}}`→`49`).
- ✅ DO confirm with a consistent, reproducible differential or OOB callback.
- ✅ DO identify the interpreter and stop at proof-of-concept.
- ✅ DO keep all payloads non-destructive and within RoE volume.

## Output Format
```
## Authorization & Safety Note
[In-scope vectors; non-destructive confirmation; OOB host you control; RoE volume]

## Input → Sink Hypotheses
| Vector | Suspected interpreter | Signal |

## Confirmation Tests
| # | Type | Payload (non-destructive) | Differential observed | Reproducible? | Verdict |

## Verified Finding
### [Injection type] on [vector] — confidence: High/Med/Low
- Interpreter: ...
- Proof (minimal): ...
- Impact (bounded): ...
- What would change confidence: ...

## Self-Audit
[Reproducible differential; no destructive payload; minimal proof]
```

## Example Output
```
## Authorization & Safety Note
In-scope: api.acme.com/v1/products?category=. Non-destructive only; OOB host oob.myhandle.example; low volume.

## Input → Sink Hypotheses
| Vector | Suspected interpreter | Signal |
|--------|----------------------|--------|
| category param | SQL (results-affecting) | result count changes with quote |

## Confirmation Tests
| # | Type | Payload | Differential | Reproducible? | Verdict |
|---|------|---------|--------------|---------------|---------|
| 1 | SQLi boolean | category=books' AND '1'='1 | full product list | yes (3x) | candidate |
| 2 | SQLi boolean | category=books' AND '1'='2 | empty list | yes (3x) | VULN (consistent T/F) |
| 3 | SQLi time | category=books'||pg_sleep(3)--  (single, low-volume) | ~3s delay vs <300ms baseline | yes (2x) | confirms |

## Verified Finding
### Boolean+time-based SQL injection on /v1/products?category= — confidence: High
- Interpreter: PostgreSQL (pg_sleep responded).
- Proof (minimal): consistent boolean differential (1=1 returns rows, 1=2 returns none) plus a 3s
  time delay from a single pg_sleep probe. No data extracted, no rows modified.
- Impact (bounded): query is injectable; likely full read of the products DB and possibly more — I did
  NOT extract data; reporting at proof-of-injection.
- What would change confidence: if a WAF caused the timing — ruled out by reproducible boolean pairs.

## Self-Audit
Differential reproduced 3x; only SELECT-side boolean and one benign pg_sleep used; no DROP/DELETE/UPDATE;
stopped at proof, no DB dump.
```

## Techniques Used
- **ST-01 (Clear Objective Statement)** — frames injection as input interpreted as code/query.
- **ST-02 (Structured Sequential Instructions)** — input→sink map then SQLi/NoSQL/command/SSTI passes.
- **QA-02 (Adversarial Thinking)** — uses the differential/boolean/OOB methods attackers rely on.
- **RT-05 (Evidence-Based Reasoning)** — requires a reproducible differential, not a single error.
- **DD-07 (Self-Audit Table)** — verification enforces non-destructive, minimal-proof confirmation.
