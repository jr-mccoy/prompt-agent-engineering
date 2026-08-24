---
title: "Legal Issue Spotter from a Fact Pattern"
category: legal/research
description: "Read a fact pattern and produce a ranked, jurisdiction-aware issue list with claims, defenses, elements at issue, and the facts that drive each."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - legal
  - research
  - issue-spotting
  - case-analysis
  - irac
updated: "2026-05-08"
related_prompts:
  - domain-legal/research/legal_research_memo_irac.md
  - domain-legal/research/legal_precedent_comparison_table.md
  - domain-legal/litigation/legal_case_strategy_assessment.md
---

**Purpose:** Convert a raw fact pattern into a structured issue list a junior associate could hand to a senior on day one of a matter. Each issue includes the claim or defense, the elements actually in dispute, the driving facts, the controlling jurisdiction, and an initial assessment of strength.

**When to use:** New matter intake, hypothetical analysis, exam-style fact patterns, pre-engagement triage, or whenever you have facts but not yet a theory of the case.

---

## Your Input

- **Jurisdiction:** [State and venue, federal court and circuit, or "unknown — flag jurisdictional questions"]
- **Posture:** [Pre-litigation / pleading / discovery / dispositive motion / appeal / advisory]
- **Client / role:** [Plaintiff / defendant / target / acquirer / employee / employer / etc.]
- **Fact pattern:** [Free text — chronology, parties, communications, transactions, harm]
- **Documents available:** [Contracts, emails, policies, regulations — or none yet]
- **What the client wants:** [Damages / injunction / dismissal / clean exit / negotiated resolution]
- **What I already suspect:** [Optional — your starting theory; the model should not anchor to it]
- **Statute of limitations clock:** [Known dates and any tolling facts]

---

## Constraints

**Must:**
- Identify both offensive (claims) and defensive (affirmative defenses, immunities, procedural bars) issues.
- For each issue, list the elements of the claim/defense and mark which are contested, conceded, or unknown.
- Tie every contested element to specific facts from the input.
- Identify limitations, notice, exhaustion, jurisdictional, and standing issues separately — these often dispose of cases before merits.
- Flag jurisdictional and choice-of-law questions if the facts are multi-state or cross-border.
- Rank issues by a combination of (a) likelihood of success and (b) potential impact, and explain the ranking.

**Must Not:**
- Invent facts, parties, dates, or documents that were not supplied.
- Cite specific cases, statutes, or rules unless the user supplied them. If authority would normally be cited here, write `[CITE: governing standard for {issue}]` so the user knows where to drop in their research.
- Treat one jurisdiction's rule as universal. If the user's jurisdiction is unstated, list issues that vary by jurisdiction with a `[jurisdiction-dependent]` tag.
- Collapse separate issues into one (e.g., breach of contract and breach of the implied covenant are not the same issue even when they ride on the same facts).
- Score "strength" without naming the factual or doctrinal driver of the score.

---

## Instructions

1. Read the fact pattern. Build a chronology if dates and events are dense enough to need one.
2. Inventory every potential claim and defense — including ones the user did not ask about. Err on the side of over-including; you will rank later.
3. For each candidate issue, list the elements. Mark each element: **Met** / **Disputed** / **Unknown** / **Likely-not-met**.
4. For each disputed or unknown element, name the specific fact(s) in the pattern that drive the dispute and the additional discovery or research needed to resolve it.
5. Separately list **threshold** issues: subject-matter jurisdiction, personal jurisdiction, venue, standing, limitations, exhaustion, notice, mandatory pre-suit procedures, arbitration/forum-selection clauses.
6. Flag any **multi-jurisdiction or choice-of-law** issues with the conflict that needs to be resolved.
7. Rank issues by the combination of likelihood of success on the merits and dispositional/strategic impact.
8. End with **Top 3 to research first** with a one-sentence rationale each.

---

## Output Format

```markdown
## Matter Summary
- Jurisdiction (assumed / supplied): {...}
- Posture: {...}
- Client role: {...}
- Likely controlling law: {...} [or jurisdiction-dependent if unclear]

## Chronology (if useful)
| Date | Event | Source in input |
|------|-------|-----------------|

## Threshold / Procedural Issues
| Issue | Status | Driving facts | Action needed |
|-------|--------|---------------|----------------|
| Subject-matter jurisdiction | ... | ... | ... |
| Personal jurisdiction | ... | ... | ... |
| Venue / forum-selection | ... | ... | ... |
| Standing | ... | ... | ... |
| Statute of limitations | ... | ... | ... |
| Exhaustion / notice / pre-suit | ... | ... | ... |
| Arbitration clause | ... | ... | ... |

## Substantive Issues — Offensive (Potential Claims)

### Issue 1: {Claim name}
- Elements:
  1. {Element} — Met / Disputed / Unknown — {fact tie}
  2. ...
- Driving facts: {bullet list}
- Open factual questions: {bullet list}
- Open legal questions: {bullet list with [CITE: ...] placeholders}
- Initial strength: {Strong / Moderate / Weak / Cannot assess yet} — because {reason}
- Damages or remedy theory: {...}

### Issue 2: ...

## Substantive Issues — Defensive (Affirmative Defenses, Immunities, Bars)

### Defense 1: {...}
- Elements / requirements
- Driving facts
- Open questions
- Strength

## Choice of Law / Multi-Jurisdiction Flags
- {Conflict and which jurisdictions' law could apply}

## Ranked Issue List
| Rank | Issue | Type | Strength | Dispositional impact | Why ranked here |
|------|-------|------|----------|----------------------|-----------------|

## Top 3 to Research First
1. {Issue} — {one-sentence rationale}
2. ...
3. ...

## Information Needed Before Next Step
- Documents: {...}
- Witnesses to interview: {...}
- Discovery to issue: {...}
- Research questions: {...}
```

---

## Verification

- [ ] Every contested element cites specific facts from the input.
- [ ] No case names, statutory sections, or rule numbers appear unless supplied by the user; otherwise `[CITE: ...]` placeholders are used.
- [ ] Threshold and procedural issues are listed separately from merits.
- [ ] Choice-of-law / multi-jurisdiction conflicts flagged when applicable.
- [ ] Defensive issues included even if user framed the matter offensively.
- [ ] Ranking explains the "why," not just the score.
- [ ] No invented facts, parties, dates, or documents.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Treating "breach of contract" and "breach of implied covenant" as one issue | Separate; the implied covenant has its own elements and is jurisdiction-dependent |
| Skipping limitations because "it's probably fine" | Always compute the running limitations period; tolling is fact-specific |
| Defaulting to federal common law | Identify the governing-law question explicitly when the parties or events are multi-state |
| Listing a claim without naming its disputed elements | Useless to a senior — every claim must show which elements are actually contested |
| Filling in citations the model "remembers" | Use `[CITE: ...]` placeholders only — do not generate case names or pinpoints |
| Forgetting standing in non-traditional plaintiffs | Organizational, third-party, taxpayer, and qui tam standing are distinct doctrines |
| Conflating personal jurisdiction with venue | Different doctrines, different waivers, different remedies |
