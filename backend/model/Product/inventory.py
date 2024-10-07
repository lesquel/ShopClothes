from .cloth import Cloth
from backend.validator import Validator

class Inventory:
    allClothes = []
    
    @classmethod
    def add_cloth(cls, cloth: Cloth):
        cls.allClothes.append(Validator.validate_type(cloth, Cloth, "La prenda ingresada no es valida"))
    
    @classmethod
    def remove_cloth(cls, cloth: Cloth):
        cls.allClothes.remove(Validator.validate_type(cloth, Cloth, "La prenda ingresada no es valida"))
    
    @classmethod
    def show_inventory(cls):
        return [cloth.show_cloth() for cloth in cls.allClothes]
    
    
    
    @classmethod
    def get_cloth_by_name(cls, name):
        return [cloth for cloth in cls.allClothes if cloth.name == name]
    
    @classmethod
    def get_cloth_by_brand(cls, brand):
        return [cloth for cloth in cls.allClothes if cloth.brand == brand]

    @classmethod
    def get_cloth_by_category(cls, category):
        return [cloth for cloth in cls.allClothes if cloth.category == category]
    
    @classmethod
    def get_cloth_by_color(cls, color):
        return [cloth for cloth in cls.allClothes if cloth.color == color]
    
    @classmethod
    def get_cloth_by_size(cls, size):
        return [cloth for cloth in cls.allClothes if cloth.size == size]
    
    @classmethod
    def get_cloth_by_price(cls, price):
        return [cloth for cloth in cls.allClothes if cloth.price == price]
    
    @classmethod
    def get_cloth_by_discount(cls, discount):
        return [cloth for cloth in cls.allClothes if cloth.discount == discount]
    
    @classmethod
    def get_cloth_by_stock(cls, stock):
        return [cloth for cloth in cls.allClothes if cloth.stock == stock]

    
    @classmethod
    def get_cloth_by_description(cls, description):
        return [cloth for cloth in cls.allClothes if cloth.description == description]
    
