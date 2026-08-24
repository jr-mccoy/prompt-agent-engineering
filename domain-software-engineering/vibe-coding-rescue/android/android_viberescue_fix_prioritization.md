---
title: "Prioritize Findings From Android Vibe-Rescue Audits Into a Ranked Fix Queue"
category: software-engineering/vibe-coding-rescue/android
description: "Take the findings from android_viberescue_codebase_audit.md and android_viberescue_security_privacy_audit.md and produce a ranked fix queue across four tiers (Tier 0 security-critical, Tier 1 crash/data-loss, Tier 2 fragility/maintenance, Tier 3 cleanup) with per-fix impact × effort × reversibility × blast-radius scoring, test-coverage gap, batch-vs-isolate recommendation, and dependency order. Output is consumable directly by android_viberescue_fix_executor.md."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-03
  - RT-02
  - RT-05
  - QA-01
difficulty: intermediate
tags:
  - vibe-coding
  - android
  - prioritization
  - planning
  - triage
updated: "2026-05-17"
related_prompts:
  - domain-software-engineering/vibe-coding-rescue/android/android_viberescue_codebase_audit.md
  - domain-software-engineering/vibe-coding-rescue/android/android_viberescue_security_privacy_audit.md
  - domain-software-engineering/vibe-coding-rescue/android/android_viberescue_fix_executor.md
  - domain-software-engineering/vibe-coding-rescue/viberescue_decompose_stuck_task.md
---

# Prioritize Findings From Android Vibe-Rescue Audits Into a Ranked Fix Queue

**Purpose:** A vibe-coded Android app coming out of audits will have dozens of findings spanning security, fragility, sprawl, and hygiene. Fixing them in the wrong order — or batching unsafe combinations — makes things worse. This prompt takes raw audit output and produces a four-tier fix queue where each item has explicit impact × effort × reversibility × blast-radius scoring, a test-coverage gap note, a batch-vs-isolate recommendation, and a dependency order. The output is structured so an automated agent (or a careful human) can pop items from the front and feed them straight into `android_viberescue_fix_executor.md`.

**When to use:**
- After running `android_viberescue_codebase_audit.md` and/or `android_viberescue_security_privacy_audit.md`.
- Before beginning any actual fix work.
- Whenever the team needs to communicate to a stakeholder why a specific fix is being done first.

**Don't use when:** You have only one or two findings. Just fix them.

**Audience:** Engineer planning the work, or an agent that will execute fixes in sequence.

**Agent portability note:** Written for any coding agent. The output schema is the contract — keep field names exact so the executor prompt can parse it.

---

## Inputs Required

Refuse to prioritize without 1, 2, and 4.

1. **Codebase audit output.** The full report from `android_viberescue_codebase_audit.md`. Paste as-is, or paste the path if your agent can read it.
2. **Security audit output.** The full report from `android_viberescue_security_privacy_audit.md`. Same.
3. **Optional: wall-diagnosis output.** From `android_viberescue_wall_diagnosis.md`. If primary mode A1–A12 is provided, prioritization weights shift to favor that mode's recovery first.
4. **Stakes and timeline.**
   - Deployment posture (Play Store / internal / prototype).
   - User count (rough).
   - Available engineering capacity (solo / pair / team; hours per week).
   - Timeline pressure (next release date, audit deadline, none).
5. **Optional: blocked fixes.** Findings you've already attempted and abandoned, with reason. Will be downgraded or deferred.
6. **Optional: project rules file.** If one exists (`CLAUDE.md` / `.cursorrules`), paste it. Fixes that violate the rules will be flagged.

---

## Instructions

### Step 1 — Merge and deduplicate findings

Read both audit reports. Build a single working list of findings. For each, capture:

- ID (assign a stable identifier: `SEC-001`, `FRAG-014`, etc.)
- Source audit (security / fragility)
- File:line
- Category (from the audit's category schema)
- Severity (from the audit)
- Confidence (from the audit)
- AI-pattern tag (from the audit)

Deduplicate: if both audits flagged the same file:line with overlapping concern, merge into one finding and tag it `source: both`. Keep the higher severity.

### Step 2 — Score each finding on four axes

Assign 1–5 on each axis:

| Axis | 1 (low) | 3 (medium) | 5 (high) |
|------|---------|------------|----------|
| **Impact if not fixed** | Hygiene; no user-visible effect | Fragility under specific conditions; possible regression | Active security hole, crash, data loss, or compliance failure |
| **Effort to fix** | <1 hour, single file, mechanical | 1–4 hours, 2–5 files, requires care | >4 hours, many files, requires design |
| **Reversibility** | Trivial revert; isolated change | Revertible but touches shared code | Hard to revert; data migration, schema change, or coordinated release |
| **Blast radius** | One screen / one feature | One module / one user flow | App-wide / cross-cutting (auth, DI, navigation, build) |

Multiply: **priority_score = (Impact × Reversibility) / Effort × Blast_radius_weight**, where blast_radius_weight = 1 for low, 1.5 for medium, 2 for high.

(The formula's purpose is to surface high-impact, easy-to-revert, low-effort fixes first while still giving cross-cutting fixes their due weight. It's a ranking heuristic, not a metric — sanity-check the ordering.)

### Step 3 — Assign to a tier

- **Tier 0 — Security-critical, must fix now:** Any Critical severity from the security audit. Any auth bypass. Any data exposure. Any exported component without justification that's reachable. Any cleartext credential transmission. Time-bounded: do not ship another release until Tier 0 is clear.
- **Tier 1 — Crash or data-loss risk:** Critical severity from the fragility audit. Lifecycle violations that lose user data. Coroutine scope leaks that crash on rotation. Hilt graph errors that fail at runtime. Anything that breaks core flows under realistic conditions.
- **Tier 2 — Fragility / maintenance burden:** High severity from either audit. Mixed-API patchwork. Compose state sprawl. Duplication / sprawl. Test gaps that allow Tier 1 issues to land silently.
- **Tier 3 — Cleanup:** Medium severity. Null-safety idiom inconsistencies. Dead code. Manifest hygiene without security implications.

Within each tier, sort by priority_score descending.

### Step 4 — Identify batch-safe vs isolate-required fixes

For each finding, recommend **BATCH** or **ISOLATE**.

- **BATCH** is appropriate when: same file or same cluster of files, same category, low blast radius, mechanical change. Example: fixing 12 `Log.d` calls that leak PII across the codebase.
- **ISOLATE** is required when: high blast radius, cross-module, security-relevant, requires architectural decision, or the audit confidence was Medium / Low. Example: replacing hand-rolled auth with Credential Manager — one PR.

Default to ISOLATE for Tier 0. Most Tier 0 should not be batched.

### Step 5 — Identify dependency order

Some fixes block others. Build a dependency graph:

- Fixes that change DI bindings (Hilt) block fixes that depend on those bindings.
- Fixes that change navigation block fixes that add screens.
- Fixes that consolidate duplicates (delete one of two repositories) block fixes inside the deleted one.
- Fixes that adopt EncryptedSharedPreferences block other fixes that store sensitive data.
- Fixes that update the version catalog or BOM block fixes that depend on updated library versions.

Output the dependency graph as a list of `(must-finish-first, then)` pairs.

### Step 6 — Identify test-coverage gaps per fix

For each Tier 0 and Tier 1 fix:

- Does a test exist that would have caught this issue?
- If not, what test should be written BEFORE the fix? (This is the test the executor prompt will write first.)

Examples:
- Tier 0 finding: `exported="true"` on BillingActivity → test: an instrumentation test that asserts the manifest's exported flags match the expected set.
- Tier 1 finding: rotation loses state on profile screen → test: a Compose UI test (or instrumentation test) that rotates and asserts state preservation.

If no realistic test can be written, say so and require human review on the fix.

### Step 7 — Flag fixes that may require human-only judgment

Some fixes should not be agent-executed:

- Migrations that touch a Room schema with existing user data (need a verified migration).
- Auth refactors that change how existing sessions are validated (need staged rollout).
- Permission removals (need user-impact assessment).
- Backup / restore behavior changes.
- Anything where input 5 (blocked fixes) shows prior attempts failed.

Mark these `human_required: true`.

### Step 8 — Build the queue

Emit the queue in execution order: Tier 0 first (in dependency order, then priority_score), then Tier 1, then Tier 2, then Tier 3. Each entry has the full field set.

If the total queue is huge (>50 items), cap each tier at 20 in the main output and appendix the rest. Note explicitly.

### Step 9 — Sanity check and dual-failure pass

- **Harmful direction:** Did any Tier 0 get misplaced into a lower tier because the audit confidence was Medium? Re-check Critical-severity items.
- **Unhelpful direction:** Does the queue lead with 30 batch-safe Tier 3 cleanup fixes? Re-check tier assignments.

### Step 10 — Verify and output

Run the verification checklist.

---

## Constraints

### Must
- Merge both audits into one queue.
- Score every finding on impact, effort, reversibility, blast radius.
- Assign every finding to Tier 0, 1, 2, or 3.
- Recommend BATCH or ISOLATE per finding.
- Build a dependency graph for fixes that block other fixes.
- Identify test-coverage gaps for Tier 0 and Tier 1.
- Flag `human_required: true` where agent execution is unsafe.
- Output is parseable: stable field names, consistent IDs, machine-readable structure.

### Must Not
- Reorder Critical-severity security findings out of Tier 0 because they're expensive.
- Batch Tier 0 fixes by default.
- Omit dependency relationships ("just go in priority order") when fixes interact.
- Reference Claude-Code-specific tool names.
- Recommend a fix that violates the project's rules file (input 6) without flagging the conflict.

---

## False-Positive Prevention (MUST follow)

DON'T:
- Treat Medium-severity security findings as Tier 0. Tier 0 is Critical only.
- Assume effort is "1 hour" without considering test coverage gaps that must be filled first.
- Place all duplication findings in Tier 2 — if the duplication is in an auth path, it may be Tier 0.
- Forget that the rules-file fix (`android_viberescue_rules_file.md`) is often the right Tier 2 because it prevents regression.
- Batch fixes across modules when the project doesn't have module-isolated tests.

DO:
- Re-read the audit confidence label before tiering — Low-confidence findings may need verification before fixing.
- When in doubt on BATCH vs ISOLATE, choose ISOLATE.
- Surface "no test possible" as a first-class output, not a silent omission.
- Acknowledge when the queue exceeds realistic engineering capacity (input 4) and recommend descoping.

---

## Dual-Failure Prevention (QA-20)

HARMFUL failure: Tier 0 fix executed before its dependency, leaving a half-applied security change that's worse than the original.

UNHELPFUL failure: Queue of 200 items with no clear "do this first," team paralyzed.

Quality check: A senior engineer reads the top 5 items in Tier 0, agrees with the order, and could hand item #1 to an executor agent without further triage.

---

## Output Format

```markdown
# Android Vibe-Rescue Fix Queue — [App name]

## Inputs Summary
- Fragility findings: [N]
- Security findings: [N]
- Deduplicated: [N]
- Stakes / capacity: [from input 4]

## Tier Summary
- Tier 0 (security-critical): [N items, est. [N] engineer-hours]
- Tier 1 (crash / data loss): [N items, est. [N] hours]
- Tier 2 (fragility / maintenance): [N items, est. [N] hours]
- Tier 3 (cleanup): [N items, est. [N] hours]

## Dependency Graph
- SEC-003 must finish before SEC-007 (binding change required for token storage)
- FRAG-012 must finish before FRAG-018 (consolidation deletes file FRAG-018 lives in)
- [...]

## Queue (execution order)

### Tier 0

#### Fix SEC-001 — [Short title]
- **Source:** security audit | fragility audit | both
- **File:** path/to/File.kt:42-58
- **Category:** [from audit]
- **Severity (audit):** Critical
- **Confidence (audit):** High
- **AI-pattern signal:** yes / neutral
- **Score:** impact=5, effort=2, reversibility=5, blast=2 → priority_score=12.5
- **Tier:** 0
- **Batch / isolate:** ISOLATE
- **Depends on:** none | [other fix IDs]
- **Test-coverage gap:** [test to write before fixing, or "no realistic test possible — requires human review"]
- **human_required:** false | true (reason)
- **Fix direction (from audit):** [verbatim from audit's remediation field]
- **Suggested commit message:** "[tier-tag] [short description]"

#### Fix SEC-002 — [...]
[...]

### Tier 1
[Same schema.]

### Tier 2
[Same schema.]

### Tier 3
[Same schema.]

## Descoping Recommendation
[If queue exceeds capacity: list what to defer and why.]

## Conflicts With Project Rules
[If input 6 provided and any fix violates it: list with rationale.]

## Recommended Next Step
Run `android_viberescue_fix_executor.md` on the first item in Tier 0 (or the first item with no unmet dependencies).
```

---

## Verification

- [ ] Both audits merged and deduplicated.
- [ ] Every finding has scores on all four axes.
- [ ] Every finding tiered.
- [ ] BATCH / ISOLATE assigned per finding.
- [ ] Dependency graph present.
- [ ] Test-coverage gap noted for every Tier 0 and Tier 1 fix.
- [ ] human_required flag set where appropriate.
- [ ] Queue capped per tier with appendix overflow if huge.
- [ ] Conflicts with rules file flagged if input 6 provided.

---

## Techniques Used

- **ST-01 (Clear Objective):** Output is one executable queue, not a discussion of priorities.
- **ST-02 (Structured Sequential Instructions):** Ten steps drive merge → score → tier → batch → dependencies → tests → human-gate → queue → sanity → verify.
- **ST-03 (Output Format Specification):** Strict schema so the executor prompt can consume directly.
- **CM-02 (Constraint Specification):** Must Not block prevents misordering and unsafe batching.
- **DS-03 (Multi-Criteria Ranking):** Four-axis scoring with explicit formula and tier mapping.
- **RT-02 (Decomposition):** Tiering + dependency graph break the work into independently-executable units.
- **RT-05 (Evidence-Based Reasoning):** Tiering grounded in audit evidence (severity + confidence) rather than vibes.
- **QA-01 (Self-Verification):** Verification checklist + dual-failure prevention prevents misordering and queue-paralysis.
