# YOLO Object Detection Project
Scripts and pipeline to support training a YOLOv8 Object Detection model from custom dataset. 

Runnable scripts can be found under scripts/ dir. It is not requires to have an active venv, as the bash scripts will activate and deactivate the venv automatically. If using a Windows machine, \ vs / will have to be hand edited.

In future edits, this might become a feature but for now, sorry! I have begun to use Path() objects for many file paths rather than strings, so if you see a / operation with a Path object, it is probably correct, so do not blindly change / to \\ or vice versa.

To come:
- scripts to train a YOLO classifier (they exist in the classifier/ but are not structured)
- more examples, especially ones to include the different helper functions that make life easier, like extract frames from a video or detecting blur.
- Better organization




# Setting Up Your Python Environment

Follow these steps to set up your Python environment for working with a specific module.


First, before setting up the virtual environment, we need to ensure that the CUDA Toolkit is installed on your machine (assuming you are to be using a GPU). Download and installation instructions can be found [here](https://developer.nvidia.com/). Make sure to install the correct version of the toolkit for your machine. Do a machine restart to ensure all drivers are active for the GPU. 



Depending on how you have installed Python, the python command might be different. However you are able to start an interactive Python session on the command line is what you should use in place of <python3> in the commands below. Generally, just <python> will work, however, Windows machines might have it set up to be <py>. You can change this by looking up how to export PATH on your machine.

```bash
# Navigate to the top level of this project directory
# Create a virtual environment named 'venv'
python -m venv venv

# Activate virtual environment
source venv/bin/activate # for unix machines
# OR
source venv\\Scripts\\activate # for windows
```




```bash
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


### examples/
Contains runnable python scripts that require no input. Change any variables for your specific use case, and run! Ensure that the virtual environment is activated if running on the command line or that your IDE environment has the virtual environment active if running through an editor.

#### examples/train_model.py
This script will train a YOLO object detection model from a baseline, pretrained model. YOLO documentation can provide details on the different size models they use, but it seems that the small model (yolov8s.pt) tends to have the best balance between performance and training time for the amount of data and processing power we currently have.

For a specific use case, please be sure to update the constants.py file in the obj_detector/ directory to set desired values, otherwise defaults will be used. Explore constants.py or the code to see what defaults will be implemented. The train_model.py itself has more details about arguements. Any additional training arguements can be included in the dictionary that is passed to the train function.

#### examples/predict_image.py
This script will predict a single image and output a text file containing the bounding box information, including the confidence score. 

There are many flags and optionals that can be provided, however the only absolutely necessary information is the model_path and img_path. Everything else has defaults.

#### examples/predict_frames.py
This script is the same as predict_image.py except it will predict every image in a directory. As the file name suggests, it is useful to predict over all the frames of a video, granted the frames of the video are in the passed directory.

Again, there are many flags and defaults. The only necessary arguements to the predict_frames() function are the model_path and frames_path. All other variables have defaults. 

There are also flags that will smooth the annotations up to a constant set in contants.py, in which the bounding box predictions per object will be linearly interpolated across n frames. If you would like to have the predicted bounding boxes drawn onto the frames, then set the draw_frames boolean to True.

#### examples/predict_frames_stitch.py
This script is the same as predict_frames.py except it demonstrates how to take the frames (assumed to have the bounding box information drawn on them) and create a video. The defaults frame rate is 30, and is set in constants.py. A different frame rate can be passed in as an argument to util.frames_to_video()

#### examples/predict_frames_exp_lvl.py
This script is more specific to the Developmental Intelligence Lab's structure. Provided an experiment and a model_path, the parent and child frames from one particular experiment for each subject will be genereated and placed at some output_path destination. 

The output will create one directory for each subject and camera angle. 

#### examples/predict_video.py
Similar to other prediction scripts, set desired variables and hit go. All default arguements are shown in the script, so the only ones truly necessary are the video_path.


### scripts/py_scripts/ and scripts/sh_scripts/
These directories contain scripts that were initially used to develop this project and run experiments. They can still be utilized, however are not as bullet proof as the example scripts. The structure of the project has changed significantly since these scripts have been updated. Please use them with caution.

There is generally one shell script that calls one of the python scripts. This was to provide a simpler interface to call the python scripts rather than provide command line arguments. If one wishes to run the scripts, please give it your best shot :) 



