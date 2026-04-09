---
title: "Context-Aware Knowledge Organization"
type: concept
tags: [architecture, knowledge-management, organization]
created: 2026-04-09
updated: 2026-04-09
---

A higher-order organizational principle in [[LLM-wiki Architecture]] where contexts (such as "Personal," "Research," "Work") exist as top-level containers above topics and pages. Different contexts can treat the same topic with different levels of rigor, curation, and purpose.

For example, a "Health" topic might exist in both Personal and Research contexts:

- **Personal/Health** — subjective, experiential, lightly curated
- **Research/Health** — rigorous sourcing, peer-reviewed papers, formal structure

Implementation options:

- **Directories** — contexts as top-level folders (e.g., `wiki/personal/topics/`, `wiki/research/topics/`), all topics treated uniformly
- **Tags** — contexts as YAML frontmatter tags, allowing the same page to exist in multiple contexts simultaneously
- **Hybrid** — both directories and tags, maximizing flexibility

Key insight: many knowledge systems conflate topics and contexts, leading to either duplicate pages or rigid hierarchies. By making contexts explicit and first-class, the system acknowledges that the same knowledge may be relevant in different ways to different purposes.

This pattern is especially useful for individuals who navigate multiple domains (technical work, personal growth, research interests, creative projects) and need different organizational rigor for each.

---
*My notes - do not edit below this line*
