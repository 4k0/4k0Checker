import os
import requests
import random
from rich.console import Console
from checkers.steam_checker import SteamChecker
from checkers.instagram_checker import InstagramChecker
from checkers.github_checker import GitHubChecker
from checkers.lastfm_checker import LastFMChecker
from checkers.tiktok_checker import TikTokChecker
from config import WEBHOOK_URL
import ctypes
import string

class Helper:
    @staticmethod
    def read_file(filename, is_random=False):
        if is_random:
            return []

        accounts = []
        with open(filename, encoding="utf8") as file:
            accounts = [line.rstrip('\n') for line in file]
        return accounts

    @staticmethod
    def generate_random_text(num_characters):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(num_characters))


def set_window_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def show_help():
    console.print("[bold]Available commands:[/bold]")
    console.print("  help - Display this help message")
    console.print("  services - Display available checkers")
    console.print("  file - Scan .txt files in the current folder and choose one for wordlist")
    console.print("  text - Generate random characters for wordlist")
    console.print("  run [NUMERICAL ID] - Run a specific checker")
    console.print("  exit - Exit the program")

def show_services():
    console.print("Available services:")
    console.print("1. [blue]Steam[/blue] Checker")
    console.print("2. [magenta]Instagram[/magenta] Checker")
    console.print("3. GitHub Checker")
    console.print("4. Last[red]FM[/red] Checker")
    console.print("5. T[red]ik[/red]T[cyan]ok[/cyan] Checker")


def choose_file():
    txt_files = [f for f in os.listdir() if f.endswith(".txt")]
    if not txt_files:
        print("No .txt files found in the current folder.")
        return None
    else:
        print("Wordlist files:")
        for i, file_name in enumerate(txt_files, start=1):
            print(f"{i}. {file_name}")

        while True:
            try:
                choice = int(input("Choose a file (enter the number) or press Enter to skip: "))
                if choice == 0:
                    return None
                elif 1 <= choice <= len(txt_files):
                    return txt_files[choice - 1]
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

def run_checker(checker_id, wordlist_filename):
    checkers = {
        "1": SteamChecker(),
        "2": InstagramChecker(),
        "3": GitHubChecker(),
        "4": LastFMChecker(),
        "5": TikTokChecker()
    }
    if checker_id in checkers:
        checker = checkers[checker_id]
        current_service = checker.__class__.__name__
        set_window_title(f"github@4k0's Checker | {current_service}")

        os.system("cls||clear")

        console.print(f"""\n\n
     Steam, Instagram, GitHub & LastFM Checker.
      @4k0           <3                     23/12/23 

                             \n""", style="purple")

        if wordlist_filename or accounts:
            accounts = Helper.read_file(wordlist_filename, is_random=False)
        else:
            print("No wordlist file selected. Using the provided list of accounts or generating random characters.")
            num_characters = int(input("How many characters do you want? "))
            accounts = [Helper.generate_random_text(num_characters) for _ in range(num_characters)]

        random.shuffle(accounts)
        for account in accounts:
            checker.check(WEBHOOK_URL, account)
    else:
        print("Invalid checker ID.")
console = Console()

os.system("cls||clear")

#for the window
set_window_title("github@4k0's Checker")

console.print(f"""\n\n
                           
 Steam, Instagram, GitHub & LastFM Checker.
  @4k0           <3                     23/12/23 

                     \n""", style="purple")

# checks if it exists
if not os.path.isfile("config.py"):
    console.print("Config file not found. Creating a new one.")
    with open("config.py", "w") as config_file:
        config_file.write("WEBHOOK_URL = ''")

from config import WEBHOOK_URL

# configure
if not WEBHOOK_URL:
    WEBHOOK_URL = input("Single Webhook URL: ")
    with open("config.py", "w") as config_file:
        config_file.write(f"WEBHOOK_URL = '{WEBHOOK_URL}'")

while True:
    command = input("Enter command (type 'help' for available commands): ")

    if command.lower() == "help":
        show_help()
    elif command.lower() == "services":
        show_services()
    elif command.lower() == "file":
        wordlist_filename = choose_file()
        if wordlist_filename:
            print(f"Selected wordlist file: {wordlist_filename}")
    elif command.lower() == "text":
        num_characters = int(input("How much characters you want? "))
        accounts = [Helper.generate_random_text(num_characters) for _ in range(num_characters)]
        print(f"Generated random characters for wordlist.")

    elif command.lower().startswith("run"):
        _, checker_id = command.split(" ", 1)
        if 'wordlist_filename' in locals() or 'accounts' in locals():
            run_checker(checker_id, wordlist_filename if 'wordlist_filename' in locals() else accounts)
        else:
            print("Please select a wordlist file using the 'file' command or generate random characters using the 'text' command first.")
    elif command.lower() == "exit":
        break
    else:
        print("Invalid command. Type 'help' for available commands.")
