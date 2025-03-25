from collections import deque

class PullRequestQueue:
    def __init__(self):
        self.queue = deque()
        self.pr_counter = 1  # Generador de IDs únicos

    def create_pr(self, source_branch, target_branch, title, author):
        pr = {
            "id": self.pr_counter,
            "title": title,
            "author": author,
            "source": source_branch,
            "target": target_branch,
            "status": "pending"
        }
        self.queue.append(pr)
        self.pr_counter += 1
        return pr["id"]

    def approve_pr(self, pr_id):
        for pr in self.queue:
            if pr["id"] == pr_id:
                pr["status"] = "approved"
                return True
        return False

    def get_next_pr(self):
        if self.queue:
            return self.queue.popleft()
        return None