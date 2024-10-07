from enum import Enum

from backend.model.product import Cloth
from .order import Order
from backend.validator import Validator

class Operation(Enum):
    ADD = 1
    REMOVE = 2

class ShoppingCart:
    def __init__(self, costumer): 
        from backend.model.person.costumer import Costumer
        self.__costumer = Validator.validate_type(
            costumer, Costumer, "El cliente ingresado no es valido"
        )
        self.__clothes = []
        self.__total_price = 0
        

    @property
    def total(self):
        return self.__total_price

    @total.setter
    def total(self, value):
        self.__total_price = value
        
    def add_product(self, cloth: Cloth):
        self.__clothes.append(Validator.validate_type(cloth, Cloth, "La prenda ingresada no es valida"))
        self.update_price(Operation.ADD, cloth)

    def remove_product(self, cloth: Cloth):
        if any(cloth.name == c.name for c in self.__clothes):
            self.__clothes.remove(cloth)
            self.update_price(Operation.REMOVE, cloth)
        else:
            raise ValueError("La prenda no esta en el carrito")

    def show_shopping_cart(self):
        return [cloth.name for cloth in self.__clothes]

    def update_price(self, operation, cloth: Cloth):
        if operation == Operation.ADD:
            self.__total_price += cloth.price
        else:
            self.__total_price -= cloth.price

    def confirm_cart(self):
        if not self.__clothes:
            raise ValueError("El carrito esta vacio")
        
        orden = Order(self.__clothes, self.__total_price)
        self.__costumer.make_purchase(orden)
        
        del self

