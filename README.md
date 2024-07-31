# py-aws-lambda

[![PyPI - Version](https://img.shields.io/pypi/v/py-aws-lambda.svg)](https://pypi.org/project/py-aws-lambda)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/py-aws-lambda.svg)](https://pypi.org/project/py-aws-lambda)

-----

## Table of Contents

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install py-aws-lambda
```

## Get Started

This project is set up using `hatch`. 
* Run `xi_init.ps1` or `xi_init.sh` to apply `pyproject.toml`
  - run `exit` (deactivate env) first if you get `Cannot remove active environment: py-aws-lambda`  
* Run other `.ps1` or `.sh` files for relevant tasks
* `x1` means execution, and generally the 1st thing to run
* run `hatch -h` 

## Project Creation

### Initialisation
* This project is generated using `hatch new py-aws-lambda`
* `pyproject.toml` is then edited to include `[tool.hatch.envs.py-aws-lambda]` etc.
* script files e.g. `x*.ps1` are added 
* set up with git 
* Run e.g. `xi_init.ps1` to apply `pyproject.toml`

### Git

```shell
git init
git config --global --add safe.directory E:/code/python/py-aws-lambda
```

### Sync Dependencies
* run `hatch shell` to activate env, it also syncs dependencies

### Tests Data
* use `./test_data` directory put test data
  * test data cannot be put into `./tests`, otherwise when running `hatch test`, it treats them as tests to execute
  * you can pattern exclude these files but that requires more project config

### Test in PyCharm
* mark `tests` as Test Root, allows right-clicking directories inside to run tests
* run tests from root, and save test config as a file e.g. `test.run.xml`
* IMPORTANT: unmark `tests` as Test Root once `test.run.xml` is generated
  - if `tests` is marked as root, you CANNOT run a single test file, 
  - because it treats `tests` as root and can't find files within `src`
  - you can verify this by putting `import sys; print(sys.path)` at the top of a test file and run it

### Static Analysis
* add dependency `mypy`
* each package needs to add an empty `py.typed` file to make pycharm happy
* so each package has `__init__.py` and `py.typed`, seems pointless, just live with it

### Publish
* `hatch build`
* `hatch publish` - ask chatGPT how to set up a PyPI Account

## AWS lambda serverless function

### Setting up
* install aws tooling by adding dependencies "aws-lambda-powertools", "serverless-wsgi"
* define them in `pyproject.toml`

### Lambda functions
* need to create `template.yaml` file
  - `Handler: src/py_aws_lambda.handler.users_handler.lambda_handler`
    - This refers to the `users_handler` file, which has a `lambda_handler` function to resolve the endpoints
  - `Path: /py-aws-lambda/users/{id}`
    - This has to 100% match definition in `users_handler`: `@app.get("/py-aws-lambda/users/<id>")` 
* `src/py_aws_lambda.handler.users_handler`
  - `@app.get("/py-aws-lambda/users/<id>")` # defines the endpoint 
  - `def lambda_handler(event, context):` # handler to be put int `template.yaml` `Handler`

### Building
* need to export dependencies into `requirements.txt`, because aws tooling only supports this one way of resolving dependencies
* build with `sam build`

#### convert `pyproject.toml` to `requirements.txt`
* `pip-tools` is an extra tool convert `pyproject.toml` into `requirements.txt`

```shell
pip install pip-tools
pip-compile --output-file=requirements.txt pyproject.toml
```

### Run in dev
```shell
sam local start-api
```

## License

`py-aws-lambda` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
