#!/usr/bin/env bash
# ops/run.sh <op> <file>
# e.g. ./ops/run.sh ingest raw/logseq-journals/2025_10_15.md

set -euo pipefail

OP="$1"
TARGET="$2"

OP_INSTRUCTIONS=$(cat "../ops/${OP}.md")
TARGET_CONTENT=$(cat "$TARGET")
THE_SYSTEM_INSTRUCTIONS=$(cat "../CLAUDE.md")

OLLAMA_MODEL="gemma3:4b"
OLLAMA_ENDPOINT=http://localhost:11434/api/chat

PROMPT="You are operating a personal knowledge wiki (see `<system-context>`), performing the `${OP}` operation on the target file (`${TARGET}`). Follow the instructions in `<agent-instructions>` exactly.

<system-context>
${THE_SYSTEM_INSTRUCTIONS}
</system-context>

<agent-instructions>
Follow these instructions exactly:

${OP_INSTRUCTIONS}
</agent-instructions>

---

The file to process is: ${TARGET}

<target-content>
${TARGET_CONTENT}
</target-content>"

curl -s $OLLAMA_ENDPOINT \
  -d "$(jq -n \
    --arg model "$OLLAMA_MODEL" \
    --arg content "$PROMPT" \
    '{model: $model, messages: [{role: "user", content: $content}], stream: false}'
  )" | jq -r '.message.content'