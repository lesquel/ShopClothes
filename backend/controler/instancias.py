from backend.model.product import Size, Cloth
from backend.model.product import Category, Brand, Color, CategoryType


# Instancias de las categorías
pantalones = Category("Pantalones", CategoryType.BOTTOMS)
camisetas = Category("Camisetas", CategoryType.TOPS)
zapatos = Category("Zapatos", CategoryType.SHOES)
ropas = Category("Ropas", CategoryType.OTHER)

# Instancias de los colores
blanco = Color("Blanco")
negro = Color("Negro")
rojo = Color("Rojo")
amarillo = Color("Amarillo")
azul = Color("Azul")

# Instancias de los brands
nike = Brand("Nike")
puma = Brand("Puma")
reebok = Brand("Reebok")
asics = Brand("Asics")



product1 = Cloth(
    name="Pantalon",
    description="Este pantalón es el mejor",
    stock=10,
    category=pantalones,
    size=Size.M,
    brand=nike,
    color=blanco,
    price=100,
    discount=0.2,
    img="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80",
)
product2 = Cloth(
    name="Camiseta",
    description="Esta camiseta es la mejor",
    stock=3,
    category=camisetas,
    size=Size.M,
    brand=puma,
    color=blanco,
    price=100,
    discount=0.2,
    img="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80",
)
product3 = Cloth(
    name="Pantaleta",
    description="Esta pantalon es la mejor",
    stock=10,
    category=camisetas,
    size=Size.M,
    brand=puma,
    color=azul,
    price=100,
    discount=0.2,
    img="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80",
)
product4 = Cloth(
    name="Otro pantalon",
    description="Esta pantalon es la mejor",
    stock=10,
    category=zapatos,
    size=Size.M,
    brand=reebok,
    color=negro,
    price=100,
    discount=0.2,
    img="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80",
)