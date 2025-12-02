export type ViewType = "home" | "cart" | "favorites" | "profile"

export interface Product {
  id: number
  name: string
  category: string
  price: number
  image: string
  spicy: number
  description: string
  ingredients: string
}

export interface Category {
  id: string
  name: string
  slug: string
}

export interface CartItem {
  product: Product
  quantity: number
}

export interface Order {
  id: number
  userId: number
  items: CartItem[]
  total: number
  date: string
  status: "pending" | "completed" | "cancelled"
}

export interface AppUser {
  name: string
  email: string
  avatar?: string
  id?: number
  loginDate?: string
}
