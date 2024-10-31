import sys
import importlib
from typing import Dict
from commands.base_cmd import Command
import subprocess
import colorama
import os

COMMANDS: Dict[str, str] = {
    "goto": "goto",
    "show": "show",
    "cdir": "cdir",
    "help": "help",
    "clear": "clear",
    "git":"git",
}

colorama.init(autoreset=True)

def get_cwd() -> str:
    return os.getcwd()

def main():
    while True:
        current_dir = get_cwd()
        sys.stdout.write(f"{current_dir} $ ")
        sys.stdout.flush()

        cmd = input().strip()

        if cmd.lower() == "exit":
            break

        parts = cmd.split()
        command = parts[0]
        args = parts[1:]

        # Check if the command is in the COMMANDS dictionary
        if command in COMMANDS:
            module_name = f"commands.{COMMANDS[command]}"
            try:
                module = importlib.import_module(module_name)
                command_class_name = f"{command.capitalize()}Command"
                command_class = getattr(module, command_class_name)

                if issubclass(command_class, Command):
                    command_instance = command_class()
                    command_instance.run(args)
                else:
                    print(f"{colorama.Fore.RED}Command {command} is not a valid command implementation.{colorama.Style.RESET_ALL}")

            except Exception as e:
                print(f"{colorama.Fore.RED}Error executing command {command}: {e}.{colorama.Style.RESET_ALL}")

        else:
            try:
                result = subprocess.run(parts, check=True, text=True, capture_output=True)
                print(result.stdout)
                if result.stderr:
                    print(f"{colorama.Fore.RED}Error: {result.stderr}{colorama.Style.RESET_ALL}") 
            except subprocess.CalledProcessError as e:
                print(f"{colorama.Fore.RED}Error: {e.stderr}{colorama.Style.RESET_ALL}")
            except FileNotFoundError:
                print(f"{colorama.Fore.RED}Command not found: {command}{colorama.Style.RESET_ALL}")

if __name__ == "__main__":
    main()
