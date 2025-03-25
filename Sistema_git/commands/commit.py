from models.commit import Commit

class CommitCommand:
    def __init__(self, repo, message):
        self.repo = repo
        self.message = message

    def execute(self):
        if not self.repo.staging_area.get_files():
            raise ValueError("No hay archivos en staging para commitear.")
        
        latest_commit = self.repo.commits[-1].commit_id if self.repo.commits else None
        new_commit = Commit(
            message=self.message,
            author="user@example.com",
            parent=latest_commit,
            files=self.repo.staging_area.get_files(),
            branch_name=self.repo.current_branch
        )
        self.repo.commits.append(new_commit)
        self.repo.staging_area.clear()
        self.repo._save_repo()
        return f"Commit '{new_commit.commit_id[:6]}' creado."