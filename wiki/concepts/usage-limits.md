---
title: "Usage Limits"
type: concept
tags: [claude, usage, tokens, throttling, rate-limiting, optimization]
created: 2026-04-09
updated: 2026-04-09
---

Rate limits on Claude API and Claude web/desktop products that reset every 5 hours. Usage is determined by message count rather than raw tokens, and affected by message length, file attachment size, conversation history length, tool usage (e.g., web research), model choice, and artifact creation.

Different subscription tiers offer different allocations: Pro provides baseline limits (~45 messages per 5 hours for short conversations with cheaper models); Max provides 5x allocation; and Team plans offer customizable higher limits. A typical "short conversation" is approximately 200 English sentences at 15-20 words each.

Optimization strategies include [[LLM Caching|caching]] via [[Claude Projects]], model selection (Haiku for cost, Sonnet for balance, Opus for quality), conversation compaction via `/compact` when hitting context window limits, and focusing work into focused 5-hour sprints. [[Claude Projects]] provide automatic caching that removes uploaded content from the usage calculation, making them the primary tool for managing large knowledge bases.

See also: [[Claude Code]] (primary consumer of limits), [[Retrieval-Augmented Generation]] (mechanism for efficient context handling)

---
*My notes - do not edit below this line*
