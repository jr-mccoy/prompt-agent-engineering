---
title: "Conversation Analytics Metrics Framework"
category: voice-conversational-ui/analytics
description: "Design a conversation analytics framework with key metrics including task completion rate, fallback rate, turns-to-completion, containment rate, CSAT, instrumentation strategy, and alerting"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - OC-03
  - DS-06
difficulty: intermediate
tags:
  - conversation-analytics
  - metrics
  - task-completion
  - containment-rate
  - csat
  - dashboard
  - alerting
updated: "2026-03-19"
---

# Conversation Analytics Metrics Framework

**Objective:** Design a conversation analytics framework, producing specifications for key performance metrics, instrumentation strategy, dashboard design, and alerting thresholds for monitoring conversational AI health and effectiveness.

**When to Use:**
- Use when: Launching a chatbot or voice assistant and need to measure success
- Use when: Existing bot lacks visibility into performance
- Use when: Building a business case for chatbot investment (need ROI metrics)
- Use when: Operations team needs dashboards and alerts
- Don't use when: Analyzing specific conversation logs (use `analytics_conversation_optimization.md`)

## Instructions

1. **Define Core Metrics**
   Establish the metrics that matter for your conversational AI:

   **Task Completion Metrics:**
   - **Task completion rate**: % of conversations where user goal was achieved
   - **Self-service rate (containment)**: % resolved without human intervention
   - **First-contact resolution**: % resolved in a single conversation session
   - **Abandonment rate**: % of users who leave mid-conversation

   **Efficiency Metrics:**
   - **Turns to completion**: Average turns to resolve a task
   - **Time to resolution**: Wall-clock time from start to resolution
   - **Deflection rate**: % of queries handled by bot vs total support volume

   **Quality Metrics:**
   - **Fallback rate**: % of turns where bot couldn't understand
   - **Escalation rate**: % of conversations handed to human agents
   - **CSAT (Customer Satisfaction)**: Post-conversation survey score
   - **NPS or CES**: Net Promoter Score or Customer Effort Score

   **Operational Metrics:**
   - **Response time**: Bot response latency (p50, p95, p99)
   - **Uptime**: System availability percentage
   - **Concurrent conversations**: Peak load handling
   - **Error rate**: System errors (API failures, timeouts)

2. **Design Instrumentation Strategy**
   Define what to log and where:
   - **Conversation events**: Start, end, intent, entity, slot fill, handoff
   - **System events**: API calls, errors, timeouts, latency
   - **User events**: Input type, feedback, satisfaction rating
   - **Contextual metadata**: Channel, device, user segment, time of day
   - **Privacy**: What NOT to log (PII handling, data retention policy)

3. **Build Dashboard Design**
   - **Executive dashboard**: KPIs, trends, ROI metrics
   - **Operations dashboard**: Real-time health, error rates, response times
   - **Product dashboard**: Intent popularity, flow completion, user journeys
   - **NLU dashboard**: Confidence distributions, confusion patterns, fallback analysis
   - Refresh frequency: Real-time for ops, daily for product, weekly for executive

4. **Set Alerting Thresholds**
   Define alert rules:
   - **Critical**: Fallback rate >30%, response time >5s, error rate >5%
   - **Warning**: Fallback rate >20%, CSAT <3.5, containment <50%
   - **Info**: New intent patterns detected, volume spike
   - Alert channels: PagerDuty, Slack, email based on severity
   - Escalation path: Who gets notified at each level

5. **Design Reporting Cadence**
   - **Daily**: Automated health summary (volume, errors, CSAT)
   - **Weekly**: Performance trends, top failed intents, improvement opportunities
   - **Monthly**: Business impact report (deflection savings, CSAT trends)
   - **Quarterly**: Strategic review (roadmap alignment, competitive benchmarking)

6. **Plan Metric Collection Architecture**
   - Event pipeline: How events flow from bot to analytics
   - Storage: Time-series DB for metrics, data warehouse for analysis
   - Processing: Real-time (alerting) vs batch (reporting)
   - Visualization: Grafana, Looker, custom dashboards
   - Integration: Connect to existing BI tools

7. **CRITICAL: Validate the framework**
   - Ensure metrics align with business objectives
   - Verify instrumentation captures all needed events
   - Test alerting with simulated degradation
   - Confirm dashboards are actionable (not just informational)
   - Check that privacy requirements are met
   - **Confidence**: High (production-validated), Medium (designed), Low (theoretical)

## False-Positive Prevention (MUST follow)

- **DON'T** track vanity metrics (total conversations) without quality metrics
- **DON'T** measure only bot performance — include the full user journey
- **DON'T** set thresholds without baseline data (collect first, then set)
- **DON'T** log PII in analytics (anonymize or redact)
- **DO** tie metrics to business outcomes (cost savings, customer satisfaction)
- **DO** track metrics per intent/flow, not just globally (global averages hide problems)
- **DO** include user satisfaction as a first-class metric, not an afterthought

## Expected Output

```markdown
## Conversation Analytics Framework: [Bot Name]

### Metric Definitions
| Metric | Formula | Target | Current | Status |
|--------|---------|--------|---------|--------|
| Task completion | completed / total conversations | >75% | - | Pending baseline |
| Containment rate | self-served / total | >65% | - | Pending baseline |
| Fallback rate | fallback turns / total turns | <15% | - | Pending baseline |
| Avg turns to complete | sum(turns) / completed | <5 | - | Pending baseline |
| CSAT | avg(survey_score) | >4.0/5 | - | Pending baseline |
| Response time (p95) | 95th percentile latency | <2s | - | Pending baseline |

### Instrumentation Schema
| Event | Fields | Privacy |
|-------|--------|---------|
| conversation.start | session_id, channel, user_segment, timestamp | No PII |
| intent.detected | session_id, intent, confidence, entities (anonymized) | Entities redacted |
| conversation.end | session_id, outcome, duration, turns | No PII |
| user.feedback | session_id, rating, comment (optional, anonymized) | Comment anonymized |

### Dashboard Specifications
| Dashboard | Audience | Refresh | Key Widgets |
|-----------|----------|---------|-------------|
| Executive | Leadership | Weekly | KPI cards, trend lines, ROI |
| Operations | Bot team | Real-time | Error rate, latency, volume |
| Product | Product team | Daily | Intent heatmap, flow funnel |

### Alert Configuration
| Alert | Condition | Severity | Channel | Escalation |
|-------|-----------|----------|---------|------------|
| High fallback | >30% for 15min | Critical | PagerDuty | Bot team on-call |
| Slow response | p95 >5s for 5min | Critical | PagerDuty | Infrastructure |
| Low CSAT | <3.0 daily avg | Warning | Slack | Product team |
| Volume spike | >2x normal | Info | Slack | Bot team |
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Analytics framework design
- **ST-02 (Structured Sequential Instructions):** Metrics → instrumentation → dashboards → alerts
- **RT-02 (Multi-Dimensional Analysis):** Task, efficiency, quality, operational dimensions
- **OC-03 (Structured Output):** Metric tables, dashboard specs, alert rules
- **DS-06 (Prioritization Guidance):** Severity-based alerting

## Customization Guide

- **For Customer Service Bots**: Emphasize containment, CSAT, escalation metrics
- **For Voice Assistants**: Add voice-specific metrics (ASR accuracy, no-input rate)
- **For Internal Tools**: Focus on efficiency metrics, less on CSAT
- **For E-commerce**: Add conversion rate, cart abandonment, revenue attribution
