#!/usr/bin/env python3
"""Contains driver logic"""

import argparse
from pcc import lex, parse, assembly_gen, code_emitter
import os

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
      tokens = lexer.tokenize(text)

    if args.parse or args.codegen:
      parser = parse.Parser(tokens)
      program_ast = parser.parse_program()

      if args.codegen:
        code_generator = assembly_gen.AssemblyGenerator(program_ast)
        program_aast = code_generator.parse_program_ast()
        output_file = os.path.basename(args.filename)[:-2]
        code_emitter = code_emitter.CodeEmitter(output_file, program_aast)
        code_emitter.emit()
