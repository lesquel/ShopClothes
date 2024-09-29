class Order:
    def __init__(self, id: int, costumer: str, clothes: list, date: str):
        self.__id = id
        self.__costumer = costumer
        self.__clothes = clothes
        self.__date = date 