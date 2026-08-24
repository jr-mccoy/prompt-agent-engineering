---
title: "Bug Bounty Report Post-Mortem"
category: bug-bounty/learning
description: "Extract durable lessons from an accepted, rejected, or duplicate report to raise your hit rate, signal quality, and payout over time"
techniques:
  - ST-01
  - RT-02
  - QA-02
  - DS-06
  - DD-07
difficulty: beginner
tags:
  - bug-bounty
  - post-mortem
  - learning
  - hit-rate
  - feedback
updated: "2026-06-18"
related_prompts:
  - domain-software-engineering/bug-bounty/bugbounty_skill_development_plan.md
  - domain-software-engineering/bug-bounty/bugbounty_disclosure_report_writer.md
  - domain-software-engineering/bug-bounty/bugbounty_program_selection_roi.md
---

# Bug Bounty Report Post-Mortem

**Objective:** Convert each report outcome — accepted, rejected, duplicate, or down-tiered — into a specific, actionable lesson, so your hit rate and payouts trend up instead of repeating the same mistakes.

## When to Use
- A report just resolved (any outcome) and you want to learn from it deliberately.
- A pattern of rejections/duplicates is frustrating you and you want to diagnose the cause.
- Periodically (e.g., monthly) to review your last N reports for trends.

## Inputs / Context
- **The report(s)** and their outcomes (accepted/severity, rejected/reason, duplicate, informative, N/A).
- **Triager feedback** if any.
- **Your time invested** per report (to assess ROI).

## Instructions

1. **Categorize the outcome honestly** and record the program's stated reason. Don't rationalize a rejection as "they were wrong" without evidence — the goal is improvement, not vindication.

2. **Diagnose the root cause by outcome type:**
   - **Rejected (not a vuln / out of scope / not rewarded class):** was it a scope/class misread (fixable upstream with the scope analyzer) or a false positive (fixable with triage)?
   - **Duplicate:** was it an obvious bug on a mature program (program-selection lesson) or just bad luck on timing (report faster)?
   - **Down-tiered:** was impact under-articulated (severity/impact lesson) or genuinely lower than you thought (calibration lesson)?
   - **Accepted:** what made it land — and is the approach repeatable?

3. **Locate the lesson in your workflow:** map the root cause to the specific stage/prompt that should have caught or improved it (scope analysis, recon, triage, severity, report writing, program selection).

4. **Assess ROI:** time invested vs. outcome. Repeated low-ROI patterns (slow programs, saturated scope, low-impact classes) are a program-selection or specialization signal.

5. **Extract 1–3 concrete, behavioral changes** for next time (e.g., "read out-of-scope vuln-types list before testing," "report within 24h on wide-scope programs," "always include an escalation-potential paragraph").

6. **Update your running trends:** acceptance rate, common rejection reasons, best-performing class/program — to guide where you spend time.

7. **CRITICAL — verify the lessons are specific and actionable:**
   - Confirm each lesson is a behavior change, not a platitude ("be more careful").
   - Confirm the root cause is mapped to a fixable workflow stage.
   - Confirm you separated "my mistake" from "out of my control" honestly.
   - Confirm trends are based on actual outcomes, not a single emotional data point.

## False-Positive Prevention (MUST follow)
- ❌ Do NOT conclude "the triager was wrong" without concrete evidence — default to finding the improvable cause.
- ❌ Do NOT produce vague lessons ("get better") — every lesson must be a specific behavior change.
- ❌ Do NOT over-update on one outcome; trends need several data points.
- ❌ Do NOT ignore ROI — a "valid" bug that took 20h on a stingy program is still a selection lesson.
- ✅ DO map each root cause to a specific workflow stage/prompt.
- ✅ DO extract behavioral changes you can apply next session.
- ✅ DO track trends across reports, not just the latest.

## Output Format
```
## Outcome
[Accepted(severity)/Rejected(reason)/Duplicate/Down-tiered/Informative] + triager feedback

## Root-Cause Diagnosis
[What actually drove the outcome; my-mistake vs out-of-control]

## Workflow Stage Responsible
[Which stage/prompt should have caught/improved this]

## ROI Check
[Time invested vs outcome; selection/specialization signal?]

## Concrete Changes (1-3, behavioral)
1. ...

## Trend Update
- Acceptance rate: ...
- Common rejection reason: ...
- Best class/program so far: ...

## Self-Audit
[Lessons specific + actionable; cause mapped to a stage; honest attribution]
```

## Example Output
```
## Outcome
Down-tiered: I reported an IDOR as High; program accepted but rated Medium. Feedback: "valid, but you
demonstrated a single-record read; bulk-enumeration impact not shown."

## Root-Cause Diagnosis
My mistake (fixable): I proved the minimum (one cross-account read) and articulated escalation only as a
vague aside. The bug is real; the *impact case* was thin. Not out of my control.

## Workflow Stage Responsible
Severity/impact (bugbounty_severity_cvss_impact.md) and report writing — I labeled escalation as
"potential" but didn't make the enumeration impact vivid or evidenced.

## ROI Check
~3h for a Medium — acceptable. Program triages fast; good selection. Keep this program.

## Concrete Changes
1. For IDOR/BOLA, always include a clearly-labeled escalation paragraph quantifying blast radius (e.g.,
   "IDs are sequential → all N users' records reachable"), while still only performing minimal proof.
2. In the severity prompt, explicitly fill the "potential vs proven" section before drafting the report.

## Trend Update
- Acceptance rate: 4/6 valid.
- Common rejection reason: 1 out-of-scope vuln type (now fixed via scope analyzer habit).
- Best class/program so far: access-control on Acme.

## Self-Audit
Both lessons are behavioral and tied to specific stages; attribution is honest (my impact articulation,
not triager error); trend is over 6 reports, not one.
```

## Techniques Used
- **ST-01 (Clear Objective Statement)** — turns outcomes into actionable lessons, not venting.
- **RT-02 (Multi-Dimensional Analysis)** — diagnoses by outcome type across the workflow.
- **QA-02 (Adversarial Thinking)** — forces honest my-mistake-vs-out-of-control attribution.
- **DS-06 (Prioritization Guidance)** — ROI and trends steer where to spend future time.
- **DD-07 (Self-Audit Table)** — verification enforces specific, stage-mapped, evidence-based lessons.
