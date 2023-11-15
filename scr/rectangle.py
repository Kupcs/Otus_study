from base_f import Figure



class Rectangle(Figure):
    """"Класс четырехугольник"""
    def __init__(self, side_a, side_b, name):
        super().__init__(name = "Rectangle")
        if side_a <= 0 or side_b <= 0 <= 0:
            raise ValueError("В фигуре не может быть отрицательных или нулевых сторон")
        self.side_a = side_a
        self.side_b = side_b
        self.name = name

    def get_perimetr(self):
        return int((self.side_a + self.side_b) * 2)

    def get_area(self):
        return int(self.side_a * self.side_b)




