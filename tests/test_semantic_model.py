import pytest
from src.semantic.schema import SemanticModel, Dimension, Measure, Relationship
from src.semantic.loader import SemanticModelLoader


def test_dimension_creation():
    """Test creating dimensions."""
    dim = Dimension(
        sql="Customers.region",
        type="string",
        description="Customer region"
    )
    assert dim.sql == "Customers.region"
    assert dim.type == "string"


def test_measure_creation():
    """Test creating measures."""
    measure = Measure(
        expression="SUM(Orders.total_amount)",
        type="currency",
        description="Total revenue"
    )
    assert measure.expression == "SUM(Orders.total_amount)"
    assert measure.type == "currency"


def test_relationship_creation():
    """Test creating relationships."""
    rel = Relationship(
        from_table="Orders",
        to_table="Customers",
        from_column="customer_id",
        to_column="id"
    )
    assert rel.from_table == "Orders"
    assert rel.to_table == "Customers"


def test_semantic_model_loader():
    """Test loading semantic model from dict."""
    model_def = {
        'name': 'test_model',
        'dimensions': {
            'region': {
                'sql': 'Customers.region',
                'type': 'string'
            }
        },
        'measures': {
            'revenue': {
                'expression': 'SUM(Orders.total_amount)',
                'type': 'currency'
            }
        },
        'relationships': [
            'Orders.customer_id → Customers.id'
        ]
    }
    
    model = SemanticModelLoader.load_from_dict(model_def)
    
    assert model.name == 'test_model'
    assert 'region' in model.dimensions
    assert 'revenue' in model.measures
    assert len(model.relationships) == 1
    
    # Test dimension retrieval
    region_dim = model.get_dimension('region')
    assert region_dim is not None
    assert region_dim.sql == 'Customers.region'
    
    # Test measure retrieval
    revenue_measure = model.get_measure('revenue')
    assert revenue_measure is not None
    assert revenue_measure.expression == 'SUM(Orders.total_amount)'


def test_relationship_string_parsing():
    """Test parsing relationship strings."""
    rel = SemanticModelLoader._parse_relationship_string('Orders.customer_id → Customers.id')
    
    assert rel.from_table == 'Orders'
    assert rel.from_column == 'customer_id'
    assert rel.to_table == 'Customers'
    assert rel.to_column == 'id'


def test_invalid_relationship_string():
    """Test invalid relationship string format."""
    with pytest.raises(ValueError):
        SemanticModelLoader._parse_relationship_string('invalid format')


def test_dimension_validation():
    """Test dimension validation."""
    # Should require either sql or expression
    with pytest.raises(ValueError):
        Dimension(type="string")