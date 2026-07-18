# voiceclone

A weekend learning project living inside the miko repo (but fully self-contained):
fine-tune per-source LoRA adapters on my own writing so a model outputs in my
style, plus RAG over the same corpus, a LangGraph router, and a DeepEval suite.

Sources (all under `../raw/`, read-only):
- `obsidian` — Obsidian + Logseq markdown (via symlinks)
- `icloud` — iCloud Notes HTML export
- `aichats` — AI chat export JSON, **user-role turns only** (dropped into `raw/ai-chats/`)

## Layout

- `src/voiceclone/` — parsing, pipeline, rag, router, evals + `cli.py` (Typer)
- `notebooks/` — Colab notebooks: `01_train_lora` (Unsloth QLoRA), `02_serve_vllm` (multi-LoRA + cloudflared tunnel)
- `data/`, `adapters/`, `chroma/` — gitignored outputs; never committed

## Usage

Everything local runs through uv:

```bash
uv run voice --help
uv run pytest
```

GPU work (training, vLLM serving) runs on Google Colab; data moves via Google
Drive (`MyDrive/voiceclone/`). Local code talks to vLLM through a cloudflared
tunnel URL as an OpenAI-compatible endpoint.

## Milestones

1. ✅ Repo cleanup + scaffold
2. Data pipeline: `voice prep`, `voice stats` (85/15 doc-level seeded split)
3. RAG: `voice rag index`, `voice rag query`
4. LoRA fine-tuning on Colab (one adapter per source)
5. vLLM multi-LoRA serving: `voice serve-smoke`
6. LangGraph router: `voice route`
7. DeepEval: `voice eval`
8. Stretch: hyperparameter sweep, Terraform S3 detour

Base model: `Qwen/Qwen2.5-3B` (fp16 on T4). Embeddings: `BAAI/bge-small-en-v1.5`
(CPU — this is an Intel Mac, so torch is pinned by platform to 2.2.2).

## Privacy

Training corpora, adapters, and the vector store derive from personal journals.
They stay in gitignored directories and must never be committed or published.
The repo has no remote; if it ever gets one, run `git filter-repo` first.
