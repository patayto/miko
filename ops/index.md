# Index

Scans the `raw/` directories and populates the `sources` table with all discoverable source files. Cross-references with the `log` table to mark already-ingested files. Does not ingest or write to `wiki/`.

## When to use

Run before any batch ingest session, or when new files have been added to `raw/` and you want to update the queue. Also run if the `sources` table is empty.

## Supported file types

`.md`, `.txt`, `.pdf`, `.html`, `.py`

## Steps

1. **Scan each raw subdirectory** for supported file types. Each line of output is `fullpath|bytes`:
   ```bash
   find /Users/filipe/obsidian/miko/raw/obsidian-notes -maxdepth 1 -type f \( -name "*.md" -o -name "*.txt" -o -name "*.pdf" -o -name "*.html" -o -name "*.py" \) -exec stat -f "%N|%z" {} \; | sort
   find /Users/filipe/obsidian/miko/raw/logseq-journals -maxdepth 1 -type f \( -name "*.md" -o -name "*.txt" -o -name "*.pdf" -o -name "*.html" -o -name "*.py" \) -exec stat -f "%N|%z" {} \; | sort
   find /Users/filipe/obsidian/miko/raw/logseq-pages   -maxdepth 1 -type f \( -name "*.md" -o -name "*.txt" -o -name "*.pdf" -o -name "*.html" -o -name "*.py" \) -exec stat -f "%N|%z" {} \; | sort
   find /Users/filipe/obsidian/miko/raw/icloud-raw  -maxdepth 2 -type f \( -name "*.md" -o -name "*.txt" -o -name "*.pdf" -o -name "*.html" -o -name "*.py" \) -exec stat -f "%N|%z" {} \; | sort
   find /Users/filipe/obsidian/miko/raw  -maxdepth 1 -type f \( -name "*.md" -o -name "*.txt" -o -name "*.pdf" -o -name "*.html" -o -name "*.py" \) -exec stat -f "%N|%z" {} \; | sort
   ```

2. **For each file found**, compute from the `fullpath|bytes` output:
   - `path` — relative to `raw/`, e.g. `obsidian-notes/2025-12-01.md`
   - `filename` — basename only, e.g. `2025-12-01.md`
   - `filetype` — extension without dot, e.g. `md`
   - `discovered` — today's date
   - `content_length` — byte count from stat output (field after `|`), e.g. `5432`
   - `content_size` — MB: byte count ÷ 1048576, rounded to 6 decimal places, e.g. `0.005180`

   Insert if not already in `sources` (use INSERT OR IGNORE to skip existing records):
   ```bash
   sqlite3 /Users/filipe/obsidian/miko/miko.db \
     "INSERT OR IGNORE INTO sources (path, filename, filetype, discovered, status, content_length, content_size)
      VALUES ('obsidian-notes/2025-12-01.md', '2025-12-01.md', 'md', '2026-04-09', 'pending', 5432, 0.005180);"
   ```

3. **Cross-reference with the log** to mark already-ingested sources. For each source whose `filename` matches a `subject` in `log` with `operation = 'ingest'` and `status = 'complete'`, update its status:
   ```bash
   sqlite3 /Users/filipe/obsidian/miko/miko.db << 'SQL'
   UPDATE sources
   SET status = 'ingested',
       ingested = (
           SELECT MAX(timestamp) FROM log
           WHERE log.subject = sources.filename
             AND log.operation = 'ingest'
             AND log.status = 'complete'
       )
   WHERE filename IN (
       SELECT DISTINCT subject FROM log
       WHERE operation = 'ingest' AND status = 'complete'
   );
   SQL
   ```

   Also mark ignored sources (log status = 'partial', reason is stub):
   ```bash
   sqlite3 /Users/filipe/obsidian/miko/miko.db << 'SQL'
   UPDATE sources
   SET status = 'ignored',
       notes = (
           SELECT summary FROM log
           WHERE log.subject = sources.filename
             AND log.operation = 'ingest'
             AND log.status = 'partial'
           ORDER BY timestamp DESC LIMIT 1
       )
   WHERE filename IN (
       SELECT DISTINCT subject FROM log
       WHERE operation = 'ingest' AND status = 'partial'
   ) AND status = 'pending';
   SQL
   ```

4. **Report counts** to the human:
   ```bash
   sqlite3 /Users/filipe/obsidian/miko/miko.db \
     "SELECT status, COUNT(*) FROM sources GROUP BY status;"
   ```

5. **Append a log entry:**
   ```bash
   sqlite3 /Users/filipe/obsidian/miko/miko.db \
     "INSERT INTO log (timestamp, operation, subject, status, summary, details)
      VALUES ('YYYY-MM-DD HH:MM', 'index', 'raw/', 'complete',
              'Indexed N files across 3 raw directories; X pending, Y ingested, Z ignored.',
              '[\"New sources added: N\", \"Already ingested: Y\", \"Ignored stubs: Z\"]');"
   ```

## Notes

- `INSERT OR IGNORE` ensures this operation is safely idempotent — re-running it will not create duplicate records.
- Do not delete or modify existing `sources` records; only add new ones or update status.
- The `sources` table is the authoritative queue for ingest. Ingest operations should always start by querying `sources WHERE status = 'pending'`.
