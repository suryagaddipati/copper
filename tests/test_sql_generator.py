import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from executors.sql_generator import SQLGenerator
from semantic.schema import SemanticModel, Dimension, Measure, DataSource, Relationship
from query.builder import Query


class TestSQLGenerator(unittest.TestCase):
    
    def setUp(self):
        self.model = SemanticModel(
            name="test_model",
            datasources={
                'orders': DataSource(
                    type='table',
                    database='analytics',
                    schema='public',
                    table='orders'
                ),
                'customers': DataSource(
                    type='table',
                    database='analytics', 
                    schema='public',
                    table='customers'
                )
            },
            dimensions={
                'customer_name': Dimension(
                    expression='customers.name',
                    type='string'
                ),
                'order_date': Dimension(
                    expression='orders.order_date',
                    type='date'
                ),
                'order_year': Dimension(
                    expression='YEAR(orders.order_date)',
                    type='number'
                )
            },
            measures={
                'total_orders': Measure(
                    expression='COUNT(orders.id)',
                    type='number'
                ),
                'total_amount': Measure(
                    expression='SUM(orders.amount)',
                    type='number'
                ),
                'avg_amount': Measure(
                    expression='AVG(orders.amount)',
                    type='number'
                )
            },
            relationships=[
                Relationship(
                    **{'from': 'orders', 'to': 'customers'},
                    from_column='customer_id',
                    to_column='id'
                )
            ]
        )
        self.generator = SQLGenerator(self.model)
    
    def test_simple_dimension_query(self):
        query = Query(self.model).dimensions(['customer_name'])
        sql = self.generator.generate(query)
        
        expected_lines = [
            "SELECT",
            "  customers.name AS customer_name",
            "FROM", 
            "  analytics.public.customers"
        ]
        
        self.assertEqual(sql, "\n".join(expected_lines))
    
    def test_simple_measure_query(self):
        query = Query(self.model).measures(['total_orders'])
        sql = self.generator.generate(query)
        
        expected_lines = [
            "SELECT",
            "  COUNT(orders.id) AS total_orders",
            "FROM",
            "  analytics.public.orders"
        ]
        
        self.assertEqual(sql, "\n".join(expected_lines))
    
    def test_dimension_and_measure_query(self):
        query = Query(self.model).dimensions(['customer_name']).measures(['total_orders'])
        sql = self.generator.generate(query)
        
        expected_lines = [
            "SELECT",
            "  customers.name AS customer_name,",
            "  COUNT(orders.id) AS total_orders",
            "FROM",
            "  analytics.public.orders",
            "  LEFT JOIN analytics.public.customers",
            "    ON orders.customer_id = customers.id",
            "GROUP BY",
            "  customers.name"
        ]
        
        self.assertEqual(sql, "\n".join(expected_lines))
    
    def test_multiple_dimensions_and_measures(self):
        query = Query(self.model)\
            .dimensions(['customer_name', 'order_year'])\
            .measures(['total_orders', 'total_amount'])
        
        sql = self.generator.generate(query)
        
        expected_lines = [
            "SELECT",
            "  customers.name AS customer_name,",
            "  EXTRACT(YEAR FROM orders.order_date) AS order_year,",
            "  COUNT(orders.id) AS total_orders,",
            "  SUM(orders.amount) AS total_amount",
            "FROM",
            "  analytics.public.orders",
            "  LEFT JOIN analytics.public.customers",
            "    ON orders.customer_id = customers.id",
            "GROUP BY",
            "  customers.name,",
            "  EXTRACT(YEAR FROM orders.order_date)"
        ]
        
        self.assertEqual(sql, "\n".join(expected_lines))
    
    def test_query_with_filters_manual(self):
        """Test filters by manually setting them to avoid ANTLR dependency."""
        query = Query(self.model).dimensions(['customer_name']).measures(['total_orders'])
        
        # Manually set filters to avoid ANTLR parsing
        query._filters = ['orders.amount > 100', 'customers.region = "West"']
        
        sql = self.generator.generate(query)
        
        expected_lines = [
            "SELECT",
            "  customers.name AS customer_name,",
            "  COUNT(orders.id) AS total_orders",
            "FROM",
            "  analytics.public.orders",
            "  LEFT JOIN analytics.public.customers",
            "    ON orders.customer_id = customers.id",
            "WHERE",
            "  orders.amount > 100",
            "  AND   customers.region = \"West\"",
            "GROUP BY",
            "  customers.name"
        ]
        
        self.assertEqual(sql, "\n".join(expected_lines))
    
    def test_function_mappings(self):
        query = Query(self.model).measures(['avg_amount'])
        sql = self.generator.generate(query)
        
        self.assertIn("AVG(orders.amount)", sql)
    
    def test_date_function_conversion(self):
        query = Query(self.model).dimensions(['order_year'])
        sql = self.generator.generate(query)
        
        self.assertIn("EXTRACT(YEAR FROM orders.order_date)", sql)
    
    def test_table_reference_building(self):
        generator = SQLGenerator(self.model)
        datasource = self.model.get_datasource('orders')
        
        table_ref = generator._build_table_reference('orders', datasource)
        self.assertEqual(table_ref, 'analytics.public.orders')
    
    def test_table_alias_creation(self):
        model_with_alias = SemanticModel(
            name="alias_test",
            datasources={
                'ord': DataSource(
                    type='table',
                    table='order_table'
                )
            }
        )
        
        generator = SQLGenerator(model_with_alias)
        datasource = model_with_alias.get_datasource('ord')
        
        table_ref = generator._build_table_reference('ord', datasource)
        self.assertEqual(table_ref, 'order_table AS ord')
    
    def test_required_tables_extraction(self):
        query = Query(self.model)\
            .dimensions(['customer_name', 'order_date'])\
            .measures(['total_orders'])
        
        required_tables = self.generator._get_required_tables(query)
        
        self.assertIn('customers', required_tables)
        self.assertIn('orders', required_tables)
    
    def test_table_names_from_expression(self):
        expression = "orders.amount + customers.discount"
        tables = self.generator._extract_table_names_from_expression(expression)
        
        self.assertEqual(set(tables), {'orders', 'customers'})
    
    def test_no_from_clause_when_no_tables(self):
        empty_model = SemanticModel(name="empty")
        generator = SQLGenerator(empty_model)
        
        query = Query(empty_model)
        from_clause = generator._build_from_clause(query)
        
        self.assertEqual(from_clause, "")
    
    def test_no_where_clause_when_no_filters(self):
        query = Query(self.model).dimensions(['customer_name'])
        where_clause = self.generator._build_where_clause(query)
        
        self.assertIsNone(where_clause)
    
    def test_no_group_by_when_dimensions_only(self):
        query = Query(self.model).dimensions(['customer_name'])
        group_by_clause = self.generator._build_group_by_clause(query)
        
        self.assertIsNone(group_by_clause)
    
    def test_no_group_by_when_measures_only(self):
        query = Query(self.model).measures(['total_orders'])
        group_by_clause = self.generator._build_group_by_clause(query)
        
        self.assertIsNone(group_by_clause)
    
    def test_expression_conversion(self):
        expression = "COUNT(orders.id) + SUM(orders.amount)"
        converted = self.generator._convert_expression_to_sql(expression)
        
        self.assertEqual(converted, "COUNT(orders.id) + SUM(orders.amount)")
    
    def test_case_expression_formatting(self):
        expression = "CASE WHEN orders.amount > 100 THEN 'high' ELSE 'low' END"
        converted = self.generator._convert_expression_to_sql(expression)
        
        expected = "CASE\n    WHEN orders.amount > 100 THEN\n      'high'\n    ELSE\n      'low'\n  END"
        self.assertEqual(converted, expected)
    
    def test_postgresql_dialect(self):
        generator = SQLGenerator(self.model, dialect="postgresql")
        self.assertEqual(generator.dialect, "postgresql")
    
    def test_convenience_function(self):
        from executors.sql_generator import generate_sql
        
        query = Query(self.model).dimensions(['customer_name'])
        sql = generate_sql(query)
        
        self.assertIsInstance(sql, str)
        self.assertIn("SELECT", sql)
        self.assertIn("customers.name", sql)


class TestSQLGeneratorComplexScenarios(unittest.TestCase):
    
    def setUp(self):
        self.model = SemanticModel(
            name="complex_model",
            datasources={
                'orders': DataSource(type='table', table='orders'),
                'customers': DataSource(type='table', table='customers'),
                'products': DataSource(type='table', table='products'),
                'order_items': DataSource(type='table', table='order_items')
            },
            dimensions={
                'customer_name': Dimension(expression='customers.name', type='string'),
                'product_name': Dimension(expression='products.name', type='string'),
                'order_month': Dimension(expression='MONTH(orders.order_date)', type='number')
            },
            measures={
                'revenue': Measure(expression='SUM(order_items.price * order_items.quantity)', type='number'),
                'order_count': Measure(expression='COUNT(DISTINCT orders.id)', type='number')
            },
            relationships=[
                Relationship(**{'from': 'orders', 'to': 'customers'}, from_column='customer_id', to_column='id'),
                Relationship(**{'from': 'order_items', 'to': 'orders'}, from_column='order_id', to_column='id'),
                Relationship(**{'from': 'order_items', 'to': 'products'}, from_column='product_id', to_column='id')
            ]
        )
        self.generator = SQLGenerator(self.model)
    
    def test_multi_table_join_query(self):
        query = Query(self.model)\
            .dimensions(['customer_name', 'product_name'])\
            .measures(['revenue'])
        
        sql = self.generator.generate(query)
        
        # The SQL generator should include the tables needed for the query
        self.assertIn("customers", sql)
        self.assertIn("products", sql) 
        self.assertIn("order_items", sql)
        self.assertIn("GROUP BY", sql)
        # Note: JOIN logic may vary based on implementation
    
    def test_complex_measure_expression(self):
        query = Query(self.model).measures(['revenue'])
        sql = self.generator.generate(query)
        
        self.assertIn("SUM(order_items.price * order_items.quantity)", sql)
    
    def test_date_function_extraction(self):
        query = Query(self.model).dimensions(['order_month'])
        sql = self.generator.generate(query)
        
        self.assertIn("EXTRACT(MONTH FROM orders.order_date)", sql)


if __name__ == '__main__':
    unittest.main()