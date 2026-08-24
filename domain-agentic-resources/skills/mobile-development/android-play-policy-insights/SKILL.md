---
name: android-play-policy-insights
description: Automated auditor designed to verify Android applications against Google Play Policy domains. It cross-references static code analysis with Play Store declarations to generate deterministic compliance reports, identifying undeclared data collection, architectural risks, and missing disclosures across Permissions and APIs Hygiene, User Account and Identity, and Data Safety and Privacy domains.
license: Complete terms in LICENSE.txt
metadata:
  author: Google LLC
  last-updated: '2026-07-13'
  upstream: https://github.com/android/skills
  upstream-path: play/play-policy-insights
  upstream-commit: 23d9eae21a4bfe0209e5b678f0ebe931e3c7dff4
  upstream-synced: '2026-08-02'
  keywords:
  - account deletion
  - accessibility api
  - all files access
  - audio recording
  - audit
  - compliance
  - contacts access
  - data disclosure
  - data safety
  - data safety label
  - data transmission
  - demo credentials
  - exact alarm
  - foreground services
  - location access
  - login credentials
  - manifest hygiene
  - package visibility
  - permissions hygiene
  - photo and video access
  - photopicker
  - play policy
  - pre-submission audit
  - privacy policy
  - prominent disclosure
  - restricted permissions
  - scoped storage
  - sms and call log
  - static analysis
  - target sdk
  - user consent
---

# Play Policy Insights: data safety, login credentials, and restricted permissions

You must audit Android apps for three specific policy domains. You must check
data safety, demo login credentials, and restricted permissions.

## Path Resolution

*   **repo_root**: Absolute path to the directory containing this `SKILL.md`.
*   **app_dir**:: Absolute path to the directory containing app's code.
*   **temp_dir**: Absolute path to the scratch directory at the workspace root.
    It is located at `.scratch/play_policy_insights_<uuid>`. **Containment
    Mandate**: You must confine all file system writes, intermediate artifacts,
    and logs strictly to this directory. This ensures the skill remains portable
    and safe across diverse execution environments, including local harnesses
    and CI/CD pipelines, by avoiding reliance on system-level temporary paths or
    user home directories.

## Critical mandates

-   **Execution Mode Awareness** Before starting Phase 2, evaluate if your
    execution environment provides a tool to spawn or delegate tasks to
    general-purpose sub-agents (e.g., tools often named `invoke_agent`,
    `delegate_task`, or `spawn_worker`, using generic agent profiles like
    'generalist' or 'coding_agent').

-   If **YES**, you MUST use **Mode A (Delegation)**.

-   If **NO**, use **Mode B (Sequential Self-Execution)**. You must read the
    prompt files intended for the subagents, follow their instructions, and
    write the expected output files to disk.

-   **Sub-agents orchestration:**

    -   If you use "Mode A (Delegation)", wait for "SUCCESS" confirmation from
        sub-agents to know when they are done.

    -   **Idempotency & Timeout Safeguard**: If a sub-agent fails or times out,
        you MUST verify the presence and integrity of its target output file
        (e.g., `<temp_dir>/worker_<goal_name>.json`) before retrying. If the
        file exists and contains valid JSON, treat the execution as **SUCCESS**
        and proceed. Otherwise, retry up to three times.

-   **Fail-fast mandate:** The automated audit in Phase 1 is the source of
    truth. If `orchestrator.py` fails, you must stop immediately with an
    explanation of failure. Do not use manual auditing as a fallback.

## The two-phase protocol

### Phase 1: Fact gathering and triage

1.  **Initialize and triage**:
    -   Run `python3 <repo_root>/scripts/orchestrator.py init <app_dir>`.
    -   This will create the scratch environment, perform static analysis, map
        the codebase, identify audit goals, and produce prompts for subagents
        for each audit goal and prompts for designated critic and aggregator
        subagents.
    -   You must wait (up to 5 minutes) for the script to finish.
2.  **Capture environment**: Note values of the `temp_dir`, and
    `activated_goals` from the JSON output. You will need them in Phase 2.
3.  **Evaluate goals**: If `activated_goals` is empty, skip to step 3 of Phase 2
    (Aggregation). Otherwise, proceed to step 1 of Phase 2 (Detailed analysis).

### Phase 2: Goal-oriented audit

Determine your execution capabilities and proceed with either Mode A OR Mode B.

#### Mode A: Orchestrator WITH Delegation Capabilities (Parallel)

1.  **Detailed analysis**: For each goal in `activated_goals` (e.g.,
    `permissions_and_apis`, `data_safety_part_1`, `data_safety_part_2`),
    delegate to a sub-agent. **Concurrency Limit:** You must not spawn more than
    3 sub-agents simultaneously. Spawn the first batch of up to 3, wait for
    their completions, and then spawn the next batch. Repeat until all goals are
    complete. Pass the prompt: `"Read your instructions from
    <temp_dir>/prompt_worker_<goal_name>.md and execute. MANDATORY: You must
    use your file-writing capabilities to save your final JSON findings directly
    to the file system at <temp_dir>/worker_<goal_name>.json. You are strictly
    forbidden from outputting the JSON in your chat response. To minimize
    context usage, your final response must be exactly 'SUCCESS' and nothing
    else."` **Validate**: Confirm every
    `<temp_dir>/worker_<goal_name>.json` exists and contains valid JSON. If a
    sub-agent fails or times out, but the valid JSON output file is already
    present on disk, do NOT retry; proceed normally. Only retry the
    corresponding worker (up to three times) if the file is missing or invalid.
2.  **Aggregate Findings**: Execute the python aggregation command:
   `python3 <repo_root>/scripts/orchestrator.py aggregate <temp_dir>`. This
   produces `aggregated_findings.json` and returns a JSON object containing
   `critic_chunks` representing the number of chunks to verify (e.g.,
   `{"temp_dir": "...", "critic_chunks": 2}`).
3.  **Parallel Critic review**: For each chunk index `i` from 1 to
   `critic_chunks`, delegate to a sub-agent. **Concurrency Limit:** You must not
   spawn more than 3 critic sub-agents simultaneously. Batch them in groups of 3
   as above. Pass the prompt:
   `"Read your instructions from <temp_dir>/prompt_critic_<i>.md and execute. MANDATORY: You must use your file-writing capabilities to save your final JSON findings directly to the file system at <temp_dir>/critic_output_<i>.json. You are strictly forbidden from outputting the JSON in your chat response. To minimize context usage, your final response must be exactly 'SUCCESS' and nothing else."`
   **Validate**: Confirm each `<temp_dir>/critic_output_<i>.json` exists and
   contains valid JSON before proceeding. If it failed or timed out, but the
   valid JSON file is present, proceed normally. Otherwise, retry that specific
   critic chunk.
4.  **Proceed to Finalization** (Step 4 below)

#### Mode B: Orchestrator WITHOUT Delegation Capabilities (Sequential)

1.  **Detailed Analysis**: For each goal in `activated_goals`, sequentially:
    -   Read the contents of `<temp_dir>/prompt_worker_<goal_name>.md`.
    -   Execute the instructions contained within that file yourself.
    -   **CRITICAL**: You MUST format your findings exactly as requested in the
        prompt and save them to `<temp_dir>/worker_<goal_name>.json`. **Do not**
        summarize findings in your thoughts or chat; move to the next task.
    -   **Validate**: Confirm `<temp_dir>/worker_<goal_name>.json` exists before
        moving to the next goal.
2.  **Aggregate Findings**: Execute the python aggregation command:
   `python3 <repo_root>/scripts/orchestrator.py --aggregate <temp_dir>`.
   This produces `aggregated_findings.json` and returns a JSON object containing
   `critic_chunks` representing the number of chunks to verify.
3.  **Sequential Critic review**: For each chunk index `i` from 1 to
   `critic_chunks`, sequentially:
    -   Read the contents of `<temp_dir>/prompt_critic_<i>.md`.
    -   Execute the steps yourself and save your findings to
      `<temp_dir>/critic_output_<i>.json`.
    -   **Validate**: Confirm `<temp_dir>/critic_output_<i>.json` exists before
      moving to the next chunk.
4.  **Proceed to Finalization** (Step 4 below)

#### Finalization (Both Modes)

4.  **Present findings**: Run `python3 <repo_root>/scripts/generate_report.py <temp_dir>`. 
    It will produce `<temp_dir>/compliance_report.md`. Present this output file to user.
5.  **STOP**: The audit is complete. Await further instructions.

---

<!-- BEGIN LOCAL WRAPPER -->
<!-- Not from upstream. Source: local-wrapper.md. Re-applied on every sync;
     edit that file, never this block. -->

## When NOT to Use This Skill

Do NOT use this skill when:

- **The target is not an Android app source tree** — iOS, or a store listing you
  cannot build from source. Use
  [`mobile-store-policy-readiness`](../mobile-store-policy-readiness/).
- **Python 3 or a writable workspace scratch directory is unavailable.** Phase 1 has
  an explicit fail-fast mandate: if `orchestrator.py` fails you must stop, and manual
  auditing is forbidden as a fallback. In a constrained environment, use
  [`mobile-store-policy-readiness`](../mobile-store-policy-readiness/), which is
  script-free.
- **The app has already been rejected.** Working backward from a citation is a
  different task — use the rejection playbook in
  [`mobile-store-policy-readiness`](../mobile-store-policy-readiness/).
- **You need App Store / cross-platform coverage.** This skill is Play-only.
- **You want a legal opinion or an approval guarantee.** The generated report's own
  disclaimer is correct: Play review has final authority. Route legal questions to
  `domain-legal/`.

## Policy currency caveat

The bundled `resources/policies.json` and the policy prose in the goal files are a
**snapshot** pinned to this skill's `last-updated` date. Play policy changes
frequently. The audit's *analysis* remains sound, but before acting on any specific
requirement, open the policy URL that `policies.json` carries for that entry and
confirm the current wording. Do not treat a bundled excerpt as verification.

## Verification

The two-phase protocol validates its own *pipeline* (worker JSON exists and parses,
critic chunks complete). That is not the same as validating the *report*. Before
acting on `compliance_report.md`, check:

- [ ] Every `🔴 Critical` and `🟡 Important` finding cites a real file and line, and
      that line actually contains what the finding claims — per the Concrete
      Attributions mandate in `resources/common_mandates.md`
- [ ] No finding rests on code inside `build/`, `test/`, `androidTest/`, or a sample
      module
- [ ] No finding treats local-only processing (on-device cache, prefs, local DB) as
      collection or sharing
- [ ] Findings the critic marked `MANUAL_REVIEW` are presented as open questions, not
      as violations
- [ ] Findings the critic `PRUNED` do not reappear in the final report
- [ ] Empty result sets render as `[]`, not as placeholder or `N/A` entries
- [ ] Data Safety discrepancies are framed against declarations the user actually
      supplied — the skill cannot read the Play Console
- [ ] The disclaimer is intact

Then verify the policy itself is current — see the caveat above. A correct finding
against a superseded policy is still wasted work.

If the run produced an unusually long Critical list, re-check the first three boxes
before escalating anything: over-flagging is the failure mode these mandates exist to
prevent.

## Related Skills

- [`mobile-store-policy-readiness`](../mobile-store-policy-readiness/) — **the
  complement, run after this.** Covers what this skill does not: the Apple App Store,
  non-code submission surfaces (store listing, screenshots, age rating, privacy
  policy URL reachability, review notes), live policy verification, and rejection
  triage. It is script-free, so it also serves as the fallback when this skill's
  prerequisites are unavailable.
- [`android-play-billing-upgrade`](../android-play-billing-upgrade/) — monetization
  findings usually land here.
- [`android-release-pipeline`](../android-release-pipeline/) — gate the release train
  on a clean audit.
- [`android-quarterly-maintenance`](../android-quarterly-maintenance/) — recurring
  cadence; policy drift is a standing risk, not a one-time check.

> **Note on quality.** This skill's false-positive discipline lives in
> `resources/common_mandates.md` and `resources/critic.md` rather than in this body —
> presumption of compliance, mandatory `file:line` citation before any
> Critical/Important finding, forced downgrade where compliance cannot be verified,
> and a `VERIFIED`/`MANUAL_REVIEW`/`PRUNED` critic pass. Read those before assuming
> anything is missing, and preserve them if you ever adapt this skill.
