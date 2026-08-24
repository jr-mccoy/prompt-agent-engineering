---
title: "Software Engineering Prompt Review (2026-04-04)"
category: domain-software-engineering
description: "Archived 2026-04-04 review of the software-engineering prompt library focused on agentic coding execution-contract consistency."
techniques:
  - ST-03
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - review
  - audit-report
  - reference
updated: "2026-04-04"
related_prompts: []
artifact_type: "reference"
---

# Software Engineering Prompt Review (AI Coding Agent Focus)

**Date:** 2026-04-04  
**Scope:** `domain-software-engineering/**` prompt library  
**Assumption:** Prompts are used directly with coding agents (e.g., Codex/ChatGPT/Claude Code), not as installed skills.

## Executive Summary

The software-engineering prompt set is broad and generally well-structured. The main gap is not topical coverage; it is **execution-contract consistency** for agentic coding sessions.

In practical terms, many prompts explain *what* to analyze, but fewer enforce *how* an agent should:
- bound repository scope,
- provide evidence for claims,
- run verifiable checks,
- and report residual risk.

## What Works Well

1. **Strong domain decomposition** (analysis, testing, devops, cloud, api, mobile).
2. **Good workflow orientation** in guide files.
3. **Actionable checklists** in many prompts (especially testing and API workflow materials).

## Key Gaps for AI Coding Agents

1. **Missing explicit output contracts**
   - Some prompts do not require file/line citations, command evidence, or diff summaries.
2. **Insufficient safety guardrails in infra-related prompts**
   - Dry-run-first and rollback requirements are not consistently mandatory.
3. **Inconsistent migration-risk framing**
   - API prompts discuss versioning but do not always force breaking-change impact tables.
4. **Scope creep risk**
   - Prompts often omit strict path boundaries, which can trigger broad edits by agents.

## Recommended Baseline Clause Set

Prepend this baseline to software-engineering prompts used by coding agents:

1. **Scope Clause:** Work only in specified paths.
2. **Evidence Clause:** Cite exact files/lines or command output for every major claim.
3. **Change Clause:** Prefer smallest safe patch set; list non-goals.
4. **Validation Clause:** Run exact verification commands and report output.
5. **Risk Clause:** Document assumptions, uncertainty, and rollback strategy.

## Changes Applied in This Review

To operationalize the review, the following docs were updated:

- `domain-software-engineering/README.md`
  - Added agent-usage notes and a prompt-hardening pattern.
- `domain-software-engineering/testing/testing_workflow_guide.md`
  - Added prompt-only agent wrapper and bounded execution guidance.
- `domain-software-engineering/devops/devops_workflow_guide.md`
  - Added execution guardrails with dry-run and rollback emphasis.
- `domain-software-engineering/api/api_design_workflow_guide.md`
  - Added production-safe API change and migration validation addendum.

## Next Suggested Follow-Up

1. Add a shared `agent_output_contract.md` and reference it from all subdomain READMEs.
2. Add a lightweight lint/check script that flags prompts missing:
   - verification command section,
   - risk section,
   - explicit scope instruction.
3. Standardize severity schema across analysis/testing/devops prompts.

