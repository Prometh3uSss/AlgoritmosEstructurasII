# models/branch.py
class Branch:
    def __init__(self, name):
        self.name = name
        self.latest_commit = None  # ID del último commit en esta rama

    def to_json(self):
        return {
            "name": self.name,
            "latest_commit": self.latest_commit
        }

    @classmethod
    def from_json(cls, data):
        branch = cls(data["name"])
        branch.latest_commit = data["latest_commit"]
        return branch