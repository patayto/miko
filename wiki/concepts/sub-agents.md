---
title: "Sub-agents"
type: concept
tags: [claude-code, parallelism, agents, workflow]
created: 2026-04-09
updated: 2026-04-09
---

Sub-agents are spawned [[Claude Code]] instances that handle delegated work in parallel. Designing their use is directly analogous to writing multi-threaded code: the benefit depends entirely on how well the task is decomposed to avoid write conflicts and redundant work.

By default, [[Claude Code]] uses sub-agents conservatively — primarily for read operations like file reads, web fetches, and text searches. To unlock meaningful parallelism, explicit orchestration is required: the prompt must name which steps are independent and can be delegated. Vague instructions produce serial execution even when parallel is possible.

The intended long-term pattern is to accumulate a personal library of specialised sub-agents, each with a defined focus and role. The [[SuperClaude Framework]] models this with individual `*.md` agent definition files. There is also an idea to "humanise" these agents — giving them distinct personalities or energies rather than purely functional definitions — so that the library feels like a team rather than a set of tools.

For complex tasks, combining sub-agents with [[ultrathink]] + Plan Mode + "revving" produces split-role analysis: each sub-agent approaches the same problem from a different angle, and the combined output is richer than a single pass.

See also: [[Claude Code Hooks]], [[Claude Code]], [[SuperClaude Framework]], [[ultrathink]]

---
*My notes - do not edit below this line*
