# K Market Express - Backend API

Backend construido con **FastAPI** y **Python**.

## Instalación

\`\`\`bash
pip install fastapi uvicorn pydantic
\`\`\`

## Ejecutar el servidor

\`\`\`bash
uvicorn main:app --reload
\`\`\`

El servidor estará disponible en: `http://localhost:8000`

## Documentación interactiva

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Endpoints principales

- `GET /api/products` - Obtener todos los productos
- `GET /api/products/{id}` - Obtener producto por ID
- `GET /api/categories` - Obtener todas las categorías
- `POST /api/orders` - Crear una orden
\`\`\`

---

**FRONTEND-APP - TypeScript Vite**
