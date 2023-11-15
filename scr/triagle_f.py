import math
from base_f import Figure
from rectangle import Rectangle
from circle_class import Circle

class Triagle(Figure):
    """"Класс трекголник"""

    def __init__(self, side_a, side_b, side_c, name):
        super().__init__(name = "Triagle")
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("В фигуре не может быть отрицательных или нулевых сторон")
        if not side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
            ValueError("нельзя создать треугольник")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_perimetr(self):
        p = int(self.side_a + self.side_b + self.side_c)
        return p

    def area(self):
        """"для расчета площади треугольник исп формула Герона"""
        p = int((self.side_a + self.side_b + self.side_c) / 2)
        s = math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))
        return s
