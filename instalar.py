#!/usr/bin/env python3
"""Instalador del Agente Documentador."""

import subprocess
import sys
import os

DEPENDENCIAS = [
    "click",
    "rich",
    "jinja2",
    "gitpython",
]

def main():
    print("=== Instalador del Agente Documentador ===\n")

    base = os.path.dirname(os.path.abspath(__file__))
    venv_dir = os.path.join(base, ".venv")

    # 1. Verificar Python
    version = sys.version_info
    print(f"Python {version.major}.{version.minor}.{version.micro} detectado")
    if version < (3, 8):
        print("ERROR: Se requiere Python 3.8+")
        sys.exit(1)

    # 2. Crear venv si no existe
    if not os.path.exists(venv_dir):
        print(f"\nCreando entorno virtual en {venv_dir}...")
        subprocess.check_call([sys.executable, "-m", "venv", venv_dir])

    # Usar el python del venv para instalar
    if sys.platform == "win32":
        venv_python = os.path.join(venv_dir, "Scripts", "python.exe")
    else:
        venv_python = os.path.join(venv_dir, "bin", "python3")

    # 3. Instalar dependencias en el venv
    print("\nInstalando dependencias...")
    for dep in DEPENDENCIAS:
        print(f"  -> {dep}")
    subprocess.check_call(
        [venv_python, "-m", "pip", "install", "--quiet"] + DEPENDENCIAS
    )

    # 4. Verificar estructura
    archivos_requeridos = [
        "documentar.py",
        "core/__init__.py",
        "core/explorador.py",
        "core/orquestador.py",
        "core/git_manager.py",
        "templates/README.md.j2",
        "templates/modulo.md.j2",
    ]
    faltantes = [f for f in archivos_requeridos if not os.path.exists(os.path.join(base, f))]
    if faltantes:
        print(f"\nADVERTENCIA: Faltan archivos: {faltantes}")
    else:
        print("\nEstructura verificada correctamente.")

    print("\nInstalacion completada.")
    print(f"\nUso:")
    print(f"  source {venv_dir}/bin/activate")
    print(f"  python {os.path.join(base, 'documentar.py')} <ruta-proyecto>")
    print(f"\n  O directamente:")
    print(f"  {venv_dir}/bin/python3 {os.path.join(base, 'documentar.py')} <ruta-proyecto>")


if __name__ == "__main__":
    main()
