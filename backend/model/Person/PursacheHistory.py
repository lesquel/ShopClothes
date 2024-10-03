from ..Person.Costumer import Costumer

class PursacheHistory:
    def __init__(self, costumer: Costumer, order: str):
        self.__costumer = costumer
        self.__order = order