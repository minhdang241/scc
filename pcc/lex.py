"""Contains lexer logic"""

import enum
import dataclasses
from typing import List
import re


class TokenType(enum.StrEnum):
  TK_IDENTIFIER = enum.auto()
  TK_CONSTANT = enum.auto()
  TK_KEYWORD = enum.auto()
  TK_OPAREN = enum.auto()
  TK_CPAREN = enum.auto()
  TK_OBRACE = enum.auto()
  TK_CBRACE = enum.auto()
  TK_SEMICOLON = enum.auto()


class TokenPattern(enum.StrEnum):
  IDENTIFIER = r"^[a-zA-Z_]\w*\b"
  CONSTANT = r"^[0-9]+\b"
  INT_KEYWORD = r"^int\b"
  VOID_KEYWORD = r"^void\b"
  RETURN_KEYWORD = r"^return\b"
  OPAREN = r"^\("
  CPAREN = r"^\)"
  OBRACE = r"^{"
  CBRACE = r"^}"
  SEMICOLON = "^;"


@dataclasses.dataclass
class Token:
  value: str
  type: TokenType


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
    Raises:
        ValueError: if no pattern matches the text

    """
    print("Tokenizing the text")

    tokens = []
    while text:
      text = text.strip()
      found = False
      while text.startswith("//"):
        # Ignore comment
        index = text.find("\n")
        text = text[index + 1 :].strip()

      for pattern in TokenPattern:
        result = re.search(pattern, text)
        if not result:
          continue
        found = True
        start, end = result.span()

        match pattern:
          case TokenPattern.IDENTIFIER:
            token_type = TokenType.TK_IDENTIFIER
          case TokenPattern.CONSTANT:
            token_type = TokenType.TK_CONSTANT
          case TokenPattern.INT_KEYWORD, TokenPattern.VOID_KEYWORD, TokenPattern.RETURN_KEYWORD:
            token_type = TokenType.TK_KEYWORD
          case TokenPattern.OPAREN:
            token_type = TokenType.TK_OPAREN
          case TokenPattern.CPAREN:
            token_type = TokenType.TK_CPAREN
          case TokenPattern.OBRACE:
            token_type = TokenType.TK_OBRACE
          case TokenPattern.CBRACE:
            token_type = TokenType.TK_CBRACE
          case TokenPattern.SEMICOLON:
            token_type = TokenType.TK_SEMICOLON
        token = Token(value=text[start:end], type=token_type)
        tokens.append(token)
        text = text[end:]
        break
      if not found:
        raise ValueError(f"There is no pattern matching the text {text}")
    return tokens


if __name__ == "__main__":
  lexer = Lexer()
  tokens = lexer.tokenize("int main(void) {};")
  print(tokens)
  assert len(tokens) == 8
