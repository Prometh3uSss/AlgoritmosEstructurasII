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
        # Guardar en data/repos/<nombre>/repo.json
        repo_data = {
            "name": self.name,
            "current_branch": self.current_branch,
            "branches": {name: branch.to_json() for name, branch in self.branches.items()},
            "commits": [commit.to_json() for commit in self.commits]
        }
        save_json(f"data/repos/{self.name}/repo.json", repo_data)