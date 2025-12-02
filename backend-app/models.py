from pydantic import BaseModel
from typing import Optional, Literal

class Product(BaseModel):
    id: int
    name: str
    category: str
    price: int
    image: str
    spicy: int
    description: str
    ingredients: str

class Category(BaseModel):
    id: str
    name: str
    slug: str

class CartItem(BaseModel):
    product: Product
    quantity: int

class Order(BaseModel):
    id: int
    userId: int
    items: list[CartItem]
    total: int
    date: str
    status: Literal["pending", "completed", "cancelled"]

class AppUser(BaseModel):
    name: str
    email: str
    avatar: Optional[str] = None
    id: Optional[int] = None
    loginDate: Optional[str] = None
