# Registro de cambios

## Ejecucion: 2026-04-13 11:57:50

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 14
- **Directorios:** 3


## Arbol de directorios

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/agente-documentador/docs/core_changelog.md
- Estado: nuevo

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-13 12:09:31

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 17
- **Directorios:** 3

- **Commits:** 1
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** Agente Documentador v0.1.0 (Carlos, 2026-04-13T11:57:21+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 1 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/agente-documentador/docs/core_registro.md
- Estado: nuevo

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-13 12:37:01

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 21
- **Directorios:** 3


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 108 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`







---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-13 14:09:49

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 23
- **Directorios:** 3

- **Commits:** 4
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 228 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** feat: registro centralizado de proyectos + cron multi-proyecto (Carlos, 2026-04-13T12:09:41+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 4 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:31:38

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 23
- **Directorios:** 3

- **Commits:** 5
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 333 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion horaria (Carlos, 2026-04-13T12:37:01+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 5 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:31:58

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 8
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** auto: cambios de sesión Claude Code (Carlos, 2026-04-13T14:26:38+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 8 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:32:28

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 9
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:31:38+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 9 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:32:58

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 10
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:31:58+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 10 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:33:03

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 11
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:32:28+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 11 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:33:46

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 12
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:32:58+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 12 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:35:08

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 13
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:33:03+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 13 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:38:25

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 14
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:33:46+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 14 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:39:26

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 15
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:35:08+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 15 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:39:45

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 16
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:38:25+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 16 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:40:53

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 17
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:39:26+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 17 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:41:16

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 18
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:39:46+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 18 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:41:57

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 19
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:40:53+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 19 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:42:06

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 20
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:41:17+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 20 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:42:14

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 21
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:41:57+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 21 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:42:55

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 22
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:42:06+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 22 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:42:59

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 23
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:42:14+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 23 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:43:04

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 24
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:42:55+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 24 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:43:12

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 25
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:42:59+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 25 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:44:16

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 26
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:43:04+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 26 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:46:15

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 27
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:43:12+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 27 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:46:15

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 28
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:44:16+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 28 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:46:21

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 29
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:46:15+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 29 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:47:33

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 30
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:46:15+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 30 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:47:57

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 31
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:46:21+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 31 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:49:21

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 32
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:47:33+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 32 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:49:50

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 33
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:47:57+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 33 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:50:57

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 34
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:49:21+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 34 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:52:42

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 35
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:49:50+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 35 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:53:59

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 36
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:50:57+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 36 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:56:00

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 37
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:52:42+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 37 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 11:59:02

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 38
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:53:59+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 38 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 12:00:56

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 39
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:56:00+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 39 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 12:02:40

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 40
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T11:59:02+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 40 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 12:09:15

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 41
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T12:00:56+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 41 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 12:16:41

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 42
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T12:02:40+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 42 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 12:27:40

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 43
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T12:09:15+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 43 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 12:29:57

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 44
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T12:16:41+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 44 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 12:30:46

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 45
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T12:27:40+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 45 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 12:34:23

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 46
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T12:29:57+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 46 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 12:36:31

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 47
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T12:30:46+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 47 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 13:01:02

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 48
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T12:34:23+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 48 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 13:01:41

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 49
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T12:36:31+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 49 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 13:02:25

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 50
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T13:01:02+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 50 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 13:02:49

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 51
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T13:01:41+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 51 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 13:06:07

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 52
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T13:02:25+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 52 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 13:06:45

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 53
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T13:02:49+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 53 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 13:07:47

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 54
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T13:06:07+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 54 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 13:10:41

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 55
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T13:06:45+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 55 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 13:20:46

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 56
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T13:07:47+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 56 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 13:21:22

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 57
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T13:10:41+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 57 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 13:21:42

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 58
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T13:20:46+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 58 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 13:25:03

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 59
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T13:21:22+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 59 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 13:25:28

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 60
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T13:21:42+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 60 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 13:27:03

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 61
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T13:25:03+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 61 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 13:30:00

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 62
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T13:25:28+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 62 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 13:32:37

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 63
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T13:27:03+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 63 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 13:33:22

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 64
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T13:30:00+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 64 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 13:34:40

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 65
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T13:32:37+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 65 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 13:39:11

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 66
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T13:33:22+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 66 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 13:41:00

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 67
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T13:34:40+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 67 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 13:41:31

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 68
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T13:39:11+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 68 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 13:42:08

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 69
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T13:41:00+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 69 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 13:42:42

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 70
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T13:41:31+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 70 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 13:44:05

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 71
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T13:42:08+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 71 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
## Ejecucion: 2026-04-14 13:56:43

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/README.md
- Estado: sobrescrito
```md
# agente-documentador

> Documentacion generada automaticamente por el Agente Documentador.

## Estructura del proyecto

- **Archivos:** 22
- **Directorios:** 3

- **Commits:** 72
- **Rama activa:** `main`


## Arbol de directorios

```
agente-documentador/
├── core/
├── docs/
├── templates/

```


## Configuracion

| Archivo | Tamano |
|---------|--------|
| `proyectos.yaml` | 442 bytes |




## Modulos


### instalar.py

> Instalador del Agente Documentador.


- **Funciones:** `main`


### documentar.py

> Agente Documentador - Punto de entrada principal.


- **Funciones:** `main`


### core/registro.py

> Registro de proyectos para auto-documentacion.


- **Funciones:** `listar`, `registrar`, `desregistrar`


### core/__init__.py

> Core del Agente Documentador.




### core/git_manager.py

> Git Manager - extrae informacion del historial git.

- **Clases:** `GitManager`



### core/changelog.py

> Changelog - registra cada ejecucion y permite deshacer.

- **Clases:** `Changelog`



### core/explorador.py

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.

- **Clases:** `Explorador`



### core/orquestador.py

> Orquestador - coordina la generacion de documentacion.

- **Clases:** `Orquestador`






## Git

**Ultimo commit:** docs: auto-documentacion PAT (Carlos, 2026-04-14T13:42:42+02:00)

### Contribuidores

| Autor | Commits |
|-------|---------|
| Carlos | 72 |


### Ramas

- `main`



---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/instalar.md
- Estado: sobrescrito
```md
# instalar.py

**Ruta:** `instalar.py`

> Instalador del Agente Documentador.




## Funciones


### `main()`






---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/documentar.md
- Estado: sobrescrito
```md
# documentar.py

**Ruta:** `documentar.py`

> Agente Documentador - Punto de entrada principal.




## Funciones


### `main(ruta_proyecto, output, formato, incluir_git, force, deshacer, registrar, desregistrar, listar, verbose)`

Genera documentacion automatica para el proyecto en RUTA_PROYECTO.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_registro.md
- Estado: sobrescrito
```md
# registro.py

**Ruta:** `core/registro.py`

> Registro de proyectos para auto-documentacion.




## Funciones


### `listar()`




### `registrar(ruta, output, git)`

Anade un proyecto al registro. Devuelve False si ya existia.


### `desregistrar(ruta)`

Elimina un proyecto del registro. Devuelve False si no estaba.




---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_git_manager.md
- Estado: sobrescrito
```md
# git_manager.py

**Ruta:** `core/git_manager.py`

> Git Manager - extrae informacion del historial git.


## Clases


### `GitManager`

Gestiona la lectura de informacion git de un proyecto.


**Metodos publicos:**

- `es_repo_git()`
- `obtener_resumen()`
- `obtener_archivos_modificados_recientes()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_changelog.md
- Estado: sobrescrito
```md
# changelog.py

**Ruta:** `core/changelog.py`

> Changelog - registra cada ejecucion y permite deshacer.


## Clases


### `Changelog`

Gestiona el registro de cambios y la reversion.


**Metodos publicos:**

- `registrar_antes()`
- `guardar()`
- `deshacer()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_explorador.md
- Estado: sobrescrito
```md
# explorador.py

**Ruta:** `core/explorador.py`

> Explorador de proyectos - analiza estructura de archivos y codigo fuente.


## Clases


### `Explorador`

Explora un proyecto y extrae su estructura y metadatos.


**Metodos publicos:**

- `explorar()`








---
*Generado con Agente Documentador v0.1.0*

```

### Fichero: /Users/carlos/Desktop/Proyectos de Claude/Funidelia/Agentes/agente-documentador/docs/core_orquestador.md
- Estado: sobrescrito
```md
# orquestador.py

**Ruta:** `core/orquestador.py`

> Orquestador - coordina la generacion de documentacion.


## Clases


### `Orquestador`

Genera documentacion a partir de la estructura explorada.


**Metodos publicos:**

- `planificar()`
- `generar()`








---
*Generado con Agente Documentador v0.1.0*

```

---
