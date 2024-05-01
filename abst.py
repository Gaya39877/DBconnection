from abc import ABC, abstractmethod

class Phone(ABC):
    @abstractmethod
    def func(self):
        pass

class samsung(Phone):
    def func(self):
        pass

obj = samsung()
