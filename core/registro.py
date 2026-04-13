"""Registro de proyectos para auto-documentacion."""

from pathlib import Path

import yaml

REGISTRO_PATH = Path(__file__).resolve().parent.parent / "proyectos.yaml"


def _leer() -> dict:
    if not REGISTRO_PATH.exists():
        return {"proyectos": []}
    return yaml.safe_load(REGISTRO_PATH.read_text(encoding="utf-8")) or {"proyectos": []}


def _guardar(data: dict):
    REGISTRO_PATH.write_text(
        yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )


def listar() -> list[dict]:
    return _leer().get("proyectos", [])


def registrar(ruta: str, output: str = "docs", git: bool = True) -> bool:
    """Anade un proyecto al registro. Devuelve False si ya existia."""
    ruta_abs = str(Path(ruta).resolve())
    data = _leer()
    proyectos = data.get("proyectos", [])

    for p in proyectos:
        if str(Path(p["ruta"]).resolve()) == ruta_abs:
            return False

    proyectos.append({"ruta": ruta_abs, "output": output, "git": git})
    data["proyectos"] = proyectos
    _guardar(data)
    return True


def desregistrar(ruta: str) -> bool:
    """Elimina un proyecto del registro. Devuelve False si no estaba."""
    ruta_abs = str(Path(ruta).resolve())
    data = _leer()
    proyectos = data.get("proyectos", [])
    nuevos = [p for p in proyectos if str(Path(p["ruta"]).resolve()) != ruta_abs]

    if len(nuevos) == len(proyectos):
        return False

    data["proyectos"] = nuevos
    _guardar(data)
    return True
