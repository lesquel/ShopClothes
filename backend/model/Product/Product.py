from .Category import Category
from .Size import Size
from .Brand import Brand
from .Color import Color
class Product:
    def __init__(self, id : int, name: str, description: str, stock: int, category: Category, size: Size, brand: Brand, color: Color, price: float, discount: float, img: str):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__stock = stock
        self.__category = category
        self.__size = size
        self.__brand = brand
        self.__color = color
        self.__price = price
        self.__discount = discount
        self.__img = img
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        self.__id = value
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, value):
        self.__description = value
    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, value):
        self.__stock = value
    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, value):
        self.__category = value
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        self.__size = value
    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, value):
        self.__brand = value
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, value):
        self.__color = value
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        self.__price = value
    @property
    def discount(self):
        return self.__discount
    @discount.setter
    def discount(self, value):
        self.__discount = value
    @property
    def img(self):
        return self.__img
    @img.setter
    def img(self, value):
        self.__img = value