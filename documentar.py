#!/usr/bin/env python3
"""Agente Documentador - Punto de entrada principal.

Explora un proyecto, analiza su estructura y genera documentacion automatica.
"""

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from core.explorador import Explorador
from core.orquestador import Orquestador
from core.git_manager import GitManager
from core.changelog import Changelog
from core import registro

console = Console()


@click.command()
@click.argument("ruta_proyecto", type=click.Path(exists=True), required=False)
@click.option("--output", "-o", default="docs", help="Carpeta de salida para la documentacion.")
@click.option("--formato", "-f", type=click.Choice(["markdown", "html"]), default="markdown", help="Formato de salida.")
@click.option("--incluir-git", is_flag=True, default=False, help="Incluir historial git en la documentacion.")
@click.option("--force", is_flag=True, default=False, help="Sobrescribir sin pedir confirmacion (respeta secciones PROTEGIDO).")
@click.option("--deshacer", is_flag=True, default=False, help="Revierte la ultima ejecucion usando CAMBIOS.md.")
@click.option("--registrar", is_flag=True, default=False, help="Registra el proyecto para auto-documentacion.")
@click.option("--desregistrar", is_flag=True, default=False, help="Elimina el proyecto del registro.")
@click.option("--listar", is_flag=True, default=False, help="Muestra los proyectos registrados.")
@click.option("--verbose", "-v", is_flag=True, default=False, help="Mostrar informacion detallada.")
def main(ruta_proyecto, output, formato, incluir_git, force, deshacer,
         registrar, desregistrar, listar, verbose):
    """Genera documentacion automatica para el proyecto en RUTA_PROYECTO."""

    # --- Modo listar ---
    if listar:
        proyectos = registro.listar()
        if not proyectos:
            console.print("[dim]No hay proyectos registrados.[/dim]")
            return
        tabla = Table(title="Proyectos registrados")
        tabla.add_column("Proyecto", style="bold")
        tabla.add_column("Ruta")
        tabla.add_column("Output")
        tabla.add_column("Git")
        for p in proyectos:
            from pathlib import Path
            nombre = Path(p["ruta"]).name
            tabla.add_row(nombre, p["ruta"], p.get("output", "docs"), str(p.get("git", True)))
        console.print(tabla)
        return

    # --- Modo registrar ---
    if registrar:
        if not ruta_proyecto:
            console.print("[red]Debes indicar la ruta del proyecto.[/red]")
            return
        if registro.registrar(ruta_proyecto, output=output, git=incluir_git):
            from pathlib import Path
            console.print(f"[green]Registrado:[/green] {Path(ruta_proyecto).resolve()}")
        else:
            console.print("[yellow]Ya estaba registrado.[/yellow]")
        return

    # --- Modo desregistrar ---
    if desregistrar:
        if not ruta_proyecto:
            console.print("[red]Debes indicar la ruta del proyecto.[/red]")
            return
        if registro.desregistrar(ruta_proyecto):
            console.print(f"[green]Desregistrado.[/green]")
        else:
            console.print("[yellow]No estaba registrado.[/yellow]")
        return

    # --- De aqui en adelante se necesita ruta_proyecto ---
    if not ruta_proyecto:
        console.print("[red]Debes indicar la ruta del proyecto.[/red]")
        console.print("Uso: documentar.py [OPCIONES] RUTA_PROYECTO")
        return

    # --- Modo deshacer ---
    if deshacer:
        from pathlib import Path
        output_dir = Path(ruta_proyecto).resolve() / output
        console.print(Panel.fit(
            "[bold red]Agente Documentador �� Deshacer[/bold red]\n"
            "Revirtiendo ultima ejecucion",
            border_style="red",
        ))
        resultado = Changelog.deshacer(output_dir)
        if "error" in resultado:
            console.print(f"\n[red]{resultado['error']}[/red]")
            return
        console.print(f"\n[bold]Ejecucion revertida:[/bold] {resultado['fecha_revertida']}")
        if resultado["restaurados"]:
            console.print(f"\n  [green]Restaurados ({len(resultado['restaurados'])}):[/green]")
            for f in resultado["restaurados"]:
                console.print(f"    <- {f}")
        if resultado["eliminados"]:
            console.print(f"\n  [yellow]Eliminados ({len(resultado['eliminados'])}):[/yellow]")
            for f in resultado["eliminados"]:
                console.print(f"    x {f}")
        if resultado["sin_cambio"]:
            console.print(f"\n  [dim]Sin cambio: {len(resultado['sin_cambio'])} ficheros[/dim]")
        console.print("\n[bold green]Reversion completada.[/bold green]")
        return

    # --- Modo normal: documentar ---
    console.print(Panel.fit(
        "[bold blue]Agente Documentador[/bold blue]\n"
        "Generador automatico de documentacion",
        border_style="blue",
    ))

    # 1. Explorar
    console.print("\n[bold]1/4 Explorando proyecto...[/bold]")
    explorador = Explorador(ruta_proyecto, verbose=verbose)
    estructura = explorador.explorar()
    console.print(f"  Encontrados: {len(estructura['archivos'])} archivos en {len(estructura['directorios'])} directorios")

    # 2. Info git (opcional)
    info_git = None
    if incluir_git:
        console.print("\n[bold]2/4 Analizando historial git...[/bold]")
        git_mgr = GitManager(ruta_proyecto)
        if git_mgr.es_repo_git():
            info_git = git_mgr.obtener_resumen()
            console.print(f"  Commits: {info_git['total_commits']}, Contribuidores: {len(info_git['contribuidores'])}")
        else:
            console.print("  [yellow]No es un repositorio git, omitiendo.[/yellow]")
    else:
        console.print("\n[bold]2/4 Git omitido[/bold] (usa --incluir-git para activar)")

    # 3. Planificar: mostrar que ficheros se van a tocar
    console.print("\n[bold]3/4 Planificando escritura...[/bold]")
    orquestador = Orquestador(
        estructura=estructura,
        info_git=info_git,
        output_dir=output,
        formato=formato,
        verbose=verbose,
    )
    plan = orquestador.planificar()

    if plan["nuevos"]:
        console.print(f"\n  [green]Ficheros nuevos ({len(plan['nuevos'])}):[/green]")
        for f in plan["nuevos"]:
            console.print(f"    + {f}")
    if plan["sobrescribir"]:
        console.print(f"\n  [yellow]Ficheros a sobrescribir ({len(plan['sobrescribir'])}):[/yellow]")
        for f in plan["sobrescribir"]:
            console.print(f"    ~ {f}")
    if plan["protegidos"]:
        console.print(f"\n  [red]Secciones PROTEGIDO detectadas (se preservaran):[/red]")
        for f in plan["protegidos"]:
            console.print(f"    ! {f}")

    if not plan["nuevos"] and not plan["sobrescribir"]:
        console.print("\n  [dim]No hay ficheros que generar.[/dim]")
        return

    # Pedir confirmacion si hay ficheros a sobrescribir y no se uso --force
    if plan["sobrescribir"] and not force:
        if not click.confirm("\nSe sobrescribiran ficheros existentes (las secciones PROTEGIDO se preservan). Continuar?"):
            console.print("[yellow]Operacion cancelada.[/yellow]")
            return

    # 4. Generar documentacion
    console.print("\n[bold]4/4 Generando documentacion...[/bold]")
    resultado = orquestador.generar()

    console.print(f"\n[bold green]Documentacion generada en: {resultado['output_dir']}[/bold green]")
    console.print(f"  Archivos creados: {resultado['archivos_creados']}")
    console.print(f"  Secciones protegidas preservadas: {resultado['secciones_preservadas']}")


if __name__ == "__main__":
    main()
