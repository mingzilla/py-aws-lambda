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
  * I would like my API to not just work using lambda, I want to have lambda internally just redirect to my endpoint implementation. 
  * please show me how i can run my api server with and without using sam
    * if `flask` is used, just call the `lambda` implementation
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
  * `/src/py_aws_lambda/handler/users_handler.py`, which has one function per endpoint, plus a `lambda_handler` function to be referred to by `template.yaml`
  * GET: `/users/{id}`
  * POST: `/users`
  * PUT: `/users/{id}`
  * DELETE: `/users/{id}`
* how to handle: GET, PUT, DELETE
  * takes all the submitted parameters and request body
  * print them out (no need to do any actual processing or interacting with a service or a database) 
  * then send a 200 valid response to the client side
* how to handle: POST
  * take a query parameter `skip` e.g. `/users?skip=true`, and a request body field `name`
  * print them out (no need to do any actual processing or interacting with a service or a database) 
  * then send a 201 valid response to the client side
* `/addresses` endpoints - same as `/users`
* the root of the app would be similar to e.g. `http://host/py-aws-lambda`
  * so the url for the `/users` endpoints would be e.g. `http://host/py-aws-lambda/users`
* `template.yaml`
  * use `python3.12`

can you show me how to set up such an application?
