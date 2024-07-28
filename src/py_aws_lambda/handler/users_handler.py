from aws_lambda_powertools.event_handler.api_gateway import ApiGatewayResolver

app = ApiGatewayResolver()

@app.get("/users/<id>")
def get_user(id):
    print(f"GET /users/{id}")
    return {"message": f"User {id} details"}, 200

@app.post("/users")
def create_user():
    print("POST /users")
    return {"message": "User created"}, 201

@app.put("/users/<id>")
def update_user(id):
    print(f"PUT /users/{id}")
    return {"message": f"User {id} updated"}, 200

@app.delete("/users/<id>")
def delete_user(id):
    print(f"DELETE /users/{id}")
    return {"message": f"User {id} deleted"}, 200

def lambda_handler(event, context):
    return app.resolve(event, context)
