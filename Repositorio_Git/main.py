from repositorio import Repositorio

def main():
    # Inicializar el repositorio
    repo = Repositorio()

    # Agregar archivos y hacer commits
    repo.hacer_commit("Initial commit")  # No hay rama seleccionada

    # Crear una nueva rama y trabajar en ella
    repo.crear_rama("main")
    repo.cambiar_rama("main")
    repo.hacer_commit("Initial commit on main")

    # Crear otra rama
    repo.crear_rama("develop")
    repo.cambiar_rama("develop")
    repo.hacer_commit("Added new feature")

    # Cambiar a la rama principal y hacer commit
    repo.cambiar_rama("main")
    repo.hacer_commit("Merged develop into main")

    # Mostrar el historial de commits
    repo.mostrar_historial()

if __name__ == "__main__":
    main()