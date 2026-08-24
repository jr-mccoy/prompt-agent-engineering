---
title: "User Story Reconstruction — Infer the User Stories Behind a Codebase"
category: "learning-coding"
description: "Reconstruct the likely user stories behind supplied code by inferring functionality and user needs from the actual implementation, then surface missing stories and prioritized enhancements — grounded in evidence and honest about inference."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-05
  - QA-01
difficulty: intermediate
tags:
  - learning-coding
  - user-stories
  - requirements
  - reverse-engineering
  - product
updated: "2026-06-07"
related_prompts:
  - domain-learning-coding/learning_backend_code_analysis.md
  - domain-learning-coding/learning_frontend_code_analysis.md
  - domain-learning-coding/learning_code_pattern_recognition.md
  - domain-learning-coding/learning_mini_lesson_generation.md
---

# User Story Reconstruction

**Objective:** Reconstruct the likely user stories behind supplied code by inferring functionality and user needs from the actual implementation, then surface missing stories and prioritized enhancements — grounded in code evidence and explicit about what is inferred.

**When to use:**
- Onboarding to an undocumented codebase by recovering its intended requirements.
- Reverse-engineering a legacy system before extending it.
- Teaching a learner to connect code to user needs.
- Finding requirement gaps before a refactor or feature push.

**When NOT to use:**
- Writing forward requirements for a new product (use a PRD prompt).
- When you have no code and would be inventing a product from scratch.
- When authoritative requirements docs already exist (read those instead).

**Audience:** Developers, product-minded engineers, and learners studying how code maps to needs.

---

## Inputs / Context

The user supplies:
1. **The code** to analyze, pasted wrapped in a named tag, e.g. `<code>...</code>`, or a reference (file paths).
2. **Language / framework / app type** (web app, API, CLI, mobile).
3. **Known user roles** if any (end user, admin, integrator).
4. **Goal** (onboarding understanding, gap analysis, enhancement planning).
5. **Optional:** any partial docs or product context.

Cite the code feature/location (referencing the tag name) behind each reconstructed story.

---

## Constraints

### Must
- Infer each story from observable functionality in `<code>`; cite the feature/location that supports it.
- Use the enhanced story template (Role / Need / Functionality / Benefit) consistently.
- Distinguish **reconstructed** stories (evidenced by code) from **inferred-need** statements (the "why," which is interpretation).
- Categorize stories (core features, UI, data, admin, integration) and keep them distinct and non-redundant.
- For missing stories and enhancements, ground suggestions in actual gaps, not wishlist features.

### Must Not
- Invent functionality the code doesn't implement.
- State a user benefit as fact when it's an interpretation — label it.
- Duplicate the same story across categories.
- Recommend enhancements unrelated to what the code does.

---

## Instructions

1. **Map functionality.** From `<code>`, list the core capabilities the code actually implements (endpoints, screens, jobs, commands), each with its location.
2. **Infer user needs.** For each capability, infer the need it addresses; mark the need as interpretation.
3. **Categorize.** Group capabilities (Core Features, UI, Data Processing, Admin, Integration).
4. **Write reconstructed stories.** For each, fill Role / Need / Functionality / Benefit, citing the supporting code.
5. **Identify missing stories.** From gaps evident in the code (e.g., create without delete, no error states, no admin path), propose the missing stories — flagged as gaps.
6. **Suggest enhancements.** Prioritized improvements that extend real functionality, each with a one-line rationale.
7. **Self-check (verification).** Does each reconstructed story trace to real code? Are needs/benefits labeled as inference? Are gaps real, not wishlist?

---

## False-Positive Prevention

❌ **DON'T:**
- Write a story for a feature the code doesn't actually implement.
- Present an inferred user motivation as established fact.
- Restate the same capability as multiple "different" stories.
- Suggest enhancements that have nothing to do with the existing code.
- Assume a user role the code shows no evidence of.

✅ **DO:**
- Cite the code feature behind every reconstructed story.
- Label needs and benefits as interpretation of intent.
- Keep stories distinct and grouped sensibly.
- Base missing-story claims on observable gaps in the code.
- Tie enhancements to real functionality.

---

## Output Format

```
# User Story Reconstruction — [app]

## Functionality Map
| Capability | Location | Inferred Need (interpretation) |

## Reconstructed User Stories
### [Category] — [brief description]
1. **Role:** ... **Need:** ... **Functionality:** ... **Benefit:** ...
   *(Evidence: [code location])*

## Potential Missing User Stories
### [Category] — [why valuable]
1. [story]  *(Gap: [what's absent in the code])*

## Enhancement Suggestions
| Priority | Enhancement | Rationale |
```

---

## Example Output

```markdown
# User Story Reconstruction — Orders Service (REST API)

## Functionality Map
| Capability | Location | Inferred Need (interpretation) |
|------------|----------|--------------------------------|
| Create order | `POST /orders` in `<code>` | Customers need to place orders |
| Get order | `GET /orders/{id}` | Customers/staff need to view an order |
| List orders | `GET /orders` (filter, paginate) | Staff need to find orders |
| Auth via JWT scopes | auth middleware | Access must be restricted by permission |

## Reconstructed User Stories

### Core Features — order lifecycle the API supports
1. **Role:** Customer **Need:** place an order for selected items **Functionality:** `POST /orders` with items + shipping address **Benefit:** complete a purchase without manual processing.
   *(Evidence: create handler + `CreateOrderDto` in `<code>`)*
2. **Role:** Customer **Need:** check the status/details of an order **Functionality:** `GET /orders/{id}` **Benefit:** confidence the order is being handled.
   *(Evidence: get handler in `<code>`)*

### Operations / Admin — staff order management
3. **Role:** Operations staff **Need:** find orders by customer or status **Functionality:** `GET /orders` with filters + pagination **Benefit:** locate and triage orders efficiently.
   *(Evidence: list handler query params in `<code>`)*

### Security — access control
4. **Role:** System **Need:** restrict actions by permission **Functionality:** JWT scope checks (`orders:read` / `orders:write`) **Benefit:** customers can't access others' orders; staff get appropriate access.
   *(Evidence: scope guards in `<code>`)*

## Potential Missing User Stories

### Order lifecycle completeness — gaps in the CRUD/lifecycle
1. **Role:** Customer **Need:** cancel a pending order **Functionality:** cancel endpoint **Benefit:** correct mistakes before fulfillment.
   *(Gap: no cancel/delete path found in `<code>` despite a `cancelled` status existing)*
2. **Role:** Operations staff **Need:** update order status **Functionality:** status-transition endpoint **Benefit:** move orders through fulfillment.
   *(Gap: statuses exist but no transition handler is present)*

### Resilience — error/edge handling
3. **Role:** Integrator **Need:** safe retries **Functionality:** idempotency on create **Benefit:** no duplicate orders on retry.
   *(Gap: Idempotency-Key documented in examples but no handling logic visible)*

## Enhancement Suggestions
| Priority | Enhancement | Rationale |
|----------|-------------|-----------|
| High | Order cancellation endpoint | A `cancelled` status exists with no way to reach it |
| High | Idempotency handling on create | Prevents duplicate orders on client retries |
| Medium | Status-transition endpoint | Completes the order lifecycle for staff |
| Low | Webhook on status change | Lets integrators react without polling |
```

---

## Verification

- [ ] Every reconstructed story cites the supporting code feature/location.
- [ ] Needs and benefits are labeled as interpretation, not fact.
- [ ] Stories are distinct, non-redundant, and categorized.
- [ ] Missing stories are based on observable gaps in the code.
- [ ] Enhancements extend real functionality, each with a rationale.
- [ ] No invented features or unsupported user roles.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the goal as evidence-grounded story reconstruction.
- **ST-02 (Structured Sequential Instructions):** Map → infer needs → categorize → reconstruct → gaps → enhancements → verify.
- **ST-03 (Output Format Specification):** Fenced template fixes the story/gap/enhancement structure.
- **RT-05 (Evidence-Based Reasoning):** Requires each story to trace to a real code feature.
- **QA-01 (Self-Verification):** Final pass confirms grounding and labels inference.

---

## Related Prompts

- `domain-learning-coding/learning_backend_code_analysis.md` — Analyze the backend behind the stories.
- `domain-learning-coding/learning_frontend_code_analysis.md` — Analyze the frontend behind the stories.
- `domain-learning-coding/learning_code_pattern_recognition.md` — Understand the patterns implementing the features.
- `domain-learning-coding/learning_mini_lesson_generation.md` — Teach the reconstructed system as lessons.
