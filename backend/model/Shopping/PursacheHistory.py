from datetime import datetime

from backend.validator import Validator
from ..Person.Costumer import Costumer
from .Order import Order


class PursacheHistory:
    def __init__(self, costumer: Costumer, order: Order):
        self.__costumer = Validator.validate_type(
            costumer, Costumer, "El cliente ingresado no es valido"
        )
        self.__order = Validator.validate_type(
            order, Order, "La orden ingresada no es valida"
        )
        self.__date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
