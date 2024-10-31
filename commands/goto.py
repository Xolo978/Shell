import os
from typing import List
from .base_cmd import Command

class GotoCommand(Command):
    def run(self,args: List[str]) -> None:
        if(len(args)!=1):
            print("Usage: goto <path>")
            return
        try:
            os.chdir(args[0])
            print(f"Changed directory to {args[0]}")
        except FileNotFoundError:
            print(f"Directory {args[0]} not found")
        except PermissionError:
            print(f"Permission denied for directory {args[0]}")