---
title: "Rule 30(b)(6) Deposition Notice Drafter"
category: legal/discovery
description: "Draft the Rule 30(b)(6) (or state-analog) notice itself — topics described with reasonable particularity and mapped to claim elements, definitions, time period, logistics, and a conferral agenda — as the upstream companion to the 30(b)(6) examination outline, which assumes the topics already exist."
techniques:
  - CM-03
  - DT-05
  - QA-02
  - ST-03
difficulty: advanced
tags:
  - legal
  - discovery
  - 30b6
  - deposition-notice
  - corporate-representative
  - depose-a-company
  - who-speaks-for-the-company
updated: "2026-09-24"
related_prompts:
  - domain-legal/depositions/legal_deposition_outline_30b6.md
  - domain-legal/discovery/legal_document_request_drafter.md
  - domain-legal/discovery/legal_meet_and_confer_letter.md
---

# Rule 30(b)(6) Deposition Notice Drafter

**Objective:** Produce a notice whose topics an entity cannot credibly call vague or overbroad and whose answers will actually close proof gaps: each topic tied to an element or defense, bounded by time and subject, drafted so a designee can be prepared on it, and paired with an agenda for the conferral the rule contemplates.

> **Scope guard — attorney-facing.** For litigation counsel noticing an organizational party (or, by subpoena, a nonparty organization). It does not examine the witness and does not decide whether a deposition is worth its cost. A self-represented party should route to `domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md`.

## When to Use

- Written discovery has left gaps that only the entity's binding knowledge can fill (policies, systems, corporate decisions, document provenance).
- You need to establish authenticity, business-record foundation, or preservation facts efficiently.
- The opposing entity has objected to a prior notice and you are re-serving narrower topics.

**Not this prompt if:**
- The notice is served and you need the examination itself — use `domain-legal/depositions/legal_deposition_outline_30b6.md`.
- You are deposing an individual in their personal capacity — use `domain-legal/depositions/legal_deposition_outline_witness.md` and an ordinary notice.
- You are the *receiving* entity objecting to topics — use `domain-legal/discovery/legal_motion_for_protective_order_drafter.md` or `domain-legal/discovery/legal_discovery_response_objections.md`.

## Inputs

- **Jurisdiction and court (required):** Forum, the operative rule (FRCP 30(b)(6) or state analog), and any local rule, standing order, or case-management order on deposition limits.
- **Case posture:** Caption, claims and defenses, discovery cutoff, depositions already taken, and any limit on number or hours of depositions.
- **Proof gaps:** For each element or defense you need to prove or rebut, what the entity knows that written discovery has not supplied.
- **Prior discovery:** Interrogatory responses, document productions (Bates ranges), and prior objections the entity made to topics or requests.
- **Deponent entity:** Party or nonparty; if nonparty, confirm a subpoena will accompany the notice.
- **Logistics:** Proposed date, location or remote platform, recording method (stenographic, audiovisual), interpreter needs.
- **Companion documents:** Whether to attach a document request under the rule allowing requests to accompany a party-deponent notice `[VERIFY: FRCP 30(b)(2) / state analog]`.

## Method

**Ground rules:** Do not invent case law on topic particularity, "contention topics," or time allotment; use `[CITE: proposition]` / `[NEED HOLDING: …]`. Any number (hours, topic limits, notice period) that the user did not supply is `[VERIFY: …]`. Draft for the stated forum only.

1. **Build the gap-to-topic map first.** List each element/defense, the fact the entity holds, and why written discovery did not resolve it. No topic without a row; no row without a topic.
2. **Draft each topic for preparability.** A topic must tell the entity whom to talk to and what to read. Use a subject + scope + time frame + system/document anchor pattern (e.g., "The criteria Defendant used from January 2023 through June 2025 to approve or deny warranty claims for the Model 7 compressor, including the written policies identified at DEF-004410–4482"). Avoid "including but not limited to" chains and "all facts supporting" formulations, which courts in many forums treat as contention discovery better suited to interrogatories `[VERIFY: forum practice]`.
3. **Add foundation topics deliberately.** Document authenticity, business-record foundation, data-system structure, search and collection methodology, and preservation — only those your case needs.
4. **Draft definitions sparingly.** Define only terms used in topics; do not import a 40-term definitions section from the document requests.
5. **Stress-test each topic as opposing counsel.** For every topic, write the strongest objection (vague, overbroad, duplicative, privileged, disproportionate, seeks legal conclusion) and revise until the objection is weak. Record the objection you anticipate anyway.
6. **Handle privilege-adjacent topics.** Topics about investigations, litigation holds, or attorney-involved decisions should target facts and dates, not advice or work product.
7. **Assemble the notice.** Caption; the notice paragraph naming the entity and the rule; the description of the entity's obligation to designate and prepare; date, time, place, recording method; topics; any attached document requests; signature and certificate of service.
8. **Draft the conferral agenda.** The rule contemplates that the parties confer about the topics and the identity of designees `[VERIFY: current text of FRCP 30(b)(6) or analog]`; list, per topic, where you can narrow and where you will hold firm.

## Output Format

```markdown
# Rule 30(b)(6) Notice Package — {Caption} — Deponent: {Entity}

## 1. Gap-to-Topic Map (internal — work product)
| # | Element / defense | Fact the entity holds | Why written discovery did not resolve it | Topic # |

## 2. Notice (service-ready draft)
{Caption}
NOTICE OF DEPOSITION OF {ENTITY} PURSUANT TO {RULE}
{notice paragraph; designation and preparation obligation; date/time/place; recording method}
### Definitions
### Matters for Examination
1. {topic}
2. ...
### Documents to Be Produced (if any)
{signature block; certificate of service}

## 3. Topic Stress Test (internal)
| Topic # | Strongest objection | Revision made | Residual risk |

## 4. Conferral Agenda
| Topic # | Can narrow to | Will not narrow because | Designee questions to ask |

## 5. Verification Items
```

## Verification

- [ ] Jurisdiction lock: rule, local rules, and deposition limits tied to the stated forum; unknown numbers marked `[VERIFY]`.
- [ ] Citation discipline: no invented authority on particularity, contention topics, or duration.
- [ ] Scope discipline: the package drafts the notice and conferral plan; it does not script the examination.
- [ ] Every topic traces to a gap-map row, and every row has a topic.
- [ ] Each topic has a subject, a time frame, and an anchor a designee could prepare from.
- [ ] No topic seeks legal conclusions, privileged advice, or "all facts supporting" contentions without a flagged reason.
- [ ] Nonparty entity paired with a subpoena; party entity's document requests comply with the forum's timing rule `[VERIFY]`.
- [ ] Topic count and expected hours fit any deposition limit in the case-management order.

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Copying RFP categories into topics ("all documents concerning…") | Topics describe *matters for testimony*; rewrite as knowledge the entity must prepare |
| Sweeping "including but not limited to" topics | Bound by subject, time, and anchor; list inclusions only if exhaustive |
| Contention topics that belong in interrogatories | Target facts and decisions; flag any contention topic for attorney decision |
| Omitting the time period | Every topic states a date range tied to the claims |
| Forgetting a nonparty needs a subpoena | Flag and cross-reference `domain-legal/discovery/legal_subpoena_drafter.md` |
| No plan for conferral | Output always includes the negotiation agenda |

## Example

**Input sketch:** Federal court; plaintiff Linwood Bakeries (fictional) sues equipment maker Oreland Ovens Inc. for breach of warranty. Gap: Oreland's interrogatory answer says warranty denials follow "standard criteria" but produces no criteria document. Also need authenticity of service tickets produced at ORE-1100–1390.

**Output (abridged):**

> **Gap map row 1.** Element: breach of warranty — denial was contrary to warranty terms. Entity fact: the criteria actually applied. Unresolved because: Interrogatory No. 6 response refers to "standard criteria" without identifying them. → Topic 1.
>
> **Topic 1.** "The criteria Oreland used from March 2024 through the date of this notice to evaluate warranty claims on Series 400 convection ovens, including who applied them, where they are recorded, and any changes to them during that period."
>
> **Topic 3.** "The creation, maintenance, and retrieval of the service tickets produced at ORE-1100–1390, including the system in which they are kept and whether entries are made at or near the time of the service visit."
>
> **Stress test, Topic 1.** Anticipated objection: overbroad as to "any changes." Revision: limited to Series 400 ovens. Residual risk: low.
>
> **Conferral agenda, Topic 3.** Can narrow to: a stipulation of authenticity and business-record status in lieu of testimony. Will not narrow: system description if the stipulation is refused.
