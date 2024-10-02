from .Category import Category
from .Size import Size
from .Brand import Brand
from .Color import Color
class Product:
    def __init__(self, id : int, category: Category, size: Size, brand: Brand, color: Color, price: int, discount: float, img: str):
        self.__id = id
        self.__category = category
        self.__size = size
        self.__brand = brand
        self.__color = color
        self.__price = price
        self.__discount = discount
        self.__img = img