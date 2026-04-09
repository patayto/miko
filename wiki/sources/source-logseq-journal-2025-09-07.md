---
title: "Logseq Journal 2025-09-07"
type: source
tags: [tools, dev-setup, personal-history]
created: 2026-04-09
updated: 2026-04-09
---

A personal journal entry exploring two technical tools and a nostalgic reflection on schooling history.

## Technical Setup: Qwen Code Integration

The author discovered [[Qwen Code]], a code-generation LLM, and decided to integrate it with [[Claude Code]] to extend session limits and reduce API costs. The proposed approach uses [[LiteLLM]], a unified interface for multiple LLM providers, to route requests between Claude and Qwen.

The implementation plan involves:
- Configuring environment variables (`ANTHROPIC_BASE_URL`, `ANTHROPIC_AUTH_TOKEN`) to point to a local LiteLLM server at localhost:4000
- Creating a `config.yaml` file to define the model list with provider keys (specifically OpenRouter for Qwen access)
- Optionally leveraging Docker for isolation, though the author acknowledges this is currently beyond their scope
- A minimal setup script was referenced to streamline the process

This reflects a practical approach to managing API costs and session limitations in development workflows.

## Framework Exploration: BMAD Method

The author rediscovered the [[BMAD Method]], a methodology for development which includes detailed user-guide documentation. The approach involves copying team configuration files from the method's repository into Claude Projects to bootstrap a UI agent, suggesting the method provides reusable frameworks for project structuring.

## Personal History: Schooling Timeline

The entry includes an extended personal reflection triggered by memories of a school project named "Chip" (previously called "Chipmunk"), a technology and design assignment from Year 10 (approximately 2007-2008). The author was trying to recall details of the project, potentially referencing the Alvin and the Chipmunks film franchise.

The reflection evolved into reconstructing a complete schooling timeline from 1994 (birth) through 2013 (university start), broken down by year and age at year/term starts. This suggests the author engages in detailed chronological self-documentation and memory reconstruction.

---
*My notes - do not edit below this line*
