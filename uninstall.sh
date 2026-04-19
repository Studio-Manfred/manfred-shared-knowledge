#!/bin/bash
set -euo pipefail

# Manfred Shared Knowledge — Claude Code Uninstaller
# Removes files installed by install.sh
# Use --yes to skip confirmation prompts

CLAUDE_DIR="${CLAUDE_HOME:-$HOME/.claude}"
ASSUME_YES=false
REMOVED=0

SKILLS=(
  a11y-design a11y-dev a11y-qa
  brief-prd
  deploy
  linkedin-reflect linkedin-show-and-tell linkedin-teach
  markitdown-convert
  meeting-summary
  transcript-anonymizer
)

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
  "$CLAUDE_DIR/shared/DESIGN.md"
  "$CLAUDE_DIR/shared/design-principles.md"
)

echo "This will remove:"
for f in "${FILES_TO_REMOVE[@]}"; do
  if [ -f "$f" ]; then
    echo "  - $f"
  fi
done
for name in "${SKILLS[@]}"; do
  if [ -d "$CLAUDE_DIR/skills/$name" ]; then
    echo "  - $CLAUDE_DIR/skills/$name/"
  fi
done
echo ""

if [ "$ASSUME_YES" = false ]; then
  if [ ! -t 0 ]; then
    echo "Error: stdin is not a terminal (piped execution detected)."
    echo "Re-run with --yes to skip the confirmation prompt:"
    echo "  curl -fsSL https://raw.githubusercontent.com/jens-wedin/manfred-shared-knowledge/main/uninstall.sh | bash -s -- --yes"
    exit 1
  fi
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

for name in "${SKILLS[@]}"; do
  if [ -d "$CLAUDE_DIR/skills/$name" ]; then
    rm -rf "$CLAUDE_DIR/skills/$name"
    echo "  🗑  removed $CLAUDE_DIR/skills/$name/"
    REMOVED=$((REMOVED + 1))
  fi
done

# Clean up empty shared/ dir if nothing else is in it
if [ -d "$CLAUDE_DIR/shared" ] && [ -z "$(ls -A "$CLAUDE_DIR/shared")" ]; then
  rmdir "$CLAUDE_DIR/shared"
  echo "  🗑  removed empty $CLAUDE_DIR/shared/"
fi

# Clean up empty skills/ dir if nothing else is in it
if [ -d "$CLAUDE_DIR/skills" ] && [ -z "$(ls -A "$CLAUDE_DIR/skills")" ]; then
  rmdir "$CLAUDE_DIR/skills"
  echo "  🗑  removed empty $CLAUDE_DIR/skills/"
fi

echo ""
echo "────────────────────────────────────────────────"
echo "  Removed: $REMOVED file(s)"
echo "────────────────────────────────────────────────"
echo ""
echo "To remove the plugin marketplace, run inside Claude Code:"
echo "  /plugin marketplace remove manfred"
echo ""
