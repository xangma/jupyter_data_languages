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

## Git and VS Code

Start with [Git's hands-on tutorial](https://git-scm.com/docs/gittutorial), then
use the command manuals for the recovery you need:
[restore](https://git-scm.com/docs/git-restore),
[reset](https://git-scm.com/docs/git-reset),
[revert](https://git-scm.com/docs/git-revert) and
[reflog](https://git-scm.com/docs/git-reflog).
The Session 2 recovery examples concern ordinary commits. Reverting a merge
requires choosing a mainline parent and affects later merges; read the
`git revert` manual and discuss the intended history before attempting it.
Rewriting published history is a separate, coordinated workflow; the
[push manual](https://git-scm.com/docs/git-push) explains force and lease checks.

VS Code's guides cover [Source Control](https://code.visualstudio.com/docs/sourcecontrol/overview),
[staging and commits](https://code.visualstudio.com/docs/sourcecontrol/staging-commits),
[remotes and synchronisation](https://code.visualstudio.com/docs/sourcecontrol/repos-remotes),
[merge conflicts](https://code.visualstudio.com/docs/sourcecontrol/merge-conflicts)
and [troubleshooting](https://code.visualstudio.com/docs/sourcecontrol/troubleshooting).
For the CPD interface, see the [JupyterLab Git project and usage guide](https://github.com/jupyterlab/jupyterlab-git#usage).
JupyterHub starts the server; JupyterLab provides the editor and Git panel.
The course's [screenshot notes](https://github.com/xangma/jupyter_data_languages/blob/codex/phd-python-2026/book/screenshots/README.md) record the captured version
and how the example states were created.

Session 2 was also reviewed against
[Coleman Krawczyk's original Git lecture](https://github.com/CKrawczyk/jupyter_data_languages/blob/master/Git.ipynb),
the suggested [Medium tutorial](https://medium.com/@jaaeehoonkim/git-tutorial-1-31d0b1db1940)
and [GeeksforGeeks topic index](https://www.geeksforgeeks.org/git/git-tutorial/).
Use the primary manuals above to check command behaviour. The core practical
introduces concepts before hosting and practises shared recovery without
requiring an online account.

The earlier notebooks remain in `classes/`, the three root plotting notebooks,
and `Previous_notebooks/`. They are historical references, outside the validated
2026 teaching path. They may need extra packages or repairs; do not treat the
old Slurm session as part of the Python course.
