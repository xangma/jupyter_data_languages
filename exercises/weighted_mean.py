"""Deliberately incorrect classroom starter; excluded from the passing suite."""
import numpy as np


def weighted_mean(values, errors):
    """Return the mean of measurements (BUG: ignores measurement errors)."""
    return float(np.mean(values))
