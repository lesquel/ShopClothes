import flet as ft
from components.Card import Card
def HomePage(page: ft.Page):
    page.add(
            ft.SafeArea(
                ft.Column(
                    [
                        ft.Text("Home", size=30),
                        
                        ft.Row(
                            [
                                Card("Product 1"),
                                Card("Product 2"),
                                Card("Product 3"),
                                Card("Product 4"),
                                Card("Product 5"),
                            ],
                            
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                            wrap=True,
                            #spacing=5,
                        ),
                    ]
                )
            ),
        )