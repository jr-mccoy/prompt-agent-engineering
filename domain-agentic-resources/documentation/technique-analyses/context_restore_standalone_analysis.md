# Technique Analysis: context-restore (Standalone)

**Resource Type:** Command
**Path:** claude-code-resources/commands/orchestration/context-restore.md
**Date Analyzed:** 2025-12-22

---

## Executive Summary

The context-restore command is a sophisticated context rehydration system focused on **intelligent retrieval and reconstruction** of project context across multi-agent AI workflows. Unlike its companion context-save command, this focuses specifically on the challenges of:
- Semantic-aware context retrieval from vector databases
- Token-budget-constrained context loading
- Relevance-based prioritization
- Session state reconstruction
- Context merging and conflict resolution

**Complexity:** 5/5 (Advanced semantic search, multi-stage ranking, budget optimization)
**Novel Techniques:** 3 new techniques discovered
**Primary Use Case:** Resuming long-running projects with intelligent context selection

---

## Identified Techniques

### Technique 1: Semantic Vector Retrieval with Cosine Similarity
- **Category:** CM (Context Management) - Extension of existing + NEW
- **Pattern:** Using multi-dimensional embeddings and cosine similarity for context retrieval
- **Example from resource:**
```python
def semantic_context_retrieve(project_id, query_vector, top_k=5):
    """Semantically retrieve most relevant context vectors"""
    vector_db = VectorDatabase(project_id)
    matching_contexts = vector_db.search(
        query_vector,
        similarity_threshold=0.75,
        max_results=top_k
    )
    return rank_and_filter_contexts(matching_contexts)
```
- **Maps to existing:** Extends CM-04 (Summary-Expand Loop) with vector semantics
- **Effectiveness:** Retrieves semantically relevant context regardless of keyword matches

### Technique 2: Multi-Stage Relevance Scoring
- **Category:** CM (Context Management) + NEW
- **Pattern:** Composite relevance score combining semantic similarity, temporal decay, and historical impact
- **Example from resource:**
```python
def rank_context_components(contexts, current_state):
    """Rank context components based on multiple relevance signals"""
    for context in contexts:
        relevance_score = calculate_composite_score(
            semantic_similarity=context.semantic_score,
            temporal_relevance=context.age_factor,
            historical_impact=context.decision_weight
        )
```
- **Maps to existing:** NEW - multi-dimensional ranking algorithm
- **Effectiveness:** Prioritizes most valuable context, not just most recent or most similar

### Technique 3: Token-Budget-Constrained Progressive Loading
- **Category:** CM (Context Management) + NEW
- **Pattern:** Incremental context loading with real-time token counting and budget enforcement
- **Example from resource:**
```python
def rehydrate_context(project_context, token_budget=8192):
    """Intelligent context rehydration with token budget management"""
    prioritized_components = prioritize_components(context_components)
    current_tokens = 0
    for component in prioritized_components:
        component_tokens = estimate_tokens(component)
        if current_tokens + component_tokens <= token_budget:
            restored_context[component] = load_component(component)
            current_tokens += component_tokens
```
- **Maps to existing:** NEW - practical API constraint management
- **Effectiveness:** Maximizes context utility within hard token limits

### Technique 4: Component Prioritization Framework
- **Category:** CM (Context Management) + DS (Domain-Specific)
- **Pattern:** Pre-defined component hierarchy with domain-specific ordering
- **Example from resource:**
```python
context_components = [
    'project_overview',
    'architectural_decisions',
    'technology_stack',
    'recent_agent_work',
    'known_issues'
]
prioritized_components = prioritize_components(context_components)
```
- **Maps to existing:** Combines CM with DS-02 (Metric Specification) for priority definition
- **Effectiveness:** Ensures critical context (architecture, decisions) loads before supplementary details

### Technique 5: Three-Way Context Merging
- **Category:** CM (Context Management) + NEW
- **Pattern:** Merge strategies borrowed from version control for context conflict resolution
- **Example from resource:** "Implement three-way merge strategies, Detect and resolve semantic conflicts, Maintain provenance and decision traceability"
- **Maps to existing:** NEW - applying Git-like merge to AI context
- **Effectiveness:** Handles concurrent context updates from multiple agents safely

### Technique 6: Lazy Loading with Context Streaming
- **Category:** CM (Context Management) + IT (Interaction)
- **Pattern:** On-demand loading of context components as needed during workflow
- **Example from resource:** "Support lazy loading of context components, Implement context streaming for large projects, Enable dynamic context expansion"
- **Maps to existing:** IT techniques + NEW implementation for context
- **Effectiveness:** Reduces initial load time, enables infinite-scale context

### Technique 7: Cryptographic Context Validation
- **Category:** QA (Quality Assurance) + CM (Context Management) + NEW
- **Pattern:** Using cryptographic signatures to validate context integrity and detect tampering
- **Example from resource:** "Cryptographic context signatures, Semantic consistency verification, Version compatibility checks"
- **Maps to existing:** QA-01 (Chain-of-Verification) extended to context integrity
- **Effectiveness:** Ensures context hasn't been corrupted or maliciously modified

### Technique 8: Cross-Project Knowledge Transfer
- **Category:** DS (Domain-Specific) + CM (Context Management) + NEW
- **Pattern:** Extracting semantic vectors from one project and adapting them to another project's domain
- **Example from resource:**
```
Workflow 2: Cross-Project Knowledge Transfer
1. Extract semantic vectors from source project
2. Map and transfer relevant knowledge
3. Adapt context to target project's domain
4. Validate knowledge transferability
```
- **Maps to existing:** NEW - meta-learning across projects
- **Effectiveness:** Enables learning transfer, prevents reinventing solutions

### Technique 9: Adaptive Context Expansion
- **Category:** CM (Context Management) + IT (Interaction) + NEW
- **Pattern:** Dynamically expanding context based on workflow needs discovered during execution
- **Example from resource:** "Enable dynamic context expansion" in lazy loading section
- **Maps to existing:** NEW - reactive context management
- **Effectiveness:** Starts minimal, expands only when agent requests additional context

---

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: Composite Relevance Scoring for Context Retrieval
- **Description:** Multi-dimensional scoring algorithm combining semantic similarity, temporal decay, and historical impact to rank context components
- **Implementation:**
  - Semantic score: Cosine similarity of embeddings
  - Temporal relevance: Age-based decay function
  - Historical impact: Manually assigned or usage-derived weight
  - Final score: Weighted combination of all three
- **Use case:** Retrieving context for project resumption when full history exceeds token budget
- **Proposed category:** CM (Context Management)
- **Proposed code:** CM-10

**Why novel:** Existing techniques treat context as all-or-nothing or simple recency-based. This enables intelligent triage.

### Pattern 2: Cross-Project Knowledge Transfer via Vector Mapping
- **Description:** Extracting learned patterns from one project's context and adapting them to another project's domain through vector space mapping
- **Implementation:**
  - Extract high-impact context vectors from source project
  - Map source domain vocabulary to target domain
  - Validate transferability through semantic consistency checks
  - Inject adapted knowledge into target project context
- **Use case:** New projects in similar domains, organizational knowledge sharing
- **Proposed category:** DS (Domain-Specific) or CM (Context Management)
- **Proposed code:** DS-22 or CM-11

**Why novel:** Treats AI context as transferable knowledge asset, not project-specific state.

### Pattern 3: Dynamic Context Expansion with Lazy Loading
- **Description:** Starting with minimal context and progressively expanding based on runtime agent requests
- **Implementation:**
  - Load core context (project overview, current task)
  - Monitor agent requests for additional context
  - Fetch and inject requested components on-demand
  - Track expansion patterns to optimize future loads
- **Use case:** Large codebases where full context is impractical, exploratory workflows
- **Proposed category:** IT (Interaction Techniques) or CM (Context Management)
- **Proposed code:** IT-15 or CM-12

**Why novel:** Inverts traditional model (load everything upfront → load incrementally on demand).

---

## Multi-Technique Combinations

**Core Combination:** Semantic Retrieval + Relevance Scoring + Token-Budget Loading + Lazy Expansion

**Workflow:**
1. **Phase 1 (Boot):** Load minimal context (project overview, current objective) - ~1000 tokens
2. **Phase 2 (Retrieval):** Semantic vector search retrieves top-K relevant contexts
3. **Phase 3 (Ranking):** Multi-stage relevance scoring re-ranks by semantic + temporal + impact
4. **Phase 4 (Budget):** Progressive loading of ranked contexts until token budget exhausted
5. **Phase 5 (Expansion):** Lazy load additional components if agent requests them

**Synergies:**
- Semantic retrieval ensures relevant candidates
- Relevance scoring prioritizes within candidates
- Token budgets prevent API limit breaches
- Lazy expansion handles unpredictable needs

**Result:** Optimal context loading balancing relevance, budget, and flexibility.

---

## Comparison with context-save

**Key Differences:**

| Aspect | context-save | context-restore |
|--------|--------------|-----------------|
| **Primary concern** | Comprehensive capture | Intelligent retrieval |
| **Data flow** | Project → Storage | Storage → Agent |
| **Optimization goal** | Completeness, lossless | Relevance, budget-fit |
| **Key techniques** | Fingerprinting, Knowledge graphs, Multi-format serialization | Semantic search, Relevance ranking, Token budgets |
| **Complexity** | High (capture all nuance) | High (select optimal subset) |

**Complementary Nature:**
- context-save ensures rich, structured capture
- context-restore ensures intelligent, budget-aware retrieval
- Together: Complete context lifecycle management

---

## Integration Notes

**Add to MASTER_TECHNIQUE_INDEX:**
- **CM-10:** Composite Relevance Scoring for Context Retrieval
- **DS-22:** Cross-Project Knowledge Transfer via Vector Mapping (or CM-11)
- **IT-15:** Dynamic Context Expansion with Lazy Loading (or CM-12)

**Update Existing Techniques:**
- **CM-04:** Add reference to semantic-aware expansion (context-restore extends this)
- **QA-01:** Add context integrity validation as application

**Cross-reference with existing prompts:**
- Related to: `engineering/engineering_delivery_sprint_planner.md` (project resumption)
- Applies to: All multi-session workflows, long-running projects
- Complements: AG-06 (Memory & Learning Architecture)
- Extends: CM-04 (Summary-Expand Loop) with semantic awareness

**Integration with other commands:**
- **Paired with:** context-save (complete lifecycle)
- **Used by:** full-stack-feature (session resumption), issue (continuing investigation)
- **Enables:** multi-agent-optimize (historical performance data), improve-agent (prior optimization attempts)

**Best Practices:**
- Always define token budget explicitly (don't rely on defaults)
- Prioritize architectural decisions and technology stack over implementation details
- Use semantic search for large contexts (>10,000 tokens captured)
- Implement lazy expansion for exploratory workflows
- Validate context integrity with checksums/signatures
- Consider temporal decay (older decisions may be obsolete)

---

## Production Considerations

**Token Budget Selection:**
- Small tasks: 2,000-4,000 tokens (core context only)
- Medium tasks: 4,000-8,000 tokens (core + domain-specific)
- Large tasks: 8,000-16,000 tokens (comprehensive)
- Never exceed 50% of model's context window with restored context

**Performance Optimization:**
- Cache frequently-accessed context components
- Pre-compute embeddings during context-save (don't compute at restore time)
- Use approximate nearest neighbor (ANN) search for large vector databases
- Implement context component compression (gzip, brotli)

**Error Handling:**
- Graceful degradation if vector database unavailable (fall back to file system)
- Partial context restoration if budget exhausted mid-load
- Validate context version compatibility (schema evolution)
- Handle corrupted context (checksum failures, invalid JSON)

**Monitoring:**
- Track context retrieval latency (P50, P95, P99)
- Monitor token budget utilization (average vs. limit)
- Measure semantic relevance scores (how good are retrieval results?)
- Log context expansion requests (which components are requested lazily?)

---

## Analysis Metadata

**Analyzer:** Claude (Task 2.2 completion - command 7 of 7)
**Analysis Duration:** 25 minutes
**Confidence Level:** High
**Review Status:** Complete
**Priority for Integration:** Critical - Essential for production multi-session workflows

**Technique Complexity Score:** 5/5
- Advanced vector search and semantic ranking
- Multi-dimensional optimization (relevance + budget + freshness)
- Production-grade error handling and validation
- Cross-project knowledge transfer capabilities

**Novel Techniques Identified:** 3 high-value patterns
**Existing Techniques Extended:** 2 (CM-04, QA-01)
**Integration Readiness:** High - Clear use cases, well-defined patterns
