from flask import Flask

from py_aws_lambda.handler.addresses_handler import get_address, create_address, update_address, delete_address
from py_aws_lambda.handler.users_handler import get_user, create_user, update_user, delete_user

app = Flask(__name__)

@app.route('/users/<id>', methods=['GET'])
def flask_get_user(id):
    return get_user(id)

@app.route('/users', methods=['POST'])
def flask_create_user():
    return create_user()

@app.route('/users/<id>', methods=['PUT'])
def flask_update_user(id):
    return update_user(id)

@app.route('/users/<id>', methods=['DELETE'])
def flask_delete_user(id):
    return delete_user(id)

@app.route('/addresses/<id>', methods=['GET'])
def flask_get_address(id):
    return get_address(id)

@app.route('/addresses', methods=['POST'])
def flask_create_address():
    return create_address()

@app.route('/addresses/<id>', methods=['PUT'])
def flask_update_address(id):
    return update_address(id)

@app.route('/addresses/<id>', methods=['DELETE'])
def flask_delete_address(id):
    return delete_address(id)

if __name__ == '__main__':
    app.run(debug=True)
