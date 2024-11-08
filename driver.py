#!/usr/bin/env python3
"""Contains driver logic"""

import argparse
from pcc import lex, parse, assembly_gen

if __name__ == "__main__":
  argparser = argparse.ArgumentParser(
    prog="Simple C Compiler Driver",
    description="Compile C file to executable file",
  )
  argparser.add_argument("filename")
  argparser.add_argument("--lex", action="store_true", help="Perform lexical analysis only")
  argparser.add_argument("--parse", action="store_true", help="Perform up to parse pass")
  argparser.add_argument("--codegen", action="store_true", help="Perform up to codegen pass")
  args = argparser.parse_args()

  if args.parse or args.lex or args.codegen:
    tokens = []
    with open(args.filename, "r") as f:
      text = f.read()
      lexer = lex.Lexer()
      try:
        tokens = lexer.tokenize(text)
      except ValueError:
        exit(1)

    if args.parse or args.codegen:
      parser = parse.Parser(tokens)
      program_ast = parser.parse_program()

      if args.codegen:
        code_generator = assembly_gen.AssemblyGenerator(program_ast)
        program = code_generator.parse_program_ast()
