from pcc import codegen


class TestCodeGenerator:
  def test_codegen_succeed(self):
    code_generator = codegen.CodeGenerator()
    assert code_generator != None
