import pytest



@pytest.fixture
def for_triangle():
     yield 3, 2, 4

@pytest.fixture
def get_data_for_triangle_from_db():
     def _wrapper(triangle_sides:str):
          if triangle_sides == "integer":
               return 3, 4, 5
          if triangle_sides == "float":
               return 3.2, 4.1, 5.4
     yield _wrapper

@pytest.fixture
def for_square():
     yield 3


@pytest.fixture()
def input_for_rectangle():
     yield 2, 7, 14

@pytest.fixture
def get_data_for_rectangle_from_db():
     def _wrapper(rectangle_sides:str):
          if rectangle_sides == "integer":
               return 2, 4
          if rectangle_sides == "float":
               return 3.2, 4.1
     yield _wrapper

@pytest.fixture()
def input_for_circle():
     yield 2, 12.566370614359172
