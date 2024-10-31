#!/usr/bin/env python3
"""Contains driver logic"""

from __future__ import annotations
import argparse
import lex
import parse

if __name__ == "__main__":
  argparser = argparse.ArgumentParser(
    prog="Simple C Compiler Driver",
    description="Compile C file to executable file",
  )
  argparser.add_argument("filename")
  argparser.add_argument("--lex", action="store_true", help="Perform lexical analysis only")
  argparser.add_argument("--parse", action="store_true", help="Perform lexical and parse pass")
  argparser.add_argument("--codegen")
  args = argparser.parse_args()

  # Pass 1: Lex
  tokens = []
  if args.parse or args.lex:
    with open(args.filename, "r") as f:
      text = f.read()
      lexer = lex.Lexer()
      try:
        tokens = lexer.tokenize(text)
      except ValueError:
        exit(1)

  if args.parse:
    parser = parse.Parser(tokens)
    parser.parse_program()
