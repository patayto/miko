---
title: "Claude Projects"
type: concept
tags: [claude, projects, caching, rag, context-management]
created: 2026-04-09
updated: 2026-04-09
---

A feature of Claude (web and desktop) that provides automatic content caching and [[Retrieval-Augmented Generation]] (RAG) for managing large knowledge bases. Projects allow users to upload core working documents once, and Claude automatically caches this content so it doesn't count against usage limits on repeated access.

As projects accumulate more files and information, Claude switches to a faster, RAG-powered mode that maintains response quality while keeping latency low. This mechanism substantially increases the effective context window without proportional token cost, making Projects an essential tool for [[Usage Limits|managing usage limits]].

Best practices for Projects include uploading all core reference documents at session start and using the same project across related tasks to maximize caching benefits. Projects are particularly valuable for [[Claude Code]] workflows where the same codebase, documentation, and architectural context are repeatedly referenced.

See also: [[Retrieval-Augmented Generation]] (RAG mechanism behind Projects)

---
*My notes - do not edit below this line*
