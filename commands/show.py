import os
from .base_cmd import Command
from typing import List

class ShowCommand(Command):
    def run(self,args: List[str]) -> None:
        target_dir = "."
        if len(args):
            target_dir = args[0]
        try:
            contents = os.listdir(target_dir)
            if contents:
                for item in contents:
                    print(item)
            else:
                print(f"{target_dir} is empty")
        except NotADirectoryError:
            print(f"{target_dir} is not a directory")
        except FileNotFoundError:
            print(f"Directory {target_dir} not found")
        except PermissionError:
            print(f"Permission denied for {target_dir}")
        