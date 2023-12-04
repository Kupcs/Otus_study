import pytest
from scr.rectangle import Rectangle



def test_area_positive(input_for_rectangle):
    side_a, side_b, area = input_for_rectangle
    figure = Rectangle(side_a, side_b)
    assert figure.area() == area

@pytest.mark.parametrize(("rectangle_sides", "area"),
                          [
                              ("integer", 8),
                              ("float", 13.12)
                          ], ids=["test_with_integer", "test_with_float"])
def test_check_rectangle_perimetr_positive(get_data_for_rectangle_from_db, rectangle_sides, area):
    side_a, side_b = get_data_for_rectangle_from_db(rectangle_sides=rectangle_sides)
    figure = Rectangle(side_a, side_b)
    assert figure.area() == area


