# Query

Answers a question using wiki content as the knowledge base.

## When to use

Run when the human asks a question the wiki should be able to answer, or asks for a synthesis across multiple topics.

## Steps

1. Read `index.md` to identify pages relevant to the question.

2. Read the full content of each relevant page. If a page links to others that seem relevant, read those too.

3. Write a clear answer. Cite specific wiki pages using [[wikilinks]] for every claim. If the wiki does not cover something, say so explicitly rather than drawing on outside knowledge.

4. Present the answer to the human.

5. Ask: "Should I save this as a query page?"
   - Yes: save to `wiki/queries/query-slug.md` with type: query. Update `index.md`. Append to `log.md`.
   - No: append a brief entry to `log.md` only.

6. Append to `log.md`:

```
## [YYYY-MM-DD HH:MM] query | question summary
Status: complete
Summary: one sentence on what was found.
Details:
- Pages consulted: [[x]], [[y]], [[z]]
- Saved as query page: yes - [[query-title]] | no
```

## Notes

- If the wiki lacks enough information to answer, say so and suggest which ingest or consolidate operation would fill the gap.
- Strong answers are worth saving. A saved query page becomes part of the wiki and compounds over time.
