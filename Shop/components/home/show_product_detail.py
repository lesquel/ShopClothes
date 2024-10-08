import flet as ft
def add_to_cart(e, current_user,product):
    current_user.get_shopping_cart().add_product(product)
    print(current_user.get_shopping_cart().show_shopping_cart())

def Description(text):
    return ft.Container(
        content=ft.Text(text),
        padding=ft.padding.all(10),
        alignment=ft.alignment.center,
        border=ft.border.only(top=ft.border.BorderSide(1, "white")),
        width=200,
    )

def show_product_detail(page: ft.Page, product):
    # Importar HomePage aquí para evitar el ciclo de dependencias
    from Shop.pages.home import HomePage

    # Configurar el color de fondo de la página
    page.padding = ft.padding.all(20)

    # Función para volver a la página principal
    def go_back(e):
        page.go('/')

    # Crear la vista detallada del producto con mejoras en el diseño
    detail_view = ft.SafeArea(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.icons.ARROW_BACK,
                            on_click=go_back,
                        ),
                        ft.Text(
                            "Detalle del Producto",
                            size=35,
                            weight=ft.FontWeight.BOLD,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Container(
                    content=ft.Image(
                        src=product.img,
                        width=400,
                        height=400,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    padding=ft.padding.all(20),
                    alignment=ft.alignment.center,
                ),
                ft.Column(
                    controls=[
                        ft.Text(
                            f"Nombre: {product.name}",
                            size=25,
                        ),
                        ft.Text(
                            f"Descripción: {product.description}",
                            size=18,
                        ),
                        ft.Row(
                            controls=[
                                Description(f"Precio: {product.price}$"),
                                Description(f"Descuento: {product.discount}%"),
                                Description(f"Cantidad: {product.stock}"),
                                Description(f"Tamaño: {product.size.name}"),
                                Description(f"Color: {product.color.name}"),
                                Description(f"Marca: {product.brand.name}"),
                                Description(f"Categoría: {product.category.name}"),
                            ],
                            wrap=True,  
                        ),
                        ft.ElevatedButton(
                            "Agregar al carrito",
                            icon=ft.icons.ADD_SHOPPING_CART,
                            on_click=lambda e: add_to_cart(e,page.current_user,product),
                            
                        ),
                    ],
                    expand=True,
                    alignment=ft.alignment.center,
                    horizontal_alignment=ft.alignment.center,
                    spacing=20,
                ),
            ],
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.alignment.center,
        ),
        expand=True,
    )

    # Limpiar la página antes de mostrar el detalle
    page.controls.clear()
    # Añadir la vista detallada a la página
    page.add(detail_view)
    page.update()