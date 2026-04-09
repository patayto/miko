---
title: "Python Learnings for Kraken"
type: source
tags: [python, django, kraken, async, llm, caching]
created: 2026-04-09
updated: 2026-04-09
---

A working notes page capturing Python and [[Django]] discoveries made while at [[Kraken]]. Half concrete learnings, half open questions — the shape of someone actively mapping unfamiliar territory.

The notes begin with a runtime question: CPython (the standard Python interpreter, built on C) versus PyPy (an alternative runtime). PyPy is flagged as genuinely unclear — the author doesn't know whether it is better, worse, or just different, and for what workloads.

The bulk of the notes concern [[Django]]. A Django view is any Python callable that receives an HTTP request and returns an HTTP response — a deliberately minimal definition. Async views, defined with `async def` and served via ASGI, are the right choice when a view calls LLMs, external APIs, or multiple services in parallel. At [[Kraken]], async views are standard for [[pydantic-ai]] LLM agent calls, which are async-native.

An interesting design problem emerges around [[Fuzzy Cache|LLM caching]]: traditional caches like `@functools.lru_cache` require exact key matches. LLM inputs are freeform and vary subtly, making exact-match caching largely useless. The notes raise the concept of a [[Fuzzy Cache]] — a cache that matches on semantic similarity — as an open question for the GenAI world.

Open questions about the [[Kraken]] stack: documentation tooling (Sphinx?), web server (nginx, gunicorn?), hosting model (serverless, EC2?).

See also: [[Django]], [[pydantic-ai]], [[Kraken]], [[Fuzzy Cache]]

---
*My notes - do not edit below this line*
