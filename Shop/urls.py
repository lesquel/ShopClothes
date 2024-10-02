import flet as ft
from Shop.views import update_view
def handle_navigation(page: ft.Page, event: ft.ControlEvent):
    # Determinar el índice seleccionado desde el evento
    selected_index = event.control.selected_index if hasattr(event.control, 'selected_index') else None
    
    if selected_index is not None:
        if selected_index == 0:
            page.go("/")
        elif selected_index == 1:
            page.go("/account")
        elif selected_index == 2:
            page.go("/search")
    
    # Actualizar la vista para reflejar la ruta cambiada
    update_view(page)

