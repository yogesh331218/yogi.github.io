import os
from github import Github

#website to upload files to github repository in python 
def upload_file_to_github(repo_name, file_path, commit_message, branch="main"):
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError("GITHUB_TOKEN environment variable not set")

    g = Github(token)
    repo = g.get_user().get_repo(repo_name)

    with open(file_path, "r") as file:
        content = file.read()

    repo.create_file(file_path, commit_message, content, branch=branch)
    print(f"File {file_path} uploaded to {repo_name} on branch {branch}")

# Example usage
upload_file_to_github("yogi.github.io", "/workspaces/yogi.github.io/second.py", "Initial commit")
