import flet as ft
from inicio_sesion import LoginView

def main(page: ft.Page):
    page.title = "Sistema de Horarios"
    page.window_width = 800
    page.window_height = 600
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    def cambiar_vista(vista):
        page.clean()
        page.add(vista)
        page.update()

    login = LoginView(page, cambiar_vista)
    cambiar_vista(login)

ft.app(target=main)
