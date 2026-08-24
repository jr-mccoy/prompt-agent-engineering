---
title: "Intent Taxonomy Design"
category: voice-conversational-ui/dialog-architecture
description: "Create a comprehensive intent taxonomy for a conversational domain including hierarchical organization, intent-entity relationships, disambiguation rules, and coverage validation"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - OC-03
  - QA-02
difficulty: intermediate
tags:
  - intent-taxonomy
  - intent-classification
  - entity-mapping
  - disambiguation
  - nlu-design
  - conversation-architecture
updated: "2026-03-19"
---

# Intent Taxonomy Design

**Objective:** Create a comprehensive intent taxonomy for a conversational domain, producing a hierarchical intent organization with entity relationships, disambiguation rules, and coverage validation against expected user scenarios.

**When to Use:**
- Use when: Starting a new conversational AI project and need to define intents
- Use when: An existing bot has too many (or too few) intents causing confusion
- Use when: Migrating from one NLU platform to another
- Use when: Consolidating multiple bots into a unified intent space
- Don't use when: Generating training utterances (use `nlu_training_data_generation.md`)

## Instructions

1. **Gather Input Data**
   - Collect user queries from logs, support tickets, search queries, or focus groups
   - Sample at least 200-500 real user utterances
   - Identify the domain(s) the bot must cover
   - Document known user goals and tasks

2. **Cluster Utterances into Intent Groups**
   - Group similar utterances by user goal (what they want to accomplish)
   - Separate utterances by action type: informational, transactional, navigational
   - Identify outliers: utterances that don't fit any group (potential new intents or out-of-scope)
   - Target 15-50 intents for most applications (more = fragmentation, fewer = ambiguity)

3. **Design Hierarchical Organization**
   - **Domain level**: Top-level grouping (Orders, Account, Products, Support)
   - **Intent level**: Specific user goals within a domain
   - **Sub-intent level** (if needed): Variations requiring different handling
   - Create a tree structure showing the hierarchy
   - Ensure each leaf intent maps to a distinct system response or action

4. **Map Intent-Entity Relationships**
   For each intent, define:
   - Required entities: Must be present to fulfill the intent
   - Optional entities: Refine the response but aren't mandatory
   - Entity types: Built-in (date, number, location) vs custom
   - Entity inheritance: Entities shared across related intents
   - Cross-intent entities: Same entity used differently by different intents

5. **Define Disambiguation Rules**
   For each pair of potentially confusing intents:
   - What utterances could match both?
   - What distinguishing features separate them?
   - Disambiguation question: "Did you mean X or Y?"
   - Default behavior when disambiguation fails
   - Confidence threshold for requiring disambiguation

6. **Validate Coverage**
   - Map each original user utterance to an intent
   - Calculate coverage: % of utterances assigned to an intent
   - Identify uncovered scenarios (out-of-scope candidates)
   - Test intent boundaries with borderline utterances
   - Verify that 80% of expected user scenarios map to specific intents

7. **CRITICAL: Check for common taxonomy problems**
   - **Too granular**: Intents that could be one intent with entity differentiation
   - **Too broad**: Intents that handle very different user needs
   - **Overlapping**: Two intents that match the same utterances
   - **Missing**: User goals without a corresponding intent
   - **Dead**: Intents that never get triggered in practice
   - **Confidence**: High (data-driven), Medium (expert judgment), Low (guesswork)

## False-Positive Prevention (MUST follow)

- **DON'T** create separate intents for every entity variation (use one intent with entities)
- **DON'T** design intents based on system capabilities alone — design from user goals
- **DON'T** have more than 50 intents without hierarchical organization
- **DON'T** assume your taxonomy is complete — plan for regular review and updates
- **DO** base intent design on real user data, not imagination
- **DO** test with utterances from users unfamiliar with the system
- **DO** plan for intent evolution as user needs change

## Expected Output

```markdown
## Intent Taxonomy: [Domain Name]

### Taxonomy Overview
- **Total Intents:** [Count]
- **Domains:** [Count]
- **Coverage:** [X]% of sampled utterances
- **Average Intents per Domain:** [Count]

### Hierarchy

#### Domain: Orders
| Intent | Description | Required Entities | Optional Entities |
|--------|-------------|-------------------|-------------------|
| orders.check_status | Check order delivery status | order_id OR email | - |
| orders.cancel | Cancel an existing order | order_id | cancellation_reason |
| orders.modify | Change order details | order_id | item, quantity, address |
| orders.return | Initiate a return | order_id | item, return_reason |

#### Domain: Account
| Intent | Description | Required Entities | Optional Entities |
|--------|-------------|-------------------|-------------------|
| account.balance | Check account balance | - (auth required) | account_type |
| account.update_info | Update profile | field_name | new_value |

### Disambiguation Matrix
| Intent A | Intent B | Distinguishing Feature | Disambiguation Question |
|----------|----------|----------------------|------------------------|
| orders.cancel | orders.return | Cancel = before ship, Return = after | "Do you want to cancel before shipping or return a received item?" |
| account.balance | orders.check_status | balance = money, status = delivery | "Are you checking your account balance or an order status?" |

### Coverage Report
| Scenario Category | Utterance Count | Mapped Intent | Coverage |
|-------------------|----------------|---------------|----------|
| Order queries | 150 | orders.* | 95% |
| Account queries | 80 | account.* | 88% |
| Out-of-scope | 45 | fallback | N/A |

### Taxonomy Health Metrics
| Metric | Value | Status |
|--------|-------|--------|
| Total intents | [Count] | [OK / Too many / Too few] |
| Overlapping pairs | [Count] | [OK / Needs disambiguation] |
| Uncovered scenarios | [Count] | [OK / Needs new intents] |
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Intent taxonomy creation
- **ST-02 (Structured Sequential Instructions):** Data → cluster → hierarchy → entities → validate
- **RT-02 (Multi-Dimensional Analysis):** Coverage, disambiguation, entity mapping
- **OC-03 (Structured Output):** Hierarchical taxonomy with tables
- **QA-02 (Quality Indicators):** Coverage metrics and health checks

## Customization Guide

- **For Small Bots (<15 intents)**: Skip hierarchy, use flat taxonomy
- **For Enterprise Bots (50+ intents)**: Add domain-level routing, consider multi-model approach
- **For Multi-language**: Verify intent boundaries hold across languages
- **For Voice Assistants**: Account for ASR errors in utterance clustering
