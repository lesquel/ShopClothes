import flet as ft

def Card(title: str, description: str, img: str, on_click):
    return ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Image(
                        src=img, 
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
                    ft.TextButton(
                        "Ver detalle",
                        icon=ft.icons.INFO,
                        on_click=on_click,
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
        width=300,  # Ancho fijo, ajustable si se desea
    )


