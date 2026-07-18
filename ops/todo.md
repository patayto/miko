# Ops TODO

## Source backfill

**Background:** Prior to 2026-05-11, `source_id` in `index_pages` was treated as optional and most ingest runs did not set it. Wiki pages created before this date also lack a `## Sources` section.

**Goal:** Ensure every wiki page has (a) a `source_id` in `index_pages` and (b) a `## Sources` section in its markdown body.

**Approach (when ready to execute):**

1. Query pages with NULL source_id:
   ```bash
   sqlite3 /Users/filipe/obsidian/miko/miko.db \
     "SELECT title, type, updated FROM index_pages WHERE source_id IS NULL AND ignored = 0 ORDER BY updated;"
   ```

2. For each page, look up the log for the original ingest operation to find the source file:
   ```bash
   sqlite3 /Users/filipe/obsidian/miko/miko.db \
     "SELECT l.subject, s.id FROM log l JOIN sources s ON s.filename = l.subject
      WHERE l.operation = 'ingest' AND l.details LIKE '%Page Title%';"
   ```

3. Update `index_pages.source_id` from the matched source.

4. Read each wiki page and append a `## Sources` section above the `---` footer if missing.

**Note:** This does not require re-ingesting files — use existing `log` and `sources` entries as the authority. The `log.details` JSON array contains the page titles created per ingest run, which is sufficient to reconstruct the mapping.

**Estimated scope:** ~50–100 pages as of 2026-05-11. Grow conservatively as more files are ingested without source tracking.
