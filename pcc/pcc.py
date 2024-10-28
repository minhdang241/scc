#!/usr/bin/env python3
"""
Compiler driver
"""

from __future__ import annotations
import argparse
import lex

if __name__ == "__main__":
  parser = argparse.ArgumentParser(
    prog="Simple C Compiler Driver",
    description="Compile C file to executable file",
  )
  parser.add_argument("filename")
  parser.add_argument("--lex", action="store_true", help="Perform lexical analysis only")
  parser.add_argument("--parse")
  parser.add_argument("--codegen")
  args = parser.parse_args()

  # Pass 1: Lex
  if args.lex:
    with open(args.filename, "r") as f:
      text = f.read()
      lexer = lex.Lexer()
      try:
        tokens = lexer.tokenize(text)
      except ValueError:
        exit(1)
