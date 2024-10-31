import sys
import importlib
from typing import Dict
from commands.base_cmd import Command

COMMANDS: Dict[str, str] = {
    "goto":"goto",
    "show":"show",
    "cdir":"cdir",
    "help":"help",
}


def main():
    sys.stdout.write("$")
    sys.stdout.flush()
    cmd = input().strip()
    while cmd != "exit":
        parts = cmd.split()
        command = parts[0]
        args = parts[1:]
        if command not in COMMANDS:
            sys.stderr.write(f"Command {command} not found\n")
        else:
            # Dynamically importing the module
            module_name = f"commands.{COMMANDS[command]}"
            try:
                module = importlib.import_module(module_name)
                command_class_name = f"{command.capitalize()}Command"
                command_class = getattr(module, command_class_name)

                #Checking if the class is a valid command implementation
                if issubclass(command_class, Command):
                    #Creating a instance of the class and running it
                    command_instance = command_class()
                    command_instance.run(args)
                else:
                    print(f"Command {command} is not a valid command implementation")
            except Exception as e:
                print(f"Error executing command {command}: {e}")
        sys.stdout.write("$")
        sys.stdout.flush()
        cmd = input().strip()


if __name__ == "__main__":
    main()
