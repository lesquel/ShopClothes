
from backend.validator import Validator
from .order import Order


class PursacheHistory:
    def __init__(self):
        self.__pursache_history = []
        
    def add_product(self, order: Order):
        self.__pursache_history.append(Validator.validate_type(order, Order, "La orden ingresada no es valida"))

    def show_pursache_history(self):
        return [order.show_order() for order in self.__pursache_history]            