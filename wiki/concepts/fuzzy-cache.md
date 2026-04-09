---
title: "Fuzzy Cache"
type: concept
tags: [caching, llm, semantic-similarity, performance]
created: 2026-04-09
updated: 2026-04-09
---

A fuzzy cache matches lookup keys on semantic similarity rather than exact equality. It is the natural extension of traditional caching for the LLM/GenAI world, where inputs are freeform text that varies in ways that shouldn't matter.

Traditional caches (e.g. `@functools.lru_cache`) require exact key matches. For LLM inputs — user queries, dynamic prompts, agent instructions — exact repetition is rare. Two prompts that differ by a single word may warrant identical responses, but will always miss a standard cache.

A fuzzy cache would embed keys as vectors and retrieve on cosine similarity or equivalent. The hard design question is threshold: too loose, and semantically different queries get stale or wrong responses; too tight, and the hit rate is negligible.

This is an open problem as of mid-2025. No production-standard solution is noted.

See also: [[pydantic-ai]], [[Django]], LLM Caching (not yet written)

---
*My notes - do not edit below this line*
