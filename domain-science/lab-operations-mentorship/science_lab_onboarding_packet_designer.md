---
title: "Lab Onboarding Packet Designer"
category: science/lab-operations-mentorship
description: "Design a new-trainee onboarding packet covering safety/EHS, software and compute setup, data-management and notebook conventions, authorship norms, communication expectations, and the mentoring compact, plus a first-30/60/90-day plan."
techniques:
  - ST-01
  - ST-03
  - RT-03
  - QA-01
  - QA-02
  - CM-02
difficulty: advanced
tags:
  - onboarding
  - lab-operations
  - data-management
  - notebook-conventions
  - authorship-norms
  - safety-training
  - mentoring-compact
  - 30-60-90-plan
updated: "2026-06-26"
related_prompts:
  - domain-science/lab-operations-mentorship/science_individual_development_plan_drafter.md
  - domain-science/lab-operations-mentorship/science_one_on_one_mentorship_session_plan.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# Lab Onboarding Packet Designer

**Objective:** Design a structured onboarding packet that gets a new trainee productive and oriented while setting clear, humane expectations from day one. The packet routes safety/EHS and required training to the institution, walks through software and compute setup, codifies data-management and notebook conventions, states authorship and attribution norms, sets communication expectations, and includes the mentoring compact. The output is a packet checklist plus a first-30/60/90-day plan, with all institution-specific items marked `[user-supplied]`.

**When to use:** When a trainee is joining a lab and the lab wants a repeatable, dignity-preserving onboarding rather than ad-hoc, word-of-mouth ramp-up.

**Required inputs:**
- **Discipline.** The lab's field, so safety, tooling, and notebook conventions fit the work (wet-lab vs. computational vs. field differ substantially).
- **Career stage.** The incoming trainee's stage, so expectations and the 30/60/90 plan are calibrated.
- **Lab modality.** Wet-lab, dry/computational, field, or mixed — drives which sections are emphasized.

**Optional inputs:**
- Existing lab tooling (version control, data store, electronic lab notebook, compute cluster, chat).
- Existing data-management plan or reproducibility conventions to reference.
- Known institutional training requirements (only as the lab can supply them).
- Lab norms already in place the lab wants to preserve.

**Constraints — Must:**
- Route all safety/EHS and compliance training (biosafety, chemical, radiation, animal/IACUC, human-subjects/IRB, lab-specific) to the institution as required steps; provide the checklist structure, not invented policy content.
- Cover data-management and notebook conventions concretely (where data lives, naming, backups, electronic lab notebook expectations, version control) and cross-reference reproducibility practice.
- State authorship and attribution norms up front (e.g., a contribution/CRediT-style approach, when authorship is discussed, how credit is handled), consistent with ICMJE-style authorship principles where applicable.
- Set communication and meeting expectations (response-time norms, which channels, 1:1 and lab-meeting cadence, how to ask for help).
- Include the mentoring compact (reciprocal trainee/mentor commitments) so expectations are mutual from the start.
- Provide a first-30/60/90-day plan with realistic, stage-appropriate milestones and an early low-stakes win.

**Constraints — Must Not:**
- Do not invent institutional policies, named people, performance facts, or career statistics. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not state specific safety procedures, training durations, or compliance requirements from memory; route them to the institution as `[user-supplied]`.
- Do not present authorship norms as fixed rules where they are lab-specific; mark lab decisions `[user-supplied]`.
- Do not use hype language ("novel," "groundbreaking," "first-ever," "gold standard") in any drafted text.
- Do not omit well-being and where-to-get-help orientation from the packet.

**Instructions:**

1. **Confirm scope.** Capture discipline, career stage, and lab modality. Note existing tooling and conventions if supplied.
2. **Safety & required training section.** Build a checklist of training categories relevant to the modality, each routed to the institution with `[user-supplied]` placeholders for specifics and sign-off. Emphasize that no bench/field work begins before required clearances.
3. **Software & compute setup.** List accounts, access, version control, electronic lab notebook, compute/cluster access, and core tools, in setup order, with a "you have access when…" check for each. Mark lab-specific endpoints `[user-supplied]`.
4. **Data-management & notebook conventions.** Specify where raw and processed data live, naming and folder conventions, backup expectations, notebook standards, and version control practice. Cross-reference the reproducibility self-audit so good record-keeping starts on day one.
5. **Authorship & attribution norms.** State how contribution and credit are handled, when authorship conversations happen, and the contribution-tracking approach (CRediT-style). Mark lab-specific decisions `[user-supplied]` and align to ICMJE-style principles where relevant.
6. **Communication & expectations.** Set channel norms, reasonable response-time expectations, meeting cadence (1:1s, lab meeting), and how to ask for help without it being a failure. Keep expectations explicit and reciprocal.
7. **Mentoring compact.** Embed reciprocal trainee/mentor commitments (modeled on the AAMC mentor–mentee compact concept), and point to the IDP process for goal-setting.
8. **Well-being & support orientation.** Include where to get help (institutional counseling/EAP/health services, ombuds, key contacts) marked `[user-supplied]`, and a note that asking for support is expected and normal — this is orientation, not a clinical resource.
9. **First-30/60/90-day plan.** Lay out stage-appropriate milestones for each window, including an early low-stakes win, a checkpoint conversation per window, and what "on track" looks like — framed as support, not surveillance.

**Output format (locked):**

```
## Packet Overview
- Discipline / subfield: [...]
- Lab modality: [wet / dry / field / mixed]
- Incoming trainee stage: [...]

## 1. Safety & Required Training (routed to institution)
| Training / clearance | Required before | Status | Sign-off |
|---|---|---|---|
[all specifics [user-supplied]]

## 2. Software & Compute Setup
| Item | Setup step | "You have access when…" | Notes |
|---|---|---|---|

## 3. Data-Management & Notebook Conventions
- Raw data location: [...]
- Naming / folder convention: [...]
- Backup expectation: [...]
- Notebook standard (ELN/paper): [...]
- Version control: [...]
- (See reproducibility self-audit)

## 4. Authorship & Attribution Norms
- Contribution model (CRediT-style): [...]
- When authorship is discussed: [...]
- Credit & acknowledgment: [...]
[lab-specific = [user-supplied]]

## 5. Communication & Expectations
- Channels & response-time norms: [...]
- Meeting cadence (1:1 / lab meeting): [...]
- How to ask for help: [...]

## 6. Mentoring Compact
**Trainee commits to:** [...]
**Mentor commits to:** [...]
- Goal-setting via IDP: [link/process]

## 7. Well-Being & Support Orientation
- Where to get help: [[user-supplied]]
- Note: asking for support is expected; this packet is orientation, not a clinical resource.

## 8. First 30 / 60 / 90-Day Plan
| Window | Milestones | Early win | Checkpoint | "On track" looks like |
|---|---|---|---|---|
| Day 30 | | | | |
| Day 60 | | | | |
| Day 90 | | | | |
```

**Reporting-standard alignment:** No formal reporting standard; aligns to ICMJE-style authorship principles and CRediT contribution roles for attribution, FAIR-oriented data-management and reproducibility practice for the conventions section, the AAMC mentor–mentee compact concept, and CIMER/Entering Mentoring expectation-aligning competencies. Institution-specific safety/EHS and compliance content is deferred to the institution.

**Verification checklist (before delivering):**
- [ ] Discipline, career stage, and lab modality captured before tailoring sections.
- [ ] All safety/EHS and compliance specifics routed to the institution as `[user-supplied]`.
- [ ] Data-management and notebook conventions are concrete and cross-reference reproducibility.
- [ ] Authorship/attribution norms stated up front, with lab-specific items marked `[user-supplied]`.
- [ ] Communication expectations and meeting cadence are explicit and reciprocal.
- [ ] Mentoring compact embedded with both-sides commitments.
- [ ] Well-being/support orientation present with routing and a normalize-asking note.
- [ ] 30/60/90 plan is stage-appropriate, includes an early win, and is framed as support not surveillance.
- [ ] No invented policies, names, performance facts, or career stats; gaps marked `[user-supplied]`.
- [ ] No hype adjectives in drafted text.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Fabricated compliance | Specific safety/training rules asserted as fact | Route every safety/EHS item to the institution as `[user-supplied]` |
| Tooling mismatch | Generic setup steps that don't match the lab's stack | Use `[user-supplied]` endpoints and "you have access when…" checks |
| Late authorship surprise | Packet silent on credit until a dispute arises | Require an up-front authorship/attribution section (CRediT/ICMJE-aligned) |
| Surveillance plan | A 30/60/90 plan that reads as a performance trap | Frame milestones as support, include checkpoints and an early win |
| Hidden expectations | Norms "everyone just knows" left unwritten | Make communication, response-time, and help-seeking norms explicit |
