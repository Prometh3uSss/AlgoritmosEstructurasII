class Commit:
    def __init__(self, message, files, parent=None):
        self.message = message
        self.files = files
        self.parent = parent
        self.id = self.generate_id()

    def generate_id(self):
        # Generar un hash SHA-1 (simplificado)
        return hash(self.message)

class Repository:
    def __init__(self):
        self.commits = []
        self.staging_area = []
    
    def git_init(self):
        print("Repositorio creado.")
    
    def git_add(self, file):
        self.staging_area.append(file)
        print(f"Archivo {file} agregado al área de staging.")
    
    def git_commit(self, message):
        if not self.staging_area:
            print("No hay archivos en el área de staging.")
            return
        new_commit = Commit(message, self.staging_area.copy(), self.commits[-1] if self.commits else None)
        self.commits.append(new_commit)
        self.staging_area.clear()
        print(f"Commit creado: {message}")

    def git_status(self):
        print("Estado del repositorio:")
        print(f"Archivos en staging: {self.staging_area}")
        print(f"Commits: {[commit.message for commit in self.commits]}")

class PullRequest:
    def __init__(self, source_branch, target_branch):
        self.source_branch = source_branch
        self.target_branch = target_branch
        self.status = "pendiente"

class PullRequestManager:
    def __init__(self):
        self.pull_requests = []

    def create_pull_request(self, source_branch, target_branch):
        pr = PullRequest(source_branch, target_branch)
        self.pull_requests.append(pr)
        print(f"Pull request creado de {source_branch} a {target_branch}.")

# Ejemplo de uso
repo = Repository()
repo.git_init()
repo.git_add("archivo1.txt")
repo.git_commit("Primer commit")
repo.git_status()

pr_manager = PullRequestManager()
pr_manager.create_pull_request("feature", "main")