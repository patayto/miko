---
title: "pydantic-ai"
type: entity
tags: [python, llm, agents, async, pydantic]
created: 2026-04-09
updated: 2026-04-09
---

pydantic-ai is a Python library for building LLM agents on top of Pydantic's structured output validation. It is async-native, making it a natural fit for [[Django]] async views.

[[Kraken]] uses pydantic-ai as its LLM agent framework. The async-native design is specifically called out as a reason for its adoption — LLM calls are inherently high-latency, and async is the right model for them.

See also: [[Django]], [[Kraken]], [[Fuzzy Cache]]

---
*My notes - do not edit below this line*
