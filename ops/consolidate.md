# Consolidate

Scans recent human writing in `raw/` to surface connections, duplicates, and fragments that should become wiki pages.

## When to use

Run after a writing session or when asked. Operates on recent files in `raw/logseq-journals/`, `raw/logseq-pages/`, and `raw/obsidian-notes/`.

## Steps

1. **Read recent source files** starting from the most recent dates.

2. **Pull all current wiki pages** to cross-reference:
   ```bash
   sqlite3 /Users/filipe/obsidian/miko/miko.db \
     "SELECT title, type, summary FROM index_pages WHERE ignored = 0 ORDER BY type, title;"
   ```

3. **Find fragments:** blocks containing a clear idea with no corresponding wiki page.

4. **Find implicit connections:** concepts mentioned in human writing that match an existing page but are not wikilinked. Note these — do not modify raw files.

5. **Find duplicate concepts:** the same idea under different names across multiple files.

6. **Present all findings to the human before doing anything:**

```
## Consolidate findings - YYYY-MM-DD

### Fragments that could become wiki pages
- "quote or paraphrase" — from logseq-journals/YYYY_MM_DD.md
  Suggested page: [[concept-name]]

### Unlinked connections
- You mentioned "topic" in obsidian-notes/file.md — matches [[existing-wiki-page]]

### Possible duplicates
- "new name" (journals/today) appears to overlap with [[existing-page]]

### Proposed actions — awaiting your approval
1. Create [[concept-name]] from the fragment above
2. Note the connection in [[existing-wiki-page]]
3. Merge "new name" into [[existing-page]]?
```

7. **Wait for human approval.** Do not create or update any pages until confirmed.

8. **Execute approved actions.** Update `index_pages` for each page created or modified:
   ```bash
   sqlite3 /Users/filipe/obsidian/miko/miko.db \
     "INSERT OR REPLACE INTO index_pages (title, type, summary, updated)
      VALUES ('Page Title', 'concept', 'Summary.', 'YYYY-MM-DD');"
   ```

9. **Append a log entry:**
   ```bash
   sqlite3 /Users/filipe/obsidian/miko/miko.db \
     "INSERT INTO log (timestamp, operation, subject, status, summary, details)
      VALUES ('YYYY-MM-DD HH:MM', 'consolidate', '', 'complete',
              'One sentence.',
              '[\"Files scanned: N\", \"Fragments found: N\", \"Actions approved: N\", \"Pages created: [[x]]\", \"Pages updated: [[y]]\"]');"
   ```

## Rules

- Do not write to `raw/` files.
- Do not create or update wiki pages without human approval.
- Do not add [[wikilinks]] inside raw files.
- Do not write to `index.md` or `log.md` — use the database only.
