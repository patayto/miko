---
title: "Shadow Publishing Pipeline"
type: concept
tags: [ml, testing, metrics, targeting, safety]
created: 2026-04-09
updated: 2026-04-09
---

A production-safe experimentation pattern that publishes allocations (e.g., predicted customer segments) to a separate namespace before committing to primary production, allowing real-world metric measurement without impacting live traffic.

## Core Idea

Instead of blindly launching a new model or algorithm variant, publish its outputs to "shadow" segments with special metadata markers (e.g., `PD_Q1T1_US_MALE` for "Predictive Demographics, Q1, Test 1"). These shadow segments are attached to eligible bids without running any actual ad lines—so no advertiser budget is spent, and the model's real-world performance can be measured against ground truth.

## What Gets Measured

- **Audience size:** How many customers match the shadow attribute after downstream filtering (Audience Ingestion and Evaluation removes ineligible customers: children, seniors, inactive accounts, bots, etc.)
- **BDR (Bid Data Rate):** The percentage of bid requests that target eligible customers—a proxy for audience quality and accuracy
- **Segment stability:** Whether metrics stabilize within expected timeframes (typically 3 days due to caching)

## Validation Process

Before moving to production:

1. **Compare baseline:** Publish shadow versions of existing 3P segments and confirm metrics match current production (confidence check)
2. **Test new model:** Publish shadow variants of new 1P predictions at different quality thresholds and review BDR/size trade-offs
3. **A/B framework:** Set up multiple shadow segments at different dial-up ratios (50:50, 25:75, etc.) and observe metric progression
4. **Sign-off:** Once shadow metrics align with expectations, update production segment targeting strings

## Benefits

- **De-risk launches:** Test in production without impact
- **Cheap experimentation:** No budget spend; metric data is free
- **Cross-team visibility:** Other teams can query Athena or SageMaker on the shadow datasets to validate hypotheses
- **Metric feedback loop:** Catches misalignment between expected and actual performance early

## Related Concepts

Works in conjunction with the [[Dial-Up Mechanism]] to smoothly blend old and new allocations while maintaining safety and measurement capability.

---
*My notes - do not edit below this line*
