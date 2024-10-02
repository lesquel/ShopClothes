from ..Person.Costumer import Costumer
class Order:
    def __init__(self, id: int, costumer: Costumer, clothes: list, date: str):
        self.__id = id
        self.__costumer = costumer
        self.__clothes = clothes
        self.__date = date 