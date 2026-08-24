---
title: "Compliance Training Module Designer (Generic)"
category: education-teaching/higher-ed-corporate
description: "Design a compliance training module that satisfies legal/regulatory documentation requirements (which the user must supply for their jurisdiction) while still producing actual behavior change — not just a click-through."
techniques:
  - ST-02
  - CM-02
  - DS-01
  - OC-01
  - QA-01
difficulty: intermediate
tags:
  - corporate-training
  - compliance
  - regulatory
  - legal-required
  - behavior-change
  - ethics
  - safety
updated: "2026-05-09"
related_prompts:
  - domain-education-teaching/higher-ed-corporate/hecorp_microlearning_module.md
  - domain-education-teaching/higher-ed-corporate/hecorp_corporate_onboarding_program.md
  - domain-education-teaching/higher-ed-corporate/hecorp_async_lms_module_designer.md
---

# Compliance Training Module Designer (Generic)

## Objective

Design a compliance training module that (a) meets the legal and documentation requirements of the user's jurisdiction and industry — which the user must supply, since regulations vary — and (b) produces actual behavior change, not just a click-through completion record.

> **Important:** This prompt does not assert specific regulatory requirements for any specific jurisdiction. The user must supply the controlling legal/regulatory specification (statute, rule, policy text, or compliance counsel guidance) before the module can be designed. The prompt will treat that specification as authoritative for content and documentation requirements.

## When to Use

- Annual or new-hire required training on a regulated topic (e.g., harassment prevention, safety, data privacy, ethics, anti-bribery, conflicts of interest, information security)
- Replacement of a stale generic vendor module
- Industry- or role-specific compliance not covered by an off-the-shelf course
- Post-incident retraining where the prior training didn't transfer

## When NOT to Use

- Topic isn't actually compliance — use `hecorp_async_lms_module_designer.md`
- Quick refresher only — use `hecorp_microlearning_module.md`
- Onboarding overall — use `hecorp_corporate_onboarding_program.md`

---

## Inputs Needed

- **Compliance topic:** [...]
- **Jurisdiction(s) covered:** [Country, state/province, locality — list each]
- **Industry / sector:** [Healthcare, finance, government, education, manufacturing, etc.]
- **Controlling regulation or policy text:** [User must paste or summarize the statute / rule / policy that governs — the prompt will reference this rather than inventing requirements]
- **Audit/documentation requirements:** [What the regulator needs to see — completion records, attestation, time-stamped logs]
- **Learner population:** [Roles, locations, languages]
- **Frequency:** [One-time / annual / on event]
- **Time budget:** [How long the regulation or your organization permits]
- **Learning outcomes desired beyond compliance:** [What you want learners to actually do]
- **Prior incident / risk signal:** [Any specific behaviors driving the need]

---

## Instructions

### Step 1: Confirm Authoritative Source

Before designing content:

- [ ] User has provided the controlling regulation, policy, or counsel guidance
- [ ] If user is uncertain about jurisdiction or controlling text, **stop and request it**
- [ ] Distinguish between *minimum legal requirement* and *organization's preferred standard* (the latter often exceeds the former)

The prompt does NOT generate specific regulatory citations from training data — those must come from the user's authoritative source.

### Step 2: Separate Two Outcomes

Compliance training has two distinct outcomes that often get conflated:

| Outcome | What it requires |
|---------|------------------|
| **Documentation** — proving training happened | Completion record, attestation, time-stamped log, identity verification per regulation |
| **Behavior change** — learners actually do the right thing | Realistic scenarios, decision practice, transfer cues, manager reinforcement |

Design for both. Most compliance training fails at the second.

### Step 3: Map Required Content From Authoritative Source

From the regulation or policy the user supplied, extract:

- Topics that must be covered (cite source)
- Specific definitions that must be taught
- Examples or scenarios required
- Reporting / escalation channels that must be named
- Any required disclosures or learner attestations

If the source is silent on something, do not invent it.

### Step 4: Add Behavior-Change Layer

For each required topic, design:

- **Recognize** — scenarios where the learner correctly identifies the issue
- **Decide** — branching scenario where the learner makes the call
- **Act** — what to do, who to tell, how to escalate
- **Recover** — what if the learner is wrong, what if they're the target, what if they witness

Use realistic scenarios from the learner's actual work, anonymized. Avoid corporate-stock-photo case studies.

### Step 5: Knowledge Check Items With Real Stakes

Items must:

- Test the actual decision the learner needs to make
- Have a defensible correct answer per the source regulation/policy
- Not be trivially passable by elimination
- Provide feedback that explains *why* per the source
- Not punish honest mistakes — feedback teaches

A passing threshold (e.g., 80%) tied to documentation policy is typical; confirm with policy.

### Step 6: Documentation & Audit Trail

Specify what must be captured:

- Learner identity verification per policy (SSO, attestation checkbox, witnessed)
- Time-stamped completion
- Content version (so you can prove what was trained on what date)
- Score / pass record if required
- Retention period per policy
- Re-training trigger conditions

Output a documentation specification that the LMS administrator and compliance officer can validate against the regulation.

### Step 7: Manager & Reinforcement Plan

Compliance training that ends at the LMS rarely transfers. Build:

- Manager talking points (3–5 sentences) for the next team meeting
- A short manager prompt to use in 1:1s
- A performance-support job aid for the moment of decision
- Reporting channel reminders (posters, intranet pinned post)
- Real-world reinforcement: how the org responds when issues are raised (signal that reporting is safe)

### Step 8: Reporting & Retaliation Safeguards

If the topic involves reporting (harassment, ethics, safety), make explicit:

- Multiple reporting paths (manager, HR, hotline, ombuds, external)
- Anti-retaliation policy named and linked
- What the learner should expect after reporting
- Confidentiality boundaries (what can be confidential, what cannot)

These elements are often required by regulation; verify against source.

### Step 9: Translation, Localization, Accessibility

- Translation requirements per jurisdiction and population
- Cultural adaptation of examples (a US-only scenario may not land in EU/APAC)
- Accessibility baseline: captions, alt text, screen-reader, color contrast
- Time-limit accommodations
- Plain-language reading level

### Step 10: Annual Revision Cycle

- Trigger to update: regulation change, incident, audit finding, vendor update
- Owner of update
- Version control on content and item bank
- Audit-ready archive of prior versions

### Step 11: Pre-Launch Legal/Compliance Review

- [ ] Compliance counsel reviewed against authoritative source
- [ ] Documentation spec validated by audit team
- [ ] HR/legal sign-off recorded
- [ ] Vendor / off-the-shelf content gaps documented
- [ ] Translations reviewed by qualified speakers
- [ ] Accessibility checker passed

This step is not optional and is not the prompt's job — it's the user's.

---

## Output Format

1. Authoritative source confirmation note
2. Documentation vs. behavior-change outcomes split
3. Required content map (cited to source)
4. Behavior-change layer (recognize / decide / act / recover)
5. Knowledge-check items + feedback
6. Documentation & audit-trail specification
7. Manager & reinforcement plan
8. Reporting & retaliation safeguards
9. Translation/localization/accessibility plan
10. Annual revision cycle plan
11. Pre-launch review checklist (handoff to compliance/legal)

---

## False-Positive Prevention

❌ **DON'T:**
- Cite regulations the user didn't provide — invented citations are dangerous
- Conflate "training completed" with "learner can act correctly"
- Use corporate-stock scenarios that learners will never see at work
- Skip manager reinforcement and call it done at the LMS
- Forget translation and accessibility — they're often legally required, not optional
- Allow "click-next" passability

✅ **DO:**
- Anchor on authoritative source supplied by user
- Design for documentation AND behavior
- Use realistic, role-specific scenarios
- Specify documentation/audit-trail rigorously
- Pair with manager reinforcement and reporting infrastructure
- Send to compliance/legal review before launch

---

## Quality Indicators

- [ ] Authoritative source confirmed and cited
- [ ] Required content matches source
- [ ] Behavior-change layer present, not only knowledge checks
- [ ] Documentation spec defensible
- [ ] Reporting paths and anti-retaliation explicit
- [ ] Reinforcement plan paired
- [ ] Compliance/legal review handoff ready

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **ST-02** | Source → required content → behavior layer → docs → reinforcement → review pipeline. |
| **CM-02** | Constrains content to user-supplied authoritative source; refuses to invent regulations. |
| **DS-01** | Compliance-training frame separates documentation from behavior-change outcomes. |
| **OC-01** | Documentation spec and required-content map enforce auditable output. |
| **QA-01** | Pre-launch legal/compliance review and annual revision cycle close the loop. |
