"""Run explicitly: python -m pytest exercises/test_weighted_mean.py -q."""
import pytest
from weighted_mean import weighted_mean


@pytest.mark.parametrize("errors, expected", [([1, 3], 1.2), ([3, 1], 2.8)])
def test_analytical_answers(errors, expected):
    assert weighted_mean([1, 3], errors) == pytest.approx(expected)


def test_error_rescaling():
    assert weighted_mean([1, 3], [2, 6]) == pytest.approx(1.2)


@pytest.mark.parametrize("values, errors", [([], []), ([1, 2], [1]),
    ([1], [0]), ([1], [-1]), ([float("nan")], [1]), ([1], [float("inf")])])
def test_invalid_measurements(values, errors):
    with pytest.raises(ValueError):
        weighted_mean(values, errors)
