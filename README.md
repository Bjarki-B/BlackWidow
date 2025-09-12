# BlackWidow

## How to create the BlackWidow conda environment
To create a conda environment to run BlackWidow in, run the following:
`conda create -f blackwidow_env.yml -n blackwidow`
or
`mamba create -f blackwidow_env.yml -n blackwidow`

## How to build a BlackWidow virtual python environment
First, create a virtual enviroment for BlackWidow development:
`python -m venv /path/to/environments/blackwidow`

Next, activate that virtual environment
`source /path/to/environments/blackwidow/bin/actviate`

Then use the `requirements.txt` file to install dependencies
`pip install -r requirements.txt`
