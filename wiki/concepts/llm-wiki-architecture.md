---
title: "LLM-wiki Architecture"
type: concept
tags: [architecture, knowledge-management, llm, systems-design]
created: 2026-04-09
updated: 2026-04-09
---

An LLM-enabled knowledge management system architecture inspired by [[Andrej Karpathy]]'s approach, designed to integrate personal knowledge capture (Logseq, Obsidian) with structured wiki generation.

The core structure uses four layers:

1. **raw/** — read-only input sources (Logseq graphs, Obsidian vaults, external articles, PDFs)
2. **wiki/** — LLM-generated structured output organized by type (concepts, entities, sources, queries)
3. **Operational guides** — CLAUDE.md (agent instructions), index.md (catalog), log.md (append-only timeline)
4. **Operations** — discrete workflows (ingest, query, lint, audit) that process and maintain the system

Key design principles include [[Log Partitioning]] to manage context size, [[Nested Index Structure]] for hierarchical organization, and [[Domain-Specific Parsing Agents]] to handle diverse source formats. The architecture supports [[Context-Aware Knowledge Organization]], allowing topics to be treated with different rigor in different contexts (e.g., Personal vs Research).

A critical insight from Karpathy: log entries with consistent prefixes become parseable with simple unix tools, preserving an evolving timeline of what the system has done. This enables future agents to understand recent activity without full context.

The author contemplates scaling decisions: should logs and indices be partitioned by date or topic? Should they use traditional databases (SQL) or caching layers (Redis)? Should operations be handled by a single monolithic agent or specialized agents per operation?

---
*My notes - do not edit below this line*
