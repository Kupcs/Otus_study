from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self,name):
        self.name = name


    @abstractmethod
    def get_perimetr(self):
        pass


    @abstractmethod
    def area(self):
        pass

    def add_area(self, name2):
        if not isinstance(name2, Figure):
            raise ValueError("Нужно передать фигуру")
        return int(self.area()) + int(name2.area())



