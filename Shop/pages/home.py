import flet as ft
from Shop.components.Card import Card

def HomePage(page: ft.Page):
    def create_product_row(start, end):
        return ft.ResponsiveRow(
            controls=[
                Card(title=f"Product {i}", description=f"Description {i}")
                for i in range(start, end + 1)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
            run_spacing=10,
        )

    content = ft.Column(
        [
            ft.Container(
                content=ft.Text("Home", size=30, weight=ft.FontWeight.BOLD),
                margin=ft.margin.only(bottom=20),
            ),
            create_product_row(1, 5),
            create_product_row(6, 10),
            create_product_row(11, 15),
            create_product_row(16, 20),
        ],
        spacing=20,
        scroll=ft.ScrollMode.AUTO
    )

    # Hacer scrollable el contenido
    scrollable_content = ft.Container(
        content=content,
        expand=True,
        padding=20,
    )

    page.add(
        ft.SafeArea(
            content=scrollable_content
        )
    )

    def update_layout(e):
        width = page.window_width
        if width < 600:
            columns = 1
        elif width < 1000:
            columns = 2
        else:
            columns = 3

        for row in content.controls:
            if isinstance(row, ft.ResponsiveRow):
                # Cambia la cantidad de columnas dinámicamente
                for card in row.controls:
                    card.width = 300 if columns >= 3 else None  # Ajusta el ancho máximo
                row.update()
        page.update()

    page.on_resize = update_layout
    update_layout(None)

