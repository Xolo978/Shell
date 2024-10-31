from typing import List

from commands.create import CreateCommand
from commands.goto import GotoCommand
from commands.show import ShowCommand
from .base_cmd import Command

class HelpCommand(Command):
    def run (self,args:List[str]) -> None:
        for command_class in [GotoCommand, ShowCommand, CreateCommand, HelpCommand]:
            command_instance = command_class()
            command_name, command_desc = command_instance.get_info()
            print(f"- {command_name}: {command_desc}")
    
    def get_info(self):
        return "help", "List all available commands."