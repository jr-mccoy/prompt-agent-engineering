---
title: "Motion Safety Audit — Vestibular Triggers, Flashing Thresholds, Auto-Playing Motion, and Reduced-Motion Alternatives Against WCAG"
category: frontend-development/animation
description: "Audit a site's motion for the people it can harm: classify every animation by vestibular risk, check flashing content against the WCAG three-flash and area thresholds, find auto-playing motion longer than five seconds without a pause control, and verify that each risky animation has a tested reduced-motion alternative rather than a global off switch."
techniques:
  - DS-32
  - RT-02
  - QA-24
  - DS-06
difficulty: intermediate
tags:
  - reduced-motion
  - vestibular-disorders
  - wcag-animation
  - pause-stop-hide
  - photosensitive-seizures
  - parallax
  - accessibility-audit
  - website-makes-me-dizzy
  - stop-autoplaying-animation
  - motion-sickness-from-scrolling
updated: "2026-10-03"
related_prompts:
  - domain-frontend-development/animation/frontend_animation_motion_performance.md
  - domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md
  - domain-frontend-development/animation/frontend_animation_motion_system_design.md
---

# Motion Safety Audit

**Objective:** Find the motion on a site that can make people dizzy, nauseous, or unable to
read — or, in the case of flashing, trigger seizures — and produce a fix list where each
finding cites the WCAG success criterion or vestibular trigger involved, the evidence, and
a tested alternative that keeps the interface understandable.

**When to Use:**
- A user or support ticket says the site "makes me feel sick" or "won't stop moving".
- A launch includes parallax, scroll-linked effects, auto-playing video backgrounds,
  carousels, or animated illustrations.
- An accessibility audit needs its motion slice done in depth (WCAG 2.2.2, 2.3.1, 2.3.3).
- The team added `prefers-reduced-motion` once and has never checked what it covers.
- **Not this prompt if** the problem is dropped frames and stutter — use
  `domain-frontend-development/animation/frontend_animation_motion_performance.md`. For a
  whole-site WCAG audit across all criteria, use
  `domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md`; this
  prompt goes deeper on motion only. To define the motion tokens and patterns themselves,
  use `frontend_animation_motion_system_design.md`.

## Inputs / Context

1. **Pages and states in scope**, including scroll-heavy marketing pages and in-app
   transitions.
2. **Motion inventory** if one exists; otherwise screen recordings at 60fps of each page
   scrolled top to bottom and each major interaction.
3. **Code access** to CSS (`@keyframes`, `transition`, scroll-driven animations), JS
   animation libraries, video and Lottie/GIF assets, and any reduced-motion handling.
4. **Conformance target** (usually WCAG 2.2 AA; note that 2.3.3 is AAA but is the
   criterion most directly about vestibular harm).
5. **Product constraints**: which motion is considered essential to meaning.

## Method

1. **Enumerate the applicable criteria (DS-32).**
   - **2.2.2 Pause, Stop, Hide (A):** moving, blinking or scrolling content that starts
     automatically, lasts more than 5 seconds and sits alongside other content needs a
     mechanism to pause, stop or hide it.
   - **2.3.1 Three Flashes or Below Threshold (A):** nothing flashes more than three times
     in any one-second period, unless below the general and red flash thresholds (the
     area rule: combined flashing area under roughly a 341 × 256 px rectangle at a
     1024 × 768 viewing reference).
   - **2.3.3 Animation from Interactions (AAA):** motion triggered by interaction can be
     disabled unless essential.
   - **`prefers-reduced-motion` (Media Queries Level 5)** as the user's OS-level signal.
2. **Inventory and classify every animation (RT-02)** on four axes: trigger
   (auto / scroll / interaction), duration and looping, area of the viewport that moves,
   and vestibular pattern. High-risk patterns: parallax at different speeds, scroll-jacking
   or scroll-linked movement in a direction other than the scroll, zoom/scale of large
   areas, spinning or rotation, large-area slides, and auto-playing background video with
   camera movement. Low-risk: opacity fades, colour changes, small-area transforms under
   ~10% of the viewport.
3. **Test flashing content.** For any blinking, strobing, rapid colour alternation, or
   video, count flashes per second frame by frame; if more than three, measure area
   against the threshold. Use a photosensitivity analysis tool (e.g. PEAT) for video.
   Treat a failure here as blocking: it is a seizure risk, not a comfort issue.
4. **Check auto-playing motion against 2.2.2.** For carousels, marquees, animated
   heroes, Lottie loops, and video backgrounds: does it run over 5 seconds, and is there a
   visible, keyboard-operable pause that persists? Pausing on hover alone fails keyboard
   and touch users.
5. **Audit the reduced-motion implementation.** Emulate `prefers-reduced-motion: reduce`
   in DevTools and re-run the inventory. For each high-risk animation, record what
   happens: removed, replaced with a cross-fade, or unchanged. Check JS libraries
   separately — CSS media queries do not reach JS-driven timelines unless the code reads
   `matchMedia('(prefers-reduced-motion: reduce)')` or the library's own reduced-motion
   setting (verify the setting's name against the library's current docs).
6. **Record what you checked and cleared (QA-24).** List animations reviewed and judged
   safe with the reason (small area, opacity only, under 5 seconds, essential), so a short
   findings list is not mistaken for a short review.
7. **Prioritise (DS-06).** Flash failures first, then 2.2.2 failures, then high-risk
   vestibular motion without a reduced alternative, then in-app toggle and polish. Rate
   confidence: High = reproduced with emulation or frame count; Medium = read from code,
   not reproduced; Low = reported by a user without a reproduction.

## Output Format

```
# Motion safety audit — [site/pages]   Target: [WCAG level]   Date: [..]

## Criteria applied
## Motion inventory
| # | Element | Trigger | Duration/loop | Area | Pattern | Risk | Reduced-motion behaviour |
## Flashing
| Element | Flashes/s | Area vs threshold | Result |
## Auto-playing motion (2.2.2)
| Element | Runs > 5 s? | Pause control? | Keyboard/touch operable? | Result |
## Findings
| ID | Finding | Criterion / trigger | Severity | Confidence | Evidence | Fix |
## Checked and cleared
| Element | Why safe | Evidence |
## Prioritised fix list
```

## Verification

- [ ] Every finding names a WCAG criterion or a named vestibular pattern.
- [ ] Flashing content was counted frame by frame, not judged by eye.
- [ ] Every auto-playing element was timed against the 5-second rule.
- [ ] Reduced-motion behaviour was observed with emulation, not inferred from CSS alone.
- [ ] JS-driven animations were checked separately from CSS.
- [ ] A checked-and-cleared table exists.
- [ ] Fixes keep meaning intact (state changes remain perceivable).

## False-Positive Prevention

1. **All motion as harmful.** A 150ms opacity fade is not a vestibular trigger. Removing
   it can make state changes harder to perceive.
2. **Reduced motion as a global kill switch.** `* { animation: none !important }` breaks
   spinners, progress indicators and essential feedback. Reduce per pattern.
3. **Media query present = handled.** A CSS block does nothing for a GSAP or Framer
   Motion timeline that never reads the preference. Verify in the browser.
4. **Hover-to-pause as a pause mechanism.** It fails keyboard and touch users and does not
   persist; 2.2.2 needs a real control.
5. **Treating 2.3.3 as optional because it is AAA.** It may be outside the conformance
   target, but vestibular harm is real; report it as a recommendation with the level noted.
6. **Flash judgement from a recording at 30fps.** Low frame rates can hide flashes; use
   60fps capture or analyse the source asset.
7. **"Essential" stretched to cover brand motion.** Essential means the information or
   function would change without it; a hero parallax is not essential.

## Example Output

```
# Motion safety audit — "Northpeak Outdoor" marketing site + checkout
Target: WCAG 2.2 AA (2.3.3 reported as recommendation)   Date: 2026-10-02

## Motion inventory (12 animations; excerpt)
| 1 | Hero mountain parallax (3 layers) | scroll | continuous | 100% vw | parallax | High | unchanged |
| 2 | Promo marquee "FREE SHIPPING"     | auto   | infinite   | 6% vh   | scrolling text | Medium | unchanged |
| 3 | Product carousel                  | auto   | 4 s/slide, loops | 40% | large-area slide | High | stops autoplay |
| 4 | "Sale" badge pulse                | auto   | infinite, 4 Hz | 1% | flashing | — | unchanged |
| 5 | Add-to-cart button scale          | click  | 120ms      | <1%     | small transform | Low | unchanged |
| 6 | Route transition (checkout)       | click  | 350ms      | 100%    | horizontal slide | Medium | unchanged (GSAP) |

## Flashing
| Sale badge | 4 flashes/s (red↔white) | 48 × 20 px, far below area threshold | Pass 2.3.1 on area; still
  distracting — reduce to 1 Hz or static |

## Auto-playing motion (2.2.2)
| Marquee  | yes (infinite) | no            | — | Fail |
| Carousel | yes (loops)    | pause on hover | no (keyboard, touch) | Fail |

## Findings
| M1 | Marquee scrolls forever with no pause | 2.2.2 | High | High | timed; no control in DOM |
  Make static, or add visible Pause button that persists per session |
| M2 | Carousel pause only on hover | 2.2.2 | High | High | keyboard focus does not pause |
  Add Pause/Play button; stop autoplay on any interaction |
| M3 | Hero parallax unchanged under reduced motion | vestibular: parallax; 2.3.3 (AAA) | High | High |
  emulated reduce → layers still move at 0.3/0.6/1.0× | Static layered image under reduce |
| M4 | Checkout route slide ignores preference | 2.3.3 (AAA) | Medium | High | GSAP timeline never reads
  matchMedia | Cross-fade 150ms under reduce via matchMedia check |

## Checked and cleared
| Add-to-cart scale | <1% of viewport, 120ms, interaction-triggered | code + emulation |
| Form field focus glow | colour only, 100ms | code |
| Loading spinner | essential progress indicator; kept under reduce | product decision |

## Prioritised fix list
1. M1, M2 — 2.2.2 failures (Level A) — this sprint.
2. M3 — highest vestibular risk on the most-visited page — this sprint.
3. M4, badge pulse rate — next sprint; add in-app "Reduce motion" toggle that overrides OS.
```

## Techniques Used

- **DS-32 Regulatory Enumeration Pattern** — the WCAG motion criteria and media query listed up front with their thresholds.
- **RT-02 Multi-Dimensional Analysis Framework** — each animation classified by trigger, duration, area and vestibular pattern.
- **QA-24 Dismissed-Candidates Coverage Table** — safe animations recorded with the reason they were cleared.
- **DS-06 Prioritization and Severity Guidance** — seizure risk, then Level A failures, then vestibular risk, then polish.

## Related Prompts

- `frontend_animation_motion_performance.md` — when the same animations also stutter or drop frames.
- `domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md` — the full WCAG audit this motion slice plugs into.
- `frontend_animation_motion_system_design.md` — building reduced-motion equivalents into every motion pattern from the start.
