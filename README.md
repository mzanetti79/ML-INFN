# ML INFN

Here you can find the code concerning the INFN course on data analytics and ML. The code is entirely in python, with scriptis to be edited and run locally or jupyter notebooks.
The present code is largely (almost entirely) based on Francesco "Checco" Mosconi's DataWeekends classes (https://www.dataweekends.com)

# Prerequisites:
- Anaconda (https://www.continuum.io/downloads), with Python 2.7
- Atom (https://atom.io)

## Directory structure:
- current folder: standalone scripts
- advanced: jupyter ipython notebooks with slightly more advanced exercises and examples
- data: datasets used

## Getting Started:

### Create a conda environment
From the current folder run:
```shell
conda env create
```

Answer yes when prompted and then activate the environment:

```shell
source activate ml-infn
```

### Check that all required packages are correctly installed

```shell
python check_prerequisites.py
```
