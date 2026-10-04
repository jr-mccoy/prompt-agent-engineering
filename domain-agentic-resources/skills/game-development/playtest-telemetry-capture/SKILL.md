---
name: playtest-telemetry-capture
description: Instruments a playtest build to capture exactly what the playtest protocol asks for, using a small event schema traced to research questions, pseudonymous participant codes, build stamping, an observer bookmark hotkey, video sync markers, consent gating and retention rules, then validates and exports the logs for synthesis. Use when asked to "add telemetry to the playtest build", "log deaths and quit points", "capture playtest data", or "sync playtest video with gameplay logs".
metadata:
  tags:
    - game-dev
    - playtesting
    - telemetry
    - user-research
    - consent
    - data-capture
  updated: "2026-10-04"
---
# Playtest Telemetry Capture

Turns a playtest protocol's "telemetry to capture" line into working instrumentation: a
minimal event log written locally by the build, aligned with session video and observer
notes, gated on consent, and checked by a validation script before anyone draws
conclusions from it.

## Purpose

Playtest data is lost in predictable ways. The build logs everything except the one event
the research question needed. Video and logs cannot be lined up. A crash truncates the
file. Two sessions ran different builds and nobody noticed. A participant's name ends up
in a file name. This skill prevents those losses at the instrumentation stage, when they
are cheap to fix.

## When to Use This Skill

- Preparing a build for an in-person or remote moderated playtest (typically 5–15 players)
- The protocol specifies telemetry (deaths, time per section, quit points, ability use)
  and the build does not yet emit it
- Observers need a way to mark moments that can be matched to gameplay and video later
- Logs from a previous round were incomplete, misaligned or mixed across builds

## When NOT to Use This Skill

- **Choosing research questions, participants, the session script, or synthesising
  findings.** Use the one-off prompt
  `domain-game-development/testing/testing_playtest_protocol_synthesis.md`. This skill
  starts from that protocol's telemetry list and hands data back to its synthesis step.
- **Functional QA test plans** (does the feature work as specified). See
  `domain-game-development/testing/testing_gameplay_test_plan.md`.
- **Live-service analytics at scale** (cohorts, retention, funnels across thousands of
  players). That is product analytics; see `domain-data-analytics/`.
- **Automated bots or test harnesses.** See
  `domain-game-development/testing/testing_automated_game_testing.md`.

## Prerequisites

- The playtest protocol, with research questions (RQs) and the decision each one informs
- Access to the game's event or messaging system and a place to write files on the test
  device
- Whoever owns privacy or legal questions for your organisation, for Step 3

## Workflow

### Step 1: Trace every event to a research question

Write the trace table before writing code. An event that answers no RQ is not logged.

| RQ | Decision it informs | Event(s) that answer it | Payload |
|---|---|---|---|
| RQ1: Do players find the double-jump without the tutorial? | Keep or add tutorial prompt | `ability_first_use` | ability id, section, t since section enter |
| RQ2: Where does difficulty spike in world 1? | Rebalance sections | `death`, `retry`, `section_enter`/`section_exit` | cause, position, section |
| RQ3: Why do players quit early? | Fix onboarding | `quit`, `pause`, `settings_changed` | section, menu path |

Telemetry tells you *what* happened and *where*, never *why*. Keep the "why" with the
observation notes and the post-session interview from the protocol.

### Step 2: Define the event envelope and names

Every event is one JSON object on one line (JSON Lines). Envelope fields:

| Field | Example | Rule |
|---|---|---|
| `schema_version` | `1` | Increment when fields change |
| `build_id` | `0.4.2+a1b2c3` | Version plus commit; also shown on screen (Step 5) |
| `session_id` | random UUID | Generated at session start |
| `participant_code` | `P07` | Pseudonym only; mapping to a person is stored elsewhere |
| `t_ms` | `183250` | Milliseconds on a monotonic session clock, starting at 0 |
| `event` | `death` | `snake_case`, past-tense or noun form, from a fixed list |
| `section` | `1-2` | Level or section id, where meaningful |
| `payload` | `{"cause": "spikes", "x": 12.5, "y": 3.0}` | Event-specific; no free text from the player |

Also log `wall_clock_utc` once, in `session_start`, so sessions can be ordered without
putting wall-clock time on every event.

Standard events for most protocols: `session_start`, `session_end`, `section_enter`,
`section_exit`, `death`, `retry`, `quit`, `pause`, `settings_changed`,
`objective_complete`, `ability_first_use`, `observer_bookmark`, `sync_marker`. Keep the
allowed names in a text file (one per line); the validation script uses it.

### Step 3: Set up consent and data handling before the first session

Agree these with whoever owns privacy or legal questions, in writing:

- **Consent form contents:** what is recorded (gameplay events, screen, face camera,
  voice), why, who sees it, how long it is kept, and that the participant may stop at any
  time and ask for their data to be deleted. Keep the NDA separate from the consent form.
- **Minors:** require a parent or guardian's consent and follow the rules that apply where
  the test runs. Do not proceed on assumptions.
- **Jurisdiction:** data-protection law (for example GDPR in the EU/UK) may govern
  recordings of identifiable people. Confirm what applies; this skill does not give legal
  advice.
- **Separation:** the participant-code-to-person mapping lives in one restricted document,
  never in log files, file names or video titles.
- **Retention:** set a deletion date for raw video and logs, and assign an owner to carry
  it out.

**Consent gate in the build:** logging stays off until the moderator enters the
participant code and confirms consent (debug menu or launch argument). Without that step
the build writes nothing.

### Step 4: Implement local-first, crash-safe logging

Write locally first. The lab network is not part of the experiment.

```text
on session_start(participant_code, consent_confirmed):
  if not consent_confirmed: return            # no logging without consent
  session_id = uuid4(); clock0 = monotonic_ms()
  file = open_append("playtest_logs/" + participant_code + "_" + session_id + ".jsonl")
  log("session_start", payload={"wall_clock_utc": utc_now_iso()})

log(event, section=None, payload={}):
  line = json({schema_version, build_id, session_id, participant_code,
               t_ms: monotonic_ms() - clock0, event, section, payload})
  queue.push(line)                            # never block the game thread on disk I/O

background writer:
  every 250 ms or 50 lines: write queued lines + "\n"; flush
on quit / crash handler: drain queue; flush; close
```

- Use a monotonic clock, not wall-clock time, so system clock changes cannot reorder events.
- Append one complete line per event. After a crash, the file is still valid up to the
  last full line; the validator tolerates a truncated final line.
- Optional upload happens after the session, from the file, never live during play.

### Step 5: Add observer and alignment tooling

- **Bookmark hotkey:** a key or a second device that logs `observer_bookmark` with a
  short tag (`confused`, `stuck`, `delight`, `bug`, `quote`). Observers tag in the moment
  and write details later.
- **Sync marker:** at session start, show a full-screen marker for a few frames and play a
  short tone, logging `sync_marker` at the same time. The marker's frame in the video
  equals that event's `t_ms`, which aligns every other event with the recording.
  Avoid bright flashing; a static high-contrast card is enough.
- **Build watermark:** draw `build_id` and `participant_code` in a screen corner, so every
  video frame identifies its build and session.

### Step 6: Run the session checklists

Before each session:
- [ ] Fresh save or the protocol's specified save loaded
- [ ] Consent captured on paper or form; participant code entered in the build
- [ ] Logging indicator on; screen and camera recording running; sync marker shown
- [ ] Build watermark matches the build planned for this round

After each session:
- [ ] Recording stopped and saved under the participant code
- [ ] Log file copied off the device and validated (Step 7)
- [ ] Anomalies noted (crash, moderator intervention, hardware problem) in the session notes

### Step 7: Validate and export

Run the bundled validator over every session file before synthesis:

```bash
python3 scripts/validate_playtest_log.py sessions/*.jsonl \
  --events allowed_events.txt --csv section_summary.csv
```

It checks the envelope, one session/build/participant per file, monotonic `t_ms`,
`session_start` first, missing `session_end`, unknown event names and payload keys that
look like personal data. It prints a per-session summary and writes a CSV of time, deaths
and quits per section. Exit code 1 means at least one file has errors.

**If validation fails:**
1. A backwards `t_ms` usually means wall-clock time was used; fix the clock source before
   the next session and treat that session's timings as unreliable.
2. Mixed `build_id` values mean the build changed mid-round; analyse those sessions
   separately.
3. An unknown event name is a typo or an unlisted event; fix the code or the list, never
   both silently.

Hand the CSV and the bookmark list to the protocol's synthesis step. Telemetry counts are
**Observed** evidence; report them as n/N players ("4 of 6 died at the second gap"), not
as percentages from small samples.

## Verification

- [ ] Every logged event appears in the RQ trace table
- [ ] With consent not confirmed, the build writes no file
- [ ] A forced crash mid-session leaves a file that validates with only a truncation warning
- [ ] Sync marker visible in the video and present in the log; a known event lines up
      within a frame or two
- [ ] No names, emails or free text in logs or file names
- [ ] Validator passes on a full dry-run session before real participants arrive

## Common Failure Modes

| Symptom | Cause | Fix |
|---|---|---|
| Logs too large and nobody reads them | Logging every frame or every input | Log only events in the trace table; sample positions at most every few seconds if heatmaps are needed |
| Hitches during play | Synchronous disk writes on the game thread | Queue lines and write from a background thread |
| Video and log disagree | No shared reference point | Use the sync marker; keep recorder frame rate constant |
| Sessions not comparable | Build changed between sessions | Freeze the build for a round; watermark `build_id` |
| Identity leaks | Real names in participant fields or file names | Codes only; mapping stored separately with restricted access |
| Team over-reads numbers | Treating 6 players as a statistic | Report n/N; pair each number with observations |

## Safety & Constraints

**NEVER:**
- Record a participant before consent is confirmed, or keep recording after they withdraw
- Log free text typed by players, voice transcripts, or device identifiers in telemetry
- Keep raw video past the agreed retention date

**ALWAYS:**
- Run a full dry-run session with a team member before the first participant
- Keep the participant mapping in one restricted location with a named owner

## Reference Files

| Resource | Purpose |
|---|---|
| `scripts/validate_playtest_log.py` | Validates JSONL session logs and writes a per-section summary CSV (standard library only) |

## Related Skills

- `game-feel-juice-pass`: the feedback being evaluated is often what the playtest measures
- `godot-gdscript-patterns` / `unity-ecs-patterns`: where to hook an event bus for logging
- Prompt `domain-game-development/testing/testing_playtest_protocol_synthesis.md`:
  research questions in, synthesis out; this skill is the capture step in between
