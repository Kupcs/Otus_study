from abc import ABC


class Figure(ABC):
    def __init__(self,name):
        self.name = name

    def get_perimetr(self):
        raise NotImplementedError ("определите фукция в доч классе")

    def perimetr(self):
        return self.get_perimetr()

    def get_area(self):
        raise NotImplementedError ("определите фукция в доч классе")

    def area(self):
        return self.get_area()

    def add_area(self, name2):
        if not isinstance(name2, Figure):
            raise ValueError("Нужно передать фигуру")
        return int(self.area()) + int(name2.area())



