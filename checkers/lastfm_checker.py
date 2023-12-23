import requests
from rich.console import Console

console = Console()

class LastFMChecker:
    @staticmethod
    def check(webhook, username):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

        response = requests.get(f'https://www.last.fm/user/{username}', headers=headers)

        if response.status_code == 404:
            console.print(f'Last.fm Username {username} is Available')
            requests.post(webhook, data={"content": f"\🎵 New Last.fm Username Found `{username}` \n`--------------------------------`"})
        elif response.status_code == 200:
            console.print(f'Last.fm Username {username} is Unavailable')
        else:
            console.print(f"Something went wrong while checking Last.fm username {username}")
