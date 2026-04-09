---
title: "Dual-Layer Knowledge System"
type: concept
tags: [knowledge-management, architecture]
created: 2026-04-09
updated: 2026-04-09
---

An organizational principle that separates personal understanding (knowledge) from source materials (information) in a knowledge management system. Knowledge is the human's written synthesis of a topic—their beliefs, connections, and mental model. Information is the raw source material: research papers, blog posts, videos, and other external references that informed that knowledge.

This separation serves multiple purposes:

1. **Update clarity**: A Fact can be updated without changing the human's Knowledge document; a Knowledge document can be rewritten without necessarily invalidating all Facts.
2. **Source accountability**: Each Fact tracks which Information sources support it and which newer sources challenge it, creating a clear audit trail.
3. **Semantic grouping**: Multiple pieces of Information may converge on the same Fact or Knowledge, and the system can identify conceptual equivalence across diverse sources.
4. **Validation scope**: When validating whether Knowledge is still true, the system fetches the latest Information, compares it against existing sources and challenges, and only flags the Knowledge for human review if conflicts emerge.

In practical terms: "Transformers" might be a Topic. The human's Knowledge on Transformers is their own summary of the architecture, benefits, and use cases. The Information layer contains links to "Attention Is All You Need," MoE papers, recent benchmarks, and competing architectures. Facts capture atomic claims (e.g., "Standard transformer uses linear complexity in sequence length via multi-head attention with masking"). Challenges to that Fact might include newer work on quadratic attention bottlenecks or recent efficiency improvements.

See also: [[LLM-wiki Architecture]], [[Knowledge Validation Agent]]

---
*My notes - do not edit below this line*
