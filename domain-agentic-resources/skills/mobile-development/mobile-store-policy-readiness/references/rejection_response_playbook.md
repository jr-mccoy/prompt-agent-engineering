# Rejection Response Playbook

Use when the app has **already been rejected**. This inverts the normal workflow: you
start from a known citation and work back to the code, rather than searching for
risk.

## Step 0: Get the verbatim notice

Ask for the rejection message **exactly as received**, not a paraphrase.

Reason: the response depends entirely on which clause the reviewer cited, and
paraphrases routinely drop the distinguishing detail. "They said something about
permissions" and a specific restricted-permission citation lead to different work.

If the user cannot paste it, ask for: the cited guideline/policy identifier, the
reviewer's own wording, any screenshot attached, and the submission date.

**Do not proceed on a paraphrase.** Do not guess the citation.

## Step 1: Read the cited policy

Open the cited section from
[`policy_source_registry.md`](policy_source_registry.md) and read it now. The version
in your memory may predate the current text, and rejections are often driven by
recent changes.

Record: the requirement as currently written, and the URL + read date.

## Step 2: Classify the rejection

| Type | Signal | Response shape |
|---|---|---|
| **Genuine violation** | Cited behavior exists and does violate the current requirement | Fix, then resubmit with a change summary |
| **Declaration mismatch** | Behavior is fine; the declaration doesn't match it | Correct the declaration; often no code change |
| **Reviewer could not reproduce** | "Unable to locate", "could not sign in", "did not function" | Fix access — credentials, notes, walkthrough. Usually not a code defect |
| **Misunderstanding** | Cited behavior does not exist, or is being read incorrectly | Reply with evidence. Do not change working code to appease |
| **Ambiguous** | Citation is generic; the specific trigger is unclear | Ask the review team for specifics before changing anything |

Classifying wrongly is expensive in both directions: shipping a needless refactor for
a misunderstanding, or arguing about a real violation and burning review cycles.

## Step 3: Locate the trigger in the app

Search for the specific behavior cited — not the general topic. Produce `file:line`
for the trigger, or state plainly that you could not find it.

**If you cannot find the cited behavior, that is a finding in itself** and points
toward *Misunderstanding* or *Reviewer could not reproduce*. Do not invent a
plausible cause to explain the rejection.

Check especially, since these are invisible in first-party code:

- Third-party SDK behavior
- Merged library manifests
- A build variant or flavor that differs from what was submitted
- Server-driven behavior the reviewer saw but the code does not show

## Step 4: Draft the response

Structure:

1. **Acknowledge** the citation specifically
2. **State what changed**, or why nothing needed to change
3. **Point to evidence** — the screen, the flow, the setting
4. **Give reproduction steps** where the reviewer needs to see it

Rules:

- Factual and specific. No argumentation about policy fairness.
- Never claim a change you have not actually made.
- Never assert what the policy "really means" — quote what it says.
- If disputing, lead with evidence, not interpretation.
- Keep it short. Reviewers process volume.

Template:

```
Re: [citation as given]

[What we changed / Why the cited behavior does not occur]

Specifically:
- [Change 1] — [where the reviewer can see it]
- [Change 2] — [where the reviewer can see it]

To reproduce:
1. [Step]
2. [Step]

Demo account: [credentials, verified working on this build]
```

## Step 5: Pre-resubmission check

- [ ] Cited issue actually addressed in the build being submitted (not just in the
      working tree)
- [ ] Demo credentials tested against that exact build
- [ ] Declarations updated if behavior changed
- [ ] Review notes explain the change
- [ ] Ran the readiness checklist for the surfaces you touched — fixes routinely
      introduce a second violation

## Escalation

If a rejection is upheld and you believe it is factually wrong, escalation channels
exist for both stores (Play policy appeals; Apple's App Review Board). This skill can
help assemble the factual record. It cannot predict an outcome, and it does not
advise on whether to escalate — that is a business decision.

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Guessing the citation from a paraphrase | Wrong fix, second rejection, cycles burned |
| Rewriting large subsystems to appease an ambiguous notice | Introduces new risk; often unnecessary |
| Arguing policy interpretation | Reviewers apply policy, not debate it |
| Claiming a fix not in the submitted build | Escalates a rejection into a trust problem |
| Resubmitting without updating declarations | The mismatch outlives the code fix |
