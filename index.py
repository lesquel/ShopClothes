from backend.model import person as PS, product as PR
from backend.error_handler import ErrorHandler



@ErrorHandler()
def main():
    persona1 = PS.Costumer("juan", "1234")
    marca1 = PR.Brand("nike")

    categoia1 = PR.Category("Pantalon", PR.CategoryType.BOTTOMS)

    color1 = PR.Color("azul")

    size1 = PR.Size.XXL

    product1 = PR.Cloth("pantalon", "pantalon azul", 7,"categoia1", size1, marca1, color1, 100, 0, "img")
    product2 = PR.Cloth("pantalon1", "pantalon rojo", 5,categoia1, size1, marca1, color1, 100, 0, "img")

    shopping1 = persona1.get_shopping_cart() 
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
    print()
    print(PR.Brand.get_all_brands())
    
    
if __name__ == "__main__":
    error = main()
    if isinstance(error, dict) and error.get("error"):
        print(error)
    