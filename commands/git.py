import os
from .base_cmd import Command
from typing import List
import colorama

class GitCommand(Command):
    def run(self, args: List[str]) -> None:
        if not args:
            print(f"{colorama.Fore.YELLOW}Usage: git <command> [options]{colorama.Style.RESET_ALL}")
            return
        command_str = "git " + " ".join(args)
        exit_code = os.system(command_str)
        if exit_code != 0:
            print(f"{colorama.Fore.RED}Error: Command failed with exit code {exit_code}.{colorama.Style.RESET_ALL}")
        
    def get_info(self):
        return "git", "Run git commands."