import flet as ft
from Shop.components.Card import Card
from backend.controler.products import PRODUCTS
from Shop.components.home.show_product_detail import show_product_detail

def HomePage(page: ft.Page):
    content = ft.Container(
        content=ft.Column(
            [
                ft.Container(
                    content=ft.Text("Home", size=30, weight=ft.FontWeight.BOLD),
                    margin=ft.margin.only(bottom=20),
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    Card(
                                        title=product.name, 
                                        description=product.description,
                                        img=product.img,
                                        stock=product.stock,
                                        on_click=lambda e, p=product: show_product_detail(page, p)
                                    ) for product in PRODUCTS
                                ],
                                width=page.width,
                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                spacing=10,
                                wrap=True,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=20,
                        scroll=ft.ScrollMode.AUTO,
                    ),
                    padding=ft.padding.only(bottom=100),
                    expand=True,
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=0,
            expand=True,
        ),
        width=page.width,
        height=page.height,
        padding=ft.padding.all(20),
    )

    page.add(
        ft.SafeArea(
            content=content
        )
    )

    def update_layout(e):
        content.width = page.width
        content.height = page.height
        page.update()

    page.on_resize = update_layout