---
title: "Logseq Journal 2025-08-29"
type: source
tags: [claude-code, ai-workflow, agents, hooks, planning]
created: 2026-04-09
updated: 2026-04-09
---

A full-day session moving from LLM prompts and MCP servers (the previous day) into [[Claude Code]], agents, and workflow design. The second thread, brief and unexplained, is a note about merging iCloud accounts.

The author explored [[Claude Code]] as a coding assistant with its own extension ecosystem. Key resources catalogued: official Anthropic docs, a builder.io walkthrough, the `awesome-claude-code` GitHub collection, and template libraries including aitmpl.com. The [[SuperClaude Framework]] was noted as an impressive reference implementation that closely parallels the author's own prior attempts to build something similar — same instincts, further developed.

Two concrete AI workflow ideas emerged. First: a [[Diagram Generation as Agent|diagram-generation agent]] that keeps codebase documentation current — invoked as slash commands (`/class-diagram`, `/architecture-diagram`), wired to an MCP server or custom agent, so diagrams can be created or updated on demand and validated for accuracy. Second: a [[Project Planning Agents|project planning agent]] trained on planning textbooks, capable of multi-level output — from a full software PRD down to a chore checklist — choosing the right level of detail based on the query, ideally without being told.

[[Sub-agents]] became a major focus. The [[Claudelog]] source makes the parallel-processing analogy explicit: designing sub-agent delegation is like writing multi-threaded code. The author noted an idea to "humanise" agents — giving them distinct personalities or energies rather than purely functional definitions — and to build a personal library of specialised agents over time.

[[Claude Code Hooks]] enable shell commands to fire on four triggers: PreToolUse, PostToolUse, UserPromptSubmit, and Stop. The smart-dispatcher pattern lets hooks route intelligently rather than firing on every event. A key caveat: over-triggering slows the agent without costing tokens.

For [[ultrathink|thinking and planning]], the `ultrathink` keyword signals maximum thinking budget. Combined with Plan Mode, "revving" (priming the model's reasoning before a task), and split-role [[Sub-agents]], this forms a layered approach to high-quality outputs on complex problems.

See also: [[Skills vs MCP Servers]], [[Claude Code]]

---
*My notes - do not edit below this line*
