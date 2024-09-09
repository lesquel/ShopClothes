import flet as ft
def HomePage(page: ft.Page):
    page.add(
            ft.SafeArea(
                ft.Column(
                    [
                        ft.Text("Home", size=30),
                    ]
                )
            )
        )