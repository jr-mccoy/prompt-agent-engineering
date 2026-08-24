# Architecture — Children's Book Studio (design bundle)

## §0 Overview

A pipeline that converts a children's-writing idea into a finished, publishable manuscript + submission package. Seven sequential stages (0–6), routed by form and age band, with a dynamic revision loop at Stage 4 and four hard gates. Enforcement is by orchestrator critique. Implements the conventions of `domain-childrens-writing/` and references its 22 prompts rather than rebuilding them.

## §1 Scope

**Job to be done:** "Take my children's-book idea and give me a finished manuscript I can query."

**Success criteria (observable):**
- A complete manuscript inside the form's word-count band and target reading level.
- For nonfiction: every factual specific sourced or cut; back matter present.
- For across-difference work: a flags-and-questions audit (never a certification).
- A submission package with no fabricated comps/agents (all bracketed for author verification).

**Inputs and trust levels:**
- The author's idea, draft, and any research — *trusted* (the author's own content).
- Any external facts the nonfiction path needs — *untrusted until sourced* (must be verified, never supplied from memory).

**Autonomy:** the system *recommends and drafts*; the author owns and approves all files. It proposes edits as new versions; it does not silently overwrite.

**Blast radius (worst case):**
1. A nonfiction kids' book asserting fabricated facts as true (misinformation to children).
2. Over-certifying a write-across-difference portrayal as authentic/safe.
3. Age-inappropriate/mature content in a young-child product.
4. A publishing package with invented comps/agents misdirecting the author's market efforts.
5. Overwriting the author's own draft.

**Out of scope (non-goals):** mature-content YA (ages 14+ → `domain-creative-writing/`); teaching children (`domain-education-teaching/`); parenting one's own child (`domain-parenting/`); illustration *production* (the system writes art notes, not final art); certifying cultural authenticity; market research / verifying comps.

## §2 Justification (Gate 0)

<!-- GATE-0: JUSTIFIED -->
<!-- JUSTIFICATION-START -->
An agent is required because the stage sequence and the number of revision passes are input-dependent: different forms (board book, verse novel, STEM nonfiction) traverse different stages and craft passes, and the Stage-4 revision loop's tool selection, pass count, and stop condition are only knowable from what the diagnostic surfaces in the specific manuscript. A deterministic workflow cannot, because it would have to fix the route and the number of revision passes in advance, before the draft exists.
<!-- JUSTIFICATION-END -->

**Walking the complexity ladder:**
1. Deterministic function — no (creative generation).
2. Single model call — no (multi-stage: ideation → structure → draft → multi-pass revision → publishing prep).
3. Fixed code-controlled workflow — *nearly*, but two sources of runtime dynamism push past it:
   - **Form-conditioned routing:** different forms (board book, verse novel, STEM nonfiction) traverse different stage sequences and craft passes, chosen at runtime from the project's classification.
   - **Stage 4 revision loop:** which craft tools run, how many passes, and the stopping condition depend on what the diagnostic surfaces in *this* manuscript — step count/order/tool-selection are data-dependent.
4. → **Agent justified.** The justification is bounded: the spine is sequential; the agentic parts are the top-level routing and the Stage-4 evaluator-optimizer loop. No multi-agent escalation beyond three role-scoped agents.

## §3 Topology

- **TP-04 (routing / handoff)** at the top: the orchestrator classifies form/age/entry-stage and routes.
- **TP-03 (sequential chaining)** for the Stage 0→6 spine.
- **TP-07 (evaluator-optimizer)** inside Stage 4: diagnose → fix → re-check Gate A, looping to convergence.

**Primitives:**
- *Agents:* orchestrator (router/critic), manuscript-craft-reviewer (Stage 4 loop), nonfiction-accuracy-checker (Gate B nonfiction).
- *State:* the manuscript file (versioned) + the project spec/convention contract from Stage 0.
- *Memory:* none durable across projects (each run is one book).
- *Handoff:* orchestrator → stage prompt → domain prompt; results critiqued back at the gate.
- *Guardrail positions:* the four gate checkpoints (Stages 0, 4, 5, 6).
- *HITL location:* the author is in the loop at every gate (approves each stage's output); integrity gates are non-overridable.

## §4 Architecture (concrete)

**Agents** — see `agents/*.md` for full specs (authority Can-Do / Ask-First / Never).

**Tools** — see `tools/*.md`. The "tools" are minimal and read-mostly: read a domain prompt, read/write a manuscript file (write = save-new-version), estimate a reading level. No network, no money, no destructive operations beyond versioned file writes the author controls.

**Seams & validation:** the only untrusted-content seam is nonfiction external facts, validated by the source-plan / `VERIFY` discipline (Gate B). Representation content is validated by the flags-only audit constraint (never certified). Publishing content is validated by the anti-fabrication bracketing (Gate C).

**Context handling:** each stage receives the prior stage's gated artifact plus the project spec; the manuscript is the carried state. No compaction needed at this scale (single-book runs).

**Model right-sizing:** a single strong general model suffices for all stages; no per-agent model differentiation is required. Cost scales with manuscript length × revision passes, bounded by the Stage-4 convergence condition.
