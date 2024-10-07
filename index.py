from backend.model import person as PS, shopping as SH, product as PR

persona1 = PS.Costumer("juan", "1234")
persona2 = PS.Costumer("juan", "1234")
marca1 = PR.Brand("nike")

categoia1 = PR.Category("Pantalon", PR.CategoryType.BOTTOMS)

color1 = PR.Color("azul")

size1 = PR.Size.XXL

product1 = PR.Cloth("pantalon", "pantalon azul", 7,categoia1, size1, marca1, color1, 100, 0, "img")
product2 = PR.Cloth("pantalon1", "pantalon rojo", 5,categoia1, size1, marca1, color1, 100, 0, "img")

shopping1 = SH.ShoppingCart(persona1)
shopping1.add_product(product1)

shopping1.add_product(product1)
shopping1.add_product(product1)
shopping1.add_product(product2)

# shooping2 = SH.ShoppingCart(persona1)
# shooping2.add_product(product1)
# shooping2.add_product(product1)



shopping1.confirm_cart()

print(persona1.show_pursache_history())


print(PR.Inventory.show_inventory())