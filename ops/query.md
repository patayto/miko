# Query

Answers a question using wiki content as the knowledge base.

## When to use

Run when the human asks a question the wiki should be able to answer, or asks for a synthesis across multiple topics.

## Steps

1. **Find relevant pages** using the database:

   By keyword in title or summary:
   ```bash
   sqlite3 /Users/filipe/obsidian/miko/miko.db \
     "SELECT title, type, summary FROM index_pages
      WHERE ignored = 0 AND (title LIKE '%keyword%' OR summary LIKE '%keyword%')
      ORDER BY type;"
   ```

   By type:
   ```bash
   sqlite3 /Users/filipe/obsidian/miko/miko.db \
     "SELECT title, summary FROM index_pages WHERE type = 'concept' AND ignored = 0;"
   ```

   Most recently updated (useful for "what's been happening"):
   ```bash
   sqlite3 /Users/filipe/obsidian/miko/miko.db \
     "SELECT title, type, updated FROM index_pages WHERE ignored = 0 ORDER BY updated DESC LIMIT 20;"
   ```

2. **Read the full content** of each relevant wiki page. If a page links to others that seem relevant, read those too.

3. **Write a clear answer.** Cite specific wiki pages using [[wikilinks]] for every claim. If the wiki does not cover something, say so explicitly — do not draw on outside knowledge.

4. **Present the answer to the human.**

5. **Ask:** "Should I save this as a query page?"
   - **Yes:** save to `wiki/queries/query-slug.md` with `type: query`. Then:
     ```bash
     sqlite3 /Users/filipe/obsidian/miko/miko.db \
       "INSERT OR REPLACE INTO index_pages (title, type, summary, updated)
        VALUES ('Query Title', 'query', 'One-line summary.', 'YYYY-MM-DD');"
     ```
   - **No:** proceed to logging.

6. **Append a log entry:**
   ```bash
   sqlite3 /Users/filipe/obsidian/miko/miko.db \
     "INSERT INTO log (timestamp, operation, subject, status, summary, details)
      VALUES ('YYYY-MM-DD HH:MM', 'query', 'brief question summary', 'complete',
              'One sentence on what was found.',
              '[\"Pages consulted: [[x]], [[y]], [[z]]\", \"Saved as query page: yes — [[title]] | no\"]');"
   ```

## Notes

- If the wiki lacks enough information to answer, say so and suggest which ingest or consolidate operation would fill the gap.
- Strong answers are worth saving. A saved query page becomes part of the wiki and compounds over time.
