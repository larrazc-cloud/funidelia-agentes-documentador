# PAT — Agente Documentador Automatico

## Que es PAT

PAT es un agente local que mantiene la documentacion tecnica de nuestros proyectos actualizada de forma automatica. Analiza el codigo fuente, extrae la estructura y genera documentacion Markdown sin intervencion manual.

## Que problema resuelve

La documentacion tecnica de los proyectos se queda obsoleta porque nadie la actualiza manualmente. PAT elimina ese problema: cada hora revisa si ha habido cambios en el codigo y, si los hay, regenera la documentacion, hace commit y sube a GitHub.

## Como funciona

1. **Explora** el proyecto: escanea archivos, directorios y detecta el lenguaje
2. **Extrae simbolos** del codigo: clases, funciones, docstrings, argumentos (actualmente Python via AST)
3. **Analiza git** (opcional): commits, contribuidores, ramas, ultimo cambio
4. **Genera documentacion** Markdown usando plantillas Jinja2
5. **Registra cada ejecucion** en un changelog con el contenido anterior de cada fichero

## Protecciones

- **Confirmacion antes de sobrescribir**: si hay ficheros existentes, pide confirmacion interactiva (saltable con `--force`)
- **Secciones PROTEGIDO**: cualquier bloque marcado con `<!-- PROTEGIDO inicio -->` ... `<!-- PROTEGIDO fin -->` nunca se sobrescribe, ni siquiera con `--force`. Ideal para notas manuales del equipo
- **Deshacer**: cada ejecucion queda registrada con el contenido previo. Se puede revertir con `--deshacer`
- **Solo actua si hay cambios**: el hook comprueba si hay cambios en codigo fuente (excluyendo docs/ y *.md) antes de ejecutar

## Registro de proyectos

PAT mantiene un registro centralizado (`proyectos.yaml`) de los proyectos que vigila. Se gestionan con:

```
--registrar <ruta>      Anade un proyecto
--desregistrar <ruta>   Lo elimina
--listar                Muestra los proyectos registrados
```

### Proyectos actualmente registrados

| Proyecto | Ruta |
|----------|------|
| agente-documentador | Funidelia/Agentes/agente-documentador |
| Reviews amazon | Funidelia/Reviews amazon |
| agente-ux (PACO) | Funidelia/Agentes/agente-ux |
| funidelia-product-hub | Funidelia/funidelia-product-hub |
| proyecto-licencias | Funidelia/proyecto-licencias |

## Ejecucion automatica

- **Hook Stop de Claude Code**: se dispara al terminar cada respuesta de Claude (configurado en `~/.claude/settings.json`, ejecuta `pat-hook.sh`)
- **Proceso**: recorre todos los proyectos registrados, comprueba cambios en codigo fuente (excluyendo `docs/` y `*.md`), documenta solo los que han cambiado, commitea y sube a GitHub
- **Coste**: cero. Todo corre en local, no usa APIs externas

## Stack tecnico

- Python 3.14 con entorno virtual
- **click** para el CLI
- **rich** para la interfaz en terminal
- **Jinja2** para plantillas de documentacion
- **GitPython** para analisis de repositorios
- **PyYAML** para el registro de proyectos
- Crontab del sistema para ejecucion periodica

## Documentacion que genera por proyecto

| Fichero | Contenido |
|---------|-----------|
| `docs/README.md` | Vision general: estructura, modulos, configuracion, info git |
| `docs/<modulo>.md` | Detalle por modulo: clases, metodos publicos, funciones, argumentos |
| `docs/CAMBIOS.md` | Historial de ejecuciones con contenido previo (para deshacer) |

## Repo

`larrazc-cloud/funidelia-agentes-documentador` (GitHub)

## Proximos pasos posibles

- Soporte para mas lenguajes (JavaScript/TypeScript, Go)
- Generacion en formato HTML
- Dashboard web con estado de documentacion por proyecto
- Notificaciones cuando un proyecto lleva X dias sin documentar
