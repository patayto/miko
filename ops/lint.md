# Lint

Health-checks the wiki and reports issues. Does not modify anything unless the human approves specific fixes.

## When to use

Run periodically - weekly, or when the wiki feels stale. No input required.

## Steps

1. Read `index.md` to get the full list of wiki pages.

2. Read each wiki page listed in `index.md`.

3. Check for orphan pages: pages with no inbound [[wikilinks]] from any other wiki page.

4. Check for broken links: [[wikilinks]] in wiki page bodies that do not match any page in `index.md`.

5. Check for stubs: pages or inline notes marked as "not yet written".

6. Check for stale pages: pages whose `updated` date is more than 90 days ago.

7. Suggest 2-3 topics worth investigating that have no wiki page yet.

8. Suggest 1-2 types of sources worth finding to fill gaps.

9. Present the report:

```
## Lint report - YYYY-MM-DD

### Orphan pages
- [[page-name]] - no inbound links

### Broken links
- [[missing-page]] - linked from [[some-page]], does not exist

### Stubs
- concept-name - noted in [[source-page]] on YYYY-MM-DD, not yet written

### Stale pages
- [[old-page]] - last updated YYYY-MM-DD

### Suggested topics to investigate
1. ...
2. ...

### Suggested sources to find
1. ...
```

10. Wait for human instructions on which issues to fix.

11. Execute approved fixes. Update `index.md`. Append to `log.md`.

12. Append to `log.md`:

```
## [YYYY-MM-DD HH:MM] lint
Status: complete
Summary: N issues found, N fixed.
Details:
- Orphans: N
- Broken links: N
- Stubs: N
- Fixes applied: list any
```
