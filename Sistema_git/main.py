import os  # Importación crítica
import argparse
from models.repository import Repository
from models.commit import Commit
from commands.init import InitCommand
from commands.add import AddCommand
from commands.commit import CommitCommand
from utils.file_handler import load_json, save_json, load_current_repo

def main():
    parser = argparse.ArgumentParser(
        description="Sistema Git Simulado",
        epilog="Ejemplo: python main.py init mi_repo"
    )
    subparsers = parser.add_subparsers(
        dest="command",
        title="Comandos",
        help="Comandos disponibles"
    )

    # git init <repo_name>
    init_parser = subparsers.add_parser("init", help="Inicializa un nuevo repositorio")
    init_parser.add_argument("repo_name", type=str, help="Nombre del repositorio")

    # git add <file1> <file2>...
    add_parser = subparsers.add_parser("add", help="Añade archivos al área de staging")
    add_parser.add_argument("filenames", nargs="+", help="Nombres de los archivos")

    # git commit -m "mensaje"
    commit_parser = subparsers.add_parser("commit", help="Crea un nuevo commit")
    commit_parser.add_argument("-m", "--message", required=True, help="Mensaje del commit")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    try:
        if args.command == "init":
            cmd = InitCommand(args.repo_name)
            result = cmd.execute()
            
            # Guardar repositorio como activo
            with open("data/current_repo.txt", "w") as f:
                f.write(args.repo_name)
            print(result)

        elif args.command in ["add", "commit"]:
            repo_name = load_current_repo()
            if not repo_name:
                print("Error: No hay repositorio activo. Ejecuta 'git init' primero.")
                return

            repo_data = load_json(f"data/repos/{repo_name}/repo.json")
            if not repo_data:
                print(f"Error: Repositorio '{repo_name}' no existe.")
                return

            repo = Repository(repo_name)
            repo.current_branch = repo_data.get("current_branch", "main")
            repo.commits = [Commit.from_json(c) for c in repo_data.get("commits", [])]

            if args.command == "add":
                cmd = AddCommand(repo, args.filenames)
                result = cmd.execute()
            elif args.command == "commit":
                cmd = CommitCommand(repo, args.message)
                result = cmd.execute()

            # Guardar cambios
            repo._save_repo()
            print(result)

    except Exception as e:
        print(f"Error crítico: {str(e)}")

if __name__ == "__main__":
    os.makedirs("data/repos", exist_ok=True)  # Aquí se usa 'os'
    main()