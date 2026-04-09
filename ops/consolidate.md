# Consolidate

Scans recent human writing in `raw/` to surface connections, duplicates, and fragments that should become wiki pages.

## When to use

Run after a writing session or when asked. Operates on recent files in `raw/logseq-journals/`, `raw/logseq-pages/`, and `raw/obsidian-notes/`.

## Steps

1. Read recent journal files starting from the most recent dates. Read any pages or notes the human mentions.

2. Find fragments: blocks or passages containing a clear idea with no corresponding wiki page and no [[wikilink]] to one.

3. Find implicit connections: concepts mentioned in the human's writing that already have a wiki page but are not linked. Note these for the human - do not modify raw files.

4. Find duplicate concepts: the same idea written about in multiple places under different names.

5. Present all findings to the human before doing anything:

```
## Consolidate findings - YYYY-MM-DD

### Fragments that could become wiki pages
- "quote or paraphrase" - from logseq-journals/YYYY_MM_DD.md
  Suggested page: [[concept-name]]

### Unlinked connections
- You mentioned "topic" in obsidian-notes/file.md - matches [[existing-wiki-page]]

### Possible duplicates
- "new name" (journals/today) appears to overlap with [[existing-page]]

### Proposed actions - awaiting your approval
1. Create [[concept-name]] from the fragment above
2. Note the connection in [[existing-wiki-page]]
3. Merge "new name" into [[existing-page]]?
```

6. Wait for human approval. Do not create or update any pages until confirmed.

7. Execute approved actions. Update `index.md`. Append to `log.md`.

8. Append to `log.md`:

```
## [YYYY-MM-DD HH:MM] consolidate
Status: complete
Summary: one sentence.
Details:
- Files scanned: N
- Fragments found: N
- Actions approved: N
- Pages created: [[x]], [[y]]
- Pages updated: [[a]]
```

## Rules

- Do not write to `raw/` files.
- Do not create or update wiki pages without human approval.
- Do not add [[wikilinks]] inside raw files.
