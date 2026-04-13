import pytest
import numpy as np
from unittest.mock import patch
from simulations.model_outline import OracleNode

def test_read_capacity_failure():
    node = OracleNode(node_id=1, methodology_class="INSTITUTIONAL", accuracy=0.9, failure_rate=0.1)

    # Mock random to return a value less than failure_rate to trigger failure
    with patch("numpy.random.random", return_value=0.05):
        result = node.read_capacity(true_capacity=100.0)

    assert result is None
    assert node.is_active is False

def test_read_capacity_institutional_success():
    node = OracleNode(node_id=1, methodology_class="INSTITUTIONAL", accuracy=0.9, failure_rate=0.1)

    # random() > failure_rate, normal() returns 0.1
    with patch("numpy.random.random", return_value=0.5), \
         patch("numpy.random.normal", return_value=0.1) as mock_normal:

        result = node.read_capacity(true_capacity=100.0)

    assert result == pytest.approx(110.0)  # 100 * (1 + 0.1)
    assert node.is_active is True
    # Institutional noise should be normal(0, 1 - accuracy)
    mock_normal.assert_called_once_with(0, pytest.approx(0.1))

def test_read_capacity_cbpr_success():
    node = OracleNode(node_id=1, methodology_class="CBPR", accuracy=0.9, failure_rate=0.1)

    with patch("numpy.random.random", return_value=0.5), \
         patch("numpy.random.normal", return_value=0.1) as mock_normal:

        result = node.read_capacity(true_capacity=100.0)

    assert result == pytest.approx(110.0)
    assert node.is_active is True
    # CBPR noise should be normal(0, (1 - accuracy) * 1.5)
    mock_normal.assert_called_once_with(0, pytest.approx(0.15))

def test_read_capacity_physical_success():
    node = OracleNode(node_id=1, methodology_class="PHYSICAL", accuracy=0.9, failure_rate=0.1)

    with patch("numpy.random.random", return_value=0.5), \
         patch("numpy.random.normal", return_value=0.1) as mock_normal:

        result = node.read_capacity(true_capacity=100.0)

    assert result == pytest.approx(110.0)
    assert node.is_active is True
    # PHYSICAL noise should be normal(0, (1 - accuracy) * 0.5)
    mock_normal.assert_called_once_with(0, pytest.approx(0.05))

def test_read_capacity_capped_at_zero():
    node = OracleNode(node_id=1, methodology_class="INSTITUTIONAL", accuracy=0.9, failure_rate=0.1)

    # Return a very negative noise to make capacity drop below 0
    with patch("numpy.random.random", return_value=0.5), \
         patch("numpy.random.normal", return_value=-1.5):

        result = node.read_capacity(true_capacity=100.0)

    assert result == 0.0  # Cap at 0.0
    assert node.is_active is True
