---
title: "System Prompt Versioning Protocol"
category: prompt-engineering/system-prompts
description: "Define how a system prompt is versioned, deployed, rolled back, and tracked so changes are auditable and reversible."
techniques:
  - QA-01
difficulty: intermediate
tags:
  - versioning
  - rollback
  - protocol
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/library-maintenance/library_prompt_changelog_writer.md
---

## Objective

Establish version, changelog, deployment gating, and rollback rules for a system prompt so any change can be traced, evaluated, and reverted.

## When to Use

- A system prompt is in production
- Multiple authors edit the same prompt
- A team needs to know exactly which version produced a given output

## Inputs

1. Current prompt
2. Owners
3. Deployment surface and how prompt is delivered (file, config, API)
4. Eval set used to gate changes

## Constraints

**Must:**
- Use semver (MAJOR.MINOR.PATCH)
- MAJOR for behavior changes that fail prior eval cases
- MINOR for additive behavior that does not regress eval cases
- PATCH for clarification, typo, formatting that does not change behavior
- Every version has a changelog entry
- Every deployment passes the eval set
- Every version has a documented rollback target

**Must Not:**
- Deploy without eval pass
- Edit a deployed version in place; bump version instead
- Lose a prior version (history is preserved)

## Instructions

1. Add `version` and `changelog` to frontmatter.
2. Decide MAJOR/MINOR/PATCH per change against the eval set.
3. Pre-deploy: run eval set; record results.
4. Deploy: tag version; record commit/hash.
5. Post-deploy: monitor for N hours/days per category.
6. Rollback: predefined target version + condition.

## Output Format

```
PROMPT FRONTMATTER
  version: 2.3.1
  owner: <name>
  changelog:
    - 2.3.1 (date): <patch description>
    - 2.3.0 (date): <minor>
    - 2.0.0 (date): <major - rationale>

EVAL GATE
  set: <ref>
  required pass rate: <x%>
  current pass rate: <y%>
  decision: gate-passed | gate-failed

DEPLOYMENT RECORD
  version: ...
  deployed_at: ...
  ref: <commit hash>
  by: <author>

ROLLBACK PLAN
  target_version: <prev>
  trigger: <condition>
  steps:
    1. revert config to <ref>
    2. run smoke set
    3. announce to <channel>

VERSIONING DECISIONS
  - change <id>: classification = <major|minor|patch>; reason
```

## Verification

- Version is semver
- Changelog covers every shipped version
- Eval gate is run pre-deploy
- Rollback target and trigger are predefined, not improvised
