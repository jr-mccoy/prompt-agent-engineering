---
title: "Multi-Step Form State Architecture — Step Graph, Branch Invalidation, Draft Persistence, URL-Synced Navigation, and a Rechecked Final Submit"
category: frontend-development/forms
description: "Design or review the state architecture of a multi-step form or wizard: model steps as a graph whose branches are derived from answers, clear or park answers when an earlier branch changes, persist drafts with a versioned schema and a deliberate privacy choice, keep the URL, back button and refresh in step with the form, and make the final submit re-validate everything on the server once, idempotently."
techniques:
  - GT-01
  - GT-06
  - DP-07
  - RT-02
difficulty: intermediate
tags:
  - multi-step-form
  - form-wizard
  - form-state
  - draft-autosave
  - conditional-branching
  - step-navigation
  - long-form-loses-my-answers
  - back-button-breaks-form
  - save-and-continue-later
updated: "2026-10-03"
related_prompts:
  - domain-frontend-development/forms/frontend_forms_validation_design.md
  - domain-frontend-development/forms/frontend_forms_accessibility_ux.md
  - domain-frontend-development/architecture/frontend_state_management_selection.md
---

# Multi-Step Form State Architecture

**Objective:** Produce a state design for a multi-step form that never loses a user's
answers, never submits answers from a branch the user abandoned, survives refresh, back
button and deploys, and reaches the server through one rechecked, idempotent submit —
with the failure each design choice prevents written next to it.

**When to Use:**
- Building an application, onboarding, quote, checkout or claims flow longer than three
  steps.
- Users report losing answers on refresh, back button, or session timeout.
- Submitted records contain fields from a path the user did not take.
- Product wants "save and continue later" or cross-device resume.
- Drop-off by step is high and nobody can say where state, rather than content, is to
  blame.
- **Not this prompt if** you need per-field rules, schema choice, async checks or error
  timing — use `domain-frontend-development/forms/frontend_forms_validation_design.md`
  (this prompt consumes its per-step schemas). For step announcements, focus moves and
  progress semantics for assistive technology, use
  `domain-frontend-development/forms/frontend_forms_accessibility_ux.md`. For choosing an
  app-wide state library, use
  `domain-frontend-development/architecture/frontend_state_management_selection.md`.

## Inputs / Context

1. **Steps and fields**, with which answers decide later steps (branch conditions).
2. **Data sensitivity** per field (PII, financial, health) — decides where drafts may live.
3. **Resume requirement**: same tab only, same device, or cross-device.
4. **Back end**: one final submit endpoint, or per-step saves to a server-side draft.
5. **Framework and form library** in use, and the router.
6. **Funnel data** if available: entries, completions and exits per step.

## Method

1. **Model the flow as a step graph (RT-02).** List steps as nodes and branch conditions
   as edges. Derive the *visible step list* from current answers; never hard-code it.
   Keep one form state object for the whole flow with a per-step schema slice, so cross-
   step rules (end date after start date set two steps earlier) can be checked.
2. **Predict failure modes (DP-07)** for each design choice before picking it:
   - *Branch change*: user picks "Business", fills 3 business steps, goes back and picks
     "Individual". Without invalidation, hidden business fields are submitted.
   - *Refresh / tab crash*: in-memory state only → all answers lost.
   - *Deep link*: user opens `/apply/step-5` with steps 2–4 empty.
   - *Deploy mid-flow*: a stored draft no longer matches the new schema.
   - *Double submit*: slow network, user clicks twice → two applications.
3. **Define branch invalidation.** When a branch-deciding answer changes, compute which
   fields are now unreachable and either clear them or park them (kept locally, excluded
   from submission, restored if the user switches back). Submission payloads are built
   only from reachable steps.
4. **Choose draft persistence deliberately.** Options: memory only; `sessionStorage`
   (survives refresh, not tab close); `localStorage` (survives restarts; readable by any
   script on the origin and persists on shared computers — avoid for sensitive fields);
   server-side draft keyed to the account (cross-device; needs auth and retention
   policy). Autosave with a debounce (e.g. 800–1,500ms after typing stops) and on step
   change. Stamp every draft with a schema version; on mismatch, migrate known fields or
   discard with a message — never load silently.
5. **Sync navigation with the URL.** One URL per step (path or `?step=`), so back,
   forward and refresh behave. Guard deep links: redirect to the first incomplete
   reachable step. The browser back button moves one step back, not out of the flow.
   Warn before leaving only when unsaved changes exist.
6. **Gate the final submit (GT-01).** The submit is reachable only from a review step
   that shows the reachable answers. On submit, the server re-validates the whole payload
   against the full schema, including cross-step rules (GT-06: recheck immediately
   before commit, because answers and server-side state such as prices or eligibility may
   have changed since the step was filled). Send an idempotency key generated when the
   review step opens; the server returns the original result for a repeat key.
7. **Map server errors back to steps.** A server validation error for a field on step 2
   must route the user to step 2 with the error shown, not a generic banner on review.
8. **Instrument.** Per-step entry, completion and exit events, time on step, validation
   error counts per field, and draft restores — so state problems can be told apart from
   content problems. Rate each finding (for audits): High = reproduced, Medium = read in
   code, Low = inferred from analytics.

## Output Format

```
# Multi-step form state design — [flow]   Steps: [n]   Date: [..]

## Step graph
| Step | Fields | Shown when | Decides | Schema slice |
## Failure modes and the design choice that prevents each
| Failure | Prevention |
## Branch invalidation rules
| Changed answer | Fields made unreachable | Clear or park |
## Draft persistence
Storage: [..]  Sensitive fields excluded: [..]  Autosave: [..]  Schema version: [..]  Retention: [..]
## Navigation
URL scheme: [..]  Deep-link rule: [..]  Back behaviour: [..]  Leave warning: [..]
## Final submit
Review step contents · server re-validation scope · idempotency key · error-to-step mapping
## Instrumentation
## Findings (for an existing flow)
| ID | Finding | Severity | Confidence | Evidence | Fix |
```

## Verification

- [ ] The visible step list is derived from answers, not hard-coded.
- [ ] Every branch-deciding field has an invalidation rule.
- [ ] Submission payload is built from reachable steps only.
- [ ] Draft storage choice is justified against field sensitivity.
- [ ] Drafts carry a schema version and a mismatch rule.
- [ ] Refresh, back, deep link and double-click were each tested.
- [ ] Server re-validates the full payload and accepts an idempotency key.

## False-Positive Prevention

1. **One form per step as simpler.** Separate forms lose cross-step rules and make
   invalidation harder; one state object with slices is usually simpler overall.
2. **`localStorage` as free persistence.** It keeps national ID numbers on a library
   computer; choose storage by sensitivity.
3. **Per-step client validation as sufficient.** Steps were valid when filled; prices,
   eligibility or earlier answers may have changed. Re-check at submit.
4. **Clearing every downstream answer on any change.** Only fields made unreachable
   should go; editing a phone number should not wipe the next five steps.
5. **A state machine library as a requirement.** A small explicit step graph often
   suffices; adopt a library when branches multiply, not by default.
6. **Drop-off blamed on length alone.** Check whether exits cluster at a step with a
   validation error spike or a draft-restore failure before cutting steps.

## Example Output

```
# Multi-step form state design — "Harrow Mutual" small-business insurance quote
Steps: 7 (5–7 shown depending on answers)   Date: 2026-10-02

## Step graph
| 1 Applicant type | type | always | 2b vs 2i | applicantSchema |
| 2b Business details | legalName, companyNo, employees | type=business | 4 | businessSchema |
| 2i Personal details | name, dob, niNumber | type=individual | — | personalSchema |
| 3 Premises | address, sqm, buildYear | always | 3a | premisesSchema |
| 3a Listed building | listingGrade | buildYear < 1900 | — | listedSchema |
| 4 Employees' liability | payroll | employees > 0 | — | elSchema |
| 5 Cover & review | coverLevel, startDate | always | — | coverSchema + full refine |

## Failure modes and the design choice that prevents each
| Business→Individual switch submits companyNo | branch invalidation; payload from reachable steps |
| Refresh on step 4 loses data | sessionStorage draft, autosave 1,000 ms + on step change |
| Cross-device "continue later" | server draft for signed-in users only |
| Old draft after deploy | draft.v=3; v2 → migrate (field rename map); v1 → discard + notice |
| Double click on Submit | idempotency key from review step; server returns first quote |

## Branch invalidation rules
| type | 2b ↔ 2i fields | park (restore if switched back within session) |
| buildYear ≥ 1900 | listingGrade | clear |
| employees → 0 | payroll | clear |

## Draft persistence
Storage: sessionStorage (anonymous), server draft (signed in). niNumber never stored client-side;
re-entered on resume. Retention: server drafts deleted after 30 days.

## Navigation
/quote/:step; deep link to /quote/cover with empty premises → redirect /quote/premises.
Back = previous reachable step. Leave warning only if unsaved (not autosaved) input exists.

## Final submit
Server validates full schema incl. startDate ≥ today and premium recalculated (rate table may have
changed since step 5 opened); mismatch → return to review with the new price highlighted.
Server error "companyNo not found" → route to step 2b with field error.

## Findings (current production flow)
| W1 | 6.8% of individual quotes contain companyNo | High | High | data export, 4,112 of 60,470 | invalidation |
| W2 | 23% of step-4 exits follow a refresh event | High | Medium | analytics | session draft |
| W3 | 312 duplicate quotes last month from double submit | Medium | High | DB query | idempotency key |
```

## Techniques Used

- **GT-01 Phase-Gated Action Cycle** — submit is reachable only from the review step, after all reachable steps validate.
- **GT-06 Pre-Commit Recheck** — the server re-validates the whole payload and recalculates live values immediately before commit.
- **DP-07 Failure Mode Prediction** — branch switches, refresh, deep links, deploys and double submits are named before choices are made.
- **RT-02 Multi-Dimensional Analysis Framework** — graph, invalidation, persistence, navigation and submission designed as separate dimensions.

## Related Prompts

- `frontend_forms_validation_design.md` — per-field and per-step validation rules and async checks this design relies on.
- `frontend_forms_accessibility_ux.md` — announcing step changes, moving focus and labelling progress.
- `domain-frontend-development/architecture/frontend_state_management_selection.md` — when the flow's state should live in an app-wide store.
