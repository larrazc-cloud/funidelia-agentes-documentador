"""Explorador de proyectos - analiza estructura de archivos y codigo fuente."""

import os
import ast
import re
from pathlib import Path

EXTENSIONES_CODIGO = {
    ".py", ".js", ".ts", ".jsx", ".tsx", ".java", ".go", ".rs",
    ".rb", ".php", ".c", ".cpp", ".h", ".cs", ".swift", ".kt",
}

IGNORAR_DIRS = {
    "__pycache__", "node_modules", ".git", ".venv", "venv", "env",
    ".tox", ".mypy_cache", ".pytest_cache", "dist", "build",
    ".next", ".nuxt", "target", "bin", "obj",
}

IGNORAR_ARCHIVOS = {
    ".DS_Store", "Thumbs.db", ".gitkeep",
}


class Explorador:
    """Explora un proyecto y extrae su estructura y metadatos."""

    def __init__(self, ruta: str, verbose: bool = False):
        self.ruta = Path(ruta).resolve()
        self.verbose = verbose

    def explorar(self) -> dict:
        """Devuelve un dict con la estructura completa del proyecto."""
        archivos = []
        directorios = []
        modulos = []

        for root, dirs, files in os.walk(self.ruta):
            # Filtrar directorios ignorados
            dirs[:] = [d for d in dirs if d not in IGNORAR_DIRS]

            rel_root = Path(root).relative_to(self.ruta)
            if str(rel_root) != ".":
                directorios.append(str(rel_root))

            for f in files:
                if f in IGNORAR_ARCHIVOS:
                    continue
                ruta_abs = Path(root) / f
                ruta_rel = ruta_abs.relative_to(self.ruta)
                info = self._analizar_archivo(ruta_abs, ruta_rel)
                archivos.append(info)

                if info.get("tipo") == "python" and info.get("simbolos"):
                    modulos.append(info)

        return {
            "nombre_proyecto": self.ruta.name,
            "ruta": str(self.ruta),
            "archivos": archivos,
            "directorios": sorted(directorios),
            "modulos": modulos,
        }

    def _analizar_archivo(self, ruta_abs: Path, ruta_rel: Path) -> dict:
        """Extrae metadatos de un archivo."""
        ext = ruta_abs.suffix.lower()
        info = {
            "nombre": ruta_abs.name,
            "ruta": str(ruta_rel),
            "extension": ext,
            "tamano": ruta_abs.stat().st_size,
            "tipo": self._clasificar(ext),
        }

        if ext == ".py":
            info["simbolos"] = self._extraer_simbolos_python(ruta_abs)
        elif ext in (".md", ".rst", ".txt"):
            info["descripcion"] = self._extraer_descripcion_texto(ruta_abs)

        return info

    def _clasificar(self, ext: str) -> str:
        if ext in EXTENSIONES_CODIGO:
            return {".py": "python", ".js": "javascript", ".ts": "typescript",
                    ".go": "go", ".rs": "rust", ".java": "java"}.get(ext, "codigo")
        if ext in (".md", ".rst", ".txt"):
            return "documentacion"
        if ext in (".json", ".yaml", ".yml", ".toml", ".ini", ".cfg"):
            return "configuracion"
        return "otro"

    def _extraer_simbolos_python(self, ruta: Path) -> dict:
        """Extrae clases, funciones y docstrings de un archivo Python."""
        try:
            source = ruta.read_text(encoding="utf-8", errors="ignore")
            tree = ast.parse(source)
        except (SyntaxError, ValueError):
            return {}

        simbolos = {"clases": [], "funciones": [], "docstring": None}

        # Docstring del modulo
        docstring = ast.get_docstring(tree)
        if docstring:
            simbolos["docstring"] = docstring.strip().split("\n")[0]

        for nodo in ast.iter_child_nodes(tree):
            if isinstance(nodo, ast.ClassDef):
                cls_info = {
                    "nombre": nodo.name,
                    "docstring": (ast.get_docstring(nodo) or "").split("\n")[0],
                    "metodos": [
                        n.name for n in ast.iter_child_nodes(nodo)
                        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
                        and not n.name.startswith("_")
                    ],
                }
                simbolos["clases"].append(cls_info)

            elif isinstance(nodo, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if nodo.name.startswith("_"):
                    continue
                fn_info = {
                    "nombre": nodo.name,
                    "docstring": (ast.get_docstring(nodo) or "").split("\n")[0],
                    "args": [a.arg for a in nodo.args.args if a.arg != "self"],
                }
                simbolos["funciones"].append(fn_info)

        return simbolos

    def _extraer_descripcion_texto(self, ruta: Path) -> str:
        """Extrae la primera linea no vacia de un archivo de texto."""
        try:
            with open(ruta, encoding="utf-8", errors="ignore") as f:
                for linea in f:
                    linea = linea.strip()
                    if linea and not linea.startswith("#"):
                        return linea[:200]
                    if linea.startswith("# "):
                        return linea[2:].strip()[:200]
        except OSError:
            pass
        return ""
