from pcc import parse


class TestParser:
  def test_parser_succeed(self):
    parser = parse.Parser()
    tokens = []

    parser.parse(tokens)
    # assert ast != None
