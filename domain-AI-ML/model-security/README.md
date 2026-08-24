# Model Security

Security of the model itself — the attacks that apply to a deployed model whether or not an agent is involved: adversarial inputs, training-data poisoning, extraction, membership and content leakage, artifact provenance, and the serving surface through which all of them arrive. **All prompts here are defensive and assume authorized review; none produce exploit code, payloads, or offensive procedures.**

**10 prompts.** Part of [`domain-AI-ML/`](../README.md) — see the domain README for the lifecycle routing table and the [boundary with adjacent domains](../README.md#boundary-with-adjacent-domains).

## When to enter here

- Before exposing a model through an API, a product surface, or a partner integration.
- Training data is not fully under your control, or the weights are not ones you produced.
- A security or customer review asks what could be done to the model.
- **Start with the threat model** — it decides which of the others you actually need.

**Not here:**
- The attack surface is an autonomous agent's tools, memory, and delegated privileges — [`../agentic-ai-systems/`](../agentic-ai-systems/README.md), which covers trust boundaries, least-agency scoping, memory poisoning and supply-chain attestation for agents.
- The attack surface is the surrounding application — injection at the app layer, output handling, authn/z → `domain-software-engineering/analysis/security/security_llm_application_review.md`.
- The question is a privacy *obligation* rather than an attack → [`../responsible-ai-governance/`](../responsible-ai-governance/README.md).

## Prompts


**Start here**

| Prompt | Use it to |
|---|---|
| [`mlsec_ml_threat_model.md`](mlsec_ml_threat_model.md) | Build a defensive threat model for a deployed ML model by walking a six-category attack taxonomy across the training, artifact, and inference surfaces, judging applicability from the model's actual exposure, and attaching a mitigation with its own detection signal. |

**Inference-time attacks**

| Prompt | Use it to |
|---|---|
| [`mlsec_adversarial_robustness_assessment.md`](mlsec_adversarial_robustness_assessment.md) | Measure a model's robustness to adversarial inputs under a threat model the deployment actually faces — defining the perturbation budget from the real input channel, evaluating with adaptive rather than fixed attacks, and reporting robust accuracy as a lower bound rather than a guarantee. |
| [`mlsec_adversarial_defense_strategy.md`](mlsec_adversarial_defense_strategy.md) | Choose and layer defenses against adversarial inputs — weighing robust training, input transformation, detection, and architectural containment against their clean-accuracy and latency costs, and committing to re-evaluate each under an attacker who knows the defense is there. |

**Training-time attacks**

| Prompt | Use it to |
|---|---|
| [`mlsec_data_poisoning_backdoor_defense.md`](mlsec_data_poisoning_backdoor_defense.md) | Defend the training set against poisoning and backdoors by tracing every path bytes take into training, placing controls at the contribution boundary rather than only at the model, and separating detectable distribution shift from a patient campaign that stays under the gate. |

**Confidentiality of the model**

| Prompt | Use it to |
|---|---|
| [`mlsec_model_extraction_defense.md`](mlsec_model_extraction_defense.md) | Defend a served model against functional stealing by pricing what extraction is worth to an attacker, reducing what each response reveals, budgeting queries against legitimate usage, and accepting that the goal is making extraction uneconomic rather than impossible. |
| [`mlsec_model_watermarking_provenance.md`](mlsec_model_watermarking_provenance.md) | Design watermarking, canaries, and output provenance for a model — deciding what claim you actually need to support, whether the evidence would survive an adversary and a dispute, and refusing to present attribution machinery as a deterrent. |

**Confidentiality of the data**

| Prompt | Use it to |
|---|---|
| [`mlsec_membership_inference_defense.md`](mlsec_membership_inference_defense.md) | Assess and reduce what a model leaks about who was in its training set — measuring the attack against a correctly matched non-member baseline, treating the generalization gap as the underlying cause, and stating what each mitigation does and does not protect. |
| [`mlsec_model_inversion_leakage_audit.md`](mlsec_model_inversion_leakage_audit.md) | Audit what a model reconstructs or regurgitates from its training data — separating genuine memorization from plausible-looking generation, testing extraction against known-planted content, and reporting per-record risk rather than a corpus-level average. |

**Artifact and serving surface**

| Prompt | Use it to |
|---|---|
| [`mlsec_ml_supply_chain_audit.md`](mlsec_ml_supply_chain_audit.md) | Audit the provenance and integrity of everything that enters a model — pretrained weights, datasets, serialization formats, and framework dependencies — establishing what is actually verified versus merely trusted, and what the load path can execute. |
| [`mlsec_secure_inference_endpoint_design.md`](mlsec_secure_inference_endpoint_design.md) | Design the serving-side controls around a model — authentication and per-caller budgets, response shaping, input validation, abuse and cost containment, and security logging — treating the endpoint as the surface where every model-level threat is actually delivered. |

## Conventions

- **Prefix:** `mlsec_` — one prefix per subdirectory, so a filename identifies its home.
- **Frontmatter:** the domain's eight fields — `title`, `category` (`AI-ML/model-security`), `description`, `techniques` (validated against `techniques/MASTER_TECHNIQUE_INDEX.md`), `difficulty`, `tags`, `updated`, `related_prompts`.
- **Structure:** five H2 sections — `Inputs / Context`, `Constraints`, `Verification`, `False-Positive Prevention`, `Example Output` — with `Objective`, `When to Use`, `When NOT to Use`, `Instructions`, `Output Format`, `Techniques Used`, `Related Prompts` as bold labels inside them.
- **No fabrication:** no invented benchmark numbers, accuracy figures, SOTA claims, or dataset statistics. Quantities that would change a decision are marked for measurement or verification.
- **Framework-neutral:** the user names the stack; prompts avoid hardcoding APIs that drift.
- **Defensive only.** Every prompt states that it is for authorized review and forbids attack code, payloads, and step-by-step offensive procedures.
- **No fabricated security facts.** No CVE, attack success rate, incident, or platform statistic is asserted from memory; quantities that would change a decision are marked `[verify against a primary source]`.
- **Attack feasibility is grounded in the threat model** — in what an attacker can actually reach, at what rate, with what feedback — never in whether the attack exists in the literature.
- **Defenses declare whether they prevent or raise cost**, and a defense evaluated only against attacks that predate it is reported as unevaluated.

## What lives elsewhere

- Agent-side security posture — threat model, trust boundaries, least agency, zero trust, AIBOM, memory poisoning, SecOps → [`../agentic-ai-systems/`](../agentic-ai-systems/README.md).
- Red-teaming exercise design → [`../responsible-ai-governance/rai_red_teaming_plan.md`](../responsible-ai-governance/rai_red_teaming_plan.md).
- Privacy obligations, differential privacy, and deletion → [`../responsible-ai-governance/`](../responsible-ai-governance/README.md).
