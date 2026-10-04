---
title: "Transcreation Brief — Re-Creating a Headline, Slogan, or Campaign Line for Another Language and Culture"
category: professional-writing/translation
description: "Brief and evaluate the creative adaptation of marketing and creative copy into another language: decompose each source line into intent, mechanism (pun, rhyme, idiom, cultural reference), and mandatories; separate what must stay identical (brand name, regulated claims, legal lines) from what is free; commission close, adapted, and free routes per line, each with a literal back-translation and rationale; score routes on anchored criteria; and require an in-market native check for unintended meanings and a legal check on claims and name conflicts before anything ships."
techniques:
  - CM-12
  - CM-11
  - QA-02
  - DS-06
difficulty: advanced
tags:
  - human-translation
  - transcreation
  - creative-adaptation
  - marketing-copy
  - back-translation
  - tagline
  - adapt-slogan-for-another-country
  - pun-does-not-translate
  - campaign-in-another-language
updated: "2026-10-02"
related_prompts:
  - domain-professional-writing/translation/translation_project_brief_and_glossary.md
  - domain-software-engineering/localization/localization_cultural_adaptation.md
  - domain-agentic-resources/skills/marketing/copywriting/SKILL.md
---

# Transcreation Brief

**Objective:** Get a campaign line, slogan, or headline to land in another language the
way it lands at home — same intent, same effect, its own words — while keeping every
mandatory element identical and catching the meanings a non-native team cannot hear.

**When to Use:**
- A tagline, headline, product name, or campaign idea relies on wordplay, rhythm, an
  idiom, or a cultural reference that will not survive translation.
- A brand is launching a campaign in a new market and wants it to sound native.
- A literal translation came back correct but flat, or accidentally funny.
- **Not this prompt if** the text is informational and accuracy is the goal — brief it
  with `translation/translation_project_brief_and_glossary.md`. For adapting a website or
  app's imagery, colours, and content strategy by region, use
  `domain-software-engineering/localization/localization_cultural_adaptation.md`. To
  write the original source-language copy, use
  `domain-agentic-resources/skills/marketing/copywriting/SKILL.md`.

> **Native-market rule.** The routes are written or confirmed by a transcreator who is a
> native speaker of the target language living in, or closely connected to, the market,
> with copywriting skill. A model may propose routes and back-translations, but no line
> ships without an in-market native check (step 6) and, for claims or names, a legal check.

## Inputs / Context

1. **Source creative** — every line, with the visual it sits on and the channel.
2. **Brand voice** — three adjectives and two lines the brand would never say.
3. **Campaign objective** — what the reader should feel, think, or do.
4. **Target market** — language variant, region, audience segment.
5. **Mandatories** — brand name, product names, regulated or substantiated claims,
   legal lines, character limits per placement.
6. **Known sensitivities** — cultural, religious, political, competitor slogans in market.

## Method

1. **Decompose each line through several lenses (CM-12).** For every line record:
   *intent* (what it must make the reader feel or do), *mechanism* (pun, rhyme,
   alliteration, idiom, cultural reference, imperative), *literal content*, *tone*, and
   *relationship to the visual*. The mechanism is what usually cannot be translated;
   the intent is what must survive.
2. **Separate fixed from free, with reasons (CM-11).**
   - **Fixed:** brand name, trademarks, legal lines, and **claims** — a claim cannot be
     strengthened or added in adaptation ("the best", "clinically proven", "natural"),
     because what is substantiated at home may be unsubstantiated or regulated in the
     target market.
   - **Free:** wording, image metaphor, idiom, rhythm — anything that serves the intent
     and stays within the brand's voice.
3. **Commission three routes per key line.**
   - **Close** — as near the source as works naturally.
   - **Adapted** — a new mechanism doing the same job (a target-language idiom for a
     source pun).
   - **Free** — a new line from the intent, if the market needs it.

   Each route carries a **literal back-translation** into the source language and a
   one-line rationale, so non-speakers can judge what it says.
4. **Score each route (DS-06).** Anchored 1–5 on: intent fidelity, naturalness in market,
   brand-voice fit, risk (unintended meanings, claims), and fit to placement (length, visual).
   Risk is a gate, not a weight: a route with an unresolved risk flag cannot win.
5. **Check length and placement.** Character counts per placement; the line works with
   the visual it sits on; no idiom that depends on a picture the market will not see.
6. **Stress-test before choosing (QA-02).** An in-market native reviewer, not the
   transcreator, checks each surviving route for: slang or double meanings, homophones,
   unfortunate associations, similarity to a competitor's or a political slogan, and
   region-specific readings. Product or campaign **names** get a trademark search and a
   linguistic check in market.
7. **Recommend and record.** The recommended route per line, a runner-up, the reasons,
   and the open risks for the client and their legal team.

## Output Format

```
# Transcreation — [campaign]   [source] → [target market]   Due: [..]

## Line decomposition
| Line | Intent | Mechanism | Literal content | Tone | Visual link |

## Fixed vs free
Fixed: [items, with reason]   Free: [...]

## Routes
### Line [n]: "[source]"
| Route | Target line | Back-translation | Rationale | Chars |
|---|---|---|---|---|
| Close | | | | |
| Adapted | | | | |
| Free | | | | |

## Scores (1–5; risk is a gate)
| Route | Intent | Natural | Voice | Placement | Risk flag | Total |

## In-market check
[reviewer; findings per route]

## Recommendation
Line [n]: [route] — runner-up: [..] — why: [...]
Open risks for client/legal: [...]
```

## Verification

- [ ] Every line has intent and mechanism recorded before any route was written.
- [ ] Fixed items appear unchanged in every route; no claim is stronger than the source.
- [ ] Every route has a literal back-translation and a rationale.
- [ ] Scores use stated anchors; no route with an open risk flag is recommended.
- [ ] A named in-market native reviewer checked the surviving routes.
- [ ] Names and claims are flagged for trademark and legal checks.

## False-Positive Prevention

1. **Close is not automatically safe.** A faithful line can be flat, odd, or carry a
   second meaning the source never had.
2. **Free is not automatically better.** A brilliant new line that drifts from the
   campaign's intent breaks the campaign across markets.
3. **Back-translation is a window, not a verdict.** It shows what a line says, not how it
   feels; never choose on back-translation alone.
4. **The transcreator cannot clear their own line.** The stress-test is a second native
   speaker's job.
5. **Don't import claims.** "Proper" or "real" in one market may be a regulated or
   challengeable claim in another; flag for legal rather than assume.
6. **Don't over-localise the brand.** The brand's voice survives; only its words change.

## Example Output

Scenario: UK bakery chain "Hearth" opening shops in Germany; hero line "Proper bread.
No shortcuts." on a photo of dough proving overnight; poster and social placements
(≤ 40 characters); brand voice: warm, plain, a little dry.

```
# Transcreation — Hearth launch   EN (UK) → DE (Germany)   Due: 2026-11-04

## Line decomposition
| "Proper bread. No shortcuts." | trust: we do it the slow, right way | two-beat rhythm;
  "proper" is warm British colloquial; "shortcuts" = cutting corners | bread made properly,
  without cutting corners | dry, confident | dough proving overnight |

## Fixed vs free
Fixed: "Hearth" (trademark); no claim beyond the source (no "best", no "traditional"
  unless substantiated). Free: wording, idiom, rhythm.

## Routes
### Line 1: "Proper bread. No shortcuts."
| Close   | "Richtiges Brot. Ohne Abkürzungen." | Right bread. Without shortcuts/abbreviations. |
  literal | 33 |
| Adapted | "Echtes Brot. Ohne Wenn und Aber." | Real bread. Without ifs and buts. | German
  idiom for "no compromise"; keeps two-beat rhythm | 32 |
| Free    | "Brot braucht Zeit. Wir nehmen sie uns." | Bread needs time. We take it. | ties
  to the overnight-proving photo; warm and plain | 38 |

## Scores (1–5; risk is a gate)
| Close   | 3 | 2 | 2 | 5 | "Abkürzungen" reads first as "abbreviations" | — (gated) |
| Adapted | 4 | 5 | 4 | 5 | "echt" may be read as a quality claim → legal check | 18 (pending) |
| Free    | 5 | 5 | 5 | 4 | none found | 19 |

## In-market check
Reviewer: J. Hartmann (Hamburg). Close: "sounds like a dictionary". Adapted: natural; the
idiom is common in ads. Free: natural, fits the photo; no double meanings.

## Recommendation
Line 1: Free — runner-up: Adapted (if legal clears "echt") — why: carries intent and
links to the visual. Open risks: trademark search for "Hearth" in DE; legal view on "echt".
```

## Techniques Used

- **CM-12 Multi-Lens Request Framing** — each line read for intent, mechanism, content, tone, and visual.
- **CM-11 Reasoning-Based Constraint Design** — fixed items carry their reason (trademark, claims, law).
- **QA-02 Adversarial Stress-Test** — a second native speaker hunts unintended meanings and conflicts.
- **DS-06 Prioritization and Severity Guidance** — risk gates the scores before any route can win.

## Related Prompts

- `domain-professional-writing/translation/translation_project_brief_and_glossary.md` — the brief for informational text.
- `domain-software-engineering/localization/localization_cultural_adaptation.md` — regional adaptation of a product's content and design.
- `domain-agentic-resources/skills/marketing/copywriting/SKILL.md` — writing the source-language copy.
