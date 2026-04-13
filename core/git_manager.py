"""Git Manager - extrae informacion del historial git."""

from pathlib import Path

try:
    import git
except ImportError:
    git = None


class GitManager:
    """Gestiona la lectura de informacion git de un proyecto."""

    def __init__(self, ruta: str):
        self.ruta = Path(ruta).resolve()
        self._repo = None

    def es_repo_git(self) -> bool:
        """Comprueba si la ruta es un repositorio git."""
        if git is None:
            return False
        try:
            self._repo = git.Repo(self.ruta, search_parent_directories=True)
            return True
        except (git.InvalidGitRepositoryError, git.NoSuchPathError):
            return False

    def obtener_resumen(self) -> dict:
        """Devuelve un resumen del repositorio git."""
        if not self._repo:
            return {}

        commits = list(self._repo.iter_commits(max_count=500))

        contribuidores = {}
        for c in commits:
            autor = c.author.name
            contribuidores[autor] = contribuidores.get(autor, 0) + 1

        # Ramas
        ramas = [r.name for r in self._repo.branches]

        # Ultimo commit
        ultimo = commits[0] if commits else None

        return {
            "total_commits": len(commits),
            "contribuidores": contribuidores,
            "ramas": ramas,
            "rama_activa": str(self._repo.active_branch) if not self._repo.head.is_detached else "HEAD detached",
            "ultimo_commit": {
                "mensaje": ultimo.message.strip().split("\n")[0],
                "autor": ultimo.author.name,
                "fecha": ultimo.committed_datetime.isoformat(),
            } if ultimo else None,
        }

    def obtener_archivos_modificados_recientes(self, max_commits: int = 20) -> list[str]:
        """Devuelve los archivos modificados en los ultimos N commits."""
        if not self._repo:
            return []

        archivos = set()
        for commit in self._repo.iter_commits(max_count=max_commits):
            archivos.update(commit.stats.files.keys())
        return sorted(archivos)
