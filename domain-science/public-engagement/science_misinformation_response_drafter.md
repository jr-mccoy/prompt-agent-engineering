---
title: "Misinformation Response Drafter"
category: science/public-engagement
description: "Drafts a response to public scientific misinformation using inoculation and debunking best practice — fact-first, myth labeled once, fallacy exposed, fact reinforced — and decides when not to respond."
techniques:
  - ST-01
  - ST-03
  - RT-03
  - QA-01
  - QA-02
  - CM-02
difficulty: advanced
tags:
  - misinformation
  - debunking
  - inoculation
  - prebunking
  - truth-sandwich
  - science-communication
  - fact-myth-fallacy-fact
  - public-engagement
updated: "2026-06-26"
related_prompts:
  - domain-science/public-engagement/science_social_media_thread_drafter.md
  - domain-science/public-engagement/science_explainer_for_general_audience.md
  - domain-science/writing-communication/science_lay_summary_translator.md
---

# Misinformation Response Drafter

**Objective:** Draft a response to a piece of public scientific misinformation using the Debunking Handbook structure — fact–myth–fallacy–fact (the "truth sandwich"). The response leads with the accurate fact, states the myth once and clearly labeled, exposes the rhetorical fallacy or manipulation technique, and reinforces the fact — without amplifying or over-repeating the falsehood. It also includes an explicit decision on whether to respond at all, since amplifying a fringe claim can do more harm than ignoring it.

**When to use:** A false or misleading scientific claim is circulating and you are considering a public correction (post, FAQ, statement, comment). You want a draft that corrects effectively, avoids the familiarity backfire, represents the other side fairly, and matches the audience's tone.

**Required inputs:**
- **Discipline.** <field the claim touches, e.g., vaccines/immunology, climate, nutrition>
- **Study type.** <basis of the corrective evidence: observational / experimental / modeling / systematic review / consensus body>
- **The finding(s) / claim** (user-supplied; never invented) — both the accurate fact you can support AND the misinformation claim as actually stated — plus the audience/forum.
- **Reach of the misinformation.** <how widely it's spreading; is it fringe or mainstream?>

**Optional inputs:**
- The specific source or spreader (to assess amplification risk; do not fabricate quotes).
- The manipulation technique you suspect (cherry-picking, false expert, conspiratorial reasoning, false balance, etc.).
- Audience's likely prior beliefs and emotional stake.
- Conflicts of interest to disclose.
- Length/platform constraints.

**Constraints — Must:**
- Structure the response fact–myth–fallacy–fact: lead with the fact, state the myth once with a clear "this is false" label, name the fallacy/technique, close by reinforcing the fact (truth sandwich).
- First, run a respond / do-not-respond decision based on reach and amplification risk; recommend silence (or a non-amplifying alternative) when responding would spread a fringe claim.
- Represent the misinformation and its proponents accurately; correct the claim, do not caricature the people.
- Calibrate the corrective claim (consensus vs. single study; what the evidence does and does not establish).
- Match tone to the audience: correct, do not condescend; avoid ridicule and dunking.
- Disclose conflicts of interest where relevant; link primary sources for the fact.

**Constraints — Must Not:**
- Do not invent findings, statistics, quotes, citations, or opponents' positions. Draft only from user-supplied facts; mark gaps `[user-supplied]`. Do not fabricate claims about who said what.
- Do not use hype language ("novel," "groundbreaking," "first-ever," "gold standard," "cure," "breakthrough," "proves") in the drafted response.
- Do not repeat the myth more than necessary, headline it, or place it before the fact (familiarity backfire risk).
- Do not overstate the certainty of the correction or imply the science is more settled than it is.

**Instructions:**

1. **Confirm the claim pair.** Restate the discipline, study type, the user-supplied accurate fact, the user-supplied misinformation claim as actually stated, the audience/forum, and the reach. Mark gaps `[user-supplied]`.
2. **Decide whether to respond.** Weigh the misinformation's current reach against the amplification a public response would create. If the claim is fringe and a response would spread it, recommend not responding (or a quieter alternative: a one-time FAQ, a prebunk, addressing the underlying concern without naming the claim). State the recommendation and rationale.
3. **Lead with the fact.** Draft the opening as the accurate, calibrated fact in plain language — the first thing the reader sees.
4. **State the myth once, labeled.** Present the misinformation a single time, clearly marked as false, without giving it a memorable headline.
5. **Expose the fallacy.** Name the manipulation technique driving the myth (cherry-picking, fake expert, false balance, conspiratorial reasoning, etc.) and explain in one or two sentences how it misleads — this is the inoculation/prebunk that helps readers resist similar claims.
6. **Reinforce the fact.** Close by restating the accurate fact so the reader's last impression is the truth, not the myth (completing the sandwich), with a primary-source link.
7. **Set tone and disclose.** Tune the register to the audience — respectful, not condescending; remove ridicule. Add COI disclosure if relevant. Represent proponents fairly.
8. **Run the backfire-risk check.** Verify: fact comes first; myth appears once and labeled; no fabricated positions; no hype; no over-repetition; calibration intact; tone non-condescending.

**Output format (locked):**

```
## Claim Pair (confirmed)
- Discipline / study type:
- Accurate fact (user-supplied):
- Misinformation claim, as stated (user-supplied):
- Audience / forum / reach:

## Respond or Not?
- Recommendation: [respond / do not respond / quieter alternative]
- Rationale (reach vs. amplification):

## Drafted Response (Fact–Myth–Fallacy–Fact)
**Fact (lead):** [accurate, calibrated fact]
**Myth (stated once, labeled false):** [myth]
**Fallacy / technique:** [name + how it misleads — the inoculation]
**Fact (reinforce):** [restate the fact + primary-source link]
**Tone / disclosure note:** [audience match; COI if any]

## Backfire-Risk Check ("Did I avoid the backfire risks?")
| Check | Pass? |
|---|---|
| Fact leads (not the myth) |  |
| Myth stated only once and labeled false |  |
| Fallacy/technique named (inoculation present) |  |
| Proponents represented fairly, not caricatured |  |
| No hype; correction calibrated |  |
| Tone corrects without condescending |  |
| No fabricated quotes/positions/stats |  |
```

**Reporting-standard alignment:** Aligns to the Debunking Handbook (fact–myth–fallacy–fact structure; lead with the fact to avoid the familiarity backfire effect; the "truth sandwich") and to inoculation theory / prebunking (exposing the manipulation technique so audiences can resist similar misinformation). Also follows the science-communication norm of not amplifying fringe falsehoods.

**Verification checklist (before delivering):**
- [ ] A respond / do-not-respond decision is made with a reach-vs-amplification rationale.
- [ ] The response leads with the accurate fact, not the myth.
- [ ] The myth is stated once, clearly labeled false, and not headlined.
- [ ] The fallacy/manipulation technique is named and briefly explained (inoculation present).
- [ ] The response closes by reinforcing the fact (truth sandwich) with a primary-source link.
- [ ] The correction is calibrated; no hype words appear.
- [ ] Proponents' positions are represented accurately; no fabricated quotes or claims about who said what.
- [ ] Tone corrects without condescending; backfire-risk check is completed.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Familiarity backfire | A correction that opens by quoting the myth, making it more memorable | Fact-first structure; myth stated once, mid-response, labeled false |
| Amplifying a fringe claim | A thorough rebuttal that hands a tiny claim a large new audience | Respond/do-not-respond gate weighing reach vs. amplification; offer a quieter alternative |
| Strawmanning | A "fair" summary of the myth that's easier to knock down than what proponents actually said | Represent the claim as user-supplied/as actually stated; do not fabricate or exaggerate positions |
| Overcorrection | Claiming the science is fully settled when the corrective evidence is partial | Calibrate the fact; ban "proves"; distinguish consensus from single study |
| Condescension / dunking | A correct-but-mocking tone that hardens the audience against the fact | Tone match to audience; remove ridicule; correct claims, not people |
```
