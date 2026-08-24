---
title: "Finding Triage & Validation"
category: bug-bounty/triage
description: "Pre-report gate that confirms a candidate finding is real, in-scope, exploitable, and likely non-duplicate before you spend time writing it up"
techniques:
  - ST-01
  - QA-02
  - RT-05
  - DS-06
  - DD-07
difficulty: intermediate
tags:
  - bug-bounty
  - triage
  - validation
  - false-positive
  - duplicate
updated: "2026-06-18"
related_prompts:
  - domain-software-engineering/bug-bounty/bugbounty_severity_cvss_impact.md
  - domain-software-engineering/bug-bounty/bugbounty_disclosure_report_writer.md
  - domain-software-engineering/bug-bounty/bugbounty_program_scope_analyzer.md
---

# Finding Triage & Validation

**Objective:** Decide whether a candidate finding is worth reporting — by confirming it is genuinely reproducible, in scope, exploitable with real impact, and unlikely to be a known/duplicate or out-of-scope class — before investing in a write-up.

## When to Use
- You think you found something and want a go/no-go gate before writing the report.
- You want to avoid the two biggest time-wasters: reporting false positives and reporting out-of-scope/known issues.
- You have several candidates and need to decide which deserve a full report.

## Inputs / Context
- **The candidate finding(s):** what you observed, where, and how you triggered it.
- **The program scope & exclusions** (from `bugbounty_program_scope_analyzer.md`).
- **Any evidence you captured** (requests/responses, screenshots).

## Instructions

1. **Authorization/scope recheck.** Confirm the affected asset is in scope and the vuln *type* is not on the program's out-of-scope/not-rewarded list (self-XSS, missing headers, rate-limit, etc.). An out-of-scope finding fails the gate regardless of how real it is.

2. **Reproducibility check:** can you reproduce it from a clean state (fresh session/account) following written steps? A finding you can't reproduce on demand isn't report-ready. Note environmental dependencies.

3. **Exploitability check:** is there a realistic attacker path, or does it require improbable preconditions (victim runs attacker JS, attacker already has admin, requires MITM on a victim's network)? Down-rank or reject theoretical-only issues.

4. **Real-impact check:** what concretely happens — data exposed, state changed, money moved, account taken over? Separate "interesting behavior" from "security impact." No impact → no report (or report as informational only if the program wants it).

5. **Duplicate-likelihood check:** is this a low-hanging, obvious issue on a mature program (likely already reported), or something requiring specific insight (less likely duplicate)? You can't know for sure, but obvious bugs on old programs are often duplicates — factor it into prioritization, not into whether it's valid.

6. **Evidence-sufficiency check:** do you have the request/response deltas, accounts used, and a clean repro that a triager could follow without guesswork?

7. **Render a go/no-go verdict** per finding with reasons, and for "go" findings, a readiness checklist for the report.

8. **CRITICAL — be your own harshest triager:**
   - Try to *disprove* the finding: find the benign explanation (caching, your own data, intended sharing, client-side-only).
   - Confirm in scope AND in a rewarded vuln class.
   - Confirm reproducible from clean state with captured evidence.
   - State a confidence level and exactly what evidence supports the "go."

## False-Positive Prevention (MUST follow)
- ❌ Do NOT pass a finding you can only reproduce sometimes or from a dirty state.
- ❌ Do NOT pass an out-of-scope asset or a not-rewarded vuln type, however real.
- ❌ Do NOT pass "interesting but no impact" behavior as a security finding.
- ❌ Do NOT ignore the benign explanation — actively look for it first.
- ✅ DO attempt to disprove the bug before passing it.
- ✅ DO require clean-state reproducibility and captured evidence.
- ✅ DO match the finding to a rewarded, in-scope class.

## Output Format
```
## Scope & Class Recheck
[In scope? Rewarded class? cite policy]

## Validation Checklist (per finding)
| Check | Result | Notes |
| Reproducible from clean state | ✅/❌ | ... |
| Realistic attacker path | ✅/❌ | ... |
| Concrete security impact | ✅/❌ | ... |
| Benign explanation ruled out | ✅/❌ | ... |
| Evidence sufficient | ✅/❌ | ... |

## Duplicate-Likelihood
[Low/Med/High + reasoning]

## Verdict: GO / NO-GO — confidence: High/Med/Low
[Reasons; if GO, what's ready and what to capture before writing]
```

## Example Output
```
## Scope & Class Recheck
Asset api.acme.com is in scope; IDOR (broken access control) is a rewarded class. ✅

## Validation Checklist
| Check | Result | Notes |
|-------|--------|-------|
| Reproducible from clean state | ✅ | fresh login as A, fetch B's order id → 200 + B's data, 3x |
| Realistic attacker path | ✅ | any authenticated user can iterate/obtain IDs |
| Concrete security impact | ✅ | cross-account PII (name, address, items) |
| Benign explanation ruled out | ✅ | order is B's private order, not shared/demo; not my own data |
| Evidence sufficient | ✅ | full request/response for both accounts captured |

## Duplicate-Likelihood
Medium — IDOR is common, but this endpoint isn't UI-linked and uses non-sequential IDs, so it's less
likely already found. Worth reporting promptly.

## Verdict: GO — confidence: High
Real, in-scope, reproducible cross-account read with captured evidence. Proceed to severity scoring,
then the report. Before writing, redact B's PII in screenshots to the minimum needed to prove the bug.
```

## Techniques Used
- **ST-01 (Clear Objective Statement)** — a go/no-go gate, not just a description.
- **QA-02 (Adversarial Thinking)** — the disprove-it-first step actively hunts the benign explanation.
- **RT-05 (Evidence-Based Reasoning)** — requires clean-state reproduction and captured deltas.
- **DS-06 (Prioritization Guidance)** — duplicate-likelihood and impact inform what to report first.
- **DD-07 (Self-Audit Table)** — the checklist forces an explicit per-criterion verdict.
