#!/bin/bash

# 1. Fixed the curly brace position for the second variable
num_articles=${1:-1}
model=${2:-"haiku"}

# 2. Used a C-style loop to allow variable usage and correct counting
for ((i=1; i<=num_articles; i++)); do
    echo "Processing article $i of $num_articles using $model..."
    claude --allow-dangerously-skip-permissions --dangerously-skip-permissions --print --model $model /miko:ingest
done

exit 0
