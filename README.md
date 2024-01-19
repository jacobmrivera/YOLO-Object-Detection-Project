# YOLO Object Detection Project
Scripts and pipeline to support training a YOLOv8 Object Detection model from custom dataset. 

Runnable scripts can be found under scripts/ dir. It is not requires to have an active venv, as the bash scripts will activate and deactivate the venv automatically. If using a Windows machine, \ vs / will have to be hand edited.

In future edits, this might become a feature but for now, sorry!

### scripts/py_scripts
Contains runnable python files that can be run using CLI. Requires flag inputs.

### scripts/sh_scripts
Contains bash scripts that call the py_scripts. Easier interface to run python files, as the user can change variabels, rather than command line arguements.

# Setting Up Your Python Environment

Follow these steps to set up your Python environment for working with a specific module.


```bash
# Navigate to the top level of this project directory
# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Install this package for easy usage the -e flag for development mode of the python package,
# which prevents user from reinstalling it after every change.
pip install -e .

# If only running scripts, without changing package, run
pip install .



# You can deactivate virtual env here by running:
deactivate

# or go on to run scripts.

```
