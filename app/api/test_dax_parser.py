#!/usr/bin/env python3
"""
Unit tests for DAX parser module
"""
import unittest
from dax_parser import parse_dax_expression, validate_dax_expression, DAXTokenType


class TestDAXParser(unittest.TestCase):
    """Test cases for DAX expression parser"""
    
    def test_simple_identifier(self):
        """Test parsing simple identifiers"""
        result = parse_dax_expression("Orders[OrderID]")
        
        self.assertTrue(result.success)
        self.assertEqual(len(result.errors), 0)
        
        # Check tokens
        non_ws_tokens = [t for t in result.tokens if t.type != DAXTokenType.WHITESPACE]
        self.assertEqual(len(non_ws_tokens), 4)
        self.assertEqual(non_ws_tokens[0].type, DAXTokenType.IDENTIFIER)
        self.assertEqual(non_ws_tokens[0].value, "Orders")
        self.assertEqual(non_ws_tokens[1].type, DAXTokenType.BRACKET_OPEN)
        self.assertEqual(non_ws_tokens[2].type, DAXTokenType.IDENTIFIER)
        self.assertEqual(non_ws_tokens[2].value, "OrderID")
        self.assertEqual(non_ws_tokens[3].type, DAXTokenType.BRACKET_CLOSE)
        
        print("✅ Simple identifier test passed!")
    
    def test_function_call(self):
        """Test parsing function calls"""
        result = parse_dax_expression("SUM(Orders[Amount])")
        
        self.assertTrue(result.success)
        self.assertEqual(len(result.errors), 0)
        
        # Check that SUM is recognized as a function
        function_tokens = [t for t in result.tokens if t.type == DAXTokenType.FUNCTION]
        self.assertEqual(len(function_tokens), 1)
        self.assertEqual(function_tokens[0].value, "SUM")
        
        print("✅ Function call test passed!")
    
    def test_complex_expression(self):
        """Test parsing complex expressions"""
        result = parse_dax_expression("SUM(Orders[Amount]) + RELATED(Customers[Discount]) * 0.1")
        
        self.assertTrue(result.success)
        self.assertEqual(len(result.errors), 0)
        
        # Check for expected tokens
        function_tokens = [t for t in result.tokens if t.type == DAXTokenType.FUNCTION]
        self.assertEqual(len(function_tokens), 2)  # SUM and RELATED
        
        operator_tokens = [t for t in result.tokens if t.type == DAXTokenType.OPERATOR]
        self.assertGreaterEqual(len(operator_tokens), 2)  # + and *
        
        number_tokens = [t for t in result.tokens if t.type == DAXTokenType.NUMBER]
        self.assertEqual(len(number_tokens), 1)  # 0.1
        
        print("✅ Complex expression test passed!")
    
    def test_string_literals(self):
        """Test parsing string literals"""
        result = parse_dax_expression('IF(Orders[Status] = "Completed", "Done", "Pending")')
        
        self.assertTrue(result.success)
        self.assertEqual(len(result.errors), 0)
        
        # Check for string tokens
        string_tokens = [t for t in result.tokens if t.type == DAXTokenType.STRING]
        self.assertEqual(len(string_tokens), 3)
        self.assertEqual(string_tokens[0].value, '"Completed"')
        self.assertEqual(string_tokens[1].value, '"Done"')
        self.assertEqual(string_tokens[2].value, '"Pending"')
        
        print("✅ String literals test passed!")
    
    def test_trailing_semicolons(self):
        """Test that trailing semicolons are handled properly"""
        result1 = parse_dax_expression("Orders[OrderID];;")
        result2 = parse_dax_expression("Orders[OrderID]")
        
        self.assertTrue(result1.success)
        self.assertTrue(result2.success)
        
        # Both should normalize to the same expression
        self.assertEqual(result1.normalized_expression, result2.normalized_expression)
        
        print("✅ Trailing semicolons test passed!")
    
    def test_validation_function(self):
        """Test the validation function for main parser integration"""
        result = validate_dax_expression("SUM(Orders[Amount])")
        
        self.assertIsInstance(result, dict)
        self.assertTrue(result['valid'])
        self.assertEqual(len(result['errors']), 0)
        self.assertGreater(result['tokens'], 0)
        self.assertIn('normalized', result)
        
        print("✅ Validation function test passed!")
    
    def test_error_handling(self):
        """Test error handling for invalid expressions"""
        # Unmatched parentheses
        result = parse_dax_expression("SUM(Orders[Amount]")
        self.assertFalse(result.success)
        self.assertGreater(len(result.errors), 0)
        
        # Unmatched brackets
        result = parse_dax_expression("Orders[Amount")
        self.assertFalse(result.success)
        self.assertGreater(len(result.errors), 0)
        
        print("✅ Error handling test passed!")
    
    def test_whitespace_normalization(self):
        """Test whitespace normalization"""
        result = parse_dax_expression("  SUM  (  Orders [ Amount ]  )  ")
        
        self.assertTrue(result.success)
        normalized = result.normalized_expression
        
        # Should be cleaned up but readable
        self.assertNotIn("  ", normalized)  # No double spaces
        self.assertIn("SUM", normalized)
        self.assertIn("Orders", normalized)
        
        print("✅ Whitespace normalization test passed!")


if __name__ == '__main__':
    unittest.main()