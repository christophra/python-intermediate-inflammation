"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.

    :param data: Inflammation values for M days as int array of shape (N, M)
    :returns: Daily mean, float array of size M
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.

    :param data: Inflammation values for M days as int array of shape (N, M)
    :returns: Daily maximum, int array of size M
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array.

    :param data: Inflammation values for M days as int array of shape (N, M)
    :returns: Daily minimum, int array of size M
    """
    return np.min(data, axis=0)

def patient_normalise(data):
    """Normalise patient data from a 2D inflammation data array."""
    max_data = np.nanmax(data, axis=1) # NaN values should not propagate
    max_data[max_data < 0] = 0 # negative values should be like zeros
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / max_data[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0 # NaN values, e.g. from div by 0 should map to 0
    normalised[normalised < 0] = 0 # "all entries should fall between 0 and 1"
    return normalised

def attach_names(data, names):
    """Attach patient names to each row of inflammation data.

    :param data: 2D array
    :param names: list of strings
    :returns: a list of dictionaries [{'name':_name, 'data':_data}]
    """
    if len(data) != len(names):
        raise ValueError("{} patients in data but got names for {} patients".format(
            len(data), len(names),
        ))

    return [{'name': _n, 'data':_d} for _n, _d in zip(names, data)]


class Observation:
    """One inflammation observation."""
    def __init__(self, day, value):
        self.day = day
        self.value = value

    def __str__(self):
        return str(self.value)


class Patient:
    """A patient in an inflammation study."""
    def __init__(self, name):
        self.name = name
        self.observations = []

    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1].day + 1

            except IndexError:
                day = 0

        new_observation = Observation(day, value)

        self.observations.append(new_observation)
        return new_observation

    @property
    def last_observation(self):
        try:
            return self.observations[-1]
        except IndexError:
            return None

    def __str__(self):
        return self.name
