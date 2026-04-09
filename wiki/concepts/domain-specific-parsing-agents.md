---
title: "Domain-Specific Parsing Agents"
type: concept
tags: [architecture, agents, knowledge-management]
created: 2026-04-09
updated: 2026-04-09
---

A multi-agent pattern for handling diverse source formats in an [[LLM-wiki Architecture]]. Rather than building a single monolithic parser, each source domain (technical articles, personal journals, research papers, etc.) has its own specialized parsing agent with domain-aware rules and templates.

The workflow:

1. A **sorting agent** examines new files dropped into `raw/`
2. If a domain-specific agent exists (e.g., `logseq-parsing-agent.md`, `research-paper-agent.md`), the file is routed there
3. If no agent exists, the sorting agent attempts to parse the file or creates a new domain and agent template

Benefits include:

- **Specialization** — agents can learn domain conventions (e.g., Logseq uses specific YAML frontmatter; research papers have abstracts and citations)
- **Token efficiency** — domain-specific parsing instructions are more focused than generic rules
- **Learning** — agents can propose new parsing templates when encountering unfamiliar source types
- **Scalability** — adding a new source type only requires adding a new agent, not modifying core ingest logic

This approach decouples format handling from core wiki operations, making the system more extensible and maintainable.

---
*My notes - do not edit below this line*
