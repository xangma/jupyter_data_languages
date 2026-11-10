import numpy as np
import pytest
from astropy import units as u
from astropy.table import QTable
from pathlib import Path
from course2026.analysis import fit_velocity, usable_rows, weighted_mean


@pytest.mark.parametrize("errors, expected", [([1, 3], 1.2), ([3, 1], 2.8)])
def test_known_weighted_means(errors, expected):
    mean, error = weighted_mean([1, 3], errors)
    assert mean == pytest.approx(expected)
    assert error == pytest.approx(np.sqrt(0.9))


def test_equal_errors_and_rescaling():
    assert weighted_mean([1, 3], [2, 2]) == pytest.approx((2, np.sqrt(2)))
    mean, error = weighted_mean([1, 3], [2, 6])
    assert mean == pytest.approx(1.2)
    assert error == pytest.approx(2 * np.sqrt(0.9))


@pytest.mark.parametrize("values, errors", [([], []), ([1, 2], [1]),
    ([[1, 2]], [[1, 2]]), ([1], [0]), ([1], [-1]),
    ([np.nan], [1]), ([1], [np.inf])])
def test_invalid_mean_inputs(values, errors):
    with pytest.raises(ValueError):
        weighted_mean(values, errors)


def test_exact_line_and_unit_conversion():
    x = np.arange(1, 7) * u.Mpc
    y = (70 * x.value + 300) * u.km / u.s
    p, cov = fit_velocity(x.to(u.kpc), y.to(u.m / u.s), np.ones(6) * u.km / u.s)
    np.testing.assert_allclose(p, [70, 300], atol=1e-8)
    assert cov.shape == (2, 2)
    assert np.all(np.linalg.eigvalsh(cov) > 0)


def test_incompatible_units_are_rejected():
    with pytest.raises(u.UnitConversionError):
        fit_velocity(np.arange(4) * u.s, np.arange(4) * u.km / u.s, np.ones(4) * u.km / u.s)


def test_catalogue_recovery_and_selection():
    table = QTable.read(Path(__file__).parents[1] / "data" / "mock_galaxies.ecsv")
    mask = usable_rows(table)
    assert 0 < mask.sum() < len(table)
    p, cov = fit_velocity(table["distance"][mask], table["velocity"][mask], table["velocity_error"][mask])
    truth = np.array([table.meta["slope"], table.meta["intercept"]])
    assert np.all(np.abs(p - truth) < 4 * np.sqrt(np.diag(cov)))
    selected = mask & (table["apparent_magnitude"] < 16.5)
    assert 0 < selected.sum() < mask.sum()
    assert table["distance"][selected].mean() < table["distance"][mask].mean()


@pytest.mark.parametrize("x,y,sigma", [([1, 2], [1, 2], [1, 1]),
    ([1, 1, 1], [1, 2, 3], [1, 1, 1]), ([1, 2, 3], [1, np.nan, 3], [1, 1, 1]),
    ([1, 2, 3], [1, 2, 3], [1, 0, 1])])
def test_invalid_fit_inputs(x, y, sigma):
    with pytest.raises(ValueError):
        fit_velocity(np.array(x) * u.Mpc, np.array(y) * u.km / u.s, np.array(sigma) * u.km / u.s)
