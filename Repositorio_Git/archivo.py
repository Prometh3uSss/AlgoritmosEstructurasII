class Archivo:
    def __init__(self, nombre, contenido):
        self.nombre = nombre
        self.contenido = contenido

    def __repr__(self):
        return f"Archivo(nombre={self.nombre}, contenido={self.contenido})"