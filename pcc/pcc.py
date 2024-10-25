#!/usr/bin/env python3
"""
Compiler driver
"""
from __future__ import annotations
import argparse

if __name__ == "__main__":
  parser = argparse.ArgumentParser(
      prog="Simple C Compiler Driver",
      description="Compile C file to executable file",
  )
  parser.add_argument("file_name")
  parser.add_argument("--lex")
  parser.add_argument("--parse")
  parser.add_argument("--codegen")
  args = parser.parse_args()
  print(args.file_name)
