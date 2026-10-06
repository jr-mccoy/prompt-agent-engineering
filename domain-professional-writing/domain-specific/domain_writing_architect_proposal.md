---
title: "Architect RFP Response — Scored to the Evaluation Criteria, Commitments with Conditions"
category: professional-writing/domain-specific
description: "Write an architecture firm's RFP response that follows the client's evaluation criteria and weights, states schedule and cost commitments with the approvals and consultants they depend on, describes each portfolio project at the firm's actual role, and replaces unsupported ROI with a method. The writing step cited by client-services-studio's architect vertical; distinct from general services proposals (business_writing_client_engagement_proposal)."
techniques:
  - DT-05
  - CM-03
  - RT-23
  - QA-20
difficulty: advanced
tags:
  - architect-proposal
  - rfp-response
  - architecture-firm
  - design-services-proposal
  - public-sector-rfp
  - respond-to-an-rfp
updated: "2026-10-06"
related_prompts:
  - domain-professional-writing/business-writing/business_writing_client_engagement_proposal.md
  - client-services-studio/prompts/stage-5-proposal-and-sow.md
  - domain-professional-writing/business-writing/business_writing_proposal.md
---

# Architect RFP Response

**Objective:** Turn an RFP and the firm's record into a technical proposal an evaluation
panel can score high on every weighted criterion, where each promise about cost, schedule,
or performance names the condition it depends on.

**When to Use:**
- Responding to a public or institutional RFP/RFQ for design services with stated
  evaluation criteria (libraries, schools, civic, healthcare, campus work).
- A private client has issued a brief and asked several firms for proposals.
- Your draft leads with design vision while the RFP weights approach, experience, and
  schedule — and needs re-balancing.
- Running `client-services-studio/` with the architect vertical: Stage 5 assembles the
  proposal and SOW; this prompt writes the RFP-facing prose.
- **Not this prompt if** the engagement is a general professional-services proposal with
  no RFP and no design scope — use
  `domain-professional-writing/business-writing/business_writing_client_engagement_proposal.md`.
  For a persuasive internal investment case, use `business_writing_proposal.md`.

**Audience:** An evaluation panel (owner's representative, facilities staff, often a board
member or user-group lead) scoring each response against a published rubric, usually
without the chance to ask questions. They need to find each criterion answered where they
expect it, and to believe the schedule and budget statements. The principal signs the
proposal; licensed-practice, code, and contract positions are the firm's to own.

## Inputs / Context

Paste source material inside named tags and refer to it by tag name:

1. **The RFP** in `<rfp>` — scope, evaluation criteria and weights, page limit, required
   forms, submission format (including whether fee goes in a separate envelope), stated
   construction budget, target dates, required approvals.
2. **Project type** — building type, area (existing and new), key program requirements.
3. **Client priorities** — from `<rfp>` and any pre-proposal meeting notes in
   `<meeting_notes>`; quote their words.
4. **Design approach** — conceptual direction, how it meets the program; sketches named,
   not described at length.
5. **Relevant experience** in `<portfolio>` — for each project: client, year, area,
   construction cost, the firm's **role** (architect of record, design architect,
   associate, interiors only), certifications actually achieved, references.
6. **Team and consultants** — named staff with roles and hours; consultants proposed and
   whether the client or the firm appoints them.
7. **Budget and timeline** — the firm's stage durations, estimating approach, owner review
   periods, and the approvals outside the firm's control.
8. **Engagement record** in `<engagement_record>` (optional, from client-services-studio
   Stages 3–5) — stage boundaries, iterations per stage, exclusions, consent-risk
   allocation, fee. When present, scope and exclusion wording is used verbatim so the
   proposal maps to the SOW.
9. **Draft** in `<draft_proposal>` (optional).

## Method

1. **Build the criteria matrix first (DT-05).** List each evaluation criterion with its
   weight, the RFP section that defines it, and the proposal section that answers it.
   Allocate pages roughly in proportion to weight within the page limit. A criterion
   with no proposal section is a lost score; a section with no criterion is cut or moved
   to an appendix.
2. **Write "Understanding" in the client's terms.** Restate the program, site, and
   priorities using the RFP's words and the client's metrics. Name the one or two
   project risks a panel will be worried about (phasing an occupied building, approvals,
   budget), so the approach section can answer them.
3. **Define the approach as scope (CM-03).** Stages in this appointment, deliverables per
   stage, design iterations included, owner decision points, consultants and who appoints
   them, exclusions. If `<engagement_record>` is supplied, copy its stage and exclusion
   language; do not paraphrase it.
4. **State commitments with their conditions.**
   - Schedule: firm-controlled durations per stage, owner review periods, and approvals
     (planning, historic, code review) as dependencies with their owner. Compute the
     date path from notice to proceed and compare it with the RFP's target; if they
     conflict, say how you would close the gap.
   - Cost: design to the stated construction budget, with estimates at named milestones
     and a reconciliation step; never a promise about bid results.
   - Code, zoning, and approvals statements are `[VERIFY: authority having jurisdiction]`
     unless `<rfp>` states them.
5. **Tag every claim's provenance (RT-23).** Portfolio statements carry the firm's role
   from `<portfolio>`; certifications are named at the level achieved; performance and
   ROI figures need a source (energy model, measured post-occupancy data) or are replaced
   by the method that would produce them.
6. **Verify before output.** Re-read against the matrix: every criterion answered in its
   section; every date recomputed from durations; every portfolio sentence matches the
   role column; every "will" sentence is either within the firm's control or carries its
   condition. Report page count against the limit.

## Output Format

```
## Criteria matrix
| Criterion (RFP §) | Weight | Proposal section | Pages | Evidence offered |

## 1. Understanding of the project
## 2. Approach and methodology
   Stages and deliverables | Iterations | Owner decisions | Consultants | Exclusions
## 3. Cost management
## 4. Relevant experience
   | Project | Year | Firm's role | Area / cost | Relevance to this RFP |
## 5. Team
## 6. Schedule
   | Stage | Firm weeks | Owner/authority dependency | Ends |
## Claims ledger
| Claim | Source / basis | Status |
## Items for the principal before submission
```

## Verification

- [ ] Every evaluation criterion maps to a section, and page allocation follows the weights.
- [ ] No fee figures in the technical proposal if `<rfp>` requires a separate fee envelope.
- [ ] Schedule dates recompute from the stated durations and review periods.
- [ ] Every approval on the critical path names who controls it.
- [ ] Cost language commits to a process and milestones, not to bid outcomes.
- [ ] Each portfolio project states the firm's role exactly as in `<portfolio>`.
- [ ] No ROI, energy, or savings figure without a source; code statements sourced or `[VERIFY]`.

## False-Positive Prevention

1. **The eloquent wrong brief.** Six pages of design vision score well with the firm and
   poorly with a panel whose rubric gives "approach" and "experience" half the points;
   the criteria matrix is the check, not the quality of the prose.
2. **Schedule promises that ride on someone else's calendar.** "Bid documents by October"
   is a firm commitment only for the weeks the firm controls; planning-board and
   historic-commission time belongs to them, and a panel that has been burned before
   will read an unconditional date as naivety.
3. **"On budget" as a promise about the market.** The firm controls design decisions and
   estimate checkpoints, not contractor bids; a promise about the latter becomes an
   argument when bids come in.
4. **Portfolio inflation by verb.** "We designed the Harlow Community Center" when the
   firm did the interiors under another architect will be checked by a reference call,
   and one overstated role taints the whole experience section.
5. **Certification drift.** "LEED-certified library" next to a Silver plaque, or
   "designed to Net Zero" for a project never modelled, is checkable and damaging.
6. **ROI from a percentage someone remembers.** "30% energy savings, 7-year payback"
   without an energy model or measured data is invented; commit to the modelling instead.
7. **Consultant scope promised as the firm's.** MEP performance, cost estimates, or
   surveys delivered by others should be named as such, with who appoints them.

## Dual-Failure Prevention (QA-20)

- **Harmful:** the proposal wins on commitments the firm cannot keep — an unconditional
  bid date, a construction cost guarantee, a performance figure — and the firm carries
  them into a contract and a fee dispute.
- **Unhelpful:** every sentence hedged into "subject to approvals and market conditions",
  so the panel cannot score a schedule or a cost process at all, and a less careful
  competitor wins.
- **Bar:** each commitment has a number or date the panel can score *and* the single
  condition it depends on, stated once, next to it.

## Example Output

Scenario: Calder Martin Architects responds to the Town of Eastfield RFP for the Eastfield
Public Library: renovation of a 12,000 sf 1968 building and a 3,500 sf addition; construction
budget $6.2M; priorities "an accessible front door, a real children's room, a meeting room the
community can use after hours, and lower operating costs"; bid documents targeted October
2027; Planning Board site plan approval and Historic District Commission (HDC) review required;
20-page limit; fee in a separate envelope. Criteria: Understanding 20, Approach 25,
Experience 25, Team 15, Schedule 15 (= 100). `<portfolio>`: Millbrook Branch Library (2023,
architect of record, renovation + 2,800 sf addition, $4.9M, LEED Silver certified); Harlow
Community Center (2021, interiors only, prime architect Rowe Design). `<draft_proposal>`
spends 7 of 20 pages on design vision and says "we designed Harlow", "LEED Gold-level
performance", "30% energy savings with a 7-year payback", "bid-ready by June 2027 guaranteed".

```
## Criteria matrix
| Criterion (RFP §)      | Weight | Proposal section | Pages | Evidence offered |
| Understanding (4.1)    | 20     | 1                | 4     | client's priorities quoted; site risks |
| Approach (4.2)         | 25     | 2, 3             | 5     | stage plan, cost checkpoints |
| Experience (4.3)       | 25     | 4                | 5     | Millbrook (AOR); Harlow (interiors) |
| Team (4.4)             | 15     | 5                | 3     | named leads, consultant roles |
| Schedule (4.5)         | 15     | 6                | 3     | date path + dependencies |
Total 20 pages (limit 20). Design vision folded into §1–2 (draft's 7 pages → 2).

## 1. Understanding of the project
Four priorities, in the Town's words, drive every decision: an accessible front door, a
children's room, an after-hours meeting room, lower operating costs. Two risks shape the
approach: keeping a 1968 building and its HDC context intact while adding 3,500 sf, and a
$6.2M construction budget that must cover upgrades the addition may trigger in the existing
building [VERIFY: code official — existing-building code scope].

## 2. Approach and methodology
Stages in this appointment: Schematic Design (SD), Design Development (DD), Construction
Documents (CD), bidding support. Two design iterations per stage are included; further
iterations are additional services. Library Board decisions at the end of SD and DD.
Consultants appointed by Calder Martin: Northgate Engineering (MEP/FP), Ridgeline Cost
(independent estimates). Survey and geotechnical reports are appointed by the Town.
Exclusions: construction administration (separate proposal on request), furniture
procurement, hazardous-materials abatement design.

## 3. Cost management
We design to the $6.2M construction budget. Ridgeline Cost prices the design at end of SD,
end of DD and 90% CD. If an estimate exceeds the budget, we present reduction options to the
Library Board before the next stage begins. We do not control bid results; these checkpoints
are how we keep the design priced against the budget. Operating cost: we will run an energy
model at SD and agree an energy-use target with the Board at SD sign-off, in place of a
savings figure we cannot yet support (Claims ledger #3).

## 4. Relevant experience
| Project                    | Year | Firm's role          | Area / cost        | Relevance |
| Millbrook Branch Library   | 2023 | Architect of record  | reno + 2,800 sf / $4.9M | occupied-building phasing; LEED Silver certified |
| Harlow Community Center    | 2021 | Interior architect (prime: Rowe Design) | — | after-hours meeting-room layout and access control |

## 5. Team
Principal-in-charge and project architect named with hours [from staffing plan]; Northgate
and Ridgeline leads named with their roles in §2.

## 6. Schedule  (notice to proceed assumed Mon 4 Jan 2027)
| Stage                  | Firm weeks | Owner/authority dependency               | Ends |
| SD                     | 10         | —                                        | 15 Mar 2027 |
| Board SD review        | —          | Library Board, 2 wk                      | 29 Mar 2027 |
| DD                     | 12         | —                                        | 21 Jun 2027 |
| Board DD review        | —          | Library Board, 2 wk                      | 5 Jul 2027 |
| CD (incl. 90% estimate)| 16         | Planning Board + HDC approval before issue | 25 Oct 2027 |
Firm weeks 10 + 12 + 16 = 38; owner reviews 2 + 2 = 4; 42 weeks → 25 Oct 2027, inside the
October target only if approvals land before CD issue. To protect that, we propose submitting
to the Planning Board and HDC at SD sign-off [VERIFY: boards accept SD-level submissions].
Each week of approval beyond CD completion moves the bid date by a week.

## Claims ledger
| # | Claim (draft)                          | Source / basis            | Status |
| 1 | "We designed Harlow"                   | portfolio: interiors only | Rewritten to role |
| 2 | "LEED Gold-level performance"          | Millbrook certified Silver | Corrected to Silver |
| 3 | "30% savings, 7-year payback"          | none                      | Replaced by SD energy model |
| 4 | "Bid-ready by June 2027 guaranteed"    | recomputed: 25 Oct 2027   | Replaced by §6 date path |

## Items for the principal before submission
- Confirm with the code official what the addition triggers in the existing building.
- Confirm the Planning Board and HDC accept concept-level submissions (drives §6).
- Confirm reference contacts for Millbrook and for Rowe Design on Harlow.
```

## Techniques Used

- **DT-05 Element-by-Element Assessment Matrix** — the criteria matrix maps each weighted criterion to a section and page allocation before any prose is written.
- **CM-03 Scope Definition** — stages, iterations, appointments, and exclusions are stated as scope, verbatim from the engagement record when one exists.
- **RT-23 Input Provenance Tagging** — the claims ledger ties portfolio roles, certifications, and performance figures to their source or replaces them.
- **QA-20 Dual-Failure Quality Test** — commitments are tested against both overpromising and hedging until nothing is scoreable.

## Related Prompts

- `domain-professional-writing/business-writing/business_writing_client_engagement_proposal.md` — general services proposals without an RFP or design scope.
- `client-services-studio/prompts/stage-5-proposal-and-sow.md` — assembles proposal and SOW; this prompt supplies the architect-specific writing.
- `domain-professional-writing/business-writing/business_writing_proposal.md` — persuasive internal investment proposals.
