import os
import requests
from decouple import config

# Loading the GitHub_PAT from .env file
github_pat = config("GITHUB_PAT")

username = "CheyenneMDavid"

# List of repositories to delete
repositories = [
    # "repo1",
    # "repo2",
    # Replace the above with the actual names I wanna delete.
]


# Loop through the repositories and delete them
for repo in repositories:
    url = f"https://api.github.com/repos/{username}/{repo}"
    headers = {"Authorization": f"token {github_pat}"}

    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        print(f"Repository {repo} has been deleted.")
    else:
        print(f"Error deleting repository {repo}. Status code: {response.status_code}")
