#!/bin/bash
# PAT hook — documenta proyectos registrados que tengan cambios.
# Llamado por el hook Stop de Claude Code.

DIR="$(cd "$(dirname "$0")" && pwd)"
VENV="$DIR/.venv/bin/python3"
REGISTRO="$DIR/proyectos.yaml"

[ ! -f "$REGISTRO" ] && exit 0

grep 'ruta:' "$REGISTRO" | sed 's/.*ruta: *//' | while read -r RUTA; do
    [ ! -d "$RUTA" ] && continue
    cd "$RUTA" || continue

    git rev-parse --is-inside-work-tree > /dev/null 2>&1 || continue

    CAMBIOS=$(git diff HEAD --name-only -- . ':!docs/' ':!*.md' 2>/dev/null)
    [ -z "$CAMBIOS" ] && continue

    "$VENV" "$DIR/documentar.py" --force --incluir-git -o docs "$RUTA" 2>/dev/null

    cd "$RUTA"
    git add docs/
    if ! git diff --cached --quiet; then
        git commit -m "docs: auto-documentacion PAT"
        git push 2>/dev/null
    fi
done
