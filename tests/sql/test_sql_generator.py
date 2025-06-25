#!/usr/bin/env python3
import unittest

from src.parser.antlr_parser import validate_copper_syntax
from src.sql.sql_generator import SQLGenerator


class TestSQLGenerator(unittest.TestCase):
    
    def test_simple_view_sql(self):
        copper_code = """model: orders {
  dimension: order_id {
    type: string
  }
  dimension: amount {
    type: number
  }
}

view: orders_view {
  from: orders
}"""
        
        result = validate_copper_syntax(copper_code)
        self.assertTrue(result['valid'], f"Parser failed: {result['errors']}")
        
        generator = SQLGenerator(result)
        sql = generator.generate_view_sql("orders_view")
        
        expected_lines = [
            "SELECT",
            "  orders.order_id,",
            "  orders.amount",
            "FROM orders"
        ]
        
        for line in expected_lines:
            self.assertIn(line, sql)
        
        print("✅ Simple view SQL test passed!")
    
    def test_model_with_multiple_dimensions(self):
        copper_code = """model: customers {
  dimension: customer_id {
    type: string
  }
  dimension: name {
    type: string
  }
  dimension: email {
    type: string
  }
  dimension: age {
    type: number
  }
}

view: customer_view {
  from: customers
}"""
        
        result = validate_copper_syntax(copper_code)
        self.assertTrue(result['valid'], f"Parser failed: {result['errors']}")
        
        generator = SQLGenerator(result)
        sql = generator.generate_view_sql("customer_view")
        
        # Check that all dimensions are included
        self.assertIn("customers.customer_id", sql)
        self.assertIn("customers.name", sql)
        self.assertIn("customers.email", sql)
        self.assertIn("customers.age", sql)
        self.assertIn("FROM customers", sql)
        
        print("✅ Multiple dimensions test passed!")
    
    def test_view_not_found(self):
        copper_code = """model: orders {
  dimension: order_id {
    type: string
  }
}

view: orders_view {
  from: orders
}"""
        
        result = validate_copper_syntax(copper_code)
        generator = SQLGenerator(result)
        
        with self.assertRaises(ValueError) as context:
            generator.generate_view_sql("nonexistent_view")
        
        self.assertIn("View 'nonexistent_view' not found", str(context.exception))
        
        print("✅ View not found error test passed!")
    
    def test_model_not_found(self):
        copper_code = """view: invalid_view {
  from: nonexistent_model
}"""
        
        result = validate_copper_syntax(copper_code)
        generator = SQLGenerator(result)
        
        with self.assertRaises(ValueError) as context:
            generator.generate_view_sql("invalid_view")
        
        self.assertIn("Model 'nonexistent_model' not found", str(context.exception))
        
        print("✅ Model not found error test passed!")
    
    def test_view_without_from(self):
        result = {
            'valid': True,
            'models': [],
            'views': [{
                'name': 'bad_view',
                'type': 'view',
                'properties': {},  # No 'from' property
                'children': []
            }]
        }
        
        from src.parser.antlr_parser import ParsedNode, NodeType
        
        view_node = ParsedNode(
            type=NodeType.VIEW,
            name='bad_view',
            properties={},
            children=[],
            line_number=1
        )
        
        result['views'] = [view_node]
        
        generator = SQLGenerator(result)
        
        with self.assertRaises(ValueError) as context:
            generator.generate_view_sql("bad_view")
        
        self.assertIn("has no 'from' property", str(context.exception))
        
        print("✅ View without 'from' error test passed!")


if __name__ == '__main__':
    unittest.main()