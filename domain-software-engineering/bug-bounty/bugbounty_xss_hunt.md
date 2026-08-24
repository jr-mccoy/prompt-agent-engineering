---
title: "XSS Hunting (Reflected / Stored / DOM)"
category: bug-bounty/hunting
description: "Black-box test plan for cross-site scripting on in-scope targets: source-to-sink mapping, context-aware payload reasoning, and impact escalation with safe proof"
techniques:
  - ST-01
  - ST-02
  - QA-02
  - RT-05
  - DD-07
difficulty: intermediate
tags:
  - bug-bounty
  - xss
  - dom-xss
  - stored-xss
  - context-aware
updated: "2026-06-18"
related_prompts:
  - domain-software-engineering/bug-bounty/bugbounty_finding_triage_validation.md
  - domain-software-engineering/bug-bounty/bugbounty_severity_cvss_impact.md
  - domain-software-engineering/bug-bounty/bugbounty_poc_builder.md
---

# XSS Hunting (Reflected / Stored / DOM)

**Objective:** Find where attacker-controlled input executes as script in another user's browser on an in-scope target, reasoning about injection *context*, and prove it with a safe, non-disruptive payload.

## When to Use
- The target reflects input into pages, stores user content shown to others, or does client-side rendering.
- You want a methodical XSS pass rather than spraying `alert(1)`.
- You have a candidate reflection and need to confirm execution + realistic impact.

## Inputs / Context
- **In-scope pages/params** that reflect or store input (search, profile fields, comments, error pages).
- **Your own test accounts** for stored-XSS (so only you view the payload during testing).
- **RoE limits** — confirm whether the program excludes self-XSS or low-impact XSS.

## Instructions

1. **Authorization gate.** Confirm pages are in scope. For stored XSS, place payloads only where **you** are the victim (your own profile/test content) — do NOT inject script into areas that would execute in real users' or staff browsers. Use benign, non-disruptive proof (see step 6), never payloads that deface, phish, or exfiltrate real user data.

2. **Map sources → sinks:** identify every place input enters (query/body/path/headers/fragment) and where it lands in the response or DOM. Classify each as reflected, stored, or DOM-based.

3. **Determine the injection context** for each candidate: HTML body, attribute, JS string, URL, CSS, or template. Context dictates the break-out sequence — a payload that works in HTML body fails in a JS string and vice-versa.

4. **Reason out a context-appropriate proof payload:** the minimal sequence that escapes the current context and executes. Track encoding/escaping applied by the app to see whether it's context-correct (e.g., HTML-encoding inside a JS context doesn't help).

5. **For DOM XSS:** trace client-side flows from sources (`location`, `document.referrer`, `postMessage`) to dangerous sinks (`innerHTML`, `eval`, `document.write`, framework bindings) in the JS; confirm execution from a source you control.

6. **Use safe proof of execution:** prefer a benign, attributable marker — e.g., a `console.log`/`document.title` change, or a request to *your own* collaborator with a unique token — over disruptive popups, and never exfiltrate real cookies/data. Capture the executing payload and context.

7. **CRITICAL — verify execution, context, and impact:**
   - Confirm the payload actually *executes* (not just reflects unsanitized) — reflection ≠ XSS.
   - Confirm it executes in the intended context and across a realistic path (not only your own browser's address bar for a non-exploitable self-XSS).
   - Check the finding isn't an out-of-scope vuln type (some programs exclude self-XSS / `text/plain` reflections).
   - State realistic impact (session/account effect? CSRF-token theft? defacement scope?) without over-claiming.
   - Assign confidence (High/Med/Low) and note what would change it.

## False-Positive Prevention (MUST follow)
- ❌ Do NOT report reflected input as XSS without confirming script *execution* in a browser context.
- ❌ Do NOT report self-XSS (only exploitable by pasting into your own console/URL) if the program excludes it or there's no delivery path.
- ❌ Do NOT inject payloads where real users/staff would execute them; use your own test content.
- ❌ Do NOT exfiltrate real users' cookies/data as "proof" — use a benign marker to your own collaborator.
- ✅ DO identify the injection context and craft a context-correct payload.
- ✅ DO confirm execution and a realistic delivery path.
- ✅ DO scale the impact claim to what's actually reachable.

## Output Format
```
## Authorization & Safety Note
[In-scope pages; own test content for stored; benign proof; self-XSS RoE stance]

## Source → Sink Map
| Input | Lands in | Context | Type (R/S/DOM) | Encoding applied |

## Confirmation
| # | Param | Context | Proof payload (benign) | Executed? | Delivery path |

## Verified Finding
### [Type] XSS on [location] — confidence: High/Med/Low
- Context + break-out: ...
- Proof of execution (benign): ...
- Delivery path / who can be targeted: ...
- Realistic impact: ...
- What would change confidence: ...

## Self-Audit
[Execution confirmed; context correct; no real-user payload delivery; benign proof]
```

## Example Output
```
## Authorization & Safety Note
In-scope: app.acme.com profile bio (stored), /search?q= (reflected). Stored payload on my own test
profile only. Program does NOT exclude stored XSS. Benign proof via document.title + own collaborator.

## Source → Sink Map
| Input | Lands in | Context | Type | Encoding |
|-------|----------|---------|------|----------|
| q | <div>…</div> on results page | HTML body | reflected | none |
| bio | profile page rendered to viewers | HTML body | stored | none |

## Confirmation
| # | Param | Context | Proof payload | Executed? | Delivery |
|---|-------|---------|---------------|-----------|----------|
| 1 | q | HTML body | "><img src=x onerror="document.title='xss-«token»'"> | yes (title changed) | victim clicks crafted link |
| 2 | bio | HTML body | same benign marker | yes on profile view | anyone viewing my profile |

## Verified Finding
### Stored XSS in profile bio — confidence: High
- Context + break-out: bio reflected unencoded into HTML body; img/onerror executes on render.
- Proof of execution: viewing my own test profile set document.title to "xss-«unique token»" and sent a
  tokened request to my collaborator. No real cookies/data exfiltrated.
- Delivery path: any user viewing the attacker's profile executes the script — realistic stored vector.
- Realistic impact: script runs in viewers' authenticated context (session-riding, CSRF-token theft,
  UI redress). Reported as stored XSS affecting profile viewers.
- What would change confidence: if a CSP blocked inline handlers — confirmed no effective CSP on this page.

## Self-Audit
Execution confirmed (title + collaborator hit) in the correct HTML-body context; payload lived only on
my own profile; proof was a benign marker, no real-user data taken.
```

## Techniques Used
- **ST-01 (Clear Objective Statement)** — XSS framed as input executing in another user's browser.
- **ST-02 (Structured Sequential Instructions)** — source→sink map, context, payload, DOM trace, proof.
- **QA-02 (Adversarial Thinking)** — context-aware break-out reasoning mirrors real exploitation.
- **RT-05 (Evidence-Based Reasoning)** — requires confirmed execution, not mere reflection.
- **DD-07 (Self-Audit Table)** — verification enforces benign proof and a realistic delivery path.
