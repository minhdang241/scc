from pcc import lex
import pytest


class TestLexer:
  def test_tokenize_succeed(self, multi_digit_file_content):
    lexer = lex.Lexer()
    tokens = []
    tokens = lexer.tokenize(multi_digit_file_content)
    assert len(tokens) == 10

  @pytest.mark.xfail
  def test_tokenize_fail(self, at_sign_file_content):
    lexer = lex.Lexer()
    lexer.tokenize(at_sign_file_content)
