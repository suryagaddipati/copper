#!/usr/bin/env python3
"""
Test Suite for Copper Parser

Comprehensive tests for tokenizer, parser, and overall functionality.
Tests against example files and various edge cases.
"""

import unittest
import sys
import os
from pathlib import Path

# Add parser directory to path for imports
sys.path.insert(0, os.path.dirname(__file__))

try:
    # Try relative imports first (when run as module)
    from .tokenizer import CopperTokenizer, TokenType, Token
    from .parser import CopperParser, ParseError
    from .copper_parser import parse_string, parse_file, CopperParseResult
    from .ast_nodes import *
except ImportError:
    # Fall back to direct imports (when run as script)
    from tokenizer import CopperTokenizer, TokenType, Token
    from parser import CopperParser, ParseError
    from copper_parser import parse_string, parse_file, CopperParseResult
    from ast_nodes import *


class TestTokenizer(unittest.TestCase):
    """Test the tokenizer"""
    
    def test_simple_tokens(self):
        """Test basic token recognition"""
        source = "model: orders { }"
        tokenizer = CopperTokenizer(source)
        tokens = tokenizer.get_tokens()
        
        expected = [
            TokenType.MODEL,
            TokenType.COLON,
            TokenType.IDENTIFIER,
            TokenType.LEFT_BRACE,
            TokenType.RIGHT_BRACE,
            TokenType.EOF
        ]
        
        actual = [token.type for token in tokens]
        self.assertEqual(actual, expected)
    
    def test_string_literals(self):
        """Test string literal parsing"""
        source = 'label: "Order ID"'
        tokenizer = CopperTokenizer(source)
        tokens = tokenizer.get_tokens()
        
        self.assertEqual(tokens[0].type, TokenType.LABEL)
        self.assertEqual(tokens[2].type, TokenType.STRING_LITERAL)
        self.assertEqual(tokens[2].value, "Order ID")
    
    def test_number_literals(self):
        """Test number literal parsing"""
        source = "tiers: [0, 50, 100.5, -25]"
        tokenizer = CopperTokenizer(source)
        tokens = tokenizer.get_tokens()
        
        number_tokens = [token for token in tokens if token.type == TokenType.NUMBER_LITERAL]
        expected_values = ["0", "50", "100.5", "-25"]
        actual_values = [token.value for token in number_tokens]
        
        self.assertEqual(actual_values, expected_values)
    
    def test_boolean_literals(self):
        """Test boolean literal parsing"""
        source = "primary_key: yes hidden: false"
        tokenizer = CopperTokenizer(source)
        tokens = tokenizer.get_tokens()
        
        bool_tokens = [token for token in tokens if token.type == TokenType.BOOLEAN_LITERAL]
        expected_values = ["yes", "false"]
        actual_values = [token.value for token in bool_tokens]
        
        self.assertEqual(actual_values, expected_values)
    
    def test_dax_expression(self):
        """Test DAX expression tokenization"""
        source = 'expression: Orders[OrderID] ;;'
        tokenizer = CopperTokenizer(source)
        tokens = tokenizer.get_tokens()
        
        expected_types = [
            TokenType.EXPRESSION,
            TokenType.COLON,
            TokenType.DAX_EXPRESSION,
            TokenType.SEMICOLON_SEMICOLON,
            TokenType.EOF
        ]
        
        actual_types = [token.type for token in tokens]
        self.assertEqual(actual_types, expected_types)
        
        # Check DAX expression content
        dax_token = tokens[2]
        self.assertEqual(dax_token.value, "Orders[OrderID]")
    
    def test_complex_dax_expression(self):
        """Test complex multi-line DAX expression"""
        source = '''expression: 
            VAR CurrentRevenue = SUM(Orders[Amount])
            VAR PreviousRevenue = CALCULATE(
                SUM(Orders[Amount]),
                DATEADD(Orders[OrderDate], -1, YEAR)
            )
            RETURN DIVIDE(CurrentRevenue - PreviousRevenue, PreviousRevenue) ;;'''
        
        tokenizer = CopperTokenizer(source)
        tokens = tokenizer.get_tokens()
        
        dax_token = None
        for token in tokens:
            if token.type == TokenType.DAX_EXPRESSION:
                dax_token = token
                break
        
        self.assertIsNotNone(dax_token)
        self.assertIn("VAR CurrentRevenue", dax_token.value)
        self.assertIn("RETURN DIVIDE", dax_token.value)
    
    def test_comments(self):
        """Test comment parsing"""
        source = '''# This is a comment
        model: orders {
            # Another comment
        }'''
        
        tokenizer = CopperTokenizer(source)
        tokens = tokenizer.get_tokens()
        
        comment_tokens = [token for token in tokens if token.type == TokenType.COMMENT]
        self.assertEqual(len(comment_tokens), 2)
        self.assertEqual(comment_tokens[0].value, "This is a comment")
        self.assertEqual(comment_tokens[1].value, "Another comment")
    
    def test_keywords(self):
        """Test keyword recognition"""
        keywords = [
            ('model', TokenType.MODEL),
            ('dimension', TokenType.DIMENSION),
            ('measure', TokenType.MEASURE),
            ('view', TokenType.VIEW),
            ('string', TokenType.DIM_STRING),
            ('count', TokenType.MEAS_COUNT),
            ('left_outer', TokenType.JOIN_LEFT_OUTER),
            ('many_to_one', TokenType.REL_MANY_TO_ONE),
            ('usd', TokenType.FMT_USD),
            ('miles', TokenType.UNIT_MILES),
        ]
        
        for keyword, expected_type in keywords:
            with self.subTest(keyword=keyword):
                tokenizer = CopperTokenizer(keyword)
                tokens = tokenizer.get_tokens()
                self.assertEqual(tokens[0].type, expected_type)


class TestParser(unittest.TestCase):
    """Test the parser"""
    
    def test_simple_model(self):
        """Test parsing a simple model"""
        source = '''
        model: orders {
            dimension: order_id {
                type: string
                expression: Orders[OrderID] ;;
                primary_key: yes
            }
        }
        '''
        
        result = parse_string(source)
        self.assertTrue(result.success, f"Parse failed: {result.error}")
        
        program = result.ast
        self.assertEqual(len(program.statements), 1)
        
        model = program.statements[0]
        self.assertIsInstance(model, Model)
        self.assertEqual(model.name, "orders")
        self.assertEqual(len(model.dimensions), 1)
        
        dimension = model.dimensions[0]
        self.assertEqual(dimension.name, "order_id")
        self.assertEqual(dimension.type, "string")
        self.assertTrue(dimension.primary_key)
        self.assertIsInstance(dimension.expression, DaxExpression)
        self.assertEqual(dimension.expression.raw_text, "Orders[OrderID]")
    
    def test_model_with_measure(self):
        """Test parsing a model with measures"""
        source = '''
        model: orders {
            measure: total_revenue {
                type: sum
                expression: Orders[Amount] ;;
                value_format: usd
                label: "Total Revenue"
            }
        }
        '''
        
        result = parse_string(source)
        self.assertTrue(result.success)
        
        model = result.ast.statements[0]
        self.assertEqual(len(model.measures), 1)
        
        measure = model.measures[0]
        self.assertEqual(measure.name, "total_revenue")
        self.assertEqual(measure.type, "sum")
        self.assertEqual(measure.label, "Total Revenue")
        self.assertIsInstance(measure.value_format, FormatName)
        self.assertEqual(measure.value_format.name, "usd")
    
    def test_simple_view(self):
        """Test parsing a simple view"""
        source = '''
        view: sales_analysis {
            from: orders
            
            join: customers {
                type: left_outer
                relationship: many_to_one
                expression: Orders[CustomerID] = Customers[CustomerID] ;;
            }
        }
        '''
        
        result = parse_string(source)
        self.assertTrue(result.success, f"Parse failed: {result.error}")
        
        view = result.ast.statements[0]
        self.assertIsInstance(view, View)
        self.assertEqual(view.name, "sales_analysis")
        self.assertEqual(view.from_model, "orders")
        self.assertEqual(len(view.joins), 1)
        
        join = view.joins[0]
        self.assertEqual(join.name, "customers")
        self.assertEqual(join.type, "left_outer")
        self.assertEqual(join.relationship, "many_to_one")
        self.assertIsInstance(join.expression, DaxExpression)
    
    def test_view_with_extends(self):
        """Test parsing a view with extends"""
        source = '''
        view: retail_sales {
            extends: [base_sales]
            from: orders
        }
        '''
        
        result = parse_string(source)
        self.assertTrue(result.success)
        
        view = result.ast.statements[0]
        self.assertEqual(view.extends, ["base_sales"])
    
    def test_dimension_with_tiers(self):
        """Test parsing dimension with tiers"""
        source = '''
        model: orders {
            dimension: order_value_tier {
                type: tier
                expression: Orders[TotalAmount] ;;
                tiers: [0, 50, 200, 500, 1000]
            }
        }
        '''
        
        result = parse_string(source)
        self.assertTrue(result.success)
        
        dimension = result.ast.statements[0].dimensions[0]
        self.assertEqual(dimension.tiers, [0.0, 50.0, 200.0, 500.0, 1000.0])
    
    def test_string_tiers(self):
        """Test parsing dimension with string tiers"""
        source = '''
        model: customers {
            dimension: customer_tier {
                type: tier
                expression: SWITCH(TRUE(), ...) ;;
                tiers: ["Standard", "Premium", "VIP"]
            }
        }
        '''
        
        result = parse_string(source)
        self.assertTrue(result.success)
        
        dimension = result.ast.statements[0].dimensions[0]
        self.assertEqual(dimension.tiers, ["Standard", "Premium", "VIP"])
    
    def test_comments_in_model(self):
        """Test handling comments within models"""
        source = '''
        # Main model definition
        model: orders {
            # Primary key dimension
            dimension: order_id {
                type: string
                expression: Orders[OrderID] ;;
            }
            
            # Revenue measure
            measure: total_revenue {
                type: sum
                expression: Orders[Amount] ;;
            }
        }
        '''
        
        result = parse_string(source)
        self.assertTrue(result.success)
        
        # Should parse successfully despite comments
        model = result.ast.statements[0]
        self.assertEqual(len(model.dimensions), 1)
        self.assertEqual(len(model.measures), 1)
    
    def test_error_handling(self):
        """Test error handling for invalid syntax"""
        # Missing colon
        source = "model orders { }"
        result = parse_string(source)
        self.assertFalse(result.success)
        self.assertIsInstance(result.error, ParseError)
        
        # Unclosed brace
        source = "model: orders {"
        result = parse_string(source)
        self.assertFalse(result.success)
        
        # Invalid dimension type
        source = '''
        model: orders {
            dimension: test {
                type: invalid_type
            }
        }
        '''
        result = parse_string(source)
        self.assertFalse(result.success)
    
    def test_position_tracking(self):
        """Test that line/column positions are tracked correctly"""
        source = '''# Comment
        model: orders {
            dimension: order_id {
                type: string
            }
        }'''
        
        result = parse_string(source)
        self.assertTrue(result.success)
        
        model = result.ast.statements[0]
        # Model should be on line 2
        self.assertEqual(model.line, 2)
        
        dimension = model.dimensions[0]
        # Dimension should be on line 3
        self.assertEqual(dimension.line, 3)


class TestExampleFiles(unittest.TestCase):
    """Test parsing actual example files"""
    
    def setUp(self):
        """Set up test environment"""
        self.examples_dir = Path(__file__).parent.parent / "examples"
        self.assertTrue(self.examples_dir.exists(), "Examples directory not found")
    
    def test_parse_all_examples(self):
        """Test parsing all example .copper files"""
        copper_files = list(self.examples_dir.glob("*.copper"))
        self.assertGreater(len(copper_files), 0, "No .copper files found in examples/")
        
        for copper_file in copper_files:
            with self.subTest(file=copper_file.name):
                result = parse_file(copper_file)
                if not result.success:
                    print(f"\\nParse error in {copper_file.name}:")
                    print(f"  {result.error}")
                self.assertTrue(result.success, f"Failed to parse {copper_file.name}: {result.error}")
    
    def test_ecommerce_orders_example(self):
        """Test specific parsing of ecommerce_orders.copper"""
        file_path = self.examples_dir / "ecommerce_orders.copper"
        if not file_path.exists():
            self.skipTest("ecommerce_orders.copper not found")
        
        result = parse_file(file_path)
        self.assertTrue(result.success, f"Parse failed: {result.error}")
        
        # Should contain one model
        self.assertEqual(len(result.ast.statements), 1)
        
        model = result.ast.statements[0]
        self.assertIsInstance(model, Model)
        self.assertEqual(model.name, "orders")
        
        # Should have dimensions and measures
        self.assertGreater(len(model.dimensions), 0)
        self.assertGreater(len(model.measures), 0)
        
        # Check some specific dimensions
        dimension_names = [dim.name for dim in model.dimensions]
        self.assertIn("order_id", dimension_names)
        self.assertIn("customer_id", dimension_names)
        
        # Check some specific measures
        measure_names = [meas.name for meas in model.measures]
        self.assertIn("total_revenue", measure_names)
        self.assertIn("total_orders", measure_names)
    
    def test_sales_analysis_view_example(self):
        """Test specific parsing of sales_analysis_view.copper"""
        file_path = self.examples_dir / "sales_analysis_view.copper"
        if not file_path.exists():
            self.skipTest("sales_analysis_view.copper not found")
        
        result = parse_file(file_path)
        self.assertTrue(result.success, f"Parse failed: {result.error}")
        
        # Should contain one view
        self.assertEqual(len(result.ast.statements), 1)
        
        view = result.ast.statements[0]
        self.assertIsInstance(view, View)
        self.assertEqual(view.name, "sales_analysis")
        self.assertEqual(view.from_model, "orders")
        
        # Should have multiple joins
        self.assertGreater(len(view.joins), 0)
        
        # Check join names
        join_names = [join.name for join in view.joins]
        self.assertIn("customers", join_names)


class TestIntegration(unittest.TestCase):
    """Integration tests"""
    
    def test_round_trip_simple(self):
        """Test that we can parse and represent a simple structure"""
        source = '''
        model: test {
            dimension: id {
                type: string
                expression: Test[ID] ;;
                primary_key: yes
            }
            
            measure: count {
                type: count
                expression: Test[ID] ;;
            }
        }
        '''
        
        result = parse_string(source)
        self.assertTrue(result.success)
        
        # Verify the structure is correctly parsed
        model = result.ast.statements[0]
        self.assertEqual(model.name, "test")
        self.assertEqual(len(model.dimensions), 1)
        self.assertEqual(len(model.measures), 1)
        
        # Check dimension
        dim = model.dimensions[0]
        self.assertEqual(dim.name, "id")
        self.assertEqual(dim.type, "string")
        self.assertTrue(dim.primary_key)
        self.assertEqual(dim.expression.raw_text, "Test[ID]")
        
        # Check measure
        meas = model.measures[0]
        self.assertEqual(meas.name, "count")
        self.assertEqual(meas.type, "count")
        self.assertEqual(meas.expression.raw_text, "Test[ID]")
    
    def test_file_not_found(self):
        """Test handling of non-existent files"""
        result = parse_file("nonexistent.copper")
        self.assertFalse(result.success)
        self.assertIn("File not found", str(result.error))
    
    def test_invalid_file_extension(self):
        """Test handling of invalid file extensions"""
        # Create a temporary file with wrong extension
        import tempfile
        import os
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("model: test {}")
            temp_file = f.name
        
        try:
            result = parse_file(temp_file)
            self.assertFalse(result.success)
            self.assertIn("Expected .copper file", str(result.error))
        finally:
            os.unlink(temp_file)


def run_example_validation():
    """Run validation on all example files"""
    examples_dir = Path(__file__).parent.parent / "examples"
    if not examples_dir.exists():
        print("Examples directory not found")
        return False
    
    copper_files = list(examples_dir.glob("*.copper"))
    if not copper_files:
        print("No .copper files found in examples/")
        return False
    
    all_valid = True
    
    print(f"Validating {len(copper_files)} example files:")
    print("-" * 50)
    
    for copper_file in copper_files:
        result = parse_file(copper_file)
        if result.success:
            print(f"✓ {copper_file.name}")
            
            # Count statements
            models = sum(1 for stmt in result.ast.statements if isinstance(stmt, Model))
            views = sum(1 for stmt in result.ast.statements if isinstance(stmt, View))
            
            details = []
            if models > 0:
                details.append(f"{models} model{'s' if models != 1 else ''}")
            if views > 0:
                details.append(f"{views} view{'s' if views != 1 else ''}")
            
            if details:
                print(f"  ({', '.join(details)})")
        else:
            print(f"✗ {copper_file.name}")
            print(f"  Error: {result.error}")
            all_valid = False
    
    print("-" * 50)
    if all_valid:
        print("All example files parsed successfully!")
    else:
        print("Some files failed to parse.")
    
    return all_valid


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Test the Copper parser")
    parser.add_argument("--validate-examples", action="store_true",
                       help="Run validation on example files")
    parser.add_argument("--file", help="Parse a specific file")
    
    args = parser.parse_args()
    
    if args.validate_examples:
        run_example_validation()
    elif args.file:
        result = parse_file(args.file)
        if result.success:
            print(f"✓ Successfully parsed {args.file}")
            print(f"Found {len(result.ast.statements)} statements")
        else:
            print(f"✗ Parse error: {result.error}")
    else:
        # Run unit tests
        unittest.main(verbosity=2)