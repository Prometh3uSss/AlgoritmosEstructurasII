def validate_message(message):
    return len(message.strip()) > 0

def validate_repo_exists(repo_name):
    return os.path.exists(f"data/repos/{repo_name}")