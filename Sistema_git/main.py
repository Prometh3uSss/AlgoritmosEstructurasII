import argparse
import os
from models.repository import Repository
from commands.init import InitCommand
from commands.add import AddCommand
from commands.commit import CommitCommand
from utils.file_handler import load_json, save_json, load_current_repo

def main():
    parser = argparse.ArgumentParser(description="Sistema Git Simulado")
    subparsers = parser.add_subparsers(dest="command")

    # git init <repo_name>
    init_parser = subparsers.add_parser("init")
    init_parser.add_argument("repo_name")

    # git add <file1> <file2>...
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("filenames", nargs="+")

    # git commit -m "mensaje"
    commit_parser = subparsers.add_parser("commit")
    commit_parser.add_argument("-m", "--message", required=True)

    args = parser.parse_args()

    if args.command == "init":
        cmd = InitCommand(args.repo_name)
        result = cmd.execute()
        
        # Guardar repositorio como activo
        with open("data/current_repo.txt", "w") as f:
            f.write(args.repo_name)
            
        print(result)

    elif args.command in ["add", "commit"]:
        try:
            # Cargar repositorio activo
            repo_name = ""
            with open("data/current_repo.txt", "r") as f:
                repo_name = f.read().strip()
            
            repo_data = load_json(f"data/repos/{repo_name}/repo.json")
            if not repo_data:
                raise FileNotFoundError("Repositorio no encontrado")
            
            # Reconstruir objeto Repository
            repo = Repository(repo_name)
            repo.current_branch = repo_data["current_branch"]
            repo.commits = [Commit.from_json(c) for c in repo_data["commits"]]
            
            if args.command == "add":
                cmd = AddCommand(repo, args.filenames)
                result = cmd.execute()
                
            elif args.command == "commit":
                cmd = CommitCommand(repo, args.message)
                result = cmd.execute()
                
            # Guardar cambios
            save_json(f"data/repos/{repo_name}/repo.json", {
                "name": repo.name,
                "current_branch": repo.current_branch,
                "commits": [c.to_json() for c in repo.commits]
            })
            
            print(result)

        except FileNotFoundError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error inesperado: {str(e)}")

if __name__ == "__main__":
    # Crear directorio data si no existe
    os.makedirs("data/repos", exist_ok=True)
    main()