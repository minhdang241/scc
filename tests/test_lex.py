from pcc import lex
import importlib
from tests import resources
import pytest


class TestLexer:
  def test_tokenize_succeed(self):
    lexer = lex.Lexer()
    path = importlib.resources.files(resources).joinpath("multi_digit.c")
    tokens = []
    with open(path) as file:
      tokens = lexer.tokenize(file.read())
    assert len(tokens) == 10

  @pytest.mark.xfail
  def test_tokenize_fail(self):
    path = importlib.resources.files(resources).joinpath("at_sign.c")
    lexer = lex.Lexer()
    with open(path) as file:
      lexer.tokenize(file.read())
