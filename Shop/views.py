import flet as ft
from pages.home import HomePage
from pages.account import AccountPage
from pages.search import SearchPage
def update_view(page: ft.Page):
    # Limpiar las vistas existentes
    page.controls.clear()

    # Añadir la vista correspondiente basada en la ruta actual
    if page.route == "/":
        HomePage(page)
    elif page.route == "/account":
        AccountPage(page)
    elif page.route == "/search":
        SearchPage(page)

    # Actualizar la página para reflejar los cambios
    page.update()
