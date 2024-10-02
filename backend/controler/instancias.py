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
    "Pantalones": Category(1, "Pantalones"),
    "Camisetas": Category(2, "Camisetas"),
    "Zapatos": Category(3, "Zapatos"),
    "Ropas": Category(4, "Ropas"),
}

CATEGORIES = Categories(CATEGORIES_DICT)

# Instancias de los colores
COLORS_DICT = {
    "Blanco": Color(1, "Blanco"),
    "Negro": Color(2, "Negro"),
    "Rojo": Color(3, "Rojo"),
    "Amarillo": Color(4, "Amarillo"),
    "Azul": Color(5, "Azul"),
}

COLORS = Colors(COLORS_DICT)

# Instancias de los brands
BRANDS_DICT = {
    "Nike": Brand(1, "Nike"),
    "Puma": Brand(2, "Puma"),
    "Reebok": Brand(3, "Reebok"),
    "Asics": Brand(4, "Asics"),
}

BRANDS = Brands(BRANDS_DICT)