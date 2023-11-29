import pytest
from scr.triagle import Triagle


def test_create_triangle_positive(for_triangle):
    a,b,c = for_triangle
    assert a + b > c, f"сумма сторон a и b  больше или стороны с"
    assert a + c > b, f"сумма сторон a и c  больше или стороны b"
    assert b + c > a, f"сумма сторон b и c  больше или стороны a"


@pytest.mark.parametrize(("side_a", "side_b", "side_c"),
                        [(3, 4, 7),
                         (2.3, 3, 1.2)
                        ], ids=["integer", "float"])
def test_triangle_sides_positive(side_a, side_b, side_c):
    assert side_a > 0, f"сторонa a меньше или ровна 0"
    assert side_b > 0, f"сторонa b меньше или ровна 0"
    assert side_c > 0, f"сторонa c меньше или ровна 0"


@pytest.mark.parametrize(("triangle_sides", "perimetr"),
                          [
                              ("integer", 12),
                              ("float", 12.7)
                          ], ids=["test_with_integer", "test_with_float"])
def test_check_triangle_perimetr_positive(get_data_for_triangle_from_db, triangle_sides, perimetr):
    side_a, side_b, side_c = get_data_for_triangle_from_db(triangle_sides=triangle_sides)
    t = Triagle(side_a, side_b, side_c, "Triagle")
    assert t.get_perimetr() == perimetr



