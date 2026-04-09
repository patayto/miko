---
title: "Logseq Journal 2025-10-27"
type: source
tags: [journal, tooling, yoga, llm, markov-chains]
created: 2026-04-09
updated: 2026-04-09
---

An afternoon journal entry covering three unrelated explorations: migrating Claude tooling from MCP servers to Skills, using [[Markov Chains]] to model yoga sequencing, and investigating whether a PS5 can run local LLMs.

## MCP → Skills migration

The author decided to switch all MCP servers to [[Skills]] across both [[Claude Code]] and Claude Desktop. Prior research had already been done (referenced via Logseq block IDs). The migration was treated as a concrete to-do for that afternoon, not a future project.

## Yoga flows as Markov chains

A Northwestern blog post demonstrated that yoga sequences can be modelled as a [[Markov Chains|Markov chain]], where each pose has a probability distribution over valid successor poses. This framing treats a yoga flow as a probabilistic walk through pose-space rather than a fixed sequence. Supporting datasets were identified: a Kaggle yoga poses dataset, a PubMed study, and the Yoga-82 benchmark.

The author extended this into a project idea: a [[Yoga Flow Generation]] app that generates sequences in a recognisable stylistic idiom — the example given was "in the style of the waterbending scroll" (a reference to Avatar: The Last Airbender). The implication is that style would be encoded in the transition probabilities.

## LLM on PS5

A brief research thread explored whether the PS5's AMD RDNA 2 GPU could be used for local LLM inference. Community sources (fast.ai forums, Reddit, Hacker News, PS4Linux) suggest it is technically constrained: the GPU is not directly programmable via standard ML frameworks like PyTorch, and jailbreaking is a prerequisite for any Linux-based approach. The question was left open.

See also: Claude Code Skills architecture (not yet written), PS5 GPU specifications (not yet written)

---
*My notes - do not edit below this line*
