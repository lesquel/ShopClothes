from .Cloth import Cloth


class Stock:
    allStocks = []

    @classmethod
    def __add_new_stock(cls, stock):
        if not any(s.__name == stock.__name for s in cls.allStocks):
            cls.allStocks.append(stock)
        else:
            raise ValueError("Esta marca ya se ha agregado")

    @classmethod
    def get_all_brands(cls):
        return [stock.__name for stock in cls.allStocks]

    def __init__(self, cloth: str, amount: float):
        if not isinstance(Cloth, cloth):
            raise ValueError("La ropa ingresada es invalida")
        self.__cloth = cloth
        self.__amount = amount
        Stock.__add_new_stock(self)
