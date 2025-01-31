from commit import Commit
from rama import Rama
from archivo import Archivo

class Repositorio:
    def __init__(self):
        self.ramas = {}
        self.rama_actual = None
        self.historial = []

    def crear_rama(self, nombre):
        # Validar que el nombre de la rama no esté vacío
        if not nombre or not isinstance(nombre, str):
            print("El nombre de la rama no puede estar vacío o no ser una cadena.")
            return
        if nombre in self.ramas:
            print(f"La rama '{nombre}' ya existe.")
            return
        self.ramas[nombre] = Rama(nombre)
        print(f"Rama '{nombre}' creada.")

    def cambiar_rama(self, nombre):
        # Validar que el nombre de la rama no esté vacío
        if not nombre or not isinstance(nombre, str):
            print("El nombre de la rama no puede estar vacío o no ser una cadena.")
            return
        if nombre not in self.ramas:
            print(f"La rama '{nombre}' no existe.")
            return
        self.rama_actual = self.ramas[nombre]
        print(f"Cambiado a la rama '{nombre}'.")

    def hacer_commit(self, mensaje):
        # Validar que el mensaje no esté vacío
        if not mensaje or not isinstance(mensaje, str):
            print("El mensaje del commit no puede estar vacío o no ser una cadena.")
            return
        if self.rama_actual is None:
            print("No hay ninguna rama seleccionada.")
            return
        archivos = self.rama_actual.commit_actual.archivos if self.rama_actual.commit_actual else []
        nuevo_commit = Commit(mensaje, archivos, self.rama_actual.commit_actual)
        self.rama_actual.commit_actual = nuevo_commit
        self.historial.append(nuevo_commit)
        print(f"Commit realizado: {mensaje}")

    def merge(self, nombre_rama):
        # Validar que el nombre de la rama no esté vacío
        if not nombre_rama or not isinstance(nombre_rama, str):
            print("El nombre de la rama no puede estar vacío o no ser una cadena.")
            return
        if nombre_rama not in self.ramas:
            print(f"La rama '{nombre_rama}' no existe.")
            return
        rama_a_mergear = self.ramas[nombre_rama]
        if rama_a_mergear.commit_actual is None:
            print(f"La rama '{nombre_rama}' no tiene commits para fusionar.")
            return
        self.rama_actual.commit_actual = rama_a_mergear.commit_actual
        print(f"Rama '{nombre_rama}' fusionada en '{self.rama_actual.nombre}'.")

    def mostrar_historial(self):
        if not self.historial:
            print("No hay historial de commits.")
            return
        for commit in self.historial:
            print(commit)