from models.repository import Repository
from utils.file_handler import create_dir

class InitCommand:
    def __init__(self, repo_name):
        self.repo_name = repo_name

    def execute(self):
        repo_path = f"data/repos/{self.repo_name}"
        if os.path.exists(repo_path):
            raise FileExistsError(f"El repositorio '{self.repo_name}' ya existe.")
        
        create_dir(repo_path)
        repo = Repository(self.repo_name)
        repo._save_repo()  # Guardar repo.json
        return f"Repositorio '{self.repo_name}' creado exitosamente."