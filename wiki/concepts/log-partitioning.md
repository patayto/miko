---
title: "Log Partitioning"
type: concept
tags: [architecture, optimization, knowledge-management]
created: 2026-04-09
updated: 2026-04-09
---

A scalability optimization for [[LLM-wiki Architecture]] where the append-only activity log is split into smaller pieces rather than kept as a single monolithic file.

In a growing knowledge base, the log can become arbitrarily large, forcing the agent to load and parse increasingly more context just to understand recent activity. Partitioning strategies include:

- **By date** — each day or week gets its own log file (e.g., `log-2026-04.md`, `log-2026-w15.md`), reducing load time for recent entries
- **By topic** — separate logs for specific domains (e.g., `log-technical.md`, `log-personal.md`)
- **Hybrid** — date-based partitions with a high-level index pointing to relevant entries

The tradeoff: partitioning reduces context per query but requires sophisticated indexing to maintain a coherent timeline of the system's evolution. The author questions whether traditional databases (SQL) or caching layers (Redis) are more appropriate than flat file partitioning for production deployments.

---
*My notes - do not edit below this line*
