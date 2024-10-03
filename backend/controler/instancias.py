from backend.model.Product.Category import Category
from backend.model.Product.Brand import Brand
from backend.model.Product.Color import Color

class Categories:
    def __init__(self, categories_dict):
        for key, value in categories_dict.items():
            setattr(self, key, value)

class Colors:
    def __init__(self, colors_dict):
        for key, value in colors_dict.items():
            setattr(self, key, value)

class Brands:
    def __init__(self, brands_dict):
        for key, value in brands_dict.items():
            setattr(self, key, value)

# Instancias de las categorías
CATEGORIES_DICT = {
    "Pantalones": Category("Pantalones"),
    "Camisetas": Category("Camisetas"),
    "Zapatos": Category("Zapatos"),
    "Ropas": Category("Ropas"),
}

CATEGORIES = Categories(CATEGORIES_DICT)

# Instancias de los colores
COLORS_DICT = {
    "Blanco": Color("Blanco"),
    "Negro": Color("Negro"),
    "Rojo": Color("Rojo"),
    "Amarillo": Color("Amarillo"),
    "Azul": Color("Azul"),
}

COLORS = Colors(COLORS_DICT)

# Instancias de los brands
BRANDS_DICT = {
    "Nike": Brand("Nike"),
    "Puma": Brand("Puma"),
    "Reebok": Brand("Reebok"),
    "Asics": Brand("Asics"),
}

BRANDS = Brands(BRANDS_DICT)