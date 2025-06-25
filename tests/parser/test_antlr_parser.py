#!/usr/bin/env python3
"""
Unit tests for Copper parser
"""
import unittest
import os
from src.parser.antlr_parser import validate_copper_syntax


class TestCopperParser(unittest.TestCase):
    """Test cases for Copper language parser"""
    
    def test_simple_model(self):
        """Test parsing of a simple model"""
        copper_code = """model: orders {
  dimension: order_id {
    type: string
  }
}"""
        
        result = validate_copper_syntax(copper_code)
        
        # Check that parsing succeeded
        self.assertTrue(result['valid'], f"Parser failed with errors: {result['errors']}")
        
        # Check statistics
        self.assertEqual(result['statistics']['total_models'], 1)
        self.assertEqual(result['statistics']['total_views'], 0)
        self.assertEqual(result['statistics']['total_dimensions'], 1)
        self.assertEqual(result['statistics']['total_measures'], 0)
        
        # Check that we have no errors
        self.assertEqual(len(result['errors']), 0)
        
        print("✅ Simple model test passed!")
    
    def test_minimal_example_file(self):
        """Test parsing the minimal.copper example file"""
        example_file = os.path.join(os.path.dirname(__file__), '..', '..', 'examples', 'minimal.copper')
        
        with open(example_file, 'r') as f:
            copper_code = f.read()
        
        result = validate_copper_syntax(copper_code)
        
        # Check that parsing succeeded
        self.assertTrue(result['valid'], f"Parser failed with errors: {result['errors']}")
        
        # Check statistics
        self.assertEqual(result['statistics']['total_models'], 1)
        self.assertEqual(result['statistics']['total_dimensions'], 1)
        
        print(f"✅ Example file test passed! Found {result['statistics']['total_models']} model(s)")
    
    def test_multiple_dimensions(self):
        """Test parsing a model with multiple dimensions"""
        copper_code = """model: customers {
  dimension: customer_id {
    type: string
  }
  dimension: customer_name {
    type: string
  }
  dimension: age {
    type: number
  }
}"""
        
        result = validate_copper_syntax(copper_code)
        
        # Check that parsing succeeded
        self.assertTrue(result['valid'], f"Parser failed with errors: {result['errors']}")
        
        # Check statistics
        self.assertEqual(result['statistics']['total_models'], 1)
        self.assertEqual(result['statistics']['total_dimensions'], 3)
        self.assertEqual(result['statistics']['total_measures'], 0)
        
        print("✅ Multiple dimensions test passed!")
    
    def test_simple_view(self):
        """Test parsing a simple view"""
        copper_code = """view: sales_view {
  from: orders
}"""
        
        result = validate_copper_syntax(copper_code)
        
        # Check that parsing succeeded
        self.assertTrue(result['valid'], f"Parser failed with errors: {result['errors']}")
        
        # Check statistics
        self.assertEqual(result['statistics']['total_models'], 0)
        self.assertEqual(result['statistics']['total_views'], 1)
        
        print("✅ Simple view test passed!")
    
    def test_model_and_view(self):
        """Test parsing both model and view"""
        copper_code = """model: orders {
  dimension: order_id {
    type: string
  }
}

view: order_view {
  from: orders
}"""
        
        result = validate_copper_syntax(copper_code)
        
        # Check that parsing succeeded
        self.assertTrue(result['valid'], f"Parser failed with errors: {result['errors']}")
        
        # Check statistics
        self.assertEqual(result['statistics']['total_models'], 1)
        self.assertEqual(result['statistics']['total_views'], 1)
        self.assertEqual(result['statistics']['total_dimensions'], 1)
        
        print("✅ Model and view test passed!")
    
    def test_dax_expressions(self):
        """Test parsing models with DAX expressions"""
        copper_code = """model: orders {
  dimension: order_id {
    type: string
    expression: Orders[OrderID] ;;
  }
  dimension: calculated_value {
    type: number
    expression: SUM(Orders[Amount]) + 100 ;;
  }
}"""
        
        result = validate_copper_syntax(copper_code)
        
        # Check that parsing succeeded
        self.assertTrue(result['valid'], f"Parser failed with errors: {result['errors']}")
        
        # Check statistics
        self.assertEqual(result['statistics']['total_models'], 1)
        self.assertEqual(result['statistics']['total_dimensions'], 2)
        
        print("✅ DAX expressions test passed!")
    
    def test_all_example_files(self):
        """Test parsing all example files"""
        import glob
        example_files = glob.glob('../../examples/*.copper')
        
        for example_file in example_files:
            with self.subTest(file=example_file):
                print(f"\n🧪 Testing {example_file}...")
                
                with open(example_file, 'r') as f:
                    copper_code = f.read()
                
                result = validate_copper_syntax(copper_code)
                
                # Check that parsing succeeded
                self.assertTrue(result['valid'], 
                    f"Parser failed for {example_file} with errors: {result['errors']}")
                
                # Print statistics
                print(f"   ✅ Models: {result['statistics']['total_models']}")
                print(f"   ✅ Views: {result['statistics']['total_views']}")
                print(f"   ✅ Dimensions: {result['statistics']['total_dimensions']}")
                print(f"   ✅ Measures: {result['statistics']['total_measures']}")


if __name__ == '__main__':
    unittest.main()