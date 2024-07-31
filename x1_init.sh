#!/bin/bash

hatch env remove
hatch env create
hatch shell py-aws-lambda
pip install pip-tools
echo $PYTHONPATH