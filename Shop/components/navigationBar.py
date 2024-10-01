import flet as ft
from Shop.urls import handle_navigation
def navigationBar(page: ft.Page):
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.icons.PERSON, label="Cuenta"),
            ft.NavigationBarDestination(icon=ft.icons.SEARCH, label="Search"),
        ],
        border=ft.Border(
            top=ft.BorderSide(color=ft.colors.BLACK, width=1),
        ),
        on_change=lambda e: handle_navigation(page, e),
    )