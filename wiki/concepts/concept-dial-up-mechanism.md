---
title: "Dial-Up Mechanism"
type: concept
tags: [ml, targeting, rollout, testing, machine-learning]
created: 2026-04-09
updated: 2026-04-09
---

A controlled rollout strategy for gradually transitioning production audiences from one data source to another (e.g., third-party to first-party predictions) while monitoring key metrics at each stage.

## How it Works

The mechanism uses **consistent hashing** to deterministically assign customers across multiple allocation datasets without reversion. A job generates multiple output datasets corresponding to different control:test ratios (e.g., 0:100, 25:75, 50:50, 75:25, 100:0), where customers are assigned to buckets based on a consistent hash of their ID modulo a set of buckets (typically 100).

**Example output:**
- 100% control (3P): all customers from third-party allocations
- 75:25 mix: 75% from 3P, 25% from 1P (new predictive model)
- 50:50 mix: equal split
- 25:75 mix: 25% from 3P, 75% from 1P
- 100% test (1P): all customers from first-party predictive allocations

## Production Deployment

Each ratio is published as a separate production segment with a distinct attribute name (e.g., `PD_Q1T3_MALE_1P_50`). As metrics stabilize (typically 3 days due to caching layers), the targeting string of the main production segment is updated to point to the next ratio. This continues for 2–4 update cycles over ~2 weeks, with monitoring and pauses for weekends.

## Advantages

- **Smooth metric changes:** BDR and recognition rate increase gradually, reducing advertiser shock
- **Rollback capability:** If metrics degrade, revert to the previous ratio
- **Data collection:** Each stage yields production metrics (shadow publishing mode) to validate expected outcomes
- **Consistent user experience:** Customers stay assigned to the same allocation through deterministic hashing
- **Low overhead:** All variants publish at once; only segment targeting strings change

## Real-world Example

When launching PD nationwide, the mechanism reduced BDR jumps from a projected ~60% spike (from failed first launch) to measured increases of ~2% per update cycle. This gave advertisers time to adjust strategies and leadership confidence in the product's stability.

---
*My notes - do not edit below this line*
