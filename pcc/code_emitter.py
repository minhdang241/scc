"""
This module contains the CodeEmitter class which is responsible for emitting
assembly code from an abstract assembly syntax tree (AAST) to a file.
"""

from pcc import assembly_gen


class CodeEmitter:
  """
  A class to emit assembly code from an abstract assembly syntax tree (AAST) to a file.
  """

  def __init__(self, filename: str, program_aast: assembly_gen.Program):
    self.filename = filename
    self.program_aast = program_aast

  def emit(self):
    print("Emit code to file")
    with open(self.filename, "w") as file:
      file.write(CodeEmitter._to_assembly(self.program_aast))

  @staticmethod
  def _to_assembly(aast: assembly_gen.AAST) -> str:
    if isinstance(aast, assembly_gen.Program):
      return CodeEmitter._to_assembly(aast.function_definition)

    spaces = " " * 4
    result = []
    if isinstance(aast, assembly_gen.Function):
      result.append(f"{spaces}.global _{aast.name}\n")
      result.append(f"_{aast.name}:\n")
      for instructor in aast.instructions:
        result.append(CodeEmitter._to_assembly(instructor))
    elif isinstance(aast, assembly_gen.Instruction):
      if isinstance(aast, assembly_gen.Mov):
        result.append(f"{spaces}movl {CodeEmitter._to_assembly(aast.src)}, {CodeEmitter._to_assembly(aast.dst)}\n")
      elif isinstance(aast, assembly_gen.Ret):
        result.append(f"{spaces}ret")
      else:
        raise ValueError(f"Invalid instructor: {aast}")
    elif isinstance(aast, assembly_gen.Operand):
      if isinstance(aast, assembly_gen.Register):
        result.append("%eax")
      elif isinstance(aast, assembly_gen.Imm):
        result.append(f"${aast.value}")
      else:
        raise ValueError("Invalid operand: {aast}")
    else:
      raise ValueError("Invalid aast: {aast}")
    return "".join(result)
