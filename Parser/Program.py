from abc import ABC, abstractmethod

class Program(ABC):
    @abstractmethod
    def eval(self):
        pass