---
title: "2026 Mar 27 - Is This Still True?"
type: source
tags: [knowledge-management, ai-agents, fact-checking, research]
created: 2026-04-09
updated: 2026-04-09
---

Design document for a knowledge management system that automatically validates whether information in a personal knowledge base remains accurate and relevant over time. The system uses AI agents to scan cached, RAG-backed knowledge, search for recent information (via SerpAPI and Google Scholar), and flag outdated or challenged facts for human review.

The architecture separates **knowledge** (the human's written understanding of a topic) from **information** (source materials like papers, blog posts, videos). A Topic aggregates both, with a queue of new information sources and a set of Facts. Each Fact has supporting sources and challenges (newer information that may contradict or supersede it). An agent runs periodic updates, proposing new Facts or requesting human-in-the-loop validation for significant changes.

The design leverages **citation patterns** as a signal for research evolution: by tracking which papers co-cite with foundational work (e.g., Transformers + MoE), the system can detect when new techniques become standard. The system uses postgres as backing store, with optional RAG/pgvector for semantic similarity matching and grouping related Facts.

Tech stack proposed: FastAPI, postgres, pydantic-ai, SQLAlchemy + Alembic, with optional extensions for task queues (Celery), observability (Langfuse/structlog), and a React frontend.

Key design tensions: whether agents should be global or topic-specific; how to handle immutable Fact history while allowing updates; which updates warrant human review vs. silent updates; whether to track rejected facts and removed challenges; how to prevent agent re-processing of already-ingested information.

---
*My notes - do not edit below this line*
