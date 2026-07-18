# Lint

Health-checks the wiki and reports issues. Does not modify anything unless the human approves specific fixes.

## When to use

Run periodically — weekly, or when the wiki feels stale. No input required.

## Steps

1. **Load all current pages** from the database:
   ```bash
   sqlite3 /Users/filipe/obsidian/miko/miko.db \
     "SELECT title, type, updated FROM index_pages WHERE ignored = 0 ORDER BY type, title;"
   ```

2. **Read each wiki page** listed in the results.

3. **Check for stale pages** (not updated in 90+ days):
   ```bash
   sqlite3 /Users/filipe/obsidian/miko/miko.db \
     "SELECT title, type, updated FROM index_pages
      WHERE ignored = 0 AND updated < date('now', '-90 days')
      ORDER BY updated;"
   ```

4. **Check for orphan pages:** pages with no inbound [[wikilinks]] from any other wiki page.

5. **Check for broken links:** [[wikilinks]] in wiki page bodies that have no matching `title` in `index_pages`:
   ```bash
   # After extracting wikilinks from page bodies, check each one:
   sqlite3 /Users/filipe/obsidian/miko/miko.db \
     "SELECT title FROM index_pages WHERE title = 'Suspected Missing Page';"
   ```

6. **Check for stubs:** pages or inline notes marked as `(not yet written)`.

7. **Suggest 2–3 topics** worth investigating that have no wiki page yet.

8. **Suggest 1–2 types of sources** worth finding to fill gaps.

9. **Present the report:**

```
## Lint report - YYYY-MM-DD

### Stale pages (>90 days)
- [[page-name]] — last updated YYYY-MM-DD

### Orphan pages
- [[page-name]] — no inbound links

### Broken links
- [[missing-page]] — linked from [[some-page]], not in index

### Stubs
- concept-name — noted in [[source-page]], not yet written

### Suggested topics to investigate
1. ...
2. ...

### Suggested sources to find
1. ...
```

10. **Wait for human instructions** on which issues to fix.

11. **Execute approved fixes.** Update `index_pages` for any pages modified:
    ```bash
    sqlite3 /Users/filipe/obsidian/miko/miko.db \
      "UPDATE index_pages SET updated = 'YYYY-MM-DD', summary = 'New summary.' WHERE title = 'Page Title';"
    ```

12. **Append a log entry:**
    ```bash
    sqlite3 /Users/filipe/obsidian/miko/miko.db \
      "INSERT INTO log (timestamp, operation, subject, status, summary, details)
       VALUES ('YYYY-MM-DD HH:MM', 'lint', '', 'complete',
               'N issues found, N fixed.',
               '[\"Stale: N\", \"Orphans: N\", \"Broken links: N\", \"Stubs: N\", \"Fixes applied: list any\"]');"
    ```

## Rules

- Do not write to `raw/` files.
- Do not create or update wiki pages without human approval.
- Do not write to `index.md` or `log.md` — use the database only.
