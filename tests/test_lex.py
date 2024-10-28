import importlib.resources
from pcc import lex
import importlib
from tests import resources


class TestLexer:
  def test_tokenize(self):
    lexer = lex.Lexer()
    path = importlib.resources.files(resources).joinpath("multi_digit.c")
    tokens = []
    with open(path) as file:
      tokens = lexer.tokenize(file.read())
    assert len(tokens) == 10
