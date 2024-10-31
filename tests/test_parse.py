import importlib.resources
from pcc import lex, parse
import importlib
from tests import resources


class TestParser:
  def test_parser_succeed(self):
    lexer = lex.Lexer()
    path = importlib.resources.files(resources).joinpath("return_2.c")
    with open(path, "r") as file:
      tokens = lexer.tokenize(file.read())
    parser = parse.Parser(tokens=tokens)
    print(tokens)
    program = parser.parse_program()
    assert program != None
    parse.print_ast(program)
    assert isinstance(program, parse.Program)
