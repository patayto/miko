---
title: "Skills vs MCP Servers"
type: concept
tags: [claude-code, tooling, mcp, skills]
created: 2026-04-09
updated: 2026-04-09
---

Skills and MCP (Model Context Protocol) servers are two mechanisms for extending [[Claude Code]] with additional capabilities. The author migrated from MCP servers to Skills across both [[Claude Code]] and Claude Desktop in October 2025 after prior research into the tradeoffs.

MCP servers run as external processes that expose tools to Claude via a defined protocol. They require configuration, process management, and can introduce latency or reliability concerns tied to the server lifecycle.

Skills are a more integrated mechanism for packaging reusable capabilities. They are invoked inline within the Claude interface and do not require a separate server process. The author's decision to migrate suggests Skills were considered a cleaner or lower-overhead alternative for their workflow.

See also: MCP server architecture (not yet written), Claude Code Skills specification (not yet written)

---
*My notes - do not edit below this line*
