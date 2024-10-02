import flet as ft
from Shop.components.Card import Card
from backend.controler.products import PRODUCTS
from Shop.components.home.show_product_detail import show_product_detail

def HomePage(page: ft.Page):

    content = ft.Column(
        [
            ft.Container(
                content=ft.Text("Home", size=30, weight=ft.FontWeight.BOLD),
                margin=ft.margin.only(bottom=20),
            ),
            ft.Column(  # Contenedor para las filas de tarjetas
                controls=[
                    ft.Row(
                        controls=[
                            Card(
                                title=product.name, 
                                description=product.description,
                                img=product.img,
                                on_click=lambda e, p=product: show_product_detail(page, p)  # Pasar el producto a la vista de detalle
                            ) for product in PRODUCTS
                        ],
                        width=page.width,  # Ancho del Row
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        spacing=10,
                        wrap=True,  # Ajustar automáticamente a nuevas filas
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                scroll=ft.ScrollMode.ALWAYS,  # Hacer el contenedor scrollable verticalmente
                expand=True,  # Expandir para usar todo el espacio disponible
            )
        ], 
        alignment=ft.MainAxisAlignment.CENTER,
    )

    page.add(
        ft.SafeArea(
            content=content
        )
    )
