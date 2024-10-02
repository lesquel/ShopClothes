import flet as ft

def show_product_detail(page: ft.Page, product):
    # Importar HomePage aquí para evitar el ciclo de dependencias
    from Shop.pages.home import HomePage

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
