# Ingest

Processes a source file from `raw/` and integrates its knowledge into the wiki.

## When to use

Run when the human points you at a specific file in `raw/`, drops a new file into `raw/`, or asks you to process a Logseq journal entry or Obsidian note.

## Steps

1. Read the source file fully.

2. Check `index.md` for any existing page on the same subject. If one exists, you will update it in step 5 rather than create a new page.

3. Briefly summarize to the human:
   - The source's main subject (one sentence)
   - 3-5 key ideas
   - Which existing wiki pages it touches
   - Which new pages it might warrant
   Then proceed with steps 4-9 autonomously.

4. Write a source summary page in `wiki/sources/` using the filename format `source-title-slug.md`.
   - type: source
   - Body: 200-400 words summarising key claims in your own words. Do not reproduce the source text.
   - Link every concept and entity using [[wikilinks]].

5. Update or create concept pages in `wiki/concepts/`.
   - If a page exists: read it fully, then revise the body to incorporate what this source adds. Update the `updated` date.
   - If no page exists: create one. type: concept. Body: 150-300 words. Write in present tense. No references to "this article" or "this source".

6. Update or create entity pages in `wiki/entities/` for each named person, tool, organisation, or project.
   - Same update-or-create rule as concepts.

7. If the source references concepts that deserve their own page but you did not create one, note them in the source page body as: `See also: concept-name (not yet written)`.

8. Update `index.md`. Add or update one row per page created or modified.

9. Append to `log.md`:

```
## [YYYY-MM-DD HH:MM] ingest | filename
Status: complete
Summary: one sentence.
Details:
- Source page: [[source-page-title]]
- Concepts updated: [[x]], [[y]]
- Entities updated: [[a]]
- New pages created: [[b]], [[c]]
- Stubs noted: name1, name2
```

## Rules

- Do not reproduce large chunks of source text in wiki pages.
- Do not create a new page if one already exists on the same topic.
- Do not write to anything inside `raw/`.
- If a source file is empty, a stub, or contains no substantive content: do not create wiki pages. Instead, append a row to the "Ignored Sources" section of `index.md` with a note explaining why (e.g., "empty stub", "bare URL only"). This prevents re-scanning.

## task.md: Master Personal Todo List

### Purpose

`task.md` is a persistent, master todo list that captures all actionable personal tasks extracted from sources throughout the wiki system. It serves as a single source of truth for the human's open action items, regardless of where they originated.

### Location & Format

- **File:** `/Users/filipe/obsidian/miko/task.md`
- **Type:** query
- **Structure:** Checklist format with sections by category/theme
- **Format for each todo:** `- [ ] Task description [[Source Page Title]]`

### Rules for Agents

1. **When to update:** Any source you ingest (Logseq journals, Obsidian notes, or other sources) may contain actionable items. Extract them.

2. **How to add tasks:** 
   - Read the current `task.md` to avoid duplicates
   - Append new tasks as unchecked items (`- [ ]`)
   - Always include a backlink to the source page where the task was discovered
   - Organize by logical section/category if possible

3. **Structure example:**
   ```
   - [ ] Specific actionable task [[Source Page Name]]
   ```

4. **Never delete items** from the master list. The human may mark them complete elsewhere and will manage the list themselves.

5. **Always preserve the footer:** The line `---` followed by `*My notes - do not edit below this line*` must remain unchanged.

6. **Avoid duplicates:** Before adding a task, scan the list to ensure it doesn't already exist. Reword rather than duplicate if needed.

### When NOT to Update

- If the source is purely conceptual or knowledge-focused (no action items)
- If the extracted items are setup TODOs for incomplete course outlines or templates (use judgment)

### Example

If ingesting a source with tasks like "Research X", "Contact Y", "Fix Z", append them as:
```
- [ ] Research X [[Source Title]]
- [ ] Contact Y [[Source Title]]
- [ ] Fix Z [[Source Title]]
```
