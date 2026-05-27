from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float
    stock_quantity: int


class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = None
    

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    stock_quantity: int

    model_config = {
        'from_attributes': True
    }

class ProductStockUpdate(BaseModel):
    stock_quantity: int