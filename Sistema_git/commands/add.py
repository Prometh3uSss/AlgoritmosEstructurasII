from utils.sha1_generator import generate_sha1_checksum

class AddCommand:
    def __init__(self, repo, filenames):
        self.repo = repo
        self.filenames = filenames

    def execute(self):
        for filename in self.filenames:
            checksum = generate_sha1_checksum(filename)
            self.repo.staging_area.add_file(filename, "A", checksum)
        return f"Archivos {self.filenames} añadidos al staging."