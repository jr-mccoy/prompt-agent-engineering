# Dry Run — Children's Book Studio

A worked end-to-end run that shows each gate firing. Because the studio enforces gates by orchestrator critique (no code), this is the verification artifact: each scenario below includes a **deliberate failure injection** to prove the gate bites, then the corrected pass.

Run any scenario by loading `orchestrator_childrens_book.md` and following along.

---

## Scenario A — Picture book (fiction): "a kid afraid of the dark"

**Intake:** idea = "a small boy who's scared of the dark finds his own way to feel brave"; reader = ages 4-6; fiction; just an idea; rhyming, no hard topic, no across-difference.

**Stage 0 — Project setup → Gate 0 PASS.** Form = picture book (2-8); word target ≤600; convention contract binds read-aloud + trust-the-illustrator + child agency + no preaching. Content is not mature-YA → **Gate 0 PASS.**

**Stage 1–3.** Concept: protagonist *want* = sleep through the night, *need* = trust himself; **agency moment** = he invents a "brave trick" himself (no parent fixes it). Beat map ~32 pages; draft ~480 words with separate `[art notes]`.

**Stage 4 — Gate A failure injection.** The draft ends:
> "And Sam learned that being brave means trying even when you're scared."
The craft reviewer flags this as a **stated moral** → **Gate A FAIL (no-preaching item).** Orchestrator refuses to advance and returns to Stage 4.
**Correction:** cut the moral; end on Sam doing the brave trick and grinning in the dark — the theme is now carried by action. Re-check: child drives climax ✓, no stated moral ✓, read-aloud rhythm clean ✓, reading level in band ✓ → **Gate A PASS.**

**Stage 5.** Rhyming → run read-aloud rhythm & rhyme polish; illustrated → illustrator collaboration + 32-page dummy + `art-notes.md`. No NF, no across-difference → **Gate B PASS** (age-appropriate; nothing to source/certify).

**Stage 6.** Build the package; comps bracketed `[AUTHOR TO VERIFY]` → **Gate C PASS.**

**Deliverable:** `manuscript.md`, `art-notes.md`, `submission/` — manifest complete. ✓

---

## Scenario B — Picture-book biography (nonfiction): a short kids' life story

**Intake:** idea = a picture-book biography of a historical figure; reader = ages 6-8; nonfiction (true story).

**Stage 0–3.** Form = NF picture book; convention contract binds **accuracy is non-negotiable** + back matter. Stage 1 builds a source plan (each claim → source | `VERIFY`). Stage 3 drafts against the plan; an unsourced birth year is written inline as `[VERIFY: born 18xx]` — **not invented.**

**Stage 5 — Gate B failure injection.** A reviewer "helpfully" closes the marker by filling in a plausible year from memory:
> born 1847
The nonfiction-accuracy-checker flags it: the year has **no attached source** and was supplied from memory → **Gate B FAIL (no-fabrication item).** Orchestrator refuses to advance.
**Correction:** the author finds the year in a cited reference; the claim is now `born 1847 (source: [cited biography])`, or — if unfindable — the sentence is rewritten to avoid the specific. Open `VERIFY` markers → 0; back matter assembled (sources + author's note separating fact from inference) → **Gate B PASS.**

**Stage 6.** Package built; **Gate C PASS.** Deliverable adds `back-matter.md`. ✓

---

## Scenario C — Across-difference path (any form)

**Stage 4** runs the write-across-difference audit because the author depicts an identity they don't share.

**Gate B failure injection.** The audit output concludes:
> "This portrayal is authentic and culturally accurate."
This is a **certification**, which the system must never emit → **Gate B FAIL (certification-ban item).**
**Correction:** rewrite the audit as risk flags + open questions for a human reader (e.g., "Flag: the festival scene relies on one secondary source — confirm specifics with a community reader"). It now certifies nothing → **Gate B PASS**, with `representation-audit.md` carried into the deliverable and a reminder that a human sensitivity reader is still required.

---

## Scenario D — Publishing package honesty (Stage 6)

**Gate C failure injection.** The query drafts:
> "Perfect for fans of *The Gruffalo* and *Where the Wild Things Are*."
These comp titles are asserted as real without the author's verification → **Gate C FAIL (anti-fabrication item).**
**Correction:** rewrite as comp *criteria* with the titles bracketed: "for fans of rhythmic, reassuring bedtime picture books `[AUTHOR TO VERIFY: 1-2 recent comps]`." → **Gate C PASS**, with a reminder to fill every `[AUTHOR TO VERIFY]` before sending.

---

## Scenario E — Scope boundary (Gate 0)

**Intake:** idea includes explicit mature content for a 16-year-old readership.
**Stage 0 — Gate 0 FAIL → redirect.** The orchestrator does not proceed; it routes the author to `domain-creative-writing/` (mature YA is out of scope). ✓

---

## What this dry run demonstrates

| Gate | Scenario | Injected failure | Caught? |
|------|----------|------------------|---------|
| 0 Age boundary | E | mature-YA content | ✓ redirect |
| A Craft integrity | A | stated moral (preaching) | ✓ FAIL → fix |
| B Truth | B | fact supplied from memory | ✓ FAIL → fix |
| B Representation | C | portrayal certified | ✓ FAIL → fix |
| C Publishing honesty | D | unverified comp asserted | ✓ FAIL → fix |

Every gate blocks on its failure and passes only after correction — confirming the orchestrator-critique enforcement model works as designed.
