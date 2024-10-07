import flet as ft
from Shop.components.navigationBar import navigationBar
from Shop.views import update_view
def main(page: ft.Page):
    page.adaptive = True
    # page.window.full_screen = True
    page.title = "Shop"

    # Definir la barra de navegación
    navigationBar(page) 

    # Configurar la vista inicial
    update_view(page)

# Ejecutar la aplicación
if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
