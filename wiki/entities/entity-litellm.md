---
title: "LiteLLM"
type: entity
tags: [dev-tools, llm-routing, api-gateway]
created: 2026-04-09
updated: 2026-04-09
---

A unified interface library and local proxy service that standardizes API calls across multiple LLM providers including Claude, OpenAI, Qwen, and others. LiteLLM enables developers to abstract away provider-specific API differences and route requests dynamically based on cost, availability, or capability requirements.

LiteLLM can be deployed as a local server (typically on localhost:4000) and configured via `config.yaml` to define a list of available models and their associated provider keys. It supports fallback routing, allowing requests to fail over from one provider to another if needed.

Integration with [[Claude Code]] involves configuring environment variables (`ANTHROPIC_BASE_URL`, `ANTHROPIC_AUTH_TOKEN`) to point to the LiteLLM proxy rather than Anthropic's servers directly. This allows [[Claude Code]] to transparently use alternative providers like [[Qwen Code]] for certain requests, enabling cost optimization and session limit management.

Docker deployment is available for more complex setups, though minimal configuration can run LiteLLM with a simple setup script.

---
*My notes - do not edit below this line*
