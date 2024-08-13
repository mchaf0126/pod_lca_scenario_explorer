#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = CLF_b_public_dataset
PYTHON_VERSION = 3.10
PYTHON_INTERPRETER = venv_pub/Scripts/python

#################################################################################
# COMMANDS                                                                      #
#################################################################################


## Install Python Dependencies
requirements: test_environment
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt

## Create public dataset
public_dataset:
	$(PYTHON_INTERPRETER) -m src.public_dataset

## Lint using flake8
lint:
	$(PYTHON_INTERPRETER) -m flake8 src/data

## Test python environment is setup correctly
test_environment:
	$(PYTHON_INTERPRETER) test_environment.py
