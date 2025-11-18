from fastapi import FastAPI

# Create FastAPI app normally
app = FastAPI()

# Define routes
@app.get("/products")
def get_products():
    return [
        {"id": 101, "name": "Laptop"},
        {"id": 102, "name": "Book"},
    ]
