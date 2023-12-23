import requests
import bs4
from rich.console import Console

console = Console()

class SteamChecker:
    @staticmethod
    def check(webhook, id):
        request = requests.get(f'https://steamcommunity.com/id/{id}')
        lxml = bs4.BeautifulSoup(request.content, 'lxml')
        title = lxml.find('title')
        word_list = title.text.split()
        if word_list[-1] == "Error":
            console.print(f'{id} is Available')
            requests.post(webhook, data={"content": f"\🌠 New Steam ID Found `{id}` \n remember **it can be banned** or **blacklisted.** ;3\n`--------------------------------`"})
        else:
            console.print(f'{id} is Taken')
