---
title: "TypeScript Component and Props Typing"
category: frontend-development/typescript
description: "Design and review type-safe component contracts — props, generics, discriminated unions, event handlers, refs, and children — across React, Vue, and Angular."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - typescript
  - component-typing
  - props
  - generics
  - discriminated-unions
  - event-handlers
  - react-vue-angular
updated: "2026-06-21"
related_prompts:
  - domain-frontend-development/typescript/frontend_typescript_type_safety_audit.md
  - domain-frontend-development/react/frontend_react_component_patterns.md
  - domain-frontend-development/vue/frontend_vue_composition_api.md
  - domain-frontend-development/angular/frontend_angular_architecture.md
---

# TypeScript Component and Props Typing

**Objective:** Design or review the type contracts of UI components — props, generic parameters, discriminated unions for variant APIs, event-handler and ref types, and children/slot typing — so that misuse is caught at compile time and component APIs are self-documenting, across React, Vue, or Angular.

**When to Use:**
- Use when: Designing a reusable component's public type API (props, variants, generics)
- Use when: Reviewing components where props are loosely typed, over-typed, or rely on runtime checks the types could enforce
- Use when: A polymorphic/variant component needs mutually-exclusive prop combinations expressed in the type system
- Don't use when: You need a whole-codebase soundness audit (use the type-safety audit prompt) or a runtime-validation/schema design task

## Instructions

1. **Identify the framework and typing idioms in use**
   - Determine the framework (React, Vue with `<script setup>`/`defineProps`, Angular with decorators/inputs) and its idiomatic typing approach
   - Note the TypeScript configuration relevant to components (`strict`, `exactOptionalPropertyTypes`, JSX settings)
   - Identify whether types are authored manually, inferred, or generated — and treat framework-version-specific macro/decorator behavior as "verify against current docs"

2. **Review the props contract**
   - Check that required vs optional props are modeled correctly (avoid optional props that are actually required)
   - Look for overly-broad prop types (`string` where a union of literals is meant; `any`/`object`)
   - Evaluate default values and whether optionality matches defaults
   - Assess whether prop names and types are self-documenting and minimal (no leaking internal types into the public API)

3. **Model variant APIs with discriminated unions**
   - Find components with mutually-exclusive prop combinations enforced only at runtime (e.g., `href` vs `onClick`, `variant`-dependent props)
   - Express these as discriminated unions keyed on a literal discriminant so invalid combinations fail to compile
   - Verify exhaustiveness handling (a `never` check in the default branch of switches over the discriminant)
   - Ensure the union does not degrade autocomplete or produce confusing error messages

4. **Type generics deliberately**
   - Identify components that should be generic (lists, selects, tables, data renderers) and parameterize them over the item/value type
   - Constrain type parameters appropriately (`<T extends ...>`); avoid unconstrained generics that collapse to `unknown`/`any`
   - Check that generic inference flows from props (e.g., `items` infers `T`) rather than requiring explicit annotation at call sites
   - Avoid gratuitous generics where a concrete type is clearer

5. **Type events, refs, and children/slots**
   - Use the framework's precise event types for handlers (avoid `any` event parameters); narrow `event.target`/`currentTarget` correctly
   - Type refs/`ref`/template refs and forwarded refs precisely (element type or component instance type)
   - Type `children`/slots/`ng-content` projections to the intent (renderable content vs a render function vs a constrained element)
   - For polymorphic `as`/element-type props, type the resulting attribute surface correctly or note the complexity tradeoff

6. **CRITICAL: Verify findings before reporting**
   - Confirm a "missing" type would actually catch a real misuse, not just add ceremony
   - Check that a proposed discriminated union compiles and preserves good autocomplete before recommending it
   - Validate generic inference at representative call sites rather than only at the definition
   - **Confidence level** for each finding:
     - **High Confidence:** A type clearly permits a real misuse, or a runtime-only invariant is trivially expressible in types
     - **Medium Confidence:** A typing improvement that is likely beneficial but adds API surface or complexity
     - **Low Confidence:** A stylistic or advanced-typing suggestion whose payoff depends on usage patterns

7. **Prioritize recommendations**
   - Rank by the severity of bugs the typing change prevents and by API clarity
   - Separate quick wins (literal unions, precise event types) from larger redesigns (generic refactor, polymorphic typing)
   - Note any DX tradeoffs (error-message clarity, inference depth) for advanced typings

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Add generics where a concrete type is clearer and the component is not actually reused across types
- Replace a simple optional prop with an elaborate union when a default value already expresses intent
- Recommend discriminated unions that worsen autocomplete or produce cryptic errors
- Type event handlers as `any` "to keep it simple" — the framework provides precise types
- Leak internal implementation types into a public props API for the sake of reuse
- Over-constrain generics so legitimate call sites no longer infer
- Assert framework-macro behavior (e.g., a specific `defineProps`/decorator capability) from memory — verify against current docs

✅ **DO:**
- Express runtime-only prop invariants (mutually-exclusive props) as discriminated unions when feasible
- Prefer literal-union props over broad `string`/`number` for finite sets
- Use the framework's event and ref types; narrow targets explicitly
- Make generics infer from props so call sites stay clean
- Keep the public API minimal and self-documenting; hide internals
- Add exhaustiveness `never` checks so new variants surface as compile errors
- Note DX tradeoffs and verify framework-specific behavior against current docs

## Expected Output

A component-typing design/review including:
- Framework and typing-idiom identification
- A props, variant, generics, and events/refs/children assessment
- Concrete typed examples for recommended changes
- Detailed findings with severity, confidence, location, and evidence
- Prioritized recommendations with DX tradeoffs noted

### Output Format

```markdown
## TypeScript Component Typing Review

### Executive Summary
[2-3 sentences: overall type-contract quality and the highest-value improvements]

### Context
- **Framework:** [React / Vue / Angular]
- **Relevant tsconfig flags:** [strict, exactOptionalPropertyTypes, ...]
- **Typing style:** [manual / inferred / generated]

### Contract Assessment
| Dimension | Observation | Assessment |
|-----------|-------------|------------|
| Props precision | ... | ... |
| Variant modeling | ... | ... |
| Generics | ... | ... |
| Events / refs / children | ... | ... |

### Detailed Findings

#### Finding 1: [Name]
- **Severity:** High | Medium | Low
- **Confidence:** High | Medium | Low
- **Location:** [files]
- **Evidence:** [snippet]
- **Impact:** [what misuse it allows]
- **Recommendation:** [typed example]
- **DX Tradeoff:** [if any]
- **Effort:** Low | Medium | High

[Additional findings...]

### Prioritized Recommendations

#### Quick Wins (< 1 day each)
| # | Action | Impact | Effort |
|---|--------|--------|--------|

#### Larger Redesigns (multi-day)
| # | Action | Impact | Effort | Dependencies |
|---|--------|--------|--------|--------------|

### Patterns to Preserve
[List]
```

## Example Output

```markdown
## TypeScript Component Typing Review

### Executive Summary
The `Button` component allows incompatible prop combinations (both `href` and `onClick`) that only fail at runtime, and the `Select` component is non-generic so its `onChange` value is typed `any`. Modeling `Button` as a discriminated union and making `Select` generic over its option type would eliminate two classes of real bugs with modest, autocomplete-friendly changes.

### Context
- **Framework:** React (TSX)
- **Relevant tsconfig flags:** `strict: true`, `exactOptionalPropertyTypes` not set
- **Typing style:** Manual prop interfaces

### Contract Assessment
| Dimension | Observation | Assessment |
|-----------|-------------|------------|
| Props precision | `variant: string` should be a literal union | Weak |
| Variant modeling | `Button` link/button modes not discriminated | Weak |
| Generics | `Select` not generic; value is `any` | Weak |
| Events / refs / children | `onClick: (e: any) => void` in places | Mixed |

### Detailed Findings

#### Finding 1: `Button` Permits Incompatible Props
- **Severity:** High
- **Confidence:** High
- **Location:** `src/ui/Button.tsx`
- **Evidence:**
  ```tsx
  interface ButtonProps {
    href?: string;        // link mode
    onClick?: () => void; // button mode
    variant?: string;     // should be a union
  }
  ```
- **Impact:** A `Button` can be given both `href` and `onClick`, or an invalid `variant`; misuse surfaces only at runtime.
- **Recommendation:** Discriminate the two modes and use a literal union for `variant`:
  ```tsx
  type Variant = 'primary' | 'secondary' | 'ghost';
  type ButtonProps =
    | { as: 'a'; href: string; variant?: Variant; onClick?: never }
    | { as?: 'button'; onClick: () => void; variant?: Variant; href?: never };
  ```
- **DX Tradeoff:** Slightly longer type; autocomplete remains good because the discriminant is `as`.
- **Effort:** Low

#### Finding 2: `Select` Is Not Generic
- **Severity:** Medium
- **Confidence:** High
- **Location:** `src/ui/Select.tsx`
- **Evidence:**
  ```tsx
  interface SelectProps {
    options: { label: string; value: any }[];
    onChange: (value: any) => void; // value is any
  }
  ```
- **Impact:** Callers lose type information about the selected value; typos and wrong-type handling go uncaught.
- **Recommendation:** Parameterize over the value type so it infers from `options`:
  ```tsx
  interface SelectProps<T> {
    options: { label: string; value: T }[];
    value?: T;
    onChange: (value: T) => void;
  }
  function Select<T>(props: SelectProps<T>) { /* ... */ }
  // <Select options={[{label:'A', value:1}]} onChange={(v) => /* v: number */} />
  ```
- **DX Tradeoff:** None significant; `T` infers from `options`.
- **Effort:** Low

#### Finding 3: Imprecise Event Handler Types
- **Severity:** Low
- **Confidence:** Medium
- **Location:** `src/ui/SearchBox.tsx`
- **Evidence:**
  ```tsx
  const onChange = (e: any) => setQuery(e.target.value);
  ```
- **Impact:** No checking that `target` is an input; `value` access is unverified.
- **Recommendation:** Use the framework's event type and narrow:
  ```tsx
  const onChange = (e: React.ChangeEvent<HTMLInputElement>) =>
    setQuery(e.currentTarget.value);
  ```
- **DX Tradeoff:** None.
- **Effort:** Low

### Prioritized Recommendations

#### Quick Wins (< 1 day each)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Discriminate `Button` modes + literal `variant` union | High - blocks invalid combos | 2 hours |
| 2 | Make `Select` generic over option value | Medium - value type safety | 2 hours |
| 3 | Replace `any` event params with precise event types | Low - target safety | 1 hour |

#### Larger Redesigns (multi-day)
| # | Action | Impact | Effort | Dependencies |
|---|--------|--------|--------|--------------|
| 1 | Introduce a polymorphic `as` prop pattern for layout primitives | Medium - flexible, typed element surface | 3 days | Agree on the pattern + error-message tradeoffs |

### Patterns to Preserve
- **Manual prop interfaces with explicit required/optional** where already precise
- **Forwarded refs typed to the underlying element** in existing inputs
- **Exhaustive `switch` over existing variant unions** with a `never` default
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Focuses on compile-time-enforced component contracts across frameworks
- **ST-02 (Structured Sequential Instructions):** Steps move from framework idioms to props to variants to generics to events/refs
- **RT-02 (Multi-Dimensional Analysis Framework):** Treats props precision, variant modeling, generics, and event/ref typing as separate axes
- **RT-05 (Evidence-Based Reasoning):** Each finding cites code and shows a concrete typed fix
- **DS-06 (Prioritization Guidance):** Splits quick wins from larger redesigns and notes DX tradeoffs

## Related Prompts

- [frontend_typescript_type_safety_audit.md](frontend_typescript_type_safety_audit.md) - Whole-codebase soundness and `any`-leakage audit
- [../react/frontend_react_component_patterns.md](../react/frontend_react_component_patterns.md) - Component composition the types should mirror
- [../vue/frontend_vue_composition_api.md](../vue/frontend_vue_composition_api.md) - Typing `defineProps`/composables in Vue
- [../angular/frontend_angular_architecture.md](../angular/frontend_angular_architecture.md) - Typed inputs/outputs in Angular components
