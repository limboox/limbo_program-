import flet as ft

def main(page: ft.Page):
    def login_clicked(e):
        if username.value == "admin" and password.value == "1234":
            show_admin()
        elif username.value == "user" and password.value == "9876":
            show_user()
        else:
            page.snack_bar = ft.SnackBar(
                ft.Text("Usuario o contraseña incorrectos"), bgcolor="red"
            )
            page.snack_bar.open = True
            page.update()

    def show_admin():
        page.controls.clear()
        page.add(
            ft.Column(
                [
                    ft.Text("Bienvenido, Admin 👑", size=25),
                    ft.ElevatedButton("Cerrar sesión", on_click=lambda e: show_login())
                ],
                alignment="center",
                horizontal_alignment="center"
            )
        )
        page.update()

    def show_user():
        page.controls.clear()
        page.add(
            ft.Column(
                [
                    ft.Text("Bienvenido, Usuario 🙋", size=25),
                    ft.ElevatedButton("Cerrar sesión", on_click=lambda e: show_login())
                ],
                alignment="center",
                horizontal_alignment="center"
            )
        )
        page.update()

    def show_login():
        page.controls.clear()
        page.add(
            ft.Column(
                [
                    ft.Text("Login", size=30, weight="bold"),
                    username,
                    password,
                    login_btn
                ],
                alignment="center",
                horizontal_alignment="center"
            )
        )
        page.update()

    username = ft.TextField(label="Usuario")
    password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)
    login_btn = ft.ElevatedButton("Iniciar sesión", on_click=login_clicked)

    # inicia mostrando login
    show_login()

ft.app(target=main)
