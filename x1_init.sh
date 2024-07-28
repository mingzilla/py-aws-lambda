#!/bin/bash

hatch env remove
hatch env create
hatch shell py-aws-lambda
echo $PYTHONPATH