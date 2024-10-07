from backend.controler.instancias import COLORS, BRANDS, CATEGORIES
from backend.model.product import Size, Cloth

product1 = Cloth(
    name="Pantalon",
    description="Este pantalón es el mejor",
    stock=10,
    category=CATEGORIES.Pantalones,
    size=Size.M,
    brand=BRANDS.Nike,
    color=COLORS.Blanco,
    price=100,
    discount=0.2,
    img="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80",
)
product2 = Cloth(
    name="Camiseta",
    description="Esta camiseta es la mejor",
    stock=3,
    category=CATEGORIES.Camisetas,
    size=Size.M,
    brand=BRANDS.Puma,
    color=COLORS.Blanco,
    price=100,
    discount=0.2,
    img="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80",
)
product3 = Cloth(
    name="Pantaleta",
    description="Esta pantalon es la mejor",
    stock=10,
    category=CATEGORIES.Camisetas,
    size=Size.M,
    brand=BRANDS.Puma,
    color=COLORS.Blanco,
    price=100,
    discount=0.2,
    img="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80",
)
product4 = Cloth(
    name="Otro pantalon",
    description="Esta pantalon es la mejor",
    stock=10,
    category=CATEGORIES.Zapatos,
    size=Size.M,
    brand=BRANDS.Puma,
    color=COLORS.Blanco,
    price=100,
    discount=0.2,
    img="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80",
)

PRODUCTS = [product1, product2, product3,product4]
