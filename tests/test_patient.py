"""Tests for the Patient model."""

import numpy as np
import numpy.testing as npt
import pytest


def test_patient():
    """Test Patient class constructor."""
    from inflammation.models import Patient, Person

    alice = Patient('Alice')
    assert str(alice) == 'Alice'

    assert alice.last_observation is None
    alice.add_observation(42)
    assert alice.last_observation.value == 42
    alice.add_observation(32)
    assert alice.last_observation.value == 32
    assert isinstance(alice, Person)
