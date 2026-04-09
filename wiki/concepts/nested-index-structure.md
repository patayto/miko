---
title: "Nested Index Structure"
type: concept
tags: [architecture, indexing, knowledge-management]
created: 2026-04-09
updated: 2026-04-09
---

A hierarchical approach to organizing and indexing knowledge in an [[LLM-wiki Architecture]], inspired by Python's `__init__.py` pattern. Rather than maintaining a single flat index, topics are organized as directories containing:

- A specialized `index.md` at the topic level
- Any number of pages (`page.md`) within the topic
- Nested subdirectories with their own indices (sub-topics)

This structure enables:

- **Scoped indexing** — agents can load a topic-level index without understanding the entire wiki
- **Clear boundaries** — related pages live together, making connections explicit
- **Scalability** — adding new topics doesn't bloat the root index
- **Lazy evaluation** — the system can drill into topics only when necessary

The base `index.md` references either `page`s or `topic`s (directories with their own `index.md`), creating a tree structure. Like unix filesystems, this allows arbitrary nesting depth while keeping individual files manageable.

The author contemplates whether index optimization techniques (e.g., tagging strategies, caching, SQL backing) could further enhance discoverability within this structure.

---
*My notes - do not edit below this line*
