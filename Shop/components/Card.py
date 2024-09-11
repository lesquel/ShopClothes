import flet as ft

def Card(title: str):
    return ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text(title, size=24, weight=ft.FontWeight.BOLD),
                ],
                spacing=10,
            ),
            padding=20,
            width=200,
            border_radius=10,
            alignment=ft.alignment.center,
        ),
    )