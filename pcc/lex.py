"""Contains the code for lexer"""

from __future__ import annotations
import enum
from dataclasses import dataclass
from typing import List


class TokenType(enum.StrEnum):
  TK_IDENTIFIER = enum.auto()
  TK_CONSTANT = enum.auto()
  TK_KEYWORD = enum.auto()
  TK_OPAREN = enum.auto()
  TK_CPAREN = enum.auto()
  TK_OBRACE = enum.auto()
  TK_CBRACE = enum.auto()

@dataclass
class Token:
  type: TokenType
  value: str

class Lexer:
  """
  Contains all the logic of the lexer pass.
  """

  def __init__(self):
    pass

  def tokenize(self, text: str) -> List[Token]:
    """
    Tokenize a text and return a list of tokens.

    Args:
        text: the input text to tokenize
    Returns:
        a list of Tokens

    """
    text = text.strip()

    return []
