---
title: "Safety and Tool-Fit Check Before Activating a Browser Automation"
category: productivity/automation
description: "A go/no-go check that runs before any browser automation is activated in production: blast-radius scoring, authority review, credential handling, ToS compliance, rollback, and failure detection — so the automation either launches with defenses in place or doesn't launch."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - browser-automation
  - safety-check
  - pre-flight
  - go-no-go
  - production-readiness
updated: "2026-04-20"
related_prompts:
  - domain-productivity/automation/browserauto_recording_blueprint.md
  - domain-productivity/automation/browserauto_weekly_audit.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_code_footgun_detector.md
  - domain-productivity/operating-cadence/cos_authority_boundaries.md
---

# Safety and Tool-Fit Check Before Activating a Browser Automation

**Objective:** A single go/no-go check that runs before any recorded, scripted, or AI-driven browser automation is activated on a real schedule. The check scores blast radius, confirms authority, inspects credential handling, verifies ToS compliance, validates rollback, and tests failure detection. Output: a clear launch / hold decision and, if hold, the exact remediation list.

**When to use:** Before flipping any browser automation from manual-trigger or dry-run to live schedule. Before extending an automation's scope (new sites, new actions, higher frequency). After any tool upgrade that changes the automation's behavior. Periodic re-review (quarterly) of existing live automations.

**Audience:** Automation engineer, ops lead, or reviewer acting as a second set of eyes. Meant to be run as a peer review, even when "peer" is the same user coming back the next day with fresh attention.

---

## Inputs Required

1. **The automation description** — what it does, on what trigger, on what site(s).
2. **The recording blueprint** (`browserauto_recording_blueprint.md` output) or equivalent design doc.
3. **Dry-run results** — how many runs, what failures, what success rate.
4. **Credential handling** — how the automation authenticates (SSO, stored password, API token, session cookie), where credentials live, who can rotate them.
5. **ToS / legal review status** — has the site's ToS been read for this use; is authenticated access in-scope for the account type.
6. **Ownership** — named human responsible when the automation fails.
7. **Rollback plan** — how to stop the automation and continue manually.

Refuse to launch the check if dry-run results are not available. Design review without execution data is incomplete.

---

## Instructions

### Step 1 — Score blast radius

For a wrong action, score the consequence on three dimensions:

- **Data scope:** touches only user's own data / touches team data / touches customer data / touches external systems.
- **State change:** read-only / writes internal / writes to external party / triggers irreversible action (payment, send, delete).
- **Reversibility:** instant undo / minutes to undo / hours to undo / not practically reversible.

Derive a blast-radius tier:
- **Green:** read-only, own data, reversible.
- **Yellow:** writes to internal system, reversible in hours.
- **Red:** external state change or irreversible action.

The tier determines the depth of the rest of the check. Green automations get a lighter review; Red automations need every section satisfied before launch.

### Step 2 — Authority check

For the actions the automation will take:
- Does the user have authority for these actions in the first place (independent of automation)? If not, stop — the automation cannot confer authority the user doesn't have.
- Does the organization's policy or the agent's authority map (reference `cos_authority_boundaries.md`) explicitly allow these actions unattended?
- For Yellow/Red: is there a named approver who has signed off on automating this action, not just doing it manually?

Authority to act manually is not the same as authority to act unattended on a schedule. Make the distinction explicit.

### Step 3 — Credential handling review

- **Storage:** are credentials stored in a vault (1Password, AWS Secrets Manager, Vault, managed secrets)? Plaintext in scripts, config files, or recordings is a fail.
- **Scope:** does the credential have the minimum access needed? Over-privileged credentials expand blast radius.
- **Rotation:** what happens when the credential rotates — does the automation handle it gracefully, or does it fail silently?
- **Audit trail:** does the site log this account's actions? Can the actions be distinguished from manual use?
- **Account type:** if this is a personal account being used for org work, flag it as a separate concern — personal accounts often lack the audit / review path.

### Step 4 — ToS and legal review

- Has the site's ToS been checked for this use? Many sites prohibit unattended / automated access under standard ToS; some have enterprise ToS that allow it.
- If scraping: is there rate-limit language? Respect it explicitly.
- If the site is owned by a partner / vendor / customer, has written or informal permission been obtained?
- If regulated data is touched (PII, PHI, financial records), is the automation path covered by the existing compliance posture, or is a new review needed?

A ToS failure is a hold. Don't launch and hope.

### Step 5 — Rollback and manual continuity

- **Stop-button:** is there a single action that pauses the automation — a schedule toggle, a killswitch, a flag file?
- **Runbook:** if the automation is down, can the user (or a colleague) continue manually from the runbook? Is the runbook current?
- **State recovery:** if the automation is mid-run and stops, is the state recoverable? A half-run that left partial state is the common incident.

For Red tier: the runbook is non-optional. Yellow tier: runbook recommended. Green tier: a note on manual continuity is enough.

### Step 6 — Failure detection

- **What "failed" means:** non-zero exit, no output produced, duration exceeded, error alert surfaced, downstream consumer didn't receive.
- **Alert path:** where does a failure get noticed? Silent failures are the default — make explicit how failure reaches a human.
- **Degraded-success detection:** not all failures are loud. If the automation runs but produces empty / wrong output, who notices? Sampling review is the common defense.

### Step 7 — Drift / re-review schedule

Sites change. Set a re-review trigger:
- Time-based (quarterly default).
- Event-based (failure rate climbs, downstream consumer complains, ToS changes, credentials rotated to a new model).

An automation with no re-review trigger is a future incident.

### Step 8 — Go / hold decision

Based on Steps 1–7, a go/hold verdict. Green tier: go if all sections are passed. Yellow tier: go if all sections pass AND dry-run success rate is ≥95% over at least 3 runs. Red tier: go only if all sections pass, dry-run success rate is ≥98% over at least 5 runs, named approver has signed off, runbook is current, and rollback is tested.

If hold, produce the exact remediation list. Do not issue a "launch, but fix soon" verdict. Launch with deferred remediation becomes permanent.

---

## Constraints

### Must
- Score blast radius on all three dimensions before anything else.
- Distinguish authority-to-act from authority-to-act-unattended.
- Check credential storage, scope, rotation, and audit.
- Verify ToS and legal posture.
- Confirm rollback and runbook status appropriate to tier.
- Define failure detection with an explicit human-reachable alert.
- Set a re-review trigger.

### Must Not
- Issue "launch, but fix soon" verdicts. Every remediation is blocking.
- Accept plaintext credentials in any form.
- Accept a ToS violation on the grounds that "everyone does it."
- Let the automation confer authority the user doesn't have.
- Skip rollback for Red tier automations.
- Treat dry-run green as a substitute for the other checks.

---

## False-Positive Prevention

1. **Don't down-tier an automation to avoid the checks.** If the action touches external state or is hard to reverse, it's Red tier regardless of how low-risk it feels.
2. **Don't accept verbal ToS allowance.** If the site's ToS prohibits automation and the vendor "said it's fine," require written confirmation.
3. **Don't confuse retrying with success.** If the dry-run takes 5 retries to succeed, the live automation will fail more often than the success rate suggests.
4. **Don't approve Red tier on an unmonitored stack.** An automation with no observability is always a hold for Red.
5. **Don't skip re-review triggers.** Every long-running automation eventually goes wrong in a way the original design didn't anticipate.
6. **If the same user did the recording and the safety check,** the review is not independent. Wait a day, bring a colleague, or have a structured second pass.

---

## Output Format

```
# Safety check — [automation name]

## Blast radius
- Data scope: [own / team / customer / external]
- State change: [read-only / internal-write / external-write / irreversible]
- Reversibility: [instant / minutes / hours / not practically]
- **Tier: Green / Yellow / Red**

## Authority
- User authorized to act manually: Y/N
- Policy / authority-map allows unattended: Y/N
- Named approver (for Y/R): [name, date]

## Credential handling
- Storage: [vault name / FAIL if plaintext]
- Scope / least privilege: Y/N
- Rotation-safe: Y/N
- Audit trail present: Y/N
- Account type: [org / personal + flag]

## ToS / legal
- ToS reviewed: [yes/no + link to relevant section]
- Rate limit respected: Y/N
- Partner / vendor permission (if applicable): [status]
- Regulated data: [none / covered / new review needed]

## Rollback / manual continuity
- Stop-button: [what / where]
- Runbook: [current / stale / missing]
- State recovery: [covered / not covered]

## Failure detection
- Definition of failure: [list]
- Alert path: [to whom, how fast]
- Degraded-success check: [sampling / none]

## Re-review
- Time-based trigger: [date]
- Event-based triggers: [list]

## Dry-run success rate
[N runs, X successes, Y% — compared to tier threshold]

## Verdict
- [ ] Go
- [ ] Hold — remediations required:
  1. [item]
  2. [item]
```

---

## Verification

- [ ] Blast-radius tier matches the action set, not the feel.
- [ ] Authority is checked for unattended operation, not just manual.
- [ ] Credential handling has no plaintext.
- [ ] ToS status is documented.
- [ ] Rollback and runbook appropriate to tier.
- [ ] Failure detection reaches a human.
- [ ] Re-review trigger is set.
- [ ] Verdict is a clean go or hold — no deferred remediation.
