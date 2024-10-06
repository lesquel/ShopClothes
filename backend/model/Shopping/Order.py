from datetime import datetime

from backend.model.Product import Cloth
from backend.model.Person import Costumer 
from backend.validator import Validator
class Order:
    def __init__(self, costumer: Costumer, clothes: list[Cloth], total_price:float):
        self.__costumer = Validator.validate_type(costumer, Costumer, "El cliente ingresado no es valido")
        self.__clothes = Validator.validate_type_list(clothes, Cloth, "La prenda ingresada no es valida")
        self.__date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self.__total_price = total_price
        
    def show_order(self):
        return [cloth.name for cloth in self.__clothes]