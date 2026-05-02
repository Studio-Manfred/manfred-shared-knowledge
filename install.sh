#!/bin/bash
set -euo pipefail

# Manfred Shared Knowledge — Claude Code Installer
# Usage: curl -fsSL https://raw.githubusercontent.com/Studio-Manfred/manfred-shared-knowledge/main/install.sh | bash
# Use --force to overwrite existing files (creates backups first)
#
# This installs the home-level CLAUDE.md and shared/ reference docs only.
# Skills now ship as plugins via the manfred marketplace — see the final
# message for plugin install instructions.

REPO_RAW="https://raw.githubusercontent.com/Studio-Manfred/manfred-shared-knowledge/main"
CLAUDE_DIR="${CLAUDE_HOME:-$HOME/.claude}"
FORCE=false
INSTALLED=0
SKIPPED=0
FAILED=0

LEGACY_SKILLS=(
  a11y-design a11y-dev a11y-qa
  brief-prd
  deploy release
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

check_legacy_skills() {
  local found=()
  for name in "${LEGACY_SKILLS[@]}"; do
    if [ -d "$CLAUDE_DIR/skills/$name" ]; then
      found+=("$name")
    fi
  done

  if [ ${#found[@]} -gt 0 ]; then
    echo ""
    echo "⚠️  Legacy skill copies detected at $CLAUDE_DIR/skills/:"
    for name in "${found[@]}"; do
      echo "     - $name"
    done
    echo ""
    echo "   These skills are now distributed as plugins. To avoid duplicates,"
    echo "   remove the local copies after installing the matching plugin:"
    echo "     rm -rf $CLAUDE_DIR/skills/<skill-name>"
    echo ""
  fi
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

check_legacy_skills

echo "────────────────────────────────────────────────"
echo "  Installed: $INSTALLED file(s)"
echo "  Skipped:   $SKIPPED file(s) (already exist)"
if [ $FAILED -gt 0 ]; then
  echo "  Failed:    $FAILED file(s)"
fi
echo "────────────────────────────────────────────────"
echo ""

echo "🔌 Skills now ship as plugins. Inside Claude Code, run:"
echo ""
echo "     /plugin marketplace add Studio-Manfred/manfred-shared-knowledge"
echo ""
echo "   Then install only the plugins you need:"
echo "     /plugin install manfred-a11y@manfred       # accessibility"
echo "     /plugin install manfred-writing@manfred    # LinkedIn + meeting summaries"
echo "     /plugin install manfred-product@manfred    # product briefs"
echo "     /plugin install manfred-dev@manfred        # pre-merge QA, deploy, release"
echo "     /plugin install manfred-knowledge@manfred  # vault linting, MD conversion"
echo ""

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
