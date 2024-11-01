import pytest
import importlib
from tests import resources


@pytest.fixture
def multi_digit_file_content():
  path = importlib.resources.files(resources).joinpath("multi_digit.c")
  with open(path, "r") as file:
    yield file.read()


@pytest.fixture
def at_sign_file_content():
  path = importlib.resources.files(resources).joinpath("at_sign.c")
  with open(path, "r") as file:
    yield file.read()
