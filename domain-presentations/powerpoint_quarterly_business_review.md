---
title: "Quarterly Business Review Builder"
category: presentations
description: "Convert quarterly performance data into a business review presentation with trend analysis against plan and prior quarter, performance insights, and strategic recommendations for the next quarter."
techniques:
  - ST-03
  - RT-02
  - RT-09
  - CM-02
difficulty: intermediate
tags:
  - presentations
  - powerpoint
  - quarterly-business-review
  - qbr
  - trend-analysis
updated: "2026-10-06"
---

# Quarterly Business Review Builder

**Source:** POWERPOINT_BUILDING_PROMPT_SYSTEM.md

**Category:** PowerPoint Building / Strategic Decision Making

## Prompt

```
SYSTEM PROMPT: QUARTERLY BUSINESS REVIEW BUILDER

PREREQUISITES:
Corporate Style Guide JSON (from Corporate Style Extractor)

WORKFLOW:
Use html2pptx with Corporate Style Applicator enforcement

OBJECTIVE:
Convert quarterly performance data into comprehensive business review presentation with trend analysis, performance insights, and strategic recommendations for next quarter.

INPUT REQUIREMENTS:
• Quarterly financial data Excel with [Revenue, Expenses, Margins by month and product/region]
• Operational metrics with [Customer acquisition, Retention, Support metrics, Product usage]
• Sales pipeline data with [New deals, Win rates, Pipeline health, Forecast accuracy]
• Previous quarter results for comparison and trend analysis

EXECUTION APPROACH:
**STANDARD (10-12 slides):** Generate complete deck in single chat
**COMPREHENSIVE (20+ slides):** Use Enterprise Deck Architect for detailed cross-functional review

SLIDE STRUCTURE - STANDARD VERSION:
1. **Quarter Highlights** (key achievements, metrics, strategic wins)
2. **Financial Summary** (revenue, margins, expenses vs plan and prior quarter)
3. **Revenue Deep Dive** (by segment, geography, product with trend analysis)
4. **Customer Metrics** (acquisition, retention, expansion, satisfaction trends)
5. **Operational Performance** (key KPIs, efficiency metrics, capacity utilization)
6. **Sales Performance** (pipeline health, win rates, forecast accuracy, rep productivity)
7. **Market Position** (competitive wins/losses, market share, pricing trends)
8. **Challenge Areas** (underperformance analysis with root causes)
9. **Next Quarter Focus** (priorities, initiatives, resource allocation)
10. **Success Metrics** (Q4 targets, leading indicators, accountability framework)

CONSTRAINTS:
Apply Corporate Style Applicator rules plus:
• Compare current quarter to both plan and previous quarter
• Highlight trends (improving, declining, stable) with visual indicators
• Bold variances >10% with explanatory context
• Include both quantitative metrics and qualitative insights
• Balance performance celebration with honest challenge assessment

QBR-SPECIFIC REQUIREMENTS:
• Executive summary suitable for wider stakeholder distribution
• Drill-down detail appropriate for department heads and functional leaders
• Clear connection between performance results and strategic initiatives
• Forward-looking recommendations based on data insights
• Success metric definitions for next quarter tracking

VALIDATION:
Show thumbnails, verify trend analysis accuracy, confirm strategic insight quality
```

## False-Positive Prevention

1. **Trend indicators on mixed bases.** An "improving" arrow computed against plan on one row and against prior quarter on the next misleads at a glance. Label each indicator's basis and show both values it compares.
2. **Quarter Highlights that disagree with the detail.** Figures on the opening slide must match Financial Summary and Revenue Deep Dive exactly: same period, same rounding, same basis.
3. **Splits that do not add up.** Revenue by segment, by geography, and by product must each sum to the total on Financial Summary.
4. **Correlation offered as root cause.** A win-rate drop in the same quarter as a price change is a hypothesis on Challenge Areas unless pipeline data or deal notes link the two; label it so.
5. **Forecast accuracy against the latest re-forecast.** Measure it against the forecast in force at the start of the quarter, or state which forecast was used.
6. **Verify:** recompute the three largest variances from the financial data and confirm the >10% bolding was applied to every variance over the threshold, including those that weaken the narrative.

## Usage Notes

- **Purpose:** Converts quarterly data into comprehensive performance review with trends and recommendations
- **Deck Type:** Quarterly Business Reviews / Performance Analysis
- **Key Features:**
  - Comprehensive cross-functional performance review
  - Trend analysis vs both plan and previous quarter
  - Multi-dimensional metrics (financial, customer, operational, sales)
  - Honest assessment balancing wins and challenges
  - Forward-looking strategic recommendations
  - Success metrics for next quarter
  - Suitable for executive teams and department heads
  - 10-12 slides standard, 20+ for comprehensive review
  - Connects performance to strategic initiatives
