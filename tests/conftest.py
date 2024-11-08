import pytest
import importlib
from tests import resources
import json
import lex


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


@pytest.fixture
def tokens():
  path = importlib.resources.files(resources).joinpath("tokens.json")
  with open(path, "r") as file:
    data = json.load(file)
    tokens = [lex.Token(**item) for item in data]
    yield tokens
