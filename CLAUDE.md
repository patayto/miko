# The System (Miko)

You are the agent responsible for this knowledge base. Read this file fully before taking any action.

## What you are

You maintain a persistent, compounding wiki built from two sources:
- Raw capture: notes written by the human in Logseq and Obsidian (in `raw/`)
- External sources: articles, PDFs, and other files dropped into `raw/`

You do not write into `raw/`. You write only into `wiki/`. The index and log are stored in `miko.db` (SQLite) — not in markdown files.

## Directory layout

```
miko/

├── CLAUDE.md         <- this file
└── ops/              <- operation instructions
│   ├── ingest.md
│   ├── consolidate.md
│   ├── lint.md
│   └── query.md
├── miko.db               <- SQLite database (index + log)
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

`index.md` and `log.md` at the repo root are legacy human-readable views. Do not write to them. The database is authoritative.

## Database

**Path:** `/Users/filipe/obsidian/miko/miko.db`

**Tables:**

```sql
-- Raw source file registry and ingest queue
CREATE TABLE sources (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    path        TEXT NOT NULL UNIQUE, -- relative to raw/, e.g. "obsidian-notes/2025-12-01.md"
    filename    TEXT NOT NULL,        -- basename, e.g. "2025-12-01.md"
    filetype    TEXT,                 -- md | pdf | txt | html | py
    discovered  TEXT NOT NULL,        -- YYYY-MM-DD
    status          TEXT NOT NULL DEFAULT 'pending', -- pending | ingested | ignored
    ingested        TEXT,                 -- YYYY-MM-DD when completed
    notes           TEXT,
    content_length  INTEGER,              -- file size in bytes
    content_size    REAL                  -- file size in MB
);

-- Wiki page registry
CREATE TABLE index_pages (
    title           TEXT PRIMARY KEY,
    type            TEXT NOT NULL,    -- concept | entity | source | query
    summary         TEXT,
    updated         TEXT,             -- YYYY-MM-DD
    ignored         INTEGER DEFAULT 0,
    ignored_reason  TEXT,
    ignored_scanned TEXT,             -- YYYY-MM-DD
    source_id       INTEGER REFERENCES sources(id)  -- required for new pages; legacy entries may be NULL (see ops/todo.md: source backfill)
);

-- Append-only activity log
CREATE TABLE log (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp   TEXT NOT NULL,        -- YYYY-MM-DD HH:MM
    operation   TEXT NOT NULL,        -- index | ingest | consolidate | lint | query | update | create | ops
    subject     TEXT,
    status      TEXT NOT NULL,        -- complete | failed | partial
    summary     TEXT,
    details     TEXT,                 -- JSON array of bullet strings
    source_id   INTEGER REFERENCES sources(id)  -- nullable; source file this operation relates to
);
```

**`sources` is the authoritative queue for ingest.** Always check it before ingesting a file. The `log` table is append-only and must never have rows deleted.

**CLI syntax:**
```bash
sqlite3 /Users/filipe/obsidian/miko/miko.db "SQL QUERY HERE"
```

Use single quotes for SQL strings inside double-quoted bash arguments, or use `.mode` / heredoc form for multi-line inserts.

## Common queries

### Check if a page exists
```bash
sqlite3 /Users/filipe/obsidian/miko/miko.db \
  "SELECT title, type, summary FROM index_pages WHERE title = 'Page Title';"
```

### List all pages by type
```bash
sqlite3 /Users/filipe/obsidian/miko/miko.db \
  "SELECT title, summary FROM index_pages WHERE type = 'concept' AND ignored = 0 ORDER BY updated DESC;"
```

### Full-text search across titles and summaries
```bash
sqlite3 /Users/filipe/obsidian/miko/miko.db \
  "SELECT title, type, summary FROM index_pages WHERE title LIKE '%keyword%' OR summary LIKE '%keyword%';"
```

### Register a new page (or update summary/date on existing)
Always include `source_id` for new pages. Look up the id from the `sources` table first:
```bash
sqlite3 /Users/filipe/obsidian/miko/miko.db \
  "SELECT id FROM sources WHERE filename = 'filename.md';"
sqlite3 /Users/filipe/obsidian/miko/miko.db \
  "INSERT OR REPLACE INTO index_pages (title, type, summary, updated, source_id) VALUES ('Page Title', 'concept', 'One-line summary.', '2026-05-11', 42);"
```

### Mark a source as ignored
```bash
sqlite3 /Users/filipe/obsidian/miko/miko.db \
  "INSERT OR REPLACE INTO index_pages (title, type, ignored, ignored_reason, ignored_scanned) VALUES ('filename.md', 'source', 1, 'Empty stub', '2026-04-09');"
```

### Append a log entry
```bash
sqlite3 /Users/filipe/obsidian/miko/miko.db \
  "INSERT INTO log (timestamp, operation, subject, status, summary, details)
   VALUES ('2026-04-09 14:32', 'ingest', 'source-file.md', 'complete', 'One sentence summary.',
           '[\"Source page: [[Title]]\", \"Concepts created: [[X]]\"]');"
```

### View recent log entries
```bash
sqlite3 /Users/filipe/obsidian/miko/miko.db \
  "SELECT timestamp, operation, subject, status, summary FROM log ORDER BY timestamp DESC LIMIT 10;"
```

### Check what was last ingested (avoid re-ingesting)
```bash
sqlite3 /Users/filipe/obsidian/miko/miko.db \
  "SELECT subject, timestamp FROM log WHERE operation = 'ingest' ORDER BY timestamp DESC LIMIT 20;"
```

### Find stale pages (not updated in 90+ days)
```bash
sqlite3 /Users/filipe/obsidian/miko/miko.db \
  "SELECT title, updated FROM index_pages WHERE ignored = 0 AND updated < date('now', '-90 days') ORDER BY updated;"
```

## Hard rules

1. Never write to `raw/` or any symlinked directory inside it. Read only.
2. Never delete wiki pages. Update them instead.
3. The database is the authoritative record for the index and log. Do not write to `index.md` or `log.md`.
4. Always update `index_pages` after creating or updating any wiki page.
5. Always insert into `log` after completing an operation.
6. Before creating a new wiki page, check `index_pages` for an existing page on the same topic. Update rather than duplicate.
7. Use [[wikilinks]] aggressively throughout wiki page bodies.
8. Never delete rows from `log` or `sources`. Both tables are append-only. If you made an error, add a corrective log entry — do not remove the original.
9. Before ingesting any file, check `sources` for its status. If status is `ingested` or `ignored`, stop and report. Do not re-ingest.

## Operations

When asked to run an operation, load the relevant file from `ops/` and follow its instructions exactly.

| Command      | File to load          |
|--------------|-----------------------|
| index        | ps/index.md       |
| ingest       | ops/ingest.md      |
| consolidate  | ops/consolidate.md |
| lint         | ops/lint.md        |
| query        | ops/query.md       |

## Wiki page format

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

## Sources
- [[Source Page Title]]

---
*My notes - do not edit below this line*
```

The `## Sources` section lists the wiki source page(s) this page was built from. Always include it on concept and entity pages. Source pages themselves do not need this section. The section below the horizontal rule and italicised note is reserved for the human. Never modify it.
