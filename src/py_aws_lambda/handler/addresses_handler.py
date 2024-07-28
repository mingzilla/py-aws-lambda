from aws_lambda_powertools.event_handler.api_gateway import ApiGatewayResolver

app = ApiGatewayResolver()

@app.get("/addresses/<id>")
def get_address(id):
    print(f"GET /addresses/{id}")
    return {"message": f"Address {id} details"}, 200

@app.post("/addresses")
def create_address():
    print("POST /addresses")
    return {"message": "Address created"}, 201

@app.put("/addresses/<id>")
def update_address(id):
    print(f"PUT /addresses/{id}")
    return {"message": f"Address {id} updated"}, 200

@app.delete("/addresses/<id>")
def delete_address(id):
    print(f"DELETE /addresses/{id}")
    return {"message": f"Address {id} deleted"}, 200

def lambda_handler(event, context):
    return app.resolve(event, context)
