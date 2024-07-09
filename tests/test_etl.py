import pandas as pd
import pytest
from python.main import etl

def test_etl_valid_data():
    data = {
        'Date': ['2024-01-01', '2024-01-02'],
        'Network': ['Network1', 'Network2'],
        'Daily Active Users': [100, 150],
        'Subscription started': [5, 10],
        'Installs': [50, 100]
    }
    df = pd.DataFrame(data)
    most_active_networks, best_conversion_network = etl(df)

    assert not most_active_networks.empty
    assert not best_conversion_network.empty
    assert 'max_dau' in most_active_networks.columns
    assert 'conversion_rate' in best_conversion_network.columns

def test_etl_invalid_data():
    data = {
        'Date': ['2024-01-01', '2024-01-02'],
        'Network': ['Network1', 'Network2'],
        'Daily Active Users': [100, 'invalid'],
        'Subscription started': [5, 10],
        'Installs': [50, 100]
    }
    df = pd.DataFrame(data)
    with pytest.raises(Exception):
        etl(df)
