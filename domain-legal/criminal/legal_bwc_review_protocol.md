---
title: "Body-Worn Camera Review Protocol — Inconsistencies, Exculpatory Content, and Suppression Hooks"
category: legal/criminal
description: "Systematically review body-worn camera (and dash-cam) footage in a criminal case: inventory and completeness check, time-synced event log, report-versus-video inconsistency table, exculpatory and impeachment content, suppression hooks, and missing-footage follow-up — grounded only in timestamps the reviewer actually logs."
techniques:
  - ST-02
  - ST-03
  - RT-05
  - IPC-07
  - QA-01
difficulty: intermediate
tags:
  - legal
  - criminal
  - body-worn-camera
  - video-evidence
  - impeachment
  - discovery-review
updated: "2026-09-24"
related_prompts:
  - domain-legal/criminal/legal_motion_to_suppress.md
  - domain-legal/criminal/legal_brady_giglio_review_request.md
  - domain-legal/discovery/legal_document_review_coding_taxonomy.md
  - domain-legal/depositions/legal_deposition_summary.md
---

**Objective:** Turn hours of body-worn camera (BWC) and related video into a defensible work product: a time-synced event log, a table of every material inconsistency between the video and the written reports, a list of exculpatory and impeachment content, the suppression hooks the footage supports, and a follow-up list for missing or incomplete recordings — every entry tied to a file name and timestamp.

**When to Use:** On receipt of video discovery in a criminal matter; before drafting a suppression motion or cross-examination; when reports and video may diverge; when a supervisor or co-counsel needs a reliable index instead of re-watching. Prosecutors can use the same protocol to audit a case before charging or disclosure (select government posture).

**Distinct from:**
- `domain-legal/discovery/legal_document_review_coding_taxonomy.md` — civil document-review coding; this protocol is for time-based video evidence and constitutional issues.
- `domain-legal/depositions/legal_deposition_summary.md` — summarizes sworn testimony transcripts, not recordings.
- `domain-legal/criminal/legal_motion_to_suppress.md` — drafts the motion; this protocol finds and documents the hooks it will use.

---

## Your Input

- **Jurisdiction and posture:** [Court; defense or prosecution — required]
- **Charges and key elements:** [What the government must prove]
- **Video inventory:** [File names, officer/unit, camera type, stated start/end times, metadata if produced]
- **Written sources to compare:** [Incident report(s), supplemental reports, CAD/dispatch log, charging affidavit, witness statements]
- **Reviewer's logged observations:** [Timestamped notes or transcript excerpts the user has already made — the model works from these, not from footage it cannot see]
- **Agency BWC policy:** [Activation, muting, buffering, and retention rules if obtained; otherwise `[NEED TEXT]`]
- **Defense or prosecution theory:** [One or two sentences]

---

## Constraints

**Must:**
- Work only from the user's logged observations, transcripts, and supplied metadata; state explicitly that the model has not viewed the footage.
- Record every event with **file name + timestamp** (and the clock used: file-relative or burned-in) and note any clock offset between cameras.
- Classify each report-versus-video difference as **Contradiction** (video shows otherwise), **Omission** (report leaves out something on video), **Addition** (report states something not on video), or **Unverifiable** (off-camera, obstructed, inaudible).
- Flag possible exculpatory or impeachment content for Brady/Giglio tracking without concluding it is legally "material" `[VERIFY: materiality standard in jurisdiction]`.
- Map suppression hooks to the stage of the encounter (initial contact, stop, detention length, search, arrest, questioning, warnings).
- Check completeness: activation relative to first contact, gaps, mute events, officers present without footage, and retention-policy implications `[VERIFY: agency policy text]`.

**Must Not:**
- Describe what the footage shows beyond the user's logged observations, or infer tone, intent, or words that the log marks inaudible.
- Label an officer's conduct as lying, misconduct, or a policy violation without the policy text and the specific timestamp.
- Collapse camera clocks into one timeline without stating the offset method.
- Cite case law or policy provisions not supplied.
- Add "consult an attorney" boilerplate.

---

## Method

1. **Inventory and completeness.** Table each file: officer, start/end, duration, audio present, buffer segment, gaps. List officers or vehicles on scene with no footage produced.
2. **Clock synchronization.** Pick an anchor event visible on multiple cameras; compute offsets; record them.
3. **Master event log.** Chronological, synchronized entries: time → file@timestamp → what is seen/heard (per log) → speaker → significance tag (ELEMENT / SUPPRESSION / IMPEACH / EXCULP / CONTEXT).
4. **Report comparison.** For each assertion in the written sources, find the corresponding log entry and classify the difference.
5. **Exculpatory / impeachment list.** Items favorable to the defense or bearing on witness credibility, with timestamps; cross-reference to the Brady/Giglio tracker.
6. **Suppression hook map.** Stage → timestamped facts → possible ground → what else is needed (policy, testimony, metadata).
7. **Follow-up list.** Missing footage, metadata/audit-trail requests, enhanced-audio or transcript needs, preservation letters, witnesses to identify from the video.

---

## Output Format

```markdown
# BWC REVIEW — {Matter} — Reviewer {name} — {date}
_Model note: built from the reviewer's logged observations; footage not viewed by the model._

## 1. Inventory & Completeness
| File | Officer/Unit | Start | End | Audio | Buffer | Gaps / mute | Notes |
**Officers/vehicles on scene with no footage produced:** {...}

## 2. Clock Sync
| Anchor event | Cam A time | Cam B time | Offset |

## 3. Master Event Log
| Sync time | File@timestamp | Event (per log) | Speaker | Tag |

## 4. Report vs. Video
| Report / ¶ | Report says | Video (file@ts) | Classification | Significance |

## 5. Exculpatory & Impeachment Content
| # | File@ts | Content | Why favorable | Tracker ref |

## 6. Suppression Hooks
| Stage | Facts (file@ts) | Possible ground | Needed to perfect |

## 7. Follow-Up
- [ ] {Request / preservation / enhancement / witness ID}
```

---

## Worked Example (abbreviated)

**Input:** Defense; resisting-arrest and assault-on-officer charges. Two BWC files (Ofc. A, Ofc. B). Report says the client "swung his fist at Ofc. A" before being taken down. Reviewer's log: A-cam 00:03:10 client's hands visible at sides; 00:03:12 camera view obstructed; B-cam 00:02:58 (offset +14s) shows client's right arm raised — log notes "appears to be shielding face." A-cam audio muted 00:04:40–00:06:05.

**Output excerpt:**
- Clock sync: anchor = patrol-car door slam; offset B = A +14s.
- Report vs. video: "swung his fist" → A@00:03:10 hands at sides; B@00:02:58 (sync 00:03:12) arm raised, reviewer notes shielding — **Contradiction (partial) / Unverifiable at A@00:03:12 (obstructed)**. Significance: goes to the force element and officer credibility.
- Exculpatory list #1: B@00:02:58 arm position; tracker ref BG-04.
- Completeness: mute 00:04:40–00:06:05 during post-arrest period; policy on muting `[NEED TEXT: agency BWC policy]`; follow-up: request audit-trail metadata for mute event.
- No statement that Ofc. A lied — the table records the documented difference.

---

## Verification

- [ ] Jurisdiction and posture locked; model's no-viewing limitation stated.
- [ ] Every entry carries file name, timestamp, and clock basis.
- [ ] Offsets between cameras computed from a named anchor event.
- [ ] Every report assertion classified (Contradiction / Omission / Addition / Unverifiable).
- [ ] Favorable items cross-referenced to the Brady/Giglio tracker.
- [ ] Completeness gaps and missing officers listed with follow-up requests.
- [ ] No invented policy text, law, or characterizations of intent.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Narrating footage the model has not seen | Work only from the reviewer's log; state the limitation at the top |
| Treating file-relative time and burned-in clock time as the same | Record the clock basis for each entry and compute offsets |
| Calling an obstructed or inaudible moment a contradiction | Classify it as Unverifiable and note what would resolve it |
| Concluding an item is "Brady material" | Flag as potentially favorable; materiality is a legal question `[VERIFY]` |
| Asserting a policy violation for a mute or late activation | Require the policy text and the exact timestamp; otherwise `[NEED TEXT]` |
| Ignoring officers on scene without footage | Completeness section lists them and generates a request |
| Summarizing instead of logging | Every significant moment gets its own timestamped row |
