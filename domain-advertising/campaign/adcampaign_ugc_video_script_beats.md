---
title: "UGC Video Ad Script — Creator Brief, Hook Options, and Shot Beats"
category: advertising/campaign
description: "Produce a short-form UGC-style video ad package a creator can actually film: a one-page creator brief, three hook options for the first seconds, a timed beat sheet pairing each spoken line with a shot and on-screen text, a do-not-say list tied to substantiation, and the disclosure and usage-rights items to settle before filming. Aspect ratio, duration caps, and safe zones are marked [VERIFY current platform spec]. Distinct from the video skill (AI or programmatic video production), content_video_shot_list_preproduction (full live-action shot lists and shooting order), paid-ads' generic hook-problem-solution outline, and quality_slop_video_script (scoring a finished script)."
techniques:
  - CM-01
  - ST-02
  - OC-03
  - QA-01
difficulty: intermediate
tags:
  - advertising
  - ugc
  - video-ads
  - creator-brief
  - campaign
  - scriptwriting
updated: "2026-09-24"
related_prompts:
  - domain-agentic-resources/skills/marketing/video/SKILL.md
  - domain-professional-writing/content-production/content_video_shot_list_preproduction.md
  - domain-professional-writing/content-quality/quality_slop_video_script.md
---

# UGC Video Ad Script and Shot Beats

**Objective:** Give a creator everything needed to film one short vertical ad in a
single session — who they are talking to, what to say in the first seconds, what to
show at each beat, what they must not claim — while keeping the "native, unpolished"
feel that makes UGC work and the disclosure and rights questions settled up front.

**When to Use:**
- You are commissioning creators (or staff) to film talking-to-camera ads and the
  last round came back off-message, unusable, or unclaimable.
- You have a winning angle from the copy matrix and need it as video.
- You want several hooks on one body so the hook can be tested without refilming.

**When NOT to use:**
- You are generating video with AI tools, avatars, or code — `skills/marketing/video/`.
- The shoot has crew, locations, and multiple setups — build this script, then run
  `domain-professional-writing/content-production/content_video_shot_list_preproduction.md`.
- The script is written and you want it scored —
  `domain-professional-writing/content-quality/quality_slop_video_script.md`.
- You need a creator-partnership or influencer contract — `domain-legal/`; this
  prompt lists the terms to settle, not their drafting.

## Inputs / Context

1. **The angle and audience** (from the copy matrix), and the single takeaway.
2. **Proof points you hold**, each sourced — these bound what the creator may say.
3. **The product in use**: what can be shown on camera in under ten seconds.
4. **Placements** the cut will run on (for spec verification).
5. **Creator profile**: who they are, and whether they genuinely use the product.
6. **Mandatory elements**: brand mention, disclaimer, CTA.

## Method

1. **Write the creator brief first.** One page: who the viewer is, what they are
   struggling with, the one takeaway, the tone ("talking to a friend, not
   presenting"), and what the creator may improvise versus must say verbatim.
2. **Draft three hooks** for the opening seconds, each a different mechanism —
   a spoken problem, a visual pattern-interrupt, a result shown first. Each hook
   must work with sound off, so pair each with on-screen text.
3. **Build the beat sheet.** Four to six beats: hook → problem → product in use →
   proof → CTA. Each beat: approximate time range, spoken line, shot (framing and
   action), on-screen text. Keep timings approximate and total duration marked
   `[VERIFY current platform spec]` for each placement.
4. **Bind claims to proof.** Every spoken or on-screen claim maps to a proof point.
   Anything else goes on the do-not-say list — including results the creator
   personally experienced but that are not typical, unless the claims review has
   cleared how to present them.
5. **Specify capture.** Orientation, framing that keeps faces and text out of
   interface overlays (safe zones `[VERIFY current platform spec]`), clean audio,
   and B-roll of the product in real use.
6. **List what must be settled before filming.** Material-connection disclosure
   (how it will appear — spoken, on-screen, and/or platform tool), usage rights
   (paid use, duration, platforms, whitelisting), and approval rounds. Flag each
   for counsel or the contract owner; do not assert what the law requires.
7. **Define deliverables.** Takes per hook, raw files, captioned and uncaptioned
   versions, and the naming convention.

## Output Format

```
# UGC ad — [product / angle]

## Creator brief
Viewer: [...]    Their problem: [...]    One takeaway: [...]
Tone: [...]      Verbatim lines: [...]   Improvise freely: [...]

## Hooks (film all three on the same body)
| Hook | Mechanism | Spoken | On-screen text | Shot |
|---|---|---|---|---|

## Beat sheet  (duration: [VERIFY current platform spec])
| Beat | ~Time | Spoken | Shot | On-screen text | Proof point |
|---|---|---|---|---|---|

## Do-not-say
| Line to avoid | Why | Say instead |
|---|---|---|

## Capture spec
Orientation: [...]  Safe zones: [VERIFY current platform spec]  Audio: [...]  B-roll: [...]

## Settle before filming  (for counsel / contract owner)
- Disclosure method: [...]
- Usage rights: [paid use, term, platforms, whitelisting]
- Approvals: [rounds, turnaround]

## Deliverables
[takes, files, versions, naming]
```

## Verification

- [ ] The creator brief states one takeaway, not three.
- [ ] Each hook works with sound off.
- [ ] Every claim in the beat sheet maps to a sourced proof point.
- [ ] Duration, orientation, and safe zones are marked for verification, not asserted.
- [ ] Disclosure and usage rights are listed as items to settle, with an owner.
- [ ] The product appears in real use, not only held up to camera.

## False-Positive Prevention

1. **Polish is not the goal.** Adding studio lighting and a teleprompter script
   removes the thing being bought. Verbatim lines should be few.
2. **A creator's personal result is not a typical result.** "I lost 8 kg" is a
   claim; it goes to the claims review, not straight into the script.
3. **Do not assert disclosure rules.** Say that a material connection must be
   disclosed in a way the reviewer approves; the exact requirement is for counsel.
4. **Do not assert durations or safe zones.** Mark and verify per placement.
5. **One body, many hooks.** Refilming the whole ad to test a hook wastes the
   creator session.
6. **Usage rights are not implied by payment.** Paid use, term, and whitelisting
   are settled in writing before filming, or the best take may be unusable.

## Example

**Input:** Standing-desk converter. Angle: "back pain after long workdays" (from copy
matrix G1). Proof: "height adjusts in under 5 seconds" (internal test log
2026-08-12); "30-day returns" (terms page). Creator: remote worker, has used it
three months. Placements: two vertical short-video placements.

```
## Creator brief
Viewer: remote worker, sits 8+ hours.  Problem: stiff by 3pm.  Takeaway: switching
to standing takes seconds, so you actually do it.  Tone: end-of-day, honest.
Verbatim: product name; "30-day returns".  Improvise: your own workday story.

## Hooks
| H1 | Spoken problem | "It's 3pm and my back already hates me." | 3PM BACK? | Creator stretching at desk |
| H2 | Pattern interrupt | (no line — desk rises) | 5 seconds. | Desk rising, close-up |
| H3 | Result first | "I stand for half my calls now." | Half my calls, standing | Creator standing on call |

## Beat sheet (duration: [VERIFY current platform spec])
| 1 | 0–3s | [hook] | [hook] | [hook] | — |
| 2 | 3–8s | "I kept meaning to stand, but switching was a whole thing." | Old setup, sighing | Switching was a hassle | — |
| 3 | 8–16s | "This goes up in about five seconds." | Real-time raise, one hand | Under 5 seconds | Test log 2026-08-12 |
| 4 | 16–22s | "So I actually do it now." | Standing on a call | — | Creator's own use (opinion) |
| 5 | 22–27s | "And there's a 30-day return window." | Product + logo | 30-day returns | Terms page |

## Do-not-say
| "It fixed my back pain" | Health claim, no substantiation | "My afternoons feel better" — to claims review |
| "Best converter on the market" | Unsubstantiated superlative | Omit |

## Capture spec
Vertical, face upper-third, text mid-frame; safe zones [VERIFY current platform spec];
lav or phone mic close; B-roll of three real raises.

## Settle before filming
- Disclosure: spoken + on-screen, method per claims review.
- Usage rights: paid use on both placements, term [TBD], whitelisting yes/no [TBD].
- Approvals: one round, 48h.
```

The do-not-say row moved the creator's back-pain line out of the script and into
the claims review — the most likely line to make the ad unrunnable.

## Techniques Used

- **CM-01 Explicit Context Framing** — the creator brief gives viewer, problem,
  and tone before any line is written.
- **ST-02 Structured Sequential Instructions** — the timed beat sheet.
- **OC-03 Markdown Table Specification** — hooks, beats, and do-not-say as tables a
  creator can film from.
- **QA-01 Self-Verification** — claims bound to proof; specs marked, not asserted.

## Related Prompts

- `domain-agentic-resources/skills/marketing/video/` — AI and programmatic video.
- `domain-professional-writing/content-production/content_video_shot_list_preproduction.md` — crewed shoots.
- `adcampaign_claims_compliance_review.md` — clears the do-not-say list and disclosure.
- `adcampaign_copy_variant_matrix.md` — where the angle came from.
