"""
Contain parser logic
"""

from typing import List
import lex
import abc
import dataclasses
import pprint


class AST(abc.ABC):
  pass


class Statement(AST):
  pass


@dataclasses.dataclass
class Constant(AST):
  value: str


@dataclasses.dataclass
class Expression(AST):
  value: Constant


@dataclasses.dataclass
class ReturnStatement(Statement):
  exp: Expression


@dataclasses.dataclass
class Identifier(AST):
  value: str


@dataclasses.dataclass
class Function(AST):
  name: Identifier
  body: Statement


@dataclasses.dataclass
class Program(AST):
  function_definition: Function


class Parser:
  """
  Implement parser using Recursive descent parsing
  """

  def __init__(self, tokens: List[lex.Token]):
    self.tokens = tokens
    self.current_index = 0

  def _expect(self, expected: str):
    """
    Check if the following tokens are valid before parsing

    Args:
      expected: The expected token
      tokens: List of the current tokens

    Raise
      ValueError: If the actual token value does not match with the expected one
    """
    if self.current_index == len(self.tokens):
      raise ValueError("Token list is empty for parsing")

    actual: lex.Token = self.tokens[self.current_index]
    if expected != actual.value:
      print(expected, actual)
      raise ValueError("The actual token value does not match with the expected one")

  def _next_token(self):
    """
    Move to the next token

    Raises:
      IndexError: If the index is out of bound
    """
    if self.current_index == len(self.tokens):
      raise IndexError("The current index is out of bound")
    else:
      self.current_index += 1

  def parse_program(self) -> Program:
    print("Parse the whole program")
    function_val = self.parse_function()
    return Program(function_val)

  def parse_statement(self) -> Statement:
    self._expect("return")
    self._next_token()
    return_val = self.parse_exp()
    self._next_token()
    self._expect(";")
    return ReturnStatement(return_val)

  def parse_function(self):
    self._expect("int")
    self._next_token()
    identifier_val = self.parse_identifier()
    self._next_token()
    self._expect("(")
    self._next_token()
    self._expect("void")
    self._next_token()
    self._expect(")")
    self._next_token()
    self._expect("{")
    self._next_token()
    statement_val = self.parse_statement()
    self._next_token()
    self._expect("}")
    return Function(identifier_val, statement_val)

  def parse_exp(self) -> Expression:
    token = self.tokens[self.current_index]
    return Expression(self.parse_int(token))

  def parse_identifier(self) -> Identifier:
    token = self.tokens[self.current_index]
    return Identifier(token.value)

  def parse_int(self, token: lex.Token) -> Constant:
    return Constant(token.value)


def print_ast(ast: AST):
  if isinstance(ast, ReturnStatement):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(ast)


if __name__ == "__main__":
  tokens = [lex.Token("return", lex.TokenType.TK_KEYWORD), lex.Token("2", lex.TokenType.TK_CONSTANT), lex.Token(";", lex.TokenType.TK_SEMICOLON)]
  parser = Parser(tokens=tokens)
  statement = parser.parse_statement()
  print_ast(statement)
