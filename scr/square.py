from base_f import Figure
from rectangle import Rectangle



class Square(Rectangle):
    """"Класс квадрат"""
    def __init__(self, side_a, name):
        super().__init__(side_a, side_a, name = "Square")
        if side_a <= 0:
            raise ValueError("В фигуре не может быть отрицательных или нулевых сторон")
        self.side_a = side_a
        self.name = name






