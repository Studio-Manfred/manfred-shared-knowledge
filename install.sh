#!/bin/bash
set -euo pipefail

# Manfred Shared Knowledge — Claude Code Installer
# Usage: curl -fsSL https://raw.githubusercontent.com/jens-wedin/manfred-shared-knowledge/main/install.sh | bash
# Use --force to overwrite existing files (creates backups first)

REPO_RAW="https://raw.githubusercontent.com/jens-wedin/manfred-shared-knowledge/main"
CLAUDE_DIR="${CLAUDE_HOME:-$HOME/.claude}"
FORCE=false
INSTALLED=0
SKIPPED=0

# Parse flags
for arg in "$@"; do
  case $arg in
    --force) FORCE=true ;;
  esac
done

echo ""
echo "╔════════════════════════════════════════════════╗"
echo "║  Manfred Shared Knowledge — Claude Code Setup  ║"
echo "╚════════════════════════════════════════════════╝"
echo ""

install_file() {
  local remote_path="$1"
  local local_path="$2"
  local label="$3"

  if [ -f "$local_path" ] && [ "$FORCE" = false ]; then
    echo "  ⏭  $label — already exists, skipping"
    SKIPPED=$((SKIPPED + 1))
    return
  fi

  if [ -f "$local_path" ] && [ "$FORCE" = true ]; then
    local backup
    backup="${local_path}.backup.$(date +%Y%m%d%H%M%S)"
    cp "$local_path" "$backup"
    echo "  📦 $label — backed up to $(basename "$backup")"
  fi

  local dir
  dir=$(dirname "$local_path")
  mkdir -p "$dir"

  if curl -fsSL "$REPO_RAW/$remote_path" -o "$local_path" 2>/dev/null; then
    echo "  ✅ $label"
    INSTALLED=$((INSTALLED + 1))
  else
    echo "  ❌ $label — download failed"
    return 1
  fi
}

echo "Installing to $CLAUDE_DIR ..."
echo ""

echo "📋 Configuration"
install_file "shared/home-claude.md" "$CLAUDE_DIR/CLAUDE.md" "CLAUDE.md (home-level)"
echo ""

echo "📚 Shared References"
install_file "shared/manfred-brand.md" "$CLAUDE_DIR/shared/manfred-brand.md" "Manfred brand guidelines"
echo ""

echo "────────────────────────────────────────────────"
echo "  Installed: $INSTALLED file(s)"
echo "  Skipped:   $SKIPPED file(s) (already exist)"
echo "────────────────────────────────────────────────"
echo ""

if [ $INSTALLED -gt 0 ] || [ $SKIPPED -gt 0 ]; then
  echo "🔌 To install Manfred plugins, run this inside Claude Code:"
  echo "     /plugin marketplace add jens-wedin/manfred-shared-knowledge"
  echo ""
  echo "   Then: /plugin install <name>@manfred"
  echo ""
fi

if [ $SKIPPED -gt 0 ]; then
  echo "To overwrite existing files (with backup), re-run with --force"
  echo ""
fi

echo "📝 For project-level setup, copy the template CLAUDE.md to your repo:"
echo "   curl -fsSL $REPO_RAW/CLAUDE.md -o ./CLAUDE.md"
echo ""
