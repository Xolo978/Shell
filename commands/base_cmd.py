from abc import ABC, abstractmethod
from typing import List

class Command(ABC):
    @abstractmethod
    def run(self,args:List[str]) -> None:
        """
        Run the command with the given arguments.
        Handle all errors and exceptions here.
        """
        pass