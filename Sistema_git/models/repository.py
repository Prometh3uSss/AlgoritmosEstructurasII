import os
import json
from datetime import datetime
from .commit import Commit
from .staging import Staging
from .branch import Branch
from utils.file_handler import save_json, load_json

class Repository:
    def __init__(self, name):
        self.name = name
        self.branches = {"main": Branch("main")}  # Rama principal por defecto
        self.current_branch = "main"
        self.staging_area = Staging()
        self.commits = []  # Lista enlazada implícita (cada commit tiene 'parent')

    def create_branch(self, branch_name):
        if branch_name in self.branches:
            raise ValueError(f"La rama '{branch_name}' ya existe.")
        self.branches[branch_name] = Branch(branch_name)
        self._save_repo()

    def switch_branch(self, branch_name):
        if branch_name not in self.branches:
            raise ValueError(f"La rama '{branch_name}' no existe.")
        self.current_branch = branch_name

    def _save_repo(self):
        repo_data = {
            "name": self.name,
            "current_branch": self.current_branch,
            "branches": {name: branch.to_json() for name, branch in self.branches.items()},
            "commits": [commit.to_json() for commit in self.commits],
            "staging_area": self.staging_area.get_files()  # ¡Incluir el staging!
        }
        save_json(f"data/repos/{self.name}/repo.json", repo_data)
    
    @classmethod
    def load(cls, repo_name):
        """Carga un repositorio desde el disco."""
        data = load_json(f"data/repos/{repo_name}/repo.json")
        if not data:
            raise ValueError(f"Repositorio '{repo_name}' no existe.")
        
        repo = cls(data["name"])
        repo.current_branch = data["current_branch"]
        repo.commits = [Commit.from_json(c) for c in data["commits"]]
        repo.branches = {name: Branch.from_json(b) for name, b in data["branches"].items()}
        repo.staging_area.files = data.get("staging_area", [])  # ¡Añade esta línea!
        return repo

    def to_json(self):
        return {
            "name": self.name,
            "current_branch": self.current_branch,
            "commits": [c.to_json() for c in self.commits]
        }

    @classmethod
    def from_json(cls, data):
        repo = cls(data["name"])
        repo.current_branch = data["current_branch"]
        repo.commits = [Commit.from_json(c) for c in data["commits"]]
        return repo