---
title: "Privilege Log Generator"
category: legal/discovery
description: "Generate Rule 26(b)(5) privilege log entries — including categorical, document-by-document, and metadata-based logs — with sufficient detail to permit assessment without waiving the privilege."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - legal
  - discovery
  - privilege-log
  - attorney-client
  - work-product
  - rule-26
updated: "2026-05-08"
related_prompts:
  - domain-legal/discovery/legal_discovery_response_objections.md
  - domain-legal/discovery/legal_document_request_drafter.md
---

**Purpose:** Build privilege-log entries — for documents withheld or redacted on the basis of attorney-client privilege, work-product doctrine, common-interest, joint-defense, or other applicable privileges — with sufficient detail to satisfy Rule 26(b)(5) (or state analog) without itself disclosing privileged content.

**When to use:** Production rolling out and a privilege population needs logging; meet-and-confer over log adequacy; supplementing a log after re-review.

---

## Your Input

- **Court / venue:** [Federal / state]
- **Privilege-log format negotiated or controlling:** [Document-by-document / metadata + descriptions / categorical / hybrid]
- **Privileges asserted:** [Attorney-client; work product (ordinary or opinion); common-interest; joint-defense; other state-specific]
- **Document set with metadata:** [For each: doc id / Bates, date, author(s), recipient(s) (To/Cc/Bcc), file type, subject line if email, custodian, basis for withholding, type of redaction (full withhold or redact)]
- **Counsel involved:** [In-house and outside counsel names with role; flag who is a lawyer vs. agent of counsel vs. business client]
- **Litigation-anticipation date for work product:** [Date litigation was anticipated; for what dispute]
- **Common-interest agreement:** [If asserted — parties, scope]

---

## Constraints

**Must:**
- For document-by-document logs, include for each entry at minimum:
  - Doc ID / Bates (or Begin/End range)
  - Date
  - Document type (email, memo, draft, attachment)
  - Author(s) with role marker (Attorney / Client / Agent of counsel / Third-party)
  - Recipient(s) with role markers (To / Cc / Bcc)
  - Subject (for emails) — redacted if itself privileged
  - Privilege(s) asserted
  - Description sufficient to assess the privilege without disclosing it
  - Withhold-vs.-redact indicator
- For categorical logs: identify the category, the privilege(s) asserted, the date range, custodians, the legal basis, and the procedure used to identify the category. Categorical logs are appropriate only where (a) the parties agree, (b) the court orders, or (c) the volume and uniformity make document-by-document infeasible.
- Mark each entry with the **basis for the privilege** in the document context: e.g., "Communication between [Attorney] and [Client] for the purpose of providing legal advice regarding [topic — described non-privilegedly]"; or "Document prepared by [counsel/agent] in anticipation of litigation in [matter] for the purpose of [purpose]."
- Identify **distribution to non-attorneys** that does not break privilege (e.g., agents of counsel; common-interest counterparties) — and flag entries where distribution may be a waiver problem.
- For email **chains**, log the top-level email; do not omit underlying emails — instead either log them as attachments or apply the chain-logging convention controlling in the venue.
- For **attachments**, log them separately if the privilege analysis differs from the parent.

**Must Not:**
- Use vague descriptions like "privileged communication" or "work product re: subject matter." Courts find these insufficient.
- Log non-privileged documents on the privilege log as a hedge — that wastes everyone's time and signals overclaim.
- Disclose privileged content in the description.
- Treat all communications "with counsel cc'd" as privileged. Carbon-copying counsel does not by itself create privilege.
- Use one description for all entries in a category without justification.
- Conflate attorney-client privilege with work-product doctrine in the same entry without identifying which content is covered by which.

---

## Instructions

1. **Choose the format** that matches the controlling rule, order, or agreement.
2. **For each candidate document**, identify:
   - Whether the privilege element is satisfied (communication / between attorney and client / made in confidence / for the purpose of legal advice — for attorney-client; document or tangible thing prepared in anticipation of litigation by or for a party or its representative — for work product).
   - Whether the privilege has been waived by disclosure to non-privileged third parties (or whether the disclosure is within a recognized non-waiver doctrine).
   - Whether redaction would be sufficient (privileged portion redacted; non-privileged portion produced).
3. **Build the log**.
4. **Quality-check** by sampling: confirm that each row, read alone, communicates the basis for the privilege without disclosing privileged content.
5. **Flag uncertain entries** for re-review.

---

## Output Format

### Document-by-document log (default)

```markdown
| Bates | Date | Type | Author(s) (role) | Recipient(s) (role) | Subject (if email) | Privilege | Description | Withhold/Redact |
|-------|------|------|-------------------|-----------------------|--------------------|-----------|-------------|-----------------|
| {ID} | {date} | Email | {Author} (Attorney) | {Recipient} (Client) | {subject — redact if privileged} | A-C | Communication from outside counsel to client providing legal advice regarding {topic — described non-privilegedly}. | Withhold |
| {ID} | {date} | Memorandum | {Author} (Outside counsel) | {Recipient} (Client) | n/a | A-C; WP (opinion) | Legal memorandum analyzing {topic — non-privileged framing} prepared in anticipation of {dispute} on or after {date}. | Withhold |
| {ID} | {date} | Draft contract | {Author} (Counsel) | {Recipient} (Client) | n/a | A-C | Draft prepared by counsel for client review and revision; reflects legal advice. | Redact |
```

### Categorical log (where appropriate)

```markdown
| Category | Description | Date range | Custodians | Privilege(s) | Basis | Volume |
|----------|-------------|------------|------------|--------------|-------|--------|
| Outside-counsel legal advice on {topic} | Communications between {firm} and in-house legal team and named business clients providing legal advice regarding {topic, described non-privilegedly}. | {start}–{end} | {list} | A-C; WP where indicated | {legal basis} | {N entries} |
```

### Footnotes / Companion document

- Privilege key: A-C = Attorney-Client; WP = Work Product (Opinion / Ordinary); CI = Common Interest; JD = Joint Defense.
- Role markers: (Attorney) = licensed counsel; (In-house) = in-house counsel; (Agent of counsel) = e.g., paralegal, expert engaged by counsel, investigator; (Client) = officer, director, or employee within the scope of the privilege; (Third party) = non-privileged distribution — flag.
- Common-interest agreement: dated {…}, between {parties}, scope: {…}.
- Litigation anticipation: as of {date} for {matter}.

---

## Verification

- [ ] Every entry has a description sufficient to assess the privilege.
- [ ] No entry uses pure-conclusion phrasing ("privileged communication").
- [ ] Privilege types separately identified per entry.
- [ ] Author and recipient roles marked.
- [ ] Email chains handled per controlling convention.
- [ ] Attachments logged separately where the analysis differs.
- [ ] Carbon-copies-to-counsel are evaluated, not assumed to create privilege.
- [ ] Common-interest claims tied to a documented agreement.
- [ ] Work-product entries identify the anticipated litigation and date.
- [ ] No privileged content disclosed in the descriptions.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Logging a non-privileged business email because counsel was cc'd | Carbon-copying counsel does not create privilege; analyze whether the communication's primary purpose is legal advice |
| Vague descriptions ("privileged communication re: project X") | Add: who, to whom, in what role, for what purpose (described non-privilegedly) |
| Combining attorney-client and work-product without distinguishing what is covered | Identify which content is covered by which privilege |
| Conflating opinion and ordinary work product | Opinion work product (mental impressions) has heightened protection; flag separately |
| Treating in-house counsel communications as automatically privileged | Privilege depends on whether the communication is for legal advice, not business advice |
| Skipping attachments because the parent is privileged | Attachments must be analyzed independently |
| Using a categorical log without basis | Categorical logging requires agreement, order, or justified necessity |
| Forgetting common-interest agreement details | The agreement defines the scope; without it, sharing with a third party can waive |
| Log entries that themselves disclose privileged content | Re-write to describe non-privilegedly |
