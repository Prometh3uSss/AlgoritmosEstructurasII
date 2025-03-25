from hashlib import sha1
from datetime import datetime

class Commit:
    def __init__(self, message, author, parent, files, branch_name):
        self.message = message
        self.author = author
        self.timestamp = datetime.now().isoformat()
        self.parent = parent  # ID del commit padre (None si es el primero)
        self.files = files  # Lista de archivos modificados
        self.branch_name = branch_name
        self.commit_id = self._generate_sha1()

    def _generate_sha1(self):
        data = f"{self.timestamp}{self.message}{self.author}".encode()
        return sha1(data).hexdigest()

    def to_json(self):
        return {
            "commit_id": self.commit_id,
            "message": self.message,
            "author": self.author,
            "timestamp": self.timestamp,
            "parent": self.parent,
            "files": self.files,
            "branch_name": self.branch_name
        }

    @classmethod
    def from_json(cls, data):
        return cls(
            message=data["message"],
            author=data["author"],
            parent=data["parent"],
            files=data["files"],
            branch_name=data["branch_name"]
        )