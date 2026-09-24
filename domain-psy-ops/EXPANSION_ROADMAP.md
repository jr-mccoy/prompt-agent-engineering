# Expansion Roadmap — `domain-psy-ops/`

**Status as of 2026-09-24:** ✅ **Wave 2 shipped in full** — all **9 Wave 2 candidates** built, taking the domain from 32 to **41 prompts** across the same **6 subdirectories**. See [Wave 2 — shipped](#wave-2--shipped-2026-09-24) below.

**Wave 1 (2026-07-28):** ✅ **32 net-new prompts** across **6 subdirectories**, launching the domain at the scale of `domain-reasoning-craft/` (41) and `domain-negotiation/` (46). Every prompt is built and validated: 8-field frontmatter with the machine-readable `reasoning:` block, exactly six `##` headings outside the fenced output template, ~8 numbered instruction steps, an 8-item False-Positive Prevention list, a locked Output Format, and a 10-item Verification checklist closing on negative assertions.

**One deliberate deviation from the house style.** Every analysis prompt (all of `technique-analysis/`, `influence-operations/`, `organizational-red-team/`, `counter-messaging/`) ends in an explicit adversarial check arguing against its own finding. The ten `personal-defense/` prompts do not, and this is a design decision rather than an omission: adversarially challenging a person working through suspected coercive control, or a parent frightened their child is being radicalized, is harmful rather than rigorous. Those prompts carry their skepticism in the mandatory ordinary-conflict / alternative reading and in the False-Positive Prevention block, and close on a next step the user chooses rather than a verdict. The three `case-studies-taxonomies/` prompts close on their subject-appropriate equivalents — the cynicism check and the outstanding-`[VERIFY]` list. All `related_prompts` resolve; all technique IDs resolve in `techniques/MASTER_TECHNIQUE_INDEX.md`.

**Filing convention:** `psyops_{specific_function}.md` inside the relevant subdirectory, with a single `psyops_` prefix across all six (the `domain-legal/` and `domain-negotiation/` precedent). `uncertainty: ambiguity` is a domain invariant.

---

## Shipped architecture

```
domain-psy-ops/                        41 prompts   ✓
├── technique-analysis/         8/8  ✓ (+1)  name the move in one artifact
├── influence-operations/       9/9  ✓ (+2)  campaign-scale assessment
├── personal-defense/         10/10  ✓ (+3)  aimed at you (safety-gated)
├── organizational-red-team/    5/5  ✓ (+1)  findings + countermeasures only
├── counter-messaging/          6/6  ✓ (+2)  overt, attributed, truthful
└── case-studies-taxonomies/    3/3  ✓       the teaching track
```

---

## The convention this domain is built on

The repository's existing dual-use precedent, `domain-software-engineering/bug-bounty/`, works because a bounty program is a **verifiable, scoped grant of permission from a consenting target**. That structure does not exist here: an influence operation's targets are, definitionally, people who do not know it is happening, so there is no authorization that would make campaign-generation legitimate.

The domain is therefore built on an **output-side** constraint rather than a permission gate — every prompt's deliverable is an assessment, a defense, or a resilience plan — reinforced by five supporting rules (no manufactured accusations, no fabricated evidence, attribution humility, safety routing, overt counter-messaging). See the [README](README.md) for the full statement.

The **characteristic failure mode** the domain is designed against is paranoid over-attribution: organic convergence read as coordination, sincere belief read as a script, incompetence read as deception. Every False-Positive Prevention block targets it, and the alternative-explanation pass is non-optional in every analysis prompt.

---

## Explicitly not gaps

These adjacent capabilities are **deliberately cross-linked rather than duplicated**. This table is the authoritative boundary; a proposal to add any of them should be checked against it first.

| Capability | Where it lives | Why it is not duplicated here |
|---|---|---|
| General fallacy scanning, source triangulation, evidence-quality scoring, bias audits | `domain-reasoning-craft/epistemic/` | Content-agnostic reasoning moves. This domain's `psyops_rhetorical_deception_scan.md` covers only the narrower class of structural moves that exhaust or trap a responder. |
| Framing and argument mapping as general reasoning technique | `domain-reasoning-craft/reasoning-moves/` | `psyops_framing_and_narrative_analysis.md` is the influence-specific application; the general moves stay upstream. |
| Where persuasion becomes manipulation inside a deal you are party to | `domain-negotiation/craft/negotiation_ethics_line.md` | Bilateral, consented, known-adversary context. Different problem from a third party influencing an audience that does not know it. |
| Defending against hard-bargaining tactics at a table | `domain-negotiation/at-the-table/` | Live negotiation defense, not influence analysis. |
| Therapy, clinical treatment, and the aftermath of manipulation or abuse | `domain-psychology/` | This domain organizes a user's observations and routes out. It never diagnoses, counsels, or treats. |
| Everyday non-clinical emotional skills | `domain-personal-development/prompts/emotional-fitness/` | Processing feeling for its own sake, rather than decoding a message or a relationship pattern. |
| Phishing and social engineering at the organizational/technical layer | `domain-software-engineering/analysis/security/` | `psyops_social_engineering_pretext_recognition.md` is individual-facing and non-technical; the technical control layer stays in security. |
| Prompt-injection and untrusted-content defense for AI agents | `domain-AI-ML/agentic-ai-systems/aiagent_prompt_injection_untrusted_content_defense.md` | Machine-target influence. Different threat model, different mitigations. |
| Building persuasive commercial creative for a client you represent | `domain-advertising/`, `domain-product-management/` | Disclosed, attributed commercial persuasion. Legitimate craft, not this domain's subject. |
| Documenting incidents for a legal matter | `domain-legal/family-self-advocacy/`, `domain-legal/personal-self-advocacy/` | Litigant-facing documentation with its own conventions and jurisdiction requirements. |
| Stakeholder and coalition mapping for policy work | `domain-policy/policy_stakeholder_coalition_map.md` | Alignment analysis, not authenticity assessment. `psyops_astroturf_vs_organic_assessment.md` answers a different question. |
| General instructional design | `domain-education-teaching/` | `psyops_media_literacy_curriculum_designer.md` is subject-specific; pedagogy scaffolding stays upstream. |
| Operational risk registers, FMEA, heat maps | `domain-risk/` | Risk artifacts rather than influence assessment. `risk_threat_model_non_technical.md` is the general sibling of `psyops_org_influence_threat_model.md`. |

### Permanently out of scope

Not a backlog — these will not be built, and the reasoning is in the README's load-bearing convention:

- Propaganda, persuasion copy, or messaging intended to influence an audience covertly.
- Covert persona construction, sockpuppet design, or inauthentic engagement.
- Audience targeting packages, psychographic segmentation for influence, or micro-targeting design.
- Coordinated-inauthentic-behavior playbooks, brigading guidance, or detection-evasion technique.
- Pretext construction, or unauthorized social-engineering testing against people.
- Deprogramming or intervention scripts to be run on another person.
- Anything that produces a verdict naming a private individual as an operative, bot, shill, or agent.

---

## Wave 2 — shipped (2026-09-24)

All nine candidates passed the output-side constraint and were built to the Wave 1 house style (six `##` headings, 8-item False-Positive Prevention, `reasoning:` block, 10-item Verification closing on negative assertions). Analysis prompts end in an adversarial check; the three new `personal-defense/` prompts close on a user-chosen next step and each carries a Safety Block (now eight of ten in that subdirectory).

| Prompt | Subdirectory | Gap it fills | Guard specific to this prompt |
|---|---|---|---|
| `psyops_visual_media_authenticity_assessment.md` | `technique-analysis/` | Synthetic / manipulated / miscontextualized media assessment, distinct from provenance tracing | Detector scores are weak inputs, never verdicts; liar's-dividend check; hard stop on intimate imagery and anything that may depict a minor; no evasion guidance |
| `psyops_cross_platform_narrative_correlation.md` | `influence-operations/` | Same narrative across platforms with unequal data access | Visibility map before any correlation; absence on a low-visibility platform carried as unknown |
| `psyops_influence_assessment_writeup.md` | `influence-operations/` | Publishing findings with hedges that survive editing and retelling (confidence laundering) | Claim ledger; hedges built into grammar; pre-written headline; extraction test; right of reply |
| `psyops_youth_online_manipulation_guide.md` | `personal-defense/` | Grooming, coercion, and sextortion aimed at minors | Recognition-level only; self-harm first; no payment, no image handling; every service looked up officially; cross-linked to `domain-parenting/`. **Human child-safety review is still recommended** before this prompt is promoted beyond the domain — the roadmap's original condition, which authoring alone cannot satisfy |
| `psyops_elder_targeted_fraud_recognition.md` | `personal-defense/` | Approaches built for older adults, and the family-conversation problem | Dignity and independence preserved; no capacity judgments or takeover advice; secrecy-from-family as the key indicator |
| `psyops_workplace_influence_dynamics.md` | `personal-defense/` | Manipulation inside an employment relationship, with exit cost and power asymmetry | Boundary checked against `domain-personal-development/prompts/stakeholder/` (that is navigating politics; this is recognizing manipulation); no counter-tactics, diagnoses, or covert recording |
| `psyops_election_integrity_communications.md` | `counter-messaging/` | Election-process response under fixed deadlines and legal limits | Process-only and nonpartisan; no procedure from memory; no outcome projection or blanket security claims |
| `psyops_internal_comms_under_attack.md` | `counter-messaging/` | Staff as the audience an attack reaches first | Targeted individuals protected before all-staff messaging; explicit line against undisclosed staff amplification |
| `psyops_moderator_burnout_and_capture.md` | `organizational-red-team/` | Sustained hostile attention as an attrition strategy against moderators | Structure, not people; no moderator vulnerability ranking; capture read from enforcement patterns |

No Wave 3 candidates are committed. Proposals are checked against the **Explicitly not gaps** table and the **Permanently out of scope** list above before anything else.

## Deliberately deferred

| Idea | Why deferred |
|---|---|
| Country- or conflict-specific analysis guides | Would date quickly and would require ongoing factual maintenance the repository cannot provide. The domain's prompts are deliberately actor-neutral. |
| A "current techniques" reference | Same problem, worse: a stale techniques list actively misleads. `psyops_technique_taxonomy_reference.md` maps stable frameworks instead. |
| Automated indicator or scoring tooling | Scored instruments in this field produce exactly the false-positive harm the domain is designed against. Every prompt deliberately outputs confidence bands rather than scores. |
| Attribution to named state actors | Requires evidence and standing the repository does not have. `psyops_attribution_confidence_assessment.md` teaches the grading discipline instead of asserting conclusions. |
