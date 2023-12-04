import pytest
from scr.circle import Circle


def test_area_circle(input_for_circle):
    r, area = input_for_circle
    figure = Circle(r, "Krug")
    assert figure.area() == area


@pytest.mark.parametrize(("radius", "area"),
                         [(2, 12.566370614359172),
                         (1.2, 4.523893421169302)
                         ], ids=["integer_input", "float_input"])
def test_area_circle_params(radius, area):
    radius,area = radius,area
    figure = Circle(radius, "Krug")
    assert figure.area() == area
