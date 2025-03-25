import argparse
from models.repository import Repository
from commands.init import InitCommand
from commands.add import AddCommand
from commands.commit import CommitCommand
from utils.file_handler import load_json

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
        print(cmd.execute())
    elif args.command == "add":
        repo = load_current_repo()  # Función auxiliar para cargar el repo activo
        cmd = AddCommand(repo, args.filenames)
        print(cmd.execute())
    elif args.command == "commit":
        repo = load_current_repo()
        cmd = CommitCommand(repo, args.message)
        print(cmd.execute())

if __name__ == "__main__":
    main()