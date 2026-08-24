---
title: "Content Monitoring Pipeline — Capture, Filter, and Triage Tracked Sources"
category: productivity/automation
description: "Design a no-code/low-code automation that watches sources (RSS, social, search alerts), filters by keyword rules, deduplicates, rate-limits, and writes structured records to a destination with optional notification — including failure handling and maintenance."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - DS-06
  - QA-01
difficulty: intermediate
tags:
  - automation
  - content-monitoring
  - rss
  - deduplication
  - workflow-design
updated: "2026-06-07"
related_prompts:
  - domain-productivity/automation/automation_weekly_digest.md
  - domain-productivity/automation/automation_data_sync.md
  - domain-business-strategy/research/research_competitive_landscape.md
---

# Content Monitoring Pipeline

**Objective:** Specify a reliable automation that captures items from one or more tracked sources, filters them against keyword rules, deduplicates against the destination, rate-limits to avoid spam, and writes clean structured records (with optional notification) — with explicit failure handling and ongoing maintenance.

**When to use:**
- Competitive intelligence: tracking competitor blogs, releases, or job postings.
- Industry / news monitoring across multiple feeds into one review queue.
- Brand or keyword mention monitoring from search alerts or social.
- Research aggregation where a human reviews captured items later.

**When NOT to use:**
- One-time manual research — a saved search is faster than building a pipeline.
- High-volume real-time streams (firehose-scale) — needs purpose-built infrastructure, not a no-code automation.
- Sources without a stable feed/API where scraping would be brittle or against terms of service.

**Audience:** Individuals and small teams building automations in Zapier, Make, n8n, or similar no-code/low-code platforms.

---

## Inputs / Context

Supply the following before generating the automation spec:

1. **Purpose** — what you're tracking and why (e.g., "competitor blog posts for content ideas").
2. **Source(s)** — for each: type (RSS / social account or list / search alert), the URL or identifier, and check frequency.
3. **Filter rules** — include keywords, exclude terms, and any recency window.
4. **Destination** — where records land (Notion, Airtable, Google Sheets, etc.) and which fields it has.
5. **Notification target (optional)** — Slack channel / email and what should trigger a notification.
6. **Volume expectations** — normal items/day and a sane daily cap.
7. **Available integrations** — which apps you actually have connected/authorized on your platform.

---

## Constraints

### Must
- Use only sources and destinations that have a working integration on the chosen platform (or note the gap).
- Deduplicate against the destination by a stable key (URL or canonical ID) **before** writing.
- Apply include/exclude keyword filters before any write or notification.
- Make the write **idempotent** — re-running on the same item must not create a duplicate.
- Rate-limit: enforce a daily cap and route overflow to a batch list rather than dropping silently.
- Define what happens on failure (feed down, auth expired, destination write rejected).
- Include a maintenance routine (stale-feed detection, periodic cleanup).

### Must Not
- Assume an integration exists — flag any source/destination/notification channel that may need setup.
- Fire notifications on items that failed the filter or on duplicates.
- Capture personal data beyond what the purpose requires.
- Hard-fail the whole pipeline on one bad item — isolate and log it.

---

## Instructions

1. **Restate purpose and scope.** One line: what is captured, from where, to where, for whom.
2. **Define the trigger** for each source:
   - RSS: feed URL + polling interval.
   - Social: platform + account/list identifier.
   - Search alert: query string + alert source.
3. **Specify the filter step.** Translate include/exclude keywords and recency into explicit conditions; default to AND between "include" and "not exclude" groups.
4. **Specify deduplication.** Name the match key, the lookup step (search destination), and the branch: found → skip (or update "last seen"); not found → continue.
5. **Specify the record write.** Map each destination field to a source value; set status to "To Review"; record both publish date and capture timestamp.
6. **Specify the optional notification.** Only on successful, filtered, non-duplicate writes; include title, source, date, link.
7. **Specify rate limiting.** Daily cap; overflow → batch list; spike alert when today's count exceeds the normal band.
8. **Specify failure handling.** Feed unreachable, auth error, destination rejection → log with timestamp + reason and alert the maintainer; continue processing remaining items.
9. **Specify maintenance.** Stale-feed detection (no items in N days), periodic cleanup of old reviewed records.
10. **Self-check before output.** Confirm: every named integration is in the user's available list (or flagged); dedup key is stable; no notification can fire on filtered-out/duplicate items; failure paths exist for each external call. Resolve gaps or list them as assumptions, then emit the spec.

---

## False-Positive Prevention

❌ **DON'T:**
- Assume the destination, source, or Slack/email integration is already connected.
- Trust the source's `guid`/title as a dedup key when the URL is the stable identifier.
- Let a temporary feed outage or expired token silently stop captures with no alert.
- Notify on every item before applying filters (turns the channel into noise).
- Capture into free-text fields that make later dedup or filtering impossible.

✅ **DO:**
- Confirm which integrations the user actually has, and flag any that need setup.
- Pick one stable, normalized dedup key and use it consistently.
- Add explicit failure branches with logging and a maintainer alert.
- Filter and deduplicate before any write or notification.
- Write structured fields (status, tags, dates) so the review queue stays usable.

---

## Output Format

```
AUTOMATION: Monitor [CONTENT TYPE] → Capture to [DESTINATION]
PURPOSE: [one line]
INTEGRATIONS REQUIRED: [source app, destination app, notifier] — [confirmed / NEEDS SETUP]

TRIGGER
- Source: [type + URL/identifier]
- Frequency: [interval]

FILTER (continue only if all true)
- Include (title OR description contains): [keywords]
- Exclude (must NOT contain): [terms]
- Recency: [window or n/a]

DEDUPLICATION (before write)
- Match key: [URL / canonical ID]
- If found: [skip | update last_seen]
- If not found: continue

ACTION 1 — Write record to [DESTINATION]
- [field] → [value]  (repeat per field; include status, tags, publish date, capture timestamp)

ACTION 2 — Notify (optional, only on successful new write)
- Channel: [target]; Message: [title / source / date / link]

RATE LIMITING
- Daily cap: [N] → overflow to [batch list]
- Spike alert if today's count > [threshold]

FAILURE HANDLING
- Feed unreachable / auth error / write rejected → log [timestamp, reason] + alert [maintainer]; continue with next item

MAINTENANCE
- Stale feed: alert if no items in [N] days
- Cleanup: [routine + cadence]

TESTING CHECKLIST
- [ ] ...
```

---

## Example Output

```
AUTOMATION: Monitor Competitor Blog Posts → Capture to Notion "Content Radar"
PURPOSE: Track competitor blog posts to mine for content ideas and positioning shifts.
INTEGRATIONS REQUIRED: RSS by Zapier (built-in), Notion (CONFIRMED), Slack (CONFIRMED)

TRIGGER
- Source: RSS — https://competitor.com/blog/feed.xml
- Frequency: every 1 hour

FILTER (continue only if all true)
- Include (title OR description contains): pricing, launch, integration, benchmark
- Exclude (must NOT contain): webinar, hiring, job
- Recency: published within last 14 days

DEDUPLICATION (before write)
- Match key: normalized item URL (strip UTM params, lowercase host)
- If found: update "Last Seen" date; do not create new record
- If not found: continue

ACTION 1 — Write record to Notion DB "Content Radar"
- Title        → item.title
- URL          → normalized item URL
- Source       → "Competitor Blog"
- Published    → item.pubDate
- Captured     → now()
- Summary      → first 200 chars of item.description
- Status       → "To Review"
- Tags         → matched include keywords

ACTION 2 — Notify (only on successful new write)
- Channel: #content-radar
- Message: "📰 New competitor post: *{title}* — {Published} — {URL}"

RATE LIMITING
- Daily cap: 25 → overflow rows tagged "Batch" for end-of-day review
- Spike alert: if today's captures > 15, post "Captured {n} today (normal ~5)"

FAILURE HANDLING
- Feed 4xx/5xx or empty for a run → log to "Automation Errors" sheet [timestamp, "feed unreachable"] and DM maintainer; skip this run, retry next interval
- Notion write rejected → log [timestamp, item URL, error]; alert maintainer; continue with next item

MAINTENANCE
- Stale feed: if no new items in 10 days, alert "Competitor feed quiet 10d — verify it moved"
- Cleanup: weekly, archive records with Status="Reviewed" older than 60 days

TESTING CHECKLIST
- [ ] Feed currently has items matching the include filter
- [ ] Run once → record appears in Notion with all fields populated
- [ ] Re-run on same item → no duplicate, "Last Seen" updated
- [ ] Submit an excluded-keyword item → not captured, no Slack message
- [ ] Force a feed error → error logged + maintainer alerted, pipeline continues
- [ ] Run 3 days → review for false positives and tune keywords
```

---

## Verification

- [ ] Every named integration is confirmed available or flagged as needing setup.
- [ ] Filter applies before any write or notification.
- [ ] Dedup uses a stable, normalized key and runs before writing.
- [ ] The write is idempotent (re-running creates no duplicate).
- [ ] Rate limiting with overflow and spike alert is defined.
- [ ] Failure branches exist for each external call, with logging + maintainer alert.
- [ ] Notifications fire only on successful, filtered, non-duplicate writes.
- [ ] Maintenance routine covers stale feeds and cleanup.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Opens by fixing the captured→filtered→stored→notified scope so the automation has one unambiguous purpose.
- **ST-03 (Output Format Specification):** Locks the trigger→filter→dedup→action→failure spec into a fixed, copy-ready template.
- **CM-02 (Constraint Specification):** Encodes Must/Must-Not rules (idempotency, integration confirmation, no notification on duplicates) the design must satisfy.
- **DS-06 (Prioritization and Severity Guidance):** Rate-limiting, overflow routing, and spike alerts triage volume so high-signal items aren't buried.
- **QA-01 (Self-Verification):** A pre-output self-check confirms integrations, dedup key, and failure paths before the spec is emitted.

---

## Related Prompts

- `domain-productivity/automation/automation_weekly_digest.md` — Roll captured items up into a scheduled summary.
- `domain-productivity/automation/automation_data_sync.md` — Keep captured records mirrored into another system.
- `domain-business-strategy/research/research_competitive_landscape.md` — Turn monitored signals into a competitive analysis.
