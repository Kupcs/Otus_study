# from base import Figure
from scr.rectangle import Rectangle


class Square(Rectangle):
    """"Класс квадрат"""
    def __init__(self, side_a, name):
        super().__init__(side_a, side_a)
        if side_a <= 0:
            raise ValueError("В квадрате не может быть отрицательных или нулевых сторон")
        self.side_a = side_a
        self.name = name

    def area(self):
        return self.side_a**2




