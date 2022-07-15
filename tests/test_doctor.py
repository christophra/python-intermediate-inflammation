"""Tests for the Doctor model."""

import numpy as np
import numpy.testing as npt
import pytest


def test_create_doctor():
    """Test Doctor class constructor"""
    from inflammation.models import Doctor
    name = 'JD'
    doc = Doctor(name)
    assert doc.name == name


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
