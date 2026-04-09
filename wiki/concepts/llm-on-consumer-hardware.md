---
title: "LLM on Consumer Hardware"
type: concept
tags: [llm, local-inference, hardware, ps5, gpu]
created: 2026-04-09
updated: 2026-04-09
---

Running large language models locally on consumer devices — gaming consoles, laptops, desktop GPUs — is an active area of interest as model sizes shrink and quantisation techniques improve. The core constraint is VRAM: LLM inference requires holding model weights in fast memory, which consumer GPUs have in limited supply.

## PS5 feasibility

The PS5 uses an AMD RDNA 2 GPU with 16 GB of unified memory shared between CPU and GPU. On paper this is competitive with mid-range discrete GPUs. In practice, running LLMs on PS5 is constrained by:

- **Software access:** The PS5 GPU is not exposed via standard ML frameworks (PyTorch, ROCm). There is no official path for running arbitrary compute workloads.
- **Jailbreak requirement:** Community experiments on PS4/PS5 Linux suggest a jailbreak is a prerequisite for any custom compute use. This limits the approach to specific firmware versions and is not a stable platform.
- **Ecosystem immaturity:** Unlike desktop AMD GPUs with ROCm support, the PS5 GPU has no supported ML runtime.

Community discussions (fast.ai forums, Reddit r/LocalLLM, Hacker News) confirm the theoretical interest but general consensus is that it is not a practical inference platform without significant reverse-engineering effort.

## Contrast with supported paths

Practical local LLM inference on consumer hardware typically runs on: NVIDIA GPUs (CUDA), Apple Silicon (Metal/MLX), or AMD desktop GPUs with ROCm. Quantised models (GGUF via llama.cpp) can run on CPU-only or mixed CPU+GPU setups.

---
*My notes - do not edit below this line*
