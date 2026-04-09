---
title: "Marketplace-Level Models"
type: concept
tags: [ml, targeting, architecture, data-pipeline]
created: 2026-04-09
updated: 2026-04-09
---

ML approach that trains and deploys separate demographic prediction models for each Amazon marketplace (e.g., US, JP, India) rather than regional groupings, improving accuracy and enabling localization.

## Motivation

Initial Predictive Demographics used **regional models** (grouping multiple countries under a shared model, e.g., FE for "Far East" covering JP and AU). However:

- Marketplaces have distinct product catalogues and browse node taxonomies
- Customer bases differ significantly (purchasing patterns, demographics, language)
- 3P demographic training data is provided at marketplace level
- Training data distribution analysis showed marketplace models outperform regional ones at test time

## Architecture Changes

Scaling from regional to marketplace required:

1. **Data splitting:** Decompose all datasets (customer histories, 3P labels, ASIN metadata) from region-level to marketplace-level buckets
2. **Model training:** Train one model per marketplace with that marketplace's training data
3. **Inference scaling:** Run inference pipelines for 17+ independent models daily
4. **Feature consistency:** Maintain shared feature encoding across models so marketplace models remain compatible

## Enabling New Locales

Marketplace-level models unlocked expansion to data-scarce regions:

- **With training data:** Ingest new 3P signals and train marketplace-specific models (e.g., Canada, Brazil)
- **Without training data:** Use **cross-marketplace scoring** (train model in marketplace X, apply predictions to marketplace Y). Requires finding source-target pairs with similar browse node coverage (determined by data scientists analyzing catalogue overlap)

## Challenges

- **Operational complexity:** Managing and monitoring 17+ model pipelines simultaneously
- **Dependency tracking:** Ensure feature changes propagate correctly across models
- **Experiment coordination:** Support parallel experiments (Vlad trying new architectures) while carrying out infrastructure migrations
- **Convergence:** Global models later showed promise as browse node embeddings became richer and more widely shared across teams

---
*My notes - do not edit below this line*
