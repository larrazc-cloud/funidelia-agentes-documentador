"""Orquestador - coordina la generacion de documentacion."""

import re
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from core.changelog import Changelog


TEMPLATES_DIR = Path(__file__).resolve().parent.parent / "templates"

# Patron para detectar bloques PROTEGIDO en markdown:
#   <!-- PROTEGIDO inicio -->
#   contenido que nunca se toca
#   <!-- PROTEGIDO fin -->
RE_BLOQUE_PROTEGIDO = re.compile(
    r"(<!--\s*PROTEGIDO\s+inicio\s*-->.*?<!--\s*PROTEGIDO\s+fin\s*-->)",
    re.DOTALL,
)


class Orquestador:
    """Genera documentacion a partir de la estructura explorada."""

    def __init__(self, estructura: dict, info_git: dict | None = None,
                 output_dir: str = "docs", formato: str = "markdown",
                 verbose: bool = False):
        self.estructura = estructura
        self.info_git = info_git
        self.output_dir = Path(estructura["ruta"]) / output_dir
        self.formato = formato
        self.verbose = verbose
        self.env = Environment(
            loader=FileSystemLoader(str(TEMPLATES_DIR)),
            keep_trailing_newline=True,
        )
        self._rutas_salida: list[Path] = []

    # ------------------------------------------------------------------
    # Planificacion
    # ------------------------------------------------------------------

    def planificar(self) -> dict:
        """Calcula que ficheros se crearan/sobrescribiran sin tocar disco.

        Devuelve:
            {
                "nuevos": [str],        # ficheros que no existen aun
                "sobrescribir": [str],   # ficheros que ya existen y se reescribiran
                "protegidos": [str],     # ficheros existentes con secciones PROTEGIDO
            }
        """
        self._rutas_salida = self._calcular_rutas()

        nuevos = []
        sobrescribir = []
        protegidos = []

        for ruta in self._rutas_salida:
            if ruta.exists():
                sobrescribir.append(str(ruta))
                contenido = ruta.read_text(encoding="utf-8", errors="ignore")
                if RE_BLOQUE_PROTEGIDO.search(contenido):
                    protegidos.append(str(ruta))
            else:
                nuevos.append(str(ruta))

        return {
            "nuevos": nuevos,
            "sobrescribir": sobrescribir,
            "protegidos": protegidos,
        }

    def _calcular_rutas(self) -> list[Path]:
        """Devuelve la lista de paths que generar() escribiria."""
        rutas = [self.output_dir / "README.md"]
        for modulo in self.estructura.get("modulos", []):
            if modulo.get("simbolos") and (
                modulo["simbolos"].get("clases") or modulo["simbolos"].get("funciones")
            ):
                nombre = modulo["ruta"].replace("/", "_").replace(".py", ".md")
                rutas.append(self.output_dir / nombre)
        return rutas

    # ------------------------------------------------------------------
    # Generacion
    # ------------------------------------------------------------------

    def generar(self) -> dict:
        """Genera toda la documentacion y devuelve estadisticas."""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        changelog = Changelog(self.output_dir)
        archivos_creados = 0
        secciones_preservadas = 0

        # README principal
        salida_readme = self.output_dir / "README.md"
        changelog.registrar_antes(salida_readme)
        creado, preservadas = self._generar_readme()
        archivos_creados += creado
        secciones_preservadas += preservadas

        # Documentacion por modulo
        for modulo in self.estructura.get("modulos", []):
            if modulo.get("simbolos") and (
                modulo["simbolos"].get("clases") or modulo["simbolos"].get("funciones")
            ):
                nombre = modulo["ruta"].replace("/", "_").replace(".py", ".md")
                salida_mod = self.output_dir / nombre
                changelog.registrar_antes(salida_mod)
                creado, preservadas = self._generar_modulo(modulo)
                archivos_creados += creado
                secciones_preservadas += preservadas

        changelog.guardar()

        return {
            "output_dir": str(self.output_dir),
            "archivos_creados": archivos_creados,
            "secciones_preservadas": secciones_preservadas,
        }

    def _generar_readme(self) -> tuple[int, int]:
        """Genera el README principal del proyecto."""
        template = self.env.get_template("README.md.j2")

        por_tipo = {}
        for arch in self.estructura["archivos"]:
            tipo = arch.get("tipo", "otro")
            por_tipo.setdefault(tipo, []).append(arch)

        contenido_nuevo = template.render(
            nombre=self.estructura["nombre_proyecto"],
            ruta=self.estructura["ruta"],
            archivos=self.estructura["archivos"],
            directorios=self.estructura["directorios"],
            modulos=self.estructura["modulos"],
            por_tipo=por_tipo,
            git=self.info_git,
        )

        salida = self.output_dir / "README.md"
        contenido_final, preservadas = self._fusionar_protegido(salida, contenido_nuevo)
        salida.write_text(contenido_final, encoding="utf-8")
        return 1, preservadas

    def _generar_modulo(self, modulo: dict) -> tuple[int, int]:
        """Genera documentacion para un modulo individual."""
        template = self.env.get_template("modulo.md.j2")

        contenido_nuevo = template.render(
            nombre=modulo["nombre"],
            ruta=modulo["ruta"],
            simbolos=modulo["simbolos"],
        )

        nombre_salida = modulo["ruta"].replace("/", "_").replace(".py", ".md")
        salida = self.output_dir / nombre_salida
        contenido_final, preservadas = self._fusionar_protegido(salida, contenido_nuevo)
        salida.write_text(contenido_final, encoding="utf-8")
        return 1, preservadas

    # ------------------------------------------------------------------
    # Proteccion de secciones
    # ------------------------------------------------------------------

    def _fusionar_protegido(self, ruta: Path, contenido_nuevo: str) -> tuple[str, int]:
        """Reinserta las secciones PROTEGIDO del fichero existente en el nuevo contenido.

        Busca bloques <!-- PROTEGIDO inicio --> ... <!-- PROTEGIDO fin --> en el
        fichero viejo. Para cada uno, si el contenido nuevo tiene el mismo marcador
        lo reemplaza con el original. Si no lo tiene, lo agrega al final.

        Devuelve (contenido_fusionado, num_secciones_preservadas).
        """
        if not ruta.exists():
            return contenido_nuevo, 0

        contenido_viejo = ruta.read_text(encoding="utf-8", errors="ignore")
        bloques_viejos = RE_BLOQUE_PROTEGIDO.findall(contenido_viejo)

        if not bloques_viejos:
            return contenido_nuevo, 0

        resultado = contenido_nuevo
        preservadas = 0

        for bloque in bloques_viejos:
            if RE_BLOQUE_PROTEGIDO.search(resultado):
                # El nuevo contenido tiene un marcador PROTEGIDO: reemplazar
                # el primer marcador libre con el bloque original
                resultado = RE_BLOQUE_PROTEGIDO.sub(bloque, resultado, count=1)
            else:
                # No hay marcador en el nuevo: agregar al final
                resultado = resultado.rstrip() + "\n\n" + bloque + "\n"
            preservadas += 1

        return resultado, preservadas
