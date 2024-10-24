from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List


class TokenType(Enum):
    TK_IDENTIFIER = 1
    TK_CONSTANT = 2
    TK_KEYWORD = 3
    TK_OPAREN = 4
    TK_CPAREN = 5
    TK_OBRACE = 6
    TK_CBRACE = 7


@dataclass
class Token:
    token_type: TokenType
    token_value: str


class Lexer:
    def __init__(self):
        pass

    def tokenize(self, text: str) -> List[Token]:
        text = text.trim()
        while text:
            regex
