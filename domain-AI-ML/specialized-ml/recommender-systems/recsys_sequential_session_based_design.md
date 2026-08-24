---
title: "Sequential & Session-Based Recommendation Design"
category: AI-ML/specialized-ml/recommender-systems
description: "Model user behavior as an ordered sequence — choose between session-based RNN/transformer/next-item architectures, define session boundaries, balance short- vs long-term intent, handle cold sessions, and design leak-free temporal evaluation."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - DS-01
  - QA-12
difficulty: advanced
tags:
  - recommender-systems
  - sequential-recommendation
  - session-based
  - next-item-prediction
  - temporal-evaluation
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/specialized-ml/recommender-systems/recsys_candidate_ranking_design.md
  - domain-AI-ML/specialized-ml/recommender-systems/recsys_multi_objective_ranking.md
  - domain-AI-ML/specialized-ml/recommender-systems/recsys_offline_evaluation.md
---

# Sequential & Session-Based Recommendation Design

**Objective:** Help the user design a recommendation model that treats user behavior as an *ordered sequence* rather than a static set of preferences. The aim is to decide whether a sequential/session-based approach is warranted at all, choose an architecture family (Markov/co-occurrence, session-RNN, self-attentive/transformer, or next-item embedding models) matched to session length and catalog dynamics, define session boundaries and intent horizons explicitly, handle cold sessions where little or no history exists, and — most critically — design an evaluation protocol that predicts the next item strictly from *past* interactions, so reported metrics reflect what the model could actually achieve in production.

**When to Use:**
- User behavior is intrinsically ordered and intent shifts within a visit (e-commerce browse-to-buy, news/video consumption, music queues).
- Sessions are anonymous or short-lived, so long-term user profiles are weak or unavailable.
- You need next-item / next-basket prediction and suspect order carries signal that a static matrix-factorization model discards.

**When NOT to Use:**
- Interactions are essentially order-independent or sparse per user — start with `recsys_architecture_design.md` and a non-sequential baseline.
- Your problem is candidate generation + scoring without temporal structure — see `recsys_candidate_ranking_design.md`.
- You primarily need to balance competing objectives (diversity, revenue, freshness) — see `recsys_multi_objective_ranking.md`.

## Inputs / Context

Provide what you can:
- **Interaction log schema** — fields available per event (user/anon id, item id, timestamp, event type, context features).
- **Session definition signal** — how a session is or could be delimited (explicit session id, inactivity gap, app open/close).
- **Sequence length distribution** — typical and tail number of events per session and per user.
- **Catalog dynamics** — how fast items churn (e.g. news/flash-sale vs. evergreen) and catalog size.
- **Latency / serving budget** — acceptable inference time and infra (real-time next-item vs. precomputed).
- **Cold-session prevalence** — share of sessions with 0–1 prior events.
- **Target action and horizon** — next click, next purchase, next-N items, or session continuation.

## Constraints

**Must:**
- Anchor the architecture choice to the sequence-length distribution and session-boundary definition, not to model fashion.
- Define session boundaries and the intent horizon (short-term within-session vs. long-term cross-session) explicitly before modeling.
- Specify a temporal, leak-free evaluation split where each prediction uses only events strictly before the target.
- State a concrete cold-session fallback (popularity, content-based, recency) for sessions below a length threshold.

**Must Not:**
- Recommend a transformer/self-attentive model purely because it is state of the art; justify it against simpler Markov/session-RNN baselines on the user's data.
- Use random train/test splits or leave-one-out without temporal ordering on inherently sequential data.
- Fabricate offline/online metric numbers (Recall@K, MRR, NDCG) from memory; reason from the user's data and mark unknowns.
- Assume long sessions are common without checking the length distribution.

**Instructions:**

1. **Confirm sequentiality pays.** Establish that order matters here — e.g. compare a non-sequential baseline (popularity, item-kNN, MF) against the simplest sequential baseline (first-order Markov / co-occurrence). If order adds little, stop and route back to `recsys_architecture_design.md`.
2. **Define the session.** Pin down boundaries: explicit session id, or an inactivity-gap heuristic (state the gap and how you'd validate it). Decide whether modeling is within-session only, cross-session, or hybrid.
3. **Characterize sequence length.** Read the length distribution. Short sessions (2–5 events) favor Markov/GRU4Rec-style models; longer sessions with rich context favor self-attentive (SASRec/BERT4Rec-style) models. Note tail behavior and truncation/padding strategy.
4. **Separate short- vs long-term intent.** Decide how recent context (current session) and durable preference (user history) combine — separate towers, attention over both, or recency-weighted blending — and which dominates for your target action.
5. **Choose the architecture family.** Map findings to: co-occurrence/Markov (interpretable, cold-robust), session-RNN/GRU (mid-length, streaming), self-attentive transformer (long, context-rich), or embedding next-item (large catalog, latency-sensitive). Frame as candidates to be decided by evaluation, not a single empirical winner.
6. **Design the cold-session path.** Specify behavior at session start and below a length threshold: popularity-by-context, content-based, or recency. Define the threshold and the handoff back to the sequential model as the session grows.
7. **Design leak-free temporal evaluation.** Split by time; for each target event, restrict inputs to events strictly before it. Use sliding-window or last-session holdout, never random shuffles. Define metrics (Recall@K, MRR, NDCG@K) and a candidate sampling protocol, and plan an online check.
8. **Plan the offline→online bridge.** State which offline gains you'd trust, how feedback-loop bias could inflate them, and the online experiment (interleaving or A/B) that confirms the lift before rollout.

**Output Format:**

A markdown design brief:
- **Sequentiality Justification** — evidence order matters, baseline comparison plan.
- **Session Definition** — boundary rule, intent horizon, validation approach.
- **Sequence Profile** — length distribution summary, truncation/padding plan.
- **Architecture Candidates** — 2–4 families with fit rationale and tradeoffs.
- **Cold-Session Strategy** — threshold and fallback behavior.
- **Evaluation Protocol** — temporal split, leak controls, metrics, candidate sampling.
- **Offline→Online Plan** — trusted offline signals, bias caveats, online test design.
- **Open Questions / Unknowns** — items requiring measurement on the user's data.

## Verification

- [ ] Session boundaries and intent horizon are defined explicitly, not assumed.
- [ ] Architecture choice is tied to the observed sequence-length distribution.
- [ ] A cold-session fallback with a concrete length threshold is specified.
- [ ] The evaluation split is temporal and each prediction uses only past events (leak-free).
- [ ] At least one simpler baseline is included for comparison.
- [ ] No offline/online metric numbers are invented — all are to be measured on the user's data.

## False-Positive Prevention

❌ **DON'T:**
- Shuffle interactions and use a random or standard leave-one-out split on sequential data — this leaks future behavior into training and inflates Recall@K.
- Predict an early event using later events from the same session ("temporal leakage") just because they share a session id.
- Assume the transformer wins because a paper said so, without a Markov/session-RNN baseline on the same temporal split.
- Report offline lift as if it will transfer, ignoring that logged sessions were shaped by the incumbent recommender (feedback-loop bias).

✅ **DO:**
- Sort by timestamp and enforce that every target's inputs come strictly from earlier events; audit the pipeline for any future-peeking feature.
- Treat session boundaries as a modeling decision and validate the inactivity gap against actual return behavior.
- Compare candidate architectures on the identical leak-free split and choose by measured offline+online results.
- Caveat the offline–online gap and confirm gains with an interleaving or A/B test before rollout.

## Example Output

```markdown
## Sequential Recommendation Design — Browse-to-Buy E-commerce

**Sequentiality Justification:** Order plausibly matters (category drift within session).
Plan: compare item-kNN baseline vs. first-order Markov on the same temporal split.

**Session Definition:** Inactivity gap of 30 min OR app close. Horizon: within-session
intent dominant; user history as a secondary recency-weighted tower. Validate gap against
return-visit distribution.

**Sequence Profile:** Median 4 events/session, p90 = 11, long tail to 40+. Truncate to
last 20, left-pad shorter sessions.

**Architecture Candidates:**
- First-order Markov / co-occurrence — interpretable baseline, cold-robust.
- GRU4Rec-style session-RNN — fits 4–11 length, streaming-friendly.
- Self-attentive (SASRec-style) — for the long tail; higher latency, evaluate before adopting.

**Cold-Session Strategy:** < 2 events → context-popularity (category + device). Hand off
to session model at event 2.

**Evaluation Protocol:** Time split (last 2 weeks = test). Per target, inputs = events
before it only. Metrics: Recall@20, MRR, NDCG@20 with 100 sampled negatives + all positives.

**Offline→Online Plan:** Trust relative ranking of candidates offline; confirm with
interleaving A/B. Caveat: logs reflect current recommender (feedback-loop bias) — numbers TBD.

**Open Questions:** Measure actual order-lift over MF; confirm 30-min gap empirically.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** Drives the ordered design flow from sequentiality check through evaluation.
- **RT-02 (Multi-Dimensional Analysis Framework):** Forces explicit baseline-vs-candidate comparison rather than defaulting to a single architecture.
- **CM-02 (Constraint Specification):** Encodes the leak-free and no-fabrication constraints that govern the design.
- **DS-01 (Framework Application):** Maps sequence-length and session signals to architecture families.
- **QA-12 (False Positives Identification):** Enforces the temporal, leak-free evaluation protocol.

**Related Prompts:**
- `recsys_candidate_ranking_design.md` — non-temporal candidate generation and scoring.
- `recsys_multi_objective_ranking.md` — balancing relevance against diversity, revenue, freshness.
- `recsys_offline_evaluation.md` — building the offline metric harness this design relies on.
