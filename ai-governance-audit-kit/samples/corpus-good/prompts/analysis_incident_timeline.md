---
title: "Incident Timeline"
description: "Reconstruct an incident timeline from logs, chat and deploy history, separating what was known at each moment from what is known now."
tags:
  - incident
  - timeline
  - postmortem
updated: "2026-05-02"
---

<!-- SYNTHETIC TEST FIXTURE — NOT INDEPENDENT BENCHMARK EVIDENCE -->

# Incident Timeline

**Objective:** Reconstruct a defensible incident timeline.

## When to Use

- An incident is closed and the review needs an agreed sequence of events.

## When NOT to Use

- The incident is still open — use the live status channel instead.

## Method

1. Collect deploy history, alert timestamps and chat transcript.
2. Place each event on one clock, naming the source for every entry.
3. Mark, per entry, what responders knew at that moment.
4. Separate contributing factors from the trigger.

## Output Format

One table, columns: time, event, source, known-at-the-time.

## Verification

- [ ] Every entry names its source.
- [ ] Hindsight is never presented as contemporaneous knowledge.
