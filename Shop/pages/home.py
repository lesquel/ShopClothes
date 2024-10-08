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
                    padding=ft.padding.only(bottom=100),
                    expand=True,
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    Card(
                                        product=p,
                                        on_click=lambda e, p=p: show_product_detail(page, p)
                                    ) for p in PRODUCTS
                                ],
                                width=page.width,
                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                spacing=10,
                                wrap=True,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=20,
                        expand=True,
                        scroll=ft.ScrollMode.AUTO,
                    ),
                    
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

    page.on_resized = update_layout