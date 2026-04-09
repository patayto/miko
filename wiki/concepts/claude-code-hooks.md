---
title: "Claude Code Hooks"
type: concept
tags: [claude-code, automation, hooks, lifecycle]
created: 2026-04-09
updated: 2026-04-09
---

Hooks are shell commands configured in [[Claude Code]] settings that fire automatically in response to agent lifecycle events. Four trigger points are available:

- **PreToolUse** — before a tool executes
- **PostToolUse** — after a tool completes
- **UserPromptSubmit** — when the user submits a prompt
- **Stop** — when the agent finishes responding

Hooks run outside the token budget, so over-triggering them slows the agent without incurring direct cost. The **smart-dispatcher pattern** addresses this: a single entry-point hook inspects the event context and routes selectively, rather than every hook firing on every event indiscriminately.

A practical starting point: ask [[Claude Code]] to review your existing systems and suggest where hooks would be useful. The agent can identify patterns in your workflow that would benefit from automation.

See also: [[Sub-agents]], [[Claude Code]]

---
*My notes - do not edit below this line*
