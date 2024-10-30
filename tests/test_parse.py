from pcc import parse, lex


class TestParser:
  def test_parser_succeed(self):
    tokens = [lex.Token("return", lex.TokenType.TK_KEYWORD), lex.Token("2", lex.TokenType.TK_CONSTANT), lex.Token(";", lex.TokenType.TK_SEMICOLON)]
    parser = parse.Parser(tokens=tokens)
    statement = parser.parse_statement()
    assert statement != None
    assert isinstance(statement, parse.Statement)
