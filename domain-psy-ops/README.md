# Psy-Ops — Cognitive Security, Influence Analysis, and Manipulation Defense

Prompts for **recognizing, analyzing, and defending against psychological influence operations** — from a single manipulative message to a coordinated campaign to a controlling relationship. The domain covers the techniques themselves (what move is being run), campaign-scale activity (who is running it and how), personal exposure (what to do when it is aimed at you), organizational exposure (what to do when it is aimed at your institution), legitimate response (how to counter it honestly), and the teaching track (how to build the literacy in other people).

Users are analysts, trust-and-safety and communications staff, researchers, moderators, educators, and individuals trying to work out whether what they are experiencing or reading is what it appears to be.

---

## ⚠️ Load-bearing convention: analytic output, no manufactured accusations

This is a dual-use subject, and the repository's existing dual-use precedent does not transfer to it.
`domain-software-engineering/bug-bounty/` works because a bounty program is a **verifiable, scoped grant
of permission from a consenting target** — the authorization gate is real, so offensive methodology is
legitimate inside it. An influence operation has **no consenting target by construction**: the people
being influenced are, definitionally, people who do not know it is happening. There is no authorization
that would make campaign-generation legitimate here.

So this domain is built on an **output-side** constraint rather than a permission gate. Every prompt
enforces the following, and you must too:

1. **Analytic output only.** The deliverable is an assessment, a defense, or a resilience plan. No prompt
   in this directory produces propaganda copy, covert persona content, inauthentic engagement, audience
   targeting packages, or a coordinated-inauthentic-behavior playbook. Red-team prompts output **findings
   and countermeasures** — never the campaign material they are modeling.
2. **No manufactured accusations.** Calling a person a bot, a shill, an agent, or an operative is
   defamatory and frequently wrong. Analysis prompts output **confidence-graded assessments with a
   mandatory alternative-explanation pass**, never verdicts. Assessments attach to **behavior and content**
   — never to a named private individual as an accusation of covert affiliation.
3. **No fabricated evidence.** No invented account handles, engagement figures, dates, funding trails,
   operations, or citations. Unknowns are marked `[VERIFY]` and stay unknown. A plausible-sounding
   fabricated detail is the most dangerous possible output in this field.
4. **Attribution humility.** Attribution is the hardest claim in influence analysis and the one most
   often wrong. Prompts use explicit low / moderate / high confidence with the basis stated, and they
   actively resist attribution that the evidence does not support.
5. **Safety routing.** Every `personal-defense/` prompt that touches fear, abuse, danger, or active fraud
   carries a mandatory Safety Block — five of the seven do, and the remaining two (`information_diet_audit`,
   `cognitive_security_hygiene_plan`) are reflective audits with no distress dimension, where a pasted-in
   crisis block would be noise rather than protection. Coercive control, abuse, radicalization, and fraud
   concerns route to qualified professionals, `domain-psychology/`, and verified resources. **No prompt in
   this domain states a hotline number, URL, or service name from memory** — every one instructs the user
   to look it up from an official source, because a confidently wrong emergency number is the worst output
   this domain could produce. These prompts organize a user's own observations: they do not diagnose, do
   not provide crisis counseling, and do not script interventions on another person.
6. **Counter-messaging stays overt.** Response work is attributed, truthful, and openly sourced: a named
   sender, on a declared channel, saying true things. The domain never builds the thing it defends against.

If a request would take you outside these limits, stop — the answer is not a scoped version of the same
thing.

### The failure mode this domain is designed against

**Paranoid over-attribution — seeing operations everywhere.** It is the characteristic way this analysis
goes wrong, it is far more common than under-detection, and it does real harm to real people. Organic
convergence looks like coordination. Sincere belief looks like a script. A misleading chart is usually
incompetence, not deception. Most people repeating a false claim believe it and are not being paid. Every
False-Positive Prevention block in this domain targets that failure specifically, and the
alternative-explanation pass is non-optional in every analysis prompt.

---

## How to use this domain

Route by **what you are holding**:

```
A single artifact (post, ad, email, article, speech)   → technique-analysis/
A pattern across many accounts / outlets / weeks       → influence-operations/
Something aimed at you or someone you love             → personal-defense/
Exposure of your org, platform, or community           → organizational-red-team/
You need to respond publicly                           → counter-messaging/
You are teaching this, or studying a documented case   → case-studies-taxonomies/
```

If you are not sure whether there is anything real here at all, start with
`influence-operations/psyops_influence_operation_analysis.md` — it is built to return "insufficient
evidence; this looks organic" as a first-class result.

---

## Routing table

### `technique-analysis/` — name the move in a specific artifact

| You want to… | Prompt |
|---|---|
| Dissect an artifact into named, evidenced propaganda techniques | `psyops_propaganda_technique_identification.md` |
| Inventory the compliance pressure and dark patterns in a message or offer | `psyops_persuasion_pressure_audit.md` |
| Identify which emotions are being recruited, and for what | `psyops_emotional_manipulation_decoder.md` |
| Analyze framing, metaphor, and what the frame renders invisible | `psyops_framing_and_narrative_analysis.md` |
| Scan for deliberate deception strategies (motte-and-bailey, gish gallop, JAQing) | `psyops_rhetorical_deception_scan.md` |
| Trace a claim or image back through its chain of transmission | `psyops_provenance_and_transmission_trace.md` |
| Check statistics and charts for distortion | `psyops_statistical_and_visual_distortion_scan.md` |

### `influence-operations/` — campaign-scale analysis

| You want to… | Prompt |
|---|---|
| **Run the full analysis: actors, behavior, content, degree, effect** | `psyops_influence_operation_analysis.md` |
| Distinguish coordination from organic convergence | `psyops_coordinated_inauthentic_behavior_indicators.md` |
| Track a narrative from seeding through mainstreaming | `psyops_narrative_lifecycle_tracker.md` |
| Assess automation / sockpuppet signals on account behavior | `psyops_inauthentic_account_signal_assessment.md` |
| Decide whether a movement is manufactured or genuinely grassroots | `psyops_astroturf_vs_organic_assessment.md` |
| Map how a claim was laundered into legitimacy through outlet hops | `psyops_information_laundering_chain_map.md` |
| Grade how confident attribution can honestly be | `psyops_attribution_confidence_assessment.md` |

### `personal-defense/` — aimed at you (Safety Block on every prompt touching fear, abuse, danger, or fraud)

| You want to… | Prompt |
|---|---|
| Work out whether what you are experiencing is manipulation | `psyops_manipulation_recognition_personal.md` |
| Recognize coercive-control patterns in a relationship | `psyops_coercive_control_pattern_recognition.md` |
| Assess a group's dynamics against documented high-control criteria | `psyops_high_control_group_dynamics_assessment.md` |
| Recognize a pretext / phishing / vishing approach aimed at you | `psyops_social_engineering_pretext_recognition.md` |
| Audit what is actually shaping your beliefs | `psyops_information_diet_audit.md` |
| Build a personal cognitive-security routine | `psyops_cognitive_security_hygiene_plan.md` |
| Think through concern that someone you love is being radicalized | `psyops_concern_for_someone_radicalizing.md` |

### `organizational-red-team/` — findings and countermeasures only

| You want to… | Prompt |
|---|---|
| Threat-model who would target your organization, and how | `psyops_org_influence_threat_model.md` |
| Find which real grievances about you are exploitable — and fix them | `psyops_narrative_vulnerability_assessment.md` |
| Review social/pretext exposure of key personnel | `psyops_personnel_targeting_exposure_review.md` |
| Review a community or platform's resilience to brigading and manipulation | `psyops_community_moderation_resilience_review.md` |

### `counter-messaging/` — overt, attributed, truthful

| You want to… | Prompt |
|---|---|
| Design prebunking / inoculation before a claim arrives | `psyops_prebunking_inoculation_design.md` |
| Design a correction that actually displaces the false belief | `psyops_debunk_and_correction_design.md` |
| Decide whether responding would amplify the rumor | `psyops_rumor_response_triage.md` |
| Communicate with integrity during an active attack | `psyops_crisis_communication_integrity_plan.md` |

### `case-studies-taxonomies/` — the teaching track

| You want to… | Prompt |
|---|---|
| Map the named public taxonomies against each other | `psyops_technique_taxonomy_reference.md` |
| Study a documented, publicly attributed historical operation | `psyops_historical_operation_case_study.md` |
| Build a media-literacy teaching sequence | `psyops_media_literacy_curriculum_designer.md` |

---

## Conventions for these prompts

All prompts here are Tier-1 and follow the house style shared with `domain-reasoning-craft/` and
`domain-negotiation/`: 8-field YAML frontmatter including the machine-readable `reasoning:` block, exactly
six `##` headings (`Inputs / Context`, `Constraints`, `Instructions`, `False-Positive Prevention`,
`Output Format`, `Verification`), ~8 numbered instruction steps, an 8-item False-Positive Prevention list,
a locked output template, and a verification checklist closing on negative assertions.

Every **analysis** prompt ends in an explicit adversarial check that argues against its own finding, and
carries an alternative-explanation pass. The `personal-defense/` prompts deliberately do **not** — adversarially
challenging someone working through suspected coercive control, or a parent frightened for their child, is
harmful rather than rigorous. Those prompts close on a next step the user chooses, and carry their skepticism
in the ordinary-conflict reading and the False-Positive Prevention block instead. The `case-studies-taxonomies/`
prompts close on their own equivalents — the cynicism check and the outstanding-`[VERIFY]` list. `uncertainty: ambiguity` is a domain invariant. Filing convention is a single `psyops_` prefix
across all subdirectories.

## Related domains

| Need | Go to |
|---|---|
| General fallacy scanning, source triangulation, evidence quality, bias audits | `domain-reasoning-craft/epistemic/` |
| Where persuasion becomes manipulation inside a deal you are party to | `domain-negotiation/craft/negotiation_ethics_line.md` |
| Clinical support, therapy, and the aftermath of manipulation or abuse | `domain-psychology/` |
| Phishing and social engineering at the organizational/technical level | `domain-software-engineering/analysis/security/` |
| Building persuasive commercial creative for a client you represent | `domain-advertising/` |
| Prompt-injection and untrusted content aimed at AI agents | `domain-AI-ML/agentic-ai-systems/aiagent_prompt_injection_untrusted_content_defense.md` |
