---
title: "Policy Implementation Feasibility — Deep Assessment of Whether a Policy Can Actually Be Operated"
category: policy/implementation
description: "Assess implementation feasibility for a policy proposal at depth: legal authority, administrative capacity, funding reality, realistic timeline benchmarked against comparable efforts, dependencies, implementation failure modes (gaming, capture, evasion, under-enforcement), and the gap between proxy 'implemented' and substantive implementation. Counters the failure of policies that are sound on paper and unoperatable in practice."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - policy
  - implementation
  - administrative-capacity
  - feasibility
  - public-administration
updated: "2026-06-18"
reasoning:
  styles: [analytic, structural, causal, adversarial]
  stakes: high
  horizon: years
  uncertainty: deep
  evidence_quality: variable
  domain_complexity: regulated
  collaboration: small_team
  output_format: structured
  user_role: [policy, analyst, executive, administrator]
  mode: [diagnose, audit, plan]
related_prompts:
  - domain-policy/policy_options_memo.md
  - domain-policy/policy_stakeholder_coalition_map.md
  - domain-policy/policy_problem_framing.md
---

# Policy Implementation Feasibility

**Objective:** Determine whether a policy proposal can actually be operated, not just passed. The implementation section of an options memo is summary-level; this assessment is deep. It works through legal authority, administrative capacity, funding reality, realistic timeline, dependencies, implementation failure modes, and the divergence between proxy metrics of "implemented" and substantive implementation. The output is a feasibility verdict with the specific conditions that must hold and the specific ways implementation tends to fail.

Most policy failure is implementation failure: the law is fine, the operation is impossible. This prompt catches that before commitment.

**When to use:**
- A policy option is being seriously considered and you need to know if it can be operated, not just legislated.
- Deepening the implementation section of a `policy_options_memo.md` for the front-running option.
- Diagnosing why an enacted policy is not producing results (often an implementation gap).
- Pressure-testing a proposal a sponsor is confident about — the confidence is usually about the policy, not the operation.

**When NOT to use:**
- You need political feasibility (can it pass) rather than operational feasibility (can it run) — use `policy_stakeholder_coalition_map.md`.
- The policy is not yet specified enough to have an implementation mechanism.
- You only need a high-level feasibility flag — the options memo's summary section is enough.

**Audience:** Policy analysts, agency leaders, program designers, legislative staff, oversight bodies, and consultants advising on whether a proposed policy is operable.

---

## Inputs / Context

1. **The policy.** Specified to the level of a mechanism: who must do what, to whom, when, enforced how.
2. **The implementing bodies.** Which agencies, levels of government, or third parties would operate it.
3. **The legal basis.** Statute, regulation, charter, or authority the policy would rely on.
4. **Resourcing.** What funding and staff exist or are proposed.
5. **Comparable efforts.** Prior or parallel implementations of similar mechanisms, here or elsewhere.
6. **The intended outcome.** What "working" means substantively, beyond compliance.

---

## Constraints

### Must
- Assess **legal authority** first: does the implementing body have the legal power to do this, or would it require new authority, and is that authority contestable?
- Assess **administrative capacity** concretely: do the agencies have the people, systems, expertise, and IT to operate this — not "could they build it" but "what exists now."
- Assess **funding reality**: is the money available, allocated, authorized-but-not-appropriated, or hypothetical? Distinguish these sharply.
- Build a **realistic timeline** benchmarked against comparable efforts, not the sponsor's optimistic schedule.
- Map **dependencies**: other rules, regulations, court cases, legislative actions, system integrations, or interagency agreements the policy waits on.
- Enumerate **implementation failure modes**: gaming, regulatory capture, evasion, under-enforcement, perverse incentives — and who exploits each.
- Define what counts as **"implemented"** substantively, and identify where the **proxy metric diverges** from real implementation (a checkbox completed vs. the outcome achieved).
- Render a **verdict** with the conditions that must hold for feasibility.

### Must Not
- Conflate "the law authorizes it" with "the agency can do it." Authority and capacity are independent.
- Treat proposed or authorized funding as available funding.
- Accept the sponsor's timeline without benchmarking against how long comparable efforts actually took.
- Assume good-faith compliance. Implementation meets actors who optimize against it.
- Treat enforcement as automatic. Under-enforcement is the default state of many enacted policies.
- Declare success at the proxy level (forms filed, rules issued) when the substantive outcome is unmet.

---

## Instructions

1. **Verify legal authority.** Identify the specific authority the implementing body would rely on. Determine whether it clearly covers the action, requires interpretation, or requires new authority. Flag litigation risk and which actors would challenge it. State whether authority is a go/no-go gate.
2. **Audit administrative capacity.** For each implementing body: current headcount and relevant expertise, IT and data systems, processing throughput, and track record operating similar programs. Identify the binding capacity constraint. Distinguish "has it," "could build it in [time/cost]," and "lacks it with no clear path."
3. **Test funding reality.** Classify the money: available now / allocated / authorized but not appropriated / proposed / hypothetical. Estimate true operating cost (not just program cost — include administration, IT, enforcement, ongoing maintenance). Identify the funding cliff or renewal risk.
4. **Benchmark the timeline.** Find comparable implementations and how long they actually took from authorization to operation to results. Build a realistic timeline with phases (standup, ramp, steady state). Show the sponsor's timeline next to the benchmarked one and explain the gap.
5. **Map dependencies.** List everything the implementation waits on: companion regulations, court rulings, legislative appropriations, interagency agreements, vendor procurements, system integrations, data-sharing arrangements. Mark which are on the critical path and which could slip.
6. **Enumerate failure modes.** For each, name the mechanism and the actor who exploits it:
   - **Gaming** — meeting the letter while defeating the intent.
   - **Capture** — the regulated shaping the regulation or enforcement.
   - **Evasion** — exiting the policy's reach (jurisdiction shopping, restructuring).
   - **Under-enforcement** — the rule exists but no one is staffed or incentivized to enforce.
   - **Perverse incentives** — the policy rewards the behavior it meant to discourage.
7. **Distinguish proxy from substantive implementation.** State the substantive outcome that means "working." Then list the proxy metrics likely to be reported (rules issued, forms processed, dollars obligated) and show where each can be fully satisfied while the substantive outcome fails.
8. **Render a feasibility verdict.** Feasible / feasible-with-conditions / infeasible-as-designed. State the conditions that must hold, the single most likely point of failure, and the design changes that would most improve feasibility.

---

## False-Positive Prevention

1. **Authority-equals-capacity error.** Concluding feasibility because the law permits it, while the agency cannot operate it. Audit capacity independently.
2. **Funding mirage.** Counting proposed or authorized funds as available. Classify every dollar by its actual status.
3. **Optimistic-timeline acceptance.** Taking the sponsor's schedule at face value. Always benchmark against how long comparable efforts took.
4. **Good-faith assumption.** Modeling implementation as if regulated actors comply rather than optimize against the rule. Name who games each provision.
5. **Enforcement-by-default fallacy.** Assuming a rule enforces itself. Identify who is staffed and incentivized to enforce, or flag under-enforcement.
6. **Proxy-success trap.** Declaring implementation complete when the reportable proxy is met but the substantive outcome is not. State the substantive bar separately.
7. **Dependency blindness.** Missing the companion regulation, court case, or interagency agreement that gates the whole effort. Map the critical path.
8. **Capacity-could-build hand-wave.** Treating "the agency could build the capability" as if it exists. Price and time the build, or call it a gap.
9. **Capture naivete.** Ignoring that the regulated industry will shape enforcement. The most sophisticated affected party usually has the most influence over how a rule is applied.
10. **Single-jurisdiction confidence.** Ignoring evasion routes (relocation, restructuring, jurisdiction shopping) available to mobile actors.

---

## Output Format

```
# IMPLEMENTATION FEASIBILITY — [policy]
Implementing body / bodies: [...]
Substantive outcome ("working" means): [...]

## Legal authority
- Authority relied on: [statute / reg / charter]
- Coverage: clear / requires interpretation / requires new authority
- Litigation risk: [who challenges, on what basis]
- Gate verdict: [go / conditional / no-go]

## Administrative capacity
| Implementing body | Headcount / expertise | Systems / IT | Throughput | Comparable track record | Verdict |
|-------------------|-----------------------|--------------|------------|-------------------------|---------|
| [...]             | [...]                 | [...]        | [...]      | [...]                   | has / could build ([time/cost]) / lacks |
Binding capacity constraint: [...]

## Funding reality
| Cost component | Estimate | Funding status |
|----------------|----------|----------------|
| Program        | [...]    | available / allocated / authorized-not-appropriated / proposed / hypothetical |
| Administration | [...]    | [...]          |
| IT / systems   | [...]    | [...]          |
| Enforcement    | [...]    | [...]          |
| Ongoing O&M    | [...]    | [...]          |
Funding cliff / renewal risk: [...]

## Timeline
| Phase | Sponsor estimate | Benchmarked estimate | Basis (comparable effort) |
|-------|------------------|----------------------|---------------------------|
| Standup | [...]          | [...]                | [...]                     |
| Ramp    | [...]          | [...]                | [...]                     |
| Results | [...]          | [...]                | [...]                     |
Gap explanation: [...]

## Dependencies
| Dependency | Type | On critical path? | Slip risk |
|------------|------|-------------------|-----------|
| [...]      | reg / court / legislation / interagency / procurement | y/n | [...] |

## Implementation failure modes
| Failure mode | Mechanism | Who exploits it | Severity | Counter-design |
|--------------|-----------|-----------------|----------|----------------|
| Gaming       | [...]     | [...]           | [...]    | [...]          |
| Capture      | [...]     | [...]           | [...]    | [...]          |
| Evasion      | [...]     | [...]           | [...]    | [...]          |
| Under-enforcement | [...] | [...]          | [...]    | [...]          |
| Perverse incentive | [...]| [...]          | [...]    | [...]          |

## Proxy vs substantive implementation
- Substantive bar: [...]
- Proxy metrics likely reported: [...]
- Divergence: [where proxy can be fully met while substance fails]

## Verdict
- Feasibility: feasible / feasible-with-conditions / infeasible-as-designed
- Conditions that must hold: [...]
- Single most likely point of failure: [...]
- Highest-leverage design change: [...]
```

---

## Verification

- [ ] Legal authority assessed as a distinct gate from capacity.
- [ ] Administrative capacity audited concretely (people, systems, throughput, track record).
- [ ] Every funding component classified by actual status, not proposed status.
- [ ] Timeline benchmarked against comparable efforts, with the sponsor gap explained.
- [ ] Dependencies mapped with critical-path flags.
- [ ] All five failure modes addressed with mechanism and exploiting actor.
- [ ] Substantive implementation bar defined and separated from proxy metrics.
- [ ] Proxy/substance divergence identified.
- [ ] Verdict rendered with conditions and the single most likely failure point.
- [ ] No authority-equals-capacity reasoning.
- [ ] No proposed-funds-as-available reasoning.
- [ ] No good-faith-compliance assumption.
