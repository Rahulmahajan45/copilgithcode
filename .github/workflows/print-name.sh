#!/usr/bin/env bash
# Usage:
#   ./scripts/print_names.sh        # uses scripts/sample.txt
#   ./scripts/print_names.sh FILE   # use a different file
set -euo pipefail

file="${1:-scripts/sample.txt}"

if [[ ! -f "$file" ]]; then
  echo "Error: file not found: $file" >&2
  exit 1
fi

# Read file lines into an array (preserves spaces and blank lines)
names=()
while IFS= read -r line || [[ -n "$line" ]]; do
  names+=("$line")
done < "$file"

# Iterate with a for loop and print each name
for name in "${names[@]}"; do
  printf 'My name is "%s"\n' "$name"
done
