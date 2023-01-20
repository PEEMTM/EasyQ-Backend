from abc import ABC, abstractmethod

class Expr(ABC):
    @abstractmethod
    def eval(self):
        pass
