from base import Figure
import math



class Circle(Figure):
    """"Класс круг"""
    def __init__(self, radius, name):
        super().__init__(name = "Circle")
        if radius <= 0:
            raise ValueError("В круге не может быть отрицательного или нулевого радиуса")
        self.r = radius

    def get_perimetr(self):
        return 2 * self.r * math.pi

    def area(self):
        return math.pi * self.r**2


