---
title: "Next.js Server Actions & Mutations Analysis"
category: frontend-development/nextjs
description: "Audit Next.js Server Actions and mutation flows — 'use server' usage, form actions, revalidatePath/revalidateTag, optimistic updates, and the security/validation of actions treated as public endpoints."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: advanced
tags:
  - nextjs
  - server-actions
  - mutations
  - revalidation
  - optimistic-updates
  - input-validation
updated: "2026-06-21"
related_prompts:
  - domain-frontend-development/nextjs/frontend_nextjs_app_router.md
  - domain-frontend-development/nextjs/frontend_nextjs_data_fetching.md
  - domain-frontend-development/react/frontend_react_server_components_streaming.md
  - domain-frontend-development/performance/frontend_performance_core_web_vitals.md
---

# Next.js Server Actions & Mutations Analysis

**Objective:** Audit a Next.js application's Server Actions and mutation flows — `'use server'` usage, form actions, cache revalidation (`revalidatePath`/`revalidateTag`), optimistic updates, and the security and validation of actions treated as public network endpoints — and recommend specific, evidence-backed fixes.

**When to Use:**
- Use when: Mutations are implemented with Server Actions (`'use server'`) invoked from forms or client components and you want to verify correctness and safety.
- Use when: Data appears stale after a mutation because `revalidatePath`/`revalidateTag` is missing or targets the wrong path/tag.
- Use when: Optimistic UI (`useOptimistic`) is in use and you suspect reconciliation/rollback issues.
- Use when: You need a security review of actions — each is a callable endpoint and must validate input and authorize the caller.
- Don't use when: The app performs mutations exclusively through traditional API route handlers with no Server Actions — this prompt is Server-Action-specific.

## Instructions

1. **Inventory Server Actions**
   - List every `'use server'` function (file-level directive modules and inline `'use server'` functions) and where each is invoked (form `action`, `formAction`, called from a Client Component, bound with `.bind`).
   - Note which actions mutate data, which return values to the client, and which redirect.

2. **Audit `'use server'` Placement & Exposure**
   - Confirm `'use server'` marks server functions intended to be called from the client — each becomes a publicly reachable endpoint.
   - Flag actions exported from modules that could be imported broadly, expanding the attack surface.
   - Confirm sensitive logic that should never be client-callable is *not* exported as a Server Action.

3. **Validate Inputs (treat every action as untrusted)**
   - Confirm each action validates and parses its inputs (e.g. schema validation) rather than trusting `FormData`/arguments.
   - Flag direct use of raw form fields in queries, file paths, or commands without validation/escaping (injection risk).
   - Confirm type coercion is explicit — `FormData` values are strings; numbers/booleans must be parsed.

4. **Verify Authentication & Authorization**
   - Confirm each mutating action checks the session/identity of the caller inside the action body (not only in UI that renders the form).
   - Confirm object-level authorization: the caller is allowed to mutate the specific resource (prevent IDOR).
   - Flag actions that rely on hidden form fields for identity/role (client-controllable, therefore untrusted).

5. **Analyze Cache Revalidation**
   - For each mutation, confirm the affected data is revalidated: `revalidatePath('/route')` for path-based caches, `revalidateTag('tag')` for tagged fetches.
   - Flag mutations with no revalidation (stale reads) and over-broad revalidation (revalidating large trees unnecessarily).
   - Confirm tags used in `revalidateTag` actually match the `fetch(..., { next: { tags } })` (verify caching/tagging semantics against current docs).
   - Confirm `redirect()` usage after mutation is placed correctly relative to revalidation.

6. **Review Optimistic Updates**
   - For `useOptimistic` flows, confirm the optimistic state is derived from real state and reconciles when the action resolves.
   - Confirm rollback behavior on action failure (the UI must not keep an optimistic value that the server rejected).
   - Flag optimistic updates applied to data the server may transform (server-assigned ids, normalized values) where naive optimism diverges from truth.

7. **Audit Error Handling**
   - Confirm actions return structured results (or use a `useActionState`/form-state pattern) so the client can render validation and server errors.
   - Flag actions that throw raw errors leaking internal detail to the client, or that swallow errors silently leaving the UI in a success state.
   - Confirm pending/disabled states (`useFormStatus`/action state) prevent duplicate submissions.

8. **CRITICAL: Verify findings before reporting**
   - For each finding, confirm the action body, its invocation, and revalidation targets in code before recommending a change. Assign a Confidence level:
     - **High:** The issue is directly visible and exploitable/incorrect (e.g. a mutating action with no auth check, raw form field in a query, missing revalidation after write).
     - **Medium:** The pattern is likely problematic but depends on session middleware, ORM behavior, or version-specific caching you cannot fully see.
     - **Low:** A heuristic concern (e.g. "this revalidation may be broader than needed") requiring author confirmation.
   - Do not state version-specific caching/revalidation behavior as settled fact — note "verify against current docs." Do not invent exploit impact you have not traced.

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Don't assume UI-level gating (rendering a form only for admins) substitutes for an authorization check inside the action — it does not.
- Don't claim an action is unvalidated without checking for a schema/parse step that may be a few lines down.
- Don't flag "missing revalidation" when the route is dynamic/uncached and always re-fetches.
- Don't recommend `revalidatePath('/')` (or similarly broad) as a default fix — it over-invalidates.
- Don't assert a tag mismatch without confirming the `fetch` tagging on the read side.
- Don't invent CVE-style severity or exploit numbers; describe the concrete risk mechanism.
- Don't state Server Action / caching API semantics as fixed fact — phrase as "verify against current docs."

✅ **DO:**
- Treat every Server Action as a public POST endpoint: validate input, authenticate, authorize the specific resource.
- Cite the exact action, line, and invocation as evidence for each finding.
- Match `revalidateTag` calls to the `fetch` tags they target.
- Confirm optimistic updates reconcile and roll back on failure.
- Recommend structured error returns and pending-state guards against double submission.
- Scope revalidation to the smallest correct path/tag.
- Prioritize security findings (auth, validation, IDOR) above cache/UX findings.

## Expected Output

A structured Server Actions audit with an action inventory, per-finding detail (severity, confidence, location, evidence, recommendation), and a prioritized remediation list led by security.

- Server Action inventory
- Per-finding analysis across security, revalidation, optimistic UX, and error handling
- Prioritized recommendations with security first

### Output Format

```markdown
## Next.js Server Actions Audit

### Summary
- Actions reviewed: <n>
- Security posture: <strong | gaps | unsafe>
- Revalidation correctness: <correct | partial | missing>
- Total findings: <n> (Critical: <n>, High: <n>, Medium: <n>, Low: <n>)

### Server Action Inventory
| Action | Invoked from | Mutates | Auth check | Validation | Revalidation |
|--------|--------------|---------|------------|------------|--------------|
| ... | form/client | yes/no | yes/no | yes/no | path/tag/none |

### Findings
#### [SEVERITY] <Title>
- **Severity:** Critical | High | Medium | Low
- **Confidence:** High | Medium | Low
- **Location:** <file:line / action>
- **Evidence:** <exact code construct>
- **Risk/Impact:** <security / staleness / UX>
- **Recommendation:** <specific fix>

### Prioritized Recommendations
1. ...
```

## Example Output

```markdown
## Next.js Server Actions Audit

### Summary
- Actions reviewed: 3
- Security posture: gaps (one mutating action lacks authorization)
- Revalidation correctness: partial (one mutation does not revalidate)
- Total findings: 4 (Critical: 1, High: 1, Medium: 1, Low: 1)

### Server Action Inventory
| Action          | Invoked from | Mutates | Auth check | Validation | Revalidation |
|-----------------|--------------|---------|------------|------------|--------------|
| updateProfile   | form         | yes     | no         | no         | none         |
| deletePost      | client btn   | yes     | session yes/object no | yes | revalidatePath |
| addComment      | form         | yes     | yes        | yes        | revalidateTag (mismatch) |

### Findings

#### [CRITICAL] Mutating action with no authorization or input validation
- **Severity:** Critical
- **Confidence:** High
- **Location:** app/actions/profile.ts:3
- **Evidence:**
  ```ts
  'use server'
  export async function updateProfile(formData: FormData) {
    await db.user.update({
      where: { id: formData.get('userId') as string },   // client-controlled id
      data: { name: formData.get('name') as string },     // unvalidated
    })
  }
  ```
- **Risk/Impact:** A caller can submit any `userId` and overwrite another user's profile (IDOR), and `name` is stored unvalidated. The action is a public endpoint regardless of UI gating.
- **Recommendation:** Resolve the user id from the authenticated session (never from the form); validate `name` with a schema (length/charset); reject unauthenticated callers:
  ```ts
  const session = await auth()
  if (!session) throw new Error('Unauthorized')
  const { name } = ProfileSchema.parse({ name: formData.get('name') })
  await db.user.update({ where: { id: session.userId }, data: { name } })
  ```

#### [HIGH] Delete action checks session but not object ownership
- **Severity:** High
- **Confidence:** High
- **Location:** app/actions/posts.ts:10
- **Evidence:** `if (!session) throw...` then `db.post.delete({ where: { id } })` with `id` from the client.
- **Risk/Impact:** Any logged-in user can delete any post (broken object-level authorization).
- **Recommendation:** Verify ownership: `db.post.delete({ where: { id, authorId: session.userId } })` (or load-and-check), so callers can only delete their own resources.

#### [MEDIUM] revalidateTag does not match the fetch tag
- **Severity:** Medium
- **Confidence:** Medium
- **Location:** app/actions/comments.ts:20
- **Evidence:** Action calls `revalidateTag('comment')` but the read uses `fetch(url, { next: { tags: ['comments'] } })`.
- **Risk/Impact:** The comment list stays stale after adding a comment because the tag names differ.
- **Recommendation:** Align the strings (`'comments'`). Verify tagging semantics against current docs.

#### [LOW] Optimistic comment keeps client value if the action fails
- **Severity:** Low
- **Confidence:** Low
- **Location:** components/CommentBox.tsx:15
- **Evidence:** `useOptimistic` adds the comment but there is no error branch to roll back when the action rejects.
- **Risk/Impact:** On failure the UI shows a comment that was never saved.
- **Recommendation:** Handle the rejected action (via `useActionState` error result) and let the optimistic state reconcile from server state; surface the failure to the user.

### Prioritized Recommendations
1. Fix the profile action: session-derived id, input validation, auth gate (Critical IDOR + injection surface).
2. Add object-level ownership check to the delete action (High IDOR).
3. Correct the revalidateTag/fetch-tag mismatch so the UI reflects new comments.
4. Add rollback/error handling to the optimistic comment flow.
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** States one objective scoping the audit to `'use server'` usage, revalidation, optimistic UX, and action security.
- **ST-02 (Structured Sequential Instructions):** Proceeds from action inventory → exposure → input validation → authorization → revalidation → optimistic UX → error handling.
- **RT-02 (Multi-Dimensional Analysis Framework):** Evaluates security, cache correctness, optimistic-update reconciliation, and error handling as distinct dimensions.
- **RT-05 (Evidence-Based Reasoning):** Requires citing the exact action body, invocation, and tag/path before reporting, with explicit confidence levels.
- **DS-06 (Prioritization Guidance):** Orders remediation with security findings (auth, validation, IDOR) ahead of cache and UX issues.

## Related Prompts
- [frontend_nextjs_app_router.md](frontend_nextjs_app_router.md) - Place Server Actions correctly within App Router routing and layouts.
- [frontend_nextjs_data_fetching.md](frontend_nextjs_data_fetching.md) - Pair mutation revalidation with the read-side fetching/caching strategy.
- [../react/frontend_react_server_components_streaming.md](../react/frontend_react_server_components_streaming.md) - Understand the server/client boundary that Server Actions cross.
- [../performance/frontend_performance_core_web_vitals.md](../performance/frontend_performance_core_web_vitals.md) - Relate optimistic UX and revalidation to perceived responsiveness.
