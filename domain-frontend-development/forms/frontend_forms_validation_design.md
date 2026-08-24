---
title: "Form Validation Strategy Design & Audit"
category: frontend-development/forms
description: "Design and audit a layered form validation strategy spanning schema validation (Zod/Yup), client-side and server-side enforcement, async validation, and error-state UX across React Hook Form, Formik, or native forms."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - forms
  - validation
  - zod
  - react-hook-form
  - formik
  - async-validation
  - error-ux
updated: "2026-06-21"
related_prompts:
  - domain-frontend-development/forms/frontend_forms_accessibility_ux.md
  - domain-frontend-development/react/frontend_react_state_management.md
  - domain-frontend-development/typescript/frontend_typescript_component_typing.md
  - domain-frontend-development/accessibility/frontend_accessibility_aria_patterns.md
---

# Form Validation Strategy Design & Audit

**Objective:** Design or audit a form's validation strategy so that every rule is enforced at the correct layer (schema, client, server), async checks are debounced and race-safe, and validation errors surface with clear, well-timed UX.

**When to Use:**
- Use when: Designing validation for a new form (sign-up, checkout, settings, multi-step wizard).
- Use when: Auditing an existing form where invalid data reaches the server or users hit confusing errors.
- Use when: Choosing or migrating a form library (React Hook Form, Formik, native) and a schema layer (Zod, Yup, Valibot).
- Use when: Adding async validation (uniqueness checks, coupon codes, address lookups).
- Don't use when: The form is a single trivial input with no rules — inline `required` is sufficient and a full strategy is over-engineering.

## Instructions

1. **Inventory Fields and Rules**
   - List every field with its data type, required/optional status, and constraints.
   - Classify each rule by where it can be authoritatively enforced:
     - **Format/shape** (email pattern, min length, number range) — schema layer.
     - **Cross-field** (password confirmation, end-date after start-date) — schema refinement.
     - **Stateful/async** (username uniqueness, coupon validity, stock check) — server, mirrored client-side for UX.
   - Note which rules are security-relevant (must never be client-only).

2. **Define the Schema Layer**
   - Specify a single source-of-truth schema (e.g., Zod/Yup) that both the form and, where possible, the server can share.
   - Capture: per-field type coercion, refinements for cross-field logic, and a typed output (infer the TS type from the schema rather than hand-writing it).
   - Confirm error messages live in the schema, keyed by path, so the UI can render them by field.

3. **Map Client vs Server Enforcement**
   - For each rule, state where it runs and why. Every security/integrity rule MUST run server-side; client validation is UX, not a trust boundary.
   - Identify rules duplicated across layers and confirm they cannot drift (shared schema preferred).
   - Document how server validation errors are mapped back onto form fields (path-based error mapping).

4. **Design Async Validation**
   - For each async check, specify: trigger (on blur vs debounced on change), debounce interval, abort/cancellation of stale requests, loading indicator, and failure/timeout behavior.
   - Ensure the latest request wins (cancel or ignore out-of-order responses) to prevent race conditions.
   - Confirm submit is blocked or re-validated while async checks are pending.

5. **Design Error-State UX and Timing**
   - Decide validation timing per field: validate-on-submit, on-blur, or on-change-after-first-error (the common "touched + dirty" pattern).
   - Specify error display: inline per-field, a summary region, or both; success affordances for completed fields.
   - Define submit behavior: disabled-until-valid vs always-enabled-with-validation-on-submit, and focus management to the first invalid field.

6. **Select / Confirm the Library Integration**
   - Map the strategy onto the chosen library (React Hook Form + resolver, Formik + schema, or native + Constraint Validation API), noting controlled vs uncontrolled tradeoffs and re-render cost.
   - Verify the schema resolver is wired correctly and field registration matches schema paths.

7. **CRITICAL: Verify findings before reporting**
   - Trace at least one rule end-to-end (input → schema → client error → server enforcement) to confirm it actually fires.
   - Do not assert a library behaves a specific way from memory; phrase version-specific behavior neutrally and note "verify against current docs."
   - **Confidence level** for each finding/recommendation:
     - **High Confidence:** Verified by reading the relevant schema/handler code or reproducing the behavior.
     - **Medium Confidence:** Strongly implied by the code structure but not directly traced.
     - **Low Confidence:** Inferred from patterns; flagged for the team to confirm.

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Treat client-side validation as a security boundary — never rely on it to keep bad data out of the database.
- Duplicate validation logic by hand in two layers where it can silently drift; flag drift risk.
- Fire async validation on every keystroke without debounce/cancellation (causes request storms and race conditions).
- Validate-on-change from the very first keystroke before a field is touched (punishes users mid-typing).
- Assume a schema library coerces or trims values the way you expect — verify coercion explicitly.
- Recommend a heavy library migration when the existing setup meets the form's actual complexity.
- Hand-write TypeScript types that can diverge from the runtime schema.

✅ **DO:**
- Keep one schema as the source of truth and infer types from it.
- Enforce every integrity/security rule server-side regardless of client validation.
- Debounce async checks, cancel stale requests, and block submit while pending.
- Use a "validate after first blur/submit, then on change" timing to reduce noise.
- Map server errors back onto specific fields by path.
- Match library choice to the form's re-render and control needs.
- Trace at least one rule end-to-end before declaring the strategy sound.

## Expected Output

A validation strategy document (or audit report) that includes:
- A field/rule inventory mapped to enforcement layers.
- The schema-layer design with shared client/server intent.
- Async validation design with debounce/cancellation/loading behavior.
- Error-state UX and timing decisions.
- Prioritized findings (for audits) or a build plan (for new forms).

### Output Format

```markdown
## Form Validation Strategy: [Form Name]

### Field & Rule Inventory

| Field | Type | Required | Rules | Enforcement Layer | Security-Relevant |
|-------|------|----------|-------|-------------------|-------------------|
| ... | ... | ... | ... | schema / client / server | yes/no |

### Schema Layer
[Schema definition intent + shared client/server note]

### Client vs Server Map
[Per-rule enforcement table or notes]

### Async Validation Design
[Per-check: trigger, debounce, cancellation, loading, failure]

### Error-State UX & Timing
[Timing model, display strategy, submit & focus behavior]

### Findings / Build Plan
| ID | Issue/Task | Severity | Confidence | Location | Evidence | Recommendation |
|----|-----------|----------|------------|----------|----------|----------------|

### Prioritized Recommendations
1. ...
```

## Example Output

```markdown
## Form Validation Strategy: Account Sign-Up (React Hook Form + Zod)

### Field & Rule Inventory

| Field | Type | Required | Rules | Enforcement Layer | Security-Relevant |
|-------|------|----------|-------|-------------------|-------------------|
| email | string | yes | valid email format; unique | schema (format) + server (unique) | yes (unique) |
| username | string | yes | 3–20 chars, alphanumeric; unique | schema + server (unique) | yes (unique) |
| password | string | yes | min 12 chars, 1 number, 1 symbol | schema + server | yes |
| confirmPassword | string | yes | equals password | schema refinement | no |
| referralCode | string | no | valid active code | server (async) | yes (validity) |
| acceptTerms | boolean | yes | must be true | schema + server | yes |

### Schema Layer

Single Zod schema is the source of truth; the form's resolver and the API route both import it. The TS type is inferred (`z.infer<typeof SignUpSchema>`), so form values and server payload share one type.

```ts
const SignUpSchema = z.object({
  email: z.string().email("Enter a valid email."),
  username: z.string().min(3).max(20).regex(/^[a-z0-9_]+$/i, "Letters, numbers, underscore only."),
  password: z.string().min(12, "At least 12 characters.")
    .regex(/[0-9]/, "Include a number.").regex(/[^A-Za-z0-9]/, "Include a symbol."),
  confirmPassword: z.string(),
  referralCode: z.string().optional(),
  acceptTerms: z.literal(true, { errorMap: () => ({ message: "You must accept the terms." }) }),
}).refine((d) => d.password === d.confirmPassword, {
  path: ["confirmPassword"],
  message: "Passwords do not match.",
});

type SignUpValues = z.infer<typeof SignUpSchema>;
```

### Client vs Server Map

| Rule | Client | Server | Notes |
|------|--------|--------|-------|
| Email format | ✓ (UX) | ✓ (trust) | Shared schema, no drift |
| Username/email uniqueness | async (UX) | ✓ (authoritative) | Client check is advisory only |
| Password complexity | ✓ | ✓ | Server re-validates with same schema |
| acceptTerms === true | ✓ | ✓ | Never trust client checkbox alone |
| referralCode validity | async (UX) | ✓ | Server is source of truth |

### Async Validation Design

| Check | Trigger | Debounce | Cancellation | Loading | Failure |
|-------|---------|----------|--------------|---------|---------|
| Username unique | on blur + debounced change | 400ms | AbortController; ignore stale | spinner in field | timeout → "Couldn't verify, try again"; allow submit, server re-checks |
| Referral code | on blur | 400ms | AbortController | inline "Checking…" | invalid → field error; network error → non-blocking warning |

Submit is disabled while any async check is `pending`. The latest request always wins via `AbortController`.

### Error-State UX & Timing

- **Timing:** Fields validate on first blur, then on change once touched (`mode: "onTouched"`). The form re-validates all fields on submit.
- **Display:** Inline error under each field (`aria-describedby` wired), plus a submit-time summary listing each error linked to its field.
- **Submit:** Button is enabled; clicking an invalid form runs validation, focuses the first invalid field, and announces the summary.

### Findings (Audit of Prior Implementation)

| ID | Issue | Severity | Confidence | Location | Evidence | Recommendation |
|----|-------|----------|------------|----------|----------|----------------|
| F1 | Uniqueness enforced only client-side | High | High | `api/signup.ts` (no unique check) | Server inserts without checking; client `fetch` is the only gate | Add server-side unique constraint + 409 response mapped to field |
| F2 | Async username check fires every keystroke | High | High | `useUsernameCheck.ts` | No debounce/abort; 1 request per character | Add 400ms debounce + AbortController |
| F3 | Hand-written `SignUpValues` type diverges from schema | Medium | High | `types.ts` vs `schema.ts` | `referralCode` required in type, optional in schema | Replace with `z.infer` |
| F4 | Errors validate on every change pre-touch | Medium | Medium | RHF `mode: "onChange"` | Users see errors while typing first field | Switch to `onTouched` |
| F5 | Submit not blocked during pending async | Medium | High | submit handler | User can submit before username check resolves | Disable submit while `isValidating` |

### Prioritized Recommendations
1. **F1 — Move uniqueness to server (security).** Highest risk: duplicate/colliding accounts.
2. **F2 — Debounce + abort async checks.** Stops request storms and race conditions.
3. **F5 — Block submit while async pending.** Prevents invalid submissions slipping through.
4. **F3 — Infer types from schema.** Eliminates a whole class of drift bugs.
5. **F4 — Adjust validation timing to `onTouched`.** Reduces user-facing noise.
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Defines a single goal — a correctly layered, race-safe validation strategy.
- **ST-02 (Structured Sequential Instructions):** Walks inventory → schema → layer map → async → UX → library in order.
- **RT-02 (Multi-Dimensional Analysis Framework):** Evaluates each rule across enforcement layer, security, async behavior, and UX timing.
- **RT-05 (Evidence-Based Reasoning):** Every finding cites location and evidence and traces a rule end-to-end.
- **DS-06 (Prioritization Guidance):** Orders findings by severity (security first, then correctness, then UX).

## Related Prompts

- [frontend_forms_accessibility_ux.md](frontend_forms_accessibility_ux.md) - Accessible error announcement and field semantics for the same forms
- [../react/frontend_react_state_management.md](../react/frontend_react_state_management.md) - Where form state belongs relative to app state
- [../typescript/frontend_typescript_component_typing.md](../typescript/frontend_typescript_component_typing.md) - Typing form values and schema-inferred types
- [../accessibility/frontend_accessibility_aria_patterns.md](../accessibility/frontend_accessibility_aria_patterns.md) - ARIA for invalid/required states
