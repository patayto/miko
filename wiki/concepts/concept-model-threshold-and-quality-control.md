---
title: "Model Threshold and Quality Control"
type: concept
tags: [ml, targeting, metrics, quality]
created: 2026-04-09
updated: 2026-04-09
---

Strategy for filtering model predictions based on confidence scores to balance audience size, prediction quality, and business metrics.

## The Core Trade-off

Every ML model outputs predictions with associated confidence scores. Publishing all predictions (low threshold) maximizes audience size but increases false positives. Publishing only high-confidence predictions (high threshold) improves accuracy but shrinks the addressable audience.

## Percentile-Based Filtering

Rather than use raw model confidence scores (which vary wildly across time and regions), use **percentile rankings** within each hourly batch:

- Rank all predictions output by a model in a given hour by confidence
- Assign percentiles (0–100) to each prediction relative to others in that batch
- Set a threshold (e.g., male predictions ≥70th percentile, female ≥50th percentile)
- Only publish predictions above the threshold

This approach automatically adapts to regional variation and seasonal fluctuations in model performance without manual recalibration.

## Quality Metrics

- **On-Target Rate (OTR):** Ratio of bids that actually target the intended demographic (measured by Nielsen via survey data). Higher thresholds → higher OTR.
- **Audience size:** Total number of customer-attribute mappings. Higher thresholds → smaller audiences.
- **BDR (Bid Data Rate):** Percentage of production bids matching the segment. Used for parity checks against third-party baselines.

## Optimization Process

For new models or regions without historical targets:

1. Run shadow publishing at multiple threshold levels (e.g., 70, 50, 30, 10th percentile)
2. Observe OTR and audience size at each level
3. Select threshold that achieves target size while maintaining acceptable OTR
4. For mature regions, dial in thresholds to match existing 3P audience sizes

## Example

Marketplace India Female launched at 10th percentile threshold because the 3P training dataset was small. As PD model improved and 3P was supplemented with new signals, threshold could be raised toward the standard 70th–80th percentile.

---
*My notes - do not edit below this line*
