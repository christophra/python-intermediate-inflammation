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