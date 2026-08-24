# ARCHITECTURE — marketing-copy-evaluator-optimizer

**System:** marketing-copy-evaluator-optimizer · **Author/date:** factory sample, 2026-06-20 · **Status:** approved (sample)

## 1. Use case & scope
- **One-sentence use case:** Given a product brief and brand rules, produce marketing copy that a separate critic scores against a fixed rubric, revising until it passes or a round cap is hit.
- **Job-to-be-done:** Replace several manual editor passes with an automated generate→critique→revise loop that stops on an explicit quality bar instead of a fixed number of edits.
- **Success criteria (observable gates):**
  - [ ] Final copy passes all three rubric dimensions (on-brand voice, factual-claims-substantiation, length/format) OR is flagged "did not converge" with the best-scoring draft returned.
  - [ ] No product claim ships unless it is supported by the supplied brief (no fabricated/unsubstantiated claims).
  - [ ] The number of revision rounds is decided at runtime by the critic, not fixed in advance.
  - [ ] The critic's verdict is a deterministic pass/fail per dimension, not free-form prose.
- **Inputs:** a product brief (trusted) + brand rules (trusted) + (optionally) user-supplied source text the copy may draw on (**treated as DATA, never as instructions**).
- **Outputs:** final marketing copy + the critic's per-dimension scorecard + a convergence flag.
- **Autonomy level:** acts (rewrites copy in-loop), recommends-only on the final draft (a human ships it).
- **Blast radius:** read-only by construction. No external tools, no writes, no network, no money, no messaging — both agents operate purely on in-context content.
- **Out of scope:** image generation, publishing/posting copy anywhere, fetching live facts, legal sign-off.

## 2. Step-0 justification (the gate)

<!-- GATE-0: JUSTIFIED -->
<!-- JUSTIFICATION-START -->
An agentic loop is required because the number of revision rounds is input-dependent and only knowable at runtime: a draft passes when an explicit rubric is satisfied, which may take one round or several, with a runtime stop decision (pass) and a cap-fallback (return best draft). A single model call cannot self-correct against an independent critic, and a deterministic workflow cannot, because it would have to fix the number of revision rounds in advance instead of letting the rubric verdict decide.
<!-- JUSTIFICATION-END -->

- **Rung chosen:** TP-07 evaluator-optimizer (generator + critic loop).
- **Rejected lower rungs:** TP-02 single agent (one shot can't iterate to a quality bar; self-grading is not independent); a deterministic workflow with N fixed edit passes (wastes rounds on easy briefs, under-edits hard ones; no runtime stop).
- **Accepted cost:** up to MAX_ROUNDS× the generation tokens plus one critic pass per round — justified because quality requires iterative self-correction against an explicit, independently-applied rubric.

## 3. Topology & primitives
- **Topology:** TP-07 evaluator-optimizer (aliases: generator+critic, actor+judge loop).
- **Selection variables:** control = model; structure = iterative loop with a bounded round count; plan = "revise until critic passes or cap."
- **Primitives:** 2 roles — a **generator agent** (writes/revises copy) and a **critic/evaluator agent** (scores against the fixed rubric, emits a deterministic pass/fail verdict + per-dimension feedback). NO external tools — both read only in-context content (brief + brand rules + current draft). Shared loop-state (current draft, round number, best-scoring draft so far) held by the loop driver. Per-round tracing.

## 4. Architecture
### 4.1 Component map
```
brief + brand rules → GENERATOR (round 1 draft)
   → CRITIC scores draft vs rubric → PASS?  ── yes ──▶ ship final copy + scorecard
                                       │
                                       no (and round < MAX_ROUNDS)
                                       ▼
                          GENERATOR revises using critic feedback ──▶ (loop)
   round == MAX_ROUNDS and still failing ──▶ return best-scoring draft + flag "did not converge"
```
### 4.2 Seams
| Seam | From → To | Crosses | Validation |
|------|-----------|---------|------------|
| S1 | brief/source text → generator | trusted brief vs untrusted user source text | source text passed as a `<document>` data block; never selects the next step or alters the rubric (SAFE-01) |
| S2 | critic → loop driver | per-dimension verdict | schema check: verdict is `{voice, claims, format} ∈ {pass, fail}` + feedback; loop continues only on a deterministic fail (SAFE-02) |
| S3 | generator → output | final copy | claims-substantiation guardrail: a final independent check that every product claim maps to the brief before shipping |
### 4.3 Context / durability
The loop driver holds: current draft, round counter, and the best-scoring draft seen so far. Each generator revision gets the brief + brand rules + the latest draft + the critic's last feedback; the critic gets the brief + brand rules + the draft only (no prior feedback, so each score is fresh). State is small and in-context; a crash mid-loop restarts from the brief (cheap; no external side effects exist).
### 4.4 Cost / model right-sizing
| Component | Model | Why |
|-----------|-------|-----|
| Generator | strong | creative rewriting against nuanced brand voice |
| Critic | strong | reliable, consistent rubric application is the quality anchor |

## 6. Gates summary
- Gate 0: done (§2) · Gate A: GATE_DESIGN.md · Gate B: EVAL_HARNESS.md · Gate C: DISCLOSURE_MANIFEST.md · Kill switch: `config.halt` checked before each round.

## 8. Referenced existing prompts
`aiagent_evaluation_design`, `aiagent_failure_mode_analysis`, `aiagent_prompt_injection_untrusted_content_defense`, `correctness_eval_design_prompt`, `done_definition_*`.
