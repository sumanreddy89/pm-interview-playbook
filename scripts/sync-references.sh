#!/usr/bin/env bash
# frameworks/ is the source; pm-interview-coach/references/ is the copy the skill ships with.
# Run after editing a framework:  ./scripts/sync-references.sh
# CI runs it with --check and fails if the copy has drifted.
set -euo pipefail
cd "$(dirname "$0")/.."
if [ "${1:-}" = "--check" ]; then
  if ! diff -r frameworks pm-interview-coach/references; then
    echo "pm-interview-coach/references/ differs from frameworks/. Run ./scripts/sync-references.sh and commit." >&2
    exit 1
  fi
  echo "references match frameworks"
  exit 0
fi
rm -rf pm-interview-coach/references
cp -R frameworks pm-interview-coach/references
echo "copied frameworks/ to pm-interview-coach/references/"
