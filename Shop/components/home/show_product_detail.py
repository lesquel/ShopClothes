import flet as ft
def add_to_cart(e):
    print("Agregar al carrito")

def show_product_detail(page: ft.Page, product):
    # Importar HomePage aquí para evitar el ciclo de dependencias
    from Shop.pages.home import HomePage

    # Limpiar la página antes de mostrar el detalle
    page.controls.clear()
    
    # Crear la vista detallada del producto con mejoras en el diseño
    detail_view = ft.Container(
        content=ft.Column(
            [
                ft.Text(f"Detalle del Producto", size=35, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ft.Container(
                    content=ft.Image(src=product.img, width=400, height=400, fit=ft.ImageFit.CONTAIN),
                    padding=ft.padding.all(20),
                    alignment=ft.alignment.center,
                ),
                ft.Text(f"Nombre: {product.name}", size=25, text_align=ft.TextAlign.CENTER),
                ft.Text(f"Descripción: {product.description}", size=18, text_align=ft.TextAlign.CENTER),
                ft.Text(f"Categoría: {product.category.name}", size=18, text_align=ft.TextAlign.CENTER),
                ft.Text(f"Tamaño: {product.size.name}", size=18, text_align=ft.TextAlign.CENTER),
                ft.Text(f"Marca: {product.brand.name}", size=18, text_align=ft.TextAlign.CENTER),
                ft.Text(f"Color: {product.color.name}", size=18, text_align=ft.TextAlign.CENTER),
                ft.Text(f"Precio: {product.price}$", size=22, weight=ft.FontWeight.BOLD, color=ft.colors.GREEN, text_align=ft.TextAlign.CENTER),
                ft.Text(f"Descuento: {product.discount * 100}%", size=18, color=ft.colors.RED, text_align=ft.TextAlign.CENTER),
                ft.TextButton("Agregar al carrito", icon=ft.icons.ADD_SHOPPING_CART, on_click=add_to_cart),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
            scroll=ft.ScrollMode.AUTO,
        ),
        width=page.width,
        height=page.height,
        padding=ft.padding.only(top=20, bottom=100, left=20, right=20),
        alignment=ft.alignment.top_center,
        border_radius=ft.border_radius.all(20),
        shadow=ft.BoxShadow(
            blur_radius=10,
            spread_radius=5,
            color=ft.colors.BLACK12,
        )
    )
    
    # Añadir la vista detallada a la página
    page.add(detail_view)
    page.update()