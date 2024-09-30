from ..Person.Costumer import Costumer

class PursacheHistory:
    def __init__(self, id: int, costumer: Costumer, order: str):
        self.__id = id
        self.__costumer = costumer
        self.__order = order