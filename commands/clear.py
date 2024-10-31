import os 
from typing import List
from .base_cmd import Command

class ClearCommand(Command):
    def run(self, args: List[str]) -> None:
        os.system("cls" if os.name == "nt" else "clear")
    def get_info(self):
        return "clear", "Clear the terminal screen."
