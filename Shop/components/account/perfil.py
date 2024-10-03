from backend.model.Person.Person import Person
import flet as ft   
def PersonView(person: Person, on_edit):
    return ft.Container(
        content=ft.Column([
            ft.Row([
                ft.Icon(ft.icons.ACCOUNT_CIRCLE, size=50, color=ft.colors.BLUE),
                ft.Column([
                    # ft.Text(f"ID: {person.id}", size=16, color=ft.colors.GREY_700),
                    ft.Text(person.username, size=24, weight=ft.FontWeight.BOLD),
                ]),
            ], alignment=ft.MainAxisAlignment.START),
            ft.Container(height=10),
            ft.ElevatedButton(
                "Editar perfil",
                icon=ft.icons.EDIT,
                on_click=lambda _: on_edit(person),
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=8),
                )
            )
        ]),
        padding=20,
        margin=20,
        border_radius=10,
        border=ft.border.all(1, ft.colors.GREY_300),
    )