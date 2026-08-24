---
title: "Children's Revision & Self-Edit Pass"
category: childrens-writing
description: "A structured, layered revision pass for a children's manuscript — story, structure, character, line, and form — done in the right order, delivering a prioritized fix queue rather than a line-by-line rewrite"
techniques:
  - ST-01
  - ST-02
  - CM-02
  - RT-05
  - QA-01
difficulty: intermediate
tags:
  - childrens-writing
  - revision
  - self-edit
  - structure
  - line-edit
updated: "2026-06-18"
related_prompts:
  - domain-childrens-writing/craft-tools/childrens_opening_pages_hook.md
  - domain-childrens-writing/craft-tools/childrens_age_reading_level_calibrator.md
  - domain-childrens-writing/fiction-workshops/childrens_middle_grade_fiction_workshop.md
---

**Purpose:** Run a structured, layered revision of a children's manuscript in the right order — big to small — so the writer doesn't polish sentences they'll later cut. It diagnoses across five layers (story, structure, character/voice, line, form-specific), then delivers a **prioritized fix queue** (highest-leverage first), not a line-by-line rewrite, so the writer fixes the load-bearing problems before the cosmetic ones.

**When to use:** When a draft is complete but not working and you don't know where to start; when you keep line-editing without solving the real problem; when you need a triage of what to fix first; before sending to beta readers or an agent.

**Don't use when:** You only need one targeted fix — the opening (use the opening pages tool), reading level (use the calibrator), dialogue (use the dialogue workshop), or a brand-new draft (use a workshop). This tool is the all-layers triage.

**Input needed:**
- The full draft (or a representative chapter for longer works)
- The form (picture book / early reader / chapter book / middle grade)
- The target age band
- What must NOT change (voice, beloved lines, intentional choices)

---

## Your Input

**Form:** [Picture book / early reader / chapter book / middle grade]
**Target age:** [e.g., ages 4-7, ages 8-12]
**Preserve:** [Voice features, lines you love, intentional structural choices]
**Draft:**
```
<draft>
[Paste the manuscript or a representative chapter]
</draft>
```

---

## Instructions

You are a children's book editor running a developmental-to-line revision in the correct order. Diagnose the `<draft>` layer by layer, **biggest problems first**, and deliver a prioritized fix queue — **do not line-edit before the story is right.** Protect the writer's voice at every layer: never flatten humor, rhythm, or personality to solve a problem; flag the trade-off instead. Work the layers, then deliver in the locked format.

### Step 1: Layer 1 — Story / Concept (do this first)

Is there one clear story? Don't touch a sentence until this holds.

- **One clear want + obstacle + change?** Name the protagonist's want, the obstacle, and how they change.
- **Child agency:** does the kid drive the plot and solve the climax? (If adults/luck do, that's the top fix.)
- **No preaching:** is the theme carried by action, or announced as a moral? Flag stated lessons to cut.

If Layer 1 is broken, most line edits are premature — say so.

### Step 2: Layer 2 — Structure / Pacing

- **Arc:** clear beginning/middle/end; rising stakes.
- **Sagging middle:** episodes that don't escalate; repetition without change.
- **Page-turns / chapter-ends:** does each spread or chapter end on a pull?
- **Length vs. form:** is it within the word range for its form (see Step 6)?

### Step 3: Layer 3 — Character / Voice

- **Agency** within scenes (choices, not just reactions).
- **Distinct voices:** could you tell who's speaking with the tags removed?
- **Authentic kid voice:** age-true dialogue and interiority (no adults-in-disguise).

### Step 4: Layer 4 — Line

Only now, the sentences:

- **Clarity** for the age; **concrete verbs and nouns** over abstractions and adverbs.
- **Cut filler** (just, very, really, started to, began to) and redundancy.
- **Read-aloud:** rhythm, repeated words, tongue-twisters — children's prose is heard.

### Step 5: Layer 5 — Form-Specific Checks

| Form | Check |
|------|-------|
| Picture book | Word count (often ≤500-700); page-turn beats; leaves room for the illustrator (don't describe what art will show); read-aloud rhythm |
| Early reader | Controlled vocabulary; short sentences; decodable; one idea per line |
| Chapter book | Chapter hooks; manageable chapter length; momentum over description |
| Middle grade | Subtext; voice consistency; theme via plot; subplot pulls its weight |

### Step 6: Prioritize the Fix Queue

Rank every issue by **leverage** — fixing a Layer 1 problem can dissolve a dozen Layer 4 ones. Order the queue highest-leverage first, and tell the writer where to stop before line-editing.

### Step 7: Verify

Confirm the queue respects the layer order (no line edits ranked above a broken story), and that no proposed fix flattens the voice.

---

## Output Format

```markdown
## Revision Triage — [Form, age]

## Layer 1: Story / Concept
- Want / obstacle / change: [stated]
- Child agency: [drives plot? solves climax?]
- Preaching check: [stated morals to cut, cited]
- Verdict: [solid / needs work — STOP line-editing if broken]

## Layer 2: Structure / Pacing
- Arc / sagging middle / page-turns / length: [notes, cited]

## Layer 3: Character / Voice
- Agency / distinct voices / kid-true voice: [notes, cited]

## Layer 4: Line
- Clarity / concrete verbs / filler / read-aloud: [cited examples]

## Layer 5: Form-Specific
- [Form checks + word count vs. range]

## Prioritized Fix Queue (highest leverage first)
1. [Layer X] [fix] — why it's first
2. ...
→ Stop here before line-editing: [marker]

## Voice/Trade-off Flags
[Any fix that would cost voice — writer decides]
```

---

## Example Output

**Form:** Chapter book, ages 7-9. **Preserve:** the narrator's deadpan; the recurring "Top Five" lists.

**Layer 1: Story / Concept**
- Want / obstacle / change: Wants to win the class pet; obstacle is one-winner rule; changes by choosing to give up her turn.
- Child agency: Mostly yes, BUT the climax currently resolves because the *teacher* changes the rule. Top fix.
- Preaching check: Last line states "And that's how I learned that winning isn't everything." Cut — show it.
- Verdict: Needs work at the climax. **Don't line-edit until the climax is the child's choice.**

**Layer 2: Structure / Pacing**
- Sagging middle: chapters 4-5 repeat the same scheme without escalating. Merge or escalate.
- Page-turns: chapter 3 ends on "then she went home" — flat. Needs a pull.

**Layer 3: Character / Voice**
- Distinct voices: Booker and the narrator sound identical in chapter 6. Differentiate.

**Layer 4: Line**
- Filler: "she started to slowly walk" → "she trudged." Many "just"/"really" to cut.
- Read-aloud: "the prize-sized surprise surprised her" — unintended tongue-twister.

**Layer 5: Form-Specific**
- Word count ~9,200; on the high end for the form — the chapter 4-5 merge helps.

**Prioritized Fix Queue:**
1. [L1] Rewrite the climax so *she* solves it — highest leverage; changes the ending's meaning.
2. [L1] Cut the stated moral last line.
3. [L2] Escalate or merge chapters 4-5.
4. [L2] Add a pull to the chapter 3 ending.
5. [L3] Differentiate Booker's voice.
→ Stop here before line-editing.
6. [L4] Cut filler; fix the tongue-twister.

**Voice/Trade-off Flags:** None — the deadpan and "Top Five" lists stay; the climax fix actually gives the deadpan a better final beat.

---

## Quality Indicators

**A good revision pass:**
- [ ] Diagnoses biggest-to-smallest, story before sentences
- [ ] Flags broken agency or preaching as top-priority fixes
- [ ] Tells the writer where to STOP before line-editing
- [ ] Ranks fixes by leverage, not by order of appearance
- [ ] Includes form-specific checks and word count
- [ ] Protects voice; flags any fix that would cost it

**Common pitfalls:**

| Pitfall | Sign | Fix |
|---------|------|-----|
| Line-editing too early | Polishing prose in a broken story | Solve Layer 1 first |
| Flat triage | Every issue treated equally | Rank by leverage |
| Voice flattening | "Cleaner" but personality gone | Flag the trade-off; keep the voice |
| Ignoring form | MG rules on a picture book | Apply form-specific checks |
| Missing the moral | Stated lesson left in | Flag and cut; show via action |

---

## False-Positive Prevention

**DON'T:**
- Start with sentence polish when the story or agency is broken.
- Treat all problems as equal — leverage is the whole point.
- "Clean up" prose in a way that erases humor or rhythm; flag trade-offs.
- Apply one form's rules to another (word counts and beats differ).
- Leave a stated moral in because it's "the point" — show it instead.

**DO:**
- Work the layers top-down: story → structure → character → line → form.
- Stop and say so when Layer 1 is broken.
- Deliver a prioritized fix queue with a stop-here marker.
- Check word count against the form's range.
- Protect the writer's voice at every layer.

## Related Prompts

- [childrens_opening_pages_hook.md](childrens_opening_pages_hook.md) — Targeted fix for the opening once the story holds
- [childrens_age_reading_level_calibrator.md](childrens_age_reading_level_calibrator.md) — Tune reading level after the line layer
- [childrens_middle_grade_fiction_workshop.md](../fiction-workshops/childrens_middle_grade_fiction_workshop.md) — Rebuild structure or arc if Layer 1/2 needs major work
