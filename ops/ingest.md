# Ingest

Processes a source file from `raw/` and integrates its knowledge into the wiki.

## When to use

Run when the human points you at a specific file in `raw/`, drops a new file into `raw/`, or asks you to process a Logseq journal entry or Obsidian note.

If no specific file is given, query the sources table for the next pending item:
```bash
sqlite3 /Users/filipe/obsidian/miko/miko.db \
  "SELECT id, path, filename, content_size FROM sources WHERE status = 'pending' ORDER BY discovered LIMIT 1;"
```

## Steps

### 0. Pre-flight: confirm this file has not already been ingested

**This step is mandatory. Do not skip it.**

Check the `sources` table first (authoritative if populated):
```bash
sqlite3 /Users/filipe/obsidian/miko/miko.db \
  "SELECT id, status, ingested, notes FROM sources WHERE filename = 'filename.md';"
```

If `status = 'ingested'` or `status = 'ignored'`: **stop**. Report to the human and do nothing further.

If the sources table is empty or has no record for this file, fall back to checking the log:
```bash
sqlite3 /Users/filipe/obsidian/miko/miko.db \
  "SELECT timestamp, status, summary FROM log
   WHERE subject = 'filename.md' AND operation = 'ingest'
   ORDER BY timestamp DESC LIMIT 3;"
```

If the log shows a completed ingest for this file: **stop**. Report to the human.

If no record is found in either table: proceed.

---

### 0.5. Select model and delegate to sub-agent

```bash
sqlite3 /Users/filipe/obsidian/miko/miko.db \
  "SELECT content_size FROM sources WHERE filename = 'filename.md';"
```

Select model:
- `content_size < 0.5` (or NULL): **`haiku`**
- `content_size >= 0.5`: **`sonnet`**

**You cannot switch your own model mid-run.** Instead, spawn a sub-agent using the Agent tool with the selected model and delegate all remaining steps (1–10) to it. Pass the source path and filename explicitly in the prompt.

Example prompt to sub-agent:
> Run ops/ingest.md steps 1–10 for source file `{path}` (filename: `{filename}`). The pre-flight check (step 0) has already passed. Proceed from step 1.

---

### 1. Read the source file fully.

### 2. Check for existing wiki pages on the same subject

Before reading or planning anything further:
```bash
sqlite3 /Users/filipe/obsidian/miko/miko.db \
  "SELECT title, type, summary FROM index_pages WHERE title LIKE '%keywords%';"
```

Note which pages already exist. You will **update** them in step 5/6, not recreate them.

### 3. Briefly summarize to the human:
- The source's main subject (one sentence)
- 3–5 key ideas
- Which existing wiki pages it touches (from step 2)
- Which new pages it might warrant

Then proceed with steps 4–10 autonomously.

### 4. Write a source summary page in `wiki/sources/`

Filename format: `source-title-slug.md`. Type: `source`.

- **Every source file gets a source page, regardless of content length or type.** Personal notes, lists, stubs, and admin files all get indexed.
- Body: describe what the file contains in your own words. Aim for 200–400 words for substantive files; a single paragraph is acceptable for thin files (lists, stubs, short notes).
- Link every concept and entity using [[wikilinks]].
- Source pages do not need a `## Sources` section.

### 5. Update or create concept pages in `wiki/concepts/`

**For each concept you identified in step 3:**

Check existence first (do this before writing any file):
```bash
sqlite3 /Users/filipe/obsidian/miko/miko.db \
  "SELECT title FROM index_pages WHERE title = 'Exact Concept Name';"
```

- If it exists: read the file fully, then revise the body, update the `updated` date, and add the current source to the `## Sources` section if not already listed.
- If it does not exist: create `wiki/concepts/concept-slug.md`. Type: `concept`. Body: 150–300 words. Present tense. Always include a `## Sources` section listing `[[Source Page Title]]`.

### 6. Update or create entity pages in `wiki/entities/`

Same update-or-create logic as step 5. Entities are named people, tools, organisations, or projects. Always include a `## Sources` section on new entity pages; append to it on updates.

### 7. Note stubs in the source page body

For concepts referenced but not yet written:
`See also: concept-name (not yet written)`

### 8. Update the database index

One INSERT OR REPLACE per page created or modified. Always include `source_id` — use the id of the source file being ingested (retrieved from the `sources` table in step 9):
```bash
sqlite3 /Users/filipe/obsidian/miko/miko.db \
  "INSERT OR REPLACE INTO index_pages (title, type, summary, updated, source_id)
   VALUES ('Page Title', 'concept', 'One-line summary.', 'YYYY-MM-DD', SOURCE_ID);"
```

For pages that already exist and are being updated, preserve any existing `source_id` if it already has one — only set it if it is currently NULL.

### 9. Update the sources table

Mark the source as ingested:
```bash
sqlite3 /Users/filipe/obsidian/miko/miko.db \
  "UPDATE sources SET status = 'ingested', ingested = 'YYYY-MM-DD'
   WHERE filename = 'filename.md';"
```

If the file was not yet in the sources table, insert it:
```bash
sqlite3 /Users/filipe/obsidian/miko/miko.db \
  "INSERT OR IGNORE INTO sources (path, filename, filetype, discovered, status, ingested)
   VALUES ('subdir/filename.md', 'filename.md', 'md', 'YYYY-MM-DD', 'ingested', 'YYYY-MM-DD');"
```

### 10. Append a log entry

```bash
sqlite3 /Users/filipe/obsidian/miko/miko.db \
  "INSERT INTO log (timestamp, operation, subject, status, summary, details)
   VALUES ('YYYY-MM-DD HH:MM', 'ingest', 'source-filename.md', 'complete',
           'One sentence summary.',
           '[\"Source page: [[Title]]\", \"Concepts created: [[X]], [[Y]]\", \"Entities updated: [[Z]]\", \"New pages: [[A]], [[B]]\", \"Stubs noted: name1\"]');"
```

---

## Files with no readable content

The only case where a source page is **not** created is when the file is entirely unreadable (e.g. a binary file with no extractable text, or a file that is literally empty — zero bytes or whitespace only). In that case:

**Mark ignored in sources table:**
```bash
sqlite3 /Users/filipe/obsidian/miko/miko.db \
  "UPDATE sources SET status = 'ignored', notes = 'Reason'
   WHERE filename = 'filename.md';"
```

**Log the partial ingest:**
```bash
sqlite3 /Users/filipe/obsidian/miko/miko.db \
  "INSERT INTO log (timestamp, operation, subject, status, summary, details)
   VALUES ('YYYY-MM-DD HH:MM', 'ingest', 'filename.md', 'partial',
           'File has no readable content; no wiki pages created.',
           '[\"No source page created\"]');"
```

For all other files — including personal notes, lists, gift ideas, admin tasks, grocery lists, short stubs, and sensitive-seeming data — create a source page and mark as ingested. Do not apply personal judgement about whether a note is "worth" indexing.

---

## task.md: Master Personal Todo List

- **File:** `/Users/filipe/obsidian/miko/task.md`
- Extract actionable personal tasks from the source and append as unchecked items.
- Format: `- [ ] Task description [[Source Page Title]]`
- Read the file first to avoid duplicates.
- Never delete existing items. Never modify the footer (`---` / `*My notes - do not edit below this line*`).

---

## Hard constraints

- Do not reproduce large chunks of source text in wiki pages.
- Do not create a new page if one already exists on the same topic.
- Do not write to anything inside `raw/`.
- Do not write to `index.md` or `log.md` — use the database only.
- **Never delete rows from `log` or `sources`.** These tables are append-only. If you made an error, add a corrective log entry instead.
