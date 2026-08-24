---
title: "Science Op-Ed Drafter"
category: science/public-engagement
description: "Draft an op-ed that turns a user-supplied finding into a policy-relevant argument with a transparent claim-to-implication evidence chain and disclosed standpoint."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - RT-03
  - QA-01
  - CM-02
difficulty: advanced
tags:
  - op-ed
  - science-communication
  - evidence-chain
  - policy-relevance
  - overclaim-avoidance
  - conflict-of-interest
  - values-vs-evidence
  - persuasion
updated: "2026-06-26"
related_prompts:
  - domain-science/public-engagement/science_policy_brief_drafter.md
  - domain-science/writing-communication/science_lay_summary_translator.md
  - domain-science/statistics/science_statistical_results_interpreter.md
---

# Science Op-Ed Drafter

**Objective:** Draft a persuasive op-ed that translates a finding into a policy-relevant argument while keeping the evidence chain transparent. Each step — claim → evidence → what it does and does not support → implication — is explicit, the author's standpoint and conflicts are disclosed, counterarguments are acknowledged, and the empirical science is kept distinct from the values/policy judgment.

**When to use:** When a researcher or science communicator wants to argue for attention or action on an issue in a newspaper, magazine, or platform op-ed, and the argument must rest on evidence without overclaiming.

**Required inputs:**
- **Discipline.** The scientific field grounding the argument.
- **Study type.** Observational / experimental / RCT / meta-analysis / modeling / synthesis, etc., for each finding cited.
- **The finding(s)** (user-supplied; never invented) and the audience/outlet and its readership.
- **The policy implication the author wants to argue.**

**Optional inputs:**
- The author's standpoint, role, and any conflicts of interest.
- The strongest counterarguments and who holds them.
- Effect sizes, limitations, and competing evidence.
- A desired call to action or word-count target.

**Constraints — Must:**
- Build a visible evidence chain: claim → evidence → what it does/doesn't support → implication.
- Keep the empirical claim separate from the value or policy judgment, and say which is which.
- Disclose the author's standpoint and any conflict of interest.
- Acknowledge at least one serious counterargument and respond to it fairly.
- Calibrate certainty to the evidence: correlation is not causation; one study is not settled; state effect size with a limitation.

**Constraints — Must Not:**
- Do not invent findings, statistics, quotes, citations, or certainty. Draft only from user-supplied results; mark gaps `[user-supplied]`.
- Do not use hype: "novel," "groundbreaking," "first-ever," "gold standard," "cure," "breakthrough," "proves." Substitute calibrated claims.
- Do not present the policy preference as if it were a scientific result.
- Do not omit limitations or strongest opposing evidence to strengthen the argument.

**Instructions:**

1. **Intake and classify.** Capture discipline, study type(s), the finding, audience/outlet, and the policy implication. Note the design's causal warrant.
2. **Separate science from values.** Explicitly split what the evidence shows from what the author believes should be done about it; both belong in the op-ed but must not be conflated.
3. **Construct the evidence chain.** For the central argument, lay out claim → evidence → what it does and does not support → implication, so a reader can audit each link.
4. **Write the hook and thesis.** Open with a concrete, accurate entry point; state the thesis as a policy-relevant argument grounded in (not exceeding) the evidence.
5. **Develop the body.** Carry the evidence chain through, keeping calibrated language and pairing claims with limitations.
6. **Steelman and rebut.** Present the strongest counterargument fairly, then respond without strawmanning or overclaiming.
7. **Disclose and close.** State the author's standpoint and COI, and end with a calibrated call to action that the evidence can bear.
8. **Run the evidence-chain check.** Verify every implication traces back through a supported claim and that no value judgment is dressed as a finding.
9. **Deliver.** Output the op-ed followed by the evidence-chain check.

**Output format (locked):**

```
## Op-Ed

### Headline
[accurate, policy-relevant, hype-free]

[Hook: concrete, accurate opening.]

[Thesis: policy-relevant argument grounded in the evidence.]

[Body: evidence chain carried through — claim, evidence, scope, implication — with calibrated language and limitations.]

[Counterargument: strongest opposing view, fairly stated and answered.]

[Standpoint & disclosure: author role and any conflict of interest.]

[Close: calibrated call to action.]

— [Author, affiliation]

## Evidence-Chain Check
| Link | Content | Supported by user-supplied evidence? | Science vs values |
|---|---|---|---|
| Claim | [...] | [yes / partial / user-supplied] | empirical |
| Evidence | [...] | [...] | empirical |
| Does NOT support | [...] | n/a | empirical |
| Implication | [...] | [...] | value/policy |

Check verdict: [PASS / REVISE — reasons]
```

**Reporting-standard alignment:** No formal reporting standard; aligns to science-communication best practice and the honest-broker framing (Pielke) — transparent evidence chains, separating empirical claims from value judgments, overclaim avoidance, and disclosure of standpoint/COI.

**Verification checklist (before delivering):**
- [ ] The evidence chain (claim → evidence → scope → implication) is explicit and auditable.
- [ ] Empirical claims are visibly separated from value/policy judgments.
- [ ] Author standpoint and any conflict of interest are disclosed.
- [ ] At least one serious counterargument is acknowledged and answered fairly.
- [ ] Certainty is calibrated; effect size and a limitation appear together.
- [ ] No banned hype words in the drafted op-ed.
- [ ] No invented findings, statistics, quotes, or citations; gaps marked `[user-supplied]`.
- [ ] The evidence-chain check table is completed with a PASS/REVISE verdict.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Values-as-science | A policy preference phrased as a research result | Evidence-chain check tags each link empirical vs value |
| Overreached implication | A conclusion the cited design can't bear | Require the "what it does NOT support" link before the implication |
| Strawman rebuttal | A weak version of the opposing view, easily knocked down | Require the strongest counterargument, fairly stated |
| Hidden COI | Persuasive case with undisclosed funding/interest | Mandatory standpoint + COI disclosure line |
| Cherry-picked evidence | One supportive study, contradicting evidence omitted | Require limitations and any competing evidence be surfaced |
