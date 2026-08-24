# Expansion Roadmap — `domain-negotiation/`

**Status as of 2026-07-26:** ✅ **Wave 1 shipped in full** — **40 net-new prompts** (6 → **46**) reorganized into **8 subdirectories**, taking the domain from a preparation-only starter set to a full negotiation practitioner library at the scale of `domain-reasoning-craft/` (41). Every prompt below is built and validated: exactly six `##` headings, three resolving `related_prompts`, `category` matching its subdirectory, and all technique IDs present in `techniques/MASTER_TECHNIQUE_INDEX.md`. All new prompts follow the domain's established house style (exemplar: `preparation/negotiation_interest_mapping.md`): 9-field frontmatter with the machine-readable `reasoning:` block, six `##` headings, 9 instruction steps ending in an adversarial check, an 8-item False-Positive Prevention list, a locked Output Format template, and a Verification checklist closing on negative assertions.

**Filing convention:** `negotiation_{specific_function}.md` inside the relevant subdirectory. The domain keeps **one prefix across all subdirectories** (the `domain-legal/` precedent — `legal_*` spans `research/`, `litigation/`, `discovery/`, …), with the single pre-existing exception of `difficult-conversations/difficultconvo_*.md`, which has its own prefix because it is a distinct audience track: relationship-primary conversations where the goal is to be understood, not to win a distributive point.

**Scope discipline.** This roadmap is intentionally finite. Prompts that would duplicate `domain-legal/` (contract position papers, mediation prep, settlement valuation), `domain-personal-development/` (boundary scripts, stakeholder navigation, offer evaluation), `domain-conversation-practice/` (live role-play), or `domain-psychology/` (conflict post-mortems) are excluded — see the **Explicitly not gaps** table below, which is the authoritative boundary.

---

## Shipped architecture

```
domain-negotiation/                      46 prompts   ✓
├── preparation/            10/10  ✓ (+7)   the work before you walk in
├── at-the-table/            7/7   ✓ (NEW)  live moves once it starts
├── channels/                4/4   ✓ (NEW)  medium-specific: written, remote, cross-cultural
├── multi-party/             4/4   ✓ (+3)   three or more parties, teams, facilitation
├── after-the-deal/          4/4   ✓ (NEW)  debrief, implement, reopen, recover
├── contexts/                8/8   ✓ (NEW)  named specializations of the general machinery
├── difficult-conversations/ 5/5   ✓ (+3)   relationship-primary track (own prefix)
└── craft/                   4/4   ✓ (NEW)  building negotiation skill over time
```

**Reorganization note.** The four original top-level prompts moved into `preparation/` (BATNA, interest mapping, rehearsal) and `multi-party/` (coalition alignment), keeping the `negotiation_` prefix. Twenty-one inbound references were rewritten across `CLAUDE.md`, `PROMPT_INDEX.md`, `domain-personal-development/` (5 files), and the moved files themselves. `difficult-conversations/` did not move, so its twelve inbound references were unaffected.

### `preparation/` (10) — 3 relocated, 7 new

| File | Description |
|---|---|
| `negotiation_prep_depth_triage.md` | **NEW.** Routing entry point: how much prep this negotiation warrants, and which domain prompts to run in what order |
| `negotiation_batna_analysis.md` | *Relocated.* BATNA both sides, reservation points, ZOPA |
| `negotiation_leverage_audit.md` | **NEW.** Leverage beyond BATNA — time, information, legitimacy, relationship, scarcity, coalition — inventoried and ranked by durability |
| `negotiation_interest_mapping.md` | *Relocated.* Positions vs. interests, why-laddered per side |
| `negotiation_package_trade_design.md` | **NEW.** Log-rolling by differential valuation, MESOs, contingent terms |
| `negotiation_opening_offer_design.md` | **NEW.** Whether to move first, where to anchor, and the justification that makes the anchor stick |
| `negotiation_concession_anchoring_plan.md` | **NEW.** The concession ladder: size, order, decay, what each buys, the reciprocity rule |
| `negotiation_counterpart_simulation.md` | **NEW.** Model their brief, pressure, constraints, three likely moves, your response to each |
| `negotiation_information_plan.md` | **NEW.** What to ask, what to reveal, what to protect, and in what order |
| `negotiation_pre_meeting_rehearsal.md` | *Relocated.* Script the load-bearing moments into a decision tree |

### `at-the-table/` (7) — all new

| File | Description |
|---|---|
| `negotiation_question_sequencing_live.md` | Question sequences that surface interests and constraints in real time without signalling desperation |
| `negotiation_reading_signals_and_bluffs.md` | Interpret verbal and behavioural cues, test a claimed constraint, distinguish a real limit from a posture |
| `negotiation_hard_bargainer_defense.md` | Name and neutralize extreme anchors, exploding offers, the nibble, good-cop/bad-cop, manufactured deadlines |
| `negotiation_impasse_breaker.md` | Diagnose impasse type (positional / informational / emotional / structural / authority) and pick the matched unlock |
| `negotiation_authority_mandate_limits.md` | Set your own mandate, probe theirs, handle "I have to check with my boss," manage ratification risk |
| `negotiation_emotional_flooding_at_the_table.md` | Anger, walkouts, tears, and your own reactivity — de-escalate without conceding on substance |
| `negotiation_closing_and_final_concession.md` | Recognize the close, structure the final concession, refuse the post-agreement nibble |

### `channels/` (4) — all new

| File | Description |
|---|---|
| `negotiation_written_async_message.md` | What belongs in writing vs. live; tone calibration; the record a written position creates |
| `negotiation_counteroffer_email.md` | The counter-offer message: structure, justification, what to concede in text, what to reserve |
| `negotiation_remote_video_channel.md` | Video and phone: lost signal, turn-taking, silence that reads as disagreement, screen-share as an anchor |
| `negotiation_cross_cultural.md` | **Strong guard required** — surfaces *dimensions* on which norms vary and prescribes asking, never asserting national-character generalizations as fact |

### `multi-party/` (4) — 1 relocated, 3 new

| File | Description |
|---|---|
| `negotiation_multi_party_alignment.md` | *Relocated.* Coalition mapping and concession sequencing |
| `negotiation_team_negotiation_roles.md` | **NEW.** Who speaks, who observes, internal signals, caucus protocol, preventing the split the counterpart will hunt for |
| `negotiation_coalition_defense.md` | **NEW.** When they have coalesced against you: split the coalition legitimately, or negotiate with the bloc |
| `negotiation_facilitator_third_party.md` | **NEW.** Running a negotiation you are not a party to — the only neutral-role prompt in the repo |

### `after-the-deal/` (4) — all new

| File | Description |
|---|---|
| `negotiation_post_negotiation_debrief.md` | Outcome vs. reservation point, which moves moved the number, what their behaviour revealed about their true BATNA |
| `negotiation_implementation_and_relationship.md` | The deal is signed and nothing has happened: implementation obligations, early-warning signs, relationship maintenance |
| `negotiation_renegotiate_existing_agreement.md` | Reopening a live deal: change-of-circumstance case, relationship cost, exit-vs-amend, sequencing the ask |
| `negotiation_no_deal_recovery.md` | You walked or they did: preserve the option to reopen, extract the learning, execute the BATNA you priced |

### `contexts/` (8) — all new

Each is a **specialization**, not a restatement. Every one cross-links upstream to `preparation/` rather than re-deriving BATNA and interest theory.

| File | Description |
|---|---|
| `negotiation_salary_raise_promotion.md` | Comp negotiation: market evidence, the ask, band mechanics, the "we don't have budget" response, timing to review cycles |
| `negotiation_vendor_procurement_buyside.md` | Buyer-side, non-lawyer: competitive tension, total cost, lock-in as leverage, the renewal cliff |
| `negotiation_freelance_rate_conversation.md` | Defending a rate live: scope-vs-price trades, the discount request, raising rates on an existing client |
| `negotiation_sales_objection_handling.md` | Price, timing, authority, and competitor objections — diagnose the objection behind the objection |
| `negotiation_partnership_equity_split.md` | Founder and partner splits: contribution vs. future value, vesting, the conversation nobody wants to have early |
| `negotiation_internal_budget_headcount.md` | Negotiating inside your own organization for resources against peers with equal claim |
| `negotiation_customer_escalation_concession.md` | An angry customer wants something: what to concede, what it sets as precedent, when to hold |
| `negotiation_major_purchase_bargaining.md` | Vehicle, home, large one-off purchase: information asymmetry, the walk-away as the only real lever |

### `difficult-conversations/` (5) — 2 existing, 3 new

| File | Description |
|---|---|
| `difficultconvo_pre_brief.md` | *Existing.* One-page prep |
| `difficultconvo_post_review.md` | *Existing.* Debrief what happened |
| `difficultconvo_delivering_bad_news.md` | **NEW.** News you did not decide and cannot change — layoffs, cancelled projects, denied requests |
| `difficultconvo_receiving_hard_feedback.md` | **NEW.** Staying in the conversation without defending, and separating signal from delivery |
| `difficultconvo_saying_no_upward.md` | **NEW.** Declining a request from someone with power over you, with the alternative attached |

### `craft/` (4) — all new

| File | Description |
|---|---|
| `negotiation_style_self_assessment.md` | Your default mode under pressure, where it costs you, and the one adjustment worth drilling |
| `negotiation_deliberate_practice_loop.md` | A practice loop for one negotiation sub-skill (cross-links `domain-learning/learning_deliberate_practice_designer.md` rather than restating it) |
| `negotiation_pattern_library_builder.md` | Turn accumulated debriefs into a personal library of situation → move → outcome |
| `negotiation_ethics_line.md` | Where persuasion becomes manipulation: your pre-committed limits, and what to do when the other side crosses theirs |

---

## Explicitly not gaps (already covered — cross-link, never duplicate)

| Tempting addition | Already exists |
|---|---|
| Contract negotiation playbook, primary/fallback/walkaway | `domain-legal/contracts-transactional/legal_negotiation_position_paper.md`; `domain-legal/in-house-legalops/legal_playbook_builder_for_contract_type.md` |
| Mediation preparation | 6 prompts across `domain-legal/divorce/`, `domain-legal/custody/`, `domain-legal/family-self-advocacy/` |
| Boundary-setting script | `domain-personal-development/prompts/relationships/relationships_boundary_setting_script.md` **and** `domain-psychology/client-self-use/relational/clientself_boundary_setting_script.md` — already two; a third would be the worst duplication in the repo |
| Stakeholder navigation / org politics | Three exist: `domain-personal-development/prompts/stakeholder/stakeholder_navigation_guide.md`, `domain-engineering-workflows/workflows/engineering_stakeholder_navigation_guide.md`, `domain-policy/policy_stakeholder_coalition_map.md` |
| Conflict post-mortem (relational) | `difficult-conversations/difficultconvo_post_review.md` **and** `domain-psychology/client-self-use/relational/clientself_conflict_postmortem.md`. `after-the-deal/negotiation_post_negotiation_debrief.md` is the *deal* debrief and must demarcate against both |
| Live conversation role-play in character | `domain-conversation-practice/conversation_practice_simulator.md`. `preparation/negotiation_counterpart_simulation.md` models their *reasoning* as an analysis artifact, not the conversation |
| Evaluating the offer itself | `domain-personal-development/major-decisions/personal_career_offer_evaluation.md` — upstream of `contexts/negotiation_salary_raise_promotion.md` |
| Settlement valuation | `domain-legal/litigation/legal_settlement_value_range_analysis.md` |
| Setting your own price/rate before the conversation | `domain-personal-development/prompts/solo-dev/solo_dev_pricing_value_confidence.md` — upstream of `contexts/negotiation_freelance_rate_conversation.md` |
| Vendor selection (pre-negotiation diligence) | `domain-business-strategy/research/research_vendor_evaluation.md` — upstream of `contexts/negotiation_vendor_procurement_buyside.md` |
| Co-parenting counterpart tactics | `domain-parenting/caregiver-facing/co-parenting/` — the family-specific fork of hard-bargainer defense |

---

## Conventions for whoever authors from this list

1. **Match the exemplar exactly.** `preparation/negotiation_interest_mapping.md` — 196 lines, 9 steps. Do **not** copy `negotiation_batna_analysis.md`, the 283-line/13-step outlier. Target ~190 lines / 11–12 KB.
2. **Frontmatter field order is fixed:** `title` → `category` → `description` → `techniques` → `difficulty` → `tags` → `updated` → `reasoning` → `related_prompts`. No other fields appear in this domain.
3. **`category` matches the subdirectory:** `negotiation/preparation`, `negotiation/at-the-table`, `negotiation/channels`, `negotiation/multi-party`, `negotiation/after-the-deal`, `negotiation/contexts`, `negotiation/difficult-conversations`, `negotiation/craft`.
4. **The `reasoning:` block carries all 10 keys in order:** `styles, stakes, horizon, uncertainty, evidence_quality, domain_complexity, collaboration, output_format, user_role, mode`. `uncertainty: ambiguity` is a domain invariant — you are always reasoning about a counterpart whose true position is unobservable.
5. **`related_prompts` is exactly 3 entries**, repo-root-relative with the `domain-*/` prefix and `.md`. At least one intra-domain.
6. **`description` ends with the domain's signature clause** — "Counters the most common … failure: …".
7. **Six `##` headings only:** Inputs / Context · Constraints (Must / Must Not) · Instructions · False-Positive Prevention · Output Format · Verification. Objective / When to use / When NOT to use / Audience are bold-label paragraphs, never headings.
8. **Carry the domain-signature blocks:** a steelmanning clause in Must; confidence tagging on every estimate (`known / inferred / guessed`); an adversarial check as the final instruction step, mirrored in the Output Format template; a Verification checklist whose final 1–2 items are negative assertions ("No X.").
9. **Do not add** safety banners, "not legal advice" disclaimers, standalone no-fabrication boilerplate, `## Examples`, or a `## Related Prompts` body section — none appear in this domain. Legal-advice duty is routed to `domain-legal/` via the README instead. The one exception is `channels/negotiation_cross_cultural.md`, which needs an explicit guard against asserting cultural generalizations as fact.
10. Technique IDs must resolve in `techniques/MASTER_TECHNIQUE_INDEX.md`. The domain spine is `ST-01, ST-02, RT-02, DS-01, CM-02, QA-01`.
11. **After adding files:** update the README's Subdirectory map, per-subdirectory tables, and Quick routing; add routing rows to root `CLAUDE.md`; bump the count in root `README.md`; then regenerate with `python3 scripts/generate_prompt_index.py`.

---

## Wave 2 — candidate future work (not yet built)

- **Deepen `contexts/`** — landlord/tenant, insurance claim, medical bill, severance package, licensing/IP terms. Each must clear the non-duplication table first; several are close to `domain-legal/personal-self-advocacy/`.
- **Negotiation analytics** — designing a personal scorecard across many negotiations (outcome vs. reservation point, concession efficiency, walk-away rate), feeding `craft/negotiation_pattern_library_builder.md`.
- **Agent-mediated negotiation** — negotiating through a broker, recruiter, or agent, where your interests and your representative's diverge.
- **Reciprocal cross-links** — deliberately deferred in Wave 1. Adjacent prompts in `domain-personal-development/`, `domain-legal/`, and `domain-business-strategy/` do not yet point back into the new subdirectories; the repo caps `related_prompts` at 3, so adding backlinks means displacing existing ones and should be a considered pass, not a sweep.
