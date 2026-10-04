---
title: "Motion System Design — Duration and Easing Tokens, Choreography Rules, Pattern Catalogue, and Reduced-Motion Mapping"
category: frontend-development/animation
description: "Design a product's motion system as a small set of named duration and easing tokens, a catalogue of approved motion patterns tied to their purpose, choreography rules for stagger, sequencing and interruption, and a reduced-motion mapping for every pattern — starting from an inventory of the ad-hoc values already in the code."
techniques:
  - DS-26
  - DS-29
  - DS-02
  - QA-02
difficulty: intermediate
tags:
  - motion-design
  - motion-tokens
  - easing-curves
  - animation-duration
  - choreography
  - design-system
  - animations-feel-inconsistent
  - how-long-should-animation-be
  - make-ui-feel-polished
updated: "2026-10-03"
related_prompts:
  - domain-frontend-development/animation/frontend_animation_motion_performance.md
  - domain-frontend-development/design-direction/frontend_design_token_architecture.md
  - domain-frontend-development/design-direction/frontend_look_and_feel_hunt.md
---

# Motion System Design

**Objective:** Replace scattered, one-off animation values with a motion system a team can
apply without a designer in the room — five or six duration tokens, three or four easing
tokens, a catalogue of named patterns that say what each motion is *for*, choreography
rules, and a reduced-motion equivalent for every pattern — and give a migration path from
the values in the code today.

**When to Use:**
- The product animates, but every component picked its own `300ms ease` and it shows:
  modals, toasts and drawers each move differently.
- A design system is adding motion to its token set and needs a defensible scale.
- A redesign wants motion to carry a brand quality (calm, crisp, playful) consistently.
- Engineers keep asking "what duration should this be?" and there is no answer to point at.
- **Not this prompt if** animations stutter or drop frames — use
  `domain-frontend-development/animation/frontend_animation_motion_performance.md` (that is
  a jank and technique audit, not a system). If you are still choosing the *feel* of the
  brand, use `domain-frontend-development/design-direction/frontend_look_and_feel_hunt.md`
  first; this prompt turns a chosen feel into tokens. For vestibular safety, flashing and
  WCAG motion criteria, use `frontend_animation_motion_safety_audit.md`. General token
  tiers and naming live in
  `domain-frontend-development/design-direction/frontend_design_token_architecture.md`.

## Inputs / Context

1. **Current motion inventory**: every `transition`, `animation`, `@keyframes`, and JS
   animation call (Web Animations API, Framer Motion, GSAP), with its duration and easing.
   A code search export is enough.
2. **Desired motion character** in two or three words (e.g. "quick, confident, quiet"),
   ideally from an agreed look-and-feel spec.
3. **Component list** that moves: overlays, menus, toasts, tabs, accordions, route
   transitions, list insert/remove, loading states, gesture-driven surfaces.
4. **Platforms and input types**: pointer, touch, keyboard; whether native apps must match.
5. **Token pipeline**: how tokens ship today (CSS custom properties, Style Dictionary,
   Tailwind theme, JS constants).
6. **Constraints**: performance budget, accessibility commitments, animation libraries
   already in the bundle.

## Method

1. **Inventory and cluster what exists.** Group current durations and easings by value
   and by job. Count distinct values; most codebases have 15–30 durations doing five jobs.
   Note any easing used against its purpose (ease-in on an entering element).
2. **Fix purposes before values (DS-29).** Every motion must serve one of: *feedback*
   (a press registered), *state change* (expanded, selected), *spatial orientation*
   (where did this panel come from), *attention* (something needs you), or *continuity*
   (the same object moved). Motion with no purpose is decoration — candidate for removal.
3. **Define duration tokens by distance and size (DS-02).** A defensible default scale:
   `instant 0ms` · `fast 100ms` (feedback, hover, toggles) · `moderate 200ms` (small
   components entering: tooltip, menu) · `slow 300ms` (medium surfaces: dialog, drawer) ·
   `slower 400–500ms` (full-screen and route transitions). Rules: exits run at roughly
   two-thirds of the matching enter; nothing a user waits on exceeds 500ms; larger travel
   distance earns the next step up, not a bespoke value.
4. **Define easing tokens by direction of travel (DS-26).** `standard` (on-screen move,
   ease-in-out), `enter` (decelerate, ease-out: arrives fast, settles), `exit`
   (accelerate, ease-in: leaves without lingering), and optionally `spring` for
   gesture-driven or physical motion. Give each a `cubic-bezier()` value and a one-line
   rule. Linear only for continuous progress (spinners, progress bars).
5. **Write choreography rules.** Stagger list items 20–40ms each and cap the total
   stagger (e.g. first 6 items, ≤200ms); one primary motion at a time; parent before
   child on enter, child before parent on exit; shared-element transitions for continuity;
   every interactive transition must be interruptible and reversible mid-flight (CSS
   transitions reverse; keyframe animations and some JS timelines do not).
6. **Map every pattern to a reduced-motion equivalent.** Under
   `prefers-reduced-motion: reduce`, replace translation, scaling, parallax and rotation
   with a short opacity cross-fade or an instant state change; keep feedback that carries
   meaning. Record the mapping per pattern, not as one global kill switch.
7. **Stress-test the system (QA-02).** Apply it to the three hardest cases in the
   inventory (e.g. a nested drawer inside a dialog, a 50-row list insert, a route change
   during a pending request). If a case needs a new value, either add a token with a
   rule or change the case; never allow an untracked one-off.
8. **Plan adoption.** Token names and values, lint rule or codemod that flags raw
   durations, and the order of migration (highest-traffic components first). Rate each
   inventory finding's confidence: High when read from code, Medium when inferred from a
   recording, Low when reported by a designer without a reproduction.

## Output Format

```
# Motion system — [product]   Character: [2–3 words]   Date: [..]

## Inventory (today)
Distinct durations: [n]   Distinct easings: [n]   Purpose-less motions: [n]
| Job | Current values in use | Components | Notes |

## Duration tokens
| Token | Value | Use for | Not for |

## Easing tokens
| Token | cubic-bezier | Use for | Rule |

## Pattern catalogue
| Pattern | Purpose | Duration | Easing | Properties | Reduced-motion equivalent |

## Choreography rules
## Stress tests
| Case | Fits system? | Change made |
## Adoption plan
| Step | Scope | Mechanism (codemod / lint / manual) | Order |
## Confidence notes
```

## Verification

- [ ] Every token has a value, a "use for" and a "not for".
- [ ] Every catalogue pattern names its purpose from the five-purpose list.
- [ ] Exit durations are shorter than enter durations for the same surface.
- [ ] No user-awaited motion exceeds 500ms.
- [ ] Every pattern has a reduced-motion equivalent stated individually.
- [ ] Stress tests are reported, with any new token justified by a rule.
- [ ] Values are expressed in the team's token pipeline format.

## False-Positive Prevention

1. **More tokens as more control.** Eleven durations is no system. If two values are
   within ~50ms and do the same job, merge them.
2. **Brand character as long durations.** "Calm" is carried by easing and restraint, not
   by 600ms dialogs that make the product feel slow.
3. **Reduced motion as no motion.** Removing all transitions can make state changes
   harder to follow; a short cross-fade usually serves better than an instant jump.
4. **Library defaults as the system.** A library's default spring or tween is somebody
   else's decision. Adopt it only after checking it against the tokens.
5. **Ignoring interruption.** A beautiful 300ms menu that cannot be reversed when the
   user clicks away mid-open feels broken. Test interruption, not only playback.
6. **Treating performance as solved by tokens.** Tokens set timing; animating `height`
   still janks. Route property choices to the motion-performance audit.
7. **Value precision from a recording.** Durations read off a screen recording are
   approximate; confirm in code before calling a value "wrong".

## Example Output

```
# Motion system — "Ledger" B2B finance web app   Character: quick, quiet, precise

## Inventory (today)
Distinct durations: 23 (80ms–700ms)   Distinct easings: 9   Purpose-less motions: 4
| Overlay enter   | 150, 200, 250, 300, 350, 400ms | Dialog, Drawer, Sheet, Popover | 6 values, 1 job |
| Feedback        | 80, 100, 120, 150ms            | Button, Toggle, Checkbox        | |
| List change     | 300ms each row, no cap         | Transactions table              | 50 rows = 15 s cascade |
| Exits           | same as enters, ease-in-out    | all overlays                    | exits linger |
Purpose-less: logo wobble on hover, card tilt, dashboard number count-up on every
refetch, background gradient drift (continuous).

## Duration tokens
| motion.duration.fast     | 100ms | press, hover, toggle, focus ring | surfaces |
| motion.duration.moderate | 200ms | tooltip, menu, popover, toast    | full-screen |
| motion.duration.slow     | 300ms | dialog, drawer, sheet            | feedback |
| motion.duration.slower   | 450ms | route transition, full-screen    | anything awaited twice |
Exits: use one step down (dialog exits at moderate 200ms).

## Easing tokens
| motion.easing.standard | cubic-bezier(0.2, 0, 0, 1)   | on-screen move/resize | |
| motion.easing.enter    | cubic-bezier(0, 0, 0.2, 1)   | elements arriving     | decelerate |
| motion.easing.exit     | cubic-bezier(0.4, 0, 1, 1)   | elements leaving      | accelerate |
| motion.easing.linear   | linear                        | progress, spinners only | |

## Pattern catalogue
| Dialog open    | orientation | slow 300 | enter | opacity, transform scale 0.98→1 | fade 150 only |
| Drawer open    | orientation | slow 300 | enter | transform translateX            | fade 150 only |
| Toast in/out   | attention   | moderate/fast | enter/exit | transform Y, opacity     | fade, no slide |
| Row inserted   | continuity  | moderate | enter | opacity, background highlight   | highlight only |
| Button press   | feedback    | fast     | standard | transform scale 0.98         | unchanged (tiny) |
| Route change   | continuity  | slower   | standard | opacity cross-fade           | instant |

## Choreography rules
Stagger 30ms for the first 6 rows, then all remaining rows together (cap 180ms).
Dialog backdrop starts with the panel; panel content does not animate separately.
Count-up animations only on first load, never on refetch.

## Stress tests
| Drawer opened from inside a dialog | yes | drawer uses slow; dialog does not re-animate |
| 50-row bulk import                 | no → changed | stagger cap rule added (was 15 s) |
| Route change while request pending | yes | cross-fade waits for skeleton, not data |

## Adoption plan
1. Ship tokens as CSS custom properties + JS constants (week 1).
2. Stylelint rule flags raw `ms` values outside tokens (week 1).
3. Codemod overlays (Dialog, Drawer, Sheet, Popover) — 6 values → 1 token (week 2).
4. Remove 4 purpose-less motions; product sign-off on logo wobble (week 2).

## Confidence notes
Inventory values: High (code search). Row cascade length: High (300ms × 50 rows, timed).
"Exits linger" complaint: Medium (support tickets, reproduced on 2 of 3 overlays).
```

## Techniques Used

- **DS-26 Safe Defaults Pattern** — a default duration and easing scale that produces reasonable motion without per-component decisions.
- **DS-29 Domain Pattern Library** — named motion patterns, each with purpose, timing, properties and reduced-motion equivalent.
- **DS-02 Metric Specification** — concrete ceilings (≤500ms awaited, exit ≈ ⅔ enter, stagger cap).
- **QA-02 Adversarial Stress-Test** — the system is applied to the hardest real cases before adoption.

## Related Prompts

- `frontend_animation_motion_performance.md` — making the chosen patterns run smoothly on real devices.
- `domain-frontend-development/design-direction/frontend_design_token_architecture.md` — where motion tokens sit among primitive, semantic and component tiers.
- `domain-frontend-development/design-direction/frontend_look_and_feel_hunt.md` — choosing the motion character this system encodes.
