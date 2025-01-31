class Rama:
    def __init__(self, nombre):
        self.nombre = nombre
        self.commit_actual = None

    def __repr__(self):
        return f"Rama(nombre={self.nombre}, commit_actual={self.commit_actual})"