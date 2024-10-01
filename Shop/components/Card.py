import flet as ft
def Card(title: str, description: str):
    return ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Image(
                        src="https://i.blogs.es/0ca9a6/aa/1366_2000.jpeg", 
                        width=300, 
                        height=300
                    ),
                    ft.Text(
                        title,
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,  # Centrar el texto
                    ),
                    ft.Text(
                        description,
                        size=16,
                        text_align=ft.TextAlign.CENTER,  # Centrar el texto
                    ),
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=20,
            border_radius=10,
            alignment=ft.alignment.center,
        ),
        elevation=5,
        width=300  # Ancho fijo, ajustable si se desea
    )