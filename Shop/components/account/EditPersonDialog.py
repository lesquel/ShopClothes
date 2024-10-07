from backend.model import person as PS
import flet as ft
def EditPersonDialog(person: PS.Costumer, on_save, page: ft.Page):
    def close_dlg(e, dlg):
        dlg.open = False
        page.update()

    username_field = ft.TextField(value=person.username, label="Username")
    password_field = ft.TextField(value=person.password, label="Password", password=True)

    dlg = ft.AlertDialog(
        title=ft.Text("Editar Usuario"),
        content=ft.Column([
            username_field,
            password_field,
        ], tight=True),
        actions=[
            ft.TextButton("Cancelar", on_click=lambda e: close_dlg(e, dlg)),
            ft.TextButton("Guardar", on_click=lambda e: on_save(username_field.value, password_field.value)),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    return dlg
