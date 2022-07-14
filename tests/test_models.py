"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [3, 4]),
    ]
)
def test_daily_mean(test, expected):
    """Test that mean function works for arrays of zeros and positive integers."""
    from inflammation.models import daily_mean
    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[6, 3], [5, 2], [4, 1]], [4, 1]),
        ([[6, 3, 1], [5, 2, 0], [4, 1, 1]], [4, 1, 0]),
        ([[6, 3, -1], [5, 2, 0], [4, 1, 1]], [4, 1, -1]),

    ]
)
def test_daily_min(test, expected):
    """Test that min function works for arrays of zeros, positive and negative integers."""
    from inflammation.models import daily_min
    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_min(np.array(test)), np.array(expected))


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[6, 3], [5, 2], [4, 1]], [6, 3]),
        ([[6, 3, 1], [5, 2, 0], [4, 1, 1]], [6, 3, 1]),
        ([[6, 3, -1], [5, 2, 0], [4, 1, 1]], [6, 3, 1]),
    ]
)
def test_daily_max(test, expected):
    """Test that max function works for arrays of zeros, positive and negative integers."""
    from inflammation.models import daily_max
    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))


def test_daily_min_string():
    """Test for TypeError when passing strings"""
    from inflammation.models import daily_min

    with pytest.raises(TypeError):
        error_expected = daily_min([["Wadde", "hadde"], ["dudde", "da"]])

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]],
         [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]],
         [[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
        ([[1, 1, -1], [1, -1, -1], [-1, -1, -1]],
         [[1, 1, 0], [1, 0, 0], [0, 0, 0]]),
        ([[1, 1, -1], [1, -1, -1], [-1, -1, -1]],
         [[1, 1, 0], [1, 0, 0], [0, 0, 0]]),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
         [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]]),
        ([[float('nan'), 2, 3], [4, 5, float('nan')], [float('nan'), float('nan'), float('nan')]],
         [[0, 0.67, 1], [0.8, 1, 0], [0, 0, 0]]),
    ]
)
def test_patient_normalise(test, expected):
    """Test normalisation works for arrays of one and positive integers.
       Assumption that test accuracy of two decimal places is sufficient."""
    from inflammation.models import patient_normalise
    npt.assert_almost_equal(patient_normalise((np.array(test))), np.array(expected), decimal=2)

def test_observation():
    """Test Observation class constructor."""
    from inflammation.models import Observation
    obs = Observation(1, 42)
    assert obs.day == 1
    assert obs.value == 42


def test_person():
    """Test Person class constructor."""
    from inflammation.models import Person
    alice = Person('Alice')
    assert str(alice) == 'Alice'

    with pytest.raises(AttributeError):
        alice.add_observation(3)

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


def test_create_doctor():
    """Test Doctor class constructor"""
    from inflammation.models import Doctor
    name = 'JD'
    doc = Doctor(name)
    assert doc.name == name
    assert isinstance()


def test_doctor_is_person():
    """Test if a doctor is a person"""
    from inflammation.models import Doctor, Person
    doc = Doctor("Elliot Reid")
    assert isinstance(doc, Person)


def test_patients_added_correctly():
    """Check patients are being added correctly by a doctor. """
    from inflammation.models import Doctor, Patient
    doc = Doctor("Sheila Wheels")
    alice = Patient("Alice")
    doc.add_patient(alice)
    assert doc.patients is not None
    assert len(doc.patients) == 1
    assert doc["Alice"] is not None


def test_no_duplicate_patients():
    """Check adding the same patient to the same doctor twice does not result in duplicates. """
    from inflammation.models import Doctor, Patient
    doc = Doctor("Sheila Wheels")
    alice = Patient("Alice")
    doc.add_patient(alice)
    doc.add_patient(alice)
    assert len(doc.patients) == 1
