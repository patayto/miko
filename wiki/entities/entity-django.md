---
title: "Django"
type: entity
tags: [framework, python, web, async]
created: 2026-04-09
updated: 2026-04-09
---

Django is a Python web framework. At its core, a Django **view** is any Python callable — function or class — that receives an HTTP request and returns an HTTP response. This minimalism makes it composable.

Async views are defined with `async def` and served via ASGI rather than WSGI. They are the right choice when a view needs to call high-latency services — LLMs, external APIs, multiple parallel services — since they avoid blocking the event loop. [[Kraken]] uses async views as standard for [[pydantic-ai]] LLM agent calls.

See also: [[pydantic-ai]], [[Kraken]], [[Fuzzy Cache]]

---
*My notes - do not edit below this line*
