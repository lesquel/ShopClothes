class Inventory:
    """
    + id
+ cloth
+ amount
    """
    def __init__(self, id: int, cloth: str, amount: int):
        self.__id = id
        self.__cloth = cloth
        self.__amount = amount  