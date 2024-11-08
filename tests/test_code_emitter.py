from pcc import parse, assembly_gen, code_emitter
import importlib
from tests import resources


class TestCodeEmitter:
  def test_codegen_succeed(self, tokens):
    parser = parse.Parser(tokens=tokens)
    program_ast = parser.parse_program()
    generator = assembly_gen.AssemblyGenerator(program_ast)
    program_aast = generator.parse_program_ast()
    path = importlib.resources.files(resources).joinpath(f"{program_aast.function_definition.name}")
    emitter = code_emitter.CodeEmitter(str(path), program_aast)
    emitter.emit()
    with open(path, "r") as file:
      content = file.read()
      expected_content = "".join(["    .global _main\n", "_main:\n", "    movl $100, %eax\n", "    ret"])
      assert content == expected_content
