from models.commit import Commit

class CommitCommand:
    def __init__(self, repo, message):
        self.repo = repo
        self.message = message

    def execute(self):
        if not self.repo.staging_area.get_files():
            raise ValueError("No hay archivos en staging para commitear.")
        
        # Obtener el último commit ID si existe
        latest_commit = self.repo.commits[-1].commit_id if self.repo.commits else None
        
        # Crear nuevo commit
        new_commit = Commit(
            message=self.message,
            author="user@example.com",
            parent=latest_commit,
            files=self.repo.staging_area.get_files(),
            branch_name=self.repo.current_branch
        )
        
        # Añadir commit a la lista y limpiar staging
        self.repo.commits.append(new_commit)
        self.repo.staging_area.clear()
        
        # Actualizar la rama actual con el último commit
        self.repo.branches[self.repo.current_branch].latest_commit = new_commit.commit_id
        
        # Guardar cambios en el repositorio
        self.repo._save_repo()  #  Guarda todo (commits, branches, staging)
        
        return f" Commit '{new_commit.commit_id[:6]}' creado."