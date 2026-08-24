---
title: "Summarize a Focus Block for an Async Update"
category: productivity/deep-work
description: "Turn the end of a focus block into a short async update aimed at a specific collaborator — decision needed, artifact shared, question posed — so focus-block output becomes a teammate-readable signal rather than staying trapped in the user's head or artifact."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - OC-01
  - DS-01
  - QA-01
difficulty: beginner
tags:
  - deep-work
  - async
  - summary
  - communication
  - end-of-block
updated: "2026-04-20"
related_prompts:
  - domain-productivity/deep-work/deepwork_block_end_context_capture.md
  - domain-productivity/deep-work/deepwork_meeting_to_async_converter.md
  - domain-personal-development/prompts/agency/agency_end_of_session_review.md
---

# Summarize a Focus Block for an Async Update

**Objective:** Produce a short async update — not a reload packet for the user's future self, not full meeting minutes — aimed at one named collaborator or small group, that makes the block's output usable to them. Different audience, different format.

**When to use:** At the end of a block whose output another person needs to react to, review, or decide on. When the user would otherwise feel obliged to book a sync meeting to "walk someone through" the work. Paired with `deepwork_block_end_context_capture.md`, which addresses the user's own reload.

**Audience:** The individual writing to a specific collaborator — teammate, manager, client. Not an all-hands broadcast.

---

## Inputs Required

1. **What the block produced.** A draft, a decision, a prototype, a diagnosis, a finding.
2. **The recipient.** Name and role. If a small group, name them.
3. **What the recipient already knows** about this work. One sentence.
4. **What the recipient needs to do next.** React / review / decide / nothing (FYI).
5. **The deadline, if any.** When does the recipient need to act?
6. **The physical artifact.** Link, path, or "attached." Where the work lives.
7. **Anything genuinely uncertain.** Fragile assumption, missing data, unresolved sub-question.

---

## Instructions

1. **Match format to recipient action:**
   - **React** (informal, quick response needed) — chat-length, 3–5 sentences, link to artifact
   - **Review** (feedback expected) — short email-length, with specific review questions
   - **Decide** (a call needed) — short email-length, with the decision, the options, and a recommended path
   - **FYI** — one-sentence chat, link, no expectation

   Pick one. Do not hybridize.

2. **Lead with the ask, not the journey.** Structure: (a) what's needed from the recipient, (b) what the artifact is, (c) what's uncertain. Not: "This week I worked on..."

3. **Strip reload-packet content.** Fragile context, thinking-in-progress, project state for user's own use — all omitted. Those belong in `deepwork_block_end_context_capture.md`.

4. **Match formality to relationship.** Existing collaborator on a familiar project gets direct; external client or new stakeholder gets structured. Adjust based on input 2.

5. **Name uncertainty in one sentence, not five.** "One open question: whether the metric should apply to trial users — flagging for your call." Not a paragraph of context.

6. **End with deadline and decision mechanism if decision is needed.** "Decision by Friday — reply yes/no/ask me more."

7. **Do not editorialize.** No "I'm excited about this" or "please let me know if you have any concerns." Neutral, functional tone.

---

## Output Format

Output exactly one of four templates, chosen in step 1:

### React template
```
@[recipient] — [one-sentence ask]
[artifact link]
[one-sentence uncertainty, optional]
```

### Review template
```
Subject: [concise, artifact + ask]

[Recipient],

I need [specific ask: review / feedback on X and Y].

Artifact: [link or path]
Background (one line): [input 3]
Specific questions:
- [question 1]
- [question 2]

Open question / uncertainty: [one sentence, optional]

Deadline: [input 5]
```

### Decide template
```
Subject: Decision needed — [topic]

[Recipient],

Decision: [framed as a question]

Options:
1. [option + one-line implication]
2. [option + one-line implication]

Recommendation: [option], because [one sentence]

Artifact: [link]
Deadline: [input 5] — reply [yes/no/clarify] by then
```

### FYI template
```
@[recipient] — [one line] — [link]
```

---

## Constraints

**Must:**
- Choose exactly one format.
- Lead with the ask, not the work history.
- Name the deadline when the action is decide or review.
- Omit reload-packet content (that belongs in a different prompt).

**Must not:**
- Produce both an email and a chat version. Pick one.
- Add motivational language ("excited," "hope you like it," "no rush but...").
- Attach more than one artifact. If more exist, link them inside the artifact, not in the update.
- Explain the full block's work. Only what the recipient needs.

---

## False-Positive Prevention

- **Journey narration:** "This morning I dug into the problem and discovered..." — cut. The recipient's time is the object; your journey is not.
- **False options:** Listing three options when two are strawmen wastes the recipient's attention. Include only viable options.
- **Uncertainty burial:** Hiding uncertainty to look confident creates downstream rework. Name it in one sentence.
- **Wrong recipient action:** Asking for "thoughts" when you actually need a decision produces a conversation instead of movement. Force the action choice in step 1.
- **Polite padding:** "Hope this finds you well" adds zero information. Strip it. Brief can still be cordial via directness.

---

## Self-Verification (before finalizing)

- [ ] Exactly one format used.
- [ ] First line states the ask.
- [ ] Artifact link included.
- [ ] Deadline present when action is decide or review.
- [ ] No reload-packet content leaked in.
- [ ] No motivational or padding language.
- [ ] Uncertainty, if relevant, is one sentence.
