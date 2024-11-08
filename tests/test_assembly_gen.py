from pcc import parse, assembly_gen


class TestAssemblyGenerator:
  def test_codegen_succeed(self, tokens):
    parser = parse.Parser(tokens=tokens)
    program_ast = parser.parse_program()
    code_generator = assembly_gen.AssemblyGenerator(program_ast)
    program_aast = code_generator.parse_program_ast()
    print(program_aast)
    assert program_aast != None
    assert len(program_aast.function_definition.instructions) == 2
