---
title: "NLU Intent and Entity Schema Design"
category: voice-conversational-ui/nlu-training
description: "Design the intent and entity schema for an NLU model including granularity decisions, entity types, overlap analysis, boundary case mapping, and schema evolution planning"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - QA-02
difficulty: intermediate
tags:
  - nlu-schema
  - intent-design
  - entity-design
  - schema-evolution
  - nlu-architecture
  - classification
updated: "2026-03-19"
---

# NLU Intent and Entity Schema Design

**Objective:** Design the intent and entity schema for an NLU model, producing specifications for intent granularity decisions, entity type definitions (system, custom, composite), overlap analysis, boundary case mapping, and schema evolution planning.

**When to Use:**
- Use when: Starting a new NLU project and need to define the schema
- Use when: Existing model has poor accuracy due to schema problems
- Use when: Merging multiple NLU models into one unified schema
- Use when: Planning schema evolution for a growing conversational AI
- Don't use when: Generating training utterances (use `nlu_training_data_generation.md`)

## Instructions

1. **Gather Domain Requirements**
   - Document all user tasks and queries the NLU must handle
   - Collect sample utterances from real users (200+ minimum)
   - Identify domain constraints and vocabulary
   - Determine NLU platform capabilities and limitations

2. **Design Intent Granularity**
   Apply the "action test": Can each intent trigger a distinct system response?
   - **Too coarse**: One intent maps to multiple different system actions
   - **Too fine**: Multiple intents all trigger the same system response
   - **Just right**: Each intent → one clear system behavior
   Rules of thumb:
   - Start with 15-30 intents for most applications
   - If two "intents" differ only by an entity value, merge into one intent with an entity
   - If one "intent" requires different handling paths, consider splitting

3. **Define Entity Types**
   For each entity:
   - **System entities**: Leverage built-in types (date, number, email, phone, location)
   - **Custom enum entities**: Finite set of values with synonyms
   - **Custom regex entities**: Pattern-based (order numbers, codes)
   - **Free-form entities**: Open text capture (names, descriptions)
   - **Composite entities**: Combined entities (city + date = trip_segment)
   - **Role-based entities**: Same type, different role (departure_city vs arrival_city)

4. **Map Entity-Intent Relationships**
   - Which entities are relevant for which intents?
   - Required vs optional entities per intent
   - How entity presence changes intent disambiguation
   - Shared entities across intents (e.g., "date" used by booking, cancellation, status check)

5. **Analyze Overlap and Boundaries**
   - **Intent overlap**: Which intents are commonly confused?
   - **Entity boundary ambiguity**: Where do entity annotations become unclear?
   - **Implicit vs explicit**: When is intent implied by entity combination?
   - Create a confusion matrix prediction for likely problem areas
   - Design disambiguation strategies for each overlap

6. **Plan Schema Evolution**
   - How will new intents be added without breaking existing ones?
   - Versioning strategy for the schema
   - Deprecation plan for removed intents
   - Entity type extension (adding values to enum entities)
   - Monitoring: Tracking unmatched utterances to discover needed intents
   - Regular review cadence (monthly analysis of fallback utterances)

7. **CRITICAL: Validate the schema**
   - Map 100+ real utterances to the schema — do they all fit?
   - Check for the "orphan utterance" problem (real utterances with no matching intent)
   - Verify that entity types cover expected value ranges
   - Test boundary utterances (those that could match multiple intents)
   - Ensure the schema is platform-compatible
   - **Confidence**: High (data-validated), Medium (expert-designed), Low (estimated)

## False-Positive Prevention (MUST follow)

- **DON'T** create an intent for every possible user request (causes fragmentation)
- **DON'T** use custom entities when system entities exist (date, number, email)
- **DON'T** design entities that overlap in value space without role differentiation
- **DON'T** finalize schema without testing against real utterances
- **DO** prefer fewer, well-defined intents over many narrow ones
- **DO** test entity extraction with edge-case values
- **DO** plan for schema evolution from day one

## Expected Output

```markdown
## NLU Schema Design: [Application Name]

### Schema Overview
| Metric | Value |
|--------|-------|
| Total intents | [Count] |
| System entities | [Count] |
| Custom entities | [Count] |
| Composite entities | [Count] |
| Platform | [Rasa / Dialogflow / Alexa / Custom] |

### Intent Schema
| Intent | Description | Required Entities | Optional Entities |
|--------|-------------|-------------------|-------------------|
| book_flight | Book a new flight | destination, date | passengers, class |
| check_status | Check order/flight status | reference_id | - |
| cancel | Cancel an existing booking | reference_id | reason |

### Entity Schema
| Entity | Type | Examples | Notes |
|--------|------|---------|-------|
| destination | system:location | Paris, NYC, Tokyo | Built-in geo entity |
| date | system:date | tomorrow, next Friday, March 15 | Built-in temporal |
| passengers | system:number | 1, 2, three | Range: 1-9 |
| class | custom:enum | economy, business, first | + synonyms |
| reference_id | custom:regex | ^[A-Z]{2}\\d{4}$ | Order/booking number |

### Overlap Analysis
| Intent A | Intent B | Overlap Risk | Distinguishing Feature |
|----------|----------|-------------|----------------------|
| book_flight | check_price | High | "book" vs "how much" / "cost" |
| cancel | modify | Medium | "cancel" vs "change" |

### Schema Evolution Plan
| Phase | Changes | Timeline |
|-------|---------|----------|
| v1.0 | Core 15 intents | Launch |
| v1.1 | Add loyalty/rewards intents | Month 2 |
| v1.2 | Multi-language entities | Month 4 |
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** NLU schema design
- **ST-02 (Structured Sequential Instructions):** Requirements → granularity → entities → relationships → validation
- **RT-02 (Multi-Dimensional Analysis):** Intents, entities, overlaps, evolution
- **CM-01 (Explicit Context Framing):** Platform constraints
- **QA-02 (Quality Indicators):** Coverage and overlap metrics

## Customization Guide

- **For Multi-Language**: Define language-specific entity handling, shared vs separate schemas
- **For Voice**: Account for ASR errors in entity extraction, phonetic similarity
- **For LLM-Based NLU**: Design as function schemas rather than traditional intent/entity
- **For Hybrid Systems**: Define which intents use traditional NLU vs LLM routing
