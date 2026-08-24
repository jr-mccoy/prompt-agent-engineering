---
name: action_item_audit
description: "Run when project action lists need quality control before execution tracking."
version: "1.0.0"
category: business
tags: [action, audit, business, item]
agents_used: []
---
# Action Item Audit

## Trigger phrase
Run when project action lists need quality control before execution tracking.

## Required inputs
- Current action item backlog or meeting notes.
- Project milestones and dependencies.
- Definition of done and accountability standards.

## Output schema
- `audit_results`: action-by-action quality status (Clear/Needs Clarification/Invalid).
- `normalized_action_register`: rewritten action items with owner, due date, and success criteria.
- `execution_risks`: missing ownership, sequencing conflicts, and dependency blockers.

## Validation checklist
- [ ] Each action has a single accountable owner and due date.
- [ ] Actions are phrased as observable outcomes, not vague intentions.
- [ ] Dependencies and sequencing conflicts are explicitly captured.
- [ ] Invalid or duplicate actions are removed or merged with rationale.
