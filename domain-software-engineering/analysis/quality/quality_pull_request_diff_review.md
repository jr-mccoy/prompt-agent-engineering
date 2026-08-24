---
title: "Review Pull Request Diff as a Senior Engineer"
category: code-analysis/quality
description: "Review a single PR/diff the way a thoughtful senior engineer would — correctness, design fit, test adequacy, readability, and risk — separating blocking issues from nits, anchoring every finding to specific hunks, and delivering an explicit verdict (including 'LGTM, no blocking issues' when the diff is clean)."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - QA-20
difficulty: intermediate
tags:
  - code-review
  - pull-request
  - diff-review
  - correctness
  - triage
  - quality
updated: "2026-07-08"
related_prompts:
  - domain-software-engineering/analysis/quality/quality_code_complexity_analysis.md
  - domain-software-engineering/analysis/quality/quality_error_analysis.md
  - domain-software-engineering/testing/testing_unit_test_generation.md
---

# Review Pull Request Diff as a Senior Engineer

**Objective:** Review the supplied diff as a thoughtful senior engineer would — evaluating correctness, design fit, test adequacy, readability, and operational risk — and produce a triaged review that separates blocking issues from nits, states a confidence level for every finding, and ends with an explicit merge verdict.

## When to Use

- Use when: you have a specific PR or diff and want a rigorous second review before merging.
- Use when: you're the author and want to catch blockers before requesting human review.
- Use when: you're a new reviewer on an unfamiliar service and want a structured pass to compare against your own read.
- Don't use when: you want a whole-codebase quality assessment (use `quality_code_complexity_analysis.md`) or you haven't isolated a diff — this prompt reviews *one change set*, not a repository.

**Audience:** Software engineers reviewing or authoring PRs; tech leads doing pre-merge risk checks.

## Inputs / Context

1. **The diff (required).** Paste the unified diff wrapped in `<diff>…</diff>`. Include test files if they are part of the change. The instructions refer to this as *the diff*.
2. **PR intent (required).** 1–3 sentences: what the change is supposed to do (the PR title/description is usually enough). Wrap in `<intent>…</intent>`.
3. **Context (optional).** Language/framework, conventions, linter/formatter in use, deployment model, and any surrounding code the diff depends on, wrapped in `<context>…</context>`. If absent, the reviewer must treat claims about unseen code as *inferences*, not facts, and cap them at Question status.

## Constraints

### Must
- Anchor **every** finding to a specific file and hunk from the diff, quoting the relevant added/changed lines.
- Distinguish what is *visible in the diff* from what is *inferred about unseen code*. Inferred problems are raised as Questions, never as Blocking findings.
- Assign every finding a severity tier (Blocking / Should-fix / Question / Nit) **and** a confidence level (High / Medium / Low).
- End with exactly one verdict: `REQUEST CHANGES`, `APPROVE WITH COMMENTS`, or `LGTM — no blocking issues`. A clean diff **should** receive LGTM; do not manufacture findings to appear thorough.
- Review the change that was made, on its own terms. "I would have designed it differently" is not a finding unless the chosen design is demonstrably wrong for the stated intent.

### Must Not
- Flag style/formatting a linter or formatter already handles (import order, quote style, whitespace, line length, trailing commas) — unless the style issue conceals a behavioral bug.
- Invent behavior of functions, classes, or configs not present in the diff or supplied context.
- Rewrite the author's approach wholesale when it is sound. Suggest the *minimal* fix for each finding.
- Bury a correctness bug in a list of nits, or inflate a nit to Blocking to seem rigorous.
- Withhold a verdict or hedge it ("probably fine, but…"). Pick one.

## Instructions

1. **Understand the change before judging it.**
   - Read `<intent>`, then read the whole diff once without commenting.
   - Summarize in 2–3 sentences what the diff actually does and its blast radius (which files, layers, and callers are touched).
   - If the diff's behavior contradicts the stated intent, that mismatch is itself a candidate finding.

2. **Review across five dimensions.** For each hunk, check:
   - **Correctness:** logic errors, off-by-ones, unhandled error paths, boundary/empty/duplicate cases, concurrency and ordering assumptions, data-loss or security regressions.
   - **Design fit:** does the change sit in the right layer, follow visible conventions in the diff/context, and avoid leaking abstractions it didn't need to touch?
   - **Test adequacy:** are the behaviors this diff *adds or changes* exercised by tests in the diff? Which specific cases are missing (empty input, last page, error path)?
   - **Readability:** naming, control flow, and comments *where they affect a maintainer's ability to understand the change* — not cosmetics.
   - **Risk:** rollout/rollback safety, backwards compatibility, performance under realistic load, migrations, config/index dependencies.

3. **Draft candidate findings** with location, quoted evidence, impact, and a suggested minimal fix (RT-02 dimensions: location / description / impact / severity / recommendation).

4. **CRITICAL: Verify each candidate before reporting.**
   - Re-read the *entire post-image* of the function/hunk, not just the changed lines — is the issue already handled by a guard, caller contract, or another hunk in the same diff?
   - Search the whole diff for tests before claiming something is untested; test files may live under a different path.
   - Confirm the evidence is in the diff. If the problem only exists *if* unseen code behaves a certain way, downgrade the finding to a **Question** naming exactly what to check.
   - State what would change your assessment (e.g., "if `orders.created_at` has a unique index, B1 drops away").
   - Drop any candidate that survives only as "this pattern is sometimes bad."

5. **Triage by severity (DS-06).**
   - **Blocking:** would cause incorrect behavior, data loss, a security hole, or an outage if merged. Correctness always outranks style, design taste, and test gaps.
   - **Should-fix:** real but non-catastrophic — fix before or immediately after merge (missing edge-case tests, misleading names on new public APIs, avoidable perf traps).
   - **Question:** needs the author's answer; evidence not fully in the diff.
   - **Nit:** optional polish; batch into one commit or skip. Nits can never justify `REQUEST CHANGES`.

6. **Assign confidence to every finding.**
   - **High:** defect demonstrable from the diff alone.
   - **Medium:** strongly indicated by the diff but depends on unseen code behaving as its names/types imply.
   - **Low:** plausible concern; usually belongs as a Question or Nit rather than Blocking.

7. **Deliver the verdict.** `REQUEST CHANGES` iff ≥1 Blocking finding; `APPROVE WITH COMMENTS` for Should-fixes/Questions only; `LGTM — no blocking issues` when clean — say so plainly and include any Praise. Note genuinely good decisions (correct algorithm choice, thorough tests) in one or two lines; it calibrates the author on what to keep doing.

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Flag a missing null/error check without reading the full post-image function — the guard is often three lines above the changed hunk.
- Claim "no tests" because no test file appears *adjacent* to the changed file; test hunks may be elsewhere in the diff.
- Report linter territory (formatting, import order, naming case conventions) as findings.
- Treat an unfamiliar idiom (walrus operator, `defaultdict`, optional chaining, ORM lazy-loading) as a bug because it looks unusual.
- Assert that an unseen callee mishandles input, throws, or blocks — you cannot see it.
- Flag removed code as "lost functionality" without checking whether the same diff relocates it.

✅ **DO:**
- Re-read every changed function in full (post-image) before reporting anything about it.
- Grep the entire diff for `test`/`spec` hunks before making any test-adequacy claim.
- Verify each suspected bug with a concrete failing input or sequence ("with `?limit=0` this returns…"); if you can't construct one, downgrade or drop it.
- Convert every unseen-code dependency into a Question that names the exact thing to verify.
- Check the diff for its own mitigations (validation added in another hunk, config default, migration) before reporting.

## Dual-Failure Prevention (QA-20)

❌ **HARMFUL failure:** Approving a diff that contains a real correctness or security defect (skipped rows, unbounded query, auth check removed) because the review skimmed changed lines instead of tracing behavior — or blocking a healthy PR on a false positive, burning the author's day on rework that wasn't needed.

❌ **UNHELPFUL failure:** A wall of fifteen nits with no verdict; every sentence hedged ("might possibly consider…"); restating what the diff does without judging it; refusing to say LGTM on a clean diff out of a need to look thorough. A review that can't be acted on in one pass is a failed review.

✅ **Quality bar:** Would a thoughtful senior engineer on this team sign their name to this review — confident it would catch a real shipped bug, *and* that a competent author could action it in under ten minutes without feeling nit-picked?

## Expected Output

A triaged review: summary and verdict first, then findings grouped by severity tier (each with location, quoted evidence, impact, minimal fix, confidence), then test-adequacy and risk notes. Empty tiers are stated as empty, not padded.

### Output Format

```
# PR Review: [title from intent]

**Summary:** [2–3 sentences: what the diff does; overall assessment]
**Verdict:** [REQUEST CHANGES | APPROVE WITH COMMENTS | LGTM — no blocking issues]

## Blocking (must fix before merge)
### B1. [Title] — Confidence: [High/Medium/Low]
- Location: [file, hunk/lines]
- Evidence: [quoted lines]
- Impact: [what goes wrong, with a concrete failing input]
- Fix: [minimal change]

## Should-fix (before or shortly after merge)
### S1. [Title] — Confidence: […]   [same fields]

## Questions (author input needed)
### Q1. [Question] — [what in the diff prompted it; what answer resolves it]

## Nits (optional; never blocking)
- N1. [file:line — one line each]

## Praise
- [what was done well — 1–2 lines]

## Test adequacy
[What the diff's tests cover vs. the behaviors it changes; missing cases]

## Risk notes
[Rollout/rollback, compat, perf, migration/index dependencies]
```

## Example Output

```
# PR Review: Add keyset pagination to GET /api/orders

**Summary:** Replaces OFFSET pagination with keyset pagination: `orders_repo.list_after()`
orders by `created_at` and filters `created_at > cursor`; the handler adds `limit`/`cursor`
query params and returns `next_cursor`. One happy-path test added. The keyset approach is
right for this table, but two correctness defects need fixing before merge.
**Verdict:** REQUEST CHANGES

## Blocking (must fix before merge)

### B1. Non-unique sort key skips/duplicates rows at page boundaries — Confidence: High
- Location: db/orders_repo.py, hunk @@ -41,6 +41,14 @@ (`list_after`)
- Evidence:
    +        query = (
    +            select(Order)
    +            .where(Order.created_at > cursor)
    +            .order_by(Order.created_at)
    +            .limit(limit)
    +        )
- Impact: `created_at` is not unique (bulk imports write identical timestamps). If page N
  ends mid-group of equal timestamps, `created_at > cursor` drops the rest of that group:
  rows silently missing from paginated output. Demonstrable from the diff alone — the
  comparison and ordering both use only the timestamp.
- Fix: order by `(created_at, id)` and compare the tuple:
  `where((Order.created_at, Order.id) > (cursor_ts, cursor_id))`, encoding both fields in
  the cursor. (Combines cleanly with S1.)

### B2. `limit` is unvalidated — unbounded fetch and 500 on bad input — Confidence: High
- Location: api/handlers/orders.py, hunk @@ -18,7 +18,16 @@
- Evidence:
    +    limit = int(request.args.get("limit", DEFAULT_PAGE_SIZE))
    +    cursor = request.args.get("cursor")
- Impact: `?limit=500000` scans and serializes the table in one request (memory/latency
  blast radius); `?limit=abc` raises ValueError → unhandled 500. Both reachable by any
  caller of a public endpoint.
- Fix: clamp `1 <= limit <= MAX_PAGE_SIZE` (e.g. 100) and return 400 on non-integer input.

## Should-fix (before or shortly after merge)

### S1. `next_cursor` emitted on exact-final page — Confidence: High
- Location: api/handlers/orders.py, same hunk as B2
- Evidence:
    +    if len(orders) == limit:
    +        next_cursor = orders[-1].created_at.isoformat()
- Impact: when the last page is exactly `limit` rows, clients get a `next_cursor` leading
  to an empty page — harmless but wasteful and it complicates client termination logic.
- Fix: fetch `limit + 1` rows; if you got the extra row, there's a next page — return
  `limit` rows plus the cursor, else no cursor.

### S2. Tests cover only the happy path — Confidence: High
- Location: tests/test_orders_api.py, hunk @@ +1,22 @@
- Evidence: single test `test_list_orders_returns_first_page` (seeds 3 rows, asserts 3
  returned). No test for: empty table, final-page cursor behavior, `limit` bounds,
  malformed cursor, or the equal-timestamp boundary from B1.
- Impact: the exact defects in B1/B2 are the cases the suite doesn't exercise; regressions
  will reappear invisibly.
- Fix: add boundary tests alongside the B1/B2 fixes — the equal-timestamp case is the one
  most worth locking in.

## Questions (author input needed)

### Q1. The old endpoint accepted a `status` filter; the new handler drops it. Intentional?
- The removed hunk deletes `status = request.args.get("status")` with no replacement in the
  diff. If external clients use it, this is a silent behavioral regression; if it was dead,
  say so in the PR description. Answer determines whether this becomes Blocking.

### Q2. Is there an index covering `(created_at, id)`?
- Schema isn't in the diff. Keyset pagination on an unindexed sort key degrades to a full
  scan per page on large tables. If the index exists, no action; if not, add it in this PR
  or a fast-follow migration.

## Nits (optional; never blocking)

- N1. db/orders_repo.py:52 — `res2` → `page_rows`; the surviving `res` was removed by this
  diff, so the suffix now reads as noise.
- N2. api/handlers/orders.py:24 — comment says "default 50" but `DEFAULT_PAGE_SIZE = 25`;
  drop the comment or fix the number.

## Praise

- Switching OFFSET → keyset is the right call for this table's growth; and the handler
  stays thin, with query construction kept in the repo layer where the file's existing
  conventions put it.

## Test adequacy

Added: 1 test (first-page happy path). Changed behaviors not covered: cursor continuation,
final page, empty result, limit validation, duplicate-timestamp boundary. Adequacy: LOW —
acceptable only once S2 lands with the B1/B2 fixes.

## Risk notes

- Rollback: safe — no schema change in this diff; old clients without `cursor` get page 1.
- Compat: response gains `next_cursor`; additive, but confirm no strict response-schema
  validation on consumers. Q1 (dropped `status` param) is the real compat risk.
- Perf: hinges on Q2 (index). Verify before enabling for the largest tenants.
```

## Customization Guide

- **Language/framework:** swap the correctness checklist emphasis — e.g. for Go add goroutine/`err` shadowing checks; for React add render/dependency-array and state-batching checks; for SQL-heavy diffs add injection and transaction-boundary checks.
- **Team conventions:** paste your linter/CI config summary into `<context>` and add its rules to the "linter territory" exclusion so the review never duplicates automation.
- **Stricter gate (release branches):** promote Should-fix to Blocking and require Q-items resolved before verdict.
- **Lightweight mode (docs/config-only diffs):** collapse to Correctness + Risk dimensions and allow a two-line LGTM.
- **Very large diffs:** review commit-by-commit or file-group-by-file-group, then merge findings into one triage list — severity tiers and the single verdict stay global.

## Techniques Used

- **ST-01 (Clear Objective Statement):** the single opening sentence fixes deliverable (triaged review + verdict), stance (senior engineer), and the five review dimensions, so the model judges the diff rather than summarizing it.
- **ST-02 (Structured Sequential Instructions):** seven numbered steps enforce the order that prevents bad reviews — understand → analyze → draft → *verify* → triage → confidence → verdict — so no finding is reported before verification.
- **RT-02 (Multi-Dimensional Analysis Framework):** every finding carries location, quoted evidence, impact, severity, and a minimal fix; the five review dimensions (correctness, design fit, tests, readability, risk) are RT-02 applied to a diff.
- **DS-06 (Prioritization and Severity Guidance):** the Blocking / Should-fix / Question / Nit tiers with an explicit conflict rule (correctness outranks everything; nits can never block) make the review actionable in one pass and drive the verdict mechanically.
- **QA-20 (Dual-Failure Quality Test):** guards both directions — approving a real defect or blocking on a false positive (harmful) and nit-walls, hedging, or refusing a deserved LGTM (unhelpful) — with the named quality bar: a senior engineer would sign it, and the author can action it in ten minutes.

## Related Prompts

- `domain-software-engineering/analysis/quality/quality_code_complexity_analysis.md` — whole-codebase quality assessment when the unit of review isn't a single diff.
- `domain-software-engineering/analysis/quality/quality_error_analysis.md` — deeper pass on error handling when a review surfaces resilience concerns.
- `domain-software-engineering/testing/testing_unit_test_generation.md` — generate the missing tests a review's test-adequacy section identifies.

## Verification

- [ ] Frontmatter complete; every technique ID exists in the index.
- [ ] When-to-Use includes a don't-use case.
- [ ] Instructions include an explicit verification step (step 4).
- [ ] False-Positive Prevention has real ❌/✅ pairs.
- [ ] Dual-Failure Prevention covers harmful AND unhelpful directions.
- [ ] Findings carry Confidence levels.
- [ ] Example Output is concrete and 80–120 lines.
- [ ] No invented data or fabricated authority.
