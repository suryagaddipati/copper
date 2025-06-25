#!/usr/bin/env python3
"""
Unit tests for Copper ANTLR parser
"""
import unittest
from unittest.mock import MagicMock, patch

from antlr4 import InputStream, CommonTokenStream

from src.parser.antlr_parser import (
    CopperANTLRParser,
    CopperErrorListener,
    CopperParseTreeListener,
    NodeType,
    ParsedNode,
)
from src.parser.generated.CopperLexer import CopperLexer
from src.parser.generated.CopperParser import CopperParser


class TestCopperParseTreeListener(unittest.TestCase):
    """Unit tests for the CopperParseTreeListener"""

    def setUp(self):
        self.listener = CopperParseTreeListener()

    def _parse_text(self, text):
        input_stream = InputStream(text)
        lexer = CopperLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = CopperParser(stream)
        return parser

    def test_enter_model_statement(self):
        """Test that a model node is correctly created"""
        parser = self._parse_text("model: test_model {}")
        tree = parser.modelStatement()
        self.listener.enterModelStatement(tree)

        self.assertEqual(len(self.listener.nodes), 1)
        self.assertEqual(self.listener.nodes[0].type, NodeType.MODEL)
        self.assertEqual(self.listener.nodes[0].name, "test_model")

    def test_enter_view_statement(self):
        """Test that a view node is correctly created"""
        parser = self._parse_text("view: test_view {}")
        tree = parser.viewStatement()
        self.listener.enterViewStatement(tree)

        self.assertEqual(len(self.listener.nodes), 1)
        self.assertEqual(self.listener.nodes[0].type, NodeType.VIEW)
        self.assertEqual(self.listener.nodes[0].name, "test_view")

    def test_enter_dimension_statement(self):
        """Test that a dimension node is correctly created"""
        # First, create a model to attach the dimension to
        parser = self._parse_text("model: test_model { dimension: test_dimension {} }")
        model_tree = parser.modelStatement()
        self.listener.enterModelStatement(model_tree)

        # Now, test the dimension statement
        dimension_tree = model_tree.modelBody(0).dimensionStatement()
        self.listener.enterDimensionStatement(dimension_tree)

        model_node = self.listener.nodes[0]
        self.assertEqual(len(model_node.children), 1)
        self.assertEqual(model_node.children[0].type, NodeType.DIMENSION)
        self.assertEqual(model_node.children[0].name, "test_dimension")

    def test_enter_type_parameter(self):
        """Test that the type parameter is correctly parsed"""
        parser = self._parse_text("type: string")
        tree = parser.typeParameter()

        # Create a dummy node to attach the parameter to
        self.listener.current_node = ParsedNode(NodeType.DIMENSION, "test", {}, [], 0)
        self.listener.enterTypeParameter(tree)

        self.assertEqual(self.listener.current_node.properties['type'], "string")

    def test_enter_label_parameter(self):
        """Test that the label parameter is correctly parsed"""
        parser = self._parse_text('label: "Test Label"')
        tree = parser.labelParameter()

        self.listener.current_node = ParsedNode(NodeType.DIMENSION, "test", {}, [], 0)
        self.listener.enterLabelParameter(tree)

        self.assertEqual(self.listener.current_node.properties['label'], "Test Label")

    def test_enter_description_parameter(self):
        """Test that the description parameter is correctly parsed"""
        parser = self._parse_text('description: "Test Description"')
        tree = parser.descriptionParameter()

        self.listener.current_node = ParsedNode(NodeType.DIMENSION, "test", {}, [], 0)
        self.listener.enterDescriptionParameter(tree)

        self.assertEqual(self.listener.current_node.properties['description'], "Test Description")

    def test_enter_primary_key_parameter(self):
        """Test that the primary_key parameter is correctly parsed"""
        parser = self._parse_text("primary_key: yes")
        tree = parser.primaryKeyParameter()

        self.listener.current_node = ParsedNode(NodeType.DIMENSION, "test", {}, [], 0)
        self.listener.enterPrimaryKeyParameter(tree)

        self.assertTrue(self.listener.current_node.properties['primary_key'])

    def test_enter_hidden_parameter(self):
        """Test that the hidden parameter is correctly parsed"""
        parser = self._parse_text("hidden: no")
        tree = parser.hiddenParameter()

        self.listener.current_node = ParsedNode(NodeType.DIMENSION, "test", {}, [], 0)
        self.listener.enterHiddenParameter(tree)

        self.assertFalse(self.listener.current_node.properties['hidden'])

    def test_enter_value_format_parameter(self):
        """Test that the value_format parameter is correctly parsed"""
        parser = self._parse_text('value_format: "$#,##0.00"')
        tree = parser.valueFormatParameter()

        self.listener.current_node = ParsedNode(NodeType.DIMENSION, "test", {}, [], 0)
        self.listener.enterValueFormatParameter(tree)

        self.assertEqual(self.listener.current_node.properties['value_format'], "$#,##0.00")

    def test_enter_units_parameter(self):
        """Test that the units parameter is correctly parsed"""
        parser = self._parse_text('units: "USD"')
        tree = parser.unitsParameter()

        self.listener.current_node = ParsedNode(NodeType.DIMENSION, "test", {}, [], 0)
        self.listener.enterUnitsParameter(tree)

        self.assertEqual(self.listener.current_node.properties['units'], "USD")

    def test_enter_expression_parameter(self):
        """Test that the expression parameter is correctly parsed"""
        with patch('src.parser.antlr_parser.validate_dax_expression') as mock_validate_dax:
            mock_validate_dax.return_value = {'valid': True, 'errors': []}
            parser = self._parse_text("expression: a + b;;")
            tree = parser.expressionParameter()

            self.listener.current_node = ParsedNode(NodeType.DIMENSION, "test", {}, [], 0)
            self.listener.enterExpressionParameter(tree)

            self.assertEqual(self.listener.current_node.properties['expression'], "a+b")
            mock_validate_dax.assert_called_once_with("a+b")


class TestCopperErrorListener(unittest.TestCase):
    """Unit tests for the CopperErrorListener"""

    def setUp(self):
        self.listener = CopperErrorListener()

    def test_syntax_error(self):
        """Test that a syntax error is correctly reported"""
        self.listener.syntaxError(None, None, 1, 0, "mismatched input '{' expecting {'model', 'view', COMMENT, NEWLINE}", None)

        self.assertEqual(len(self.listener.errors), 1)
        self.assertIn("Line 1:0 - mismatched input '{' expecting {'model', 'view', COMMENT, NEWLINE}", self.listener.errors[0])

    def test_dax_syntax_warning(self):
        """Test that a DAX-related syntax error is correctly reported as a warning"""
        self.listener.syntaxError(None, None, 1, 0, "token recognition error at: '='", None)

        self.assertEqual(len(self.listener.warnings), 1)
        self.assertIn("Line 1:0 - Possible DAX syntax: token recognition error at: '='", self.listener.warnings[0])

if __name__ == '__main__':
    unittest.main()
