const API_URL = "http://localhost:8000"

export async function fetchProducts() {
  try {
    const response = await fetch(`${API_URL}/api/products`)
    return await response.json()
  } catch (error) {
    console.error("Error fetching products:", error)
    return []
  }
}

export async function fetchCategories() {
  try {
    const response = await fetch(`${API_URL}/api/categories`)
    return await response.json()
  } catch (error) {
    console.error("Error fetching categories:", error)
    return []
  }
}

export async function createOrder(orderData: any) {
  try {
    const response = await fetch(`${API_URL}/api/orders`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(orderData),
    })
    return await response.json()
  } catch (error) {
    console.error("Error creating order:", error)
    return null
  }
}
