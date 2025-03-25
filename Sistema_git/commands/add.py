from utils.sha1_generator import generate_sha1_checksum
import os

class AddCommand:
    def __init__(self, repo, filenames):
        self.repo = repo
        self.filenames = filenames

    def execute(self):
        valid_files = []
        for filename in self.filenames:
            if not os.path.exists(filename):
                print(f" Advertencia: El archivo '{filename}' no existe.")
                continue
            checksum = generate_sha1_checksum(filename)
            self.repo.staging_area.add_file(filename, "A", checksum)
            valid_files.append(filename)
        
        if not valid_files:
            raise ValueError("No se añadieron archivos: verifica que existan.")
        
        return f" Archivos {valid_files} añadidos al staging."