import os
from typing import List
from .base_cmd import Command

class CreateCommand(Command):
    def run(self,args : List[str]) -> None:
        if(len(args)!=1):
            print("Usage create <directory_name>")
            return
        directory_name = args[0]
        try:
            os.mkdir(directory_name)
            print(f"Directory {directory_name} created successfully")
        except FileExistsError:
            print(f"Directory {directory_name} already exists")
        except PermissionError:
            print(f"Permission denied to create directory {directory_name}")
        except Exception as e:
            print(f"Error creating directory {directory_name}: {e}")
    
    def get_info(self):
        return "mkdir", "Create a new directory."