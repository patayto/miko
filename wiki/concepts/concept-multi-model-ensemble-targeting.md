---
title: "Multi-Model Ensemble Targeting"
type: concept
tags: [ml, targeting, ensemble-learning]
created: 2026-04-09
updated: 2026-04-09
---

Architecture that combines predictions from multiple independent demographic models (retail, music, Twitch, video) to expand targeting reach while managing conflicts.

## The Setup

As Predictive Demographics scaled, new signals beyond retail purchase history became available:

- **Retail model:** Trained on product viewing and purchase history
- **Music model:** Derived from music consumption patterns
- **Twitch/Video models:** Trained on streaming behavior

Each model produces independent customer-to-demographic predictions with confidence scores.

## Conflict Resolution via Waterfall

When multiple models disagree on a customer's demographic (e.g., retail predicts Male, music predicts Female):

1. **Take the union:** Publish allocations from all models
2. **Apply waterfall:** Resolve conflicts by choosing allocations in priority order: Retail > Music > Twitch > Video
3. **Ranking basis:** Priorities determined by model AUROC scores (primary) and shadow mode experiments (secondary validation)

Example: If retail model says Male (0.8 confidence) but music says Female (0.7), use Male per the retail priority.

## Benefits

- **Expanded reach:** Union of models covers more customers than any single model
- **Principled prioritization:** Ranking by performance metrics ensures quality
- **Incremental expansion:** New models integrate without disrupting existing allocations
- **Measurable impact:** Shadow publish each model's contribution before committing to ensemble

## Scaling Considerations

- **Performance tracking:** Monitor each model's contribution to overall BDR and OTR
- **Inter-model competition:** Newer models (music, video) may cannibalize reach from mature models; analyze overlap
- **Feature engineering:** Keep models independent but aligned on feature definitions
- **Threshold coordination:** Ensure all models use comparable quality filtering (percentile-based thresholds)

## Related Concept

Multi-allocation resolution for customers predicted by the same model on different days uses different strategies (majority voting, relative voting), whereas cross-model conflicts use the strict waterfall approach.

---
*My notes - do not edit below this line*
