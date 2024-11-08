from pcc import parse


class TestParser:
  def test_parser_succeed(self, tokens):
    parser = parse.Parser(tokens=tokens)
    program_ast = parser.parse_program()
    assert program_ast != None
    parse.print_ast(program_ast)
    assert isinstance(program_ast, parse.Program)
