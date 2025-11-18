from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/orders")
def create_order():
    users = requests.get("http://user-service:5001/users").json()
    products = requests.get("http://product-service:5002/products").json()

    order = {
        "order_id": 1,
        "user": users[0],
        "product": products[0]
    }
    return order
