import json
import os

# Funciones existentes
def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def load_json(path):
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return json.load(f)

def load_current_repo():
    try:
        with open("data/current_repo.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

# Función faltante
def create_dir(path):
    """Crea directorios recursivamente si no existen"""
    os.makedirs(path, exist_ok=True)