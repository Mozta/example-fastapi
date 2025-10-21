from fastapi import FastAPI
from models import CustomerIn, CustomerOut

app = FastAPI(title="My API", version="0.1.0")

@app.get("/")
async def root():
    return {"message": "Hello, World!"  }

@app.post("/customers/")
async def create_customer(customer: CustomerIn) -> CustomerOut:
    customer = CustomerOut(id=1, **customer.model_dump())
    return customer