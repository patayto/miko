---
title: "ultrathink"
type: concept
tags: [claude-code, thinking, planning, performance]
created: 2026-04-09
updated: 2026-04-09
---

`ultrathink` is a keyword added to [[Claude Code]] prompts to signal maximum thinking budget — instructing the model to reason more deeply before responding.

It is part of a layered performance approach:

1. **ultrathink** — maximum thinking
2. **Plan Mode** — deliberate planning phase before execution
3. **Revving** — priming the model with context and warm-up reasoning before a complex task
4. **Split-role [[Sub-agents]]** — multiple agents each approaching the problem from a different angle

This stack is roughly: `ultrathink` + Sonnet + Plan Mode + revving is the ceiling before adding sub-agents. When that ceiling is still insufficient, split-role sub-agents extend it further.

See also: [[Claude Code]], [[Sub-agents]]

---
*My notes - do not edit below this line*
