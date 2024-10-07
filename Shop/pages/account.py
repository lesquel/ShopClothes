import flet as ft
from backend.model import person as PS 
from Shop.components.account.perfil import PersonView
from Shop.components.account.edit_person_dialog import EditPersonDialog 

def AccountPage(page: ft.Page):
    # Ejemplo de persona
    person = PS.Costumer("usuario_ejemplo", "contraseña123")

    def edit_person(p):
        def save_changes(new_username, new_password):
            # Utilizamos los setters para actualizar los datos de la persona
            person.username = new_username
            person.password = new_password
            
            # Actualizamos la vista
            person_view.content.controls[0].controls[1].controls[1].value = new_username
            dlg.open = False
            page.update()

        dlg = EditPersonDialog(p, save_changes, page)
        page.dialog = dlg
        dlg.open = True
        page.update()

    person_view = PersonView(person, edit_person)

    page.add(
        ft.SafeArea(
            ft.Column([
                ft.Container(
                    content=ft.Text("Mi cuenta", size=32, weight=ft.FontWeight.BOLD),
                    margin=ft.margin.only(left=20, top=20, bottom=10)
                ),
                person_view,
            ], spacing=0)
        )
    )

    page.update()