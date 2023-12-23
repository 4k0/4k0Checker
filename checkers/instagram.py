import requests
import bs4
from rich.console import Console
class Instagram:
    def __init__(self, username):
        self.username = str(username)

    def get_request(self):
        request = requests.get('https://www.instagram.com/' + self.username)
        if request.status_code == 200:
            return request.content
        else:
            raise Exception(f"This username is not used: {self.username}")

    def content_parser(self):
        content = self.get_request()
        source = bs4.BeautifulSoup(content, 'html.parser')
        return source

    def get_info(self):
        source = self.content_parser()
        description = source.find("meta", {"property": "og:description"}).get("content")
        info_list = description.split("-")[0]
        followers = info_list[0:info_list.index("Followers")]
        info_list = info_list.replace(followers + "Followers, ", "")
        following = info_list[0:info_list.index("Following")]
        info_list = info_list.replace(following + "Following, ", "")
        posts = info_list[0:info_list.index("Posts")]
        results = {"followers": followers, "following": following, "posts": posts}
        return results

    def print_info(self):
        info = self.get_info()
        Console.print(f"\n User Name: {self.username}")
        Console.print(f" Followers: {info['followers']}")
        Console.print(f" Following: {info['following']}")
        Console.print(f" Posts: {info['posts']}")
        Console.print("\n -" * 15)