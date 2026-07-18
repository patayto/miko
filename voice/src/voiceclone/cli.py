"""Typer CLI — the spine every milestone hangs a command off.

Commands are stubs until their milestone is built:
  prep, stats        -> milestone 2 (data pipeline)
  rag index|query    -> milestone 3 (RAG)
  serve-smoke        -> milestone 5 (vLLM multi-LoRA smoke test)
  route              -> milestone 6 (LangGraph router)
  eval               -> milestone 7 (DeepEval suite)
"""

import typer

app = typer.Typer(no_args_is_help=True, add_completion=False)
rag_app = typer.Typer(no_args_is_help=True, help="RAG index + retrieval (milestone 3).")
app.add_typer(rag_app, name="rag")


def _not_built(milestone: int) -> None:
    typer.echo(f"Not built yet — this command arrives in milestone {milestone}.")
    raise typer.Exit(code=1)


@app.command()
def prep(
    source: str = typer.Option("all", help="Source to prepare: obsidian | icloud | aichats | all"),
) -> None:
    """Parse raw sources into cleaned train/holdout JSONL splits (milestone 2)."""
    _not_built(2)


@app.command()
def stats() -> None:
    """Report corpus stats: docs, tokens, lengths, dedupe rate (milestone 2)."""
    _not_built(2)


@rag_app.command("index")
def rag_index() -> None:
    """Chunk, embed, and index the train corpora into Chroma (milestone 3)."""
    _not_built(3)


@rag_app.command("query")
def rag_query(
    query: str,
    source: str = typer.Option(None, help="Restrict to one source's collection."),
    k: int = typer.Option(5, help="Number of passages to retrieve."),
) -> None:
    """Retrieve passages for a query (milestone 3)."""
    _not_built(3)


@app.command("serve-smoke")
def serve_smoke(
    url: str = typer.Option(..., help="vLLM tunnel URL, e.g. https://xxx.trycloudflare.com"),
) -> None:
    """Smoke-test the vLLM endpoint: list models, compare base vs adapters (milestone 5)."""
    _not_built(5)


@app.command()
def route(
    query: str,
    url: str = typer.Option(..., help="vLLM tunnel URL."),
) -> None:
    """Route a query through the LangGraph classify->retrieve->generate graph (milestone 6)."""
    _not_built(6)


@app.command("eval")
def eval_cmd(
    source: str = typer.Option("all", help="Holdout source(s) to evaluate against."),
) -> None:
    """Run the DeepEval voice-similarity + RAG metrics suite (milestone 7)."""
    _not_built(7)
