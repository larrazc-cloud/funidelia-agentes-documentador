"""Changelog - registra cada ejecucion y permite deshacer."""

import re
from datetime import datetime
from pathlib import Path

SEPARADOR = "---\n"
RE_ENTRADA = re.compile(
    r"## Ejecucion: (.+?)\n(.*?)(?=## Ejecucion:|\Z)",
    re.DOTALL,
)
RE_FICHERO = re.compile(
    r"### Fichero: (.+?)\n- Estado: (.+?)\n(?:```md\n(.*?)\n```\n)?",
    re.DOTALL,
)


class Changelog:
    """Gestiona el registro de cambios y la reversion."""

    def __init__(self, output_dir: str | Path):
        self.output_dir = Path(output_dir)
        self.ruta = self.output_dir / "CAMBIOS.md"
        self._ficheros: list[dict] = []

    def registrar_antes(self, ruta: Path):
        """Captura el estado previo de un fichero antes de sobrescribirlo."""
        entrada = {"ruta": str(ruta), "estado": "nuevo", "contenido_previo": None}
        if ruta.exists():
            entrada["estado"] = "sobrescrito"
            entrada["contenido_previo"] = ruta.read_text(encoding="utf-8", errors="ignore")
        self._ficheros.append(entrada)

    def guardar(self):
        """Escribe la entrada de esta ejecucion al final de CAMBIOS.md."""
        if not self._ficheros:
            return

        ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        bloque = f"## Ejecucion: {ahora}\n\n"

        for f in self._ficheros:
            bloque += f"### Fichero: {f['ruta']}\n"
            bloque += f"- Estado: {f['estado']}\n"
            if f["contenido_previo"] is not None:
                bloque += f"```md\n{f['contenido_previo']}\n```\n"
            bloque += "\n"

        bloque += SEPARADOR

        # Leer contenido existente o crear cabecera
        if self.ruta.exists():
            contenido = self.ruta.read_text(encoding="utf-8")
        else:
            contenido = "# Registro de cambios\n\n"

        contenido += bloque
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.ruta.write_text(contenido, encoding="utf-8")

    @staticmethod
    def deshacer(output_dir: str | Path) -> dict:
        """Revierte la ultima ejecucion registrada en CAMBIOS.md.

        Devuelve:
            {"restaurados": [str], "eliminados": [str], "sin_cambio": [str]}
        """
        ruta_cambios = Path(output_dir) / "CAMBIOS.md"
        if not ruta_cambios.exists():
            return {"error": "No existe CAMBIOS.md — nada que deshacer."}

        contenido = ruta_cambios.read_text(encoding="utf-8")
        entradas = RE_ENTRADA.findall(contenido)

        if not entradas:
            return {"error": "No hay ejecuciones registradas en CAMBIOS.md."}

        # Tomar la ultima entrada
        ultima_fecha, ultimo_bloque = entradas[-1]
        ficheros = RE_FICHERO.findall(ultimo_bloque)

        restaurados = []
        eliminados = []
        sin_cambio = []

        for ruta_str, estado, contenido_previo in ficheros:
            ruta = Path(ruta_str)
            if estado == "nuevo":
                # Se creo por primera vez: eliminar
                if ruta.exists():
                    ruta.unlink()
                    eliminados.append(ruta_str)
                else:
                    sin_cambio.append(ruta_str)
            elif estado == "sobrescrito" and contenido_previo:
                # Restaurar contenido anterior
                ruta.write_text(contenido_previo, encoding="utf-8")
                restaurados.append(ruta_str)
            else:
                sin_cambio.append(ruta_str)

        # Eliminar la ultima entrada del changelog
        partes = contenido.rsplit(f"## Ejecucion: {ultima_fecha}", maxsplit=1)
        contenido_limpio = partes[0].rstrip() + "\n\n" if len(partes) > 1 else ""
        if contenido_limpio.strip() == "# Registro de cambios":
            contenido_limpio = "# Registro de cambios\n\n"
        ruta_cambios.write_text(contenido_limpio, encoding="utf-8")

        return {
            "fecha_revertida": ultima_fecha,
            "restaurados": restaurados,
            "eliminados": eliminados,
            "sin_cambio": sin_cambio,
        }
