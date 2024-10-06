from backend.validator import Validator
from .Category import Category
from .Size import Size
from .Brand import Brand
from .Color import Color
class Cloth:
    _allClothes = []

    @classmethod
    def __add_new_cloth(cls, cloth):
        if not any(c.__name == cloth.__name for c in cls._allClothes):
            cls._allClothes.append(cloth)
        else:
            raise ValueError("Esta ropa ya se ha agregado")

    @classmethod
    def get_all_clothes(cls):
        return [cloth.__name for cloth in cls._allClothes]
    
    def __init__(self,name: str, description: str, category: Category, size: Size, brand: Brand, color: Color, price: float, discount: float, img: str):
        
        self.__name = name
        self.__description = description
        # self.__stock = stock
        self.__category = Validator.validate_type(category, Category, "La categoria ingresada no es valida")
        self.__size = Validator.validate_type(size, Size, "El tamaño ingresado no es valido")
        self.__brand = Validator.validate_type(brand, Brand, "La marca ingresada no es valida")
        self.__color = Validator.validate_type(color, Color, "El color ingresado no es valido")
        self.__price = price
        self.__discount = discount
        self.__img = img
        
        Cloth.__add_new_cloth(self)
        

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
        self.__category = Validator.validate_type(value, Category, "La categoria ingresada no es valida")
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        self.__size = Validator.validate_type(value, Size, "El tamaño ingresado no es valido")
    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, value):
        self.__brand = Validator.validate_type(value, Brand, "La marca ingresada no es valida")
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, value):
        self.__color = Validator.validate_type(value, Color, "El color ingresado no es valido")
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