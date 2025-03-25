class Staging:
    def __init__(self):
        self.files = []  # Pila (LIFO)

    def add_file(self, filename, status, checksum):
        self.files.append({
            "nombre": filename,
            "estado": status,  # 'A', 'M', 'D'
            "checksum": checksum
        })

    def clear(self):
        self.files = []

    def get_files(self):
        return self.files.copy()