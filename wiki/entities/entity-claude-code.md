---
title: "Claude Code"
type: entity
tags: [tool, anthropic, cli, ai-workflow]
created: 2026-04-09
updated: 2026-04-09
---

Claude Code is Anthropic's official CLI for agentic coding assistance. It can read codebases, run terminal commands, edit files, search the web, and orchestrate [[Sub-agents]]. It is extended via [[Skills vs MCP Servers|Skills]] and MCP servers, and supports [[Claude Code Hooks|hooks]] for running shell commands at specific points in the agent lifecycle.

The author uses Claude Code as a primary development environment and workflow automation platform, building custom agents and hooks for use cases like [[Diagram Generation as Agent|diagram generation]] and [[Project Planning Agents|planning support]]. The [[SuperClaude Framework]] is a notable open-source reference for how others have structured this kind of extension.

Performance can be layered: [[ultrathink]] signals maximum thinking budget; Plan Mode encourages deliberate planning before execution; "revving" primes the model's reasoning; [[Sub-agents]] parallelise independent work.

## Cost Optimization and Provider Integration

Claude Code supports integration with alternative LLM providers through [[LiteLLM]], a proxy that routes requests across multiple providers like [[Qwen Code]] and others. By configuring environment variables to point to a local LiteLLM server, developers can extend session limits and manage API costs by transparently switching between Claude and other models on a per-request basis.

See also: [[SuperClaude Framework]], [[Claude Code Hooks]], [[Sub-agents]], [[ultrathink]], [[Skills vs MCP Servers]], [[LiteLLM]], [[Qwen Code]]

---
*My notes - do not edit below this line*
