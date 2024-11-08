from pcc import codegen, parse


class TestCodeGenerator:
  def test_codegen_succeed(self, tokens):
    parser = parse.Parser(tokens=tokens)
    program_ast = parser.parse_program()
    code_generator = codegen.CodeGenerator(program_ast)
    assembly_ast = code_generator.parse_program_ast()
    print(assembly_ast)
    assert assembly_ast != None
