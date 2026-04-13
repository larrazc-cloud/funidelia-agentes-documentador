#!/bin/bash
# Auto-documentación horaria: solo ejecuta si hubo cambios en código fuente.

DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR" || exit 1

VENV="$DIR/.venv/bin/python3"

# Comprobar si hay cambios en ficheros de codigo (excluyendo docs/)
CAMBIOS=$(git diff HEAD --name-only -- . ':!docs/' ':!*.md')

if [ -z "$CAMBIOS" ]; then
    exit 0
fi

# Ejecutar auto-documentación
$VENV "$DIR/documentar.py" --force --incluir-git .

# Commitear y subir solo si docs/ cambió
git add docs/
if ! git diff --cached --quiet; then
    git commit -m "docs: auto-documentacion horaria"
    git push
fi
