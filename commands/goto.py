import os
from typing import List
from .base_cmd import Command
from colorama import Fore, Style

class GotoCommand(Command):
    def run(self, args: List[str]) -> None:
        if len(args) != 1:
            print(f"{Fore.RED}Usage: goto <path>{Style.RESET_ALL}")
            return
        try:
            os.chdir(args[0])
            print(f"{Fore.GREEN}Changed directory to {Fore.CYAN}{args[0]}{Style.RESET_ALL}")
        except FileNotFoundError:
            print(f"{Fore.RED}Directory {Fore.CYAN}{args[0]}{Fore.RED} not found{Style.RESET_ALL}")
        except PermissionError:
            print(f"{Fore.RED}Permission denied for directory {Fore.CYAN}{args[0]}{Style.RESET_ALL}")

    def get_info(self):
        return "goto", "Change the current directory to the specified path."
