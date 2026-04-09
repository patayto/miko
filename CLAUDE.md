# The System

You are the agent responsible for this knowledge base. Read this file fully before taking any action.

## What you are

You maintain a persistent, compounding wiki built from two sources:
- Raw capture: notes written by the human in Logseq and Obsidian (in `raw/`)
- External sources: articles, PDFs, and other files dropped into `raw/`

You do not write into `raw/`. You write only into `wiki/`, `index.md`, and `log.md`.

## Directory layout

```
miko/
├── CLAUDE.md             <- this file
├── index.md              <- catalog of all wiki pages (you maintain)
├── log.md                <- append-only activity record (you maintain)
├── ops/                  <- operation instructions (load before running)
│   ├── ingest.md
│   ├── consolidate.md
│   ├── lint.md
│   └── query.md
├── raw/                  <- all inputs, read-only for you
│   ├── logseq-pages/
│   ├── logseq-journals/
│   └── obsidian-notes/
└── wiki/                 <- your output
    ├── concepts/
    ├── entities/
    ├── sources/
    └── queries/
```

## Hard rules

1. Never write to `raw/` or any symlinked directory inside it. Read only.
2. Never delete wiki pages. Update them instead.
3. Always append to `log.md`, never overwrite it.
4. Always update `index.md` after creating or updating any wiki page.
5. Before creating a new wiki page, check `index.md` for an existing page on the same topic. Update rather than duplicate.
6. Use [[wikilinks]] aggressively throughout wiki page bodies.

## Operations

When asked to run an operation, load the relevant file from `ops/` and follow its instructions exactly.

| Command      | File to load       |
|--------------|--------------------|
| ingest       | ops/ingest.md      |
| consolidate  | ops/consolidate.md |
| lint         | ops/lint.md        |
| query        | ops/query.md       |

## Output note format

Every wiki page uses this structure:

```
---
title: "Page Title"
type: concept | entity | source | query
tags: [tag1, tag2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

Body content with [[wikilinks]] throughout.

---
*My notes - do not edit below this line*
```

The section below the horizontal rule and italicised note is reserved for the human. Never modify it.

## Log entry format

Every operation appends to `log.md` using this exact format:

```
## [YYYY-MM-DD HH:MM] operation | subject
Status: complete | failed | partial
Summary: one sentence describing what happened.
Details:
- bullet list of specific actions taken
```

## Index entry format

`index.md` contains tables organised by page type. Each row follows this pattern:

```
| [[Page Title]] | one-line summary | YYYY-MM-DD |
```
