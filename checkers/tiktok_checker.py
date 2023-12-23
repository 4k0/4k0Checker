import requests
from rich.console import Console

console = Console()

class TikTokChecker:
    @staticmethod
    def check(webhook, username):
        response = requests.head(f'https://www.tiktok.com/@{username}')
        if response.status_code == 200:
            console.print(f'{username} is Unavailable')
        else:
            console.print(f'{username} is Available')
            requests.post(webhook, data={"content": f"\🌠 New TikTok Username Found `@{username}` \n remember **it can be banned** or **blacklisted.** ;3\n`--------------------------------`"})
