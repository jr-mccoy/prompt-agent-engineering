---
title: "Bug Bounty Getting-Started Orientation"
category: bug-bounty/orientation
description: "Orient a newcomer to authorized bug bounty hunting: how programs work, the legal/authorization basics, realistic income expectations, and a structured first-90-days path"
techniques:
  - ST-01
  - ST-02
  - DS-01
  - ED-01
  - DD-07
difficulty: beginner
tags:
  - bug-bounty
  - getting-started
  - authorization
  - responsible-disclosure
  - career
updated: "2026-06-18"
related_prompts:
  - domain-software-engineering/bug-bounty/bugbounty_program_scope_analyzer.md
  - domain-software-engineering/bug-bounty/bugbounty_skill_development_plan.md
  - domain-software-engineering/bug-bounty/bugbounty_program_selection_roi.md
---

# Bug Bounty Getting-Started Orientation

**Objective:** Give a newcomer a realistic, authorization-first orientation to bug bounty hunting and a concrete first-90-days plan, without over-promising income or skipping the legal/ethical foundation.

## When to Use
- You are new to bug bounties and want to understand how the field actually works before investing time.
- You want a realistic picture of effort, timeline, and income — not hype.
- You need a structured ramp from "I know some software" to "I submitted my first valid report."

## Inputs / Context
Provide what you can (the prompt should ask for anything missing):
- **Your background:** programming languages, web/mobile/cloud familiarity, any security exposure.
- **Time budget:** hours per week you can realistically commit.
- **Goal:** learning, supplemental income, or career transition.
- **Risk constraints:** employment contracts/NDAs that may restrict security testing.

## Instructions

1. **Establish the authorization foundation first.** Explain plainly that bug bounty hunting is legal *only* because a program grants permission to test specific assets under published rules. State the five non-negotiables: authorization gate, stay in scope, non-destructive testing, responsible disclosure, methodology-not-malware. Make clear that testing anything not explicitly in scope is unauthorized access and may be a crime.

2. **Explain the ecosystem** in beginner terms:
   - **Platforms** (e.g., HackerOne, Bugcrowd, Intigriti, YesWeHack, self-hosted VDPs) — what they do (mediate scope, triage, payment).
   - **Program types** — public vs. private/invite-only; paid bounty vs. VDP (recognition only).
   - **The lifecycle of a report** — submit → triage → validation → severity/bounty decision → fix → disclosure.
   - **How payouts work** — severity tiers, duplicates (only the first valid report pays), out-of-scope rejections.

3. **Set realistic expectations.** Based on the user's time budget and background, give an honest ramp: most beginners spend weeks to months before a first valid bounty; early income is irregular; the compounding asset is *skill and reputation*, not any single bug. Avoid quoting specific dollar figures as guarantees — frame ranges as "varies widely by program and severity."

4. **Recommend a learning-while-earning split.** Point to free practice grounds (deliberately vulnerable labs, CTFs, the program's own VDP-tier targets) where mistakes are safe, versus live programs where rules matter. Reference `bugbounty_skill_development_plan.md` for the structured study loop.

5. **Help pick a beachhead.** Recommend starting with a single, beginner-friendly, wide-scope program in a vuln class that matches the user's strengths (e.g., web access-control bugs for someone with web-dev background). Reference `bugbounty_program_selection_roi.md` and `bugbounty_program_scope_analyzer.md`.

6. **Produce a first-90-days plan** with weekly milestones (foundations → first recon → first hunt → first report), each with a concrete, checkable output.

7. **CRITICAL — verify the orientation is honest and safe before finalizing:**
   - Confirm you have NOT promised specific earnings or a timeline to first payout.
   - Confirm the authorization/legal foundation appears *before* any "how to find bugs" content.
   - Confirm every suggested practice target is either deliberately-vulnerable training infrastructure or an explicitly in-scope program asset.
   - Confirm advice matches the user's *stated* time budget and background, not an idealized full-timer.

## False-Positive Prevention (MUST follow)
- ❌ Do NOT imply bug bounties are reliable or quick income; most newcomers earn little for months.
- ❌ Do NOT suggest testing any site "to practice" that is not deliberately-vulnerable training infrastructure or an in-scope program asset.
- ❌ Do NOT skip or bury the authorization/legal foundation beneath tactical content.
- ❌ Do NOT recommend a vuln class wildly mismatched to the user's background and time budget.
- ✅ DO frame income as variable and skill as the compounding asset.
- ✅ DO tailor the ramp to the user's real hours-per-week and starting skills.
- ✅ DO point beginners to safe practice grounds before live targets.
- ✅ DO flag employment/NDA conflicts as something to resolve before testing.

## Output Format
```
## Reality Check
[Honest framing of effort, timeline, and income variability — 3-5 sentences]

## The Authorization Foundation (read first)
[The five non-negotiables, stated plainly]

## How the Ecosystem Works
- Platforms: ...
- Program types: ...
- Report lifecycle: ...
- How payouts/duplicates work: ...

## Your Starting Profile
| Factor | Your input | Implication |
|--------|-----------|-------------|
| Background | ... | Best-fit vuln class: ... |
| Time/week | ... | Realistic ramp: ... |
| Goal | ... | ... |

## Recommended Beachhead
[Program type + vuln class to start with, and why]

## First 90 Days
| Weeks | Focus | Checkable output |
|-------|-------|------------------|
| 1-2 | Foundations + authorization | ... |
| 3-5 | Practice labs in [class] | ... |
| 6-9 | First recon + scope analysis on a live program | ... |
| 10-13 | First hunt + first report | ... |

## Next Prompts
[Which prompts in this directory to use next]
```

## Example Output
```
## Reality Check
Bug bounties can supplement income, but they are not a steady paycheck. Most people with a software
background spend roughly 6–12 weeks of part-time effort before a first valid, paid finding, and early
results are lumpy — you may get nothing for a month and then two bugs in a week. Programs only pay the
*first* person to report a given bug, so duplicates are common and expected. Treat the first quarter as
skill-and-reputation building; the money follows the skill, not the other way around.

## The Authorization Foundation (read first)
1. Authorization gate — only test assets a program explicitly lists as in scope.
2. Stay in scope — out-of-scope testing is unpaid and may be illegal.
3. Non-destructive — no DoS, no destructive payloads, minimal proof only.
4. Responsible disclosure — report via the official channel, follow the timeline, don't go public.
5. Methodology, not malware — you're producing reports, not weaponized exploits.
Resolve any employer NDA/contract restrictions before you test anything.

## How the Ecosystem Works
- Platforms: HackerOne, Bugcrowd, Intigriti, YesWeHack mediate scope, triage findings, and handle pay.
- Program types: public (anyone) vs. private (invite); bounty (pays cash) vs. VDP (recognition only).
- Report lifecycle: submit → triage analyst validates → severity/bounty assigned → vendor fixes →
  optional coordinated disclosure.
- Payouts/duplicates: severity tiers (Low→Critical) set bounty ranges; only the first valid report of
  a unique bug is paid; out-of-scope or unverifiable reports are closed unpaid.

## Your Starting Profile
| Factor | Your input | Implication |
|--------|-----------|-------------|
| Background | 4 yrs web dev (JS/Node, REST APIs) | Best-fit class: broken access control / IDOR + API bugs |
| Time/week | ~6 hrs (evenings) | Ramp on the slower end; one program at a time |
| Goal | Supplemental income + learning | Optimize for wide-scope programs with fast triage |

## Recommended Beachhead
Start with a public, wide-scope web program and hunt broken access control / IDOR. Your API/web-dev
background means you already understand how object IDs and auth checks *should* work, which is exactly
the intuition that finds these bugs — and they're among the most common and best-paid classes.

## First 90 Days
| Weeks | Focus | Checkable output |
|-------|-------|------------------|
| 1-2 | Authorization rules + read 10 disclosed IDOR reports | Notes file summarizing 10 real bugs |
| 3-5 | Practice IDOR/access-control in deliberately-vulnerable labs | Solved lab set; documented method |
| 6-9 | Run scope analyzer + recon on one live program | Attack-surface map + compliant test plan |
| 10-13 | Hunt access-control bugs; write first report | One submitted, well-formed report |

## Next Prompts
Use bugbounty_program_selection_roi.md to pick the program, then bugbounty_program_scope_analyzer.md
to read its scope, then bugbounty_access_control_idor_hunt.md to hunt.
```

## Techniques Used
- **ST-01 (Clear Objective Statement)** — opens with an authorization-first, honest objective.
- **ST-02 (Structured Sequential Instructions)** — ordered ramp from foundation to first report.
- **DS-01 (Framework Application)** — applies the report lifecycle and five non-negotiables as a frame.
- **ED-01 (Iterative Scaffolding)** — teaches ecosystem concepts at a beginner level before tactics.
- **DD-07 (Self-Audit Table)** — the verification step checks honesty and safety before finalizing.
