---
title: "LogSeq"
type: entity
tags: [tool, note-taking, knowledge-management, outliner]
created: 2026-04-09
updated: 2026-04-09
---

LogSeq is an open-source, local-first outliner and knowledge management tool built around a daily journal and bidirectional linking. Notes are stored as plain Markdown or EDN files, giving the user full ownership of their data.

The primary interface is a block-based outliner where every bullet is an independently addressable and linkable unit. The daily journal page is the default entry point, encouraging a capture-first approach compatible with [[Interstitial Journaling]].

Key features include:

- **[[LogSeq Slash Commands]]** — a `/` trigger menu for inserting timestamps, dates, queries, and other structured content inline
- **Advanced commands** — triggered via `<`, providing block admonitions (`#+BEGIN_TIP`, `#+BEGIN_NOTE`, etc.) for multiline structured content
- **Embedded content** — supports rendered HTML (`@@html:@@`), embedded YouTube videos with timestamped playback, and code blocks with syntax highlighting
- **Bidirectional links** — `[[page links]]` and `((block references))` that surface content across the graph
- **Date links** — linking to a future date page causes blocks to appear on that page automatically, serving as a lightweight reminder system

LogSeq does not natively support kanban views. A community plugin (`logseq-kanban-plugin`) exists but has limited functionality. Template support for journals is possible via the plugin ecosystem.

Syncing options include storing the vault in a third-party cloud service, using the paid LogSeq Sync beta, or self-hosting a private cloud solution. The self-hosted option appeals for privacy reasons.

Integrations include [[Readwise]] for highlights sync.

---
*My notes - do not edit below this line*
