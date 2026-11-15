# Hints and worked answers

Attempt each task first. Read the visible **Hint** to unblock your thinking, then
expand **Worked answer** to check your numbers, code and physical reasoning.

## Primer

**Hint:** Convert the input with `np.asarray(values)` first, combine
`np.isfinite(values)` and `(values > 0)` with `&`, and ask what `0.0` claims
physically compared with `NaN`.

:::{dropdown} Worked answer
```python
def positive_finite(values):
    values = np.asarray(values)
    return values[np.isfinite(values) & (values > 0)]

assert positive_finite([-2, 0, 1, np.nan, np.inf, 3]).tolist() == [1.0, 3.0]
```

For `[-2, 0, 1, np.nan, np.inf, 3]`, the returned values are `[1, 3]`. Replacing
missing (`NaN`) entries with `0` invents an observed physical measurement of zero
(such as zero flux or zero recession velocity) and biases downstream summaries.
:::

## Session 1

### Baseline & Task A — shared masks, invalid-row counts and broadcasting

**Hint:** Use `table[:3].pprint_all()` to inspect every column and unit, count
each failure mode separately with `np.count_nonzero(...)`, and slice all columns
with one shared boolean mask.

:::{dropdown} Worked answer
```python
table[:3].pprint_all()
print("Missing velocity:", np.count_nonzero(~np.isfinite(velocity)))      # 3
print("Nonpositive sigma:", np.count_nonzero(sigma <= 0))                # 1
print("Missing magnitude:", np.count_nonzero(~np.isfinite(magnitude)))   # 1
for cut in (15.5, 16.5, 17.5):
    print(cut, np.count_nonzero(valid & (magnitude < cut)))              # 161, 262, 357
```

Three missing velocities, one zero velocity error (`sigma <= 0`) and one missing
apparent magnitude occur on five distinct rows, leaving **395 usable rows**.
Assigning zero velocity to missing entries fabricates stationary galaxies. With
the shared `valid` mask, magnitude limits of `15.5`, `16.5` and `17.5` select
**161**, **262** and **357** objects respectively. Reshaping a 1-D per-object
factor with `[:, None]` turns `(N,)` into `(N, 1)` so one scale broadcasts across
each row's three features `(N, 3)`, while `axis=0` collapses rows into `(3,)`
per-band summaries and `axis=1` collapses columns into `(N,)` per-galaxy sums.
:::

### Task B — units, constants and FITS

**Hint:** Compare the columns and `meta` dictionary of `table` against the FITS
`subset`, and consider what `.value` would return if a file stored distances in
`kpc` rather than `Mpc`.

:::{dropdown} Worked answer
```python
restored_mpc = restored["distance"].to_value(u.Mpc)
np.testing.assert_allclose(restored_mpc, distance[valid])
assert np.all(np.isfinite(restored_mpc) & (restored_mpc > 0))
```

The FITS round-trip retains the three physical columns (`distance`, `velocity`,
`velocity_error`) and their `TUNITn` units while omitting `object_id`,
`apparent_magnitude`, and arbitrary ECSV dictionary metadata (`subset.meta.clear()`).
Calling `.to_value(u.Mpc)` (like `astropy.constants` and `u.spectral()` /
`u.doppler_optical` equivalencies) checks dimensions and converts compatible
scales (`kpc` $\rightarrow$ `Mpc`), whereas `.value` blindly strips whatever unit
was stored. On real survey FITS tables and 2D cutouts, also verify row or `NAXIS`
shapes, finite bounds, `WCS` frame/projection keys, and `origin='lower'` display
orientation.
:::

### Your turn — velocity residual diagnostic

**Hint:** Subtract `70.0 * distance[valid] + 300.0` from `velocity[valid]` and
plot against `distance[valid]` around `ax.axhline(0.0, ls='--')`.

:::{dropdown} Worked answer
```python
resid = velocity[valid] - (70.0 * distance[valid] + 300.0)
fig, ax = plt.subplots(figsize=(7, 3.6))
idx = np.arange(resid.size)[::8]
ax.errorbar(distance[valid][idx], resid[idx], yerr=sigma[valid][idx], fmt="o", ms=3.5, capsize=2)
ax.axhline(0.0, color="C3", ls="--", lw=1.3)
ax.set(xlabel="Distance [Mpc]", ylabel="Velocity residual [km/s]")
fig.tight_layout()
```

Residuals scatter symmetrically around `0 km/s` across `20–200 Mpc` with no
systematic distance trend, and roughly two-thirds of the $1\sigma$ error bars
cross the zero line (`np.mean(np.abs(resid) <= sigma[valid])` $\approx 0.68$).
:::

### Task C — survey selection and figure caption

**Hint:** Name the sample sizes, common bin edges and shared validity mask in
three sentences, then check whether cutting on apparent magnitude selects on
velocity residuals at fixed distance.

:::{dropdown} Worked answer
**Example caption:** "Counts and normalised distance distributions for 395 usable
synthetic objects and the 262-object subset with apparent magnitude below 16.5,
plotted on common distance bin edges. Five rows with non-finite measurements or
nonpositive velocity errors were removed using one shared mask. The flux-limited
subset preferentially retains nearby galaxies; this synthetic diagnostic is
neither a survey completeness measurement nor a cosmological $H_0$ measurement."

**Bias analysis:** Because selection here depends only on distance and apparent
magnitude—not on velocity noise at fixed distance—the weighted linear slope need
not be biased, though losing distant objects shrinks the distance lever arm and
widens the slope uncertainty. Real distance errors, correlated peculiar
velocities or selection on the fitted observable itself can bias the estimator.
:::

## Session 2

### Task A — staging area versus working tree

**Hint:** Compare `git diff --staged` (index vs `HEAD`) with `git diff` (working
tree vs index) before restaging `test_angle.py`.

:::{dropdown} Worked answer
Before restaging, the next commit would contain `test_wraparound` (already in the
index) but omit `test_full_turns` (saved only in the working tree). That is why
`test_angle.py` appears simultaneously in both Staged and Changed lists in the
CLI, VS Code and JupyterLab—all three views read the same `.git` index and
working tree. Running `git restore --staged -- test_angle.py` unstages without
losing either edit; `git add test_angle.py` stages both tests together.
:::

### Merge conflict

**Hint:** Read both sides of `<<<<<<< HEAD ... ======= ... >>>>>>> description-b`
and write one clean sentence preserving both physical facts with all marker lines
removed.

:::{dropdown} Worked answer
A valid resolution is: `"Angles are measured in degrees, and the helper returns
their shortest separation."` Saving edits the working tree, staging selects the
resolved file for the merge commit, committing records the two-parent snapshot
locally, and pushing updates a remote repository. A pull request adds hosted
review and discussion around a proposed branch merge; `git pull` fetches and
integrates commits locally rather than opening a pull request.
:::

### Local & shared recovery

**Hint:** Check whether anyone else can already have the mistaken commit: use a
soft reset only for a private local tip, and `git revert` once a commit has been
pushed.

:::{dropdown} Worked answer
Private recovery (`git reset --soft HEAD~1`) moves `recovery-lab` back one parent
while keeping the edit staged so you can fix and recommit it (`rescue-before-undo`
still points to the discarded commit). Shared recovery (`git revert --no-edit HEAD`
followed by `git push`) records a new commit whose parent is the pushed mistake.
In `partner-practice`, `git log` shows **both** the shared mistake and its
revert, and `README.md` keeps `Angle units: degrees.` while omitting
`Validation: skipped (practice mistake).`.
:::

### Task B — independent bearing tests and catching a bug

**Hint:** Derive geometric boundary cases ($0^\circ$ and $180^\circ$) plus a
floating-point wraparound across $360^\circ$ using `pytest.approx`, then predict
which assertions fail under `abs(b - a)`.

:::{dropdown} Worked answer
```python
import pytest
from angle import angle_distance

def test_equal_bearings():
    assert angle_distance(42, 42) == 0

def test_opposite_bearings():
    assert angle_distance(0, 180) == 180

def test_float_wraparound():
    assert angle_distance(359.9, 0.1) == pytest.approx(0.2)
```

In IEEE-754 floating-point arithmetic, `360 - abs(0.1 - 359.9)` evaluates to
`0.20000000000004547`, so `pytest.approx(0.2)` avoids brittle exact-float
failure. With the deliberate `abs(b - a)` bug, `test_wraparound` returns `358`
instead of `2`, `test_float_wraparound` returns `359.8` instead of `0.2`, and
`test_full_turns` returns `630` instead of `90`, while `test_small_angles`,
`test_equal_bearings` and `test_opposite_bearings` still pass. Running
`git restore -- angle.py` discards only that unstaged bug (`git diff -- angle.py`
is empty), leaving `test_angle.py` ready to commit on `edge-case-tests`. Unit
tests still cannot catch caller inputs supplied in radians instead of degrees.
:::

## Session 3

### Core practical — plan, student checks, scalar `weighted_mean` repair and accountability

**Hint:** Pick unequal uncertainties so $1/\sigma^2$ and $1/\sigma$ disagree,
lock `test_weighted_mean.py` and `test_student_checks.py` at `TESTS_COMMIT`, and
rescale weights by `errors.min()` to avoid overflow while returning a `float`.

:::{dropdown} Worked answer
**Boundaries & plan:** The client UI, model host and OS sandbox are distinct—for
example, Cline on a laptop edits laptop files even when Qwen runs on CPD, and a
Git branch or prompt instruction is not an OS sandbox. A sound plan preserves the
scalar contract, validates matching nonempty finite 1-D arrays with `errors > 0`,
and uses $w_i = 1/\sigma_i^2$.

**Independent student tests (`test_student_checks.py`):** For `[2, 10]` with
errors `[1, 2]`, relative inverse-variance weights `[1, 1/4]` give
$(2 + 10/4)/(1 + 1/4) = 3.6$ (whereas $1/\sigma$ gives $4.67$). Equal-error tests
give `2.0` under ordinary, $1/\sigma$ and $1/\sigma^2$ weighting alike, so they
cannot catch wrong error powers.

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

**Scalar repair (`weighted_mean.py`):**

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

**Review & `AI_USE.md`:** Reject any proposal that changes `1.2` to `1.5` in a
test file or returns `(mean, uncertainty)` instead of a scalar. Record the
interface/model/host (or manual pair route), `TESTS_COMMIT`, one concrete
steering or approval decision, observed before/after `pytest` counts, and an
untested assumption (e.g. that observations share one true value with independent
Gaussian noise).
:::

### Optional follow-on — `curve_fit` $2\sigma$ scaling, survey cut and reference tuple note

**Hint:** Track how $\sigma_i \rightarrow 2\sigma_i$ scales every term of
$\chi^2(\theta) = \sum_i [y_i - f(x_i;\theta)]^2 / \sigma_i^2$ when SciPy's
`absolute_sigma=True` is enabled.

:::{dropdown} Worked answer
Doubling every $\sigma_i$ divides $\chi^2(\theta)$ by `4` everywhere: the
best-fit `[slope, intercept]` is **unchanged**, `reduced_chi2` divides by **4**,
and with `absolute_sigma=True` the covariance matrix scales by `4`, so parameter
standard errors **double**. Applying Session 1's `apparent_magnitude < 16.5` cut
leaves the toy slope unbiased but removes distant galaxies, narrowing the
distance baseline and widening the slope uncertainty $\sigma_a$.

**Reference helper note:** Unlike the scalar practice file,
`course2026.analysis.weighted_mean` returns `(mean, uncertainty)`. On `[1, 3]`
with errors `[1, 3]` and `[3, 1]`, its means are `1.2` and `2.8` with common
standard error $(\sum w_i)^{-1/2} = (1 + 1/9)^{-1/2} = \sqrt{0.9}$.
:::

## Signal extension

**Hint:** Use $\Delta f = 1/T$ for FFT bin spacing, test whether $40.3\text{ Hz}$
spans an integer number of cycles over $T$, and fold $300\text{ Hz}$ across the
Nyquist limit $f_{\mathrm{Nyq}} = f_s / 2 = 256\text{ Hz}$.

:::{dropdown} Worked answer
Halving the duration $T$ from $2\text{ s}$ to $1\text{ s}$ doubles the frequency
bin spacing $\Delta f = 1/T$ from **$0.5\text{ Hz}$ to $1.0\text{ Hz}$**. Over a
$2\text{ s}$ record ($\Delta f = 0.5\text{ Hz}$), a **$40.3\text{ Hz}$** sinusoid
falls between the $40.0\text{ Hz}$ and $40.5\text{ Hz}$ bins and exhibits
**spectral leakage** across adjacent bins. At $512\text{ Hz}$ sampling, a
**$300\text{ Hz}$** sinusoid aliases across $256\text{ Hz}$ to
$512 - 300 = \mathbf{212\text{ Hz}}$, matching `predicted_alias` and the plotted
peak on $0\text{--}256\text{ Hz}$ (whereas $40\text{ Hz}$ stays at $40\text{ Hz}$).
:::
