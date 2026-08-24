---
title: "Solo Developer Support System"
category: startup/business-operations
description: "Design a scalable user support system for a one-person app business — help center content, in-app support flows, email templates by category, triage system, response time expectations, and tool selection — with FAQ templates, triage matrix, and scaling triggers"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - CM-02
  - DS-06
difficulty: intermediate
tags:
  - solo-developer
  - startup
  - customer-support
  - user-experience
  - android
  - help-center
  - triage
updated: "2026-02-11"
---

# Solo Developer Support System

**Objective:** Design a complete user support system that one person can operate — from self-service help content and in-app support flows that deflect most questions before they reach you, to email templates for common categories, a triage system for prioritization, response time expectations that are honest about your capacity, and tool selection — producing a support workflow that keeps users happy without consuming all of your time.

**When to Use:** Use this prompt when you start receiving regular support emails and realize you need a system instead of ad-hoc responses, when bad reviews mention "developer doesn't respond," when you're spending more than an hour a day on support and it's eating into development time, or when you want to proactively set up support before launching to avoid scrambling later.

**Important context:** Support is the task that solo developers most often neglect — and it's the one that most directly affects your app's rating, retention, and reputation. A 1-star review that says "app crashed, developer never responded" does more damage than a 1-star review that says "app crashed, but developer fixed it in 2 days." The goal is not to provide 24/7 enterprise support. The goal is to build a system where 80% of questions are answered without you, and the 20% that reach you get a thoughtful response within 48 hours. That's achievable for one person.

---

## Context Gathering

Before designing your support system, understand your current situation:

1. **Current Support Volume:**
   - "How many support requests do you receive per week (email, reviews, social media)?"
   - "What are the top 3-5 topics people contact you about?"
   - "How much time do you currently spend on support per week?"
   - "Are you responding to all requests, or are some falling through the cracks?"

2. **App Characteristics:**
   - "Does your app handle payments or subscriptions?"
   - "Does your app require account creation?"
   - "Does your app store user data that could be lost?"
   - "Is your app in a regulated industry (health, finance, education)?"

3. **User Profile:**
   - "How technical are your typical users?"
   - "What age range is your primary audience?"
   - "Do your users speak primarily English, or is your app multilingual?"
   - "Where do users currently go when they have a problem (email, review, social media, in-app)?"

4. **Support Goals:**
   - "What response time do you want to target?"
   - "Are you willing to invest in a support tool, or do you want to start with free options?"
   - "Do you have any existing help content (FAQ, help articles)?"
   - "At what support volume would you consider hiring someone or adding a chatbot?"

---

## Instructions

### CRITICAL: Verification Requirements

1. **Self-service content must actually answer the question** — FAQs that restate the question without solving the problem are worse than no FAQ at all. Test every article by asking "would this solve my problem if I were an annoyed user?"
2. **Response time commitments must be ones you can actually keep** — Promising 24-hour response times when you also have a day job and a life is setting yourself up for failure. Under-promise, over-deliver.
3. **Triage priorities must reflect real impact** — A billing issue affecting a paying customer is always higher priority than a feature request, regardless of how loud the requester is.
4. **Email templates must sound human** — Templates that feel robotic ("Your request has been received and assigned ticket #47829") make users feel unvalued. Write like a person.
5. **Tool recommendations must match the developer's actual volume** — Don't recommend Zendesk ($55/month/agent) for someone getting 5 support emails a week.
6. **Acceptable null result:** If the developer is getting fewer than 5 support requests per month, a full support system is premature. A simple FAQ page and a dedicated email address may be sufficient.

### False-Positive Prevention

- Do NOT recommend building a custom support portal before you've proven the need with simpler tools
- Do NOT set up auto-responses that promise things you can't deliver ("we'll get back to you within 2 hours")
- Do NOT treat all support requests equally — paying customers and data-loss issues deserve faster response than "can you add dark mode?"
- Do NOT recommend chatbots for apps with fewer than 100 support requests per month — the setup cost exceeds the time savings
- Do NOT ignore Google Play reviews as a support channel — many users leave reviews instead of emailing
- Do NOT write FAQ content that uses jargon your users won't understand
- DO acknowledge that response time is more important than response perfection — a fast "I'm looking into this" beats a slow detailed response
- DO design the support flow to reduce volume, not just manage it
- DO include canned responses that can be personalized in 30 seconds
- DO plan for the support surge after every app update (new bugs, changed UI, confused users)

---

### Phase 1: Self-Service Foundation

#### 1.1 The 80/20 Rule of Support

In most apps, 80% of support requests fall into 5-10 categories. If you create good self-service content for those categories, you can deflect most requests before they reach your inbox.

**Step 1: Identify your top support categories.**

Audit your last 30-50 support interactions (emails, reviews, social media messages) and categorize them:

```markdown
## Support Category Audit

| Category | # of Requests | % of Total | Self-Service Possible? |
|----------|--------------|-----------|----------------------|
| How to [common task] | ________ | ________% | Yes — tutorial/guide |
| Bug report: [specific bug] | ________ | ________% | Partial — known issue page |
| Feature request | ________ | ________% | Yes — roadmap page |
| Billing/subscription issue | ________ | ________% | Partial — billing FAQ |
| Account/login problem | ________ | ________% | Yes — account FAQ |
| Data loss/recovery | ________ | ________% | Partial — backup guide |
| Crash/performance issue | ________ | ________% | Partial — troubleshooting guide |
| "How does [feature] work?" | ________ | ________% | Yes — feature guide |
| Other | ________ | ________% | Varies |
```

#### 1.2 FAQ Content Template

For each of your top categories, create an FAQ entry using this structure:

```markdown
## [Question — written exactly how a user would ask it]

**Short answer:** [1-2 sentence direct answer]

**Detailed steps:**
1. [Step 1 with specific instructions]
2. [Step 2 with specific instructions]
3. [Step 3 with specific instructions]

**Screenshots:** [Include if the steps involve UI navigation]

**Still having trouble?** [Link to contact support with pre-filled category]
```

**Good FAQ example:**
```markdown
## How do I cancel my subscription?

**Short answer:** You can cancel your subscription through the Google Play Store
app on your phone. The developer (us) cannot cancel subscriptions on your behalf —
Google manages all subscription billing.

**Steps to cancel:**
1. Open the Google Play Store app on your Android device
2. Tap your profile icon in the top right
3. Tap "Payments & subscriptions"
4. Tap "Subscriptions"
5. Find [Your App Name] and tap it
6. Tap "Cancel subscription"
7. Follow the prompts to confirm

**Important:** Canceling stops future charges but does not trigger a refund for
the current billing period. You'll retain access until the end of your current
billing cycle.

**Still having trouble?** Contact us at support@yourapp.com with subject line
"Subscription Issue" and include your Google Play order number (starts with
GPA.xxxx).
```

**Bad FAQ example (avoid this):**
```markdown
## Subscriptions

For subscription management, please refer to Google Play Store's subscription
management interface. Subscriptions are handled by the platform provider.
```

This is technically accurate but useless to a frustrated user. Write for humans, not documentation robots.

#### 1.3 Help Center Structure

Organize your help content into sections that match how users think:

```markdown
## Help Center Structure

### Getting Started
- How to create an account
- How to set up [core feature]
- Quick start guide (first 5 minutes)

### Using [App Name]
- How to [primary action 1]
- How to [primary action 2]
- How to [primary action 3]
- Tips and shortcuts

### Billing & Subscriptions
- How to subscribe / upgrade
- How to cancel your subscription
- How to request a refund
- Understanding your billing cycle
- Why was I charged?

### Account & Privacy
- How to reset your password
- How to export your data
- How to delete your account
- What data do you collect?
- Privacy policy (plain language summary)

### Troubleshooting
- App crashes on startup
- Feature X isn't working
- Sync isn't working
- Performance is slow
- Known issues and workarounds

### Feature Requests & Feedback
- How to suggest a feature
- Current roadmap / planned features
- How we prioritize features
```

#### 1.4 Where to Host Your Help Center

| Option | Cost | Complexity | Best For |
|--------|------|-----------|----------|
| **In-app FAQ screen** | Free | Low | Small help sections (10-20 articles) |
| **GitHub Pages / static site** | Free | Low-Medium | Developer-comfortable, markdown-based |
| **Notion public page** | Free | Low | Quick setup, easy to update |
| **Gitbook** | Free-$8/month | Low | Documentation-style help center |
| **Freshdesk knowledge base** | Free tier | Medium | If also using Freshdesk for tickets |
| **Zendesk Guide** | $55+/month | Medium | Enterprise-grade (overkill for most solo devs) |
| **Custom web page** | Free-$20/month | Medium | Full control over design |

**Recommendation for most solo developers:** Start with an in-app FAQ screen for the top 10 questions, plus a simple web page (Notion or static site) for the full help center. Link from the app to the web help center for detailed articles.

---

### Phase 2: In-App Support Flow Design

#### 2.1 The Support Funnel

Design your in-app support to resolve issues before the user needs to contact you:

```
User has a problem
    ↓
[STEP 1] In-app FAQ / Help screen
    → Answers question? → RESOLVED (no contact needed)
    ↓ (not answered)
[STEP 2] Search help articles
    → Finds answer? → RESOLVED
    ↓ (not found)
[STEP 3] Category selection
    → User picks: Bug Report / Feature Request / Billing / Account / Other
    ↓
[STEP 4] Category-specific self-help
    → Shows targeted troubleshooting for that category
    → Answers question? → RESOLVED
    ↓ (still not resolved)
[STEP 5] Contact form with pre-filled context
    → Category already selected
    → Device info auto-attached
    → App version auto-attached
    → User describes issue
    → SUBMITTED → email to your support inbox
```

**Why this funnel matters:** Each step filters out users whose questions can be answered without your involvement. A well-designed funnel deflects 60-80% of would-be support contacts.

#### 2.2 Auto-Collected Context

When a user does reach the contact step, automatically collect information that saves you from asking follow-up questions:

```markdown
## Auto-Collected Support Context

- App version: [e.g., 2.3.1 (build 47)]
- Android version: [e.g., Android 14]
- Device model: [e.g., Pixel 8 Pro]
- Device locale: [e.g., en-US]
- Account type: [Free / Premium / Trial]
- Account creation date: [e.g., 2025-09-15]
- Last crash date (if any): [from Crashlytics]
- Screen the user was on: [if trackable]
```

This data saves 1-2 back-and-forth emails per support request. Over 50 requests a month, that's 50-100 emails you don't have to send.

#### 2.3 In-App Support UI Guidelines

| Element | Do | Don't |
|---------|-----|-------|
| **Access point** | Settings → Help & Feedback | Bury it 5 levels deep |
| **Visibility** | Always accessible from main navigation | Only show when user complains |
| **Search** | Include if you have 10+ help articles | No search for 5 articles |
| **Tone** | "We're here to help" | "Submit a ticket" (corporate) |
| **Response expectation** | "We typically respond within 48 hours" | Nothing (user assumes instant) |
| **Confirmation** | Show "Message sent" with expected timeline | No confirmation (user wonders if it worked) |

---

### Phase 3: Triage and Templates

#### 3.1 Triage Matrix

Not all support requests are equal. Prioritize by urgency and impact:

| Priority | Label | Description | Response Target | Examples |
|----------|-------|-------------|----------------|---------|
| **P1** | Critical | Data loss, security issue, widespread crash, billing error (user charged incorrectly) | Same day (within 12 hours) | "I lost all my data," "I was double-charged," "App crashes immediately on open" |
| **P2** | High | Paying customer blocked, feature broken for subset of users, compliance-related | Within 24 hours | "Premium feature not working," "Can't access my account," "Sync stopped working" |
| **P3** | Medium | Non-blocking bug report, free user support request, how-to question not covered by FAQ | Within 48 hours | "Minor UI glitch," "How do I export my data?", "Feature doesn't work as expected" |
| **P4** | Low | Feature request, general feedback, nice-to-have improvements | Within 1 week (or batched) | "Can you add dark mode?", "It would be cool if...", "Love the app!" |

**Triage rules:**
1. Any mention of "data loss," "charged," "security," or "crash" → auto-classify as P1 or P2
2. Paying customers get +1 priority bump over free users for the same issue
3. Multiple reports of the same issue → bump priority (widespread problem)
4. Feature requests are always P4 unless they come from a paying customer with churn risk

#### 3.2 Email Response Templates

**Template 1: Bug Report Acknowledgment (P1-P2)**

```
Subject: Re: [Original subject]

Hi [Name],

Thanks for reporting this — I'm sorry you're running into trouble.

I can see from your message that [brief restatement of their issue]. I'm looking
into this now and will follow up with more information [within 24 hours / by end
of day / by tomorrow].

In the meantime, [specific workaround if one exists, e.g., "try clearing the
app cache: Settings → Apps → [App Name] → Storage → Clear Cache"].

If you have any additional details (screenshots, steps to reproduce, or when it
started happening), that would help me track this down faster.

Thanks for your patience,
[Your name]
```

**Template 2: Bug Report Resolution**

```
Subject: Re: [Original subject]

Hi [Name],

Good news — I found and fixed the issue you reported. [1-2 sentence explanation
of what went wrong in plain language].

The fix is included in version [X.Y.Z], which [is now available on the Play
Store / will be available within 24-48 hours]. Update your app and the issue
should be resolved.

If you're still experiencing the problem after updating, please let me know
and I'll dig deeper.

Thanks for reporting this — bug reports from users like you help make the app
better for everyone.

[Your name]
```

**Template 3: Feature Request Acknowledgment (P4)**

```
Subject: Re: [Original subject]

Hi [Name],

Thanks for the suggestion! [Brief acknowledgment showing you understood what
they're asking for].

I keep a list of all feature requests and factor them into my planning. I can't
promise a specific timeline for this one, but I want you to know it's been heard
and noted.

[If relevant: "This is actually something several users have asked about, so
it's on my radar." OR "I hadn't thought about this use case — interesting idea."]

If you're curious about what's coming next, [link to roadmap or changelog].

Thanks for taking the time to share this,
[Your name]
```

**Template 4: Billing / Subscription Issue (P1-P2)**

```
Subject: Re: [Original subject]

Hi [Name],

I understand the frustration — billing issues are never fun. Let me help sort
this out.

[For subscription cancellation:]
Subscriptions are managed through Google Play, so I'm not able to cancel or
refund directly from my side. Here are the steps:
1. Open Google Play Store → Profile → Payments & subscriptions → Subscriptions
2. Find [App Name] and tap "Cancel subscription"

[For refund request:]
For a refund, you can request one through Google Play:
1. Go to play.google.com/store/account/orderhistory
2. Find the charge and click "Request a refund"

Google typically processes refund requests within 1-4 business days.

[For double-charge:]
I'm looking into this. Can you send me the Google Play order numbers (they start
with GPA.xxxx) for both charges? I can investigate on my end and escalate to
Google if needed.

Let me know if you need anything else,
[Your name]
```

**Template 5: Account / Data Recovery (P1)**

```
Subject: Re: [Original subject]

Hi [Name],

I'm sorry to hear about this — I know losing [data/access] is stressful.

[If data backup exists:]
Good news: your data is backed up on our servers. I can help you restore it.
Can you confirm the email address associated with your account? Once verified,
I'll walk you through the recovery process.

[If no data backup:]
I want to be upfront with you: [App Name] currently stores data locally on
your device, and [we don't have / I don't have] a server-side backup of your
data. [If factory reset / app uninstall:] Unfortunately, that means the data
from before the [reset/uninstall] may not be recoverable.

I know that's not what you want to hear, and I'm sorry. [If applicable: "This
experience is exactly why I'm building cloud sync for a future update — so
this can't happen again."]

Is there anything else I can help with?

[Your name]
```

**Template 6: Positive Feedback / Review Thank You (P4)**

```
Subject: Re: [Original subject] — Thank you!

Hi [Name],

This made my day — thank you for the kind words! I'm a solo developer and
hearing that [specific thing they mentioned] means a lot.

If you have a moment, a review on the Play Store goes a long way in helping
other people discover the app. [Only include if they haven't already left a
review.]

Thanks for being a [App Name] user,
[Your name]
```

#### 3.3 Template Personalization Rules

Templates save time, but they must feel human. Follow these rules:

| Rule | Example |
|------|---------|
| **Always use their name** | "Hi Sarah" not "Hi there" or "Dear User" |
| **Restate their specific issue** | "the crash you're seeing when exporting PDFs" not "your reported issue" |
| **Add one personal sentence** | "I can see why that would be annoying" or "Great catch on finding that" |
| **Match their tone** | Casual user → casual response. Formal user → professional response. |
| **Sign with your name** | Users trust a person more than a brand |

Time to personalize a template: 30 seconds. Impact on user perception: enormous.

---

### Phase 4: Tool Selection

#### 4.1 Support Tool Comparison

| Tool | Cost | Best For | Key Features | Limitations |
|------|------|----------|-------------|------------|
| **Gmail + Labels** | Free | < 20 requests/month | Simple, no learning curve, labels for categories | No collaboration, no metrics, no automation |
| **Gmail + Google Sheets tracker** | Free | 20-50 requests/month | Track status manually, basic reporting | Manual data entry, no templates |
| **Freshdesk** | Free (up to 2 agents) | 20-100 requests/month | Ticketing, canned responses, knowledge base, reporting | Free tier limited features |
| **Zendesk** | $19-$55/agent/month | 50+ requests/month | Full-featured help desk, automations, analytics | Expensive for one person, complex setup |
| **Help Scout** | $20/user/month | 30-100 requests/month | Email-like interface, knowledge base, beacon widget | Paid only, no free tier |
| **Crisp** | Free (basic) | 20-80 requests/month | Live chat widget, chatbot, knowledge base | Free tier limited to 1 seat |
| **Intercom** | $74+/month | 100+ requests/month, SaaS apps | Powerful, product tours, chatbot | Expensive, enterprise-focused |
| **Notion + email** | Free | < 20 requests/month | Flexible, use as both FAQ and issue tracker | Manual, no email integration |

#### 4.2 Recommended Tool Progression

| Monthly Request Volume | Recommended Tool | Estimated Monthly Cost |
|-----------------------|-----------------|----------------------|
| 0-20 requests | Gmail with labels + Notion FAQ | $0 |
| 20-50 requests | Freshdesk Free + in-app FAQ | $0 |
| 50-100 requests | Freshdesk Free or Help Scout | $0-$20 |
| 100-200 requests | Help Scout or Zendesk | $20-$55 |
| 200+ requests | Consider hiring part-time support + Zendesk | $55+ plus contractor cost |

**Don't over-engineer your support tooling.** Gmail with labels works fine for most solo developers in the first year. Upgrade to a ticketing system when you're spending more time managing email than responding to it.

#### 4.3 Essential Tool Features Checklist

When evaluating any support tool, check for:

- [ ] **Canned responses / templates** — Pre-written replies you can personalize
- [ ] **Tagging / categorization** — Classify requests by type (bug, feature, billing)
- [ ] **Status tracking** — Open, pending, resolved
- [ ] **Search** — Find past conversations quickly
- [ ] **Basic reporting** — Volume over time, response times, category breakdown
- [ ] **Knowledge base** — Built-in FAQ/help center hosting
- [ ] **Mobile access** — Respond from your phone when needed
- [ ] **Email integration** — Works with your existing support email address

---

### Phase 5: Scaling Triggers

#### 5.1 When to Upgrade Your Support System

| Trigger | What It Means | Action |
|---------|--------------|--------|
| **> 1 hour/day on support** | Support is eating into development time | Improve self-service content, add templates |
| **> 50 requests/month** | Volume exceeds casual email management | Move to a ticketing tool (Freshdesk) |
| **Same questions keep repeating** | FAQ gaps or poor discoverability | Update FAQ, improve in-app help flow |
| **Response time slipping past 72 hours** | You're falling behind | Batch support into dedicated time blocks, consider chatbot |
| **> 100 requests/month** | One person is getting stretched | Consider part-time support contractor |
| **Negative reviews mention "no response"** | Support gaps are hurting your rating | Prioritize review responses, set up alerts |
| **Paying customers churning due to support** | Revenue impact | This is a P1 business issue — address immediately |

#### 5.2 When to Add a Chatbot

Chatbots can be helpful but are often added too early. Here's when they actually make sense:

**Add a chatbot when:**
- You're getting 100+ requests/month with high repetition
- 60%+ of requests can be answered by existing FAQ content
- You've already optimized your FAQ and in-app help flow
- You have budget for a quality chatbot tool ($50-$200/month)

**Don't add a chatbot when:**
- Your request volume is low (< 50/month)
- Most requests are unique (bugs, account-specific issues)
- You haven't built out FAQ content yet (a chatbot needs content to draw from)
- Your users are non-technical and may find chatbots frustrating

| Chatbot Tool | Cost | Best For |
|-------------|------|----------|
| **Freshdesk Freddy** | Included in paid plans | Freshdesk users |
| **Crisp Bot** | Free tier available | Simple FAQ deflection |
| **Intercom Fin** | $0.99/resolution | SaaS apps with high volume |
| **Custom (Dialogflow)** | Free-$0.007/request | Developers who want full control |

#### 5.3 When to Hire a Support Contractor

| Factor | DIY Threshold | Hire Threshold |
|--------|--------------|----------------|
| **Monthly volume** | < 100 requests | > 100 requests consistently |
| **Time spent** | < 5 hours/week | > 5 hours/week |
| **Impact on development** | Manageable | Features are delayed |
| **Response quality** | Consistent | Declining (rushed responses) |
| **Your enjoyment** | Tolerable | Dreading it |

**What to outsource first:** Tier 1 support (how-to questions, common issues, billing questions). Keep escalated issues (bugs, data loss, complex technical issues) for yourself. A support contractor with good templates and FAQ access can handle 80% of volume.

**Typical cost:** $15-$25/hour for a part-time support contractor, or $500-$1,000/month for 10-20 hours per week.

---

### Phase 6: Google Play Review Management

#### 6.1 Why Reviews Are a Support Channel

Many users leave reviews instead of sending emails. These reviews are public, permanent, and affect your app's discoverability. Responding to reviews is both a support function and a marketing function.

#### 6.2 Review Response Strategy

| Star Rating | Response Priority | Template Approach |
|-------------|------------------|-------------------|
| **1 star** | High — respond within 24-48 hours | Acknowledge, apologize, ask to contact you directly |
| **2 star** | Medium — respond within 48 hours | Acknowledge specific issue, offer solution |
| **3 star** | Medium — respond within 48 hours | Thank for feedback, address concerns |
| **4 star** | Low — batch weekly | Thank them, note their suggestion |
| **5 star** | Low — batch weekly | Genuine thank you |

**1-Star Review Response Template:**
```
Hi [Name], I'm sorry [App Name] let you down. [Address their specific concern
in 1 sentence]. I'd like to help fix this — could you email me at
support@yourapp.com so I can look into your specific situation? I want to
make this right.
```

**Key rules:**
- Never argue with a reviewer in public
- Never make excuses — take ownership
- Always provide a path to resolution (email, help article)
- Keep responses short (under 100 words)
- Respond to negative reviews before positive ones

#### 6.3 Review Monitoring

Set up Google Play Console notifications for new reviews. Check reviews at least twice per week as part of your batch processing.

---

## Expected Output

```markdown
# Support System Design: [App Name]

## Support Volume Assessment
- Current monthly requests: [N]
- Top categories:
  1. [Category] — [N] requests ([%])
  2. [Category] — [N] requests ([%])
  3. [Category] — [N] requests ([%])
- Self-service deflection target: [%]

## Self-Service Content

### Help Center
- Platform: [Notion / In-app / Static site]
- URL: [link]
- Articles created: [N]
- Top articles:
  - [Article 1 — addressing top support category]
  - [Article 2]
  - [Article 3]

### In-App Support Flow
- Access point: [Settings → Help / FAB / etc.]
- Steps: FAQ → Search → Category Select → Troubleshooting → Contact
- Auto-collected context: [App version, device, account type, etc.]

## Triage System

| Priority | Response Target | Criteria |
|----------|----------------|----------|
| P1 | Within 12 hours | [Your specific criteria] |
| P2 | Within 24 hours | [Your specific criteria] |
| P3 | Within 48 hours | [Your specific criteria] |
| P4 | Within 1 week | [Your specific criteria] |

## Templates Created
- [ ] Bug report acknowledgment
- [ ] Bug report resolution
- [ ] Feature request acknowledgment
- [ ] Billing / subscription issue
- [ ] Account / data recovery
- [ ] Positive feedback thank you

## Tooling
- Current tool: [Gmail / Freshdesk / etc.]
- Support email: [support@yourapp.com]
- Upgrade trigger: [specific volume or time threshold]

## Time Allocation
- Support batch days: [e.g., Wednesday and Thursday afternoons]
- Time per batch: [e.g., 30 minutes]
- Review response day: [e.g., Monday and Thursday]
- Monthly review of support metrics: [1st Monday]

## Scaling Plan
- At [N] requests/month: [Upgrade tool]
- At [N] requests/month: [Add chatbot]
- At [N] requests/month: [Hire support contractor]
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused on building a complete support system for one person
- **ST-02** (Structured Sequential Instructions) — Phased approach from self-service through scaling
- **RT-02** (Multi-Dimensional Analysis) — Analyzing support across channels, priorities, tools, and volume dimensions
- **CM-01** (Explicit Context Framing) — Solo developer constraints: limited time, no support team, need for automation
- **CM-02** (Constraint Specification) — Time constraints, budget constraints, volume thresholds
- **DS-06** (Prioritization Guidance) — Triage matrix and scaling triggers ordered by impact

---

## Related Prompts

- `solo_dev_weekly_operating_rhythm.md` — Scheduling support batch time in your weekly rhythm
- `solo_dev_metrics_dashboard.md` — Tracking support volume and response time as business metrics
- `solo_dev_decision_framework.md` — Deciding when to invest in support tools vs. development time
- `solo_dev_contractor_management.md` — Hiring a part-time support contractor when volume justifies it
- `solo_dev_roadmap_planner.md` — Incorporating support-driven feature requests into your roadmap

---

## Customization Guide

- **For pre-launch apps:** Build your FAQ before launch, even if it's just 5 articles covering the basics. Write your email templates. Set up a support email address. You'll be glad you did when the first users arrive with questions.
- **For apps with in-app purchases / subscriptions:** Billing-related support is your highest priority. Users who are confused about charges or can't cancel are at high risk of leaving 1-star reviews AND filing chargebacks. Make billing FAQs prominent and easy to find.
- **For apps serving non-technical users:** Use simpler language in all support content. Include screenshots in every help article. Avoid technical jargon entirely. Consider adding a "Getting Started" walkthrough in the app to reduce first-time confusion.
- **For apps with multilingual users:** Start with English-only support and be transparent about it. "Our support is currently available in English. We're working on adding more languages." Use simple, clear English that translates well in Google Translate for non-English speakers.
- **For apps with high crash rates:** Your priority is fixing crashes, not answering support emails about crashes. Every crash-related support email is a signal to prioritize stability in your development roadmap. Add a "Known Issues" section to your help center and update it honestly.
- **For developers who dread support:** Reframe it as user research. Every support conversation teaches you something about how people use your app, what confuses them, and what they wish it could do. The insights from 50 support conversations are worth more than any analytics dashboard. Batch it, template it, and it becomes manageable.
