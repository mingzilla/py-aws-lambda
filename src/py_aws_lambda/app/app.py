from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'your_secret_key' # what is this for?


@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    return jsonify({'message': 'Logged in successfully ' + data}), 200


@app.route('/api/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully'}), 200


@app.route('/api/protected', methods=['GET'])
def protected():
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized'}), 401
    return jsonify({'message': 'This is protected data'}), 200


if __name__ == '__main__':
    app.run(debug=True)
