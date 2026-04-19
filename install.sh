#!/bin/bash
set -euo pipefail

# Manfred Shared Knowledge — Claude Code Installer
# Usage: curl -fsSL https://raw.githubusercontent.com/jens-wedin/manfred-shared-knowledge/main/install.sh | bash
# Use --force to overwrite existing files (creates backups first)

REPO_RAW="https://raw.githubusercontent.com/jens-wedin/manfred-shared-knowledge/main"
REPO_GIT="${MANFRED_REPO_GIT:-https://github.com/jens-wedin/manfred-shared-knowledge.git}"
CLAUDE_DIR="${CLAUDE_HOME:-$HOME/.claude}"
FORCE=false
INSTALLED=0
SKIPPED=0
FAILED=0

SKILLS=(
  a11y-design a11y-dev a11y-qa
  brief-prd
  deploy
  linkedin-reflect linkedin-show-and-tell linkedin-teach
  markitdown-convert
  meeting-summary
  transcript-anonymizer
)

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
    return 0
  elif [ -f "$local_path" ] && [ "$FORCE" = true ]; then
    local backup
    backup="${local_path}.backup.$(date +%Y%m%d%H%M%S)"
    cp "$local_path" "$backup"
    echo "  📦 $label — backed up to $(basename "$backup")"
  fi

  local dir
  dir=$(dirname "$local_path")
  mkdir -p "$dir"

  local tmp_path="${local_path}.tmp"
  if curl -fsSL "$REPO_RAW/$remote_path" -o "$tmp_path" 2>/dev/null; then
    mv "$tmp_path" "$local_path"
    echo "  ✅ $label"
    INSTALLED=$((INSTALLED + 1))
  else
    rm -f "$tmp_path"
    echo "  ❌ $label — download failed"
    FAILED=$((FAILED + 1))
  fi
}

install_skill_dir() {
  local src="$1"
  local dest="$2"
  local label="$3"

  if [ -d "$dest" ] && [ "$FORCE" = false ]; then
    echo "  ⏭  skill/$label — already exists, skipping"
    SKIPPED=$((SKIPPED + 1))
    return 0
  elif [ -d "$dest" ] && [ "$FORCE" = true ]; then
    local backup
    backup="${dest}.backup.$(date +%Y%m%d%H%M%S)"
    mv "$dest" "$backup"
    echo "  📦 skill/$label — backed up to $(basename "$backup")"
  fi

  mkdir -p "$(dirname "$dest")"
  if cp -R "$src" "$dest"; then
    echo "  ✅ skill/$label"
    INSTALLED=$((INSTALLED + 1))
  else
    echo "  ❌ skill/$label — copy failed"
    FAILED=$((FAILED + 1))
  fi
}

install_skills() {
  if ! command -v git >/dev/null 2>&1; then
    echo "  ❌ skills — git not found. Install git and re-run."
    echo "     On macOS: xcode-select --install"
    echo "     On Debian/Ubuntu: sudo apt-get install git"
    FAILED=$((FAILED + 1))
    return
  fi

  local tmp
  tmp=$(mktemp -d)
  if ! git clone --depth=1 --quiet "$REPO_GIT" "$tmp" 2>/dev/null; then
    echo "  ❌ skills — git clone of $REPO_GIT failed"
    FAILED=$((FAILED + 1))
    rm -rf "$tmp"
    return
  fi

  local name
  for name in "${SKILLS[@]}"; do
    if [ -d "$tmp/skills/$name" ]; then
      install_skill_dir "$tmp/skills/$name" "$CLAUDE_DIR/skills/$name" "$name"
    else
      echo "  ❌ skill/$name — missing from repo clone"
      FAILED=$((FAILED + 1))
    fi
  done

  rm -rf "$tmp"
}

echo "Installing to $CLAUDE_DIR ..."
echo ""

echo "📋 Configuration"
install_file "shared/home-claude.md" "$CLAUDE_DIR/CLAUDE.md" "CLAUDE.md (home-level)"
echo ""

echo "📚 Shared References"
install_file "shared/manfred-brand.md"     "$CLAUDE_DIR/shared/manfred-brand.md"     "Manfred brand guidelines"
install_file "shared/DESIGN.md"            "$CLAUDE_DIR/shared/DESIGN.md"            "Design system spec"
install_file "shared/design-principles.md" "$CLAUDE_DIR/shared/design-principles.md" "Design principles"
echo ""

echo "⚡ Skills"
install_skills
echo ""

echo "────────────────────────────────────────────────"
echo "  Installed: $INSTALLED file(s)"
echo "  Skipped:   $SKIPPED file(s) (already exist)"
if [ $FAILED -gt 0 ]; then
  echo "  Failed:    $FAILED file(s)"
fi
echo "────────────────────────────────────────────────"
echo ""

if [ $INSTALLED -gt 0 ] || [ $SKIPPED -gt 0 ]; then
  echo "🔌 To install Manfred plugins, run this inside Claude Code:"
  echo "     /plugin marketplace add jens-wedin/manfred-shared-knowledge"
  echo ""
  echo "   Then: /plugin install <name>@manfred"
  echo ""
fi

if [ $INSTALLED -gt 0 ]; then
  echo "🧰 Skills live under $CLAUDE_DIR/skills/ — triggered automatically by keywords"
  echo ""
fi

if [ $SKIPPED -gt 0 ]; then
  echo "To overwrite existing files (with backup), re-run with --force"
  echo ""
fi

echo "📝 For project-level setup, copy the template CLAUDE.md to your repo:"
echo "   curl -fsSL $REPO_RAW/CLAUDE.md -o ./CLAUDE.md"
echo ""

if [ $FAILED -gt 0 ]; then
  exit 1
fi
