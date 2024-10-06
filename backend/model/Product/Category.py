from backend.validator import Validator
from .category_type import CategoryType
class Category:
    __allCategories = []
    
    @classmethod
    def __add_new_category(cls, category):
        if not any(c.__name ==category.__name for c in cls.__allCategories):
            cls.__allCategories.append(category)
        else: raise ValueError("Esta marca ya se ha agregado")
        
    @classmethod
    def get_all_categories(cls):
        return [category.__name for category in cls.__allCategories]
    
    def __init__(self, name: str, category_type: CategoryType):

        self.__name = name
        self.__category_type = Validator.validate_type(category_type, CategoryType, "El tipo de categoria ingresado no es valido")
        Category.__add_new_category(self)


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def category_type(self):
        return self.__category_type

    @category_type.setter
    def category_type(self, category_type):
        self.__category_type = Validator.validate_type(category_type, CategoryType, "El tipo de categoria ingresado no es valido")