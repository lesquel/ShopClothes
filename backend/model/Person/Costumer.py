from backend.model.shopping import PursacheHistory
from backend.validator import Validator
from .person import Person
from backend.model.shopping import Order

class Costumer(Person):
    def __init__(self, username: str, password: str):
        super().__init__(username, password)  
        self.__pursache_history = PursacheHistory()
        
    def make_purchase(self, order):
        self.__pursache_history.add_product(Validator.validate_type(order, Order, "La orden ingresada no es valida"))

    def show_pursache_history(self):
        return {"costumer": self.username,"orders":self.__pursache_history.show_pursache_history()}
    
        
    def __str__(self):
        return f"Costumer: {self.username}"