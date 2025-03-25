from datetime import datetime
from hashlib import sha1

class Commit:
    def __init__(self, message, author, parent, files, branch_name):
        self.message = message
        self.author = author
        self.timestamp = datetime.now().isoformat()
        self.parent = parent
        self.files = files
        self.branch_name = branch_name
        self.commit_id = self._generate_sha1()

    def _generate_sha1(self):
        # Incluir más datos para mayor unicidad (archivos, timestamp, etc.)
        data = f"{self.timestamp}{self.message}{self.author}{self.parent}{self.branch_name}".encode()
        for file in self.files:
            data += file["nombre"].encode() + file["checksum"].encode()
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