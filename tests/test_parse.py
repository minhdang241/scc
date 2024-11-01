from pcc import lex, parse


class TestParser:
  def test_parser_succeed(self, multi_digit_file_content: str):
    lexer = lex.Lexer()
    tokens = lexer.tokenize(multi_digit_file_content)
    parser = parse.Parser(tokens=tokens)
    print(tokens)
    program = parser.parse_program()
    assert program != None
    parse.print_ast(program)
    assert isinstance(program, parse.Program)
