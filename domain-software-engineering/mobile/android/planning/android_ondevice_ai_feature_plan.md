---
title: "Android On-Device AI Feature Plan"
category: mobile-development
description: "Plan an AI/ML feature for an Android app — framing the user job, deciding on-device versus cloud inference, selecting a runtime and model, and defining responsible-AI guardrails — before any ML code is written."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - AG-08
  - DS-26
  - NE-02
difficulty: advanced
tags:
  - android
  - mobile-development
  - ai
  - on-device-ml
  - gemini-nano
  - litert
  - responsible-ai
updated: "2026-06-06"
related_prompts:
  - android_app_concept_validation.md
  - android_mobile_threat_model.md
  - android_privacy_by_design_and_permissions_plan.md
---

# Android On-Device AI Feature Plan

**Objective:** Produce a complete, decision-ready plan for an AI/ML feature in an Android app — framing the user's job-to-be-done and whether AI is even the right tool, scoring on-device versus cloud inference against latency/privacy/cost/capability, selecting a concrete runtime and model with a capability-detection and tiered-fallback strategy, sizing the model-delivery and storage budget, defining the latency/UX/thermal budget, and locking responsible-AI guardrails (data flow, consent, content safety, eval harness, Play policy) — all before a single line of ML code is written.

**When to Use:** Use this prompt once a feature has been validated and scoped, and you are about to add an AI/ML capability (text generation, summarization, classification, image understanding, speech, recommendations, smart replies). Use it whenever the answer to "should this run on the device or in the cloud?" is non-obvious, when the data involved is sensitive, or when an LLM/generative component creates content-safety, hallucination, or abuse exposure. Do not use it for non-AI features or for ML implementation details (that comes after this plan).

**Sequence Map:** Use after concept validation and feature scoping (`android_app_concept_validation.md`, `android_feature_specification.md`); use before ML implementation, model integration, or any inference code. Coordinate in parallel with the threat model and privacy plan — the data-flow decisions here are inputs to both.

**Important context:** "On-device AI" on Android in 2026 spans three tiers: (1) **system-provided generative models** — Gemini Nano accessed through **AICore** and the **ML Kit GenAI APIs** (summarization, proofreading, rewrite, image description), available only on supported devices and gated by AICore feature availability; (2) **task-specific ML Kit APIs** (barcode, text recognition, face/pose detection, language ID, translation, smart reply) and **custom models via LiteRT** (the runtime formerly called TensorFlow Lite) with hardware acceleration through GPU/NNAPI-successor/NPU delegates and on-demand model delivery via **Play for on-device AI**; and (3) **cloud LLM/API inference** for capabilities that exceed what fits or runs acceptably on a phone. The plan's job is to route each capability to the right tier, never to assume one tier. The biggest failure mode is assuming Gemini Nano (or any on-device model) is universally available — it is not, so capability detection and graceful fallback are mandatory, not optional.

---

## Context Gathering

Before producing the plan, gather the following. Ask only the questions whose answers you do not already have.

1. **The AI Job-to-Be-Done:**
   - "In one sentence, what does the user accomplish with this feature, and what does success look like to them?"
   - "What is the input (user text? a photo? audio? structured app data?) and the expected output?"
   - "Is AI actually required, or would a rule, a search index, a heuristic, or a template do the job more reliably and cheaply?"

2. **Quality Bar & Error Tolerance:**
   - "What is the success metric (acceptance rate, task completion, edit distance, click-through, satisfaction)?"
   - "What is the cost of a wrong/hallucinated/offensive output — annoyance, lost trust, safety risk, legal exposure?"
   - "Is the output advisory (user reviews before acting) or autonomous (the app acts on it)?"

3. **Data Sensitivity & Privacy:**
   - "What data feeds the model — and is any of it PII, health, financial, location, biometric, child-directed, or otherwise sensitive?"
   - "Is there a regulatory or contractual reason this data must not leave the device or a region?"
   - "Has a threat model / privacy plan been started? (We will hand data-flow decisions to it.)"

4. **Device & Distribution Reality:**
   - "What is the minSdk, the target-device range, and the share of low-RAM / no-NPU devices in the audience?"
   - "What region(s) ship this feature, and are there markets where cloud connectivity is poor or expensive?"
   - "What is the acceptable app-size / download budget for any bundled or delivered model?"

5. **Operational Constraints:**
   - "Is there a backend and budget for cloud inference, or must this be self-contained?"
   - "What is the expected request volume, and what is the per-call and monthly cost ceiling?"
   - "Who owns abuse handling, rate limiting, and the on-call burden if a cloud model misbehaves?"

---

## Instructions

### Phase 1: Frame the AI Feature (is AI the right tool?)

Fill the framing table. If AI is not clearly the best tool, say so and stop — a wrong tool choice is the most expensive mistake to undo.

```markdown
## AI Feature Frame

**Job-to-be-done:** [one sentence — the user outcome]
**Input → Output:** [input modality] → [output modality]
**Why AI (vs. rule / search / heuristic / template):** [justification, or "AI not justified"]

| Dimension | Definition | This feature |
|-----------|-----------|--------------|
| Success metric | How we'll know it works | [metric + target] |
| Quality bar | Minimum acceptable quality | [e.g., ≥80% accepted unedited] |
| Error tolerance | Cost of a wrong output | [low / medium / high + why] |
| Hallucination tolerance (LLM only) | Is a fabricated answer harmful? | [acceptable / must-mitigate / unacceptable] |
| Autonomy | Advisory vs. acts-on-output | [advisory / autonomous] |
| Reversibility | Can the user undo a bad result? | [yes / no] |
```

**CHECKPOINT 1 — Tool fit gate.** If the job is deterministic, low-variability, or better served by a non-AI approach, recommend against AI and propose the simpler alternative. Only proceed to Phase 2 once AI is justified. State the decision explicitly.

### Phase 2: On-Device vs. Cloud Inference Decision

Score each capability (a feature may decompose into several) on the matrix below. Use a 1–5 scale where 5 favors on-device and 1 favors cloud; weight by what matters for this feature.

```markdown
## Inference-Location Decision Matrix

| Criterion | On-device favored when... | Cloud favored when... | Weight | On-device score (1-5) |
|-----------|---------------------------|------------------------|--------|------------------------|
| Latency | Sub-second, interactive, offline typing-speed | Latency-tolerant, batchable | [%] | [n] |
| Privacy / data residency | Data is sensitive; must not leave device/region | Data is non-sensitive | [%] | [n] |
| Cost | High volume; per-call cloud cost unsustainable | Low/spiky volume; amortize server | [%] | [n] |
| Offline availability | Must work with no/poor connectivity | Always-connected use | [%] | [n] |
| Model capability needed | Task fits a small/medium model | Needs frontier-scale reasoning | [%] | [n] |
| Model size / storage | Fits app-size/download budget | Model too large to ship | [%] | [n] |
| Battery / thermal | Infrequent or short inferences | Heavy/sustained compute drains device | [%] | [n] |
| Device fragmentation | Audience has capable NPUs/RAM, or task is light | Wide low-end device base | [%] | [n] |
| Update cadence | Model changes rarely | Need to ship model updates frequently/instantly | [%] | [n] |
| **Weighted total** | | | 100% | **[Σ /5]** |
```

Interpretation guide (state the verdict, do not just compute):

| Weighted total | Recommendation |
|----------------|----------------|
| ≥ 3.5 | **On-device primary**, cloud fallback for capability gaps |
| 2.5 – 3.5 | **Hybrid / tiered** — route by device capability and data sensitivity |
| < 2.5 | **Cloud primary**, on-device only for offline/degraded mode |

A common correct outcome is *hybrid*: sensitive or offline cases run on-device, heavy or unsupported-device cases go to cloud. Do not force a single answer.

### Phase 3: Runtime & Model Selection (Android, current 2026)

Map each capability to a concrete runtime. Use this selection table; pick the highest-leverage option that meets the quality bar.

```markdown
## Runtime / Model Selection

| Option | Best for | Availability / caveat | Notes |
|--------|----------|------------------------|-------|
| ML Kit GenAI APIs (Gemini Nano via AICore) | Summarize, proofread, rewrite, image description — on-device generative | Supported devices only; gated by AICore feature availability; **must detect + fall back** | No model to ship; system-managed; check `FeatureStatus` before use |
| ML Kit task APIs | Text/barcode/face/pose recognition, language ID, translation, smart reply | Broadly available; some models download on first use | Mature, low-risk, no LLM hazards |
| Custom model on LiteRT (TensorFlow Lite) | Bespoke classification / vision / audio / small custom transformer | You own the model + size budget | Use GPU / NNAPI-successor / NPU delegate for acceleration; CPU fallback |
| Play for on-device AI (model delivery) | Delivering / updating LiteRT models without bloating the APK | Requires Play distribution | Decouples model size from install size; supports updates |
| Hardware acceleration (NPU / GPU delegate) | Speeding any LiteRT inference | Delegate support varies by device | Always implement CPU fallback path; benchmark per device tier |
| Cloud LLM / inference API | Frontier reasoning, large context, capabilities beyond on-device | Needs connectivity + backend + budget | Adds latency, cost, privacy exposure, abuse surface |
```

For the chosen option(s), record:

```markdown
**Capability → Runtime mapping**
- [Capability A] → [runtime] because [reason]; quality bar met by [evidence/plan]
- [Capability B] → [runtime] (fallback: [runtime]) because [reason]
```

**CHECKPOINT 2 — Availability reality check.** For any on-device generative path (Gemini Nano / AICore), confirm: (a) detection logic is specified, (b) a defined fallback exists for unsupported devices, (c) the feature degrades gracefully rather than crashing or silently doing nothing. If any is missing, do not proceed.

### Phase 4: Capability Detection & Tiered Fallback

Specify the runtime decision the app makes at execution time. The order is: **on-device when available → cloud when allowed → graceful degrade.**

```markdown
## Tiered Inference Strategy

Tier 1 (preferred): [on-device runtime]
  - Detect: [e.g., AICore feature status == AVAILABLE; device RAM/NPU check; model present]
  - Use when: [conditions — incl. sensitive-data-must-stay-local]
Tier 2 (fallback): [cloud or alternate on-device]
  - Use when: Tier 1 unavailable AND [data sensitivity allows] AND [connectivity present]
  - Guardrail: never send [enumerated sensitive fields] to cloud
Tier 3 (degrade): [non-AI experience]
  - Behavior: [hide feature / manual mode / cached result / clear message]
  - Never: leave a dead button, an infinite spinner, or a silent no-op
```

Capability-detection pseudo-pattern (illustrative, not version-pinned):

```kotlin
// Decide the inference path before invoking any model.
suspend fun resolveInferencePath(input: AiInput): InferencePath {
    val onDeviceReady = genAiCapability.isAvailable()      // AICore/ML Kit feature check
        && deviceTier.meetsMinimum()                       // RAM / NPU / OS gate
    return when {
        onDeviceReady                       -> InferencePath.OnDevice
        input.containsSensitiveData         -> InferencePath.DegradeLocalOnly   // never cloud
        connectivity.isUsable() && cloudAllowed -> InferencePath.Cloud
        else                                -> InferencePath.Degrade
    }
}
```

Also decide **model delivery & size budget**:

| Delivery method | Use when | Size impact |
|-----------------|----------|-------------|
| System-managed (Gemini Nano/AICore) | Using ML Kit GenAI | 0 added app size |
| Bundled in APK/AAB | Small model, must work on first launch offline | Adds to install size |
| Play for on-device AI delivery | Medium/large model, want updates | Decoupled from install size |
| First-use download | Large model, online-at-onboarding acceptable | Deferred; needs progress + retry UX |

Record the **storage/size budget**: `[max added install size]`, `[max downloaded model size]`, `[handling when storage is low]`.

### Phase 5: Performance & UX Budget

```markdown
## Performance & UX Budget

| Aspect | Target / Rule |
|--------|---------------|
| Latency budget (p50 / p95) | [e.g., on-device first token < 1s; cloud full response < 4s] |
| Streaming / partial results | [stream tokens? show partial summary? required for >1s waits] |
| Loading UX | [skeleton / progress / "thinking" — never a frozen UI] |
| Cancellation | User can cancel an in-flight inference; cancel frees compute/budget |
| Thermal limit | Back off / fall back when device is in thermal throttle |
| Battery limit | No sustained inference on low battery; respect background restrictions |
| Concurrency | [single-flight per feature? queue? cap in-flight cloud calls] |
```

### Phase 6: Privacy & Responsible-AI Guardrails

This phase feeds the threat model and privacy plan; coordinate, do not duplicate.

```markdown
## Responsible-AI Guardrails

### Data flow (hand to privacy plan + threat model)
| Data element | Sensitivity | On-device only? | Sent to cloud? | Where stored | Retention |
|--------------|-------------|------------------|----------------|--------------|-----------|
| [field] | [PII/health/etc.] | [yes/no] | [yes/no] | [device/server/none] | [duration] |

- Default: sensitive data stays on-device. Cloud only with explicit justification + consent.

### Consent & transparency
- [ ] User is told an AI feature is in use and what data it uses (plain language)
- [ ] Consent obtained before any sensitive data leaves the device
- [ ] AI-generated output is labeled as AI-generated where required (Play AI-content policy)
- [ ] A way to opt out / disable the AI feature exists

### LLM-specific safety (only for generative/LLM paths)
- [ ] Prompt-injection / jailbreak handling for any user- or content-derived input
- [ ] Content safety filtering on inputs and outputs (block disallowed categories)
- [ ] Abuse / misuse scenarios enumerated and mitigated
- [ ] Output never executed/acted-on without validation when autonomy is high

### Quality / eval harness (before launch)
- [ ] A representative eval set exists for the target task
- [ ] Quality bar from Phase 1 is measured against it (LLM-as-judge with rubric and/or human review)
- [ ] Hallucination / error rate measured and within tolerance
- [ ] Regression check planned for any model/runtime swap

### Play policy & compliance
- [ ] Complies with Play AI-generated-content and Generative-AI policies
- [ ] Data Safety form updated for any new data collection/sharing
- [ ] Region/age restrictions handled (child-directed, regulated data)
```

### Phase 7: Cost & Abuse Model (cloud paths only)

```markdown
## Cloud Cost & Abuse Model

| Item | Value |
|------|-------|
| Est. tokens/call (in/out) or unit cost | [n] |
| Est. calls/user/day | [n] |
| Projected monthly cost @ [DAU] | [$X] |
| Cost ceiling / kill-switch threshold | [$X → action] |

Abuse / rate-limiting controls:
- [ ] Per-user and per-device rate limits
- [ ] Server-side auth on the inference endpoint (no unauthenticated calls)
- [ ] Input size caps; reject oversized/malformed payloads
- [ ] Quota / budget alarms + automatic throttle or disable
- [ ] No API keys or secrets shipped in the app
```

**CHECKPOINT 3 — Pre-implementation gate.** Do not approve implementation until: tool fit is justified (Phase 1), an inference-location verdict with fallback exists (Phases 2–4), data flow is signed off by the privacy/threat work (Phase 6), an eval plan exists (Phase 6), and any cloud path has a cost ceiling + abuse controls (Phase 7).

---

## Expected Output

1. **AI Feature Frame** — job-to-be-done, why-AI justification, quality bar, error/hallucination tolerance.
2. **Inference-Location Decision** — scored matrix per capability with an explicit on-device / hybrid / cloud verdict.
3. **Runtime & Model Selection** — concrete runtime per capability (ML Kit GenAI / ML Kit task / LiteRT / cloud) with rationale.
4. **Tiered Fallback & Delivery Plan** — detection logic, Tier 1→2→3 behavior, model-delivery method, and size/storage budget.
5. **Performance & UX Budget** — latency targets, streaming, loading/cancel UX, thermal/battery rules.
6. **Responsible-AI Guardrails** — data-flow table, consent/transparency, LLM safety, eval harness, Play policy checklist.
7. **Cost & Abuse Model** — cloud cost projection, ceiling/kill-switch, rate limiting (if any cloud path).
8. **Go/No-Go** — explicit recommendation to implement, redesign, or use a non-AI approach.

---

## CRITICAL: Verification Requirements

- [ ] The "is AI the right tool?" question is answered explicitly, with a non-AI alternative considered.
- [ ] Each capability is routed to a specific runtime — no hand-waving "use AI."
- [ ] Any on-device generative path includes capability detection AND a defined fallback (Gemini Nano/AICore is never assumed available).
- [ ] The tiered strategy degrades gracefully — no dead buttons, infinite spinners, or silent no-ops.
- [ ] Sensitive data is never sent to cloud without explicit justification and consent; default is on-device.
- [ ] Model-delivery method and a numeric size/storage budget are stated.
- [ ] Latency, thermal, and battery budgets are quantified, not aspirational.
- [ ] An eval/quality harness is planned before launch, with hallucination/error rate measured against the tolerance from Phase 1.
- [ ] Cloud paths have a cost ceiling, kill-switch, server-side auth, and rate limiting; no secrets ship in the app.
- [ ] Play AI-content policy and Data Safety implications are checked.
- [ ] Data-flow decisions are handed to the threat model and privacy plan (no duplication, no gaps).

## False-Positive Prevention

- ❌ Do NOT assume Gemini Nano / on-device generative AI is available on the user's devices — it is gated by AICore and device support.
- ✅ DO require runtime capability detection and a concrete fallback for every on-device generative path.
- ❌ Do NOT default to cloud LLM just because it is the most capable option.
- ✅ DO score latency, privacy, cost, and offline needs before choosing a location — hybrid is often correct.
- ❌ Do NOT treat "add AI" as automatically valuable.
- ✅ DO kill the AI approach when a rule, search, or heuristic meets the job better and cheaper.
- ❌ Do NOT send sensitive data to the cloud for convenience.
- ✅ DO keep sensitive inference on-device by default and gate any cloud transfer behind consent.
- ❌ Do NOT skip the eval harness because the demo "looked good."
- ✅ DO measure quality and hallucination rate against the Phase 1 tolerance before launch.
- ❌ Do NOT ship a cloud inference endpoint without auth, rate limits, and a cost ceiling.
- ✅ DO enumerate abuse scenarios and add a kill-switch/budget alarm.
- ❌ Do NOT block the UI on a multi-second inference with no streaming or cancel.
- ✅ DO budget latency, stream partial results, and let users cancel.

## Techniques Used

- **ST-02** (Structured Sequential Instructions): Frame → decide location → select runtime → fallback → budget → guardrails → cost.
- **RT-02** (Multi-Dimensional Analysis Framework): The on-device-vs-cloud matrix scores latency, privacy, cost, capability, fragmentation, and more.
- **CM-02** (Constraint Specification): Size, latency, thermal, battery, cost, and data-residency constraints are made explicit.
- **AG-08** (Evidence-Based Decision Gates): Three checkpoints gate progress on tool fit, availability reality, and pre-implementation readiness.
- **DS-26** (Safe Defaults Pattern): Sensitive data stays on-device by default; graceful degrade is the default failure mode.
- **NE-02** (Phased Workflow Architecture): Seven phases with checkpoints structure the planning process.

## Related Prompts

- [android_app_concept_validation.md](android_app_concept_validation.md) - Validate and scope the feature before planning its AI capability.
- [android_mobile_threat_model.md](android_mobile_threat_model.md) - Threat-model the data flows and cloud surface this plan defines.
- [android_privacy_by_design_and_permissions_plan.md](android_privacy_by_design_and_permissions_plan.md) - Carry the data-flow and consent decisions into the privacy plan.
