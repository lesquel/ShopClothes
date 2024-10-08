import flet as ft
def add_to_cart(e):
    print("Agregar al carrito")

def Card(product, on_click):
    return ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Image(
                        src=product.img, 
                        width=300, 
                        height=300
                    ),
                    ft.Text(
                        product.name,
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,  # Centrar el texto
                    ),
                    ft.Text(
                        product.description,
                        size=16,
                        text_align=ft.TextAlign.CENTER,  # Centrar el texto
                    ),
                    ft.TextButton(
                        "Ver detalle",
                        icon=ft.icons.PRODUCTION_QUANTITY_LIMITS,
                        on_click=on_click,
                    ),
                    ft.TextButton(
                        "Agregar al carrito",
                        disabled=True if product.stock == 0 else False,
                        icon=ft.icons.ADD_SHOPPING_CART,
                        on_click=add_to_cart,
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


