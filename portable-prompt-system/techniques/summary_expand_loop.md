# Summary-Expand Loop Template

**Source:** ADVANCED_PROMPTING_TECHNIQUES.md
**Category:** Context Window Management (Tier 5)

## Prompt

### Phase 1 (in current conversation at token limit):

```
Compress this entire conversation into a structured summary:

**Key Findings:** [3-4 detailed bullets capturing essential insights]

**Critical Details:** [Technical specifications, numbers, constraints that must be preserved]

**Open Questions:** [What still needs investigation or clarification]

**Context Required for Next Phase:** [Minimum information needed to continue analysis]

Make this summary self-contained - it will be used to continue analysis in a fresh conversation.
```

### Phase 2 (paste summary in new conversation):

```
Here is summary from deep analysis we conducted:

[PASTE SUMMARY FROM PHASE 1]

Using this context, now provide [YOUR EXPANDED REQUEST - e.g., "a comprehensive 2000-word recommendation that includes X, Y, Z"]

Expand with depth that wasn't possible in the previous conversation due to token constraints.
```

## Usage Notes

The summary forces distillation to semantic essentials, not conversational artifacts. You lose the exact wording but preserve the reasoning chain. Use this when you've burned through tokens in exploratory analysis and need comprehensive final output.
