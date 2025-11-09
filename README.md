# Jupyter notebooks for PhD class on data languages.

## Installing python
The easiest way to install python on any OS is to use [anaconda python](https://www.continuum.io/downloads).  This will install a local version of python on your system so you don't need to worry about needing admin to install new packages.  Most of the packages listed above are installed by default with anaconda.  For this class we will be using python 3, and I recommend you use this version for your research.

## Environment quick start
There are two audiences for this repository: students who just need to *run* the notebooks, and instructors/developers who also need authoring tooling such as notebook diff/strip helpers.  The required packages are split accordingly.

### Running the classes
Use whichever option matches your tooling preference; both install the same runtime stack needed by the notebooks and exercises.

```bash
# option 1: conda environment
conda env create -f env/environment.yml
conda activate astroclass

# option 2: pip + virtualenv/uv/venv
python -m venv .venv && source .venv/bin/activate
pip install -r env/requirements.txt
```

These files install the core scientific stack (python>=3.10, numpy, scipy, astropy, pandas, matplotlib, jupyter, ipywidgets, pytest, coverage, pyyaml, rich) plus the optional libraries referenced in the notebooks (`numpyro`, `tinygp`, `graphviz`).  Students do **not** need to worry about any notebook‑authoring helpers such as `nbstripout` to work through the material.

### Maintainers / developing the classes
Maintainers should install the same base environment as the students, then add the small set of tooling packages that keep the repository clean:

```bash
pip install nbstripout pre-commit

# configure helpers (runs once per clone)
nbstripout --install --attributes .gitattributes
pre-commit install
```

`nbstripout` keeps execution counts/metadata out of commits, and `pre-commit` ensures the hooks run automatically.  These are development conveniences only-students do not need them to run the notebooks.

## Optional packages used in advanced notebooks
+ `numpyro`
+ `tinygp`
+ `graphviz`

```bash
pip install numpyro tinygp graphviz
```

## Class 1
- `Git.ipynb`: Git and Git-Hub
- `General_Python.ipynb`: General python information
- `Unit_testing.ipynb`: Writing unit tests in python

## Class 2
- `General_plotting.ipynb`: How to make publication ready plots
- `mpl_style.py`: How to make a `matplotlib` style
- `Uncertainty_plotting.ipynb`: Making plots with errorbars
- `Astropy_fitting.ipynb`: using `astropy` to model and fit data

## Class 3
