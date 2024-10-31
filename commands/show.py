import os
from .base_cmd import Command
from typing import List
from colorama import Fore, Style

class ShowCommand(Command):
    def run(self, args: List[str]) -> None:
        target_dir = "."
        if len(args):
            target_dir = args[0]
        try:
            contents = os.listdir(target_dir)
            print(f"{Fore.YELLOW}Contents :{Style.RESET_ALL}")
            if contents:
                for item in contents:
                    item_path = os.path.join(target_dir, item)
                    if os.path.isdir(item_path):
                        print(f"*{Fore.BLUE}{item}{Style.RESET_ALL}") #Indicates directory
                    else:
                         print(f"~{Fore.GREEN}{item}{Style.RESET_ALL}") #Indicates file

            else:
               print(f"{Fore.YELLOW}Directory is empty{Style.RESET_ALL}")
        except NotADirectoryError:
            print(f"{Fore.RED}Not a directory{Style.RESET_ALL}")
        except FileNotFoundError:
            print(f"{Fore.RED}Directory not found{Style.RESET_ALL}")
        except PermissionError:
            print(f"{Fore.RED}Permission denied{Style.RESET_ALL}")

    def get_info(self):
        return "show", "List files and directories in the current directory."
