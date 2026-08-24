---
name: "app-launch-campaign"
description: "End-to-end launch campaign orchestrator -- generates all assets, timeline, and day-by-day playbook for solo app developers launching on the Google Play Store with zero budget."
metadata:
  type: skill
  category: marketing
  tags:
    - marketing
    - launch
    - campaign
    - solo-developer
  updated: "2026-02-11"
  title: "App Launch Campaign Orchestrator"
---

# App Launch Campaign Orchestrator

## Overview

This skill orchestrates a complete app launch campaign from 8 weeks before launch through 4 weeks after. It generates all required assets (press release, social posts, email sequences, community announcements, store listing copy), produces a week-by-week timeline with specific daily tasks, and provides validation checklists to ensure nothing falls through the cracks.

This is not a planning guide -- it is an execution engine. Feed it your app details, and it produces the actual content, timeline, and task list ready to execute.

## When to Use This Skill

Activate this skill when:
- You have an app ready for launch (or within 8 weeks of launch readiness)
- You need a structured launch plan with all assets generated, not just a strategy document
- You are a solo developer with no marketing team and need a step-by-step execution playbook
- You want to coordinate multiple marketing channels (social, email, community, press, app store) without anything falling through the cracks

Do NOT use this skill when:
- Your app is still in early development (more than 8 weeks from launchable state)
- You are looking for marketing strategy advice (use the strategy prompts instead)
- You want to run a paid advertising campaign (this skill focuses on zero-budget organic tactics)
- You need ongoing marketing support after the launch period (use the social media playbook and content strategy prompts for ongoing operations)

## Prerequisites

Before activating this skill, you should have:

1. **App ready for launch** -- Feature-complete, tested, crash-free rate above 99%
2. **App store assets** -- Screenshots (at least 4), app icon, feature graphic
3. **Landing page** -- Live and functional (see `marketing_landing_page_conversion.md`)
4. **Email list** -- At least a collection mechanism in place (landing page signup or in-app)
5. **Social media presence** -- At least one platform with a profile set up
6. **Value proposition** -- Clear one-sentence description of what makes your app different

If you are missing any of these, the skill will recommend prerequisite steps before proceeding with campaign generation.

## Input Specification

```yaml
app_name: "[Your app name]"
app_description: "[One sentence: what it does and for whom]"
differentiator: "[What makes it different from alternatives]"
launch_date: "[Target launch date: YYYY-MM-DD]"
platforms: "[android | ios | both]"
pricing_model: "[free | freemium | paid | subscription]"
price: "[Price or subscription tiers if applicable]"
target_audience: "[Specific audience description]"
audience_channels:
  - "[Where your audience hangs out online -- subreddits, Discord servers, forums]"
existing_assets:
  email_list_size: [number]
  social_followers: [number]
  beta_testers: [number]
  landing_page_url: "[URL]"
  social_profiles:
    - platform: "[twitter | linkedin | reddit | etc.]"
      handle: "[handle]"
time_budget_weekly: "[hours per week available for marketing]"
comfort_level: "[text | video | both]"  # Content format preference
```

## Workflow: 8-Week Launch Campaign

### Week 1-2: Foundation (8-7 Weeks Before Launch)

**Objective:** Build the marketing foundation -- assets, presence, and positioning.

**Daily Task Breakdown:**

| Day | Task | Time | Output |
|-----|------|------|--------|
| W1 Mon | Finalize positioning statement and messaging framework | 2 hrs | Messaging doc |
| W1 Tue | Set up / optimize social media profiles on 2 platforms | 1 hr | Profiles live |
| W1 Wed | Create or update landing page with email capture | 2 hrs | Landing page live |
| W1 Thu | Write app store listing (title, short desc, full desc) | 2 hrs | Store listing draft |
| W1 Fri | Create press kit (description, screenshots, founder bio, fact sheet) | 2 hrs | Press kit live |
| W2 Mon | Begin "building in public" content -- first post | 1 hr | First BiP post |
| W2 Tue | Research and list 15-20 journalists/bloggers for PR outreach | 2 hrs | Media list |
| W2 Wed | Research and list 10-15 communities for launch announcements | 1 hr | Community list |
| W2 Thu | Set up email tool and create welcome email | 1 hr | Email system ready |
| W2 Fri | Write and schedule 6 social posts for next 2 weeks | 1.5 hrs | Posts scheduled |

### Week 3-4: Audience Building (6-5 Weeks Before Launch)

**Objective:** Build pre-launch audience through content and community engagement.

| Day | Task | Time | Output |
|-----|------|------|--------|
| W3 Mon | Post BiP update #2 (progress, decision, or milestone) | 30 min | Post published |
| W3 Tue | Engage in 3 target communities (help, comment, be visible) | 30 min | Community presence |
| W3 Wed | Send first email to list (app preview, what to expect) | 45 min | Email sent |
| W3 Thu | Post BiP update #3 | 30 min | Post published |
| W3 Fri | Research and prepare beta tester recruitment post | 45 min | Draft ready |
| W4 Mon | Publish beta tester recruitment on 3 channels | 1 hr | Recruitment live |
| W4 Tue | Post BiP update #4 (beta tester feedback theme) | 30 min | Post published |
| W4 Wed | Engage in communities + respond to all beta applications | 45 min | Engaged |
| W4 Thu | Create demo GIF/video of core app experience (30-60 sec) | 1.5 hrs | Demo asset |
| W4 Fri | Onboard first 10-20 beta testers | 1 hr | Beta group active |

### Week 5-6: Beta and Feedback (4-3 Weeks Before Launch)

**Objective:** Collect feedback, testimonials, and build launch assets.

| Day | Task | Time | Output |
|-----|------|------|--------|
| W5 Mon | Check beta feedback, prioritize critical fixes | 1 hr | Bug/fix list |
| W5 Tue | Post BiP update #5 (beta feedback learnings) | 30 min | Post published |
| W5 Wed | Collect 3-5 testimonial quotes from beta testers (with permission) | 45 min | Testimonials |
| W5 Thu | Engage in communities | 30 min | Engaged |
| W5 Fri | Begin drafting press release | 1 hr | Press release draft |
| W6 Mon | Finalize app store listing with beta feedback improvements | 1.5 hrs | Store listing final |
| W6 Tue | Post BiP update #6 (countdown to launch) | 30 min | Post published |
| W6 Wed | Write personalized pitches for top 5 priority journalists | 2 hrs | 5 pitch drafts |
| W6 Thu | Write launch day social posts (all platforms) | 1.5 hrs | Launch posts ready |
| W6 Fri | Write launch day email to subscribers and beta testers | 1 hr | Launch email ready |

### Week 7: Pre-Launch (2 Weeks Before Launch)

**Objective:** Final preparation, begin PR outreach, build anticipation.

| Day | Task | Time | Output |
|-----|------|------|--------|
| W7 Mon | Send PR pitches to Tier 3-4 journalists (niche blogs, YouTube) | 2 hrs | Pitches sent |
| W7 Tue | Post BiP update #7 (launch prep, behind the scenes) | 30 min | Post published |
| W7 Wed | Send PR pitches to Tier 2 journalists (app-focused pubs) | 1.5 hrs | Pitches sent |
| W7 Thu | Submit to Product Hunt (if applicable, schedule hunter) | 1 hr | PH submission |
| W7 Fri | Send "launch is coming" email to full list | 45 min | Email sent |
| W7 Sat | Final app testing, verify all launch assets are ready | 1 hr | Checklist complete |

### Week 8: Launch Week (The Week Of)

**Objective:** Execute launch, maximize first-week momentum.

| Day | Task | Time | Output |
|-----|------|------|--------|
| **L-Day Mon** | Publish app on Play Store. Verify it is live and downloadable. | 1 hr | App live |
| **L-Day Mon** | Send launch email to subscribers + beta testers | 30 min | Email sent |
| **L-Day Mon** | Publish launch posts on all social platforms | 45 min | Posts live |
| **L-Day Mon** | Post in 3-5 relevant communities (Reddit, Discord, forums) | 1.5 hrs | Community posts |
| **L-Day Mon** | Send PR pitches to Tier 1 journalists (major tech pubs) | 1 hr | Pitches sent |
| **L-Day Mon** | Respond to every comment, reply, and review all day | 2+ hrs | All engaged |
| L Tue | Monitor crash reports, respond to reviews | 1 hr | Stable |
| L Tue | Share launch day metrics in BiP update | 30 min | Post published |
| L Wed | Follow up with beta testers: "How's the public version?" | 30 min | Engaged |
| L Thu | Send PR follow-ups (ONE follow-up per journalist) | 1 hr | Follow-ups sent |
| L Fri | Week 1 retrospective: publish "What I Learned Launching" post | 1 hr | Retrospective published |

### Week 9-12: Post-Launch Sustain (Weeks 1-4 After Launch)

**Objective:** Sustain momentum, build habits, transition to ongoing marketing.

**Weekly Rhythm:**

| Day | Recurring Task | Time |
|-----|---------------|------|
| Monday | Check metrics (downloads, reviews, retention, crash rate) | 15 min |
| Monday | Plan content for the week | 15 min |
| Tuesday | Create and publish one piece of content | 1 hr |
| Wednesday | Engage in communities (help, comment, be visible) | 30 min |
| Thursday | Respond to all reviews and support requests | 30 min |
| Friday | Post BiP weekly update with numbers | 30 min |

**Post-launch milestones to announce:**
- First 100 / 500 / 1,000 downloads
- First user testimonial or notable review
- First revenue (for paid/subscription apps)
- First feature shipped based on user feedback
- App store rating milestones (4.0, 4.5 stars)

---

## Templates, Metrics, and Resources

All launch asset templates (Press Release, Social Media: Twitter/Reddit/LinkedIn, Email: subscribers/beta testers, Community Announcement, Store Listing), the pre-launch Validation Checklist, Launch Period KPIs table, Attribution Tracking UTM parameters, Troubleshooting table (6 common issues), and Related Resources (prompts, agents, skills) are in the reference file.

See [references/templates-metrics-and-resources.md](references/templates-metrics-and-resources.md)

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/templates-metrics-and-resources.md` | Launch asset templates (Press Release, Social Media, Email, Community, Store Listing), Validation Checklist, KPIs, Attribution UTMs, Troubleshooting, Related Resources |
