# Hints and worked answers

Attempt the tasks first. More than one implementation may satisfy a contract;
you must still explain the scientific expectation.

## Primer

```python
def positive_finite(values):
    values = np.asarray(values)
    return values[np.isfinite(values) & (values > 0)]
```

The supplied answer is `[1, 3]`. Replacing a missing measurement with zero invents
an observed value and can shift summaries.

## Session 1

Task A: `np.count_nonzero(~np.isfinite(velocity))` gives 3 and
`np.count_nonzero(sigma <= 0)` gives 1. The missing magnitude explains the fifth
invalid row. Apply the same mask to aligned columns. `[:, None]` turns `(N,)`
into `(N, 1)`, allowing one scale to broadcast across each row.

Task B: the FITS example preserves three physical columns and units, omitting
arbitrary ECSV metadata and other columns. An explicit conversion remains correct
when a file uses compatible units with a different scale.

Task C caption: “Counts and normalised distance distributions for 395 usable
synthetic objects and the subset with apparent magnitude below 16.5, using common
bin edges. Invalid measurements were removed with one shared mask. The brighter
subset favours nearby objects; this is not a real completeness estimate or a
measurement of the Hubble constant.”

The toy slope need not be biased by the cut: it does not select on velocity
residuals at fixed distance. Real distance errors, correlations or selection on
the fitted observable can change this conclusion.

With the shared valid-row mask, magnitude cuts of 15.5, 16.5 and 17.5 select
161, 262 and 357 objects respectively.

## Session 2

```python
def test_equal_bearings():
    assert angle_distance(42, 42) == 0

def test_opposite_bearings():
    assert angle_distance(0, 180) == 180
```

A conflict resolution can say: “Angles are in degrees and the helper returns
their shortest separation.” Staging selects the next commit's content; committing
records it locally; pushing sends it to a configured remote. A PR adds review
and discussion around a proposed branch change.

With the deliberate `abs(b - a)` bug, `test_wraparound` gets 358 instead of 2
and `test_full_turns` gets 630 instead of 90. The small-angle, equal-angle and
180-degree tests still pass. `git diff -- angle.py` is empty after restoring
the correct formula; the new tests are committed on `edge-case-tests`.

## Session 3

The agent client, its model and its execution environment are different things.
An enforced sandbox restricts processes; approval rules control actions; Git or
tool checkpoints preserve review/recovery history. Planning instructions, a
branch and a virtual environment do not create a security boundary. A Cline
client on a laptop still edits that laptop's workspace when inference uses CPD.

A useful plan identifies the scalar interface, invalid inputs, inverse-variance
weights, permitted file and focused test command. Students own expected answers;
the agent may translate them into test syntax. Preserve the reviewed tests
checkpoint during repair. Reject changing `1.2` to `1.5` to match wrong code,
weakening assertions, or returning a tuple for the scalar contract. A corrective
follow-up names the mismatch, retains the agreed expectation and asks for a
bounded implementation change with actual test evidence.

Doubling all error bars leaves the fitted parameters unchanged, doubles their
standard errors and divides reduced chi-squared by four with `absolute_sigma=True`.

For example, measurements `[2, 10]` with errors `[1, 2]` have relative weights
`[1, 1/4]`, giving `(2 + 10/4) / (1 + 1/4) = 3.6`. Students should choose and
derive their own example before opening this answer. Possible additions in
`test_student_checks.py` are:

```python
import pytest
from weighted_mean import weighted_mean

def test_independent_unequal_errors():
    assert weighted_mean([2, 10], [1, 2]) == pytest.approx(3.6)

def test_equal_errors():
    assert weighted_mean([1, 3], [2, 2]) == pytest.approx(2.0)

def test_rejects_two_dimensions():
    with pytest.raises(ValueError):
        weighted_mean([[1, 3]], [[1, 3]])
```

Commit the agreed tests before the repair and keep them unchanged during it.

A scalar-only solution for the practice workspace is:

```python
import numpy as np

def weighted_mean(values, errors):
    values = np.asarray(values, dtype=float)
    errors = np.asarray(errors, dtype=float)
    if values.ndim != 1 or values.size == 0 or values.shape != errors.shape:
        raise ValueError("Need nonempty matching 1-D arrays")
    if not np.all(np.isfinite(values)) or not np.all(np.isfinite(errors)):
        raise ValueError("Measurements must be finite")
    if np.any(errors <= 0):
        raise ValueError("Standard errors must be positive")
    weights = (errors.min() / errors) ** 2
    return float(np.average(values, weights=weights))
```

Relative weights preserve inverse-variance ratios without directly forming
`1 / sigma**2`. Known means: 1.2 and 2.8; common standard error: `sqrt(0.9)`.
Equal-error tests cannot distinguish ordinary, inverse-error and inverse-variance
means. Tests do not establish that the measurements really share a true value or
have independent Gaussian errors.

An AI-use record should name the actual tool/model and execution host, tests
checkpoint, a real steering/review decision, independently derived example and
observed before/after test results. For example: “I asked the agent to preserve
the scalar API, reviewed its proposed tests against my derivation, then allowed
the focused pytest command in the practice folder. I reran the tests and checked
the diff. The agent did not choose the statistical model.” State when no AI
tool was used instead; do not copy invented usage or results.

## Signal extension

At 512 Hz sampling, a 300 Hz sinusoid aliases to `512 - 300 = 212` Hz. The
full 0–256 Hz plot shows that peak, and the frequency check compares it with
the sampling-theory prediction. At 40 Hz the predicted alias remains 40 Hz.
Halving a two-second record doubles bin spacing from 0.5 to 1 Hz; a 40.3 Hz
sinusoid falls between the original bins and exhibits spectral leakage.
