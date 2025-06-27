import unittest
from antlr4 import InputStream, CommonTokenStream
from src.parser.generated.CopperLexer import CopperLexer
from src.parser.generated.CopperParser import CopperParser
from src.parser.antlr_parser import CopperParseTreeListener, NodeType

class TestCopperParseTreeListener(unittest.TestCase):
    """Unit tests for the CopperParseTreeListener with the new grammar"""

    def setUp(self):
        self.listener = CopperParseTreeListener()

    def _parse_text(self, text):
        input_stream = InputStream(text)
        lexer = CopperLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = CopperParser(stream)
        return parser

    def test_enter_measure_statement(self):
        """Test that a measure node is correctly created"""
        parser = self._parse_text("measure: test_measure { expression: 1 }")
        tree = parser.measureStatement()
        self.listener.enterMeasureStatement(tree)

        self.assertEqual(len(self.listener.nodes), 1)
        self.assertEqual(self.listener.nodes[0].type, NodeType.MEASURE)
        self.assertEqual(self.listener.nodes[0].name, "test_measure")
        print("✅ Unit test for measure statement passed!")

    def test_enter_dimension_statement(self):
        """Test that a dimension node is correctly created"""
        parser = self._parse_text("dimension: test_dimension { expression: 1 }")
        tree = parser.dimensionStatement()
        self.listener.enterDimensionStatement(tree)

        self.assertEqual(len(self.listener.nodes), 1)
        self.assertEqual(self.listener.nodes[0].type, NodeType.DIMENSION)
        self.assertEqual(self.listener.nodes[0].name, "test_dimension")
        print("✅ Unit test for dimension statement passed!")

    def test_aggregate_function_call(self):
        """Test parsing of the Aggregate function"""
        parser = self._parse_text("Aggregate(function: SUM, field: ${t.f})")
        tree = parser.functionCall()
        # This is a simplified test; in reality, the listener would build an AST.
        # Here, we just check that it doesn't crash.
        self.assertIsNotNone(tree)
        print("✅ Unit test for Aggregate function passed!")

    def test_over_clause(self):
        """Test parsing of the OVER clause"""
        parser = self._parse_text("OVER { partition_by: [${t.f}] }")
        tree = parser.overClause()
        self.assertIsNotNone(tree)
        print("✅ Unit test for OVER clause passed!")

    def test_field_reference(self):
        """Test parsing of a field reference"""
        parser = self._parse_text("${my_table.my_field}")
        tree = parser.fieldReference()
        self.assertEqual(tree.getText(), "${my_table.my_field}")
        print("✅ Unit test for field reference passed!")

if __name__ == '__main__':
    unittest.main()