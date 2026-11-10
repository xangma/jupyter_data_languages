# Python for ICG Research

Three two-hour practical sessions for incoming PhD students at the Institute of
Cosmology and Gravitation, University of Portsmouth.

By the end you will have a small analysis you can rerun, a scientific test you can
explain, and a reviewed Git commit. You will practise using a coding agent while
retaining responsibility for the result. Each session includes a ten-minute break.

| Session | Research task | What you will practise |
| --- | --- | --- |
| 1: A defensible result | Inspect a mock galaxy catalogue and its survey selection | Arrays, shapes, masks, units, tables, FITS, plots and uncertainty |
| 2: A reproducible change | Put a small calculation under version control | Functions, Git, branches, conflicts, pytest, environments and review |
| 3: Agent-assisted science | Recover an injected relation; repair a wrong weighted mean | Fitting, residuals, acceptance tests, agent permissions and independent verification |

Start with [setup](setup.md). If imports, loops and functions are unfamiliar, work
through the primer first. The core notebooks contain short tasks, hints and exit
checks; pause before opening the [solutions](solutions.md).

All catalogue values are **invented teaching data**. They are not observations or
a measurement of the Hubble constant. The same local file is used throughout, and
the practicals need no network access after installation. Agent access is optional:
you can use the supplied candidate implementation and review it with a partner.

The book displays saved notebook results. Download/open the repository notebooks
in JupyterLab or VS Code to edit and execute them. A static book does not provide
a Python kernel; interactive CPD integration is a separate deployment step.

The [instructor guide](instructor.md) has the six-hour timetable. The signal
exercise and [further reading](further-reading.md) are extensions. HPC is covered
in separate sessions.

Adapted from Coleman Krawczyk's `jupyter_data_languages` lectures and Xan
Morice-Atkinson's 2025 additions. The original MIT licence is retained.
