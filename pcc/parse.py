"""
Contain parser logic
"""

from typing import List
from pcc import lex
from abc import ABC


class AST(ABC):
  pass


class Statement(ABC):
  pass


class Constant(ABC):
  def __init__(self, value: str):
    self.value = value


class Expression(ABC):
  def __init__(self, constant: Constant):
    self.value = constant


class ReturnStatement(Statement):
  def __init__(self, exp: Expression):
    self.exp = exp


class Identifier(AST):
  def __init__(self, value: str):
    self.value = value


class Function(AST):
  def __init__(self, name: Identifier, body: Statement):
    self.name = name
    self.body = body


class Program(AST):
  def __init__(self, function_definition: Function):
    self.function_definition = function_definition


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

  def parse_program(self):
    pass

  def parse_statement(self) -> Statement:
    self._expect("return")
    self._next_token()
    return_val = self.parse_exp()
    self._next_token()
    self._expect(";")
    return ReturnStatement(return_val)

  def parse_function(self):
    pass

  def parse_exp(self) -> Expression:
    token = self.tokens[self.current_index]
    return Expression(self.parse_int(token))

  def parse_identifier(self):
    pass

  def parse_int(self, token: lex.Token) -> Constant:
    return Constant(token.value)
