import flet as ft
from Shop.components.navigationBar import navigationBar
from Shop.views import update_view
from backend.model import person as PS
def main(page: ft.Page):
    page.adaptive = True
    # page.window.full_screen = True
    page.title = "Shop"

    page.current_user = PS.Costumer("usuario_ejemplo", "contraseña123")
    # Definir la barra de navegación
    navigationBar(page) 

    # Configurar la vista inicial
    update_view(page)

# Ejecutar la aplicación
if __name__ == "__main__":
    ft.app(target=main,view=ft.AppView.WEB_BROWSER)
