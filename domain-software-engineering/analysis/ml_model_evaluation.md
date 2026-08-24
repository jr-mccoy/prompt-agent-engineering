---
title: "ML Model Evaluation"
category: analysis
description: "Comprehensive evaluation frameworks and metrics for machine learning models"
tags:
  - machine-learning
  - model-evaluation
  - testing
  - metrics
updated: "2026-01-29"
---

# ML Model Evaluation

**Objective:** Design and execute comprehensive evaluation strategies for machine learning models, covering appropriate metrics selection, evaluation protocols, bias detection, and production readiness assessment to ensure models perform reliably in real-world conditions.

**When to Use:** Use this prompt when validating models before production deployment, comparing model alternatives, investigating model degradation, establishing evaluation baselines, or implementing continuous model monitoring.

**Instructions:**

1. **Define Evaluation Context**

   Clarify the evaluation scope:
   - Model type: Classification, regression, ranking, generative, etc.
   - Business objective and how model success translates to business success
   - Deployment environment constraints (latency, memory, compute)
   - Regulatory or compliance requirements
   - Stakeholder expectations and reporting needs

2. **Select Appropriate Metrics**

   **Classification Metrics:**

   | Metric | Use When | Formula |
   |--------|----------|---------|
   | Accuracy | Balanced classes | (TP + TN) / Total |
   | Precision | False positives costly | TP / (TP + FP) |
   | Recall | False negatives costly | TP / (TP + FN) |
   | F1 Score | Balance precision/recall | 2 * (P * R) / (P + R) |
   | F-beta | Weight P vs R | ((1 + beta^2) * P * R) / (beta^2 * P + R) |
   | ROC-AUC | Overall discrimination | Area under ROC curve |
   | PR-AUC | Imbalanced classes | Area under precision-recall |
   | Log Loss | Probability calibration | -mean(y * log(p) + (1-y) * log(1-p)) |
   | Cohen's Kappa | Inter-rater reliability | (Accuracy - Expected) / (1 - Expected) |

   **Regression Metrics:**

   | Metric | Use When | Notes |
   |--------|----------|-------|
   | MSE/RMSE | Large errors costly | Sensitive to outliers |
   | MAE | Robust to outliers | Easier to interpret |
   | MAPE | Need percentage error | Fails when y = 0 |
   | R-squared | Explain variance | Can be negative |
   | Adjusted R^2 | Compare model complexity | Penalizes features |

   **Ranking Metrics:**

   | Metric | Use When |
   |--------|----------|
   | NDCG@k | Relevance grading matters |
   | MAP | Binary relevance |
   | MRR | First result matters most |
   | Hit Rate@k | Any hit in top-k counts |

   **Generative/LLM Metrics:**

   | Metric | Measures |
   |--------|----------|
   | BLEU | N-gram precision |
   | ROUGE | Recall of n-grams |
   | BERTScore | Semantic similarity |
   | Perplexity | Language model quality |
   | Human Evaluation | Qualitative assessment |

3. **Design Evaluation Protocol**

   **Data Splits:**
   - Train/validation/test split ratios (typical: 70/15/15 or 80/10/10)
   - Temporal splits for time-series data (never leak future data)
   - Stratified splits for imbalanced classes
   - Group splits to prevent data leakage (e.g., same user in train/test)

   **Cross-Validation:**
   ```
   Technique          | Use Case
   -------------------|----------------------------------
   K-Fold             | Standard, adequate data
   Stratified K-Fold  | Imbalanced classification
   Time Series CV     | Temporal data
   Group K-Fold       | Grouped/clustered data
   Leave-One-Out      | Very small datasets
   Nested CV          | Hyperparameter tuning + evaluation
   ```

   **Holdout Sets:**
   - Golden test set (never touch during development)
   - Challenge sets (known difficult cases)
   - Out-of-distribution test sets
   - Adversarial examples

4. **Assess Model Calibration**

   Evaluate probability reliability:
   - Reliability diagrams (calibration curves)
   - Expected Calibration Error (ECE)
   - Maximum Calibration Error (MCE)
   - Brier Score

   Calibration methods if needed:
   - Platt scaling
   - Isotonic regression
   - Temperature scaling

5. **Evaluate Robustness**

   Test model stability:
   - Sensitivity to input perturbations
   - Performance on edge cases
   - Behavior with missing/corrupted data
   - Adversarial attack resistance
   - Performance variance across random seeds

6. **Detect and Measure Bias**

   **Fairness Metrics:**

   | Metric | Definition |
   |--------|------------|
   | Demographic Parity | P(Y=1\|A=0) = P(Y=1\|A=1) |
   | Equalized Odds | Equal TPR and FPR across groups |
   | Equal Opportunity | Equal TPR across groups |
   | Calibration | Equal precision across groups |
   | Individual Fairness | Similar inputs → similar outputs |

   **Bias Analysis:**
   - Slice analysis by protected attributes
   - Intersectional analysis (combinations of attributes)
   - Proxy discrimination detection
   - Historical bias in training data

7. **Benchmark Against Baselines**

   Always compare against:
   - Random baseline
   - Majority class baseline
   - Simple heuristic baseline
   - Previous production model
   - State-of-the-art for the task

   Statistical significance testing:
   - McNemar's test (paired classification)
   - Paired t-test (paired continuous)
   - Bootstrap confidence intervals
   - Multiple comparison correction (Bonferroni)

8. **Assess Production Readiness**

   **Operational Metrics:**
   - Inference latency (p50, p95, p99)
   - Throughput (requests/second)
   - Memory footprint
   - Model size (storage, download)
   - Cold start time
   - Hardware requirements (GPU, CPU)

   **Deployment Considerations:**
   - Model versioning strategy
   - Rollback capabilities
   - A/B testing infrastructure
   - Shadow mode testing
   - Monitoring and alerting
   - Data drift detection

9. **Document Evaluation Results**

   Create model card including:
   - Model description and intended use
   - Training data summary
   - Evaluation data summary
   - Performance metrics with confidence intervals
   - Limitations and failure modes
   - Ethical considerations
   - Bias evaluation results

**Expected Output:** A comprehensive model evaluation report including:
- Metric selection rationale
- Performance summary with confidence intervals
- Comparison against baselines
- Calibration analysis
- Fairness/bias assessment
- Robustness evaluation
- Production readiness assessment
- Recommended actions

**Example Output:**

```markdown
## Model Evaluation Report: Customer Churn Prediction v2.1

### Evaluation Summary

| Aspect | Status | Notes |
|--------|--------|-------|
| Performance | Pass | Exceeds baseline by 12% |
| Calibration | Warning | Over-confident at high probabilities |
| Fairness | Pass | Demographic parity within 5% |
| Robustness | Pass | Stable across 5 seeds |
| Latency | Pass | p99 = 45ms < 100ms target |

### Performance Metrics

**Test Set Results (n=50,000, holdout from 2024-Q4):**

| Metric | Value | 95% CI | Baseline | Delta |
|--------|-------|--------|----------|-------|
| ROC-AUC | 0.847 | [0.839, 0.855] | 0.756 | +12.0% |
| PR-AUC | 0.623 | [0.608, 0.638] | 0.487 | +27.9% |
| F1 @ 0.5 | 0.712 | [0.698, 0.726] | 0.634 | +12.3% |
| Precision @ 0.5 | 0.684 | [0.668, 0.700] | 0.598 | +14.4% |
| Recall @ 0.5 | 0.743 | [0.727, 0.759] | 0.677 | +9.7% |

**Confidence intervals computed via bootstrap (n=1000).**

### Calibration Analysis

Expected Calibration Error (ECE): 0.042

The model is generally well-calibrated but shows over-confidence
in the 0.8-1.0 probability range. Recommend temperature scaling
with T=1.15 before deployment.

### Fairness Evaluation

**Demographic Parity Gap:**

| Segment | Positive Rate | Gap from Overall |
|---------|---------------|------------------|
| Age 18-30 | 0.231 | +0.012 |
| Age 31-50 | 0.224 | +0.005 |
| Age 51+ | 0.209 | -0.010 |
| Overall | 0.219 | - |

All segments within 5% tolerance. No significant disparate impact detected.

### Robustness Testing

| Test | Result |
|------|--------|
| 5 random seeds | AUC std = 0.003 |
| 10% missing features | AUC = 0.831 (-1.9%) |
| Feature perturbation (5%) | AUC = 0.839 (-0.9%) |
| Temporal stability (last 3 months) | AUC range: 0.841-0.853 |

### Production Metrics

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Latency p50 | 12ms | <50ms | Pass |
| Latency p99 | 45ms | <100ms | Pass |
| Model size | 47MB | <100MB | Pass |
| Memory (inference) | 180MB | <500MB | Pass |

### Recommendations

1. **Deploy with temperature scaling (T=1.15)** to improve calibration
2. **Set up drift monitoring** on top 5 features by importance
3. **Schedule re-evaluation** in 3 months for temporal stability
4. **Consider A/B test** against rule-based system for 2 weeks
```

**False-Positive Prevention:**

- Do NOT rely solely on accuracy for imbalanced datasets - always check class-specific metrics
- Do NOT skip baseline comparisons - improvements must be measured against something
- Do NOT use test data for any decision-making during development (prevents data leakage)
- Do NOT assume metrics transfer across domains - validate on representative data
- Do NOT ignore confidence intervals - point estimates can be misleading
- Do NOT deploy without calibration check if probabilities are used downstream
- Do NOT skip fairness analysis for models affecting people
- Consider business metrics, not just ML metrics - a better model might not improve business outcomes

**Quality Indicators:**

- Metrics aligned with business objectives
- Statistical significance established for all comparisons
- Confidence intervals provided for key metrics
- Fairness evaluated across relevant demographic groups
- Calibration assessed if probabilities are used
- Baseline comparisons included
- Temporal stability verified for production models
- Operational requirements validated
