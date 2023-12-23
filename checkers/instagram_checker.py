import requests
from rich.console import Console
import checkers.instagram


console = Console()


class InstagramChecker:
    @staticmethod
    def check(webhook, username):
        from checkers.instagram import Instagram
        info = Instagram(username)
        try:
            info.print_info()
            requests.post(webhook, data={"content": f"\📸 Instagram Info for `{username}`\nFollowers: {info['followers']}, Following: {info['following']}, Posts: {info['posts']}\n`--------------------------------`"})
        except Exception as e:
            console.print(f"'{username}' Available, banned, or just an error. ({e})")
            requests.post(webhook, data={"content": f"\📸 Instagram Account `{username}` is either **available** or **banned.** ;3\n`--------------------------------`"})
