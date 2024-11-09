#!/usr/bin/env python3
"""Contains driver logic"""

import argparse
from pcc import lex, parse, assembly_gen, code_emitter
import os
import sys

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
  tokens = []
  with open(args.filename, "r") as f:
    text = f.read()
    lexer = lex.Lexer()
    try:
      tokens = lexer.tokenize(text)
    except ValueError:
      print("Failed to tokenize the text")
      sys.exit(1)

    if not args.lex:
      parser = parse.Parser(tokens)
      try:
        program_ast = parser.parse_program()
      except ValueError:
        print("Failed to parse the program")
        sys.exit(1)

      if not args.parse:
        code_generator = assembly_gen.AssemblyGenerator(program_ast)
        try:
          program_aast = code_generator.parse_program_ast()
        except ValueError:
          print("Failed to generate assembly AST")
          sys.exit(1)

        if not args.codegen:
          output_file = os.path.dirname(args.filename) + "/" + os.path.basename(args.filename)[:-2]
          code_emitter = code_emitter.CodeEmitter(output_file, program_aast)
          try:
            code_emitter.emit()
          except ValueError:
            print("Failed to emit code")
            sys.exit(1)
