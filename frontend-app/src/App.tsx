"use client"

import React from "react"
import { useState } from "react"
import type { Product, Category, CartItem, AppUser, Order, ViewType } from "./types"
import { fetchProducts, fetchCategories } from "./api"
import "./App.css"

export default function App() {
  const [currentView, setCurrentView] = useState<ViewType>("home")
  const [cart, setCart] = useState<CartItem[]>([])
  const [favorites, setFavorites] = useState<number[]>([])
  const [user, setUser] = useState<AppUser | null>(null)
  const [orders, setOrders] = useState<Order[]>([])
  const [products, setProducts] = useState<Product[]>([])
  const [categories, setCategories] = useState<Category[]>([])
  const [activeCategory, setActiveCategory] = useState("all")
  const [searchTerm, setSearchTerm] = useState("")

  React.useEffect(() => {
    fetchProducts().then(setProducts)
    fetchCategories().then(setCategories)
  }, [])

  const filteredProducts = products.filter((p) => {
    const matchesCategory = activeCategory === "all" || p.category === activeCategory
    const matchesSearch = p.name.toLowerCase().includes(searchTerm.toLowerCase())
    return matchesSearch && matchesCategory
  })

  const addToCart = (product: Product) => {
    setCart((prevCart) => {
      const existing = prevCart.find((item) => item.product.id === product.id)
      if (existing) {
        return prevCart.map((item) =>
          item.product.id === product.id ? { ...item, quantity: item.quantity + 1 } : item,
        )
      }
      return [...prevCart, { product, quantity: 1 }]
    })
  }

  const getTotalPrice = () => cart.reduce((total, item) => total + item.product.price * item.quantity, 0)

  return (
    <div className="app">
      <header className="header">
        <h1>K Market Express</h1>
        <p>Sabor coreano en tu puerta</p>
      </header>

      <nav className="nav">
        <button onClick={() => setCurrentView("home")} className={currentView === "home" ? "active" : ""}>
          Inicio
        </button>
        <button onClick={() => setCurrentView("cart")} className={currentView === "cart" ? "active" : ""}>
          Carrito ({cart.length})
        </button>
        <button onClick={() => setCurrentView("favorites")} className={currentView === "favorites" ? "active" : ""}>
          Favoritos
        </button>
        <button onClick={() => setCurrentView("profile")} className={currentView === "profile" ? "active" : ""}>
          {user ? "Perfil" : "Login"}
        </button>
      </nav>

      <main className="content">
        {currentView === "home" && (
          <div className="home">
            <div className="categories">
              {categories.map((cat) => (
                <button
                  key={cat.id}
                  onClick={() => setActiveCategory(cat.id)}
                  className={activeCategory === cat.id ? "active" : ""}
                >
                  {cat.name}
                </button>
              ))}
            </div>

            <input
              type="text"
              placeholder="Buscar productos..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="search-input"
            />

            <div className="products-grid">
              {filteredProducts.map((product) => (
                <div key={product.id} className="product-card">
                  <div className="product-image">{product.image}</div>
                  <h3>{product.name}</h3>
                  <p>{product.description}</p>
                  <div className="product-footer">
                    <span className="price">${product.price}</span>
                    <button onClick={() => addToCart(product)}>Agregar</button>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {currentView === "cart" && (
          <div className="cart">
            <h2>Carrito de Compras</h2>
            {cart.length === 0 ? (
              <p>Tu carrito está vacío</p>
            ) : (
              <>
                <div className="cart-items">
                  {cart.map((item) => (
                    <div key={item.product.id} className="cart-item">
                      <h4>{item.product.name}</h4>
                      <p>Cantidad: {item.quantity}</p>
                      <p className="price">${item.product.price * item.quantity}</p>
                    </div>
                  ))}
                </div>
                <div className="cart-total">
                  <h3>Total: ${getTotalPrice()}</h3>
                  <button className="checkout-btn">Proceder al Pago</button>
                </div>
              </>
            )}
          </div>
        )}

        {currentView === "profile" && (
          <div className="profile">
            <h2>{user ? "Mi Perfil" : "Iniciar Sesión"}</h2>
            {user ? (
              <div>
                <p>Nombre: {user.name}</p>
                <p>Email: {user.email}</p>
                <button onClick={() => setUser(null)}>Cerrar Sesión</button>
              </div>
            ) : (
              <form
                onSubmit={(e) => {
                  e.preventDefault()
                  setUser({ name: "Usuario", email: "test@example.com" })
                }}
              >
                <input type="email" placeholder="Email" required />
                <input type="password" placeholder="Contraseña" required />
                <button type="submit">Iniciar Sesión</button>
              </form>
            )}
          </div>
        )}
      </main>
    </div>
  )
}
