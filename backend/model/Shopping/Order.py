from datetime import datetime
from backend.validator import Validator
from backend.model.product import Cloth

class Order:
    def __init__(self, clothes: list[Cloth], total_price: float):

        # self.__costumer = Validator.validate_type(costumer, Costumer, "El cliente ingresado no es valido")
        self.__clothes = Validator.validate_type_list(clothes, Cloth, "La prenda ingresada no es valida")
        self.__total_price = total_price
        self.__date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    
    
    def show_order(self):
        return {
            'date': self.__date_time,
            'clothes': [cloth.name for cloth in self.__clothes],
            'total_price': self.__total_price
        }
