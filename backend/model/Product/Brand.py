class Brand:
    __allBrands = []
    
    @classmethod
    def __add_new_brand(cls, brand):
        if not any(b.__name ==brand.__name for b in cls.__allBrands):
            cls.__allBrands.append(brand)
        else: raise ValueError("Esta marca ya se ha agregado")
        
    @classmethod
    def get_all_brands(cls):
        return [brand.__name for brand in cls.__allBrands]
    
    def __init__(self, name: str):
        self.__name = name
        Brand.__add_new_brand(self)
        

    @property
    def name(self):
        return self.__name
    @name.setter    
    def name(self, value):
        self.__name = value