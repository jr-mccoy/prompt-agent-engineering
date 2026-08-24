# ARCHITECTURE — deep-research-fleet

**System:** deep-research-fleet · **Author/date:** factory sample, 2026-06-20 · **Status:** approved (sample)

## 1. Use case & scope
- **One-sentence use case:** Given a research question, return a synthesized answer where every claim cites a retrieved source.
- **Job-to-be-done:** Replace an afternoon of manual source-gathering with a sourced first draft a human can verify.
- **Success criteria (observable gates):**
  - [ ] Every claim maps to ≥1 retrieved source (no uncited assertions).
  - [ ] Sources are real and fetched this run (no fabricated citations).
  - [ ] Source disagreements are surfaced, not flattened.
  - [ ] The answer addresses the actual question.
- **Inputs:** a natural-language question (trusted); **web page content (UNTRUSTED).**
- **Outputs:** a cited markdown report + a source list.
- **Autonomy level:** acts (browses/fetches), recommends-only on conclusions.
- **Blast radius:** read-only web access. No writes, no money, no messaging.
- **Out of scope:** logins, form submission, auth'd content, real-time/streaming data.

## 2. Step-0 justification (the gate)

<!-- GATE-0: JUSTIFIED -->
<!-- JUSTIFICATION-START -->
An agent is required because the number and shape of research subtopics is input-dependent and only knowable after initial retrieval, requiring runtime decomposition and a runtime stop decision; a deterministic workflow cannot, because it would have to fix the subtopic set and source count in advance.
<!-- JUSTIFICATION-END -->

- **Rung chosen:** TP-06 orchestrator-workers.
- **Rejected lower rungs:** TP-05 parallel (fixed fan-out can't adapt subtopic count); TP-02 single agent (serial browsing too slow for breadth, bloats one context window).
- **Accepted cost:** ~15× tokens vs a chat turn — justified by genuinely breadth-first, parallelizable work.

## 3. Topology & primitives
- **Topology:** TP-06 orchestrator-workers (aliases: lead+subagents; LangGraph `Send`).
- **Selection variables:** control = model; structure = parallel; plan = built at runtime.
- **Primitives:** 1 orchestrator + N capped workers + 1 synthesizer; tools = read-only search + fetch; shared run-state persisted externally; per-worker isolated context returning condensed cited summaries; star-topology handoffs; per-agent + whole-run tracing; no runtime HITL (read-only).

## 4. Architecture
### 4.1 Component map
```
question → ORCHESTRATOR → spawn ≤ MAX_WORKERS workers (isolated context, read-only tools)
                        → workers return condensed CITED summaries → SYNTHESIZER → cited report
```
### 4.2 Seams
| Seam | From → To | Crosses | Validation |
|------|-----------|---------|------------|
| S1 | web → worker | untrusted page content | treated as data only (SAFE-01); never selects next tool |
| S2 | worker → orchestrator | condensed summary + citations | schema check: every claim has a source id |
| S3 | synthesizer → output | final report | citation-coverage guardrail (tripwire on uncited claims) |
### 4.3 Context / durability
Workers get fresh-instruction-only context; orchestrator keeps summaries, not raw pages; state persisted externally; run resumable from last completed worker.
### 4.4 Cost / model right-sizing
| Component | Model | Why |
|-----------|-------|-----|
| Orchestrator | strong | decomposition + stop decision |
| Workers | mid | read + summarize-with-citations |
| Synthesizer | strong | cross-source synthesis |

## 6. Gates summary
- Gate 0: done (§2) · Gate A: GATE_DESIGN.md · Gate B: EVAL_HARNESS.md · Gate C: DISCLOSURE_MANIFEST.md · Kill switch: `config.halt` checked before search/fetch.

## 8. Referenced existing prompts
`aiagent_multi_agent_orchestration`, `aiagent_context_engineering_at_scale`, `aiagent_prompt_injection_untrusted_content_defense`, `done_definition_*`.
