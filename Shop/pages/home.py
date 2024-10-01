import flet as ft
from Shop.components.Card import Card
def HomePage(page: ft.Page):
    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.Text("Home", size=30),
                    
                    # Crear ResponsiveRow para ajustar las columnas de manera dinámica
                    ft.ResponsiveRow(
                        controls=[
                            Card(title="Product 1", description="Description 1"),
                            Card(title="Product 2", description="Description 2"),
                            Card(title="Product 3", description="Description 3"),
                            Card(title="Product 4", description="Description 4"),
                            Card(title="Product 5", description="Description 5"),
                        ],
                        adaptive=True,
                        col=2,  # Ajustar el número de columnas según el tamaño de la pantalla
                        alignment=ft.MainAxisAlignment.CENTER,  # Centrar horizontalmente
                        spacing=10,  # Espacio entre las tarjetas
                        run_spacing=10,  # Espacio entre filas
                    ),
                ]
            )
        ),
    )

