# PAT — Agente Documentador

## Qué es
Agente que mantiene la documentación técnica de los proyectos actualizada automáticamente. Explora el código fuente, extrae estructura y símbolos (clases, funciones, argumentos) y genera documentación Markdown.

## Cómo se ejecuta
- **Automáticamente** via hook de Claude Code (`Stop`): cada vez que Claude Code termina de responder, PAT revisa los proyectos registrados y documenta los que tengan cambios en código.
- **Manualmente**: `.venv/bin/python3 documentar.py <ruta-proyecto>`

## Proyectos que vigila
Definidos en `proyectos.yaml`:
- agente-documentador (él mismo)
- Reviews amazon
- agente-ux (PACO)
- funidelia-product-hub
- proyecto-licencias

## Características clave
- Secciones `<!-- PROTEGIDO inicio -->...<!-- PROTEGIDO fin -->` nunca se sobrescriben
- Confirmación antes de sobrescribir (`--force` para saltarla)
- `--deshacer` revierte la última ejecución usando CAMBIOS.md
- `--registrar <ruta>` / `--desregistrar <ruta>` / `--listar` para gestionar proyectos

## Repo
larrazc-cloud/funidelia-agentes-documentador

## Stack
Python 3.14, click, rich, Jinja2, GitPython, PyYAML. Venv en `.venv/`.
