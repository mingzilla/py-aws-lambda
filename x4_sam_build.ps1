# Define what version of python to run in `template.yaml`
pip-compile --output-file=requirements.txt pyproject.toml

sam build
