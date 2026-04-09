---
title: "Diagram Generation as Agent"
type: concept
tags: [claude-code, architecture, diagrams, workflow, validation]
created: 2026-04-09
updated: 2026-04-09
---

A planned [[Claude Code]] workflow where architecture and class diagrams are generated and updated via slash commands (e.g. `/class-diagram`, `/architecture-diagram`), backed by an MCP server or custom agent.

The motivation: when [[Claude Code]] generates a codebase, the developer needs a fast, trustworthy way to reason about the result. Diagrams serve as a validation surface — a check that the generated code matches intended architecture. Without this, the developer is trusting the AI's output without an independent way to verify structure.

Accuracy is the hard requirement. An agent that generates plausible-but-wrong diagrams is worse than no diagrams at all, because it creates false confidence. The design must therefore include a validation path — some mechanism for checking that the diagram faithfully represents the actual code, not just what the agent thinks the code looks like.

The tooling target is Excalidraw for rendering.

See also: [[Claude Code]], [[Sub-agents]]

---
*My notes - do not edit below this line*
