### Q

### Create Serverless API
i would like to build a web server side application to provide APIs
* it's called `py-aws-lambda`
* it needs to be in `python`, so this is a `python` only project
* it should use `hatch` to configure such a python project
* I'm writing my code using `PyCharm`
* it should be able to handle user sessions
* it will be deployed to `aws` for production usage
* it should be written in aws `lambda` functions so that it's serverless
* it needs to use a library i develop and published to PyPI, the library is called `py-flat-orm`
* I would like to set up AWS Serverless Application Model (SAM) CLI on Windows
  * if there is something similar to serverless-offline, that would be great, I don't want to use node and npm because this is a python only project
* when running commands in the command line, please show me exactly which directory i need to execute the command, 
  * assuming the project is under `E:\code\python\py-aws-lambda`
  * and this directory has `.venv`, which is the activated virtual env

### Development and Production:
* development: i would like to run this application locally on my machine when i'm doing development
  * I need to be able to run the application and make these APIs available when doing development
  * when the app is running on my machine, I need to be able to remote debug the code, so that e.g. I can use Postman to make an API call, and my debug break point in `PyCharm` can catch it
* production: i need to deploy it to aws for production

### Features:
This app should offer 2 API endpoints that follow REST conventions, so correct them if my examples are not accurate:
* `/users` endpoints: 
  * `users_controller.py`
  * GET: `/users/{id}`
  * POST: `/users`
  * PUT: `/users/{id}`
  * DELETE: `/users/{id}` 
* `/addresses` endpoints: 
  * `addresses_controller.py`
  * provides GET, POST, PUT, DELETE
* each request 
  * takes all the submitted parameters or request body
  * print them out (no need to do any actual processing or interacting with a service or a database) 
  * then send a 200 or 201 valid response to the client side
* the root of the app would be similar to e.g. `http://host/py-aws-lambda`
  * so the url for the `/users` endpoints would be e.g. `http://host/py-aws-lambda/users`

can you show me how to set up such an application?
