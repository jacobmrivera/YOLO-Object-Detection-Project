# YOLO Object Detection Project
Scripts and pipeline to support training a YOLOv8 Object Detection model from custom dataset. 

Runnable scripts can be found under scripts/ dir. It is not requires to have an active venv, as the bash scripts will activate and deactivate the venv automatically. If using a Windows machine, \ vs / will have to be hand edited.

In future edits, this might become a feature but for now, sorry!


### examples/
Contains runnable python scripts that require no input. Change any variables for your specific use case, and run! Ensure that the virtual environment is active.

### scripts/py_scripts
Contains runnable python files that can be run using CLI. Requires flag inputs.

### scripts/sh_scripts
Contains bash scripts that call the py_scripts. Easier interface to run python files, as the user can change variabels, rather than command line arguements.


# Setting Up Your Python Environment
## Requirements
- `python` ([Install](https://www.python.org/downloads/))
- `pip` ([Install](https://pip.pypa.io/en/stable/installation/))


Follow these steps to set up your Python environment for working with a specific module.

1. Check if python is installed
    - in command prompt, type:
        ```bash
        python -V
        ```
    - or type:
        ```bash
        python3 -V
        ```
    - if it is not, click the link above and download it

2. Check if pip is installed
    - in command prompt, type:
        ```bash
        pip --version
        ```
    - or type:
        ```bash
        pip3 --version
        ```
    - if not, install it using the link above.

3.  Navigate to the top level of this project directory. Run the following in Command Prompt:

    1. Create a virtual environment named 'venv'
        ```bash
        python3 -m venv venv
        ```
    2. Activate virtual environment
        ```bash
        source venv/Scripts/activate
        ```
    3. Install requirements
        ```bash
        pip install -r requirements.txt
        ```
        Install this package for easy usage the -e flag for development mode of the python package, which prevents user from reinstalling it after every change.
        ```bash
        pip install -e .
        ```
        If only running scripts, without changing package, run
        ```bash
        pip install .
        ```

    4. You can deactivate virtual env here by running:
        ```bash
        deactivate
        ```
        or go on to run scripts.




