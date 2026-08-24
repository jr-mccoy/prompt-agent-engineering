---
title: "Voice UX Best Practices Audit"
category: voice-conversational-ui/voice-ux
description: "Audit an existing voice or conversational interface against established VUI/CUI best practices evaluating discoverability, learnability, efficiency, error tolerance, and confirmation patterns"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - voice-ux
  - ux-audit
  - vui-best-practices
  - conversational-ux
  - heuristic-evaluation
  - usability
updated: "2026-03-19"
---

# Voice UX Best Practices Audit

**Objective:** Audit an existing voice or conversational interface against established VUI/CUI best practices, evaluating discoverability, learnability, efficiency, error tolerance, confirmation patterns, and progressive disclosure.

**When to Use:**
- Use when: Reviewing a voice app or chatbot before launch
- Use when: Users report confusion, frustration, or high abandonment rates
- Use when: Benchmarking a conversational interface against industry standards
- Use when: Onboarding to an existing voice project and need to assess quality
- Don't use when: Designing from scratch (use design-specific prompts first)

## Instructions

1. **Evaluate Discoverability**
   - Can users discover what the bot/assistant can do?
   - Is there an effective onboarding or welcome experience?
   - Are capabilities revealed progressively or dumped all at once?
   - Are suggestion chips, hint prompts, or "try saying" examples provided?
   - Can users ask "what can you do?" and get a useful response?

2. **Assess Learnability**
   - Can a first-time user complete the primary task without help?
   - Are interaction patterns consistent across different features?
   - Does the system teach users as they go (inline guidance)?
   - Are error messages educational (tell users what to do, not just what went wrong)?
   - Is the learning curve appropriate for the target audience?

3. **Measure Efficiency**
   - How many turns does the primary task take? (Benchmark: under 5 for simple tasks)
   - Can expert users take shortcuts (one-shot commands, "same as last time")?
   - Does the bot avoid asking for information it already has?
   - Are confirmations used judiciously (not on every turn)?
   - Is the response length appropriate? (voice: under 4 seconds; text: under 3 sentences)

4. **Test Error Tolerance**
   - How does the system handle unrecognized input?
   - Are error messages progressive (more helpful each attempt)?
   - Is there always an escape route (human, restart, different channel)?
   - Does error recovery preserve context and collected information?
   - Maximum retries before escalation: is it reasonable (2-3)?

5. **Review Confirmation Patterns**
   - Are high-stakes actions confirmed before execution?
   - Are low-stakes actions performed without unnecessary confirmation?
   - Is implicit confirmation used effectively? ("Your flight to Paris on Friday...")
   - Does explicit confirmation avoid yes/no fatigue?
   - Can users correct specific details without restarting?

6. **Check Progressive Disclosure**
   - Is information presented in digestible chunks?
   - Can users drill down for more detail on demand?
   - Are lists summarized first, with option to hear more?
   - Does the system avoid overwhelming users with options?

7. **Assess Conversational Quality**
   - Does the bot sound natural, not robotic?
   - Is personality consistent across all interactions?
   - Does the bot handle chitchat and social niceties appropriately?
   - Are transitions between topics smooth?
   - Does the bot acknowledge user emotions when appropriate?

8. **CRITICAL: Score and prioritize findings**
   - Rate each dimension on a 1-5 scale
   - Provide evidence (specific examples) for each score
   - Prioritize improvements by impact on user satisfaction
   - Distinguish quick fixes from architectural changes
   - **Confidence**: High (observed with real users), Medium (expert evaluation), Low (theoretical)

## False-Positive Prevention (MUST follow)

- **DON'T** penalize a focused bot for not handling off-topic requests
- **DON'T** require personality in utility-only interactions
- **DON'T** flag short responses as "too terse" in voice (brevity is a virtue)
- **DON'T** demand confirmation patterns for simple, reversible actions
- **DO** evaluate against the bot's stated purpose, not a universal ideal
- **DO** consider the target user's technical sophistication
- **DO** test with actual users or realistic scenarios, not just edge cases

## Expected Output

```markdown
## Voice UX Audit: [Application Name]

### Scorecard
| Dimension | Score (1-5) | Evidence | Priority |
|-----------|-------------|----------|----------|
| Discoverability | 3/5 | Welcome message exists but lists all 12 features | High |
| Learnability | 4/5 | Consistent patterns, good inline guidance | Low |
| Efficiency | 2/5 | Primary task takes 7 turns, could be 4 | High |
| Error Tolerance | 3/5 | Error messages helpful but no escalation path | Medium |
| Confirmation | 4/5 | Good implicit confirmation usage | Low |
| Progressive Disclosure | 2/5 | Lists read all 10 items in voice | High |
| Conversational Quality | 3/5 | Mostly natural but repetitive phrasing | Medium |
| **Overall** | **3.0/5** | | |

### Top Findings

#### Finding 1: [Title]
- **Dimension:** [Which dimension]
- **Severity:** High | Medium | Low
- **Evidence:** [Specific interaction example]
- **Recommendation:** [Concrete improvement]
- **Effort:** Low | Medium | High

### Quick Wins
1. [Low-effort, high-impact improvement]
2. [Another quick win]

### Architectural Changes Needed
1. [Larger change with rationale]
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Voice UX audit
- **ST-02 (Structured Sequential Instructions):** Dimension-by-dimension evaluation
- **RT-02 (Multi-Dimensional Analysis):** 7 UX dimensions
- **RT-05 (Evidence-Based Reasoning):** Requires examples for each score
- **DS-06 (Prioritization Guidance):** Impact-prioritized recommendations

## Customization Guide

- **For Voice-Only (Smart Speakers)**: Emphasize efficiency, progressive disclosure, brevity
- **For Chat-Only (Web/Mobile)**: Add visual element evaluation, rich message usage
- **For Multi-Modal**: Add screen-voice synchronization evaluation
- **For Enterprise Internal**: De-emphasize personality, emphasize efficiency and accuracy
