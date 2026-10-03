---
title: "Source Verification Log — People, Documents, and Images Checked, Sourcing Terms Recorded, and Corrections Traceable"
category: professional-writing/journalism
description: "Keep a reporter's verification log for a story: each human source assessed for identity, position to know, independence, and interest; each document traced for provenance and authenticated by content, form, and an independent confirmer; each image or video checked for earliest instance, location, time, and rights; sourcing terms (on the record, background, deep background, off the record) recorded at the moment they were agreed; every claim given a traffic-light status with a verbatim anchor; unknowns carried forward; and a corrections trail that shows what was published, on what basis, and what changed."
techniques:
  - IPC-07
  - IPC-11
  - RT-05
  - DP-28
difficulty: intermediate
tags:
  - journalism
  - source-verification
  - document-authentication
  - image-verification
  - sourcing-terms
  - corrections
  - verify-leaked-document
  - is-this-photo-real
  - anonymous-source-rules
updated: "2026-10-02"
related_prompts:
  - domain-professional-writing/journalism/journalism_story_desk_edit.md
  - domain-research-academic/research_manuscript_fact_check_reconciler.md
  - domain-professional-writing/writing/writing_unsourced_claim_disposition.md
---

# Source Verification Log

**Objective:** Give a reporter one living record of what is known, how it is known, and
on what terms — so that the story publishes only what was verified, the editor can see
why, a confidential source stays protected, and any correction can be traced to the
exact entry that failed.

**When to Use:**
- A tip, a leaked document, or a viral photo or video is the basis of a story.
- A story rests on sources who will not all be named.
- An editor asks "how do we know this?" and the answer is scattered across notebooks.
- A correction request arrives and you need to show what you relied on.
- **Not this prompt if** the draft is finished and you are checking each claim against
  the source set — use `domain-research-academic/research_manuscript_fact_check_reconciler.md`
  (or the `domain-agentic-resources/commands/non-coding/writing/fact_claim_verification_pass.md`
  command). For claims an author believes but cannot source, use
  `domain-professional-writing/writing/writing_unsourced_claim_disposition.md`. For the
  editor's pre-publication pass, `journalism/journalism_story_desk_edit.md`. This prompt
  verifies the **sources**, before and while the story is written.

## Inputs / Context

1. **The claims** the story needs to make, in a list.
2. **Human sources** — for each: how you know who they are, their role, how they know
   what they say, contact history, and the terms agreed.
3. **Documents** — how each reached you (and through whom), format, dates, metadata if
   available, and who else could confirm it.
4. **Images or video** — where first seen, the account that posted it, what it claims to show.
5. **Newsroom policy** on anonymity, number of sources, and corrections, if one exists.
6. **Security needs** — whether any source could be harmed by identification.

## Method

1. **Assess each human source (RT-05).**
   - *Identity:* confirmed how (met, employer directory, known contact)?
   - *Position to know:* first-hand (saw, did, holds the record) or second-hand (heard)?
   - *Independence:* two people who heard it from the same person are **one** source.
   - *Interest:* what they gain or lose; a motive does not disqualify, but it is recorded.
   - *Track record:* earlier information that checked out, or did not.
2. **Record sourcing terms when agreed.** Terms vary by outlet, so write the meaning, not
   only the label: *on the record* (name and words usable); *background* (usable,
   attributed to an agreed description); *deep background* (usable, no attribution);
   *off the record* (not usable; may guide further reporting only if both sides agreed
   that). Terms are agreed **before** the information, with date and wording; a later
   request to change terms is logged and decided by the editor, not by the reporter alone.
3. **Authenticate each document.**
   - *Provenance:* the chain from creator to you; gaps are stated.
   - *Form:* layout, letterhead, signatures, numbering, file properties — consistent with
     genuine documents from the same source?
   - *Content:* internal consistency; names, dates, and figures that match known facts.
   - *Confirmation:* an independent person in a position to know, or the organisation
     itself (asking it to confirm authenticity — weighing whether that exposes the source).
4. **Verify each image or video.** Earliest findable instance (reverse image search
   across engines); original uploader contacted; location by landmarks, signs, and
   terrain; time by shadows, weather records, and events; metadata if the original
   file is obtained (most platforms strip it); provenance credentials where present.
   Visual "AI tells" are not proof either way — provenance is. Usage rights obtained or noted.
5. **Give every claim a status with an anchor (DP-28, IPC-07).**
   - **GREEN — VERIFIED** — a primary document authenticated, or two independent first-hand sources.
   - **AMBER — SUPPORTED** — one credible first-hand source, attributable; publish only attributed.
   - **RED — UNVERIFIED** — not publishable as fact; becomes a reporting task.
   - **BLACK — CONTRADICTED** — evidence against; out of the story unless the dispute is the story.

   Each row carries a short verbatim anchor (the quote, the document line, the frame time).
6. **Carry unknowns forward (IPC-11).** Every gap gets an ID (U1, U2…) that travels into
   the draft notes and the desk edit; it closes only with a new log entry.
7. **Protect sources.** Confidential identities are kept in a separate, access-limited
   record, referred to here by code; metadata is scrubbed from any document before it is
   published or shared; the log itself is treated as sensitive.
8. **Keep the corrections trail.** On publication, snapshot each published claim's status.
   On a challenge: find the row, re-verify, and record the outcome — *correction* (fact
   wrong), *clarification* (fact right, misleading), or *no change* (with reason) — with
   date and the wording appended to the story. No silent edits.

## Output Format

```
# Verification log — [story slug]   Updated: [date]   Editor: [..]

## Sources
| Code | Who (or description) | Identity confirmed how | Position to know | Independent of | Interest | Terms (agreed when, exact wording) |

## Documents
| Doc | Provenance chain | Form check | Content check | Independent confirmation | Status |

## Images / video
| Item | Earliest instance | Uploader contact | Location | Time | Rights | Status |

## Claims
| # | Claim | Status | Basis (codes) | Anchor (verbatim) | Attribution in copy |

## Unknowns (carried forward)
| ID | Gap | Blocks claim # | Next step | Owner |

## Corrections trail
| Date | Claim # | Challenge | Re-verification | Outcome | Published wording |
```

## Verification

- [ ] Every claim the story makes has a row, a status, and a verbatim anchor.
- [ ] No two sources are counted as independent when they share an origin.
- [ ] Every terms entry records when and in what words it was agreed.
- [ ] Every document shows provenance, form, content, and confirmation checks — or the gap.
- [ ] No RED or BLACK claim appears as fact in the draft.
- [ ] Confidential identities appear only as codes.

## False-Positive Prevention

1. **A document's existence is not its authenticity.** A convincing PDF is a lead until
   the provenance and an independent confirmer say otherwise.
2. **Repetition is not corroboration.** Five outlets citing one original source are one source.
3. **Motive is not falsehood.** A disgruntled former employee can be right; record the
   interest and verify the claim.
4. **"Off the record" is not universal.** If the meaning was not agreed, the log says
   "terms unclear" and the editor decides before use.
5. **No visual detector settles an image.** Absence of artefacts does not make a picture
   real, and their presence does not make it fake.
6. **A correction log is not an admission of failure.** Logging a clarification that
   turned out unnecessary is still correct practice.

## Example Output

Scenario: a regional hospital's leaked internal memo says 40 nursing posts will be cut;
a nurse (deep background) and a former HR manager (background) describe it; a photo of
a staff protest circulates on social media.

```
# Verification log — hospital-nursing-cuts   Updated: 2026-10-02   Editor: L. Chen

## Sources
| N1 | ward nurse, 8 yrs | met in person; staff badge seen | first-hand: attended 09-24 briefing | — | union member | deep background, 09-25, "you can use it, don't attribute it at all" |
| H1 | former HR manager | LinkedIn + ex-colleague | second-hand: told by current HR staff | not of N1 | left on bad terms | background, 09-26, "a former HR manager" |

## Documents
| Memo "Workforce plan Q4" | N1 → reporter by hand, 09-25; N1 got it from a ward manager (gap: not seen by us) |
  hospital template, page numbers, director signature match 2025 annual report |
  ward names and bed counts match public board papers | hospital press office asked 09-30
  to confirm authenticity: "we don't comment on leaked documents" — not a denial | AMBER |

## Images / video
| Protest photo | earliest: staff group page 09-27 18:02 | poster replied, took it, grants use |
  hospital's east entrance (signage matches Street View) | 09-27 evening (union event notice) | permission by email | GREEN |

## Claims
| 1 | Hospital plans to cut 40 nursing posts | AMBER | memo + N1 | memo p.2: "reduction of 40.0 WTE registered nursing" | "according to an internal memo seen by [outlet]" |
| 2 | Staff were told at a 09-24 briefing | GREEN | N1 + second attendee N2 | N1: "matron read it out at 2" | "staff were told at a briefing" |
| 3 | Cuts will close Ward 7 | RED | H1 only, second-hand | H1: "I heard Ward 7 goes" | not in story |

## Unknowns
| U1 | memo authenticity unconfirmed by an independent insider | claim 1 | ask a board member | reporter |
| U2 | Ward 7 | claim 3 | board papers due 10-08 | reporter |

## Corrections trail
(none yet — status snapshot taken at publication)
```

## Techniques Used

- **IPC-07 Verbatim Source Anchoring** — every claim row carries the exact quote, line, or frame it rests on.
- **IPC-11 Propagating Ignorance Channels** — unknowns get IDs that travel into the draft and desk edit until closed.
- **RT-05 Evidence-Based Reasoning** — identity, position to know, independence, and interest assessed per source.
- **DP-28 Traffic-Light Verdict System** — verified / supported / unverified / contradicted with fixed criteria.

## Related Prompts

- `domain-professional-writing/journalism/journalism_story_desk_edit.md` — the editor's pass that reads this log.
- `domain-research-academic/research_manuscript_fact_check_reconciler.md` — checking a finished draft against its sources.
- `domain-professional-writing/writing/writing_unsourced_claim_disposition.md` — claims believed but not sourced.
