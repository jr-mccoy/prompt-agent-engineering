---
title: "Non-Technical Threat Model — Security Threat-Modeling Discipline for High-Visibility Actions"
category: risk/threat-modeling
description: "Adapt the security threat-modeling discipline — assets, threats, vulnerabilities, attack paths, mitigations — to a non-software situation where adversarial response is plausible: a launch event, a public statement, a partnership, a fundraise, a product reveal, an organizational change. For each asset (reputation, IP, relationships, market position), identify who would harm it, what tools they have, what the attack surface is, and what mitigations exist. Brings adversarial rigor to high-visibility moves that are usually planned as if no one is pushing back."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - risk-management
  - threat-modeling
  - adversarial
  - reputation
  - attack-surface
updated: "2026-05-10"
reasoning:
  styles: [adversarial, systems, structural, counterfactual]
  stakes: high
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: small_team
  output_format: matrix_structured
  user_role: [executive, founder, comms, policy, operator]
  mode: [audit, forecast, plan]
related_prompts:
  - domain-risk/risk_tail_risk_scan.md
  - domain-risk/risk_register_builder.md
  - domain-decision-making/scenario_strategic_pre_mortem.md
---

# Non-Technical Threat Model

**Objective:** Apply the discipline of security threat modeling to a non-software situation. For a high-visibility action where adversarial response is plausible — a launch event, a public statement, a partnership, a fundraise, a product reveal, an organizational change — identify the **assets** at stake (reputation, intellectual property, relationships, market position, momentum), the **threat actors** who would harm each, the **tools/capabilities** they have, the **attack surface** they can reach, the **attack paths** they'd take, and the **mitigations** available. The discipline this enforces: planning the move *as if an intelligent adversary is responding to it*, instead of the default of planning only the happy path and being surprised when someone pushes back.

**When to use:**
- A high-visibility, hard-to-take-back action is being planned and someone has reason to oppose it (competitor, activist, disgruntled insider, regulator, rival faction, journalist with an angle).
- A public statement or reveal where the downside is a hostile reframing, leak, or coordinated pushback.
- A partnership or fundraise where a counterparty or third party could move against you.
- Any move where "what's the worst someone could deliberately do with this?" hasn't been asked.

**When NOT to use:**
- A software/system security review — use a real STRIDE/technical threat model, not this adaptation.
- The action has no plausible adversary and no contested surface — threat modeling adds nothing to a benign internal change.
- You want non-adversarial tail risks (accidents, acts of nature, market shifts) — use `risk_tail_risk_scan.md`.
- You want a forward failure-path stress test of a plan generally — use `scenario_strategic_pre_mortem.md`.

**Audience:** Executives, founders, communications and policy leads, and operators planning high-visibility actions where intelligent opposition is realistic.

---

## Inputs / Context

1. **The action.** What's being done, when, how publicly, and why. One paragraph.
2. **Assets at stake.** What you'd lose if the action went wrong — reputation, IP, key relationships, market position, momentum, morale, funding.
3. **The landscape.** Who's around — competitors, regulators, activists, journalists, insiders, partners, rival factions — and their stance toward you.
4. **Known sensitivities.** Anything about the action that's contestable, hypocritical-looking, legally gray, or emotionally charged.
5. **Constraints on response.** What you can and can't do to defend (legal limits, brand constraints, relationships you can't burn).

---

## Constraints

### Must
- Inventory **assets** explicitly. You can't defend what you haven't named. Include intangible assets (reputation, trust, momentum, relationships) — these are usually the real targets.
- For each asset, identify **threat actors**: who would benefit from harming it or has motive to. Name them concretely, not "bad actors."
- For each threat actor, assess **capability/tools**: what they can actually do (media reach, legal action, leaks, mobilizing a base, regulatory complaints, counter-narrative, poaching, withholding).
- Map the **attack surface**: the points where the action is exposed to that actor (a quote that can be clipped, a partner who can be pressured, a document that can leak, a timing that can be exploited).
- Trace **attack paths**: the concrete sequence an actor would run (e.g., insider leaks draft → journalist frames it → competitor amplifies → regulator notices).
- For each significant attack path, assess **likelihood** and **impact**, and specify a **mitigation**: prevent (close the surface), deter (raise the actor's cost), detect (early warning), or respond (prepared reaction).
- Distinguish mitigations you do **before** the action (preparation) from **response plans** held ready for if the attack lands.

### Must Not
- Model only generic risk ("it might go badly") without a named actor and a concrete path. The adversarial frame is the whole value.
- Treat the adversary as stupid or static. Assume they're intelligent, informed, and responding to your move.
- Confuse an accident with an attack. This prompt is for *deliberate* adversarial response; route non-adversarial risk elsewhere.
- Over-rotate into paranoia — not every actor is a threat and not every surface gets attacked. Prioritize by likelihood × impact.
- Recommend only "prepare a statement." A communications response is one mitigation type; prevention, deterrence, and detection matter too.

---

## Instructions

### Step 1 — State the action and stakes
One paragraph: what's being done, how visibly, and what assets are exposed if it goes wrong.

### Step 2 — Inventory assets
List the assets at risk, tangible and intangible: reputation, IP/secrets, key relationships, market position, momentum, team morale, funding, regulatory standing. For each, note why it's valuable and how recoverable it is if damaged.

### Step 3 — Identify threat actors per asset
For each asset, ask "who would benefit from harming this, or has motive?" Name them: a specific competitor, an activist group, a regulator, a disgruntled insider, a rival internal faction, a journalist with an angle, a counterparty. Note their motive.

### Step 4 — Assess actor capabilities
For each actor, what tools do they actually have? Media reach, legal leverage, ability to leak, a mobilizable audience, regulatory channels, financial pressure, ability to poach, a credible counter-narrative. Be realistic about reach.

### Step 5 — Map the attack surface
Where is the action exposed to each actor? A clippable quote, a pressurable partner, a leakable document, an exploitable timing, an unflattering precedent, a legal gray area, an inconsistency with past statements.

### Step 6 — Trace attack paths
For each plausible actor-surface pairing, write the concrete sequence they'd run. Chain it: who does what, in what order, to turn the surface into damage to the asset.

### Step 7 — Score and mitigate
For each significant attack path: likelihood (low/med/high), impact (low/med/high). Then assign a mitigation of the right type:
- **Prevent** — close the surface (remove the gray area, secure the document, change the timing).
- **Deter** — raise the actor's cost or risk of acting.
- **Detect** — set early warning so you see the attack forming.
- **Respond** — prepare the reaction held ready if it lands.

### Step 8 — Separate preparation from response, and conclude
List what to do *before* the action (preparation) vs the **response plans** held ready. Name the single most dangerous attack path and whether the current plan defends it.

---

## False-Positive Prevention

1. **Faceless-threat vagueness.** "Someone might react badly." Name the actor, their motive, and the path. Generic risk isn't a threat model.
2. **Stupid-adversary assumption.** Modeling opponents as passive or dim. Assume intelligent, informed actors who adapt to your move and probe for the weakest surface.
3. **Accident/attack conflation.** Logging market shifts or mishaps as attacks. This prompt is for deliberate adversarial response; route accidents to a tail-risk scan.
4. **Tangible-only assets.** Listing money and IP but missing reputation, trust, relationships, and momentum — usually the actual targets of a non-technical attack. Include intangibles.
5. **Paranoia inflation.** Treating every bystander as an adversary and every surface as a breach. Prioritize by likelihood × impact; most surfaces won't be attacked.
6. **Comms-only mitigation.** Defaulting every defense to "draft a statement." Prevention (close the surface) and deterrence often beat reaction. Use all four mitigation types.
7. **Surface blindness.** Missing the inconsistency-with-past-statements or the pressurable-third-party surface because they're not obvious. The hypocrisy clip and the squeezed partner are classic attack surfaces.
8. **Preparation/response collapse.** Listing mitigations without separating what you do before the action from what you hold ready for after. Both are needed; conflating them loses the timeline.

---

## Output Format

```
# Non-technical threat model — [action]

## Action & stakes
- Action: [what, when, how visible]
- Why an adversary would respond: [the contested element]

## Asset inventory
| Asset | Why valuable | Recoverability if damaged |
|-------|--------------|---------------------------|
| Reputation | [...] | slow |
| Key partner relationship | [...] | hard |
| Market position | [...] | moderate |
| … | | |

## Threat actors
| Actor | Targets which asset | Motive | Capabilities/tools |
|-------|---------------------|--------|--------------------|
| [competitor X] | market position | [...] | media reach, counter-narrative |
| [insider] | reputation, IP | [...] | document access, leak |
| [regulator] | regulatory standing | [...] | complaint, investigation |
| … | | | |

## Attack surface
- [Surface 1: clippable quote in the announcement]
- [Surface 2: partner who can be pressured]
- [Surface 3: inconsistency with last year's statement]
- …

## Attack paths (scored)
| # | Actor | Path (sequence) | Asset hit | Likelihood | Impact |
|---|-------|-----------------|-----------|------------|--------|
| 1 | [insider→journalist→competitor] | [leak draft → hostile frame → amplification] | reputation | med | high |
| 2 | [competitor] | [counter-launch timed to overshadow] | momentum | high | med |
| … | | | | | |

## Mitigations
| Attack path | Type | Action | Before action / held ready |
|-------------|------|--------|----------------------------|
| #1 | prevent + respond | [secure draft; pre-draft factual response] | both |
| #2 | deter + detect | [pre-brief allies; monitor competitor signals] | before |
| … | | | |

## Conclusion
- Most dangerous attack path: [# — and whether the current plan defends it]
- Preparation checklist (before the action): [...]
- Response plans held ready: [...]
```

---

## Verification

- [ ] Assets inventoried, including intangibles (reputation, trust, relationships, momentum).
- [ ] Threat actors named concretely with motives, not "bad actors."
- [ ] Each actor's real capabilities/tools assessed.
- [ ] Attack surface mapped, including non-obvious surfaces (inconsistency, pressurable third parties).
- [ ] Attack paths traced as concrete sequences, not vague risks.
- [ ] Each significant path scored on likelihood and impact.
- [ ] Mitigations use all four types (prevent / deter / detect / respond), not comms-only.
- [ ] Preparation (before) separated from response plans (held ready).
- [ ] Adversary modeled as intelligent and adaptive; accidents routed elsewhere.
- [ ] Most dangerous attack path named with a defense verdict.
