
import unittest
from src.parser.antlr_parser import validate_copper_syntax

class TestCopperParser(unittest.TestCase):
    """Test cases for the new Copper language parser"""

    def test_simple_dimension(self):
        """Test parsing of a simple dimension"""
        copper_code = 'dimension: order_id { expression: ${orders.order_id} ;; }'
        result = validate_copper_syntax(copper_code)
        self.assertTrue(result['valid'], f"Parser failed with errors: {result['errors']}")
        self.assertEqual(result['statistics']['total_dimensions'], 1)
        print("✅ Simple dimension test passed!")

    def test_simple_measure(self):
        """Test parsing of a simple measure with a SUM function"""
        copper_code = 'measure: total_sales { expression: SUM(${orders.amount}) ;; }'
        result = validate_copper_syntax(copper_code)
        self.assertTrue(result['valid'], f"Parser failed with errors: {result['errors']}")
        self.assertEqual(result['statistics']['total_measures'], 1)
        print("✅ Simple measure test passed!")

    def test_measure_with_filter(self):
        """Test a measure with a simple expression"""
        copper_code = 'measure: total_amount { expression: ${orders.amount} ;; }'
        result = validate_copper_syntax(copper_code)
        self.assertTrue(result['valid'], f"Parser failed with errors: {result['errors']}")
        self.assertEqual(result['statistics']['total_measures'], 1)
        print("✅ Measure with simple expression test passed!")

    def test_measure_with_arithmetic(self):
        """Test a measure with arithmetic operations"""
        copper_code = 'measure: calculated_value { expression: ${orders.amount} + ${orders.tax} ;; }'
        result = validate_copper_syntax(copper_code)
        self.assertTrue(result['valid'], f"Parser failed with errors: {result['errors']}")
        self.assertEqual(result['statistics']['total_measures'], 1)
        print("✅ Measure with arithmetic test passed!")

    def test_complex_expression(self):
        """Test a measure with a more complex arithmetic expression"""
        copper_code = 'measure: average_order_value { expression: SUM(${orders.amount}) / COUNT(${orders.order_id}) ;; }'
        result = validate_copper_syntax(copper_code)
        self.assertTrue(result['valid'], f"Parser failed with errors: {result['errors']}")
        self.assertEqual(result['statistics']['total_measures'], 1)
        print("✅ Complex expression test passed!")

    def test_invalid_syntax(self):
        """Test that the parser correctly identifies invalid syntax"""
        copper_code = 'measure: bad_measure { expression: SUM( } THIS IS NOT VALID'
        result = validate_copper_syntax(copper_code)
        self.assertFalse(result['valid'])
        self.assertGreater(len(result['errors']), 0)
        print("✅ Invalid syntax test passed!")

if __name__ == '__main__':
    unittest.main()
