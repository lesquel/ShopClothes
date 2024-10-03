class Color:
    allColors = []
    
    @classmethod
    def __add_new_color(cls, Color):
        if not any(c.__name ==Color.__name for c in cls.allColors):
            cls.allColors.append(Color)
        else: raise ValueError("Este color ya se ha agregado")
        
    @classmethod
    def get_all_colors(cls):
        return [color.__name for color in cls.allColors]
    def __init__(self, name: str):
        if not isinstance(name,str):
            raise TypeError("El nombre del color es invalido")
        self.__name = name
        Color.__add_new_color(self)


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value