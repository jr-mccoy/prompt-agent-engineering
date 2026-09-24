---
title: "Visual Media Authenticity — Assessing Whether an Image, Video, or Audio Clip Is What It Claims"
category: psy-ops/technique-analysis
description: "Assess whether a specific image, video, or audio clip is authentic, manipulated, synthetic, or authentic-but-miscontextualized, with the heavy false-positive discipline this question demands: detector outputs are not verdicts, visual 'tells' age out as generators improve, and the most common deception is a real recording with a false caption. Treats 'cannot determine' as a first-class result and guards equally against the liar's dividend — dismissing genuine media as fake."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-04
  - QA-01
difficulty: advanced
tags:
  - psy-ops
  - synthetic-media
  - media-forensics
  - verification
  - technique-analysis
  - fake-photo
updated: "2026-09-24"
reasoning:
  styles: [analytic, evidential, adversarial]
  stakes: high
  horizon: immediate
  uncertainty: ambiguity
  evidence_quality: weak
  domain_complexity: cross_domain
  collaboration: solo_or_team
  output_format: graded_authenticity_judgment
  user_role: [analyst, journalist, trust_and_safety, researcher, individual]
  mode: [assess, verify, document]
related_prompts:
  - domain-psy-ops/technique-analysis/psyops_provenance_and_transmission_trace.md
  - domain-psy-ops/technique-analysis/psyops_statistical_and_visual_distortion_scan.md
  - domain-AI-ML/model-security/mlsec_model_watermarking_provenance.md
---

# Visual Media Authenticity Assessment

**Objective:** Assess whether a specific image, video, or audio clip is what it is presented as — and grade how confident that assessment can honestly be. There are four distinct answers, and they are routinely collapsed into two: the media is **authentic and correctly contextualized**; it is **authentic but miscontextualized** (a real recording, a false date, place, or caption); it has been **manipulated** (edited, spliced, retimed, selectively cropped); or it is **synthetic** (generated wholly or substantially). The second category is very common in practice, and an analyst hunting for generation artifacts will walk straight past it.

This question is distinct from provenance tracing. `psyops_provenance_and_transmission_trace.md` asks where a piece of media came from and how it travelled; this prompt asks whether the object itself can be trusted. The two are used together, and provenance usually resolves more cases than pixel inspection does.

The discipline this prompt enforces is that **detection claims are frequently wrong in both directions**. Automated detectors produce confident-looking scores with poor reliability outside the conditions they were trained on, and they degrade further under compression, re-encoding, and screenshotting. Visual "tells" — malformed hands, garbled text, odd lighting — are real for some generators and absent in others, and any list of them ages within months. And the symmetric error matters just as much: the **liar's dividend**, where genuine evidence is dismissed as "probably AI," is now a deliberate tactic. An assessment that calls real footage fake does as much damage as one that certifies a fabrication.

> **Stop conditions.** If the media is sexual or intimate imagery of a real person, do not analyze it here — the question of whether it is synthetic does not change what should happen next, which is reporting it to the platform and, where relevant, to the police or the relevant authority. **If there is any possibility the media depicts a minor in a sexual context, stop: do not copy, save, forward, or upload it anywhere, including to an AI tool. Report it to the platform and to your country's official child-exploitation reporting service, which you should look up from a government or police website rather than from an AI.**

**When to use:**
- An image, clip, or recording is circulating and its authenticity matters to a decision — publication, moderation, response, or belief.
- Someone has claimed that a piece of media is AI-generated or doctored, and you need to assess the claim.
- Someone has claimed that genuine-looking media is fake, and you need to assess that claim with equal rigor.
- You are writing up a media assessment and need the confidence language to be defensible.

**When NOT to use:**
- You want to trace where the media came from and how it spread — use `psyops_provenance_and_transmission_trace.md`, then return here if the object itself is still in question.
- The media is a chart or data visualization and the concern is distortion — use `psyops_statistical_and_visual_distortion_scan.md`.
- You need technical watermark or provenance-credential design for your own systems — see `domain-AI-ML/model-security/mlsec_model_watermarking_provenance.md`.
- The media is intimate imagery of a real person, or could involve a minor — see the stop conditions above.

**Audience:** Journalists, verification desks, trust-and-safety staff, researchers, and individuals deciding whether to believe or share something.

---

## Inputs / Context

1. **The media itself, and its form.** Original file, a download, a screenshot, a screen recording, a re-upload. Each generation of copying destroys evidence; record which you have.
2. **The claim attached to it.** Exactly what it is presented as showing — who, what, where, when. Authenticity is always authenticity *relative to a claim*.
3. **Earliest known appearance.** Where and when it first surfaced, as far as you can establish. Mark unknowns `[VERIFY]`.
4. **Any metadata or credentials.** File metadata, content-credential manifests, platform labels. Note which were present, absent, or stripped.
5. **Independent corroboration.** Other recordings of the same event, eyewitness accounts, official records, weather, geography, shadows, signage.
6. **Detector outputs already obtained.** Which tool, what score, on which copy of the file. These are inputs to weigh, not conclusions to repeat.
7. **Who is claiming what.** Who says it is real, who says it is fake, and what each would gain. This is context for scrutiny, not evidence of authenticity.

---

## Constraints

### Must
- Distinguish the **four outcomes** — authentic and in context, authentic but miscontextualized, manipulated, synthetic — plus **cannot determine**, and check miscontextualization first.
- Grade the finding **low / moderate / high** with the basis stated, and state what evidence would move it.
- Weight **contextual and provenance evidence** (independent recordings, geolocation, chronolocation, earliest appearance) above **artifact evidence** (visual or audio anomalies).
- Treat every **automated detector score as one weak input**, noting the tool, the copy it ran on, and that compression and re-encoding degrade reliability.
- Run the **liar's-dividend check**: assess the claim that the media is fake with the same rigor as the claim that it is real.
- State the **degradation limit**: what the copy you hold can and cannot reveal compared with an original.
- Record the **stop conditions** and honor them without exception.
- Attach the assessment to **the media and its claim** — never to the character or motives of the person who posted it.

### Must Not
- Declare media fake or real on the basis of a single artifact, a single detector score, or a feeling that it "looks AI."
- Provide a list of generator tells as if it were durable, or explain how to make synthetic media evade detection.
- Treat absence of metadata or credentials as evidence of fabrication — platforms routinely strip both.
- Treat presence of a credential or platform label as proof of authenticity beyond what it actually certifies.
- Invent metadata values, detector scores, source accounts, dates, or corroborating recordings.
- Accuse a named private individual of fabricating media.
- Analyze intimate imagery of a real person, or any media that may depict a minor sexually.

---

## Instructions

### Step 1 — Fix the claim and the copy
Write the exact claim the media is being used to support, and describe the copy you hold — original, download, screenshot, re-encode. Everything downstream is bounded by both. A screenshot of a re-upload cannot support a pixel-level finding.

### Step 2 — Check miscontextualization first
Before looking for manipulation, establish whether this is real media from a different time, place, or event. Search for earlier appearances; check whether landmarks, weather, seasons, signage, language, uniforms, and vehicles match the claim. This resolves more cases than any other step.

### Step 3 — Gather contextual corroboration
Look for independent recordings of the same event from other angles, eyewitness accounts, and official records. Geolocate and chronolocate where possible. Consistent independent corroboration is the strongest evidence of authenticity available; its absence is weak evidence of anything, since many real events are recorded once.

### Step 4 — Read metadata and credentials for what they actually say
Record what is present, absent, or stripped, and what each actually certifies. A content credential attests to a chain of custody from a particular point; it does not certify that the scene depicted is true. Absence proves nothing, because most platforms remove both.

### Step 5 — Examine artifacts, with their limits stated
Note visual or audio anomalies — inconsistent lighting and shadows, physically impossible geometry, lip-sync drift, unnatural audio cadence or room tone, splice discontinuities. For each, state how strongly it discriminates and whether compression alone could produce it. Weight artifact evidence below context.

### Step 6 — Weigh detector outputs as weak inputs
For any automated detector score, record the tool, the copy it ran on, and the known limits of that class of tool. Two detectors disagreeing is common and informative. A single score is never the finding.

### Step 7 — Run the liar's-dividend check
Argue the opposite of whichever way you are leaning. If you suspect fabrication, construct the case that it is genuine; if you believe it genuine, construct the case that it is fabricated or miscontextualized. Note specifically whether "it's AI" is being used to dismiss inconvenient genuine evidence.

### Step 8 — Adversarial check and graded judgment
Argue against your own finding one final time, then state the outcome — including **cannot determine** — with a confidence band, its basis, the degradation limit of the copy, and the specific evidence that would change it.

---

## False-Positive Prevention

1. **Miscontextualization missed.** Hunting for generation artifacts in media that is genuine but mis-captioned — the most common deception and the easiest to overlook.
2. **Detector score treated as verdict.** Repeating a percentage from a tool whose reliability on this copy, format, and generator is unknown.
3. **Stale tells.** Relying on artifacts that characterized one generation of tools and are absent in the next, or present in ordinary compressed footage.
4. **Compression read as manipulation.** Blocking, smearing, and audio artifacts from re-encoding mistaken for editing traces.
5. **Missing metadata read as fabrication.** Platforms strip metadata routinely; absence carries almost no information.
6. **The liar's dividend.** Accepting "it's probably AI" as a reason to dismiss genuine evidence, which is now a deliberate tactic in its own right.
7. **Plausibility as evidence.** Deciding authenticity by whether the content seems like something that person would do — a judgment about the claim, not the media.
8. **Accusation drift.** Moving from "this media is likely manipulated" to "this person faked it," which the evidence almost never supports.

---

## Output Format

```
# Media authenticity assessment — [short description]

## The claim and the copy
Claim the media is used to support: [...]
Copy assessed: [original / download / screenshot / re-encode] — degradation limit: [...]

## Miscontextualization check (first)
Earlier appearances found: [... / none found — search scope: ...]
Contextual consistency (place, time, weather, signage, language): [...]

## Contextual corroboration
| Evidence | Independent? | Supports | Strength |
|---|---|---|---|
| [other recording / witness / record] | [y/n] | [authentic / miscontext / unclear] | [low/mod/high] |

## Metadata and credentials
Present: [...] · Absent/stripped: [...] · What they actually certify: [...]

## Artifact observations
| Observation | Discriminating power | Could compression explain it? |
|---|---|---|

## Detector inputs (weak)
| Tool | Copy it ran on | Output | Known limits |
|---|---|---|---|

## Liar's-dividend check
[The case for the opposite conclusion; whether "it's fake" is being used to dismiss genuine evidence]

## Adversarial check
[The strongest argument against my finding]

## Judgment
Outcome: [authentic in context / authentic but miscontextualized / manipulated / synthetic / **cannot determine**]
Confidence: [low / moderate / high] — basis: [...]
Would change with: [...]
Outstanding [VERIFY] items: [...]
```

---

## Verification

- [ ] The claim and the copy are fixed first, with the copy's degradation limit stated.
- [ ] Miscontextualization was checked before manipulation or synthesis.
- [ ] Contextual and provenance evidence is weighted above artifact evidence.
- [ ] Every detector output is recorded with tool, copy, and limits, and none is treated as the finding.
- [ ] Missing metadata is not treated as evidence of fabrication.
- [ ] The liar's-dividend check was run with the same rigor as the fabrication check.
- [ ] "Cannot determine" was available and was not avoided for being unsatisfying.
- [ ] The judgment carries a confidence band, its basis, and what would change it.
- [ ] No metadata, score, source, date, or corroborating recording was invented, and no private individual is accused of fabrication.
- [ ] No evasion guidance appears, and no intimate imagery or possible depiction of a minor was analyzed.
