"""Reference analysis. Inputs, units and statistical assumptions are explicit."""

import numpy as np
from astropy import units as u
from scipy.optimize import curve_fit


def weighted_mean(values, errors):
    """Return mean and standard error for independent Gaussian measurements.

    Values and positive 1-sigma errors must be finite, matching 1-D arrays in
    the same units. Return plain numbers; the caller retains the unit.
    Correlated errors or intrinsic population scatter need a different model.
    """
    values = np.asarray(values, dtype=float)
    errors = np.asarray(errors, dtype=float)
    if values.ndim != 1 or values.size == 0 or values.shape != errors.shape:
        raise ValueError("Provide nonempty, matching one-dimensional arrays")
    if not np.all(np.isfinite(values)) or not np.all(np.isfinite(errors)):
        raise ValueError("Values and errors must be finite")
    if np.any(errors <= 0):
        raise ValueError("Standard errors must be positive")
    # Relative weights avoid overflowing 1 / sigma**2 for very small sigma.
    scale = errors.min()
    weights = (scale / errors) ** 2
    return float(np.average(values, weights=weights)), float(scale / np.sqrt(weights.sum()))


def usable_rows(table):
    """Finite rows with positive distances/errors; no survey cut is applied."""
    distance = table["distance"].to_value(u.Mpc)
    velocity = table["velocity"].to_value(u.km / u.s)
    error = table["velocity_error"].to_value(u.km / u.s)
    magnitude = np.asarray(table["apparent_magnitude"])
    return (np.isfinite(distance) & np.isfinite(velocity) & np.isfinite(error)
            & np.isfinite(magnitude) & (distance > 0) & (error > 0))


def velocity_model(distance_mpc, slope, intercept):
    """Toy low-redshift relation v = slope * distance + intercept."""
    return slope * distance_mpc + intercept


def fit_velocity(distance, velocity, error):
    """Weighted fit with exact x and known, independent Gaussian y errors.

    Accept Astropy quantities, convert to Mpc and km/s, and return numeric
    parameters [slope (km/s/Mpc), intercept (km/s)] and their covariance.
    No automatic masking, clipping, interpolation or unit guessing is done.
    """
    x = np.asarray(distance.to_value(u.Mpc), dtype=float)
    y = np.asarray(velocity.to_value(u.km / u.s), dtype=float)
    sigma = np.asarray(error.to_value(u.km / u.s), dtype=float)
    if x.ndim != 1 or x.size < 3 or x.shape != y.shape or x.shape != sigma.shape:
        raise ValueError("Need at least three matching one-dimensional measurements")
    if not all(np.all(np.isfinite(a)) for a in (x, y, sigma)) or np.any(sigma <= 0):
        raise ValueError("Measurements must be finite with positive standard errors")
    if np.unique(x).size < 2:
        raise ValueError("Need distinct distances to determine a slope")
    return curve_fit(velocity_model, x, y, sigma=sigma, absolute_sigma=True)
