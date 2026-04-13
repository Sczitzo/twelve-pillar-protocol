import pytest
import numpy as np
from unittest.mock import patch, MagicMock

from simulations.model_outline import OracleNode, OracleSubsystem, CONFIG

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


@pytest.fixture
def subsystem():
    # Initialize with default config
    sys = OracleSubsystem(CONFIG)
    # Clear the nodes so we can explicitly define them for testing
    sys.nodes = []
    sys.failure_log = []
    return sys

def create_mock_node(reading):
    node = MagicMock()
    node.read_capacity.return_value = reading
    return node

def test_consensus_lc_success_majority(subsystem):
    """Test majority consensus (LC) succeeds with sufficient quorum."""
    # 3 nodes: majority quorum is (3 // 2) + 1 = 2
    subsystem.nodes = [
        create_mock_node(100.0),
        create_mock_node(110.0),
        create_mock_node(None)
    ]

    # Valid readings are 100.0 and 110.0. Median is 105.0.
    result = subsystem.get_consensus_capacity(100.0, consensus_type="LC")

    assert result == 105.0
    assert len(subsystem.failure_log) == 0

def test_consensus_lc_failure_quorum(subsystem):
    """Test majority consensus (LC) fails when valid readings are below quorum."""
    # 3 nodes: majority quorum is 2
    subsystem.nodes = [
        create_mock_node(100.0),
        create_mock_node(None),
        create_mock_node(None)
    ]

    result = subsystem.get_consensus_capacity(100.0, consensus_type="LC")

    assert result is None
    assert len(subsystem.failure_log) == 1
    assert subsystem.failure_log[0] == {"type": "QUORUM_FAILURE", "valid": 1}

def test_consensus_sq_success_supermajority(subsystem):
    """Test supermajority consensus (SQ) succeeds with sufficient quorum."""
    # 3 nodes: supermajority quorum is ceil(2*3/3) = 2
    # Let's test with 4 nodes where SQ is ceil(8/3) = 3
    subsystem.nodes = [
        create_mock_node(100.0),
        create_mock_node(110.0),
        create_mock_node(120.0),
        create_mock_node(None)
    ]

    # Valid readings: 100, 110, 120. Median is 110.0
    result = subsystem.get_consensus_capacity(100.0, consensus_type="SQ")

    assert result == 110.0
    assert len(subsystem.failure_log) == 0

def test_consensus_sq_failure_quorum(subsystem):
    """Test supermajority consensus (SQ) fails when valid readings are below quorum."""
    # 4 nodes: supermajority quorum is ceil(8/3) = 3
    subsystem.nodes = [
        create_mock_node(100.0),
        create_mock_node(110.0),
        create_mock_node(None),
        create_mock_node(None)
    ]

    result = subsystem.get_consensus_capacity(100.0, consensus_type="SQ")

    assert result is None
    assert len(subsystem.failure_log) == 1
    assert subsystem.failure_log[0] == {"type": "QUORUM_FAILURE", "valid": 2}

def test_consensus_zero_valid_readings(subsystem):
    """Test consensus failure with zero valid readings."""
    subsystem.nodes = [
        create_mock_node(None),
        create_mock_node(None),
        create_mock_node(None)
    ]

    result = subsystem.get_consensus_capacity(100.0, consensus_type="LC")

    assert result is None
    assert len(subsystem.failure_log) == 1
    assert subsystem.failure_log[0] == {"type": "QUORUM_FAILURE", "valid": 0}

def test_consensus_odd_number_median(subsystem):
    """Test median calculation with an odd number of valid readings."""
    subsystem.nodes = [
        create_mock_node(10.0),
        create_mock_node(20.0),
        create_mock_node(30.0)
    ]

    result = subsystem.get_consensus_capacity(100.0, consensus_type="LC")

    assert result == 20.0

def test_consensus_even_number_median(subsystem):
    """Test median calculation with an even number of valid readings."""
    subsystem.nodes = [
        create_mock_node(10.0),
        create_mock_node(20.0),
        create_mock_node(30.0),
        create_mock_node(40.0)
    ]

    result = subsystem.get_consensus_capacity(100.0, consensus_type="LC")

    # Median of 10, 20, 30, 40 is 25.0
    assert result == 25.0
