from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Product, Category, Order, CartItem
from data import products, categories

app = FastAPI(title="K Market Express API", version="1.0.0")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoints de Productos
@app.get("/api/products", response_model=list[Product])
def get_products():
    """Obtener todos los productos"""
    return products

@app.get("/api/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    """Obtener un producto por ID"""
    for product in products:
        if product.id == product_id:
            return product
    return {"error": "Producto no encontrado"}

@app.get("/api/categories", response_model=list[Category])
def get_categories():
    """Obtener todas las categorías"""
    return categories

@app.post("/api/orders")
def create_order(order_data: dict):
    """Crear una nueva orden"""
    return {
        "id": len(products) + 1,
        "status": "pending",
        "total": order_data.get("total"),
        "items": order_data.get("items", []),
        "date": order_data.get("date")
    }

@app.get("/")
def root():
    """Health check"""
    return {"message": "K Market Express API - Backend operativo"}
