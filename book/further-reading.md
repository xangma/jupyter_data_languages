# Continue after the course

Use a real repository as a reading exercise: find its README, environment,
public API, one test and contribution guidance. Explain one function before
asking an agent to change it. Classroom practice should stay in your own sandbox.

| Interest | Starting point | First question |
| --- | --- | --- |
| Mock catalogues and survey modelling | [SkyPy](https://github.com/skypyproject/skypy) | How is one scientific expectation expressed as a test? |
| Cosmological emulators | [Matryoshka](https://github.com/JDonaldM/Matryoshka) | What is the training domain, and how is accuracy assessed? |
| Void–galaxy inference | [victor](https://github.com/seshnadathur/victor) | What inputs and likelihood assumptions are required? |
| Gravitational waves | [PyCBC tutorials](https://github.com/gwastro/PyCBC-Tutorials) | What sampling rate and noise assumptions enter a calculation? |

Primary documentation for this course:

- [NumPy broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)
- [Astropy units](https://docs.astropy.org/en/stable/units/) and [tables](https://docs.astropy.org/en/stable/table/)
- [SciPy curve_fit](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html): inspect `sigma` and `absolute_sigma`
- [Matplotlib error bars](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html)
- [pytest assertions](https://docs.pytest.org/en/stable/how-to/assert.html)
- [Pro Git](https://git-scm.com/book/en/v2)
- [Jupyter Book](https://jupyterbook.org/stable/) and [MyST hosting](https://mystmd.org/guide/deployment)

The earlier notebooks remain in `classes/`, the three root plotting notebooks,
and `Previous_notebooks/`. They are historical references, outside the validated
2026 teaching path. They may need extra packages or repairs; do not treat the
old Slurm session as part of the Python course.
