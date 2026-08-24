---
title: "Rasa Conversational AI Architecture"
category: voice-conversational-ui/platform-specific
description: "Architect Rasa-based conversational AI systems covering domain configuration, story and rule patterns, custom action architecture, NLU pipeline configuration, policy stack tuning, and deployment"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - QA-02
difficulty: advanced
tags:
  - rasa
  - rasa-pro
  - open-source
  - nlu-pipeline
  - stories
  - custom-actions
  - policy-stack
  - deployment
updated: "2026-03-19"
---

# Rasa Conversational AI Architecture

**Objective:** Architect a Rasa-based conversational AI system, producing specifications for domain.yml configuration, story and rule patterns, custom action architecture, NLU pipeline configuration, policy stack tuning, form handling, and deployment strategy.

**When to Use:**
- Use when: Building a conversational AI with Rasa (open-source or Pro)
- Use when: Reviewing an existing Rasa project's architecture
- Use when: Migrating from another NLU platform to Rasa
- Use when: Optimizing Rasa model performance (accuracy, speed)
- Don't use when: Using a managed platform (use Dialogflow or Alexa prompts)

## Instructions

1. **Design Domain Configuration (domain.yml)**
   - **Intents**: List all intents with used_entities configuration
   - **Entities**: Define entity types and roles
   - **Slots**: Type, influence_conversation flag, mappings
   - **Responses**: Utter templates with variations and channel-specific versions
   - **Actions**: Custom action registry
   - **Forms**: Form definitions with required slots and validation

2. **Create Story and Rule Patterns**
   - **Stories**: Multi-turn conversation training examples
     - Happy paths: Ideal conversation flows
     - Edge cases: What happens when things go wrong
     - Checkpoints: Reusable story segments
   - **Rules**: Deterministic behavior (always respond to X with Y)
     - Use rules for single-turn interactions (greetings, FAQ)
     - Use stories for multi-turn (complex dialog management)
   - **Best practice**: Rules for deterministic, stories for learned behavior

3. **Configure NLU Pipeline**
   Design the pipeline for your needs:
   ```yaml
   pipeline:
     - name: WhitespaceTokenizer      # or SpacyTokenizer for entities
     - name: RegexFeaturizer           # Pattern-based features
     - name: LexicalSyntacticFeaturizer
     - name: CountVectorsFeaturizer    # Bag of words
     - name: CountVectorsFeaturizer    # Character n-grams
       analyzer: char_wb
       min_ngram: 1
       max_ngram: 4
     - name: DIETClassifier            # Joint intent + entity
       epochs: 100
     - name: EntitySynonymMapper       # Normalize entity values
     - name: ResponseSelector          # For FAQ/chitchat
   ```
   Tune for: accuracy vs training time vs inference latency

4. **Design Custom Actions Architecture**
   - Action server setup (separate service)
   - Action organization: one file per domain or feature
   - External API integration patterns
   - Database access patterns
   - Slot setting from actions
   - Error handling in actions (tracker, dispatcher patterns)
   - Action validation (FormValidationAction)

5. **Tune Policy Stack**
   Configure the dialog management policies:
   ```yaml
   policies:
     - name: MemoizationPolicy         # Exact match on stories
       max_history: 5
     - name: RulePolicy                 # Deterministic rules
     - name: TEDPolicy                  # ML-based dialog
       max_history: 8
       epochs: 100
     - name: UnexpecTEDIntentPolicy     # Out-of-distribution detection
       max_history: 5
   ```
   Balance between: deterministic control (Rules) and learned flexibility (TED)

6. **Implement Form Handling**
   - Active forms: Multi-slot data collection
   - Slot validation: Custom validation logic per slot
   - Slot mapping: From entities, from text, from intent
   - Deactivation conditions: When to exit the form
   - Interruption handling: User asks off-topic during form fill

7. **Plan Deployment Architecture**
   - Rasa server: Model serving and dialog management
   - Action server: Custom action execution
   - Tracker store: Conversation state persistence (Redis, PostgreSQL)
   - Lock store: Distributed locking for concurrent conversations
   - Event broker: Async event streaming (Kafka, RabbitMQ)
   - Model storage: S3/GCS for model artifacts
   - Scaling: Horizontal scaling with load balancer

8. **CRITICAL: Validate the architecture**
   - Run `rasa test` for NLU and Core evaluation
   - Check story coverage with `rasa test --stories`
   - Verify custom actions handle all error cases
   - Test form interruption and resumption
   - Load test the action server
   - **Confidence**: High (cross-validated), Medium (dev tested), Low (designed only)

## False-Positive Prevention (MUST follow)

- **DON'T** use only rules (no dialog flexibility) or only stories (no determinism)
- **DON'T** set max_history too high (>10 hurts generalization)
- **DON'T** put complex business logic in domain.yml responses
- **DON'T** skip the UnexpecTEDIntentPolicy (it catches out-of-distribution inputs)
- **DO** use rules for single-turn patterns, stories for multi-turn
- **DO** validate forms with FormValidationAction
- **DO** version your trained models and support rollback

## Expected Output

```markdown
## Rasa Architecture: [Project Name]

### Domain Overview
| Component | Count | Notes |
|-----------|-------|-------|
| Intents | [Count] | [Groups] |
| Entities | [Count] | [Types] |
| Slots | [Count] | [Types] |
| Custom Actions | [Count] | [Categories] |
| Forms | [Count] | [Tasks] |
| Stories | [Count] | + [Count] rules |

### NLU Pipeline
| Component | Purpose | Key Config |
|-----------|---------|------------|
| [Tokenizer] | [Purpose] | [Config] |
| DIETClassifier | Intent + Entity | epochs: 100 |

### Policy Stack
| Policy | Priority | Purpose |
|--------|----------|---------|
| RulePolicy | 1 | Deterministic patterns |
| MemoizationPolicy | 2 | Exact story matches |
| TEDPolicy | 3 | Learned dialog management |

### Deployment Architecture
```
                    ┌─────────────────┐
                    │  Load Balancer   │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
        ┌─────┴─────┐ ┌─────┴─────┐ ┌─────┴─────┐
        │ Rasa Pod 1 │ │ Rasa Pod 2 │ │ Rasa Pod 3 │
        └─────┬─────┘ └─────┬─────┘ └─────┬─────┘
              │              │              │
        ┌─────┴──────────────┴──────────────┴─────┐
        │           Action Server (Pool)           │
        └─────────────────┬───────────────────────┘
                          │
              ┌───────────┼───────────┐
              │           │           │
        ┌─────┴─────┐ ┌──┴──┐ ┌─────┴─────┐
        │ Tracker DB │ │Redis│ │ Event Broker│
        │ (Postgres) │ │(Lock)│ │  (Kafka)  │
        └───────────┘ └─────┘ └───────────┘
```

### Model Performance
| Metric | NLU | Core | Target |
|--------|-----|------|--------|
| Accuracy | [X]% | [X]% | 90%+ |
| F1 | [X] | [X] | 0.90+ |
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Rasa architecture design
- **ST-02 (Structured Sequential Instructions):** Domain → stories → NLU → actions → policies → deployment
- **RT-02 (Multi-Dimensional Analysis):** NLU, dialog, actions, deployment dimensions
- **CM-01 (Explicit Context Framing):** Rasa-specific constraints and conventions
- **QA-02 (Quality Indicators):** Model evaluation metrics

## Customization Guide

- **For Rasa Pro**: Add CALM, enterprise analytics, Rasa Pro features
- **For Multi-Language**: Language-specific NLU pipelines, shared domain
- **For High-Volume**: Focus on scaling, caching, async actions
- **For On-Premise**: Air-gapped deployment, no cloud dependencies
