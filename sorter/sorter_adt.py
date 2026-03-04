from abc import ABC, abstractmethod

class Sorter(ABC):
    @abstractmethod
    def sort(self, data:list, key=lambda x: x) -> list:
        pass