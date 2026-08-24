---
title: "Build a Persistent Rule Set for the System Prompt"
category: prompt-engineering/system-prompts
description: "Codify the rules that should hold across every turn of every session into a stable, ranked, conflict-free block."
techniques:
  - CM-02
  - ST-02
difficulty: advanced
tags:
  - system-prompt
  - rules
  - persistence
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/escape-median/escapemedian_correction_compounder.md
---

## Objective

Distill recurring corrections, brand constraints, and load-bearing behaviors into a stable rule set placed in the system prompt that survives every turn and every user.

## When to Use

- Recurring corrections suggest rules belong upstream
- A team is operationalizing a brand or compliance standard
- A new system prompt needs its first ranked rule block

## Inputs

1. Sources of rules: corrections from past sessions, brand book, compliance docs, taste rules
2. Authority hierarchy (legal > brand > taste)
3. Maximum rule count (target 7–15)

## Constraints

**Must:**
- Rank rules by precedence (numbered 1..N)
- Each rule is testable from output alone
- Each rule has a one-line rationale linking it to its source
- Drop rules that are redundant with earlier-ranked rules

**Must Not:**
- Exceed the cap; if cap reached, escalate to a layered architecture
- Phrase rules as preferences ("try to") — they are rules
- Mix per-deployment defaults with universal rules (those go in developer prompt)

## Instructions

1. Aggregate candidate rules from each source.
2. Deduplicate.
3. Resolve conflicts by authority.
4. Rank by precedence.
5. For each rule, write the one-line test.
6. Verify against a held-out correction set.

## Output Format

```
PERSISTENT RULE SET (system-prompt block)

Rules apply in the order shown. Lower-numbered rules override higher-numbered.

1. <rule>
   test: <how to verify from output>
   source: <correction-id | brand:section | legal:reg>

2. <rule>
   ...

CONFLICTS RESOLVED
  - <r-x> vs <r-y>: kept <x> (authority: <reason>)

DROPPED
  - <candidate>: <reason>

VERIFY-AGAINST SET (held out)
  - correction <id>: <which rule catches it>
```

## Verification

- Number of rules within cap
- Every rule has test and source
- No rule is overridden by a higher-numbered rule (ranking is consistent)
- Held-out corrections are caught by the rule set
