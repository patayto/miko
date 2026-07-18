"""Central configuration: paths, source registry, split ratios, model names.

Everything that more than one module needs lives here so milestones stay
consistent (same sources, same paths, same seed).
"""

from dataclasses import dataclass
from pathlib import Path

# voice/ project root (this file lives at voice/src/voiceclone/config.py)
PROJECT_ROOT = Path(__file__).resolve().parents[2]
# miko repo root; raw inputs live here and are strictly read-only
REPO_ROOT = PROJECT_ROOT.parent
RAW_ROOT = REPO_ROOT / "raw"

DATA_DIR = PROJECT_ROOT / "data"
ADAPTERS_DIR = PROJECT_ROOT / "adapters"
CHROMA_DIR = PROJECT_ROOT / "chroma"


@dataclass(frozen=True)
class Source:
    """One training corpus: where its raw files live and how to parse them."""

    name: str          # short id used in paths, adapter names, metadata
    raw_dirs: tuple[str, ...]  # subdirectories of raw/ to walk
    filetypes: tuple[str, ...]  # extensions to pick up


SOURCES: dict[str, Source] = {
    "obsidian": Source(
        name="obsidian",
        raw_dirs=("obsidian-notes", "logseq-journals", "logseq-pages"),
        filetypes=(".md",),
    ),
    "icloud": Source(
        name="icloud",
        raw_dirs=("icloud-raw",),
        filetypes=(".html",),
    ),
    "aichats": Source(
        name="aichats",
        raw_dirs=("ai-chats",),
        filetypes=(".json",),
    ),
}

# Train/holdout split (document-level, seeded — holdout is never trained on
# and never indexed for RAG)
HOLDOUT_FRACTION = 0.15
SPLIT_SEED = 42

# Models
BASE_MODEL = "Qwen/Qwen2.5-3B"          # served by vLLM; trained via unsloth/Qwen2.5-3B
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
