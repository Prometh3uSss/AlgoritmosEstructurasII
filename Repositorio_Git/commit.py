class Commit:
    def __init__(self, mensaje, archivos, anterior=None):
        self.mensaje = mensaje
        self.archivos = archivos  # Lista de objetos Archivo
        self.anterior = anterior

    def __repr__(self):
        return f"Commit(mensaje={self.mensaje}, archivos={self.archivos})"