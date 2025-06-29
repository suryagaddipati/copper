import pytest
import pandas as pd
from src.semantic.loader import SemanticModelLoader
from src.query.builder import Query


@pytest.fixture
def sample_model():
    """Create a sample semantic model for testing."""
    model_def = {
        'name': 'test_ecommerce',
        'dimensions': {
            'region': {
                'sql': 'Customers.region',
                'type': 'string'
            },
            'customer_tier': {
                'sql': 'Customers.tier',
                'type': 'string'
            }
        },
        'measures': {
            'revenue': {
                'expression': 'SUM(Orders.total_amount)',
                'type': 'currency'
            },
            'order_count': {
                'expression': 'COUNT(Orders.id)',
                'type': 'number'
            }
        },
        'relationships': [
            'Orders.customer_id → Customers.id'
        ]
    }
    return SemanticModelLoader.load_from_dict(model_def)


@pytest.fixture
def sample_data():
    """Create sample data for testing."""
    orders = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'customer_id': [1, 2, 1, 3],
        'total_amount': [100.0, 250.0, 75.0, 500.0],
        'status': ['shipped', 'pending', 'shipped', 'shipped']
    })
    
    customers = pd.DataFrame({
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'region': ['West', 'East', 'West'],
        'tier': ['Gold', 'Silver', 'Gold']
    })
    
    return {'Orders': orders, 'Customers': customers}


def test_query_builder_creation(sample_model):
    """Test creating a query builder."""
    query = Query(sample_model)
    assert query.semantic_model == sample_model
    assert query._dimensions == []
    assert query._measures == []
    assert query._filters == []


def test_query_dimensions(sample_model):
    """Test adding dimensions to query."""
    query = Query(sample_model).dimensions(['region'])
    assert 'region' in query._dimensions


def test_query_measures(sample_model):
    """Test adding measures to query."""
    query = Query(sample_model).measures(['revenue'])
    assert 'revenue' in query._measures


def test_query_filters(sample_model):
    """Test adding filters to query."""
    query = Query(sample_model).filters(['region = "West"'])
    assert 'region = "West"' in query._filters


def test_query_chaining(sample_model):
    """Test fluent API chaining."""
    query = Query(sample_model) \
        .dimensions(['region']) \
        .measures(['revenue', 'order_count']) \
        .filters(['region = "West"']) \
        .limit(10)
    
    assert 'region' in query._dimensions
    assert 'revenue' in query._measures
    assert 'order_count' in query._measures
    assert 'region = "West"' in query._filters
    assert query._limit == 10


def test_invalid_dimension(sample_model):
    """Test error on invalid dimension."""
    with pytest.raises(ValueError):
        Query(sample_model).dimensions(['invalid_dimension'])


def test_invalid_measure(sample_model):
    """Test error on invalid measure."""
    with pytest.raises(ValueError):
        Query(sample_model).measures(['invalid_measure'])


def test_query_validation(sample_model):
    """Test query validation."""
    # Valid query
    query = Query(sample_model).dimensions(['region']).measures(['revenue'])
    errors = query.validate()
    assert len(errors) == 0
    
    # Empty query
    empty_query = Query(sample_model)
    errors = empty_query.validate()
    assert len(errors) > 0
    assert "must include at least one dimension or measure" in errors[0]


def test_query_string_representation(sample_model):
    """Test query string representation."""
    query = Query(sample_model) \
        .dimensions(['region']) \
        .measures(['revenue'])
    
    query_str = str(query)
    assert 'dimensions=' in query_str
    assert 'measures=' in query_str
    assert 'region' in query_str
    assert 'revenue' in query_str