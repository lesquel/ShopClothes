class Category:
    allCategories = []
    
    @classmethod
    def __add_new_category(cls, category):
        if not any(c.__name ==category.__name for c in cls.allCategories):
            cls.allCategories.append(category)
        else: raise ValueError("Esta marca ya se ha agregado")
        
    @classmethod
    def get_all_categories(cls):
        return [category.__name for category in cls.allCategories]
    
    def __init__(self, name: str):
        if not isinstance(name,str):
            raise TypeError("El nombre de la categoria es invalida")
        self.__name = name
        Category.__add_new_category(self)


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value