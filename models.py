from pydantic import BaseModel, validate_email

class CustomerIn(BaseModel):
    name: str
    email: str
    phone: str | None
    address: str | None

class CustomerOut(CustomerIn):
    id: int