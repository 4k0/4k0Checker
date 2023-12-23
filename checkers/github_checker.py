import requests
from rich.console import Console

console = Console()

class GitHubChecker:
    @staticmethod
    def check(webhook, user):
        ck = requests.get(f"https://github.com/{user}")
        if ck.status_code == 404:
            console.print(f'GitHub Username {user} is Available')
            requests.post(webhook, data={"content": f"\🚀 New GitHub Username Found `{user}` \n`--------------------------------`"})
        elif ck.status_code == 200:
            console.print(f'GitHub Username {user} is Unavailable')
        else:
            console.print(f"Something went wrong while checking GitHub username {user}")
