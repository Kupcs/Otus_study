import pytest
from scr.square import Square



@pytest.mark.parametrize(("side_a", "area"),
                        [(4, 16),
                         (2.5, 6.25)
                        ], ids=["test_with_integer", "test_with_float"])
def test_square_area_positive(side_a, area):
    a = Square(side_a, "s")
    assert a.area() == area


