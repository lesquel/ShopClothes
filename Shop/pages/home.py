from Shop.components.Card import Card
import flet as ft
from backend.controler.products import PRODUCTS


def show_product_detail(page: ft.Page, product):
    # Limpiar la página antes de mostrar el detalle
    page.controls.clear()
    
    # Crear la vista detallada del producto
    detail_view = ft.Column(
        [
            ft.Text(f"Nombre: {product.name}", size=30, weight=ft.FontWeight.BOLD),
            ft.Image(src=product.img, width=400, height=400),
            ft.Text(f"Descripción: {product.description}", size=20),
            ft.Text(f"Categoría: {product.category.name}", size=20),
            ft.Text(f"Tamaño: {product.size.name}", size=20),
            ft.Text(f"Marca: {product.brand.name}", size=20),
            ft.Text(f"Color: {product.color.name}", size=20),
            ft.Text(f"Precio: {product.price}$", size=20),
            ft.Text(f"Descuento: {product.discount * 100}%", size=20),
            ft.ElevatedButton("Volver", on_click=lambda e: HomePage(page))  # Botón para volver a la página principal
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
    )
    
    # Añadir la vista detallada a la página
    page.add(detail_view)
    page.update()


def HomePage(page: ft.Page):
    def create_product_row(start, end):
        return ft.ResponsiveRow(
            controls=[
                Card(
                    title=product.name, 
                    description=product.description,
                    img=product.img, 
                    on_click=lambda e, p=product: show_product_detail(page, p)  # Pasar el producto a la vista de detalle
                ) for product in PRODUCTS[start:end]
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
            create_product_row(0, 4),
            create_product_row(4, 8),
            create_product_row(8, 12),
        ],
        spacing=20,
        scroll=ft.ScrollMode.AUTO
    )

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
                for card in row.controls:
                    card.width = 300 if columns >= 3 else None  # Ajusta el ancho máximo
                row.update()
        page.update()

    page.on_resize = update_layout
    update_layout(None)
