import pytest
from scr.triagle import Triagle

e,hf

@pytest.mark.parametrize(("triangle_sides", "perimetr"),
                          [
                              ("integer", 12),
                              ("float", 12.7)
                          ], ids=["test_with_integer", "test_with_float"])
def test_check_triangle_perimetr_positive(get_data_for_triangle_from_db, triangle_sides, perimetr):
    side_a, side_b, side_c = get_data_for_triangle_from_db(triangle_sides=triangle_sides)
    t = Triagle(side_a, side_b, side_c, "Triagle")
    assert t.get_perimetr() == perimetr



