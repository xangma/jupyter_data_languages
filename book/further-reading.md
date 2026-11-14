# Continue after the course

Use an active research repository as a reading exercise: locate its `README`,
dependency specification, public API, one unit test and contribution guidelines.
Explain one function and its assumptions yourself before asking a coding agent to
modify it, and keep practice edits in your own fork or local sandbox.

| Interest | Starting point | First question |
| --- | --- | --- |
| Mock catalogues and survey modelling | [SkyPy](https://github.com/skypyproject/skypy) | How is one scientific expectation expressed as a test? |
| Cosmological emulators | [Matryoshka](https://github.com/JDonaldM/Matryoshka) | What is the training domain, and how is accuracy assessed? |
| Void–galaxy inference | [victor](https://github.com/seshnadathur/victor) | What inputs and likelihood assumptions are required? |
| Gravitational waves | [PyCBC tutorials](https://github.com/gwastro/PyCBC-Tutorials) | What sampling rate and noise assumptions enter a calculation? |

Primary documentation for this course:

- [NumPy broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)
- [Astropy units](https://docs.astropy.org/en/stable/units/) and [tables](https://docs.astropy.org/en/stable/table/)
- [SciPy `curve_fit`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html): inspect `sigma` and `absolute_sigma`
- [Matplotlib error bars](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html)
- [`pytest` assertions](https://docs.pytest.org/en/stable/how-to/assert.html)
- [Pro Git](https://git-scm.com/book/en/v2) and [coding-agent setup](agent-tools.md)

## Next steps for observational astrophysics

- [`astropy.coordinates`](https://docs.astropy.org/en/stable/coordinates/): celestial reference frames (`ICRS`, `Galactic`), proper-motion propagation and exact 2D spherical sky cross-matching (`match_to_catalog_sky`) instead of naive Euclidean RA/Dec differences.
- [`astropy.io.fits`](https://docs.astropy.org/en/stable/io/fits/) and [`astropy.wcs`](https://docs.astropy.org/en/stable/wcs/): multi-extension FITS images and binary tables, header provenance cards and pixel-to-sky World Coordinate System transformations.
- [`astroquery`](https://astroquery.readthedocs.io/en/latest/): scripted, reproducible archive and ADQL/TAP queries across **Gaia**, **Euclid**, **SDSS** and space-telescope catalogues.
- [`photutils`](https://photutils.readthedocs.io/en/stable/) and [`specutils`](https://specutils.readthedocs.io/en/stable/): background estimation, aperture/PSF photometry and 1D spectral line or continuum analysis carrying Astropy units and uncertainties.

## Next steps for theoretical and computational astrophysics

- [`JAX`](https://docs.jax.dev/en/latest/) and [`Numba`](https://numba.readthedocs.io/en/stable/): JIT compilation, batched vectorisation (`vmap`) and automatic differentiation (`grad`) when pure NumPy array operations hit CPU/GPU bottlenecks.
- [`scipy.integrate.solve_ivp`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html) and [`scipy.fft`](https://docs.scipy.org/doc/scipy/reference/fft.html): stiff and non-stiff ODE solvers with explicit relative/absolute tolerances and spectral transforms for grid or perturbation calculations.
- **Bayesian inference samplers across ICG:** ensemble MCMC with [`emcee`](https://emcee.readthedocs.io/en/stable/), nested sampling with [`dynesty`](https://dynesty.readthedocs.io/en/stable/) and [`nessai`](https://nessai.readthedocs.io/en/latest/) / [`bilby`](https://lscsoft.docs.ligo.org/bilby/) for gravitational-wave parameter estimation, and cosmological likelihood pipelines in [`Cobaya`](https://cobaya.readthedocs.io/en/latest/) and [`GetDist`](https://getdist.readthedocs.io/en/latest/).
- **Property-based and numerical-invariant testing:** [`Hypothesis`](https://hypothesis.readthedocs.io/en/latest/) for automated edge-case generation alongside analytical limiting cases, conservation-law checks (energy, momentum, probability normalisation) and step-size convergence-rate tests.
- **Profiling before scaling to SCIAMA HPC / Slurm:** profile single-core runtime and memory locally (`cProfile`, `line_profiler`) and verify deterministic seed/checkpoint reproducibility before scaling batch or job-array runs on Portsmouth's [SCIAMA HPC cluster](https://www.sciama.icg.port.ac.uk/) under Slurm.

## Git and VS Code

- **Git manuals for history & recovery:** [hands-on tutorial](https://git-scm.com/docs/gittutorial), [`git restore`](https://git-scm.com/docs/git-restore), [`git reset`](https://git-scm.com/docs/git-reset), [`git revert`](https://git-scm.com/docs/git-revert) (note `-m` mainline parent selection before reverting a merge commit), [`git reflog`](https://git-scm.com/docs/git-reflog) and [`git push --force-with-lease`](https://git-scm.com/docs/git-push).
- **Graphical Git guides:** VS Code [Source Control](https://code.visualstudio.com/docs/sourcecontrol/overview) ([staging](https://code.visualstudio.com/docs/sourcecontrol/staging-commits), [merge conflicts](https://code.visualstudio.com/docs/sourcecontrol/merge-conflicts), [remotes](https://code.visualstudio.com/docs/sourcecontrol/repos-remotes)) and the [JupyterLab Git extension guide](https://github.com/jupyterlab/jupyterlab-git#usage).
