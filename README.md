# YOLO Object Detection Project
Scripts and pipeline to support training a YOLOv8 Object Detection model from custom dataset. 


# Setting Up Your Python Environment

Follow these steps to set up your Python environment for working with a specific module.

## Step 1: Create a Virtual Environment

```bash
# Navigate to your project directory
cd /path/to/your/project

# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Install this package for easy usage
# the -e flag for development mode of the python package
# which prevents user from reinstalling it after every change.
pip install -e .

# If only running scripts, without changing package, run
pip install .



# You can deactivate virtual env here by running:
deactivate

# or go on to run scripts.
