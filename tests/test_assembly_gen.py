from pcc import parse, assembly_gen


class TestCodeGenerator:
  def test_codegen_succeed(self, tokens):
    parser = parse.Parser(tokens=tokens)
    program_ast = parser.parse_program()
    code_generator = assembly_gen.AssemblyGenerator(program_ast)
    assembly_ast = code_generator.parse_program_ast()
    print(assembly_ast)
    assert assembly_ast != None
    assert len(assembly_ast.function_definition.instructions) == 2
