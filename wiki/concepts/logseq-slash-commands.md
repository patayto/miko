---
title: "LogSeq Slash Commands"
type: concept
tags: [logseq, productivity, note-taking, commands]
created: 2026-04-09
updated: 2026-04-09
---

[[LogSeq]] slash commands are an inline command palette triggered by typing `/` inside any block. They insert structured content, link to dates, run queries, and activate other editor features without leaving the keyboard.

Notable slash commands include:

- `/time` — inserts the current time as a timestamp. Essential for [[Interstitial Journaling]] and meeting notes where temporal context matters.
- `/date` — links to a specific date page. Any block that references a date page will surface on that page, making this a lightweight future-reminder mechanism (writing to your future self).
- `/query` — inserts a Datalog query block, enabling dynamic views of content across the graph.

Beyond slash commands, [[LogSeq]] supports **advanced commands** triggered via `<`. These provide block-level admonitions for multiline structured content:

```
#+BEGIN_TIP
multiline content here
#+END_TIP
```

Other admonition types include `#+BEGIN_NOTE`, `#+BEGIN_WARNING`, `#+BEGIN_IMPORTANT`, and `#+BEGIN_CAUTION`.

The slash command system is described as rich and worth deeper systematic research — there are likely many more commands covering templates, block references, page creation, and plugin-contributed features.

---
*My notes - do not edit below this line*
