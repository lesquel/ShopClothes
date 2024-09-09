import flet as ft
def SearchPage(page: ft.Page):
    page.add(
            ft.SafeArea(
                ft.Column(
                    [
                        ft.Text("Buscar", size=30),
                    ]
                )
            )
        )