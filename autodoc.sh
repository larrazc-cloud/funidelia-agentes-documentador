#!/bin/bash
# Auto-documentacion horaria: recorre todos los proyectos registrados
# y documenta solo los que tengan cambios en codigo fuente.

DIR="$(cd "$(dirname "$0")" && pwd)"
VENV="$DIR/.venv/bin/python3"
REGISTRO="$DIR/proyectos.yaml"

if [ ! -f "$REGISTRO" ]; then
    echo "$(date): No existe proyectos.yaml"
    exit 0
fi

# Leer rutas del registro (lineas que empiezan con "- ruta:")
grep '^\- ruta:\|^  ruta:' "$REGISTRO" | sed 's/.*ruta: *//' | while read -r RUTA; do
    if [ ! -d "$RUTA" ]; then
        echo "$(date): SKIP $RUTA (no existe)"
        continue
    fi

    cd "$RUTA" || continue

    # Solo actuar si es repo git y hay cambios en codigo (excluyendo docs/)
    if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
        echo "$(date): SKIP $RUTA (no es repo git)"
        continue
    fi

    CAMBIOS=$(git diff HEAD --name-only -- . ':!docs/' ':!*.md' 2>/dev/null)
    if [ -z "$CAMBIOS" ]; then
        echo "$(date): SKIP $RUTA (sin cambios)"
        continue
    fi

    echo "$(date): DOCUMENTANDO $RUTA"

    # Leer opciones del proyecto desde el yaml
    INCLUIR_GIT=""
    OUTPUT="docs"
    # Buscar la linea de git para este proyecto
    BLOQUE=$(awk "/ruta: ${RUTA//\//\\/}/{found=1} found{print; if(/^[^ ]/ && !/ruta:/) exit}" "$REGISTRO")
    if echo "$BLOQUE" | grep -q "git: true"; then
        INCLUIR_GIT="--incluir-git"
    fi
    OUT_LINE=$(echo "$BLOQUE" | grep "output:" | head -1 | sed 's/.*output: *//')
    if [ -n "$OUT_LINE" ]; then
        OUTPUT="$OUT_LINE"
    fi

    "$VENV" "$DIR/documentar.py" --force $INCLUIR_GIT -o "$OUTPUT" "$RUTA"

    # Commitear y subir si docs/ cambio
    cd "$RUTA"
    git add "$OUTPUT/"
    if ! git diff --cached --quiet; then
        git commit -m "docs: auto-documentacion horaria"
        git push
    fi
done
