#!/bin/bash
set -euo pipefail

# Manfred Shared Knowledge — Claude Code Uninstaller
# Removes files installed by install.sh
# Use --yes to skip confirmation prompts

CLAUDE_DIR="${CLAUDE_HOME:-$HOME/.claude}"
ASSUME_YES=false
REMOVED=0

for arg in "$@"; do
  case $arg in
    --yes|-y) ASSUME_YES=true ;;
  esac
done

echo ""
echo "╔════════════════════════════════════════════════════╗"
echo "║  Manfred Shared Knowledge — Claude Code Uninstall  ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""

FILES_TO_REMOVE=(
  "$CLAUDE_DIR/CLAUDE.md"
  "$CLAUDE_DIR/shared/manfred-brand.md"
)

echo "This will remove:"
for f in "${FILES_TO_REMOVE[@]}"; do
  if [ -f "$f" ]; then
    echo "  - $f"
  fi
done
echo ""

if [ "$ASSUME_YES" = false ]; then
  read -r -p "Proceed? [y/N] " reply
  case "$reply" in
    y|Y|yes|YES) ;;
    *) echo "Aborted."; exit 0 ;;
  esac
fi

for f in "${FILES_TO_REMOVE[@]}"; do
  if [ -f "$f" ]; then
    rm "$f"
    echo "  🗑  removed $f"
    REMOVED=$((REMOVED + 1))
  fi
done

# Clean up empty shared/ dir if nothing else is in it
if [ -d "$CLAUDE_DIR/shared" ] && [ -z "$(ls -A "$CLAUDE_DIR/shared")" ]; then
  rmdir "$CLAUDE_DIR/shared"
  echo "  🗑  removed empty $CLAUDE_DIR/shared/"
fi

echo ""
echo "────────────────────────────────────────────────"
echo "  Removed: $REMOVED file(s)"
echo "────────────────────────────────────────────────"
echo ""
echo "To remove the plugin marketplace, run inside Claude Code:"
echo "  /plugin marketplace remove manfred"
echo ""
