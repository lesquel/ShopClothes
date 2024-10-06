from backend import Person as PS
from backend import Product as PR
from backend import Shopping as SH

persona1 = PS.Costumer("juan", "1234")

marca1 = PR.Brand("nike")

categoia1 = PR.Category("Pantalon", PR.CategoryType.BOTTOMS)

color1 = PR.Color("azul")

size1 = PR.Size.XXL

product1 = PR.Cloth("pantalon", "pantalon azul", categoia1, size1, marca1, color1, 100, 0, "img")
product2 = PR.Cloth("pantalon1", "pantalon rojo", categoia1, size1, marca1, color1, 100, 0, "img")
stock1 = PR.Stock(product1, 10)


shopping1 = SH.ShoppingCart(persona1)

shopping1.add_product(product1)
shopping1.add_product(product1)
shopping1.add_product(product1)
shopping1.add_product(product2)

# print(shopping1.show_shopping_cart())

# print(shopping1.total)

orden = shopping1.confirm_cart()
shopping1 = None
print(orden.show_order())