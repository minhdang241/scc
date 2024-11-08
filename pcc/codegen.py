"""
Contain code generator logic
"""

from pcc import parse
import abc
import dataclasses
from typing import List


class AAST(abc.ABC):
  pass


class Instruction(AAST):
  pass


class Operand(AAST):
  pass


@dataclasses.dataclass
class Imm(Operand):
  value: str


@dataclasses.dataclass
class Register(Operand):
  name: str = "EAX"


@dataclasses.dataclass
class Mov(Instruction):
  src: Imm | Register
  dst: Imm | Register


class Ret(Instruction):
  pass


@dataclasses.dataclass
class Function(AAST):
  name: str
  instructions: List[Instruction]


@dataclasses.dataclass
class Program(AAST):
  function_definition: Function


class CodeGenerator:
  def __init__(self, program: parse.Program):
    self.program = program

  def parse_program_ast(self) -> Program:
    function = self.parse_function_ast(self.program.function_definition)
    return Program(function)

  def parse_function_ast(self, function_definition: parse.Function) -> Function:
    instructions = self.parse_statement_ast(function_definition.body)
    return Function(function_definition.name.value, instructions)

  def parse_statement_ast(self, statement: parse.Statement) -> List[Instruction]:
    if isinstance(statement, parse.ReturnStatement):
      register = Register()
      imm = Imm(statement.exp.value.value)
      return [Mov(imm, register), Ret()]
    return []
