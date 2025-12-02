from models import Product, Category

products: list[Product] = [
    Product(
        id=1,
        name="Buldak Cheese Ramyeon",
        category="ramyeon",
        price=3990,
        image="/korean-buldak-cheese-instant-noodle-yellow-package.jpg",
        spicy=3,
        description="Fideos súper picantes con un toque cremoso de queso",
        ingredients="Fideos de trigo, base de sopa (sabor a pollo picante), verduras deshidratadas (cebolla, zanahoria), polvo de queso cheddar, aceite de sésamo, condimentos (ajo, jengibre), aceite de chile."
    ),
    Product(
        id=2,
        name="Shin Ramyun Original",
        category="ramyeon",
        price=2990,
        image="/korean-shin-ramyun-instant-noodle-red-package.jpg",
        spicy=2,
        description="El clásico picante coreano que nunca falla",
        ingredients="Fideos de trigo, base de sopa (caldo de carne), verduras deshidratadas (champiñones, zanahoria, cebolla verde), condimentos (ajo, pimienta negra), aceite de sésamo."
    ),
    Product(
        id=3,
        name="Jin Ramen Mild",
        category="ramyeon",
        price=2990,
        image="/korean-jin-ramen-instant-noodle-blue-package.jpg",
        spicy=1,
        description="Sabor suave perfecto para principiantes con caldo de verduras",
        ingredients="Fideos de trigo, base de sopa (caldo de verduras suave), verduras deshidratadas (repollo, zanahoria, cebolla), aceite vegetal, especias suaves (ajo, jengibre)."
    ),
    Product(
        id=4,
        name="Neoguri Seafood",
        category="ramyeon",
        price=3490,
        image="/korean-neoguri-instant-noodle-green-package-seafoo.jpg",
        spicy=1,
        description="Fideos gruesos con sabor a mariscos del mar",
        ingredients="Fideos de trigo gruesos, base de sopa (sabor a mariscos), algas secas, verduras deshidratadas (cebolla, zanahoria), aceite de sésamo, especias marinas."
    ),
    Product(
        id=5,
        name="Chapagetti Black Bean",
        category="ramyeon",
        price=3290,
        image="/korean-chapagetti-black-bean-instant-noodle-packag.jpg",
        spicy=0,
        description="Fideos negros con salsa de frijol negro estilo coreano",
        ingredients="Fideos de trigo, salsa de frijol negro (chunjang), verduras deshidratadas (repollo, cebolla, zanahoria), aceite vegetal, azúcar, especias (ajo, jengibre)."
    ),
    Product(
        id=6,
        name="Buldak Hot Chicken",
        category="ramyeon",
        price=3790,
        image="/korean-instant-noodle-package-red-spicy-buldak.jpg",
        spicy=3,
        description="El original súper picante con sabor a pollo picante",
        ingredients="Fideos de trigo, base de sopa (sabor a pollo picante extremo), verduras deshidratadas, aceite de chile, condimentos (ajo, jengibre, pimienta cayena), azúcar."
    ),
    Product(
        id=7,
        name="Buldak Cup Noodles",
        category="ramyeon",
        price=2490,
        image="/korean-buldak-cup-instant-noodle-spicy-red.jpg",
        spicy=3,
        description="Versión en vaso del famoso Buldak picante",
        ingredients="Fideos de trigo, base de sopa (sabor a pollo picante), verduras deshidratadas, aceite de sésamo, condimentos picantes."
    ),
    Product(
        id=8,
        name="Veggie Ramyeon",
        category="ramyeon",
        price=2790,
        image="/korean-vegetarian-instant-noodle-package-green.jpg",
        spicy=1,
        description="Opción vegetariana con verduras frescas",
        ingredients="Fideos de trigo, base de sopa (caldo de verduras), verduras deshidratadas (espinaca, zanahoria, champiñones, cebolla), aceite vegetal, especias naturales."
    ),
    Product(
        id=9,
        name="Soju Jinro Original",
        category="bebestibles",
        price=4990,
        image="/korean-soju-bottle-green.jpg",
        spicy=0,
        description="El soju más popular de Corea, suave y refrescante",
        ingredients="Agua purificada, alcohol destilado de arroz, edulcorantes naturales, acidulantes."
    ),
    Product(
        id=10,
        name="Banana Milk",
        category="bebestibles",
        price=1990,
        image="/korean-banana-milk-yellow-bottle.jpg",
        spicy=0,
        description="La icónica leche de plátano coreana en botella",
        ingredients="Leche entera, puré de plátano, azúcar, saborizante natural de plátano, estabilizantes."
    ),
    Product(
        id=11,
        name="Tteokbokki Kit",
        category="tteokbokki",
        price=5990,
        image="/korean-tteokbokki-instant-kit-red.jpg",
        spicy=2,
        description="Kit completo para hacer tteokbokki casero picante",
        ingredients="Pasteles de arroz (tteok), salsa de gochujang (pasta de chile coreana), verduras deshidratadas, fish cakes, cebolla verde seca, azúcar, ajo."
    ),
    Product(
        id=12,
        name="Honey Butter Chips",
        category="snacks",
        price=2490,
        image="/korean-honey-butter-chips-yellow.jpg",
        spicy=0,
        description="Papas crujientes con sabor a miel y mantequilla",
        ingredients="Papas, aceite vegetal, saborizante (miel, mantequilla), sal, azúcar, leche en polvo."
    ),
    Product(
        id=13,
        name="Shrimp Crackers",
        category="snacks",
        price=1990,
        image="/korean-shrimp-crackers-orange.jpg",
        spicy=0,
        description="Galletas crujientes con auténtico sabor a camarón",
        ingredients="Harina de trigo, camarón en polvo, almidón de tapioca, aceite vegetal, sal, azúcar, glutamato monosódico."
    ),
]

categories: list[Category] = [
    Category(id="all", name="Todos", slug="todos"),
    Category(id="ramyeon", name="Ramyeon", slug="ramyeon"),
    Category(id="bebestibles", name="Bebestibles", slug="bebestibles"),
    Category(id="snacks", name="Snacks", slug="snacks"),
    Category(id="tteokbokki", name="Tteokbokki", slug="tteokbokki"),
]
