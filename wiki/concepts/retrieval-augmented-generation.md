---
title: "Retrieval-Augmented Generation"
type: concept
tags: [rag, llm, retrieval, generation, context]
created: 2026-04-09
updated: 2026-04-09
---

A technique for augmenting large language model inference by retrieving relevant documents or context from a knowledge base before generating responses. RAG separates knowledge storage from generation, allowing models to reference external information without requiring all of it to be loaded into context on every request.

RAG maintains response quality while improving latency and reducing token overhead. In [[Claude Projects]], RAG is automatically enabled when projects accumulate enough files that full context would become inefficient. The system intelligently retrieves relevant documents from the uploaded knowledge base, passes them to Claude, and generates responses—all while keeping response times low and token usage manageable.

This makes RAG particularly valuable for [[Usage Limits|managing usage limits]] in projects with large codebases, documentation sets, or knowledge repositories. The technique decouples "what the model knows" from "what the model holds in context at any moment."

RAG also enables [[Dual-Layer Knowledge System|dual-layer knowledge systems]] where external information sources can be queried to validate or challenge existing facts without loading all sources into memory. In [[Knowledge Validation Agent]] systems, RAG is used for semantic similarity matching to avoid re-processing already-ingested information.

See also: [[Claude Projects]] (implementation), [[Fuzzy Cache]] (semantic-similarity variant), [[Dual-Layer Knowledge System]]

---
*My notes - do not edit below this line*
