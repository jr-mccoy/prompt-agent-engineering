---
title: "Map the Model's Default Position on a Topic"
category: prompt-engineering/escape-median
description: "Before asking a model for analysis, opinion, or recommendation on a topic, probe and map its default position — what it would say unprompted, which views it balances against each other, what it hedges on — so you can push it off the median toward the specific view you actually want."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - escape-median
  - default-output
  - position-mapping
  - personalization
  - prompt-design
updated: "2026-04-20"
related_prompts:
  - domain-prompt-engineering/escape-median/escapemedian_instruction_sharpener.md
  - domain-prompt-engineering/escape-median/escapemedian_correction_compounder.md
  - domain-prompt-engineering/escape-median/escapemedian_bootstrap_instruction_file.md
---

# Map the Model's Default Position on a Topic

**Objective:** Produce a short, written map of the model's default stance on a specific topic — what it tends to say, what views it balances against each other, what it hedges on, what it avoids — *before* you write the prompt that actually asks for analysis or recommendation. The map is then used to write a sharper prompt that pushes the model off its median toward your actual position, not the blended average of internet text.

**When to use:** You're about to ask the model for judgment on something that matters to you (a career decision, a technical tradeoff, a strategic choice), and you don't want the "balanced and reasonable" answer that averages over the training data. You want a recommendation grounded in *your* priorities, not the median user's.

**Audience:** Individual users — knowledge workers, developers, founders, researchers — who are moving past generic AI output and want responses that reflect their specific situation rather than the median case.

---

## Inputs Required

1. **The topic.** As specific as possible. Not "career advice" but "should I leave a senior IC role for a management track at the same company."
2. **The model and context** you'll eventually ask the real question in (same chat, new chat, same CLAUDE.md, etc.).
3. **Your hypothesis about the default**, if you have one. Optional — it surfaces bias early. If you don't have one, say so.
4. **The specific decision or output you'll ask for later.** The map is only useful if it's mapped against a target.

Refuse to run this as a free-standing "tell me what the model thinks about X." Mapping without a target becomes entertainment. The point is to set up a sharper second prompt.

---

## Instructions

### Step 1 — Probe the unprompted default

Ask the model the most open version of the question, with no framing:

> "What's your general view on [topic]?"

Save the answer verbatim. Do not react to it yet.

### Step 2 — Probe the balanced view

Ask:

> "What are the strongest arguments on each side of [topic]? List at least three per side."

Save the answer. Observe which side it leads with, how evenly it weights them, and which arguments it treats as throwaway.

### Step 3 — Probe the hedge

Ask:

> "If you had to recommend a single choice on [topic] with limited information, what would you recommend and why?"

Save the answer. This is the *effective* median position — the one the model defaults to when forced to pick. Notice how much the recommendation depends on the caveats it adds.

### Step 4 — Probe the avoided view

Ask:

> "What's a defensible position on [topic] that most thoughtful people disagree with, and what's the best version of the case for it?"

Save the answer. This surfaces views the model knows exist but would not produce unprompted.

### Step 5 — Assemble the map

From the four answers, write up (in the user's own words, not the model's):

- **Default opening view** — what the model leads with.
- **Balanced views** — the set of positions it treats as legitimate.
- **Effective median** — the recommendation it actually gives when forced.
- **Under-weighted views** — defensible views that exist in its training but lose out in balancing.
- **Hedge language it reaches for** — specific phrases ("it depends," "both have merit," "consider your...") that signal it's refusing to commit.

### Step 6 — Locate yourself on the map

Before writing the next prompt, the user answers:
- Which of the balanced views is closest to theirs, and why.
- Whether their position is one of the under-weighted views the model wouldn't produce unprompted.
- Which hedge language they want the next prompt to explicitly suppress.

Without this step, the map is just a survey. Step 6 is what makes it actionable.

### Step 7 — Prescribe the sharpening

State, in one or two sentences, what the next prompt needs to do to move the model off the median toward the user's position. Typical moves:
- Name the default view and tell the model not to default to it.
- Pre-commit to the user's prior (e.g., "I'm already convinced of X; I want the strongest case against my plan, not a balanced overview").
- Name the hedge phrases the model should avoid.
- Ask for a ranked recommendation, not an overview.

Hand the sharpening off to `escapemedian_instruction_sharpener.md` if the user wants a full rewrite, or apply it directly if the next prompt is simple.

---

## Constraints

### Must
- Probe with at least the four question types in Steps 1–4. Fewer probes produce a partial map.
- Save each probe response verbatim before synthesizing. Synthesizing from memory produces a blurred map.
- Name the hedge phrases specifically. Vague hedges ("it hedges a lot") can't be suppressed.
- End with an actionable prescription for the next prompt.

### Must Not
- Argue with the model's default in the probe turns. The probes are diagnostic, not persuasive.
- Treat the map as evidence about what's *true* on the topic. It's evidence about what the *model* says, not what's correct.
- Apply the map across topics. Defaults are topic-specific; "the model's default stance" in general is not a useful object.
- Skip Step 6 (locate yourself). Mapping without locating is performative.

---

## False-Positive Prevention

1. **The model's default is not the correct answer, and not the wrong answer.** It's the median of training data. Mapping it doesn't tell you what to believe — it tells you what to argue against in your next prompt.
2. **The hedge is often the signal.** If the model reaches hard for "it depends" on a topic, that's data — it probably means the training data genuinely disagrees, *or* that the topic is treated as sensitive. The two are different and warrant different responses.
3. **Probes contaminate each other within one session.** If you run all four probes in the same chat, the model's later answers are influenced by its earlier ones. For cleaner maps, run the probes in separate sessions.
4. **Persona and system prompt affect the default.** If you have a heavy CLAUDE.md or custom instructions active, you're mapping the default *as filtered by them*, not the base model's default. Note this in the map.
5. **Don't generalize one topic's map to a whole domain.** "The model is biased toward X on Y" is usually too specific. "The model is biased toward X on everything in Y's domain" usually isn't supported.
6. **If Step 6 returns "my position is the model's effective median,"** you don't need to escape the median on this topic. Stop — use the model's output as-is.
7. **The map has a shelf life.** Model updates change defaults. Re-map after any version change on a topic that matters.

---

## Output Format

```markdown
## Topic
[Specific topic statement.]

## Target prompt (next step)
[What you're going to ask the model to do with this topic.]

## Default map

### Unprompted default
[Verbatim summary of what the model leads with.]

### Balanced views the model acknowledges
- [View A] — weight: [heavy / medium / light].
- [View B] — weight: [...].
- [View C] — weight: [...].

### Effective median (what it recommends when forced to pick)
[One sentence.]

### Under-weighted but defensible views
- [...] — why the model likely under-weights it: [...].

### Hedge language to watch for
- "[phrase]"
- "[phrase]"

## Self-location
- Closest to: [view].
- Distance from effective median: [near / moderate / far / opposed].
- Is user's view in the under-weighted set? [yes/no, and why].

## Prescription for the sharpened prompt
[One or two sentences on what the next prompt must do to move the model off the median toward the user's position. Specific overrides; specific hedges to forbid.]
```

---

## Verification

- [ ] All four probe types were run (unprompted, balanced, hedge, avoided).
- [ ] Probe responses were captured verbatim before synthesis.
- [ ] Hedge phrases are quoted specifically.
- [ ] The user has located themselves on the map (Step 6).
- [ ] The prescription for the next prompt is actionable (names a default to override and hedges to forbid).
- [ ] The map is scoped to one topic, not generalized.
